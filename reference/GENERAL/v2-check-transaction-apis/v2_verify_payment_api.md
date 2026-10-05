---
title: Verify Payment API
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
To know the status of the payment, you need to integrate the **Verify Payment** API as below. You need to post the **txnId** sent by the **v2/payments** API in the **txnId** parameter.

HTTP Method: **POST**

**Environment**

|                        |                                                                            |
| :--------------------- | :------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/v3/transaction](https://test.payu.in/v3/transaction) |
| Production Environment | [https://info.payu.in/v3/transaction](https://info.payu.in/v3/transaction) |

## Request parameters

### Request header

<V2_payment_header_params />

### Body parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>txnId<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>You need to post the <strong>txnId</strong> sent by the <strong>v2/payments</strong> API. For more information, refer to any of the following:  </p>
<ul>
<li><a href="https://docs.payu.in/v2/reference/collect-payment-api-payu-hosted-v2-_payment">Collect Payment API - Non-Seamless v2 Payment</a></li>
<li><a href="https://docs.payu.in/v2/reference/v2_payment_seamless_integration">Collect Payment API - Seamless v2 Payment</a></li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>54dzPX68BZzE46Q2VYWw</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```
curl --location 'https://test.payu.in/v3/transaction' \
--header 'Content-Type: application/json' \
--header 'date: <CURRENT_DATE_GMT>' \
--header 'authorization: hmac username="<YOUR_TEST_KEY>", algorithm="sha512", headers="date", signature="<YOUR_SIGNATURE>"' \
--header 'Info-Command: verify_payment' \
--data '{
    "txnId":["512345678901234"]
}'
```
```python
import requests
import json

url = "https://test.payu.in/v3/transaction"

headers = {
    "Content-Type": "application/json",
    "date": "<CURRENT_DATE_GMT>",
    "authorization": 'hmac username="<YOUR_TEST_KEY>", algorithm="sha512", headers="date", signature="<YOUR_SIGNATURE>"',
    "Info-Command": "verify_payment"
}

payload = {
    "txnId": ["512345678901234"]
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print("Status Code:", response.status_code)
print("Response:", response.text)
```
```csharp
using System;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        using HttpClient client = new HttpClient();

        client.DefaultRequestHeaders.Add("date", "<CURRENT_DATE_GMT>");
        client.DefaultRequestHeaders.Add("authorization", "hmac username=\"<YOUR_TEST_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\"");
        client.DefaultRequestHeaders.Add("Info-Command", "verify_payment");

        string jsonBody = "{\"txnId\":[\"512345678901234\"]}";
        StringContent content = new StringContent(jsonBody, Encoding.UTF8, "application/json");

        HttpResponseMessage response = await client.PostAsync("https://test.payu.in/v3/transaction", content);

        Console.WriteLine("Status Code: " + (int)response.StatusCode);
        Console.WriteLine("Response: " + await response.Content.ReadAsStringAsync());
    }
}
```
```javascript
const url = "https://test.payu.in/v3/transaction";

const headers = {
  "Content-Type": "application/json",
  "date": "<CURRENT_DATE_GMT>",
  "authorization": 'hmac username="<YOUR_TEST_KEY>", algorithm="sha512", headers="date", signature="<YOUR_SIGNATURE>"',
  "Info-Command": "verify_payment"
};

const body = JSON.stringify({
  txnId: ["512345678901234"]
});

const response = await fetch(url, {
  method: "POST",
  headers: headers,
  body: body
});

console.log("Status Code:", response.status);
console.log("Response:", await response.text());
```
```java
import java.io.OutputStream;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class Main {
    public static void main(String[] args) throws Exception {
        URL url = new URL("https://test.payu.in/v3/transaction");
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();

        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        conn.setRequestProperty("Content-Type", "application/json");
        conn.setRequestProperty("date", "<CURRENT_DATE_GMT>");
        conn.setRequestProperty("authorization", "hmac username=\"<YOUR_TEST_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\"");
        conn.setRequestProperty("Info-Command", "verify_payment");

        String jsonBody = "{\"txnId\":[\"512345678901234\"]}";
        try (OutputStream os = conn.getOutputStream()) {
            os.write(jsonBody.getBytes("UTF-8"));
        }

        int statusCode = conn.getResponseCode();
        BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        StringBuilder response = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            response.append(line);
        }
        br.close();

        System.out.println("Status Code: " + statusCode);
        System.out.println("Response: " + response.toString());
    }
}
```
```php
<?php

$url = "https://test.payu.in/v3/transaction";

$headers = [
    "Content-Type: application/json",
    "date: <CURRENT_DATE_GMT>",
    'authorization: hmac username="<YOUR_TEST_KEY>", algorithm="sha512", headers="date", signature="<YOUR_SIGNATURE>"',
    "Info-Command: verify_payment"
];

$body = json_encode([
    "txnId" => ["512345678901234"]
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
$statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $statusCode . "\n";
echo "Response: " . $response . "\n";
```

## Response parameters

The fields in the result parameter JSON are described in the following table:

| Field               | Description                                                                                                                          | Example                      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| mihpayId            | Transaction ID is a unique number assigned by PayU for each transaction. Keep note of it for future reference for inquiry or refund. | 21612493009                  |
| bankReferenceNumber | For each successful transaction – this parameter would contain the bank reference number generated by the bank.                      | 2411194544                   |
| amount              | This parameter would contain the actual amount involved in the transaction.                                                          | 0.00                         |
| mode                | This parameter describes the payment mode by which the transaction was completed (e.g., CC for Credit Card).                         | CC                           |
| requestId           | A unique identifier for the request.                                                                                                 |                              |
| originalAmount      | The original transaction amount before applying charges or discounts.                                                                | 100.00                       |
| additionalCharges   | Additional charges, if any, applied to the transaction amount.                                                                       | 0.00                         |
| discount            | Any discount amount applied to the transaction.                                                                                      | 0.00                         |
| netDebitAmount      | Total amount debited from the payer's account after additional charges and discounts.                                                | 100.00                       |
| productInfo         | A brief description of the product or service for which the payment was being made.                                                  | example_product              |
| firstName           | The payer’s first name involved in the transaction.                                                                                  | Example Payer                |
| bankcode            | The code of the bank used for the transaction.                                                                                       | AMEX                         |
| nameOnCard          | Cardholder's name (null if the value is not captured).                                                                               | (null)                       |
| cardNo              | Masked card number for enhanced security.                                                                                            | XXXXXXXXXXXX2001             |
| cardType            | The type of card used, such as AMEX for American Express.                                                                            | AMEX                         |
| udf1 to udf5        | User-defined fields for additional optional data during the transaction process.                                                     | (null)                       |
| field2              | Context-specific information from the bank, such as codes or values relevant to verification.                                        | 140455                       |
| field9              | Describes the status of the transaction.                                                                                             | Transaction is Successful    |
| errorCode           | This parameter provides error code information.                                                                                      | E000                         |
| errorMessage        | Provides a human-readable error message for failed transactions.                                                                     | No Error                     |
| addedOn             | Timestamp when the transaction was initiated.                                                                                        | 2024-11-19 21:17:55          |
| settledAt           | Timestamp when funds were settled.                                                                                                   | 0000-00-00 00:00:00          |
| paymentSource       | The source of payment handling.                                                                                                      | payuS2S                      |
| pgType              | Indicates the type of payment gateway used.                                                                                          | CC-PG                        |
| status              | Displays the overall status of the transaction.                                                                                      | success                      |
| unmappedStatus      | Internal transaction status in PayU’s system, mapped separately.                                                                     | captured                     |
| merchantUTR         | Merchant's Unique Transaction Reference.                                                                                             | (null)                       |
| message             | General status message for the transaction.                                                                                          | Found TxnId                  |
| txnId               | The transaction ID provided by the merchant for tracking purposes.                                                                   | 54dzPX68BZzE46Q2VYWw         |
| rupayAuthRefNo      | Reference ID specific to RuPay Cards.                                                                                                | AAACAVJIggICQyRYdUiCEAAAAAA= |
| authRefNo           | A bank-specific authorization reference number.                                                                                      | AAACAVJIggICQyRYdUiCEAAAAAA= |
| originalCurrency    | The currency used for the transaction.                                                                                               | INR                          |
| threeDSVersion      | Version of the 3D Secure protocol used for securing the transaction.                                                                 | 2.2.0                        |

## Sample response

### Success scenario

Formatted JSON Response:

If successfully fetched:

```plaintext
{
    "message": "Success",
    "status": 1,
    "result": [
        {
            "mihpayId": 21612493009,
            "bankReferenceNumber": "2411194544",
            "amount": 100.00,
            "mode": "CC",
            "requestId": "",
            "originalAmount": 100.00,
            "additionalCharges": 0.00,
            "discount": 0.00,
            "netDebitAmount": 100.00,
            "productInfo": "example_product",
            "firstName": "Example Payer",
            "bankcode": "AMEX",
            "nameOnCard": null,
            "cardNo": "XXXXXXXXXXXX2001",
            "cardType": "AMEX",
            "udf1": null,
            "udf2": null,
            "udf3": null,
            "udf4": null,
            "udf5": null,
            "field2": "140455",
            "field9": "Transaction is Successful",
            "errorCode": "E000",
            "errorMessage": "No Error",
            "addedOn": "2024-11-19 21:17:55",
            "settledAt": "0000-00-00 00:00:00",
            "paymentSource": "payuS2S",
            "pgType": "CC-PG",
            "status": "success",
            "unmappedStatus": "captured",
            "merchantUTR": null,
            "mcpLookupId": null,
            "mcpAmount": null,
            "mcpCurrency": null,
            "mcpExchangeRate": null,
            "rupayAuthRefNo": "AAACAVJIggICQyRYdUiCEAAAAAA=",
            "authRefNo": "AAACAVJIggICQyRYdUiCEAAAAAA=",
            "originalCurrency": "INR",
            "threeDSVersion": "2.2.0",
            "merNetAmount": null,
            "offerAvailed": null,
            "message": "Found TxnId",
            "txnId": "54dzPX68BZzE46Q2VYWw"
        }
    ]
}
```

### Failure scenarios

* Transaction not found

```plaintext
{
    "message": "Success",
    "status": 1,
    "result": [
        {
            "message": "not found",
            "txnId": "Test1235677235455"
        }
    ]
}
```

## Sample Responses

### Success Response

```json
{
  "status": "success",
  "result": {
    "paymentId": "PAY_abc123xyz789",
    "orderId": "ORDER_123",
    "amount": 10000,
    "currency": "INR"
  },
  "message": "Transaction successful"
}
```

### Pending Response

```json
{
  "status": "pending",
  "result": {
    "paymentId": "PAY_pending456",
    "orderId": "ORDER_456",
    "redirectUrl": "https://checkout.payu.in/pay/PAY_pending456"
  },
  "message": "Awaiting completion"
}
```

### Failure Response

```json
{
  "status": "failed",
  "error": {
    "code": "PAYMENT_DECLINED",
    "message": "Declined by bank"
  },
  "result": {
    "paymentId": "PAY_failed789",
    "orderId": "ORDER_789"
  }
}
```

## Error Codes

| Code                    | HTTP Status | Description               | Resolution                        |
| ----------------------- | ----------- | ------------------------- | --------------------------------- |
| `INVALID_AMOUNT`        | 400         | Invalid amount value      | Check amount format and value     |
| `INVALID_CURRENCY`      | 400         | Unsupported currency      | Use supported currency codes      |
| `AUTHENTICATION_FAILED` | 401         | Invalid token             | Verify authentication credentials |
| `DUPLICATE_REFERENCE`   | 409         | Reference ID already used | Use unique reference ID           |
| `PAYMENT_DECLINED`      | 422         | Payment declined          | Try different payment method      |

> For complete error code list, see [Error Codes Reference](ref:error-codes).

## Next Steps

1. **Order Fulfillment**:
   - If `status` is `success`, record the `mihpayId` and `bankReferenceNumber` in your order database and mark the order as **Paid**.
2. **Handle Pending Transactions**:
   - If `status` is `pending`, schedule a background retry queue (e.g. check after 5 mins, 15 mins, and 1 hour) before marking the transaction as failed.
3. **Handle Failed Transactions**:
   - If `status` is `failure`, inspect `errorCode` and `errorMessage` to display user-friendly troubleshooting guidance or allow the customer to retry payment.
4. **Reconciliation**:
   - Match the returned `amount` and `netDebitAmount` against your ledger and bank settlement sheets.
