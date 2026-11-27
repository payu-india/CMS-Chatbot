---
title: Pre-Auth UPI Intent - Merchant Hosted
deprecated: false
hidden: true
metadata:
  robots: index
---
In Merchant Hosted UPI Intent integration, PayU returns a mandate URI (`intentURIData`), allowing your native mobile app or web app to launch installed UPI apps directly.

***

## Step 1: Post UPI Intent Pre-Auth Request

### Environment

| Environment        | URL                                                                                                   |
| :----------------- | :---------------------------------------------------------------------------------------------------- |
| **Test (Sandbox)** | [https://test.payu.in/\_payment](https://test.payu.in/_payment)                                       |
| **Production**     | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment "https://secure.payu.in/_payment") |

<Tabs>
  <Tab title="Request Parameters">
    **Environment**

    |                            |                                                                         |
    | :------------------------- | :---------------------------------------------------------------------- |
    | **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
    | **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

    The **pre_authorize** parameter as specified is used to pre-authorize payments using the Merchant Hosted Checkout integration with the **\_payment** API.

    **Mandatory Parameters**

    | Parameter                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Example                                   |
    | :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------- |
    | <Glossary>key</Glossary> `mandatory`          | `varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Your Test Key                             |
    | <Glossary>txnid</Glossary> `mandatory`        | `varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction. Character limit: 25 Note: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.' | fd3e847h2                                 |
    | amount `mandatory`                            | `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | 1000                                      |
    | <Glossary>productinfo</Glossary> `mandatory`  | `varchar` This parameter should contain a brief product description. It should be a string describing the product. Character limit: 100                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Time Magazine Subscription                |
    | firstname `mandatory`                         | `varchar` Must contain the first name of the customer. Character limit: 60                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Ashish                                    |
    | email `mandatory`                             | `varchar` Must contain the email of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information. Also, <Glossary>MIS</Glossary> reporting is shared with few issuing banks where email and mobile number is used to keep track of users using <Glossary>SI</Glossary> transactions. Character limit: 50                                                                                                                                                                                                                            | [Ashish@test.com](mailto:Ashish@test.com) |
    | phone `mandatory`                             | `varchar` Must contain the phone number of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is required to provide the correct information. Character limit: 50                                                                                                                                                                                                                                                                                                                                                                                                      | 9876543210                                |
    | <Glossary>surl</Glossary> `mandatory`         | surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |                                           |
    | <Glossary>furl</Glossary> `mandatory`         | furl is the acronym for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |                                           |
    | <Glossary>pg</Glossary> `mandatory`           | It defines the payment category for which you wish to perform UPI One-Time Mandate integration. For UPI, pg = UPI                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | UPI                                       |
    | <Glossary>bankcode</Glossary> `mandatory`     | It defines the bank with which you wish to perform <Glossary>UPI Intent</Glossary> One-Time Mandate integration using the bank code. For UPI Intent, use INTENT.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | UPI                                       |
    | <Glossary>txn_s2s_flow</Glossary> `mandatory` | This parameter must be passed with the values as 4 for UPI Intent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                           |
    | pre_authorize `mandatory for Pre-Auth`        | This parameter is set to 1 to <Glossary>Pre-authorization</Glossary> payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 1                                         |
    | <Glossary>hash</Glossary> `mandatory`         | Hash is a crucial parameter used to ensure that any data is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions. It is <Glossary>SHA-512</Glossary> hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant <Glossary>Salt</Glossary>. In the case of registration transaction, the formula used to calculate this hash is similar to the following: <br />`key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)`                           | txnid                                     |

    **Optional Parameters**

    | Parameter  | Description                                                                                                                                                                  | Example                                                         |
    | :--------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------- |
    | si_details | This parameter contains the following information in JSON format: paymentStartDate, paymentEndDate. Example: {"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"} | {"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"} |
  </Tab>

  <Tab title="Sample Request">
    ```curl
    curl --request POST \
    --url https://test.payu.in/_payment \
    --header 'accept: text/plain' \
    --header 'content-type: application/x-www-form-urlencoded' \
    --data key=JPM7Fg \
    --data pg=UPI \
    --data bankcode=INTENT \
    --data txn_s2s_flow=4 \
    --data txnid=aso6787 \
    --data siDetails='{"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}' \
    --data pre_authorize=1 \
    --data amount=100.00 \
    --data productinfo=iPhone \
    --data firstname=Ashish \
    --data email=ashish@abc.com \
    --data phone=9876543210 \
    --data surl=https://apiplayground-response.herokuapp.com/ \
    --data furl=https://apiplayground-response.herokuapp.com/ \
    --data hash=8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b
    ```
    ```python
    import requests
    url = "https://test.payu.in/_payment"
    headers = {"accept": "text/plain", "content-type": "application/x-www-form-urlencoded"}
    data = {
        "key": "JPM7Fg", "pg": "UPI", "bankcode": "INTENT",     "txn_s2s_flow": "4", "txnid": "aso6787",
        "siDetails": '{"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}',
        "pre_authorize": "1", "amount": "100.00", "productinfo": "iPhone",
        "firstname": "Ashish", "email": "ashish@abc.com", "phone": "9876543210",
        "surl": "https://apiplayground-response.herokuapp.com/",
        "furl": "https://apiplayground-response.herokuapp.com/",
        "hash": "8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b"
    }
    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    print(response.text)
    ```
    ```javascript
    const params = new URLSearchParams({
        key: "JPM7Fg", pg: "UPI", bankcode: "UPI", vpa: "anything@payu",
        txn_s2s_flow: "4", txnid: "aso6787",
        siDetails: '{"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}',
        pre_authorize: "1", amount: "100.00", productinfo: "iPhone",
        firstname: "Ashish", email: "ashish@abc.com", phone: "9876543210",
        surl: "https://apiplayground-response.herokuapp.com/",
        furl: "https://apiplayground-response.herokuapp.com/",
        hash: "8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b"
    });
    const response = await fetch("https://test.payu.in/_payment", {
        method: "POST",
        headers: {"accept": "text/plain", "content-type": "application/x-www-form-urlencoded"},
        body: params.toString()
    });
    console.log(response.status);
    console.log(await response.text());
    ```
    ```php
    <?php
    $data = http_build_query(["key" => "JPM7Fg", "pg" => "UPI", "bankcode" => "INTENT",
        "vpa" => "anything@payu", "txn_s2s_flow" => "4", "txnid" => "aso6787",
        "siDetails" => '{"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}',
        "pre_authorize" => "1", "amount" => "100.00", "productinfo" => "iPhone",
        "firstname" => "Ashish", "email" => "ashish@abc.com", "phone" => "9876543210",
        "surl" => "https://apiplayground-response.herokuapp.com/",
        "furl" => "https://apiplayground-response.herokuapp.com/",
        "hash" => "8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b"]);
    $ch = curl_init();
    curl_setopt_array($ch, [CURLOPT_URL => "https://test.payu.in/_payment", CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $data, CURLOPT_RETURNTRANSFER => true,
        CURLOPT_HTTPHEADER => ["accept: text/plain","content-type: application/x-www-form-urlencoded"]]);
    echo curl_getinfo($ch, CURLINFO_HTTP_CODE) . "\n"; echo curl_exec($ch); curl_close($ch);
    ?>
    ```
    ```java
    import java.net.URI; import java.net.http.*;
    public class IntentStep1 {
        public static void main(String[] args) throws Exception {
            String f = "key=JPM7Fg&pg=UPI&bankcode=INTENT&txn_s2s_flow=4&txnid=aso6787"
                + "&siDetails=%7B%22paymentStartDate%22%3A%222019-09-01%22%7D&pre_authorize=1"
                + "&amount=100.00&productinfo=iPhone&firstname=Ashish&email=ashish%40abc.com&phone=9876543210"
                + "&surl=https%3A%2F%2Fapiplayground-response.herokuapp.com%2F"
                + "&furl=https%3A%2F%2Fapiplayground-response.herokuapp.com%2F"
                + "&hash=8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b";
            var req = HttpRequest.newBuilder().uri(URI.create("https://test.payu.in/_payment"))
                .header("accept","text/plain").header("content-type","application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(f)).build();
            var res = HttpClient.newHttpClient().send(req, HttpResponse.BodyHandlers.ofString());
            System.out.println(res.statusCode()); System.out.println(res.body());
        }
    }
    ```
    ```csharp
    using System.Collections.Generic; using System.Net.Http; using System.Threading.Tasks;
    class IntentStep1 {
        static async Task Main() {
            var c = new HttpClient(); c.DefaultRequestHeaders.Add("accept","text/plain");
            var f = new FormUrlEncodedContent(new Dictionary<string,string>{
                {"key","JPM7Fg"},{"pg","UPI"},{"bankcode","INTENT"},{            {"txn_s2s_flow","4"},{"txnid","aso6787"},
                {"siDetails","{\"paymentStartDate\":\"2019-09-01\",\"paymentEndDate\":\"2019-12-01\"}"},
                {"pre_authorize","1"},{"amount","100.00"},{"productinfo","iPhone"},
                {"firstname","Ashish"},{"email","ashish@abc.com"},{"phone","9876543210"},
                {"surl","https://apiplayground-response.herokuapp.com/"},
                {"furl","https://apiplayground-response.herokuapp.com/"},
                {"hash","8e8de8a3cf2ba999e16c0ffdb63a645074af4ad1aa0a8d66d81555a119c004e1791173fe6199084f256623664b250d3aeb50fc2c4cfc155e729d8811a157c98b"}});
            var r = await c.PostAsync("https://test.payu.in/_payment",f);
            System.Console.WriteLine((int)r.StatusCode); System.Console.WriteLine(await r.Content.ReadAsStringAsync());
        }
    }
    ```
  </Tab>
</Tabs>

***

## Step 2: Parse `intentURIData` and Trigger App Switch

PayU returns a JSON response containing `intentURIData`:

```json
{
  "metaData": {
    "referenceId": "test123",
    "txnId": "UPI_SEAM_INT_1",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "99999999",
    "amount": "1000.00",
    "intentURIData": "upi://mandate?pa=abc@upi&pn=Merchant&mn=ONETIME&tid=test123&validitystart=20112026&validityend=20122026&am=1000.00&amrule=MAX&recur=ONETIME&tr=UPI_SEAM_INT_1&cu=INR&mode=13&block=Y&txnType=CREATE"
  }
}
```

Open the `intentURIData` URI in your mobile application to invoke the customer's UPI app. Upon PIN entry, PayU sends the confirmation callback to your `surl` and webhook.

***

## Step 3 & 4: Capture or Cancel

Execute fund capture or mandate cancellation via `postservice.php`.