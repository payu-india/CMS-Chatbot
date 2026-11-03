---
title: Cards Element - Fetch Order Status API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Fetch Order Status API** retrieves the real-time status of an order and its associated transactions from PayU's order management system. Use this API to verify final payment outcomes, reconcile unconfirmed or timed-out browser sessions, inspect SKU-level breakdowns, and verify the charged amount against the original order value before fulfilling goods or services.

<Cards_PayU_Labs />

<br />

## Postman Collection

<Postman_collection />

<Callout icon="📘" theme="info">
  ### **Reconciliation Best Practice**

  - While PayU pushes transaction outcomes via browser redirects and server-to-server webhooks, network interruptions or client drop-offs can occasionally delay delivery.
  - Implement this API as an automated reconciliation fallback whenever your server needs to determine the authoritative status of an order.
</Callout>

<Accordion_Collect_Fraud_Detection />

**Environment**

| Environment              | Base URL         |
| :----------------------- | :--------------- |
| **Test / Sandbox (UAT)** | `<redacted URL>` |
| **Production**           | `<redacted URL>` |

***

<Accordion title="Sample Request" icon="fa-code">
  <Tabs>
    <Tab title="cURL">
      ```curl
      curl --location '<redacted URL>' \
      --header 'Accept: application/json' \
      --header 'Date: Wed, 15 Jan 2026 10:35:00 GMT' \
      --header 'Authorization: hmac username="YOUR_MERCHANT_KEY", algorithm="sha512", headers="date", signature="GENERATED_SHA512_HASH"'
      ```
    </Tab>

    <Tab title="Node.js">
      ```javascript
      const axios = require("axios");
      const crypto = require("crypto");

      async function fetchOrderStatus(orderId) {
        const merchantKey = "YOUR_MERCHANT_KEY";
        const merchantSecret = "YOUR_MERCHANT_SECRET";
        const url = `<redacted URL>}`;

        const dateHeader = new Date().toUTCString();

        // For GET requests with an empty body, hash empty string or query representation as per PayU auth contract
        const requestBody = "";
        const hashString = `${requestBody}|${dateHeader}|${merchantSecret}`;

        const signature = crypto
          .createHash("sha512")
          .update(hashString)
          .digest("hex")
          .padStart(128, "0");

        const headers = {
          "Accept": "application/json",
          "Date": dateHeader,
          "Authorization": `hmac username="${merchantKey}", algorithm="sha512", headers="date", signature="${signature}"`
        };

        try {
          const response = await axios.get(url, { headers });
          console.log("Order Status Response:", response.data);
          return response.data;
        } catch (error) {
          console.error("Fetch Status Error:", error.response ? error.response.data : error.message);
        }
      }

      fetchOrderStatus("ORD_1737021000");
      ```
    </Tab>

    <Tab title="Python">
      ```python
      import requests
      import hashlib
      from datetime import datetime, timezone

      def fetch_order_status(order_id):
          merchant_key = "YOUR_MERCHANT_KEY"
          merchant_secret = "YOUR_MERCHANT_SECRET"
          url = f"<redacted URL>}"

          date_header = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
          request_body = ""
          hash_string = f"{request_body}|{date_header}|{merchant_secret}"

          signature = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().zfill(128)

          headers = {
              "Accept": "application/json",
              "Date": date_header,
              "Authorization": f'hmac username="{merchant_key}", algorithm="sha512", headers="date", signature="{signature}"'
          }

          response = requests.get(url, headers=headers)
          print(f"Status Code: {response.status_code}")
          print("Response JSON:", response.json())
          return response.json()

      fetch_order_status("ORD_1737021000")
      ```
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  ### Successful Status Response (`200 OK`)

  ```json
  {
    "message": "Order Fetched Successfully",
    "status": 1,
    "traceId": "22f3d627-ac03-432b-86b0-f086143de646",
    "data": {
      "orderReferenceId": 215,
      "orderId": "ORD_1737021000",
      "merchantId": 180012,
      "finalAmount": 550.00,
      "originalAmount": 550.00,
      "orderStatus": "PAYMENT_INITIATED",
      "skus": [
        {
          "skuId": "SKU_101",
          "skuName": "Product 1",
          "amountPerSku": 250.00,
          "quantity": 2
        }
      ]
    }
  }
  ```
</Accordion>

***

## Request Parameters

### Request Headers

| Header          | Type     | Required      | Description                                                                                                                                 |
| :-------------- | :------- | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------ |
| `Accept`        | `String` | Optional      | Set to `application/json`.                                                                                                                  |
| `Date`          | `String` | **Mandatory** | Current timestamp in UTC formatted strictly to RFC 1123 format (e.g. `Wed, 15 Jan 2026 10:35:00 GMT`).                                      |
| `Authorization` | `String` | **Mandatory** | HMAC-SHA512 authorization header formatted as:<br />`hmac username="{merchantKey}", algorithm="sha512", headers="date", signature="{hash}"` |

### Query Parameters

| Parameter | Type     | Required      | Description                                                                                      |
| :-------- | :------- | :------------ | :----------------------------------------------------------------------------------------------- |
| `orderId` | `String` | **Mandatory** | The unique merchant order ID provided during [Create Order](doc:api-cards-element-create-order). |

***

## Response Parameters

<Accordion title="Response Fields Breakdown" icon="fa-list-check">
  | Field Name              | Type             | Description                                                                                                                 |
  | :---------------------- | :--------------- | :-------------------------------------------------------------------------------------------------------------------------- |
  | `message`               | `String`         | Status response message (e.g. `Order Fetched Successfully`).                                                                |
  | `status`                | `Integer`        | API execution status indicator (`1` for success, `0` for failure).                                                          |
  | `traceId`               | `String`         | Unique server request trace ID for audit and debugging.                                                                     |
  | `data`                  | `Object`         | Order details container.                                                                                                    |
  | `data.orderReferenceId` | `Integer / Long` | PayU internal order reference number.                                                                                       |
  | `data.orderId`          | `String`         | Merchant order identifier passed in the request query.                                                                      |
  | `data.merchantId`       | `Integer`        | PayU numeric Merchant ID (MID).                                                                                             |
  | `data.finalAmount`      | `Number`         | Final payable amount after applying discounts, offers, or fees.                                                             |
  | `data.originalAmount`   | `Number`         | Original base order amount prior to offer applications.                                                                     |
  | `data.orderStatus`      | `String`         | Current order lifecycle status. Values include `PAYMENT_INITIATED`, `SUCCESS`, `FAILED`, `PENDING`, `EXPIRED`, `CANCELLED`. |
  | `data.skus`             | `Array<Object>`  | List of associated SKU objects registered during order creation.                                                            |
</Accordion>

***

## Order Status Reference

| Status Value        | Meaning                                                                                                  | Recommended Merchant Action                                          |
| :------------------ | :------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------- |
| `PAYMENT_INITIATED` | Order created and payment has been attempted; customer authentication or bank authorization in progress. | Poll status after a short interval or wait for S2S webhook.          |
| `SUCCESS`           | Payment was successfully captured and authorized by the issuing bank.                                    | Fulfill the order and deliver goods or services.                     |
| `FAILED`            | Payment failed or was rejected by issuing bank/gateway.                                                  | Inform customer and provide an option to retry payment.              |
| `PENDING`           | Transaction is under clearing or bank verification.                                                      | Keep order in pending state and re-check via status poll or webhook. |
| `EXPIRED`           | Order session expired without completion.                                                                | Require customer to re-initiate checkout.                            |
| `CANCELLED`         | Customer aborted transaction.                                                                            | Mark cart/checkout session cancelled.                                |
