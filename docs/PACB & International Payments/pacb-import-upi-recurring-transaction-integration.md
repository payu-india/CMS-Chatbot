---
title: PACB Import - UPI Recurring Transaction Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Developer integration required: server-to-server API</Banner>

After the customer has registered a mandate with a [consent transaction](/docs/post-an-upi-consent-transaction-cb), charge it with these steps:

<Cards columns="2">
  <Card title="1. Send the Pre-Debit Notification" href="#step-1-send-the-pre-debit-notification">
    Tell the customer about the upcoming debit.
  </Card>

  <Card title="2. Post the Recurring Payment" href="#step-2-post-the-recurring-payment-transaction">
    Debit the mandate.
  </Card>

  <Card title="3. Update Invoice ID (Optional)" href="#step-3-update-invoice-id-optional">
    Add the invoice details if you didn't send them.
  </Card>

  <Card title="4. Upload the Invoices" href="#step-4-upload-the-invoices">
    Required within 10 days of the payment.
  </Card>
</Cards>

***

## Step 1: Send the Pre-Debit Notification

Send the pre-debit notification at least 48 hours before the actual debit, so the customer is told about it. For more information, refer to [Pre-Debit Notification API](ref:pre_debit_notification_api).

{/* REVIEW (C17): Confluence (UPI-1305) enforces a minimum 24-hour gap between the pre-debit notification and the recurring debit, and the recurring amount must match the pre-debit amount. Confirm whether 48 hours is a cross-border-specific rule. */}

<Accordion title="Environment" icon="fa-server">
  | Environment | URL                                                    |
  | ----------- | ------------------------------------------------------ |
  | Test        | `https://test.payu.in/merchant/postservice.php?form=2` |
  | Production  | `https://info.payu.in/merchant/postservice.php?form=2` |
</Accordion>

<Accordion title="Sample request" icon="fa-upload">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
  --form 'key="9uMuDK"' \
  --form 'command="pre_debit_SI"' \
  --form 'var1="{\"authPayuId\":\"403993715534484661\",\"requestId\":\"403993715534484661_1\",\"debitDate\":\"2026-11-06\",\"amount\":\"2.00\"}"' \
  --form 'hash="YOUR_GENERATED_HASH"'
  ```

  The hash is `sha512(key|command|var1|salt)`.
</Accordion>

<Accordion title="Sample response" icon="fa-download">
  **Success**

  ```json
  {
    "status": 1,
    "action": "MANDATE_PRE_DEBIT",
    "message": "Request Processed Successfully",
    "invoiceId": "ADDA049409"
  }
  ```

  **Failure: the mandate is active at PayU, but the bank or NPCI declined the pre-debit**

  `status` contains the bank or NPCI error code, and `message` its description.

  ```json
  {
    "status": "QC",
    "action": "MANDATE_PRE_DEBIT",
    "message": "MANDATE HAS BEEN REVOKED"
  }
  ```

  **Failure: the mandate is already paused or revoked at PayU**

  `message` changes depending on the reason.

  ```json
  {
    "status": 0,
    "action": "MANDATE_PRE_DEBIT",
    "message": "Mandate is not active"
  }
  ```
</Accordion>

***

## Step 2: Post the Recurring Payment Transaction

Debit the mandate with the Recurring Payment Transaction API. Include the cross-border UDFs inside the `var1` object. For more information, refer to <Anchor target="_blank" href="ref:recurring_payment_api">Recurring Payment Transaction API</Anchor>.

<Accordion title="Environment" icon="fa-server">
  | Environment | URL                                                    |
  | ----------- | ------------------------------------------------------ |
  | Test        | `https://test.payu.in/merchant/postservice.php?form=2` |
  | Production  | `https://info.payu.in/merchant/postservice.php?form=2` |
</Accordion>

<Tabs>
  <Tab title="Request Parameters">

#### Mandatory Parameters

