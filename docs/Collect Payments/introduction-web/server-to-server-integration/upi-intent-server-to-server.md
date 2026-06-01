---
title: UPI Intent with S2S Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section includes the workflow and steps to integrate UPI Intent with Server-to-Server integration.

<NPCI_Mandate />

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout** > **UPI** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

  <HTMLBlock>{`
                            <style>
                            .tooltip-btn {
                                position: relative;
                                background-color: #4CAF50;
                                color: white;
                                padding: 10px 20px;
                                border: none;
                                border-radius: 5px;
                                cursor: pointer;
                                font-weight: bold; /* Added this line */
                            }
                            .tooltip-btn:hover::after {
                                content: attr(data-tooltip);
                                position: absolute;
                                bottom: 125%;
                                left: 50%;
                                transform: translateX(-50%);
                                background-color: #333;
                                color: white;
                                padding: 5px 10px;
                                border-radius: 4px;
                                white-space: nowrap;
                                font-size: 12px;
                                z-index: 1;
                            }
                            </style>

                            <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-upiflow', '_blank')" 
                                    class="tooltip-btn" 
                                    data-tooltip="Click here to see the Merchant Hosted Checkout >  UPI end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                                Experience the flow and get the code
                            </button>
  `}</HTMLBlock>
</Callout>

## Smart Intent Flow

### Workflow

<Image align="center" src="https://files.readme.io/991937481c8ab71eeb4f5f1477eb18e5bac248eb65d8ea924ed51705b520bb6f-UPI_One_time_Intent_-_Android_App_Non_SDK_Solution.png" />

### Steps to integrate

<Accordion title="Update Manifest File [One-Time]" icon="fa-code">
  Add package ids in your apps manifest file to allow your application to access apps installed on the customer's device. This is required for Android 11 and above.

  ```
   <queries>
          <package android:name="in.amazon.mShop.android.shopping"/>
          <package android:name="com.upi.axispay"/>
          <package android:name="com.axis.mobile"/>
          <package android:name="com.fisglobal.bandhanupi.app"/>
          <package android:name="com.bankofbaroda.upi"/>
          <package android:name="in.org.npci.upiapp"/>
          <package android:name="com.canarabank.mobility"/>
          <package android:name="com.citiuat"/>
          <package android:name="com.dbs.in.digitalbank"/>
          <package android:name="com.olive.dcb.upi"/>
          <package android:name="com.finopaytech.bpayfino"/>
          <package android:name="com.freecharge.android"/>
          <package android:name="com.google.android.apps.nbu.paisa.user"/>
          <package android:name="com.snapwork.hdfc"/>
          <package android:name="com.mgs.hsbcupi"/>
          <package android:name="com.csam.icici.bank.imobile"/>
          <package android:name="com.icicibank.pockets"/>
          <package android:name="com.euronet.iobupi"/>
          <package android:name="com.mgs.induspsp"/>
          <package android:name="com.fss.jnkpsp"/>
          <package android:name="com.jio.myjio"/>
          <package android:name="com.mycompany.kvb"/>
          <package android:name="com.kvb.mobilebanking"/>
          <package android:name="com.lcode.smartz"/>
          <package android:name="com.msf.kbank.mobile"/>
          <package android:name="com.upi.federalbank.org.lotza"/>
          <package android:name="com.infrasofttech.mahaupi"/>
          <package android:name="com.mipay.in.wallet"/>
          <package android:name="com.myairtelapp"/>
          <package android:name="com.mobikwik_new"/>
          <package android:name="com.onymy.paybee.prod"/>
          <package android:name="net.one97.paytm"/>
          <package android:name="com.phonepe.app"/>
          <package android:name="com.Version1"/>
          <package android:name="com.samsung.android.spay"/>
          <package android:name="com.sbi.upi"/>
          <package android:name="com.SIBMobile"/>
          <package android:name="com.truecaller"/>
          <package android:name="com.infrasoft.uboi"/>
          <package android:name="com.lcode.ucoupi"/>
          <package android:name="com.YesBank"/>
          <package android:name="com.dreamplug.androidapp"/>
          <package android:name="money.bullet"/>
      </queries>
  ```

  <br />
</Accordion>

<Accordion title="Step 1: Fetch the List of UPI and Smart Intent Supported Apps" icon="fa-code">
  List the specific apps for app/webview/m-web, (In IOS, UPI collect can still be used).
