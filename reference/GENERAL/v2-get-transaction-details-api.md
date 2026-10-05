---
title: Get Transaction Details API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Get Transaction Details API
deprecated: false
hidden: false
metadata:
  title: Get Transaction Details API
  description: >-
    The Get Transaction Details API retrieves transaction details between two
    specified dates with pagination support, including transaction status,
    amount, payment method, customer details, and lifecycle actions such as capture and refund.
  robots: index
---

The **Get Transaction Details** API retrieves transaction records processed by PayU between a given start date and end date. The response includes transaction status, net amount, payment mode, customer profile, and associated lifecycle actions (such as capture and refund). Results are returned in a paginated array format.

HTTP Method: **POST**

**Environment**

| Environment | URL |
| :--- | :--- |
| **Test Environment** | `https://test.payu.in/v4/reporting/transactions` |
| **Production Environment** | `https://info.payu.in/v4/reporting/transactions` |

## Request Headers

<V2_payment_header_params />

| Header | Type | Description |
| :--- | :--- | :--- |
| `Content-Type` | String | Must be set to `application/json`. |
| `Accept` | String | Must be set to `application/json`. |
| `Date` | String | Current GMT timestamp (e.g. `Tue, 12 Aug 2025 16:44:30 GMT`). |
| `Digest` | String | Base64-encoded SHA-256 hash of the JSON payload. |
| `Authorization` | String | HMAC authorization header containing merchant key and computed signature. |

## Request Body Parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>`pageNumber`<br/>`mandatory`</td>
      <td>`Number` The page number to retrieve. Use `1` for the first page and increment for subsequent pages.</td>
      <td>`1`</td>
    </tr>
    <tr>
      <td>`startDate`<br/>`mandatory`</td>
      <td>`String` The start date for the transaction search in `YYYY-MM-DD` format.</td>
      <td>`2025-08-11`</td>
    </tr>
    <tr>
      <td>`endDate`<br/>`mandatory`</td>
      <td>`String` The end date for the transaction search in `YYYY-MM-DD` format.</td>
      <td>`2025-08-11`</td>
    </tr>
    <tr>
      <td>`totalRecord`<br/>`mandatory`</td>
      <td>`Number` The total number of records requested per query batch.</td>
      <td>`50`</td>
    </tr>
  </tbody>
</Table>

## Sample Request

```bash
curl --location 'https://info.payu.in/v4/reporting/transactions' \
--header 'Accept: application/json' \
--header 'Authorization: hmac username="<YOUR_MERCHANT_KEY>", algorithm="hmac-sha256", headers="date digest", signature="{{signature}}"' \
--header 'Digest: {{digest}}' \
--header 'Date: Tue, 12 Aug 2025 16:44:30 GMT' \
--header 'Content-Type: application/json' \
--data '{
  "pageNumber": 1,
  "startDate": "2025-08-11",
  "endDate": "2025-08-11",
  "totalRecord": 50
}'
```
```python
import requests
import json

url = "https://info.payu.in/v4/reporting/transactions"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Date": "Tue, 12 Aug 2025 16:44:30 GMT",
    "Digest": "YOUR_DIGEST",
    "Authorization": "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"YOUR_SIGNATURE\""
}

payload = {
    "pageNumber": 1,
    "startDate": "2025-08-11",
    "endDate": "2025-08-11",
    "totalRecord": 50
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```
```php
<?php
$url = "https://info.payu.in/v4/reporting/transactions";

$payload = json_encode([
    "pageNumber" => 1,
    "startDate" => "2025-08-11",
    "endDate" => "2025-08-11",
    "totalRecord" => 50
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json",
    "Accept: application/json",
    "Date: Tue, 12 Aug 2025 16:44:30 GMT",
    "Digest: YOUR_DIGEST",
    "Authorization: hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"YOUR_SIGNATURE\""
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class PayURequest {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        
        String payload = "{\"pageNumber\": 1, \"startDate\": \"2025-08-11\", \"endDate\": \"2025-08-11\", \"totalRecord\": 50}";
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://info.payu.in/v4/reporting/transactions"))
            .header("Content-Type", "application/json")
            .header("Accept", "application/json")
            .header("Date", "Tue, 12 Aug 2025 16:44:30 GMT")
            .header("Digest", "YOUR_DIGEST")
            .header("Authorization", "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"YOUR_SIGNATURE\"")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```