| Parameter                 | Type          | Description                                                                                                                                            | Example                    |
| ------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| <Glossary>key</Glossary>  | `String`      | Merchant key provided by PayU.                                                                                                                         | `rjQUPktU`                 |
| `command`                 | `String`      | API command. Use `si_transaction`.                                                                                                                     | `si_transaction`           |
| `var1`                    | `JSON String` | The recurring payment details: `authpayuid`, `invoiceDisplayNumber`, `amount`, `txnid`, `phone`, `email` and `udf1`–`udf5`. See the fields below.      | See the sample request     |
| <Glossary>hash</Glossary> | `String`      | SHA-512 hash of `key\|command\|var1\|salt`.                                                                                                            | `YOUR_GENERATED_HASH`      |
| `var1.authpayuid`         | `String`      | PayU ID (`mihpayid`) of the successful consent transaction.                                                                                            | `403993715534484661`       |
| `var1.amount`             | `String`      | Amount to debit.                                                                                                                                       | `2.00`                     |
| `var1.txnid`              | `String`      | Unique transaction ID that you generate for this debit.                                                                                                | `Rec_403993715534484661_1` |
| `var1.phone`              | `String`      | Customer's phone number. Returned in the response.                                                                                                     | `9876543210`               |
| `var1.email`              | `String`      | Customer's email address.                                                                                                                              | `customer@example.com`     |
| `var1.udf1`               | `String`      | Buyer's PAN and date of birth, separated by two pipes: `PAN\|\|DOB`.{/* REVIEW (C16): the consent page uses 22/08/1972; this page uses 1990-01-15. */} | `ABCDE1234F\|\|1990-01-15` |
| `var1.udf3`               | `String`      | Invoice ID and seller name (for the reseller use case), separated by two pipes: `invoice_id\|\|sellerName`.                                            | `INV-789\|\|SellerName`    |

#### Optional Parameters

| Parameter                   | Type     | Description                                      | Example             |
| --------------------------- | -------- | ------------------------------------------------ | ------------------- |
| `var1.invoiceDisplayNumber` | `String` | Invoice number to show to the customer.          | `INV-2026-001`      |
| `var1.udf2`                 | `String` | Any extra information. Returned in the response. | `additional_info_2` |
| `var1.udf5`                 | `String` | Any extra information. Returned in the response. | `additional_info_5` |

\> **Note:** Do **not** send `var1.udf4` for UPI Autopay.

<Callout icon="📘" theme="info">
  ### **Note**

In `udf1` and `udf3`:

\- If the first value is missing, send `NULL||<VALUE>`.
\- If the second value is missing, send `<VALUE>||NULL`.

{/* REVIEW: the draft's rule for a missing second value was garbled ("\ \<VALUE>"). Confirm the format. */}

</Callout>

#### Hashing

<Accordion title="Sample Code for Hashing" icon="far fa-code">
  <HashingSample />
</Accordion>

  </Tab>

  <Tab title="Sample Request">
```curl
curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=9uMuDK' \
--data-urlencode 'command=si_transaction' \
--data-urlencode 'var1={"authpayuid":"403993715534484661","invoiceDisplayNumber":"INV-2026-001","amount":"2.00","txnid":"Rec_403993715534484661_1","phone":"9876543210","email":"customer@example.com","udf1":"ABCDE1234F||1990-01-15","udf2":"","udf3":"INV-789||SellerName","udf5":""}' \
--data-urlencode 'hash=YOUR_GENERATED_HASH'
```
```python
import hashlib
import os
import requests

KEY = "9uMuDK"
SALT = os.environ["PAYU_SALT"]  # Keep the salt on your server only
url = "https://test.payu.in/merchant/postservice.php?form=2"

var1 = ('{"authpayuid":"403993715534484661","invoiceDisplayNumber":"INV-2026-001",'
        '"amount":"2.00","txnid":"Rec_403993715534484661_1","phone":"9876543210",'
        '"email":"customer@example.com","udf1":"ABCDE1234F||1990-01-15","udf2":"",'
        '"udf3":"INV-789||SellerName","udf5":""}')
command = "si_transaction"
hash_value = hashlib.sha512(f"{KEY}|{command}|{var1}|{SALT}".encode("utf-8")).hexdigest()

form_data = {"key": KEY, "command": command, "var1": var1, "hash": hash_value}
headers = {"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

try:
    response = requests.post(url, headers=headers, data=form_data, timeout=30)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```
