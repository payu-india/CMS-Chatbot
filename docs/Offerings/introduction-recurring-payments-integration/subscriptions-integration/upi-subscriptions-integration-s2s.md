---
title: UPI Subscriptions Integration [S2S]
deprecated: false
hidden: true
metadata:
  title: UPI Subscriptions Integration for Merchant Hosted
  description: UPI subscriptions with S2S. Recurring UPI Autopay integration.
  keywords:
    - UPI subscriptions integration
    - recurring UPI merchant hosted
    - UPI Autopay integration
  robots: index
---
This section describes step-by-step procedure to implement UPI Consent Transaction (SI mandate registration) for recurring UPI payments using PayU's Server-to-Server (S2S) integration with the Legacy Decoupled flow.

## Prerequisites

Before starting the integration, ensure you have:

- Active PayU merchant account with UPI recurring payments enabled
- Merchant Key and Salt from PayU dashboard
- Test environment access for development

<Callout icon="⚠️" theme="warning">
  **Important UPI Integration Changes as per NPCI Mandate on UPI Collect Disablement**:

  - **Seamless Form Post Users**: Merchants using Seamless Form Post flow must migrate to `txn_s2s_flow` (UPI Intent S2S), as Intent is **not supported** in the seamless form post flow for Android and Desktop web. For migration guidance, refer to [UPI Intent S2S Integration](doc:upi-intent-server-to-server).

  - **For Android Apps**: Merchants must implement the Smart Intent implementation. Refer to [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) or use [PayU Android SDKs](doc:explore-android-sdks) which have Smart Intent built-in.

  - **For iOS Apps**: Merchants can implement the specific deeplink and continue using the UPI Collect flow as is.

  - **For Web**: Merchants must use the deeplink created via [UPI Intent S2S Integration](doc:upi-intent-server-to-server) to generate a QR code of the deeplink, instead of the UPI Collect flow.
</Callout>


#### I. Payment Consent Flow

<Cards>
  <Card title="1. Post the Request" href="#step-1-post-the-request">
    Send the UPI consent transaction request with S2S parameters.
  </Card>

  <Card title="2. Check Response from PayU" href="#step-2-check-the-response-from-payu">
    Handle the response for UPI Intent flows.
  </Card>

  <Card title="3. Configure Webhooks" href="#step-3-configure-webhooks">
    Set up webhooks to receive transaction status updates.
  </Card>

  <Card title="4. Verify Mandate Registration" href="#step-4-verify-mandate-registration">
    Confirm the mandate registration was successful.
  </Card>
</Cards>

#### II.  Recurring Payments Flow

<Cards>
  <Card title="1. Pre-Debit SI Notification" href="#step-1-pre-debit-si-notification">
    Send pre-debit notifications for upcoming recurring debits.
  </Card>

  <Card title="2. Recurring Payment Transaction" href="#step-2-recurring-payment-transaction">
    Execute recurring payment transactions using the registered mandate.
  </Card>
</Cards>

***

## I. Payment Consent Transaction

### Step 1: Post the Request

Before implementing, familiarize yourself with the required parameters.

<Callout icon="📘" theme="info">
  **Reference**:  For the UPI Consent Transaction - Cross Border Payments API Reference, refer to[ UPI Consent Transaction - CB](ref:upi-consent-transaction-cross-border).
</Callout>

<Accordion title="Key Parameters for UPI Mandate Registration" icon="fa-list">
  **Mandatory Parameters:**

  - `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `lastname`
  - `surl`, `furl`, `hash`
  - `pg` (must be `UPI`)
  - `bankcode` (`UPI` for Collect, `INTENT` for Intent)
  - `si` (must be `1`)
  - `si_details` (JSON object with mandate details)
  - `api_version` (must be `7`)

  **UPI-Specific Parameters:**

  - `vpa` (mandatory for UPI Collect - customer's VPA handle)

  **S2S Flow Parameters (for UPI Intent):**

  - `txn_s2s_flow` = `4` (Legacy Decoupled flow)
  - `s2s_client_ip` (customer's source IP)
  - `s2s_device_info` (customer's device/user agent)
</Accordion>

<Accordion title="Request Parameters" icon="fa-table">
  | Parameter                                                           | Description                                                                                                                                                                                                                                                             | Example                                     |
  | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
  | `key`<br />`mandatory`                                              | `String` Merchant key provided by PayU during onboarding.                                                                                                                                                                                                               | JPg\*\*\*\*f                                |
  | `txnid`<br />`mandatory`                                            | `String` The transaction ID is a reference number for a specific order that is generated by the merchant.                                                                                                                                                               | ypl938459435                                |
  | `amount`<br />`mandatory`                                           | `String` The payment amount for the transaction.                                                                                                                                                                                                                        | 10.00                                       |
  | `productinfo`<br />`mandatory`                                      | `String` A brief description of the product.                                                                                                                                                                                                                            | iPhone                                      |
  | `firstname`<br />`mandatory`                                        | `String` The first name of the customer.                                                                                                                                                                                                                                | Ashish                                      |
  | `lastname`<br />`mandatory`                                         | `String` The last name of the customer.                                                                                                                                                                                                                                 | Kumar                                       |
  | `email`<br />`mandatory`                                            | `String` The email address of the customer.                                                                                                                                                                                                                             | [abc@payu.in](mailto:abc@payu.in)           |
  | `phone`<br />`mandatory`                                            | `String` The phone number of the customer.                                                                                                                                                                                                                              |                                             |
  | `address1`<br />`optional but recommended for higher approval rate` | `String` The first line of the billing address. H.No- 17, Block C, Kalyan Bldg, Khardilkar Road, Mumbai **Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information. | 34 Saikripa-Estate, Tilak Nagar             |
  | `address2`<br />`optional but recommended for higher approval rate` | `String` The second line of the billing address.                                                                                                                                                                                                                        |                                             |
  | `city`<br />`optional but recommended for higher approval rate`     | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                           | Mumbai                                      |
  | `state`<br />`optional but recommended for higher approval rate`    | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                          | Maharashtra                                 |
  | `country`<br />`optional but recommended for higher approval rate`  | `String` The country where your customer resides.                                                                                                                                                                                                                       | India                                       |
  | `zipcode`<br />`mandatory`                                          | `String` Billing address zip code is mandatory for the cardless EMI option. Character Limit-20                                                                                                                                                                          | 400004                                      |
  | `pg`<br />`mandatory for seamless/s2s flow`                         | `String` It defines the payment category and post **UPI**.                                                                                                                                                                                                              | UPI                                         |
  | `bankcode`<br />`mandatory for seamless/s2s flow`                   | `String` Each payment option is identified with a unique bank code at PayU. For UPI Autopay, post **UPI**.                                                                                                                                                              | UPI                                         |
  | `surl`<br />`mandatory`                                             | `String` The success URL, which is the page PayU will redirect to if the transaction is successful.                                                                                                                                                                     |                                             |
  | `furl`<br />`mandatory`                                             | `String` The Failure URL, which is the page PayU will redirect to if the transaction is failed.                                                                                                                                                                         |                                             |
  | vpa `conditional`                                                   | `String` Customer's VPA handle. Mandatory for UPI Collect flow.                                                                                                                                                                                                         | `customer@upi`                              |
  | si `mandatory`                                                      | `String` Signifies successful consent taken from the user. Must be `1` for subscription setup.                                                                                                                                                                          | `1`                                         |
  | si_details `mandatory`                                              | `JSON String` JSON object containing mandate details (billingAmount, billingCurrency, billingCycle, etc.). Refer to si_details JSON Object below.                                                                                                                       | See si_details accordion                    |
  | txn_s2s_flow `conditional`                                          | `Integer` Parameter to enable S2S flow. Must be `4` for Legacy Decoupled flow (UPI Intent).                                                                                                                                                                             | `4`                                         |
  | s2s_client_ip `conditional`                                         | `String` Source IP of the customer. Required for UPI Intent flow.                                                                                                                                                                                                       | `10.200.12.12`                              |
  | s2s_device_info `conditional`                                       | `String` Customer agent's device information. Required for UPI Intent flow.                                                                                                                                                                                             | `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` |
</Accordion>

<Accordion title="Hashing Logic" icon="fa-table">
  <PACB_Hashing />
</Accordion>

<Accordion title="si_details JSON Object" icon="fa-code">
  The `si_details` parameter is a JSON object containing mandate details:

  ```json
  {
    "billingAmount": "10.00",
    "billingCurrency": "INR",
    "billingCycle": "MONTHLY",
    "billingInterval": 1,
    "paymentStartDate": "2025-06-05",
    "paymentEndDate": "2025-12-01"
  }
  ```

  | Field                             | Description                                                                       | Example      |
  | --------------------------------- | --------------------------------------------------------------------------------- | ------------ |
  | billingAmount<br />`mandatory`    | `String`<br />Maximum amount for recurring transactions.                          | `10.00`      |
  | billingCurrency<br />`mandatory`  | `String`<br />Currency code.                                                      | `INR`        |
  | billingCycle<br />`mandatory`     | `String`<br />Billing frequency: `DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`, `ADHOC`. | `MONTHLY`    |
  | billingInterval<br />`mandatory`  | `Integer`<br />Interval between billing cycles.                                   | `1`          |
  | paymentStartDate<br />`mandatory` | `String`<br />Mandate start date (YYYY-MM-DD).                                    | `2025-06-05` |
  | paymentEndDate<br />`mandatory`   | `String`<br />Mandate end date (YYYY-MM-DD).                                      | `2025-12-01` |
</Accordion>

#### A. UPI Intent Flow
<Accordion title="Request Payload Structure" icon="fa-file-code">
  #### UPI Intent Flow (with S2S Parameters)
  ```json
  {
    "key": "JPM7Fg",
    "txnid": "upiIntentTxn12345",
    "amount": "10.00",
    "productinfo": "Monthly Subscription",
    "firstname": "Ashish",
      "lastname": "Kumar",
      "email": "abc@payu.in",
    "phone": "9988776655",
      "address1": "34 Saikripa-Estate, Tilak Nagar",
      "city": "Mumbai",
      "state": "Maharashtra",
      "country": "India",
      "zipcode": "400004",
    "surl": "https://example.com/success",
    "furl": "https://example.com/failure",
      "udf1": "AAAPZ1234C||22/08/1972",
      "udf3": "INV-123_1231||MerchantName",
      "buyer_type_business": "1",
    "pg": "UPI",
    "bankcode": "INTENT",
    "api_version": "7",
    "si": "1",
    "si_details": "{\"billingAmount\":\"10.00\",\"billingCurrency\":\"INR\",\"billingCycle\":\"MONTHLY\",\"billingInterval\":1,\"paymentStartDate\":\"2025-06-05\",\"paymentEndDate\":\"2025-12-01\"}",
    "txn_s2s_flow": "4",
    "s2s_client_ip": "10.200.12.12",
      "s2s_device_info": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "hash": "generated_hash_value"
  }
  ```
</Accordion>

<Accordion title="Sample Request for UPI Intent" icon="fa-terminal">
  ```bash
