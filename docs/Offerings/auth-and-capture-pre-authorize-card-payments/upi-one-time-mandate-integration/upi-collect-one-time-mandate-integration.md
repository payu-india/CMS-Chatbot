---
title: UPI Collect OTM - Merchant Hosted
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
---
title: UPI Collect OTM - Merchant Hosted
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
<NPCI_Mandate />

The merchant initiates a call to PayU with the SI details, pg, bankcode, and pre-authorization amount. This amount is considered the Block Amount. Using these details, PayU will then relay the callback with the current status to the merchant.

The **pre_authorize** parameter is used for pre-authorize payments using the seamless integration with the _payment API.

<br />

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout**> **UPI** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

  <HTMLBlock>{`
                          <style>
                          .tooltip-btn { position: relative; background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }
                          .tooltip-btn:hover::after { content: attr(data-tooltip); position: absolute; bottom: 125%; left: 50%; transform: translateX(-50%); background-color: #333; color: white; padding: 5px 10px; border-radius: 4px; white-space: nowrap; font-size: 12px; z-index: 1; }
                          </style>
                          <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-otm', '_blank')" class="tooltip-btn" data-tooltip="Click here to see the Merchant Hosted Checkout > UPI end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">Experience the flow and get the code</button>
  `}</HTMLBlock>
</Callout>

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. Post the Pre-Auth Transaction Request" href="s#step-1-post-the-pre-auth-transaction-request">
    Submit the pre-authorization transaction request to PayU for payment hold
    <br />
  </Card>
  <Card title="2. Check the Response from PayU" href="#step-2-check-the-response-from-payu">
    Handle and process the response received from PayU after pre-auth request submission
    <br />
  </Card>
  <Card title="3. Capture a Pre-Authorized Payment" href="#step-3-capture-a-pre-authorized-payment">
    Complete the payment capture process for the pre-authorized transaction
  </Card>
  <Card title="4. Check Transaction Status" href="#step-4-check-transaction-status">
    Verify the current status of the transaction and confirm payment completion
    <br />
  </Card>
</Cards>

## Step 1: Post the Pre-Auth transaction request

Post the additional parameters for with the Pre-Authorization using the Merchant Hosted Checkout.