```javascript
const crypto = require("crypto");

const KEY = "9uMuDK";
const SALT = process.env.PAYU_SALT; // Keep the salt on your server only
const url = "https://test.payu.in/merchant/postservice.php?form=2";

const var1 = JSON.stringify({
  authpayuid: "403993715534484661",
  invoiceDisplayNumber: "INV-2026-001",
  amount: "2.00",
  txnid: "Rec_403993715534484661_1",
  phone: "9876543210",
  email: "customer@example.com",
  udf1: "ABCDE1234F||1990-01-15",
  udf2: "",
  udf3: "INV-789||SellerName",
  udf5: "",
});
const command = "si_transaction";
const hash = crypto.createHash("sha512").update(`${KEY}|${command}|${var1}|${SALT}`).digest("hex");

(async () => {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: { accept: "application/json", "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({ key: KEY, command, var1, hash }),
    });
    console.log(`Status: ${response.status}`);
    console.log(`Response: ${await response.text()}`);
  } catch (error) {
    console.error("Error:", error);
  }
})();
```
```java
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class PayURecurringPayment {
    public static void main(String[] args) throws Exception {
        String url = "https://test.payu.in/merchant/postservice.php?form=2";

        Map<String, String> formData = new LinkedHashMap<>();
        formData.put("key", "9uMuDK");
        formData.put("command", "si_transaction");
        formData.put("var1", "{\"authpayuid\":\"403993715534484661\",\"invoiceDisplayNumber\":\"INV-2026-001\",\"amount\":\"2.00\",\"txnid\":\"Rec_403993715534484661_1\",\"phone\":\"9876543210\",\"email\":\"customer@example.com\",\"udf1\":\"ABCDE1234F||1990-01-15\",\"udf2\":\"\",\"udf3\":\"INV-789||SellerName\",\"udf5\":\"\"}");
        formData.put("hash", "YOUR_GENERATED_HASH"); // sha512(key|command|var1|salt), generated on your server

        String formBody = formData.entrySet().stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                    + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create(url))
            .timeout(Duration.ofSeconds(30))
            .header("accept", "application/json")
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formBody))
            .build();

        HttpResponse<String> response = HttpClient.newHttpClient()
            .send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        string url = "https://test.payu.in/merchant/postservice.php?form=2";
        client.DefaultRequestHeaders.Add("accept", "application/json");

        var formData = new List<KeyValuePair<string, string>>
        {
            new KeyValuePair<string, string>("key", "9uMuDK"),
            new KeyValuePair<string, string>("command", "si_transaction"),
            new KeyValuePair<string, string>("var1", "{\"authpayuid\":\"403993715534484661\",\"invoiceDisplayNumber\":\"INV-2026-001\",\"amount\":\"2.00\",\"txnid\":\"Rec_403993715534484661_1\",\"phone\":\"9876543210\",\"email\":\"customer@example.com\",\"udf1\":\"ABCDE1234F||1990-01-15\",\"udf2\":\"\",\"udf3\":\"INV-789||SellerName\",\"udf5\":\"\"}"),
            new KeyValuePair<string, string>("hash", "YOUR_GENERATED_HASH") // sha512(key|command|var1|salt)
        };

        try
        {
            HttpResponseMessage response = await client.PostAsync(url, new FormUrlEncodedContent(formData));
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response: {await response.Content.ReadAsStringAsync()}");
        }
        catch (HttpRequestException e)
        {
            Console.WriteLine($"Error: {e.Message}");
        }
    }
}
```
```php
<?php
$key = '9uMuDK';
$salt = getenv('PAYU_SALT'); // Keep the salt on your server only
$url = 'https://test.payu.in/merchant/postservice.php?form=2';

$var1 = json_encode([
    'authpayuid' => '403993715534484661',
    'invoiceDisplayNumber' => 'INV-2026-001',
    'amount' => '2.00',
    'txnid' => 'Rec_403993715534484661_1',
    'phone' => '9876543210',
    'email' => 'customer@example.com',
    'udf1' => 'ABCDE1234F||1990-01-15',
    'udf2' => '',
    'udf3' => 'INV-789||SellerName',
    'udf5' => '',
]);
$command = 'si_transaction';
$hash = hash('sha512', "$key|$command|$var1|$salt");

$ch = curl_init();
curl_setopt_array($ch, [
    CURLOPT_URL => $url,
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => http_build_query(['key' => $key, 'command' => $command, 'var1' => $var1, 'hash' => $hash]),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => ['accept: application/json', 'Content-Type: application/x-www-form-urlencoded'],
    CURLOPT_TIMEOUT => 30,
]);
$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$error = curl_error($ch);
curl_close($ch);

echo $error ? "cURL Error: $error" . PHP_EOL : "Status Code: $httpCode" . PHP_EOL . "Response: $response" . PHP_EOL;
```
  </Tab>