```curl
curl --location 'https://secure.payu.in/_payment' \
--header 'accept: application/json' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642; PHPSESSID=68edd726c95b4' \
--data-urlencode 'key=BmTY3G' \
--data-urlencode 'txnid=my_order_95314' \
--data-urlencode 'amount=1.00' \
--data-urlencode 'firstname=Payu-Admin' \
--data-urlencode 'email=test@example.com' \
--data-urlencode 'phone=1234567890' \
--data-urlencode 'productinfo=my_order_95314' \
--data-urlencode 'api_version=7' \
--data-urlencode 'si=1' \
--data-urlencode 'pg=UPI' \
--data-urlencode 'bankcode=INTENT' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'surl=https://test.payu.in/admin/test_response/' \
--data-urlencode 'furl=https://test.payu.in/admin/test_response' \
--data-urlencode 'si_details={"billingAmount":"1.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2025-10-14","paymentEndDate":"2019-12-01"}' \
--data-urlencode 'hash=67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb'
```
```python
import requests

url = "https://secure.payu.in/_payment"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
}

data = {
    "key": "BmTY3G",
    "txnid": "my_order_95314",
    "amount": "1.00",
    "firstname": "Payu-Admin",
    "email": "test@example.com",
    "phone": "1234567890",
    "productinfo": "my_order_95314",
    "api_version": "7",
    "si": "1",
    "pg": "UPI",
    "bankcode": "INTENT",
    "txn_s2s_flow": "4",
    "surl": "https://test.payu.in/admin/test_response/",
    "furl": "https://test.payu.in/admin/test_response",
    "si_details": '{"billingAmount":"1.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2025-10-14","paymentEndDate":"2019-12-01"}',
    "hash": "67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb",
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.text)
```
```javascript
async function makePayURequest() {
  const url = "https://secure.payu.in/_payment";

  const body = new URLSearchParams({
    key: "BmTY3G",
    txnid: "my_order_95314",
    amount: "1.00",
    firstname: "Payu-Admin",
    email: "test@example.com",
    phone: "1234567890",
    productinfo: "my_order_95314",
    api_version: "7",
    si: "1",
    pg: "UPI",
    bankcode: "INTENT",
    txn_s2s_flow: "4",
    surl: "https://test.payu.in/admin/test_response/",
    furl: "https://test.payu.in/admin/test_response",
    si_details:
      '{"billingAmount":"1.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2025-10-14","paymentEndDate":"2019-12-01"}',
    hash: "67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb",
  });

  const response = await fetch(url, {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body,
  });

  console.log(response.status);
  console.log(await response.text());
}

makePayURequest();
```
```php
$url = "https://secure.payu.in/_payment";

$postData = [
    "key" => "BmTY3G",
    "txnid" => "my_order_95314",
    "amount" => "1.00",
    "firstname" => "Payu-Admin",
    "email" => "test@example.com",
    "phone" => "1234567890",
    "productinfo" => "my_order_95314",
    "api_version" => "7",
    "si" => "1",
    "pg" => "UPI",
    "bankcode" => "INTENT",
    "txn_s2s_flow" => "4",
    "surl" => "https://test.payu.in/admin/test_response/",
    "furl" => "https://test.payu.in/admin/test_response",
    "si_details" => '{"billingAmount":"1.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2025-10-14","paymentEndDate":"2019-12-01"}',
    "hash" => "67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb",
];

$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => $url,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => http_build_query($postData),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        "accept: application/json",
        "Content-Type: application/x-www-form-urlencoded",
    ],
]);

$response = curl_exec($ch);
$status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo $status . PHP_EOL;
echo $response;
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

public class PayUPayment {
    public static void main(String[] args) throws Exception {
        String url = "https://secure.payu.in/_payment";

        Map<String, String> formData = new LinkedHashMap<>();
        formData.put("key", "BmTY3G");
        formData.put("txnid", "my_order_95314");
        formData.put("amount", "1.00");
        formData.put("firstname", "Payu-Admin");
        formData.put("email", "test@example.com");
        formData.put("phone", "1234567890");
        formData.put("productinfo", "my_order_95314");
        formData.put("api_version", "7");
        formData.put("si", "1");
        formData.put("pg", "UPI");
        formData.put("bankcode", "INTENT");
        formData.put("txn_s2s_flow", "4");
        formData.put("surl", "https://test.payu.in/admin/test_response/");
        formData.put("furl", "https://test.payu.in/admin/test_response");
        formData.put("si_details", "{\"billingAmount\":\"1.00\",\"billingCurrency\":\"INR\",\"billingCycle\":\"MONTHLY\",\"billingInterval\":1,\"paymentStartDate\":\"2025-10-14\",\"paymentEndDate\":\"2019-12-01\"}");
        formData.put("hash", "67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb");

        String body = formData.entrySet().stream()
                .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                        + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
                .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(body))
                .build();

        HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println(response.statusCode());
        System.out.println(response.body());
    }
}
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main()
    {
        string url = "https://secure.payu.in/_payment";
        client.DefaultRequestHeaders.Accept.Add(
            new MediaTypeWithQualityHeaderValue("application/json"));

        var formData = new List<KeyValuePair<string, string>>
        {
            new("key", "BmTY3G"),
            new("txnid", "my_order_95314"),
            new("amount", "1.00"),
            new("firstname", "Payu-Admin"),
            new("email", "test@example.com"),
            new("phone", "1234567890"),
            new("productinfo", "my_order_95314"),
            new("api_version", "7"),
            new("si", "1"),
            new("pg", "UPI"),
            new("bankcode", "INTENT"),
            new("txn_s2s_flow", "4"),
            new("surl", "https://test.payu.in/admin/test_response/"),
            new("furl", "https://test.payu.in/admin/test_response"),
            new("si_details", "{\"billingAmount\":\"1.00\",\"billingCurrency\":\"INR\",\"billingCycle\":\"MONTHLY\",\"billingInterval\":1,\"paymentStartDate\":\"2025-10-14\",\"paymentEndDate\":\"2019-12-01\"}"),
            new("hash", "67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb"),
        };

        var response = await client.PostAsync(url, new FormUrlEncodedContent(formData));
        Console.WriteLine((int)response.StatusCode);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
```

  <Callout icon="📘" theme="info">
    Notes:
   -  `paymentEndDate` in the sample (`2019-12-01`) is before `paymentStartDate` — use a later end date in a real request, and keep the exact `si_details` string aligned with your hash.
    - `/_payment` usually returns HTML for a browser redirect; in production, merchants typically POST these fields from an HTML form, not a server-side HTTP client.
    - Prefer valid JSON for `si_details`, for example:

    ```
    {"billingAmount":"1.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2025-10-14","paymentEndDate":"2027-12-01"}
    ```

    Keep the same string in both the request body and the hash calculation.
  </Callout>
