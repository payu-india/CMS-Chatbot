---
title: Net Banking Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Net Banking TPV Integration - Merchant Hosted Checkout
  description: >-
    Learn how to integrate Net Banking with Third Party Validation (TPV) using
    PayU's comprehensive guide. This documentation provides step-by-step
    instructions, API details, and best practices for seamless and secure
    payment processing. Enhance your online payment solutions with efficient net
    banking integration."
  keywords:
    - Net Banking Integration for TPV
    - ' Third Party Validation Net Banking Integration'
    - API Integration for NetBanking TPV
    - ' PayU NetBanking TPV Integration'
    - TPV Net Banking Setup Guide
  robots: index
next:
  description: ''
---
---
title: Net Banking Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Net Banking TPV Integration - Merchant Hosted Checkout
  description: >-
    Learn how to integrate Net Banking with Third Party Validation (TPV) using
    PayU's comprehensive guide. This documentation provides step-by-step
    instructions, API details, and best practices for seamless and secure
    payment processing. Enhance your online payment solutions with efficient net
    banking integration."
  keywords:
    - Net Banking Integration for TPV
    - ' Third Party Validation Net Banking Integration'
    - API Integration for NetBanking TPV
    - ' PayU NetBanking TPV Integration'
    - TPV Net Banking Setup Guide
  robots: index
next:
  description: ''
---
Integrate <Glossary>TPV</Glossary> through Net Banking using the procedure described in this section.

<br />

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout** > **Net Banking** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

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
                                            font-weight: bold;
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

                                        <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-nb-tpv', '_blank')" 
                                                class="tooltip-btn" 
                                                data-tooltip="Click here to see the Merchant Hosted Checkout > Net Banking > TPV end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
                                            Experience the flow and get the code
                                        </button>
  `}</HTMLBlock>
</Callout>

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. List Account Numbers" href="#step-1-list-the-account-numbers">
    Collect account numbers and check bank network health
  </Card>
  <Card title="2. Post Parameters" href="#step-2-post-the-parameters-to-payu">
    Post transaction request with beneficiary details to PayU
  </Card>
  <Card title="3. Check Response" href="#step-3-check-the-response-from-payu">
    Validate the response and reverse hash from PayU
  </Card>
  <Card title="4. Verify Payment" href="#step-4-verify-the-payment">
    Verify the payment using verify\_payment API
  </Card>
</Cards>

**Prerequisites**: Seamless integration has to be done as per the standard kit. For more information, refer to  <a href="https://docs.payu.in/reference/_payment-merchant-hosted" target="_blank">Collect Payments API</a>  under API Reference.

***

## Step 1: List the account numbers

Collect or prepare a list of account numbers that must be posted to PayU for TPV at step 2. You can use the **Get Net Banking Status** API to check the bank network health.

<Accordion title="Sample request" icon="fa-code">
  ```
  curl -X POST "https://test.payu.in/merchant/postservice?form=2"-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&command=getNetbankingStatus&var1=AXIB&hash=11f17a5b7b3a93bd0391a0447706ebebd37ab11d8ec8aff18e7d0ca6267f44d6b0b56c4bee6a8b8998acec1491be17047d43ad3ef1b4677bf2504f48d3e779ea"
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  ```plaintext
  {
        "ibibo_code": "AXIB",
        "title": "AXIS Bank NetBanking",
        "up_status": 0,
        "mode": "NB"
  }
  ```

  To get the status of all Net Banking options pass (value "**default**" is passed in input):

  ```
  {
        "AXIB": {
              "ibibo_code": "AXIB",
              "title": "AXIS Bank NetBanking",
              "up_status": 0,
              "mode": "NB"
        },
        "SBIB": {
              "ibibo_code": "SBIB",
              "title": "State Bank of India",
              "up_status": 1,
              "mode": "NB"
        },
        "TESTPGNB": {
              "ibibo_code": "TESTPGNB",
              "title": "Test Net Banking",
              "up_status": 1,
              "mode": "NB"
        },
        "UPI": {
              "ibibo_code": "UPI",
              "title": "Test UPI",
              "up_status": 1,
              "mode": "UPI"
        },
        "CASH": {
              "ibibo_code": "CASH",
              "title": "Test Wallet",
              "up_status": 1,
              "mode": "CASH"
        }
  }
  ```