```javascript
const url = "https://info.payu.in/v4/reporting/transactions";

const payload = {
  pageNumber: 1,
  startDate: "2025-08-11",
  endDate: "2025-08-11",
  totalRecord: 50
};

const options = {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Date": "Tue, 12 Aug 2025 16:44:30 GMT",
    "Digest": "YOUR_DIGEST",
    "Authorization": "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"hmac-sha256\", headers=\"date digest\", signature=\"YOUR_SIGNATURE\""
  },
  body: JSON.stringify(payload)
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

## Response Parameters

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `message` | String | Status message describing the API result. | `Success` |
| `status` | Number | Status flag for the API call: `1` for success, `0` for failure. | `1` |
| `currentPage` | Number | Current page index in the paginated response. | `1` |
| `totalRecords` | Number | Total transaction records found for the date range. | `83` |
| `pageSize` | Number | Number of records returned on the current page. | `5` |
| `totalPages` | Number | Total available pages. | `17` |
| `hasNextPage` | Boolean | `true` if more records exist on subsequent pages. | `true` |
| `hasPreviousPage` | Boolean | `true` if previous pages exist. | `false` |
| `result` | Array | Array of transaction objects. | See details below. |

### result[].transactionDetails Object Description

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>`id`</td>
      <td>PayU transaction ID (`mihpayid`).</td>
      <td>`403993715534525267`</td>
    </tr>
    <tr>
      <td>`transactionId`</td>
      <td>Merchant transaction identifier (`txnId`).</td>
      <td>`TXN1754891007637_38614`</td>
    </tr>
    <tr>
      <td>`merchantKey`</td>
      <td>Merchant key associated with the transaction.</td>
      <td>`<YOUR_MERCHANT_KEY>`</td>
    </tr>
    <tr>
      <td>`merchantName`</td>
      <td>Business name of the merchant.</td>
      <td>`Merchant Enterprise`</td>
    </tr>
    <tr>
      <td>`status`</td>
      <td>Status of the payment: `captured`, `failed`, `dropped`, or `bounced`.</td>
      <td>`captured`</td>
    </tr>
    <tr>
      <td>`amount`</td>
      <td>Total transaction amount paid by the customer.</td>
      <td>`1000.00`</td>
    </tr>
    <tr>
      <td>`transactionFee`</td>
      <td>Base transaction amount before surcharges.</td>
      <td>`1000.00`</td>
    </tr>
    <tr>
      <td>`discount`</td>
      <td>Discount amount applied to the payment.</td>
      <td>`0.00`</td>
    </tr>
    <tr>
      <td>`additionalCharges`</td>
      <td>Additional convenience fee or surcharge applied.</td>
      <td>`0.00`</td>
    </tr>
    <tr>
      <td>`mode`</td>
      <td>Payment mode: `CC`, `DC`, `NB`, `UPI`, `CASH` (Wallet), or `EMI`.</td>
      <td>`NB`</td>
    </tr>
    <tr>
      <td>`ibiboCode`</td>
      <td>Bank or payment option code (e.g. `HDFCNB`, `AXISB`, `UPI`).</td>
      <td>`AXNBTPV`</td>
    </tr>
    <tr>
      <td>`bankRefNo`</td>
      <td>Bank reference identifier / UTR.</td>
      <td>`3abaf676-4385-491e-9488-6490672baa42`</td>
    </tr>
    <tr>
      <td>`addedOn`</td>
      <td>Date and time when transaction was initiated (`YYYY-MM-DD HH:MM:SS`).</td>
      <td>`2025-08-11 11:13:30`</td>
    </tr>
    <tr>
      <td>`updatedOn`</td>
      <td>Date and time when transaction was last modified.</td>
      <td>`2025-08-11 11:13:40`</td>
    </tr>
    <tr>
      <td>`productInfo`</td>
      <td>Product description supplied in payment request.</td>
      <td>`Order #12345`</td>
    </tr>
    <tr>
      <td>`firstName`</td>
      <td>Customer first name.</td>
      <td>`Aarav`</td>
    </tr>
    <tr>
      <td>`lastName`</td>
      <td>Customer last name.</td>
      <td>`Sharma`</td>
    </tr>
    <tr>
      <td>`phone`</td>
      <td>Customer mobile number.</td>
      <td>`9876543210`</td>
    </tr>
    <tr>
      <td>`email`</td>
      <td>Customer email address.</td>
      <td>`aarav.sharma@example.com`</td>
    </tr>
    <tr>
      <td>`cardNo`</td>
      <td>Masked card number (for card payments).</td>
      <td>`XXXXXXXXXXXX4242`</td>
    </tr>
    <tr>
      <td>`cardType`</td>
      <td>Card network type (`VISA`, `MAST`, `AMEX`, `RUPAY`).</td>
      <td>`VISA`</td>
    </tr>
    <tr>
      <td>`cardToken`</td>
      <td>Card token identifier if a saved card was used.</td>
      <td>`tok_card_12345`</td>
    </tr>
    <tr>
      <td>`udf1` to `udf5`</td>
      <td>User-defined metadata fields passed in payment initiation.</td>
      <td>`custom_val_1`</td>
    </tr>
    <tr>
      <td>`errorCode`</td>
      <td>Status error code. `E000` indicates no error.</td>
      <td>`E000`</td>
    </tr>
    <tr>
      <td>`errorMessage`</td>
      <td>Detailed error explanation from processor or bank.</td>
      <td>`No Error`</td>
    </tr>
  </tbody>