</Accordion>

<Callout icon="📘" theme="info">
  **Note**: Before you make payment request to PayU, it is recommended to validate the UPI handle provided by your customer is eligible for recurring payment using the validateVPA API. For more information, refer to [Validate VPA API](ref:validate_vpa_api).
</Callout>
#### B. UPI Collect Flow
<Callout icon="📘" theme="info">
Notes: 
* For UPI Collect flow, you must note that *si=1** 
* As per NPCI's guidelines, UPI Collect payments are allowed only on MCC 6012 and 6211. 
  </Callout>
<Accordion title="Sample request" icon="fa-code">
```curl
curl --location 'https://secure.payu.in/_payment' \
--header 'accept: application/json' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642; PHPSESSID=68ed52caaaf5e' \
--data-urlencode 'key=BmTY3G' \
--data-urlencode 'txnid=my_order_29327' \
--data-urlencode 'amount=1.00' \
--data-urlencode 'firstname=Payu-Admin' \
--data-urlencode 'email=test@example.com' \
--data-urlencode 'phone=1234567890' \
--data-urlencode 'productinfo=my_order_29327' \
--data-urlencode 'api_version=7' \
--data-urlencode 'si=1' \
--data-urlencode 'pg=UPI' \
--data-urlencode 'bankcode=UPI' \
--data-urlencode 'vpa=anything@payu' \
--data-urlencode 'surl=https://test.payu.in/admin/test_response/' \
--data-urlencode 'furl=https://test.payu.in/admin/test_response' \
--data-urlencode 'si_details={"billingAmount":"1.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2025-10-14","paymentEndDate":"2029-12-01"}' \
--data-urlencode 'hash=67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb'
```
```python
import requests

url = "https://secure.payu.in/_payment"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
}

data = {
    "key": "BmTY3G",
    "txnid": "my_order_29327",
    "amount": "1.00",
    "firstname": "Payu-Admin",
    "email": "test@example.com",
    "phone": "1234567890",
    "productinfo": "my_order_29327",
    "api_version": "7",
    "si": "1",
    "pg": "UPI",
    "bankcode": "UPI",
    "vpa": "anything@payu",
    "surl": "https://test.payu.in/admin/test_response/",
    "furl": "https://test.payu.in/admin/test_response",
    "si_details": '{"billingAmount":"1.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2025-10-14","paymentEndDate":"2029-12-01"}',
    "hash": "67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb",
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
print(response.text)
```
```javascript
async function makePayURequest() {
  const url = "https://secure.payu.in/_payment";

  const body = new URLSearchParams({
    key: "BmTY3G",
    txnid: "my_order_29327",
    amount: "1.00",
    firstname: "Payu-Admin",
    email: "test@example.com",
    phone: "1234567890",
    productinfo: "my_order_29327",
    api_version: "7",
    si: "1",
    pg: "UPI",
    bankcode: "UPI",
    vpa: "anything@payu",
    surl: "https://test.payu.in/admin/test_response/",
    furl: "https://test.payu.in/admin/test_response",
    si_details:
      '{"billingAmount":"1.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2025-10-14","paymentEndDate":"2029-12-01"}',
    hash: "67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb",
  });

  const response = await fetch(url, {
    method: "POST",
    headers: {
      accept: "application/json",
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body,
  });

  console.log(response.status);
  console.log(await response.text());
}

makePayURequest();
```
```php
$url = "https://secure.payu.in/_payment";

$postData = [
    "key" => "BmTY3G",
    "txnid" => "my_order_29327",
    "amount" => "1.00",
    "firstname" => "Payu-Admin",
    "email" => "test@example.com",
    "phone" => "1234567890",
    "productinfo" => "my_order_29327",
    "api_version" => "7",
    "si" => "1",
    "pg" => "UPI",
    "bankcode" => "UPI",
    "vpa" => "anything@payu",
    "surl" => "https://test.payu.in/admin/test_response/",
    "furl" => "https://test.payu.in/admin/test_response",
    "si_details" => '{"billingAmount":"1.00","billingCurrency":"INR","billingCycle":"MONTHLY","billingInterval":1,"paymentStartDate":"2025-10-14","paymentEndDate":"2029-12-01"}',
    "hash" => "67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb",
];

$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => $url,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => http_build_query($postData),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        "accept: application/json",
        "Content-Type: application/x-www-form-urlencoded",
    ],
]);

$response = curl_exec($ch);
$status = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo $status . PHP_EOL;
echo $response;
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

public class PayUPayment {
    public static void main(String[] args) throws Exception {
        String url = "https://secure.payu.in/_payment";

        Map<String, String> formData = new LinkedHashMap<>();
        formData.put("key", "BmTY3G");
        formData.put("txnid", "my_order_29327");
        formData.put("amount", "1.00");
        formData.put("firstname", "Payu-Admin");
        formData.put("email", "test@example.com");
        formData.put("phone", "1234567890");
        formData.put("productinfo", "my_order_29327");
        formData.put("api_version", "7");
        formData.put("si", "1");
        formData.put("pg", "UPI");
        formData.put("bankcode", "UPI");
        formData.put("vpa", "anything@payu");
        formData.put("surl", "https://test.payu.in/admin/test_response/");
        formData.put("furl", "https://test.payu.in/admin/test_response");
        formData.put("si_details", "{\"billingAmount\":\"1.00\",\"billingCurrency\":\"INR\",\"billingCycle\":\"MONTHLY\",\"billingInterval\":1,\"paymentStartDate\":\"2025-10-14\",\"paymentEndDate\":\"2029-12-01\"}");
        formData.put("hash", "67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb");

        String body = formData.entrySet().stream()
                .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                        + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
                .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(body))
                .build();

        HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println(response.statusCode());
        System.out.println(response.body());
    }
}
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main()
    {
        string url = "https://secure.payu.in/_payment";
        client.DefaultRequestHeaders.Accept.Add(
            new MediaTypeWithQualityHeaderValue("application/json"));

        var formData = new List<KeyValuePair<string, string>>
        {
            new("key", "BmTY3G"),
            new("txnid", "my_order_29327"),
            new("amount", "1.00"),
            new("firstname", "Payu-Admin"),
            new("email", "test@example.com"),
            new("phone", "1234567890"),
            new("productinfo", "my_order_29327"),
            new("api_version", "7"),
            new("si", "1"),
            new("pg", "UPI"),
            new("bankcode", "UPI"),
            new("vpa", "anything@payu"),
            new("surl", "https://test.payu.in/admin/test_response/"),
            new("furl", "https://test.payu.in/admin/test_response"),
            new("si_details", "{\"billingAmount\":\"1.00\",\"billingCurrency\":\"INR\",\"billingCycle\":\"MONTHLY\",\"billingInterval\":1,\"paymentStartDate\":\"2025-10-14\",\"paymentEndDate\":\"2029-12-01\"}"),
            new("hash", "67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb"),
        };

        var response = await client.PostAsync(url, new FormUrlEncodedContent(formData));
        Console.WriteLine((int)response.StatusCode);
        Console.WriteLine(await response.Content.ReadAsStringAsync());
    }
}
```
***