</Tabs>

<Accordion title="Sample response" icon="fa-reply">
  **Success**

  This is the response when the debit succeeds.

  ```json
  {
    "status": 1,
    "message": "Transaction Processed successfully",
    "details": {
      "Rec_403993715534484661_1": {
        "transactionid": "Rec_403993715534484661_1",
        "amount": "2.00",
        "payuid": "6611427463",
        "status": "captured",
        "field9": "Transaction Completed Successfully",
        "phone": "9876543210",
        "email": "customer@example.com",
        "udf2": "",
        "udf3": "INV-789||SellerName",
        "udf4": "",
        "udf5": ""
      }
    }
  }
  ```

  **Failure: invalid hash**

  ```json
  {
    "status": 0,
    "msg": "Invalid Hash."
  }
  ```

  **Failure: basic authentication check failed**

  ```json
  {
    "status": 1,
    "message": "Transaction Processed successfully",
    "details": {
      "REC9812123123": {
        "authpayuid": "6611192559",
        "transactionid": "REC9812123123",
        "amount": "1",
        "user_credentials": " ",
        "card_token": " ",
        "payuid": "",
        "status": "failed",
        "field9": "Basic authentication check failed",
        "phone": "",
        "email": ""
      }
    }
  }
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  **Fields in&#x20;**`details`

  | Field           | Description                                                                                 |
  | --------------- | ------------------------------------------------------------------------------------------- |
  | `transactionid` | Your transaction ID for this debit, returned as sent.                                       |
  | `amount`        | The amount you requested.                                                                   |
  | `payuid`        | PayU's ID for this recurring transaction. Use it as the reference in the settlement report. |
  | `status`        | Transaction status. See below.                                                              |
  | `field9`        | Description of the status, which you can use in customer communication.                     |
  | `phone`         | Customer's phone number, returned as sent.                                                  |
  | `email`         | Customer's email address, returned as sent.                                                 |
  | `udf1`–`udf5`   | The values you sent, returned as sent.                                                      |

  ### The status field

  Map your order status from this field only. Possible values:

  - **captured:** the payment succeeded. In some cases, NetBanking recurring payments are captured in real time (ICICI Bank in specific scenarios).
  - **pending:** common for most NetBanking (except ICICI in specific scenarios) and UPI recurring payments. Treat it as a successful start of the payment with the bank or NPCI. PayU notifies you when the bank finishes processing.
    - For UPI, `pending` usually changes to `captured` or `failed` within 10 minutes. You can query the status 10 minutes after you started the payment.
    - For NetBanking, `pending` can change to `captured` or `failed` any time from the same day up to T+2, depending on the customer's bank. You can query it once a day, up to T+2.
  - **failed:** treat `failed` or a blank value as a failed transaction.
  - **in-progress:** the transaction is still being processed.

  To get the final status of a `pending` transaction, set up a webhook or call the `verify_payment` API at regular intervals:

  - Webhooks: refer to [Webhooks](doc:webhooks).
  - `verify_payment` API: refer to [Verify Payment API](ref:verify_payment_api).

  <Callout icon="📘" theme="info">
    ### **Note**

    For UPI, call the **verify_settlement** API 10 minutes after you start the payment. For NetBanking, you can call it once a day, up to T+2.

    {/* REVIEW (C24): this note says verify_settlement, but the text above says verify_payment. Confirm which API to use. */}
  </Callout>
</Accordion>

***

## Step 3: Update Invoice ID (Optional)

If you didn't have the invoice details when you sent the [consent transaction](/docs/post-an-upi-consent-transaction-cb), add them with the UDF Update API.

For UPI Autopay, send the PAN and date of birth in `var2` (udf1) and the invoice ID and merchant name in `var4` (udf3). Don't send udf4.

<GENERALAPIsEnvironment />

<Accordion title="Sample request for UPI Autopay" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
  --form 'key="PRiQvJ"' \
  --form 'command="udf_update"' \
  --form 'var1="my_order_64240"' \
  --form 'var2="AAAPZ1234C||22/08/1972"' \
  --form 'var4="INV-123_1231||MerchantName"' \
  --form 'hash="YOUR_GENERATED_HASH"'
  ```

  | Field  | What it contains                                   |        |                |
  | ------ | -------------------------------------------------- | ------ | -------------- |
  |        |                                                    | `var1` | Transaction ID |
  | `var2` | udf1: buyer's PAN and date of birth, as \`PAN      |        | DOB\`          |
  | `var4` | udf3: invoice ID and merchant name, as \`InvoiceID |        | MerchantName\` |
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ### Success

{/* REVIEW: replace with a real UPI Autopay UDF Update response. The Confluence sample response doesn't match its request. */}

```json
{
  "status": "UDF values updated",
  "transaction_id": "my_order_64240",
  "udf1": "AAAPZ1234C||22/08/1972",
  "udf2": "",
  "udf3": "INV-123_1231||MerchantName",
  "udf4": "",
  "udf5": ""
}
```

### Failure

**The transaction ID is missing**

```json
{
  "status": 0,
  "msg": "Parameter missing"
}
```

**The transaction ID is invalid**

```json
{
  "status": 0,
  "msg": "Invalid TXN ID"
}
```

**The hash is invalid**

```json
{
  "status": 0,
  "msg": "Invalid Hash."
}
```

**UDF updates aren't enabled for your account**

```json
{
  "status": "0",
  "msg": "Update not allowed on provided Field"
}
```

**No data found for the transaction ID**

```json
{
  "status": "0",
  "msg": "No Data Found for txnid: 3424"
}
```

**Your account is inactive**

```json
{
  "msg": "Merchant is not authorized to use PayU API",
  "status": 0
}
```

</Accordion>

***

## Step 4: Upload the Invoices

<Callout icon="🚧" theme="warn">
  ### **Watch Out!**

  - Upload the invoice within **10 days** of the transaction. If you don't, your next settlement is put on hold.
  - Goods merchants must upload the invoice and the airway bill (AWB) separately: set `var3` to `Invoice` for one call and `AWB` for the other.
</Callout>

<GENERALAPIsEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
  --form 'key="YOUR_MERCHANT_KEY"' \
  --form 'command="opgsp_upload_invoice_awb"' \
  --form 'var1="403993715525825059"' \
  --form 'var2="TestInv0001234568"' \
  --form 'var3="Invoice"' \
  --form 'file=@"/path/to/file"' \
  --form 'hash="YOUR_GENERATED_HASH"'
  ```

  | Field  | What it contains                  |
  | ------ | --------------------------------- |
  | `var1` | PayU ID (`mihpayid`)              |
  | `var2` | Invoice ID                        |
  | `var3` | Document type: `Invoice` or `AWB` |
  | `file` | The file to upload                |
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  <Accordion title="Success" icon="fa-check-circle">
    **The file was uploaded**

    ```json
    {
      "responseCode": "00",
      "responseMsg": "File Uploaded Successfully"
    }
    ```
  </Accordion>

  <Accordion title="Failure" icon="fa-exclamation-triangle">
    **The upload failed**

    ```json
    {
      "responseCode": "103",
      "responseMsg": "Failed to Upload"
    }
    ```

    **Your account isn't enabled for cross-border payments**

    ```json
    {
      "responseCode": "105",
      "responseMsg": "Not an PACB merchant, contact KAM"
    }
    ```

    **The PayU ID is invalid**

    ```json
    {
      "responseCode": "107",
      "responseMsg": "The PayuID in request is invalid"
    }
    ```

    **A mandatory field is missing**

    ```json
    {
      "responseCode": "109",
      "responseMsg": "All fields are mandatory, please check!"
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="Response codes and descriptions" icon="fa-list">
  Refer to [Response Code and Description - Invoice Upload API](ref:response-code-and-description-invoice-upload-api).
</Accordion>

***

## Next Steps

<Cards columns="2">
  <Card title="Post a UPI Consent Transaction" href="/docs/post-an-upi-consent-transaction-cb">
    Register another mandate.
  </Card>

  <Card title="FAQs" href="/docs/faqs-for-cross-border-payments">
    Answers about UDFs, invoices and settlement.
  </Card>
</Cards>
