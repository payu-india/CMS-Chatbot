---
title: 'Tutorial: Android Checkout SDK'
deprecated: false
hidden: true
metadata:
  robots: index
---
Here's the code, split into the builder app, the storefront/server side, and the Android side.

1. Builder app (this project)

| File                           | Role                                                                          |
| ------------------------------ | ----------------------------------------------------------------------------- |
| `src/routes/index.tsx`         | 4-step wizard UI (category → layout → brand → export)                         |
| `src/routes/payu-checkout.tsx` | PayU Checkout Pro integration guide page                                      |
| `src/lib/builder-data.ts`      | 6 categories, sample products, 5 layouts, 5 palettes, `StoreConfig`           |
| `src/lib/site-generator.ts`    | Emits the storefront HTML/CSS/JS/SVG files                                    |
| `src/lib/android-generator.ts` | Emits the Kotlin/Gradle Android project                                       |
| `src/lib/download-bundle.ts`   | Merges both, copies site into `android/app/src/main/assets/`, zips with JSZip |

2. Storefront checkout (generated `js/payu-checkout.js`)

```js
var order = {
  amount: t.total.toFixed(2), productinfo: STORE + " order",
  firstname: form.firstname.value.trim(), email: form.email.value.trim(),
  phone: form.phone.value.trim(), udf1: form.address.value.trim(), udf2: form.city.value.trim()
};

// Inside the Android app, hand the order to PayU Checkout Pro SDK instead.
if (typeof AndroidBridge !== "undefined" && AndroidBridge.pay) {
  AndroidBridge.pay(JSON.stringify(order));
  return;
}

// Web: server signs the request, then POST to PayU's test endpoint
var signed = await (await fetch(HASH_ENDPOINT, {
  method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(order)
})).json();                            // { key, txnid, hash }
var f = document.createElement("form");
f.method = "POST"; f.action = PAYU_ACTION;  // https://test.payu.in/_payment
// ...append order + key/txnid/hash/surl/furl and submit
```

3. Server side — the only thing that touches the salt

```js
// POST /api/payu/hash   body: { hashString }
import crypto from "node:crypto";

app.post("/api/payu/hash", (req, res) => {
  const { hashString } = req.body;
  if (typeof hashString !== "string" || hashString.length > 1000) {
    return res.status(400).json({ error: "bad hashString" });
  }
  const hash = crypto.createHash("sha512")
    .update(hashString + process.env.PAYU_SALT)
    .digest("hex");
  res.json({ hash });
});
```

Sandbox pair: key `gtKFFx`, salt `eCwWELxi`. The web flow uses the same endpoint shape, returning `{ key, txnid, hash }` for the full `key|txnid|amount|productinfo|firstname|email|udf1..udf5||||||salt` string.

4. Android — `MainActivity.kt` (WebView + JS bridge)

```kotlin
class MainActivity : AppCompatActivity() {
    private val storeUrl = "file:///android_asset/index.html"
    private lateinit var webView: WebView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        webView = WebView(this); setContentView(webView)
        webView.settings.javaScriptEnabled = true
        webView.settings.domStorageEnabled = true
        webView.webViewClient = WebViewClient()
        webView.addJavascriptInterface(Bridge(), "AndroidBridge")
        webView.loadUrl(storeUrl)
    }

    inner class Bridge {
        @JavascriptInterface
        fun pay(orderJson: String) {
            val o = JSONObject(orderJson)
            val order = PayUOrder(
                amount = o.optString("amount", "1.00"),
                productInfo = o.optString("productinfo", "Order"),
                firstName = o.optString("firstname", "Customer"),
                email = o.optString("email", "test@example.com"),
                phone = o.optString("phone", "9999999999")
            )
            runOnUiThread {
                PayUCheckout(this@MainActivity).start(order) { result ->
                    when (result) {
                        is PaymentResult.Success -> webView.loadUrl("file:///android_asset/payment-success.html")
                        is PaymentResult.Failure -> webView.loadUrl("file:///android_asset/payment-failure.html")
                        is PaymentResult.Cancelled -> Toast.makeText(this@MainActivity, "Payment cancelled", Toast.LENGTH_SHORT).show()
                    }
                }
            }
        }
    }
}
```