### Step 2: Check the Response from PayU

#### A. UPI Intent Flow 
The API returns different response the following for UPI Intent.

<Accordion title="UPI Intent Response" icon="fa-check">
  For UPI Intent with S2S flow, the response is a JSON object containing the intent URI:

  ```json
  {
     "metaData": {
        "message": null,
        "referenceId": "5ae6e6d94b4b5f9dee282b95f6020c98",
        "statusCode": null,
        "txnId": "upiIntentTxn12345",
        "txnStatus": "pending",
        "unmappedStatus": "pending"
     },
     "result": {
        "paymentId": "15257049438",
        "merchantName": "Your Merchant Name",
        "merchantVpa": "merchant@hdfcbank",
        "amount": "10.00",
        "intentURIData": "upi://mandate?pa=merchant@hdfcbank&pn=MERCHANT NAME&mn=&tid=upiIntentTxn12345&validitystart=05062025&validityend=01122025&am=10.00&amrule=MAX&recur=MONTHLY&recurvalue=30&recurtype=&tr=15257049438&cu=INR&mc=5411&tn=UPI Transaction for upiIntentTxn12345&mode=13&purpose=14&orgid=159240&rev=Y&block=N&txnType=CREATE",
        "postToBank": {
           "token": "C6ABAA6A-F0CE-432A-61C1-CFA48EDE847B",
           "amount": "10.00",
           "mihpayid": "5ae6e6d94b4b5f9dee282b95f6020c98",
           "disableIntentSeamlessFailure": "0",
           "payeeVpa": "merchant@hdfcbank",
           "payeeName": "Your Merchant Name",
           "additionalCharges": 0,
           "transactionFee": "10.00"
        },
        "issuerUrl": "https://secure.payu.in/intentSeamlessHandler.php"
     }
  }
  ```
</Accordion>

<Accordion title="Response Handling Logic" icon="fa-info-circle">
  ### Handling UPI Intent Response

  1. Extract the `intentURIData` from the response
  2. Launch the UPI app using the intent URI
  3. Wait for the customer to approve the mandate
  4. Receive the final status via webhook or callback
</Accordion>

<Callout icon="📘" theme="info">
  If you want to use PayU's timer page for UPI collect, you can use the **result.acsTemplate** and **base64decode** it to redirect the customer on given HTML.
</Callout>

#### B. UPI Collect Flow

<Accordion title="Hash Validation" icon="fa-lock">

While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