</Accordion>

## Step 2: Post the parameters to PayU

With the following additional parameters, make the transaction request with the customer's bank account number to the PayU using the Collect Payment (**_payment**) API. For more information, refer to [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted).

<PaymentAPIEnvironment />

<Tabs>
  <Tab title="Request Parameters">

**Mandatory Parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| <Glossary>key</Glossary> | `String` The merchant key provided by PayU while onboarding. | |
| <Glossary>txnid</Glossary> | `String` The transaction ID is a reference number for a specific order that is generated by the merchant. | |
| amount | `String` The payment amount for the transaction. | 10.00 |
| <Glossary>productinfo</Glossary> | `String` A brief description of the product. | iPhone |
| firstname | `String` The first name of the customer. | Ashish |
| email | `String` The email address of the customer. | abc@payu.in |
| phone | `String` The phone number of the customer. | |
| <Glossary>pg</Glossary> | `String` It defines the payment category for which you wish to perform TPV. For Net Banking, pg='NB'. | NB |
| <Glossary>bankcode</Glossary> | `String` It defines the bank with which you wish to perform TPV using the bank code. For more information on the list of bank codes, refer to [Bank Codes for TPV](doc:bank-codes-for-tpv). | AXNBTPV, SBINBTPV, ICINBTPV |
| beneficiarydetail | `String` JSON format text with a key named `beneficiaryAccountNumber` with the list of account numbers and the `ifscCode` key with the list of corresponding IFSC codes (in the same order). You can post up to five account details in this parameter. | Refer to beneficiarydetail JSON Object Fields section below the table |
| <Glossary>furl</Glossary> | `String` The success URL, which is the page PayU will redirect to if the transaction is successful. | |
| <Glossary>surl</Glossary> | `String` The Failure URL, which is the page PayU will redirect to if the transaction is failed. | |
| <Glossary>hash</Glossary> | `String` It is the hash calculated by the merchant. The hash calculation logic is: <Glossary>SHA-512</Glossary>(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|\|beneficiarydetail\|<Glossary>Salt</Glossary>) | |

**Optional Parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| api_version | The api_version "6" must be passed for this parameter. | |
| address1 | `String` The first line of the billing address. *For Fraud Detection*: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is required to provide the correct information. | |
| address2 | `String` The second line of the billing address. | |
| city | `String` The city where your customer resides as part of the billing address. | |
| state | `String` The state where your customer resides as part of the billing address. | |
| country | `String` The country where your customer resides. | |
| zipcode | `String` Billing address zip code is mandatory for the cardless EMI option. `Character Limit` - 20 | |
| udf1 | `String` <Glossary>User Defined Field</Glossary> are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. | |
| udf2 | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. You can use up to five udfs in the post designated as udf1, udf2, udf3, udf4, udf5. | |
| udf3 | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. | |
| udf4 | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. | |
| udf5 | `String` User-defined fields (udf) are used to store any information corresponding to a particular transaction. | |

<Accordion title="beneficiarydetail JSON Object Fields" icon="fa-code">
  It must contain the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter. For example:

  ```
  {"beneficiaryAccountNumber":"002001600674|00000031957292212|00000035955239352|00000035955239352",  
  "ifscCode":"KTKB0000046|KTKB0000023|KTKB0000035|KTKB0000035"}
  ```
</Accordion>

<Accordion title="Checksum logic for Hash" icon="fa-code">
  The following hash logic must be used for the parameters posted:

  > 📘 beneficiarydetail parameter in hashing:
  >
  > The **beneficiarydetail** parameter value will be at last or the last value to be appended.
  >
  > ```plaintext
  > key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3
  > |udf4|udf5||||||beneficiarydetail|SALT
  > ```
</Accordion>

  </Tab>
  <Tab title="Sample Request">