5. Android — `PayUCheckout.kt` (SDK launch + hash callback)

```kotlin
class PayUCheckout(private val activity: Activity) {
    fun start(order: PayUOrder, onResult: (PaymentResult) -> Unit) {
        val txnId = "TXN" + System.currentTimeMillis()

        val params = PayUPaymentParams.Builder()
            .setAmount(order.amount)
            .setIsProduction(false)                     // TEST environment
            .setProductInfo(order.productInfo)
            .setKey(BuildConfig.PAYU_KEY)               // gtKFFx
            .setPhone(order.phone)
            .setTransactionId(txnId)
            .setFirstName(order.firstName)
            .setEmail(order.email)
            .setSurl("https://cbjs.payu.in/sdk/success")
            .setFurl("https://cbjs.payu.in/sdk/failure")
            .setUserCredential(order.userCredentials)
            .setAdditionalParams(additionalParams)
            .build()

        PayUCheckoutPro.open(activity, params, object : PayUCheckoutProListener {
            override fun onPaymentSuccess(response: Any) = onResult(PaymentResult.Success(response))
            override fun onPaymentFailure(response: Any) = onResult(PaymentResult.Failure(response))
            override fun onPaymentCancel(isTxnInitiated: Boolean) = onResult(PaymentResult.Cancelled)
            override fun onError(errorResponse: ErrorResponse) = onResult(PaymentResult.Failure(errorResponse.errorMessage))

            override fun generateHash(
                valueMap: HashMap<String, String?>,
                hashGenerationListener: PayUHashGenerationListener
            ) {
                val hashName = valueMap[PayUCheckoutProConstants.CP_HASH_NAME]
                val hashString = valueMap[PayUCheckoutProConstants.CP_HASH_STRING]
                if (hashName.isNullOrEmpty() || hashString.isNullOrEmpty()) return
                PayUHashService.fetchHash(hashString) { hash ->
                    if (hash != null) hashGenerationListener.onHashGenerated(hashMapOf(hashName to hash))
                }
            }

            override fun setWebViewProperties(webView: WebView?, bank: Any?) { }
        })
    }
}
```

6. Android — `PayUHashService.kt` (calls your server, never holds the salt)

```kotlin
object PayUHashService {
    fun fetchHash(hashString: String, onDone: (String?) -> Unit) {
        CoroutineScope(Dispatchers.IO).launch {
            val hash = runCatching { request(hashString) }.getOrNull()
            withContext(Dispatchers.Main) { onDone(hash) }
        }
    }

    private fun request(hashString: String): String? {
        val conn = (URL(BuildConfig.HASH_ENDPOINT).openConnection() as HttpURLConnection).apply {
            requestMethod = "POST"; doOutput = true
            connectTimeout = 15000; readTimeout = 15000
            setRequestProperty("Content-Type", "application/json")
        }
        OutputStreamWriter(conn.outputStream).use { it.write(JSONObject().put("hashString", hashString).toString()) }
        if (conn.responseCode != 200) return null
        return JSONObject(conn.inputStream.bufferedReader().use { it.readText() })
            .optString("hash").ifEmpty { null }
    }
}
```

Gradle side pulls `com.payu.india:payu-checkout-pro`, `payu-upi-sdk` and `payu-custom-browser`, and injects `PAYU_KEY` / `HASH_ENDPOINT` as `buildConfigField`s; the manifest adds INTERNET plus the `upi` scheme `<queries>` entry so UPI app handoff works.

Want me to also wire that `/api/payu/hash` endpoint into this project so the generated stores have a working test signer out of the box?