The order of the parameters is similar to the following code block:

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```
</Accordion>

<Accordion title="Sample Response" icon="fa-code">
  ```
      Array
      (
          [mihpayid] => 403993715523409521
          [mode] => UPI
          [status] => success
          [unmappedstatus] => captured
          [key] => JPM7Fg
          [txnid] => 5jJ9xRceXX1ydT
          [amount] => 10.00
          [discount] => 0.00
          [net_amount_debit] => 1000
          [addedon] => 2021-07-02 15:03:50
          [productinfo] => iPhone
          [firstname] => PayU User
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
          [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
          [field1] => vpa-anything@payu
          [field2] => 5jJ9xRceXX1ydT
          [field3] => 
          [field4] => PayU User
          [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
          [field6] => 
          [field7] => Transaction completed successfully
          [field8] => 
          [field9] => Transaction completed successfully
          [payment_source] => payu
          [PG_TYPE] => UPI-PG
          [bank_ref_num] => 5jJ9xRceXX1ydT
          [bankcode] => UPI
          [error] => E000
          [error_Message] => No Error
      )
  ```
</Accordion>


***

### Step 3: Configure Webhooks

Configure webhooks to receive real-time transaction status updates. PayU will send POST requests to your webhook URL.

<Accordion title="Webhook Configuration" icon="fa-cog">
  You can configure the webhook from Payu dashboard directly for payment success/failure events. For more information, refer to [Create a New Webhook](https://docs.payu.in/docs/create-a-new-webhook). Once configured, you will receive transaction updates via HTTP POST.
</Accordion>

<Accordion title="Webhook Payload Example" icon="fa-code">
  ```text
    unmappedstatus=success&phone=9988776655&txnid=upiConsentTxn12345&hash=84e335094bbcb2ddaa0f9a488eb338e143b273765d89c9dfa502402562d0b6f3c7935e28194ca92f380be7c84c3695415b106dcf52cb016a15fcf6adc98d724&status=success&firstname=Ashish&productinfo=Monthly Subscription&mode=UPI&amount=10.00&email=test@payu.in&mihpayid=403993715525317379&surl=https://example.com/success&payment_source=sist
  ```
</Accordion>

<Accordion title="Webhook Validation" icon="fa-lock">
  Always validate the webhook hash before processing:

  ```php
  function validateWebhookHash($response, $salt) {
      $hashSequence = "status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key";
      $hashVarsSeq = explode('|', $hashSequence);
      
      $hashString = $salt . '|';
      foreach(array_reverse($hashVarsSeq) as $hashVar) {
          $hashString .= isset($response[$hashVar]) ? $response[$hashVar] : '';
          $hashString .= '|';
      }
      $hashString = rtrim($hashString, '|');
      
      $calculatedHash = strtolower(hash('sha512', $hashString));
      $receivedHash = strtolower($response['hash']);
      
      return $calculatedHash === $receivedHash;
  }
  ```
</Accordion>

<Accordion title="Expected Values for Successful Registration" icon="fa-table">
  | Response Parameter | Expected Value | Description                                                               |
  | ------------------ | -------------- | ------------------------------------------------------------------------- |
  | status             | `success`      | Indicates that the transaction is successful with the UPI provider        |
  | payment_source     | `sist`         | Indicates UPI details have been marked correctly for Standing Instruction |
  | mihpayid           | `<mihpayid>`   | PayU's transaction acknowledgment for a Consent transaction               |
</Accordion>

<Accordion title="Handling Mandate Status Updates" icon="fa-bell">
  If the mandate is not confirmed by the customer or is rejected by the bank, the status is communicated as "failure" over webhook.

  | Status    | Description                                       |
  | --------- | ------------------------------------------------- |
  | `success` | Mandate registered successfully                   |
  | `failure` | Mandate registration failed or rejected           |
  | `pending` | Mandate registration is pending customer approval |

  For more information, refer to [Set up WebHook to Receive Cancellation or Modification Update from the Issuer Bank](ref:set-up-webhook-to-receive-cancellation-or-modification-update-from-the-issuer-bank).
</Accordion>

***

### Step 4: Verify Mandate Registration

After successful registration, verify the mandate status:

<Accordion title="Verification Checklist" icon="fa-check-circle">
  1. **Check Response Parameters**:
     - `status` should be `success`
     - `payment_source` should be `sist`
     - `mihpayid` should not be null

  2. **Store Mandate Details**:
     - Save `mihpayid` for future recurring payments
     - Save mandate expiry dates from `si_details`
     - Store customer's VPA for reference

  3. **Test Subsequent Payment**:
     - Use the stored mandate details to initiate a subsequent recurring payment
     - Verify the payment processes successfully
</Accordion>

## II. Recurring Payments Flow

### Workflow


<Image src="https://files.readme.io/ffac22445b558dd93d085536bb1065ab818e716c50e6839ce4569427dde92275-UPI_Autopay_-_Recurring_Payment_flow.png" align="center" />


### Step 1: Pre-Debit SI Notification

Use the **Pre-Debit SI** API to send pre-debit notifications for upcoming recurring debits with parallel sequencing support. This notification mandator for Cards and UPI recurring only and not required for ENACH recurring.

| Environment | URL                                                    |
| :---------- | :----------------------------------------------------- |
| Test        | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production  | `https://info.payu.in/merchant/postservice.php?form=2` |

<Accordion title="Request Parameters" icon="fa-info-circle">
  | Parameter                             | Description                                                                                                                                                   | Example               |
  | :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------- |
  | key <br /> <code>mandatory</code>     | <code>String</code> Your merchant key provided by PayU.                                                                                                       | JP\*\*\*g             |
  | command <br /> <code>mandatory</code> | <code>String</code> The API command name.                                                                                                                     | pre_debit_SI          |
  | hash <br /> <code>mandatory</code>    | <code>String</code> The hash value generated using the hash logic.                                                                                            | abc0ada2e12           |
  | var1 <br /> <code>mandatory</code>    | <code>JSON String</code> JSON object containing the pre-debit details. For more information refer to [var1 Object Parameters](#var1-object-parameters) table. | See var1 Object below |

  ##### Hash logic

  The hash is generated using the following formula:

  ```
  hash = sha512(key|command|var1|salt)
  ```

  ### var1 Object Parameters

  | Parameter                                       | Description                                                                                                                            | Example         |
  | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
  | authpayuid<br />`mandatory`                     | `String` The mihpayid received during the successful consent transaction.                                                              | 999000000000826 |
  | requestid<br />`mandatory`                      | `String` Unique request ID for tracking the pre-debit request.                                                                         | RCS0123459PD    |
  | debitdate<br />`mandatory`                      | `String` The date when the debit will occur in YYYY-MM-DD format.                                                                      | 2024-11-22      |
  | amount<br />`mandatory`                         | `String` The amount to be debited.                                                                                                     | 125             |
  | invoiceDisplayNumber<br />`mandatory for cards` | `String` Invoice number to display to the customer.                                                                                    | 12345678910     |
  | action<br />`optional`                          | Pass "Retrieve" or "Delete" according to the action need to be performed. For more information, refer to Additional Information table. | Retrieve        |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl --location 'https://test.info.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'command=pre_debit_SI' \
  --data-urlencode 'var1={"authpayuid":"999000000000826","requestid":"RCS0123459PD","debitdate":"2024-11-22","amount":"125","invoiceDisplayNumber":"12345678910"}' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'hash=abc0ada2e12'
  ```
  ```python
  import requests

  url = "https://test.info.payu.in/merchant/postservice.php?form=2"

  payload = {
      "command": "pre_debit_SI",
      "var1": '{"authpayuid":"999000000000826","requestid":"RCS0123459PD","debitdate":"2024-11-22","amount":"125","invoiceDisplayNumber":"12345678910"}',
      "key": "JP***g",
      "hash": "abc0ada2e12"
  }

  headers = {
      "Content-Type": "application/x-www-form-urlencoded"
  }

  response = requests.post(url, data=payload, headers=headers)
  print(response.json())
  ```
  ```csharp
  using System;
  using System.Net.Http;
  using System.Collections.Generic;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main()
      {
          using var client = new HttpClient();
          
          var content = new FormUrlEncodedContent(new[]
          {
              new KeyValuePair<string, string>("command", "pre_debit_SI"),
              new KeyValuePair<string, string>("var1", "{\"authpayuid\":\"999000000000826\",\"requestid\":\"RCS0123459PD\",\"debitdate\":\"2024-11-22\",\"amount\":\"125\",\"invoiceDisplayNumber\":\"12345678910\"}"),
              new KeyValuePair<string, string>("key", "JP***g"),
              new KeyValuePair<string, string>("hash", "abc0ada2e12")
          });
          
          var response = await client.PostAsync("https://test.info.payu.in/merchant/postservice.php?form=2", content);
          var result = await response.Content.ReadAsStringAsync();
          Console.WriteLine(result);
      }
  }
  ```
  ```javascript
  const sendPreDebitRequest = async () => {
      const url = "https://test.info.payu.in/merchant/postservice.php?form=2";
      
      const params = new URLSearchParams();
      params.append("command", "pre_debit_SI");
      params.append("var1", JSON.stringify({
          authpayuid: "999000000000826",
          requestid: "RCS0123459PD",
          debitdate: "2024-11-22",
          amount: "125",
          invoiceDisplayNumber: "12345678910"
      }));
      params.append("key", "JP***g");
      params.append("hash", "abc0ada2e12");
      
      const response = await fetch(url, {
          method: "POST",
          headers: {
              "Content-Type": "application/x-www-form-urlencoded"
          },
          body: params
      });
      
      const data = await response.json();
      console.log(data);
  };

  sendPreDebitRequest();
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class PreDebitSI {
      public static void main(String[] args) throws Exception {
          String url = "https://test.info.payu.in/merchant/postservice.php?form=2";
          
          String params = "command=pre_debit_SI" +
              "&var1=" + URLEncoder.encode("{\"authpayuid\":\"999000000000826\",\"requestid\":\"RCS0123459PD\",\"debitdate\":\"2024-11-22\",\"amount\":\"125\",\"invoiceDisplayNumber\":\"12345678910\"}", StandardCharsets.UTF_8) +
              "&key=JP***g" +
              "&hash=abc0ada2e12";
          
          HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
          conn.setRequestMethod("POST");
          conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
          conn.setDoOutput(true);
          
          try (OutputStream os = conn.getOutputStream()) {
              os.write(params.getBytes(StandardCharsets.UTF_8));
          }
          
          try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
              String line;
              while ((line = br.readLine()) != null) {
                  System.out.println(line);
              }
          }
      }
  }
  ```
  ```php
  <?php
  $url = "https://test.info.payu.in/merchant/postservice.php?form=2";

  $data = array(
      "command" => "pre_debit_SI",
      "var1" => json_encode(array(
          "authpayuid" => "999000000000826",
          "requestid" => "RCS0123459PD",
          "debitdate" => "2024-11-22",
          "amount" => "125",
          "invoiceDisplayNumber" => "12345678910"
      )),
      "key" => "JP***g",
      "hash" => "abc0ada2e12"
  );

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array("Content-Type: application/x-www-form-urlencoded"));

  $response = curl_exec($ch);
  curl_close($ch);

  echo $response;
  ?>
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  **Success Response**

  ```json
  {
      "status": "1",
      "action": "MANDATE_PRE_DEBIT",
      "message": "Request Processed Successfully"
  }
  ```

  **Error Responses**

  | Scenario                              | Response                                                                                                                               |
  | :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------- |
  | Invalid mandateSeqNo                  | `{"status":"0","message":"Invalid value for mandateSeqNo","action":"MANDATE_PRE_DEBIT"}`                                               |
  | Pre-debit already sent for sequence   | `{"status":"E9254","action":"MANDATE_PRE_DEBIT","message":"Predebit notification already sent for the mandate sequence no. 2"}`        |
  | Execution already exists for sequence | `{"status":"E9256","action":"MANDATE_PRE_DEBIT","message":"Execution already sent for the mandate sequence no.:2"}`                    |
  | Debit date exceeds 30 days            | `{"status":"E9260","action":"MANDATE_PRE_DEBIT","message":"Predebit notification can only be sent for a maximum 30 days in advance."}` |
  | Pre-debit sent for past sequence      | `{"status":"E9263","action":"MANDATE_PRE_DEBIT","message":"Predebit for calculated sequence sent during incorrect period"}`            |
