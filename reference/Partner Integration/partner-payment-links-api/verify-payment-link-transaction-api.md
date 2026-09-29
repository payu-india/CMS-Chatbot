---
title: 'Verify Payment Link Transaction API '
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Verify Payment Link Transaction API** enables partners to query the definitive status of an order after a customer completes or cancels their payment via either UPI Intent (`UPI_PL`) or Hosted Checkout (`NON_UPI_PL`).

Always invoke this API before fulfilling services, crediting balances, or confirming orders.

HTTP Method: **GET**

### Endpoints

| Environment    | URL                                                                                |
| :------------- | :--------------------------------------------------------------------------------- |
| **Test**       | `https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment` |
| **Production** | `https://partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment`      |

***

## Sample Request

## Request Headers

| Header          | Type     | Mandatory | Description                                                                                                           |
| :-------------- | :------- | :-------- | :-------------------------------------------------------------------------------------------------------------------- |
| `Authorization` | `string` | **Yes**   | Bearer token obtained from OAuth Token API (`Bearer <access_token>`). Must include the `partner_payment_links` scope. |

***

### Query Parameters

| Parameter         | Type     | Mandatory | Description                                                                                             | Example                           |
| :---------------- | :------- | :-------- | :------------------------------------------------------------------------------------------------------ | :-------------------------------- |
| `order_ref_id`    | `string` | **Yes**   | Unique order reference identifier returned during payment initiation (`/partner/payment-link/payment`). | `28408067218883788`               |
| `payment_link_id` | `string` | **Yes**   | Full canonical PayU payment link URL.                                                                   | `https://v.payu.in/PAYUMN/abc123` |

***

## Sample Request

```curl
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=28408067218883788&payment_link_id=https://v.payu.in/PAYUMN/abc123' \
--header 'Authorization: Bearer your_access_token_here'
```
```python
import requests

url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment"
params = {
    "order_ref_id": "28408067218883788",
    "payment_link_id": "https://v.payu.in/PAYUMN/abc123"
}
headers = {
    "Authorization": "Bearer your_access_token_here"
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```
```javascript
const orderRefId = '28408067218883788';
const paymentLinkId = 'https://v.payu.in/PAYUMN/abc123';
const token = 'your_access_token_here';

const url = `https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=${orderRefId}&payment_link_id=${encodeURIComponent(paymentLinkId)}`;

const response = await fetch(url, {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${token}`
  }
});

const data = await response.json();
console.log(data);
```
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;

public class VerifyPaymentLinkTransaction {
    public static void main(String[] args) {
        try {
            String orderRefId = "28408067218883788";
            String paymentLinkId = URLEncoder.encode("https://v.payu.in/PAYUMN/abc123", StandardCharsets.UTF_8.toString());
            String endpoint = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=" 
                              + orderRefId + "&payment_link_id=" + paymentLinkId;

            URL url = new URL(endpoint);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");
            conn.setRequestProperty("Authorization", "Bearer your_access_token_here");

            BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String inputLine;
            StringBuilder response = new StringBuilder();
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();
            System.out.println(response.toString());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    private static readonly HttpClient client = new HttpClient();

    static async Task Main(string[] args)
    {
        string orderRefId = "28408067218883788";
        string paymentLinkId = Uri.EscapeDataString("https://v.payu.in/PAYUMN/abc123");
        string url = $"https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id={orderRefId}&payment_link_id={paymentLinkId}";

        client.DefaultRequestHeaders.Clear();
        client.DefaultRequestHeaders.Add("Authorization", "Bearer your_access_token_here");

        HttpResponseMessage response = await client.GetAsync(url);
        string result = await response.Content.ReadAsStringAsync();
        Console.WriteLine(result);
    }
}
```
```php
<?php
$orderRefId = "28408067218883788";
$paymentLinkId = urlencode("https://v.payu.in/PAYUMN/abc123");
$url = "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=" . $orderRefId . "&payment_link_id=" . $paymentLinkId;

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Authorization: Bearer your_access_token_here"
]);

$response = curl_exec($ch);
curl_close($ch);
echo $response;
?>
```

***

## Response Parameters

| Parameter                     | Type             | Description                                                                                              |
| :---------------------------- | :--------------- | :------------------------------------------------------------------------------------------------------- |
| `order_ref_id`                | `string`         | Unique order reference identifier originally generated by PayU.                                          |
| `payment_link_id`             | `string`         | Canonical payment link URL associated with this transaction.                                             |
| `order_status`                | `string`         | Overall order status. Possible values: `success`, `failure`, `pending`.                                  |
| `payments`                    | `array`          | List of payment attempts made by the customer against this order reference.                              |
| `payments[].payment_id`       | `string`         | PayU's unique payment transaction identifier (`mihpayid`).                                               |
| `payments[].status`           | `string`         | Outcome of the individual payment attempt: `success` or `failure`.                                       |
| `payments[].method`           | `string`         | Payment mode/instrument utilized (e.g., `UPI`, `CC`, `DC`, `NB`, `CASH`).                                |
| `payments[].pg_error_message` | `string \| null` | Error description returned from the bank or payment gateway. Returns `null` for successful transactions. |

***

## Sampe Response

### Success Scenario
`(`200 OK`)`

```json
{
  "order_ref_id": "28408067218883788",
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "order_status": "success",
  "payments": [
    {
      "payment_id": "123456789",
      "status": "success",
      "method": "UPI",
      "pg_error_message": null
    }
  ]
}
```

### Failure Sceanrios
**Failed Transaction Attempt**
```json
{
  "order_ref_id": "28408067218883788",
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "order_status": "failure",
  "payments": [
    {
      "payment_id": "123456780",
      "status": "failure",
      "method": "UPI",
      "pg_error_message": "Transaction rejected: user entered incorrect UPI PIN"
    }
  ]
}
```
**Pending Transaction**

Returned when the payment attempt is still in progress or awaiting customer confirmation on their UPI app/bank page.

```json
{
  "order_ref_id": "28408067218883788",
  "payment_link_id": "https://v.payu.in/PAYUMN/abc123",
  "order_status": "pending",
  "payments": []
}
```
**Unauthorized Access (`401 Unauthorized`)**

```json
{
  "status": "failed",
  "error": "UNAUTHORIZED",
  "message": "Auth token is not valid"
}
```

**Order Reference or Link Not Found (`404 Not Found`)**

```json
{
  "status": "failed",
  "error": "NOT_FOUND",
  "message": "No transaction found for the provided order_ref_id and payment_link_id"
}
```