```curl
curl --request POST 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'txnid=netbanking_tpv_12345' \
  --data-urlencode 'amount=10.00' \
  --data-urlencode 'productinfo=iPhone' \
  --data-urlencode 'firstname=Ashish' \
  --data-urlencode 'email=test@payu.in' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'pg=NB' \
  --data-urlencode 'bankcode=AXNBTPV' \
  --data-urlencode 'beneficiarydetail={"beneficiaryAccountNumber":"002001600674","ifscCode":"KTKB0000046"}' \
  --data-urlencode 'surl=https://example.com/payment/success' \
  --data-urlencode 'furl=https://example.com/payment/failure' \
  --data-urlencode 'hash=YOUR_CALCULATED_HASH'
```
```python
import json
import requests

url = "https://test.payu.in/_payment"
data = {
    "key": "JP***g",
    "txnid": "netbanking_tpv_12345",
    "amount": "10.00",
    "productinfo": "iPhone",
    "firstname": "Ashish",
    "email": "test@payu.in",
    "phone": "9876543210",
    "pg": "NB",
    "bankcode": "AXNBTPV",
    "beneficiarydetail": json.dumps({
        "beneficiaryAccountNumber": "002001600674",
        "ifscCode": "KTKB0000046"
    }),
    "surl": "https://example.com/payment/success",
    "furl": "https://example.com/payment/failure",
    "hash": "YOUR_CALCULATED_HASH"
}
response = requests.post(url, data=data)
print(response.status_code, response.text)
```
```javascript
const params = new URLSearchParams({
  key: 'JP***g',
  txnid: 'netbanking_tpv_12345',
  amount: '10.00',
  productinfo: 'iPhone',
  firstname: 'Ashish',
  email: 'test@payu.in',
  phone: '9876543210',
  pg: 'NB',
  bankcode: 'AXNBTPV',
  beneficiarydetail: JSON.stringify({
    beneficiaryAccountNumber: '002001600674',
    ifscCode: 'KTKB0000046'
  }),
  surl: 'https://example.com/payment/success',
  furl: 'https://example.com/payment/failure',
  hash: 'YOUR_CALCULATED_HASH'
});

const response = await fetch('https://test.payu.in/_payment', {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: params
});
console.log(response.status, await response.text());
```
```java
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class NetBankingTpvPayment {
    public static void main(String[] args) throws Exception {
        Map<String, String> data = new LinkedHashMap<>();
        data.put("key", "JP***g");
        data.put("txnid", "netbanking_tpv_12345");
        data.put("amount", "10.00");
        data.put("productinfo", "iPhone");
        data.put("firstname", "Ashish");
        data.put("email", "test@payu.in");
        data.put("phone", "9876543210");
        data.put("pg", "NB");
        data.put("bankcode", "AXNBTPV");
        data.put("beneficiarydetail", "{\"beneficiaryAccountNumber\":\"002001600674\",\"ifscCode\":\"KTKB0000046\"}");
        data.put("surl", "https://example.com/payment/success");
        data.put("furl", "https://example.com/payment/failure");
        data.put("hash", "YOUR_CALCULATED_HASH");

        String body = data.entrySet().stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://test.payu.in/_payment"))
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(body))
            .build();
        HttpResponse<String> response = HttpClient.newHttpClient()
            .send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.statusCode() + " " + response.body());
    }
}
```
```php
<?php
$data = [
    'key' => 'JP***g',
    'txnid' => 'netbanking_tpv_12345',
    'amount' => '10.00',
    'productinfo' => 'iPhone',
    'firstname' => 'Ashish',
    'email' => 'test@payu.in',
    'phone' => '9876543210',
    'pg' => 'NB',
    'bankcode' => 'AXNBTPV',
    'beneficiarydetail' => json_encode([
        'beneficiaryAccountNumber' => '002001600674',
        'ifscCode' => 'KTKB0000046'
    ]),
    'surl' => 'https://example.com/payment/success',
    'furl' => 'https://example.com/payment/failure',
    'hash' => 'YOUR_CALCULATED_HASH'
];
$ch = curl_init('https://test.payu.in/_payment');
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => http_build_query($data),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => ['Content-Type: application/x-www-form-urlencoded']
]);
$response = curl_exec($ch);
echo curl_getinfo($ch, CURLINFO_HTTP_CODE) . ' ' . $response;
curl_close($ch);
?>
```

  </Tab>
</Tabs>

## Step 3: Check the response from PayU