</Accordion>

#### Response Parameters

| Parameter | Description                                                                                            | Example                        |
| :-------- | :----------------------------------------------------------------------------------------------------- | :----------------------------- |
| status    | <code>String</code> Status of the request. `1` indicates success, `0` or error code indicates failure. | 1                              |
| action    | <code>String</code> The action performed.                                                              | MANDATE_PRE_DEBIT              |
| message   | <code>String</code> Description of the response status.                                                | Request Processed Successfully |

### Step 2: Recurring Payment Transaction

Use the **Recurring Payment Transaction** API to execute recurring payment transactions for customers who have already completed a successful mandate/registration transaction with Net Banking, UPI, or Cards. For detailed API reference, refer to [Recurring Payment Transaction API - PACB](ref:recurring-payment-transaction-api-pacb).

| Environment | URL                                                |
| :---------- | :------------------------------------------------- |
| Production  | `https://info.payu.in/merchant/postservice?form=2` |
| Test        | `https://test.payu.in/merchant/postservice?form=2` |

<Accordion title="Request Parameters" icon="fa-info-circle">
  | Parameter                             | Description                                                                                  | Example                           |        |         |               |
  | :------------------------------------ | :------------------------------------------------------------------------------------------- | :-------------------------------- | ------ | ------- | ------------- |
  | key <br /> <code>mandatory</code>     | <code>String</code> Merchant Key provided by PayU                                            | JPM7Fg                            |        |         |               |
  | command <br /> <code>mandatory</code> | <code>String</code> API command. Must be `si_transaction`                                    | si_transaction                    |        |         |               |
  | var1 <br /> <code>mandatory</code>    | <code>JSON Object</code> Transaction details object containing mandatory and optional fields | Refer to var1 Object Fields below |        |         |               |
  | hash <br /> <code>mandatory</code>    | <code>String</code> SHA512 hash: \`sha512(key\\                                              | command\\                         | var1\\ | salt)\` | 9f5faabedb... |

  ### var1 Object Fields

  | Parameter                                                                      | Description                                                                                                                                                               | Example                                             |
  | :----------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------- |
  | authpayuid <br /> <code>mandatory</code>                                       | <code>String</code> The mihpayid returned in the payment response of the Registration/Consent transaction when transaction is successfully completed.                     | 6611192557                                          |
  | amount <br /> <code>mandatory</code>                                           | <code>String</code> The transaction amount which will be deducted from the customer's payment instrument.                                                                 | 10.00                                               |
  | txnid <br /> <code>mandatory</code>                                            | <code>String</code> Unique Transaction ID (Order ID) generated by the merchant for this recurring transaction.                                                            | REC15113506209                                      |
  | firstname <br /> <code>mandatory</code>                                        | <code>String</code> First name of the buyer/customer.                                                                                                                     | John                                                |
  | lastname <br /> <code>mandatory</code>                                         | <code>String</code> Last name of the buyer/customer.                                                                                                                      | Doe                                                 |
  | address1 <br /> <code>optional but recommended for higher approval rate</code> | <code>String</code> Address line 1 of the buyer.                                                                                                                          | 123 Main Street                                     |
  | city <br /> <code>optional but recommended for higher approval rate</code>     | <code>String</code> City of the buyer.                                                                                                                                    | Mumbai                                              |
  | state <br /> <code>optional but recommended for higher approval rate</code>    | <code>String</code> State of the buyer.                                                                                                                                   | Maharashtra                                         |
  | country <br /> <code>optional but recommended for higher approval rate</code>  | <code>String</code> Country of the buyer. Allowed values: `IN` or `India` only.                                                                                           | IN                                                  |
  | zipcode <br /> <code>mandatory</code>                                          | <code>String</code> ZIP/PIN code of the buyer. Must be a valid 6-digit Indian PIN code.                                                                                   | 400001                                              |
  | phone <br /> <code>optional</code>                                             | <code>String</code> The phone number of the customer.                                                                                                                     | 9999999999                                          |
  | email <br /> <code>optional</code>                                             | <code>String</code> The email address of the customer.                                                                                                                    | [customer@example.com](mailto:customer@example.com) |
  | invoiceDisplayNumber <br /> <code>mandatory for Cards SI</code>                | <code>String</code> A unique display number by merchant for every subsequent invoice/recurring charge. This must be the same value passed during `pre_debit_si` API call. | 12345678910                                         |
  | udf1<br /><code>optional but recommended for higher approval rate</code>       | <code>String</code> If needed, contains the buyer's PAN. For UPI recurring, format is "Buyer's PAN\\\|\\\|Buyer's DOB". Character limit: 255.                             | AELPR1234E or AELPR1234E\\\|\\\|02-02-1980          |
  | udf2<br /><code>optional</code>                                                | <code>String</code> User-defined field for storing transaction-specific data. Character limit: 255.                                                                       | Additional transaction data                         |
  | udf3<br />`optional but recommended for higher approval rate`                  | `String` Date of Birth (DOB) of buyer in DD-MM-YYYY                                                                                                                       | 02-02-1980                                          |
  | udf4<br />`mandatory for payment aggregators`                                  | `String` End merchant legal entity name. For UPI, this field should not be passed. Character limit: 255.                                                                  | XYZ Pvt. Ltd.                                       |
  | udf5<br />`mandatory for cross-border payments`                                | `String` Contains invoice ID for the merchant. Character limit: 255.                                                                                                      | INV123456                                           |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```bash
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPM7Fg&command=si_transaction&var1={
    \"authpayuid\": \"6611192557\",
    \"amount\": \"100.00\",
    \"txnid\": \"REC15113506209\",
    \"phone\": \"9999999999\",
    \"email\": \"customer@example.com\",
    \"firstname\": \"John\",
    \"lastname\": \"Doe\",
    \"address1\": \"123 Main Street\",
    \"city\": \"Mumbai\",
    \"state\": \"Maharashtra\",
    \"country\": \"IN\",
    \"zipcode\": \"400001\",
    \"invoiceDisplayNumber\": \"12345678910\",
    \"udf1\": \"ABCDE1234F\",
    \"udf2\": \"\",
    \"udf3\": \"15-08-1990\",
    \"udf4\": \"\",
    \"udf5\": \"INV789012\"
  }&hash=jbUS07Og8BToVZ..."
  ```
  ```python
  import requests

  url = "https://test.payu.in/merchant/postservice?form=2"

  payload = {
      "key": "JPM7Fg",
      "command": "si_transaction",
      "var1": '{"authpayuid":"6611192557","amount":"100.00","txnid":"REC15113506209","phone":"9999999999","email":"customer@example.com","firstname":"John","lastname":"Doe","address1":"123 Main Street","city":"Mumbai","state":"Maharashtra","country":"IN","zipcode":"400001","invoiceDisplayNumber":"12345678910","udf1":"ABCDE1234F","udf2":"","udf3":"15-08-1990","udf4":"","udf5":"INV789012"}',
      "hash": "jbUS07Og8BToVZ..."
  }

  headers = {
      "accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
  }

  response = requests.post(url, data=payload, headers=headers)
  print(response.json())
  ```
  ```csharp
  using System;
  using System.Net.Http;
  using System.Collections.Generic;
  using System.Threading.Tasks;

  class Program
  {
      static async Task Main()
      {
          using var client = new HttpClient();
          
          var content = new FormUrlEncodedContent(new[]
          {
              new KeyValuePair<string, string>("key", "JPM7Fg"),
              new KeyValuePair<string, string>("command", "si_transaction"),
              new KeyValuePair<string, string>("var1", "{\"authpayuid\":\"6611192557\",\"amount\":\"100.00\",\"txnid\":\"REC15113506209\",\"phone\":\"9999999999\",\"email\":\"customer@example.com\",\"firstname\":\"John\",\"lastname\":\"Doe\",\"address1\":\"123 Main Street\",\"city\":\"Mumbai\",\"state\":\"Maharashtra\",\"country\":\"IN\",\"zipcode\":\"400001\",\"invoiceDisplayNumber\":\"12345678910\",\"udf1\":\"ABCDE1234F\",\"udf2\":\"\",\"udf3\":\"15-08-1990\",\"udf4\":\"\",\"udf5\":\"INV789012\"}"),
              new KeyValuePair<string, string>("hash", "jbUS07Og8BToVZ...")
          });
          
          var response = await client.PostAsync("https://test.payu.in/merchant/postservice?form=2", content);
          var result = await response.Content.ReadAsStringAsync();
          Console.WriteLine(result);
      }
  }
  ```
  ```javascript
  const executeRecurringPayment = async () => {
      const url = "https://test.payu.in/merchant/postservice?form=2";
      
      const params = new URLSearchParams();
      params.append("key", "JPM7Fg");
      params.append("command", "si_transaction");
      params.append("var1", JSON.stringify({
          authpayuid: "6611192557",
          amount: "100.00",
          txnid: "REC15113506209",
          phone: "9999999999",
          email: "customer@example.com",
          firstname: "John",
          lastname: "Doe",
          address1: "123 Main Street",
          city: "Mumbai",
          state: "Maharashtra",
          country: "IN",
          zipcode: "400001",
          invoiceDisplayNumber: "12345678910",
          udf1: "ABCDE1234F",
          udf2: "",
          udf3: "15-08-1990",
          udf4: "",
          udf5: "INV789012"
      }));
      params.append("hash", "jbUS07Og8BToVZ...");
      
      const response = await fetch(url, {
          method: "POST",
          headers: {
              "accept": "application/json",
              "Content-Type": "application/x-www-form-urlencoded"
          },
          body: params
      });
      
      const data = await response.json();
      console.log(data);
  };

  executeRecurringPayment();
  ```
  ```java
  import java.io.*;
  import java.net.*;
  import java.nio.charset.StandardCharsets;

  public class RecurringPaymentTransaction {
      public static void main(String[] args) throws Exception {
          String url = "https://test.payu.in/merchant/postservice?form=2";
          
          String params = "key=JPM7Fg" +
              "&command=si_transaction" +
              "&var1=" + URLEncoder.encode("{\"authpayuid\":\"6611192557\",\"amount\":\"100.00\",\"txnid\":\"REC15113506209\",\"phone\":\"9999999999\",\"email\":\"customer@example.com\",\"firstname\":\"John\",\"lastname\":\"Doe\",\"address1\":\"123 Main Street\",\"city\":\"Mumbai\",\"state\":\"Maharashtra\",\"country\":\"IN\",\"zipcode\":\"400001\",\"invoiceDisplayNumber\":\"12345678910\",\"udf1\":\"ABCDE1234F\",\"udf2\":\"\",\"udf3\":\"15-08-1990\",\"udf4\":\"\",\"udf5\":\"INV789012\"}", StandardCharsets.UTF_8) +
              "&hash=jbUS07Og8BToVZ...";
          
          HttpURLConnection conn = (HttpURLConnection) new URL(url).openConnection();
          conn.setRequestMethod("POST");
          conn.setRequestProperty("accept", "application/json");
          conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
          conn.setDoOutput(true);
          
          try (OutputStream os = conn.getOutputStream()) {
              os.write(params.getBytes(StandardCharsets.UTF_8));
          }
          
          try (BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()))) {
              String line;
              while ((line = br.readLine()) != null) {
                  System.out.println(line);
              }
          }
      }
  }
  ```
  ```php
  <?php
  $url = "https://test.payu.in/merchant/postservice?form=2";

  $data = array(
      "key" => "JPM7Fg",
      "command" => "si_transaction",
      "var1" => json_encode(array(
          "authpayuid" => "6611192557",
          "amount" => "100.00",
          "txnid" => "REC15113506209",
          "phone" => "9999999999",
          "email" => "customer@example.com",
          "firstname" => "John",
          "lastname" => "Doe",
          "address1" => "123 Main Street",
          "city" => "Mumbai",
          "state" => "Maharashtra",
          "country" => "IN",
          "zipcode" => "400001",
          "invoiceDisplayNumber" => "12345678910",
          "udf1" => "ABCDE1234F",
          "udf2" => "",
          "udf3" => "15-08-1990",
          "udf4" => "",
          "udf5" => "INV789012"
      )),
      "hash" => "jbUS07Og8BToVZ..."
  );

  $ch = curl_init($url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      "accept: application/json",
      "Content-Type: application/x-www-form-urlencoded"
  ));

  $response = curl_exec($ch);
  curl_close($ch);

  echo $response;
  ?>
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  **Success Response**

  ```json
  {
    "status": 1,
    "message": "Transaction Processed successfully",
    "details": {
      "REC15113506209": {
        "transactionid": "REC15113506209",
        "amount": "100.00",
        "payuid": "6611427463",
        "status": "captured",
        "field9": "Transaction Completed Successfully",
        "phone": "9999999999",
        "email": "customer@example.com",
        "udf1": "ABCDE1234F",
        "udf2": "",
        "udf3": "15-08-1990",
        "udf4": "",
        "udf5": "INV789012"
      }
    }
  }
  ```

  **Failure Responses**

  | Scenario                    | Response                                                                                                                                                            |
  | :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  | Invalid Hash                | `{"status": 0, "msg": "Invalid Hash."}`                                                                                                                             |
  | Basic Authentication Failed | `{"status": 1, "message": "Transaction Processed successfully", "details": {"REC9812123123": {"status": "failed", "field9": "Basic authentication check failed"}}}` |
  | Invalid Country             | `{"status": 0, "message": "Invalid country. Only 'IN' or 'India' is allowed."}`                                                                                     |
  | Missing Mandatory Fields    | `{"status": 0, "message": "Missing mandatory field: firstname/lastname/address1/city/state/country/zipcode"}`                                                       |