</Table>

### result[].transactionActionDetails Object Description

| Field | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `id` | Number | Unique identifier for the action. | `138492940` |
| `actionType` | String | Type of lifecycle action: `capture` or `refund`. | `capture` |
| `amount` | Number | Amount processed in this action. | `1000.00` |
| `status` | String | Status of the action: `SUCCESS`, `queued`, or `FAILED`. | `SUCCESS` |
| `token` | String | Refund token identifier (if action is `refund`). | `REF_sHGe_906836` |
| `bankRefNo` | String | Bank reference identifier for this action. | `3abaf676-4385-491e-9488` |
| `bankArn` | String | Bank Acquirer Reference Number (ARN) for card refunds. | `123456789012` |
| `refundMode` | String | Refund routing mode (`Back to Source`). | `Back to Source` |
| `createdAt` | String | Timestamp when action was initiated. | `2025-08-11 11:13:40` |
| `updatedAt` | String | Timestamp when action status was updated. | `2025-08-11 11:13:40` |

---

## Sample Response

```json
{
  "message": "Success",
  "status": 1,
  "currentPage": 1,
  "totalRecords": 2,
  "pageSize": 5,
  "totalPages": 1,
  "hasNextPage": false,
  "hasPreviousPage": false,
  "result": [
    {
      "payuId": 403993715534525267,
      "transactionDetails": {
        "id": 403993715534525267,
        "transactionId": "TXN1754891007637_38614",
        "merchantKey": "<YOUR_MERCHANT_KEY>",
        "merchantName": "Merchant Enterprise",
        "status": "captured",
        "discount": 0.00,
        "amount": 1000.00,
        "transactionFee": 1000.00,
        "additionalCharges": 0.00,
        "mode": "NB",
        "firstName": "Aarav",
        "lastName": "Sharma",
        "addedOn": "2025-08-11 11:13:30",
        "updatedOn": "2025-08-11 11:13:40",
        "phone": "9876543210",
        "email": "aarav.sharma@example.com",
        "productInfo": "Order #12345",
        "errorCode": "E000",
        "errorDescription": "No Error",
        "ibiboCode": "AXNBTPV",
        "bankRefNo": "3abaf676-4385-491e-9488-6490672baa42",
        "errorMessage": "No Error",
        "udf1": "meta_1",
        "udf2": "",
        "udf3": "",
        "udf4": "",
        "udf5": ""
      },
      "transactionActionDetails": [
        {
          "id": 138492940,
          "bankRefNo": "3abaf676-4385-491e-9488-6490672baa42",
          "token": "",
          "actionType": "capture",
          "prevStatus": null,
          "amount": 1000.00,
          "status": "SUCCESS",
          "bankArn": null,
          "updatedAt": "2025-08-11 11:13:40",
          "createdAt": "2025-08-11 11:13:40",
          "refundMode": "-"
        }
      ]
    }
  ]
}
```

---

## Response Status & Error Codes

| HTTP Status | Message | Description |
| :--- | :--- | :--- |
| **200 OK** | `Success` | Request processed successfully with matching records. |
| **400 Bad Request** | `Invalid Date Range` | Date range exceeds permissible bounds or invalid date format. |
| **401 Unauthorized** | `Unauthorized` | Invalid merchant credentials, missing digest, or signature mismatch. |
| **500 Server Error** | `Internal Error` | Temporary processing issue on reporting service. |


## Next Steps

1. **Automate Daily Reconciliation**:
   - Ingest transaction records into your internal ERP or accounting systems by querying this endpoint across standard date windows (`startDate` and `endDate`).
2. **Paginate Large Result Sets**:
   - Check `hasNextPage` and increment `pageNumber` until all records for the time range have been processed.
3. **Audit Transaction Lifecycles**:
   - Inspect the `transactionActionDetails` array for each record to reconcile refunds, chargebacks, and partial captures against original order amounts.