</Accordion>

<Accordion title="Step 2: Get Intent URI" icon="fa-code">
  Use the **\_payment** API to get Intent URI and transaction details for the UPI app selected by the customer. For more information, refer to <Anchor label="Collect Payment API > UPI Collection with S2S Integration" target="_blank" href="https://docs.payu.in/docs/upi-intent-server-to-server">UPI Intent with S2S Integration</Anchor>.

  <Accordion title="Request Parameters" icon="fa-table">
 | Parameter | Description | Example |
|-----------|-------------|---------|
| `key`<br/>_mandatory_ | `String` Merchant key provided by PayU during onboarding. | JPg\*\*\*\*f |
| `txnid`<br/>_mandatory_ | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. | ypl938459435 |
| `amount`<br/>_mandatory_ | `String` The payment amount for the transaction. | 10.00 |
| `productinfo`<br/>_mandatory_ | `String` A brief description of the product. | iPhone |
| `firstname`<br/>_mandatory_ | `String` The first name of the customer. | Ashish |
| `lastname`<br/>_mandatory_ | `String` The last name of the customer. | Kumar |
| `email`<br/>_mandatory_ | `String` The email address of the customer. | [abc@payu.in](mailto:abc@payu.in) |
| `phone`<br/>_mandatory_ | `String` The phone number of the customer. | |
| `address1`<br/>_optional but recommended for higher approval rate_ | `String` The first line of the billing address. H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai<br/>**Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. | 34 Saikripa-Estate, Tilak Nagar |
| `address2`<br/>_optional but recommended for higher approval rate_ | `String` The second line of the billing address. | |
| `city`<br/>_optional but recommended for higher approval rate_ | `String` The city where your customer resides as part of the billing address. | Mumbai |
| `state`<br/>_optional but recommended for higher approval rate_ | `String` The state where your customer resides as part of the billing address. | Maharashtra |
| `country`<br/>_optional but recommended for higher approval rate_ | `String` The country where your customer resides. | India |
| `zipcode`<br/>_mandatory_ | `String` Billing address zip code is mandatory for the cardless EMI option. Character Limit-20 | 400004 |
| `pg`<br/>_mandatory for seamless/s2s flow_ | `String` It defines the payment category and post **UPI**. | UPI |
| `bankcode`<br/>_mandatory for seamless/s2s flow_ | `String` Each payment option is identified with a unique bank code at PayU. For UPI Autopay, post **UPI**. | UPI |
| `surl`<br/>_mandatory_ | `String` The success URL, which is the page PayU will redirect to if the transaction is successful. | |
| `furl`<br/>_mandatory_ | `String` The Failure URL, which is the page PayU will redirect to if the transaction is failed. | |
| `vpa`<br/>_conditional_ | `String` Customer's VPA handle. Mandatory for UPI Collect flow. | `customer@upi` |
| `si`<br/>_mandatory_ | `String` Signifies successful consent taken from the user. Must be `1` for subscription setup. | `1` |
| `si_details`<br/>_mandatory_ | `JSON String` JSON object containing mandate details (billingAmount, billingCurrency, billingCycle, etc.). Refer to si\_details JSON Object below. | See si\_details accordion |
| `upiAppName`<br/>_mandatory_ | Any of the values listed under the [upiAppName list](#upiAppName-list) | amazonpay |
| `txn_s2s_flow`<br/>_conditional_ | `Integer` Parameter to enable S2S flow. Must be `4` for Legacy Decoupled flow (UPI Intent). | `4` |
| `s2s_client_ip`<br/>_conditional_ | `String` Source IP of the customer. Required for UPI Intent flow. | `10.200.12.12` |
| `s2s_device_info`<br/>_mandatory_ | `String` Real customer User-Agent on _payment for every S2S 4 txn initiated from backend. For more information, refer to [s2s\_device\_info Values Description](#s2s_device_info-values-description) table<br/>**Note**: This Required for UPI Intent flow. | Android native app |
| `udf1`<br/>_mandatory if AD bank request this detail_ | `String` This parameter must contain the Buyer's PAN and date of birth in the following format (separated by two pipe characters): Buyer's PAN\|\|Buyer'sDOB | AAAPZ1234C\|\|22/08/1972 |
| `udf3`<br/>_mandatory if AD bank request this detail_ | `String` This parameter must contain the invoice ID of the transaction (generated by the merchant) and merchant name in the following format (separated by two pipe characters): Invoice ID\|\|MerchantName | INV-123\_1231\|\|MerchantName |
| `buyer_type_business`<br/>_optional in case of B2B transaction for cross-border payments_ | `Binary` To be sent as "1" in case the buyer is a business. In case of individual buyers, it can be skipped. Default is "0".<br/>**Note**: This will be included in hash if posted (covered in next section) | 1 |

####  upiAppName eNum List
  <Accordion title="UPI App Name List" icon="fa-list">
The following are the enum's expected for UPI apps:
- phonepe
- googlepay
- paytm
- bhim
- cred
- amazonpay
- whatsapp
- adityabirla
- bajajfinserv
- bankofindiaomnineo
- bharatpe
- bhimdlbupi
- canaraai1pe
- cheq
- credilio
- curiemoney
- ebixcash
- famappbytrio
- flipkart
- freo
- gomobile
- groww
- herofincorp
- idfcmobilebankingapp
- imobilebyicicibank
- indmoney
- iris
- jar
- jiofinance
- jumpp
- jupiter
- kiwi
- kreditbee
- kreditpe
- lxme
- mobikwik
- moneyview
- mufin
- myairtel
- navi
- omnicard
- onecard
- paynearby
- pinelabsplusplay
- popclub
- pzw
- rediff
- revolut
- rio
- salaryse
- samsungpay
- scapia
- shriramone
- slice
- stashfin
- supermoney
- tataneu
- timepay
- twidpay
- yespaynext
- zet
- genericintent – For any other app apart from
above
</Accordion>
#### s2s_device_info Values Description 
| Customer environment | Example value (illustrative)                                                                                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------- |
| Android native app   | `Dalvik/2.1.0 (Linux; U; Android 13; Pixel 7 Build/...)`                                                        |
| Android Chrome       | `Mozilla/5.0 (Linux; Android 13; ...) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/... Mobile Safari/537.36`   |
| iOS in-app / WebView | `Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148` |
| iOS Safari           | `Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) ... Version/17.4 Mobile/15E148 Safari/604.1`            |

  </Accordion>

  <Accordion title="Sample Request" icon="fa-code">
    ```curl
       curl --location 'https://test.payu.in/_payment' \
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'key=PRiQvJ' \
   --data-urlencode 'txnid=my_order_991' \
   --data-urlencode 'amount=1' \
   --data-urlencode 'productinfo=my_order_991' \
   --data-urlencode 'email=' \
   --data-urlencode 'phone=9368252248' \
   --data-urlencode 'txn_s2s_flow=4' \
   --data-urlencode 'hash=||||||ABCDE1234F||1990-01-01||INV123456||||||' \
   --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
   --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
   --data-urlencode 'udf1=buyer'\''s DOB' \
   --data-urlencode 'udf2=' \
   --data-urlencode 'udf3=buyer'\''s PAN' \
   --data-urlencode 'udf4=' \
   --data-urlencode 'udf5=invoice number' \
   --data-urlencode 's2s_client_ip=10.200.12.12' \
   --data-urlencode 's2s_device_info=iOS Safari' \
   --data-urlencode 'firstname=' \
   --data-urlencode 'lastname=kr' \
   --data-urlencode 'address1=308,third floor' \
   --data-urlencode 'address2=testing' \
   --data-urlencode 'city=Gurugram' \
   --data-urlencode 'state=UP' \
   --data-urlencode 'country=India' \
   --data-urlencode 'zipcode=122018' \
   --data-urlencode 'pg=UPI' \
   --data-urlencode 'bankcode=INTENT' \
   --data-urlencode 'upiAppName=gpay' \
   --data-urlencode 'udf_params={"udf7":"asdf","udf8":"12"}' \
   --data-urlencode 'buyer_type_business=1'
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 3: Retrieve Deeplink(uriIntentData) from the response," icon="fa-code">
  If metaData.unmappedStatus = pending, then get the result.intentURIData and add the prefix upi://pay?to make it to create a fully qualified deeplink to trigger the UPI App.
<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout** flow and instantly generate the complete code for seamless, zero-coding integration into your website. Navigate to **ACS Template Decoder** under **Tools & Utilities** to generate code for decoding the ACS template in the response:

  <HTMLBlock>{`
                        <style>
                        .tooltip-btn {
                            position: relative;
                            background-color: #4CAF50;
                            color: white;
                            padding: 10px 20px;
                            border: none;
                            border-radius: 5px;
                            cursor: pointer;
                            font-weight: bold; /* Added this line */
                        }
                        .tooltip-btn:hover::after {
                            content: attr(data-tooltip);
                            position: absolute;
                            bottom: 125%;
                            left: 50%;
                            transform: translateX(-50%);
                            background-color: #333;
                            color: white;
                            padding: 5px 10px;
                            border-radius: 4px;
                            white-space: nowrap;
                            font-size: 12px;
                            z-index: 1;
                        }
                        </style>

                        <button onclick="window.open('https://payu.in/integrationlab/seamless/cards', '_blank')" 
                                class="tooltip-btn" 
                                data-tooltip="Click here to see the Merchant Hosted Checkout end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                            Experience the flow and get the code
                        </button>
  `}</HTMLBlock>
</Callout>

  ```json
  {
      "metaData": {
          "message": null,
          "referenceId": "c99a6455b3e0dc5cd7167ab8c8cc10d2fa153cb509e3f64c6cd0ed9c5b64a8c9",
          "statusCode": null,
          "txnId": "my_order_26075",
          "txnStatus": "pending",
          "unmappedStatus": "pending"
      },
      "result": {
          "paymentId": "403993715535965242",
          "merchantName": "Sudhanshu",
          "merchantVpa": "payutest@hdfcbank",
          "amount": "1.00",
          "intentURIData": "pa=payutest@hdfcbank&pn=Kumar&tr=403993715535965242&tid=PPPL403993715535965242080126220900&am=1.00&cu=INR&tn=UPIIntent",
          "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vdGVzdC5wYXl1LmluL2M5OWE2NDU1YjNlMGRjNWNkNzE2N2FiOGM4Y2MxMGQyYzgzYTk5NmFhNDhiYTk4MmZjMGQ4MTI1MGY1ODgxZjMvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0b2tlbiIgdmFsdWU9IjhERDNFRUFFLUI5NTktQzY1RS03MDczLTYzQTNGQUUxMjZGRiI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYW1vdW50IiB2YWx1ZT0iMS4wMCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0ibWlocGF5aWQiIHZhbHVlPSJjOTlhNjQ1NWIzZTBkYzVjZDcxNjdhYjhjOGNjMTBkMmZhMTUzY2I1MDllM2Y2NGM2Y2QwZWQ5YzViNjRhOGM5Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJkaXNhYmxlSW50ZW50U2VhbWxlc3NGYWlsdXJlIiB2YWx1ZT0iMCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVWcGEiIHZhbHVlPSJwYXl1dGVzdEBoZGZjYmFuayI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVOYW1lIiB2YWx1ZT0iU3VkaGFuc2h1Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJhZGRpdGlvbmFsQ2hhcmdlcyIgdmFsdWU9IjAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InRyYW5zYWN0aW9uRmVlIiB2YWx1ZT0iMS4wMCI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1sncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+",
          "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
      }
  }
  ```
</Accordion>

<Accordion title="Step 4: Set the Package Name" icon="fa-code">
  Set the packageName as per the app selected by the customer on your checkout page. and start the activity.

  ```java
  fun makePayment(packageName: String,mActivity: Activity,intentUri:String) {
        val i = Intent()
        i.setPackage(packageName)
        i.action = Intent.ACTION_VIEW
        i.data = Uri.parse("upi://pay" + intentUri)
        if (null != mActivity && !mActivity.isFinishing() && !mActivity.isDestroyed()) {
            mActivity.startActivityForResult(i, 101)
        }
    }
  ```
</Accordion>

<Accordion title="Step 5: Handle the response" icon="fa-code">
  Once the user completes the payment the UPI app will be closed, and then handle the response onActivityResult.

  ```java
  override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == 101) {
            data?.getStringExtra("Status")?.let { Log.d("result", it) }
            data?.getStringExtra("response")?.let { Log.d("response", it) }
            //get Status
            //if Status == Success
            // Call Verify Payemnt//
        }
  }
  ```
</Accordion>

<Accordion title="Step 6: Verify the payment" icon="fa-code">
  <Verify_Payment_Tabs />
</Accordion>

## Specific Intent Flow

<Callout icon="📘" theme="info">
  **Notes**: Specific Intent flow works with m-web, Webview, Android or iOS apps. As per **NPCI** mandate, **Pay by any UPI App** option must be shown by all the merchants in their app on all Android devices (app/m-web/webview), Use the generic deeplink, without specific `packageName` to trigger the Pay by any UPI app.
</Callout>

### Workflow

<Image align="center" src="https://files.readme.io/b1767cf25bf9c6ca94e7cbf0de8ef28e2518ade4919b5df5f6d6ad41537ba1fd-UPI_One_time_Intent_-_m-web_or_IOS_App.png" />

### Steps to Integrate

<Accordion title="Step 1: Fetch the List of UPI and Smart Intent Supported Apps" icon="fa-code">
  You need to get the list of UPI and smart intent supported applications installed in the device.

  ```java
  private fun getSmartIntentUPIApps(context: Context?):ArrayList<HashMap<String,String>>?{
        val upiApps = ArrayList<HashMap<String, String>>()
        if (context == null)
            return null

        val intent = Intent()
        intent.data = Uri.parse("upi://pay")
        val activityList = context.packageManager.queryIntentActivities(intent, PackageManager.MATCH_DEFAULT_ONLY)
        for (resolveInfo in activityList){
            var packageInfo: PackageInfo? = null
            try {
                packageInfo = context.packageManager
                    .getPackageInfo(resolveInfo.activityInfo.packageName, 0)
                val name =
                    context.packageManager.getApplicationLabel(packageInfo.applicationInfo) as String
              val appInfo = HashMap<String, String?>()
                appInfo["bankName"] = name ?: "NA"
                appInfo["packageName"] = packageInfo.packageName
                upiApps.add(appInfo)
            } catch (e: PackageManager.NameNotFoundException) {
                e.printStackTrace()
                return upiApps
            }
        }
        return UPI apps
    }
    /* to get icon of psp app*/
    fun getUpiAppBitmap(context: Context?, packageName: String): Bitmap? {

        var upiAppBitmap: Bitmap? = null
        if (context == null)
            return upiAppBitmap
        upiAppBitmap = context.packageManager.getApplicationIcon(packageName).toBitmap()
        return upiAppBitmap
    }

  ```

  <br />
</Accordion>

<Accordion title="Step 2: Get Intent URI" icon="fa-code">
  Use the **\_payment** API to get Intent URI and transaction details for the UPI app selected by the customer. For more information, refer to <Anchor label="Collect Payment API > UPI Collection with S2S Integration" target="_blank" href="https://docs.payu.in/docs/upi-intent-server-to-server">UPI Intent with S2S Integration</Anchor>.

  <Accordion title="Request Parameters" icon="fa-table">
    | Parameter                                                                             | Description                                                                                                                                                                                                                                                             | Example                                     |
    | ------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
    | `key`<br />`mandatory`                                                                | `String` Merchant key provided by PayU during onboarding.                                                                                                                                                                                                               | JPg\*\*\*\*f                                |
    | `txnid`<br />`mandatory`                                                              | `String` The transaction ID is a reference number for a specific order that is generated by the merchant.                                                                                                                                                               | ypl938459435                                |
    | `amount`<br />`mandatory`                                                             | `String` The payment amount for the transaction.                                                                                                                                                                                                                        | 10.00                                       |
    | `productinfo`<br />`mandatory`                                                        | `String` A brief description of the product.                                                                                                                                                                                                                            | iPhone                                      |
    | `firstname`<br />`mandatory`                                                          | `String` The first name of the customer.                                                                                                                                                                                                                                | Ashish                                      |
    | `lastname`<br />`mandatory`                                                           | `String` The last name of the customer.                                                                                                                                                                                                                                 | Kumar                                       |
    | `email`<br />`mandatory`                                                              | `String` The email address of the customer.                                                                                                                                                                                                                             | [abc@payu.in](mailto:abc@payu.in)           |
    | `phone`<br />`mandatory`                                                              | `String` The phone number of the customer.                                                                                                                                                                                                                              |                                             |
    | `address1`<br />`optional but recommended for higher approval rate`                   | `String` The first line of the billing address. H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai **Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. | 34 Saikripa-Estate, Tilak Nagar             |
    | `address2`<br />`optional but recommended for higher approval rate`                   | `String` The second line of the billing address.                                                                                                                                                                                                                        |                                             |
    | `city`<br />`optional but recommended for higher approval rate`                       | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                           | Mumbai                                      |
    | `state`<br />`optional but recommended for higher approval rate`                      | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                          | Maharashtra                                 |
    | `country`<br />`optional but recommended for higher approval rate`                    | `String` The country where your customer resides.                                                                                                                                                                                                                       | India                                       |
    | `zipcode`<br />`mandatory`                                                            | `String` Billing address zip code is mandatory for the cardless EMI option. Character Limit-20                                                                                                                                                                          | 400004                                      |
    | `pg`<br />`mandatory for seamless/s2s flow`                                           | `String` It defines the payment category and post **UPI**.                                                                                                                                                                                                              | UPI                                         |
    | `bankcode`<br />`mandatory for seamless/s2s flow`                                     | `String` Each payment option is identified with a unique bank code at PayU. For UPI Autopay, post **UPI**.                                                                                                                                                              | UPI                                         |
    | `surl`<br />`mandatory`                                                               | `String` The success URL, which is the page PayU will redirect to if the transaction is successful.                                                                                                                                                                     |                                             |
    | `furl`<br />`mandatory`                                                               | `String` The Failure URL, which is the page PayU will redirect to if the transaction is failed.                                                                                                                                                                         |                                             |
    | vpa `conditional`                                                                     | `String` Customer's VPA handle. Mandatory for UPI Collect flow.                                                                                                                                                                                                         | `customer@upi`                              |
    | si `mandatory`                                                                        | `String` Signifies successful consent taken from the user. Must be `1` for subscription setup.                                                                                                                                                                          | `1`                                         |
    | si\_details `mandatory`                                                               | `JSON String` JSON object containing mandate details (billingAmount, billingCurrency, billingCycle, etc.). Refer to si\_details JSON Object below.                                                                                                                      | See si\_details accordion                   |
    | txn\_s2s\_flow `conditional`                                                          | `Integer` Parameter to enable S2S flow. Must be `4` for Legacy Decoupled flow (UPI Intent).                                                                                                                                                                             | `4`                                         |
    | s2s\_client\_ip `conditional`                                                         | `String` Source IP of the customer. Required for UPI Intent flow.                                                                                                                                                                                                       | `10.200.12.12`                              |
    | s2s\_device\_info `conditional`                                                       | `String` Customer agent's device information. Required for UPI Intent flow.                                                                                                                                                                                             | `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` |
    | `udf1`<br />`mandatory if AD bank request this detail`                                | `String` This parameter must contain the Buyer's PAN and date of birth in the following format (separated by two pipe characters): Buyer's PAN\\\|\\\|Buyer'sDOB                                                                                                        | AAAPZ1234C\\\|\\\|22/08/1972                |
    | `udf3`<br />`mandatory if AD bank request this detail`                                | `String` This parameter must contain the invoice ID of the transaction (generated by the merchant) and merchant name in the following format (separated by two pipe characters): Invoice ID\\\|\\\|MerchantName                                                         | INV-123\_1231\\\|\\\|MerchantName           |
    | buyer\_type\_business `optional in case of B2B transaction for cross-border payments` | `Binary` To be sent as "1" in case the buyer is a business. In case of individual buyers, it can be skipped. Default is "0". **Note**: This will be included in hash if posted (covered in next section                                                                 | 1                                           |

### 

  </Accordion>

  <Accordion title="Sample Request" icon="fa-code">
    ```curl
    curl --location 'https://test.payu.in/_payment' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=PRiQvJ' \
    --data-urlencode 'txnid=my_order_991' \
    --data-urlencode 'amount=1' \
    --data-urlencode 'productinfo=my_order_991' \
    --data-urlencode 'email=' \
    --data-urlencode 'phone=9368252248' \
    --data-urlencode 'txn_s2s_flow=4' \
    --data-urlencode 'hash=||||||ABCDE1234F||1990-01-01||INV123456||||||' \
    --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'udf1=buyer'\''s DOB' \
    --data-urlencode 'udf2=' \
    --data-urlencode 'udf3=buyer'\''s PAN' \
    --data-urlencode 'udf4=' \
    --data-urlencode 'udf5=invoice number' \
    --data-urlencode 's2s_client_ip=10.200.12.12' \
    --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0' \
    --data-urlencode 'firstname=' \
    --data-urlencode 'lastname=kr' \
    --data-urlencode 'address1=308,third floor' \
    --data-urlencode 'address2=testing' \
    --data-urlencode 'city=Gurugram' \
    --data-urlencode 'state=UP' \
    --data-urlencode 'country=India' \
    --data-urlencode 'zipcode=122018' \
    --data-urlencode 'pg=UPI' \
    --data-urlencode 'bankcode=INTENT' \
    --data-urlencode 'upiAppName=gpay/phonepe/paytm/qr/amazonpay' \
    --data-urlencode 'udf_params={"udf7":"asdf","udf8":"12"}' \
    --data-urlencode 'buyer_type_business=1'
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 3: Retrieve Deeplink(uriIntentData) from the response," icon="fa-code">
  If metaData.unmappedStatus = pending, then get the result.intentURIData and add the prefix upi://pay?to make it to create a fully qualified deeplink to trigger the UPI App.

  ```json
  {
    "metaData": {
        "message": null,
        "referenceId": "c99a6455b3e0dc5cd7167ab8c8cc10d2fa153cb509e3f64c6cd0ed9c5b64a8c9",
        "statusCode": null,
        "txnId": "my_order_26075",
        "txnStatus": "pending",
        "unmappedStatus": "pending"
    },
    "result": {
        "paymentId": "403993715535965242",
        "merchantName": "Sudhanshu",
        "merchantVpa": "payutest@hdfcbank",
        "amount": "1.00",
        "intentURIData": "pa=payutest@hdfcbank&pn=Kumar&tr=403993715535965242&tid=PPPL403993715535965242080126220900&am=1.00&cu=INR&tn=UPIIntent",
        "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vdGVzdC5wYXl1LmluL2M5OWE2NDU1YjNlMGRjNWNkNzE2N2FiOGM4Y2MxMGQyYzgzYTk5NmFhNDhiYTk4MmZjMGQ4MTI1MGY1ODgxZjMvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0b2tlbiIgdmFsdWU9IjhERDNFRUFFLUI5NTktQzY1RS03MDczLTYzQTNGQUUxMjZGRiI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYW1vdW50IiB2YWx1ZT0iMS4wMCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0ibWlocGF5aWQiIHZhbHVlPSJjOTlhNjQ1NWIzZTBkYzVjZDcxNjdhYjhjOGNjMTBkMmZhMTUzY2I1MDllM2Y2NGM2Y2QwZWQ5YzViNjRhOGM5Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJkaXNhYmxlSW50ZW50U2VhbWxlc3NGYWlsdXJlIiB2YWx1ZT0iMCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVWcGEiIHZhbHVlPSJwYXl1dGVzdEBoZGZjYmFuayI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVOYW1lIiB2YWx1ZT0iU3VkaGFuc2h1Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJhZGRpdGlvbmFsQ2hhcmdlcyIgdmFsdWU9IjAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InRyYW5zYWN0aW9uRmVlIiB2YWx1ZT0iMS4wMCI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1sncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+",
        "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
    }
  }
  ```
</Accordion>

<Accordion title="Step 4: Add the prefix" icon="fa-code">
  Add the prefix as per the Android/IOS to it to create a fully qualified deeplink to trigger the UPI App.

  #### Android Specific Intent prefix

  ```
  androidPrefix="intent://pay?"
  intentUriData="pa=myntra.payu@axisbank&pn=NIMIT%20BHATIA&tr=26156866365&tid=PPPL2615686636525112512114769254fab&am=10.00&cu=INR&tn=UPIIntent"
  suffix = "#Intent;scheme=upi;package=<package name>;"
  suffixForFallback="S.browser_fallback_url=<base64decoded result.acsTemplate can be used to redirect to Payu for UPI fallback>;end"
  //use androidPrefix+intentUriData+suffix+suffixForFallback to trigger the App in specific deeplink integration
  ```

  #### IOS Specific Intent prefix (Limited availability)

  ```
  phonepe = phonepe://upi/pay? 
  paytm = paytm://upi/pay? 
  googlepay = gpay://upi/pay? 
  bhim = bhim://upi/pay?
  credpay = credpay://upi/pay?
  ```
</Accordion>

<Accordion title="Step 5: Verify the payment" icon="fa-code">
  <Verify_Payment_Tabs />
</Accordion>