</Accordion>

<Callout icon="📘" theme="info">
  ### **Transaction Status Values**

  | Status      | Description                                                                  |
  | :---------- | :--------------------------------------------------------------------------- |
  | captured    | Transaction successful                                                       |
  | pending     | Payment initiated with bank/NPCI. Final status will be notified via webhook. |
  | failed      | Transaction failed                                                           |
  | in-progress | Transaction is being processed                                               |
</Callout>

## UPI Sequencing

You may attempt multiple pre-debits and executions simultaneously in certain scenarios. To address such scenarios, **mandateSeqNo** field in var1 parameter in the **Pre Debit Notification** API and **Recurring Payment** API.

<Callout icon="📘" theme="info">
  **Note**: The UPI Sequencing is only applicable for UPI autopay transactions.
</Callout>

A sequence is posted based on Mandate creation. When consent is taken, the first execution is carried out in real-time, and the execution sequence is set to 1. The subsequent pre-debit will start from 2.

### Sample Request/Response for Pre-Debit Notification API

<Accordion title="Sample request" icon="fa-code">
  ```curl
    curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data 'form=2&key=smsplus&command=pre_debit_si&var1={"authpayuid": "25600438037", "requestId": "REQ-2024-001-SEQ2", "debitDate": "2024-12-20", "amount": "100.00", "invoiceDisplayNumber": "INV-12345", "mandateSeqNo": 2}&hash=d9e184476637002a3c2db99a7324673647a313de96e574b7a9812e99153dc1a47f0f9da9b32e3a7382bb46dce09a5eb8d4471c85e1bfc1b0dac380a67ff07b43'
  ```