<Accordion title="Hash Validation Logic for Payment Response (Reverse Hashing)" icon="fa-code">
  While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

  The order of the parameters is similar to the following:

  ```
  sha512(SALT|status||||||||udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  > 📘 beneficiarydetail parameter not required in reverse hashing:
  >
  > The **beneficiarydetail** parameter should not be present in reverse hashing and order of parameters is similar to the following:
  >
  > ```
  > sha512(SALT|status||||||||udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  > ```
</Accordion>

<Accordion title="Response Parameters" icon="fa-code">
  The following table describes the parameters in the response from PayU:

  | **Param Name**   | **Description**                                                                                                                                                                                                                                                                                                          |
  | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | <Glossary>mihpayid</Glossary>         | It is a unique reference number created for each transaction at PayU's end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.                                                                                                 |
  | merchantid       | It is the unique ID of the merchant.                                                                                                                                                                                                                                                                                     |
  | txnid            | This parameter would contain the transaction ID value posted by the merchant during the transaction request.                                                                                                                                                                                                             |
  | transaction\_fee | The transaction fee for the TPV transaction. For Net Banking, INR 10 is charged by default.                                                                                                                                                                                                                              |
  | discount         | The discount amount given by bank on the transaction fee (if any).                                                                                                                                                                                                                                                       |
  | amount           | The net amount after discount (if any) is displayed in this parameter. For Net Banking, INR 10 is charged by default.                                                                                                                                                                                                    |
  | paymentgatewayid | The payment gateway identifier for the bank sending the response.                                                                                                                                                                                                                                                        |
  | pg               | The payment gateway used for the transaction. In case of Net Banking, it is "NB."                                                                                                                                                                                                                                        |
  | status           | This parameter gives the status of the transaction as either success, failed or pending. Possible values: success, failure, pending. If the value of the 'status' parameter is 'success', the transaction is successful. If the value of 'status' is 'failure' or 'pending', must be treated as a failed transaction only |
  | PG\_Type         | The bankcode (as in Merchant Hosted Checkout integration) of the bank is returned in the parameter.                                                                                                                                                                                                                      |
  | key              | This parameter contains the merchant key for the merchant's account at PayU. It would be the same as the key used while the transaction request is being posted from the merchant's end to PayU.                                                                                                                         |
  | riskactionStr    | This parameter contains risk action (if any) taken on the account holder.                                                                                                                                                                                                                                                |
  | addedon          | The transaction timestamp is returned in this parameter.                                                                                                                                                                                                                                                                 |

  > 📘 Store the mihpayid and txnid parameter values in response:
  >
  > PayU recommends you to make provisions to store the **mihpayid** and **txnid** parameter values (in the response) in your server as proof that TPV has been completed for a customer.
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  Formatted response:

  ```
  Array
  (
      [mihpayid] => 403993715524308236
      [mode] => NB
      [status] => success
      [unmappedstatus] => captured
      [key] => JP***g
      [txnid] => TtEmKjWF2uGliF
      [amount] => 10.00
      [discount] => 0.00
      [net_amount_debit] => 10
      [addedon] => 2021-10-05 12:44:06
      [productinfo] => iPhone
      [firstname] => Ashish
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@gmail.com
      [phone] => 9876543210
      [udf1] => 
      [udf2] => 
      [udf3] => 
      [udf4] => 
      [udf5] => 
      [udf6] => 
      [udf7] => 
      [udf8] => 
      [udf9] => 
      [udf10] => 
      [hash] => 74d1039311528b4a7b699db7ce195d6a219d7442271dedb23e516e29490ec743a89c12448698178907e03d32fa05e8178694db8037bc0be53380099e47c3d63f
      [field1] => 
      [field2] => 
      [field3] => 
      [field4] => 
      [field5] => 
      [field6] => 
      [field7] => 
      [field8] => 
      [field9] => Transaction Completed Successfully
      [payment_source] => payu
      [PG_TYPE] => NB-PG
      [bank_ref_num] => 30646df4-69b7-43f4-acdd-21e6a593c037
      [bankcode] => TESTPGNB
      [error] => E000
      [error_Message] => No Error
  )
  ```
</Accordion>

## Step 4. Verify the payment

<Verify_Payment_Tabs />