<Accordion title="Hashing" icon="fa-code">
  You must hash the request parameters using the following hash logic:

  ```
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).
</Accordion>

<Tabs>
  <Tab title="Request Parameters">

**Environment**

|                            |                                                                         |
| :------------------------- | :---------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

The pre\_authorize parameter as specified is used to pre-authorize payments using the Merchant Hosted Checkout integration with the \_payment API.

**Mandatory Parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| <Glossary>key</Glossary> `mandatory` | `varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account. | Your Test Key |
| <Glossary>txnid</Glossary> `mandatory` | `varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction. `Character limit`: 25 * _Note_*: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.' | fd3e847h2 |
| amount `mandatory` | `float` This parameter should contain the payment amount of the particular transaction. * _Note_*: Type-cast the amount to float type | 1000 |
| <Glossary>productinfo</Glossary> `mandatory` | `varchar` This parameter should contain a brief product description. It should be a string describing the product. `Character limit`: 100 | Time Magazine Subscription |
| firstname `mandatory` | `varchar` Must contain the first name of the customer. `Character limit`: 60 | Ashish |
| email `mandatory` | `varchar` Must contain the email of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information. Also, <Glossary>MIS</Glossary> reporting is shared with few issuing banks where email and mobile number is used to keep track of users using <Glossary>SI</Glossary> transactions. Character limit: 50 | Ashish@test.com |
| phone `mandatory` | `varchar` Must contain the phone number of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. Character limit: 50 | 9843176540 |
| <Glossary>surl</Glossary> `mandatory` | surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful. |  |
| <Glossary>furl</Glossary> `mandatory` | furl is the acronym for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed. |  |
| <Glossary>pg</Glossary> `mandatory` | It defines the payment category for which you wish to perform UPI One-Time Mandate integration. For UPI, **pg= UPI** | UPI |
| <Glossary>bankcode</Glossary> `mandatory` | It defines the bank with which you wish to perform UPI Collect One-Time Mandate integration using the bank code. For UPI Collect, use **UPI**. | UPI |
| <Glossary>vpa</Glossary> `mandatory for Collect flow` | This parameter contains the customer's VPA handle. For the list UPI handles supported, refer to UPI Handles. The merchant is advised to check the validity of the VPA through using the VPA Validation API. PayU extends support for the same if required. For more information on using VPA Validation API, refer to [Validate VPA API](ref:validate_vpa_api). | anything@payu |
| <Glossary>txn_s2s_flow</Glossary> `mandatory` | This parameter must be passed with the values as **4** for UPI Intent. | 4 |
| pre_authorize `mandatory for Pre-Auth` | This parameter is set to **1** to <Glossary>Pre-authorization</Glossary> payment. | 1 |
| <Glossary>hash</Glossary> `mandatory` | Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions. It is <Glossary>SHA-512</Glossary> hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant <Glossary>Salt</Glossary>. In the case of registration transaction, the formula is used to calculate this hash is similar to the following: `HASH = sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)` |  |

**Optional Parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| si_details | This parameter contains the following information in JSON format: * paymentStartDate * paymentEndDate **Example**: {"paymentStartDate":"2024-07-24","paymentEndDate":"2024-07-28"} |  |

  </Tab>

  <Tab title="Sample Request">

```curl
curl --request POST \
--url https://test.payu.in/_payment \
--header 'accept: text/plain' \
--header 'content-type: application/x-www-form-urlencoded' \
--data key=JPM7Fg \
--data pg=UPI \
--data bankcode=UPI \
--data vpa=anything@payu \
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
    "key": "JPM7Fg", "pg": "UPI", "bankcode": "UPI", "vpa": "anything@payu",
    "txn_s2s_flow": "4", "txnid": "aso6787",
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
$data = http_build_query(["key" => "JPM7Fg", "pg" => "UPI", "bankcode" => "UPI",
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
public class CollectStep1 {
    public static void main(String[] args) throws Exception {
        String f = "key=JPM7Fg&pg=UPI&bankcode=UPI&vpa=anything%40payu&txn_s2s_flow=4&txnid=aso6787"
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
class CollectStep1 {
    static async Task Main() {
        var c = new HttpClient(); c.DefaultRequestHeaders.Add("accept","text/plain");
        var f = new FormUrlEncodedContent(new Dictionary<string,string>{
            {"key","JPM7Fg"},{"pg","UPI"},{"bankcode","UPI"},{"vpa","anything@payu"},
            {"txn_s2s_flow","4"},{"txnid","aso6787"},
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

## Step 2: Check the response from PayU

<Accordion title="Success scenario" icon="fa-code">
  ```curl
  {
     "metaData":{
        "message":null,
        "referenceId":"c5161bae370de1bd4fb886c6c66567a8",
        "statusCode":null,
        "txnId":"a7440cc636e747b635df",
        "txnStatus":"pending",
        "unmappedStatus":"pending"
     },
     "result":{
        "postToBank":{"useMethodGet":true},
        "issuerUrl":"https://api.payu.in/public/#/c5161bae370de1bd4fb886c6c66567a8/upiLoader"
     }
  }
  ```
</Accordion>

<Accordion title="Failure scenarios" icon="fa-code">
  ```
  {
     "metaData":{
        "message":"Transaction failed due to invalid params shared by the merchant",
        "referenceId":"dde7096af9db932a9fd09b9b4383d8be",
        "statusCode":"E1101",
        "txnId":"0c4931ddee7a4f69227f",
        "txnStatus":"failed",
        "unmappedStatus":"failure"
     },
     "result":{}
  }
  ```
</Accordion>

## Step 3: Capture a pre-authorized payment

To capture a pre-authorized payment, use the following command. After the API command is successful, the transaction would be captured and settled to you.

<Tabs>
  <Tab title="Request Parameters">

**Mandatory Parameters**

| Parameter | Description |
| :--- | :--- |
| <Glossary>key</Glossary> `mandatory` | This parameter is the unique Merchant Key provided by PayU for your merchant account. The Merchant Key acts as the unique identifier (primary key) to identify a Merchant Account in our database. Sample value - YbfVda |
| <Glossary>command</Glossary> `mandatory` | For initiating a capture transaction, the value of the parameter will be passed as - capture_transaction |
| <Glossary>hash</Glossary> `mandatory` | This parameter must contain the hash value to be calculated at merchant end. Hash logic for this API is: sha512(key|command|var1|<Glossary>Salt</Glossary>) |
| var1 `mandatory` | This parameter must contain the payuId that was generated by PayU as part of <Glossary>Pre-authorization</Glossary> operation. |
| var2 `mandatory` | This parameter contains the token, that is, merchant unique reference number. |
| var3 `mandatory` | This parameter must contain the amount to be captured. |

  </Tab>

  <Tab title="Sample Request">

```curl
curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--form 'key="JF***g"' \
--form 'command="capture_transaction"' \
--form 'hash="67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019"' \
--form 'var1="15246574846"' \
--form 'var2="authorizeTransaction123"' \
--form 'var3="1"'
```
```python
import requests
url = "https://info.payu.in/merchant/postservice.php?form=2"
files = {"key": (None,"JF***g"), "command": (None,"capture_transaction"),
    "hash": (None,"67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019"),
    "var1": (None,"15246574846"), "var2": (None,"authorizeTransaction123"), "var3": (None,"1")}
response = requests.post(url, files=files)
print(response.status_code)
print(response.text)
```
```javascript
const formData = new FormData();
formData.append("key","JF***g"); formData.append("command","capture_transaction");
formData.append("hash","67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019");
formData.append("var1","15246574846"); formData.append("var2","authorizeTransaction123"); formData.append("var3","1");
const response = await fetch("https://info.payu.in/merchant/postservice.php?form=2",{method:"POST",body:formData});
console.log(response.status); console.log(await response.text());
```
```php
<?php
$ch = curl_init();
curl_setopt_array($ch, [CURLOPT_URL => "https://info.payu.in/merchant/postservice.php?form=2",
    CURLOPT_POST => true, CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POSTFIELDS => ["key"=>"JF***g","command"=>"capture_transaction",
        "hash"=>"67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019",
        "var1"=>"15246574846","var2"=>"authorizeTransaction123","var3"=>"1"]]);
echo curl_getinfo($ch, CURLINFO_HTTP_CODE)."\n"; echo curl_exec($ch); curl_close($ch);
?>
```
```java
import java.net.URI; import java.net.http.*; import java.nio.charset.StandardCharsets; import java.util.UUID;
public class CaptureStep3 {
    public static void main(String[] args) throws Exception {
        String b = UUID.randomUUID().toString();
        String body = "--"+b+"\r\nContent-Disposition: form-data; name=\"key\"\r\n\r\nJF***g\r\n"
            +"--"+b+"\r\nContent-Disposition: form-data; name=\"command\"\r\n\r\ncapture_transaction\r\n"
            +"--"+b+"\r\nContent-Disposition: form-data; name=\"hash\"\r\n\r\n67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019\r\n"
            +"--"+b+"\r\nContent-Disposition: form-data; name=\"var1\"\r\n\r\n15246574846\r\n"
            +"--"+b+"\r\nContent-Disposition: form-data; name=\"var2\"\r\n\r\nauthorizeTransaction123\r\n"
            +"--"+b+"\r\nContent-Disposition: form-data; name=\"var3\"\r\n\r\n1\r\n--"+b+"--";
        var req = HttpRequest.newBuilder().uri(URI.create("https://info.payu.in/merchant/postservice.php?form=2"))
            .header("Content-Type","multipart/form-data; boundary="+b)
            .POST(HttpRequest.BodyPublishers.ofString(body,StandardCharsets.UTF_8)).build();
        var res = HttpClient.newHttpClient().send(req,HttpResponse.BodyHandlers.ofString());
        System.out.println(res.statusCode()); System.out.println(res.body());
    }
}
```
```csharp
using System.Net.Http; using System.Threading.Tasks;
class CaptureStep3 {
    static async Task Main() {
        var c = new HttpClient();
        var f = new MultipartFormDataContent();
        f.Add(new StringContent("JF***g"),"key"); f.Add(new StringContent("capture_transaction"),"command");
        f.Add(new StringContent("67411736ab98c59522492a12751a6015c41b87764019f9dc14052690c2c7af9095d31002fc109dcf3596c2f38792d56db6f6207b1989010f2adf51c144fa3019"),"hash");
        f.Add(new StringContent("15246574846"),"var1"); f.Add(new StringContent("authorizeTransaction123"),"var2"); f.Add(new StringContent("1"),"var3");
        var r = await c.PostAsync("https://info.payu.in/merchant/postservice.php?form=2",f);
        System.Console.WriteLine((int)r.StatusCode); System.Console.WriteLine(await r.Content.ReadAsStringAsync());
    }
}
```

  </Tab>
</Tabs>

<Accordion title="Sample response" icon="fa-code">
  ```
  {
    "msg": "Transaction Processed successfully",
    "status": 1,
    "result": {
      "payuid": 613345678912399031,
      "txnId": "upiAuthCapture_12",
      "amount": 10000.00,
      "merchantId": 3,
      "authpayuid": "3975",
      "status": "in progress",
      "mode": "UPIOTM",
      "bankRefNumber": "410700457030",
      "payerVpa": "surya@icici",
      "field5": "3159219e58ed45eda39e8914b998401a@icici",
      "field9": "0|Transaction Successful"
    }
  }
  ```
</Accordion>

## Step 4: Check Transaction Status

<Verify_Payment_Tabs />

<br />

<Callout icon="👍" theme="okay">
  **Reference**: For cancelling pre-auth payments, refer to [Cancel a Pre-Authorized Transaction API](ref:cancel-a-pre-authorized-transaction).
</Callout>