</Accordion>

<Accordion title="Response in various scenarios" icon="fa-code">
  | Scenario                 | Response Payload                                                                                                                       |
  | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
  | **Success Cases**        |                                                                                                                                        |
  | Successful Pre-debit     | `{"status":1,"action":"MANDATE_PRE_DEBIT","message":"Request Processed Successfully"}`                                                 |
  | _Failure Scenarios_\*    |                                                                                                                                        |
  | Invalid mandateSeqNo     | `{"status":0,"message":"Invalid value for mandateSeqNo","action":"MANDATE_PRE_DEBIT"}`                                                 |
  | Duplicate Pre-debit      | `{"status":"E9254","action":"MANDATE_PRE_DEBIT","message":"Predebit notification already sent for the mandate sequence no.:2"}`        |
  | Execution Already Exists | `{"status":"E9256","action":"MANDATE_PRE_DEBIT","message":"Execution already sent for the mandate sequence no.:2"}`                    |
  | Too Far in Advance       | `{"status":"E9260","action":"MANDATE_PRE_DEBIT","message":"Predebit notification can only be sent for a maximum 30 days in advance."}` |
  | Incorrect Time Period    | `{"status":"E9263","action":"MANDATE_PRE_DEBIT","message":"Predebit for calculated sequence sent during incorrect period"}`            |
  | Mandate Revoked          | `{"status":"QC","action":"MANDATE_PRE_DEBIT","message":"MANDATE HAS BEEN REVOKED"}`                                                    |
  | Mandate Not Active       | `{"status":0,"action":"MANDATE_PRE_DEBIT","message":"Mandate is not active"}`                                                          |
</Accordion>

### Sample Request/Response for Recurring Payment API

<Accordion title="Sample request" icon="fa-flask">
  ```curl
    curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data 'form=2&key=smsplus&command=si_transaction&var1={"authpayuid": "25600438037", "invoiceDisplayNumber": "INV-12345", "amount": "100.00", "txnid": "TXN-2024-001-SEQ2", "phone": "9999999999", "email": "customer@example.com", "mandateSeqNo": 2}&hash=23a6d57370cc2b2c36a7a8ff3b0894a4309a153586544399155d29fe7dc2599cbcf74519d7bc3c8da1e407a874f2c953e05704279e770332db187d1c7b0cbb4d'
  ```
</Accordion>

<Accordion title="Response in various scenarios" icon="fa-flask">
  # Table 3: Scenarios and Response Payloads

  | Scenario                | Response Payload                                                                                                                                |                              |
  | :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------- |
  | **Success Cases**       |                                                                                                                                                 |                              |
  | Transaction In Progress | \`\{"status":1,"message":"Transaction Processed successfully","details":\{...,"status":"in progress","field9":"92\\                             | Transaction Initiated"\}\}\` |
  | Transaction Captured    | `{"status":1,"message":"Transaction Processed successfully","details":{...,"status":"captured","field9":"Transaction Completed Successfully"}}` |                              |
  | **Transaction Errors**  |                                                                                                                                                 |                              |
  | Authentication Failed   | `{"status":1,"message":"Transaction Processed successfully","details":{...,"status":"failed","field9":"Basic authentication check failed"}}`    |                              |
  | Invalid Hash            | `{"status":0,"msg":"Invalid Hash."}`                                                                                                            |                              |
</Accordion>

***

## Additional Resources

• **[Manage UPI Recurring Transaction](https://docs.payu.in/reference/api-commands-to-manage-upi-recurring-transaction)** - UPI recurring payment management
• **[SI Parameter JSON Details](https://docs.payu.in/reference/si-parameter-json-details)** - Detailed subscription parameter specifications
• **[RBI Guidelines](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0)** - Regulatory compliance information

<br />