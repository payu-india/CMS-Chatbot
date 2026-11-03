---
title: Cards Element - Create Order
deprecated: false
hidden: true
metadata:
  robots: index
---
---
api:
  file: checkout_elements_v1.json
  operationId: createOrder
hidden: false
link:
  new_tab: false
---
The **Create Order API** initiates the PayU Checkout Elements journey. It registers an order on PayU's payment gateway, sets up pricing, customer details, and callback actions, and returns the session credentials (`accessToken` and `encryptedOrderId`) required to initialize the client-side Checkout JS SDK.

<Cards_PayU_Labs />

<br />

## Postman Collection

<Postman_collection />

<Callout icon="📘" theme="info">
  ### **Integration Note**
  - Always call this API **server-to-server** from your secure backend.
  - Never expose your `merchantSecret` or compute the HMAC-SHA512 authorization header on the browser or client-side application.
  - The returned `transaction.encryptedOrderId` must be passed to the frontend to initialize `PayuCheckout.init({ orderId })`.
</Callout>

<Accordion_Collect_Fraud_Detection />

**Environment**

| Environment | Base URL |
| :--- | :--- |
| **Test / Sandbox (UAT)** | `<redacted URL>` |
| **Production** | `<redacted URL>` |

---

<Accordion title="Sample Request" icon="fa-code">
  <Tabs>
    <Tab title="cURL">
      ```curl
      curl --location '<redacted URL>' \
      --header 'Content-Type: application/json' \
      --header 'Accept: application/json' \
      --header 'Date: Wed, 15 Jan 2026 10:30:00 GMT' \
      --header 'Authorization: hmac username="YOUR_MERCHANT_KEY", algorithm="sha512", headers="date", signature="GENERATED_SHA512_HASH"' \
      --data-raw '{
        "orderId": "ORD_1737021000",
        "currency": "INR",
        "productinfo": "Flight Tickets",
        "paymentSource": "direct",
        "order": {
          "amount": 550.00,
          "productinfo": "Order description",
          "skus": [
            {
              "skuId": "SKU_101",
              "skuName": "Product 1",
              "amountPerSku": 250.00,
              "quantity": 2,
              "enforcedOfferKeys": []
            }
          ],
          "enforcedOfferKeys": [],
          "extraCharges": {
            "shippingCharges": 20.0,
            "codFee": 0.0,
            "otherCharges": 10.0,
            "taxInfo": {
              "breakup": {
                "CGST": 10.0,
                "SGST": 10.0
              },
              "total": 20.0
            }
          }
        },
        "customer": {
          "firstName": "John",
          "lastName": "Doe",
          "email": "john.doe@example.com",
          "phoneNumber": "9886575652",
          "address": {
            "billingAddress": {
              "name": "John Doe",
              "email": "john.doe@example.com",
              "addressLine": "123 Main Street, Apartment 4B",
              "addressLine2": "Near City Mall",
              "addressPhoneNumber": "9886575652",
              "landmark": "Opposite Central Park",
              "pincode": "110001",
              "city": "New Delhi",
              "state": "Delhi",
              "country": "IN"
            },
            "shippingAddress": {
              "name": "John Doe",
              "email": "john.doe@example.com",
              "addressLine": "456 Business Park, Floor 2",
              "addressLine2": "Tower B",
              "addressPhoneNumber": "9876543210",
              "landmark": "Near Tech Hub",
              "pincode": "110002",
              "city": "New Delhi",
              "state": "Delhi",
              "country": "IN"
            }
          },
          "deviceInfoDetails": {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "ipAddress": "192.168.1.100",
            "screenResolution": "1920x1080"
          }
        },
        "callBackActions": {
          "successUrl": "https://merchant.com/payment/success",
          "failureUrl": "https://merchant.com/payment/failure",
          "cancelUrl": "https://merchant.com/payment/cancel",
          "webhookUrl": "https://merchant.com/webhook/payment",
          "notifyUrl": "https://merchant.com/notify/payment"
        },
        "merchantCacheExpiry": 3600,
        "udf1": "Order_Tag_A",
        "udf2": "Customer_Tier_Gold",
        "udf3": "",
        "udf4": "",
        "udf5": ""
      }'
      ```
    </Tab>

    <Tab title="Node.js">
      ```javascript
      const crypto = require("crypto");
      const axios = require("axios");

      async function createOrder() {
        const merchantKey = "YOUR_MERCHANT_KEY";
        const merchantSecret = "YOUR_MERCHANT_SECRET";
        const url = "<redacted URL>";

        const requestBody = {
          orderId: "ORD_" + Date.now(),
          currency: "INR",
          productinfo: "Flight Tickets",
          paymentSource: "direct",
          order: {
            amount: 550.00,
            productinfo: "Order description"
          },
          customer: {
            firstName: "John",
            lastName: "Doe",
            email: "john.doe@example.com",
            phoneNumber: "9886575652"
          },
          callBackActions: {
            successUrl: "https://merchant.com/payment/success",
            failureUrl: "https://merchant.com/payment/failure",
            cancelUrl: "https://merchant.com/payment/cancel",
            webhookUrl: "https://merchant.com/webhook/payment"
          },
          merchantCacheExpiry: 3600
        };

        const date = new Date().toUTCString(); // RFC 1123 format
        const bodyString = JSON.stringify(requestBody);
        const hashString = `${bodyString}|${date}|${merchantSecret}`;

        const signature = crypto
          .createHash("sha512")
          .update(hashString)
          .digest("hex")
          .padStart(128, "0");

        const headers = {
          "Content-Type": "application/json",
          "Accept": "application/json",
          "Date": date,
          "Authorization": `hmac username="${merchantKey}", algorithm="sha512", headers="date", signature="${signature}"`
        };

        try {
          const response = await axios.post(url, requestBody, { headers });
          console.log("Create Order Response:", response.data);
          return response.data;
        } catch (error) {
          console.error("Create Order Error:", error.response ? error.response.data : error.message);
        }
      }

      createOrder();
      ```
    </Tab>

    <Tab title="Python">
      ```python
      import requests
      import json
      import hashlib
      from datetime import datetime, timezone

      def create_order():
          merchant_key = "YOUR_MERCHANT_KEY"
          merchant_secret = "YOUR_MERCHANT_SECRET"
          url = "<redacted URL>"

          payload = {
              "orderId": f"ORD_{int(datetime.now().timestamp())}",
              "currency": "INR",
              "productinfo": "Flight Tickets",
              "paymentSource": "direct",
              "order": {
                  "amount": 550.00,
                  "productinfo": "Order description"
              },
              "customer": {
                  "firstName": "John",
                  "lastName": "Doe",
                  "email": "john.doe@example.com",
                  "phoneNumber": "9886575652"
              },
              "callBackActions": {
                  "successUrl": "https://merchant.com/payment/success",
                  "failureUrl": "https://merchant.com/payment/failure",
                  "cancelUrl": "https://merchant.com/payment/cancel",
                  "webhookUrl": "https://merchant.com/webhook/payment"
              },
              "merchantCacheExpiry": 3600
          }

          # RFC 1123 UTC date format
          date_header = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
          body_json = json.dumps(payload, separators=(',', ':'))
          hash_string = f"{body_json}|{date_header}|{merchant_secret}"

          signature = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().zfill(128)

          headers = {
              "Content-Type": "application/json",
              "Accept": "application/json",
              "Date": date_header,
              "Authorization": f'hmac username="{merchant_key}", algorithm="sha512", headers="date", signature="{signature}"'
          }

          response = requests.post(url, headers=headers, data=body_json)
          print(f"Status Code: {response.status_code}")
          print("Response JSON:", response.json())
          return response.json()

      create_order()
      ```
    </Tab>

    <Tab title="Java">
      ```java
      import java.net.URI;
      import java.net.http.HttpClient;
      import java.net.http.HttpRequest;
      import java.net.http.HttpResponse;
      import java.nio.charset.StandardCharsets;
      import java.security.MessageDigest;
      import java.time.ZoneOffset;
      import java.time.ZonedDateTime;
      import java.time.format.DateTimeFormatter;

      public class PayUCreateOrder {
          public static String getSha512Hash(String hashString) throws Exception {
              MessageDigest md = MessageDigest.getInstance("SHA-512");
              byte[] digest = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
              StringBuilder sb = new StringBuilder();
              for (byte b : digest) {
                  sb.append(String.format("%02x", b));
              }
              while (sb.length() < 128) {
                  sb.insert(0, "0");
              }
              return sb.toString();
          }

          public static void main(String[] args) {
              try {
                  String merchantKey = "YOUR_MERCHANT_KEY";
                  String merchantSecret = "YOUR_MERCHANT_SECRET";
                  String url = "<redacted URL>";

                  String dateHeader = DateTimeFormatter.RFC_1123_DATE_TIME.format(ZonedDateTime.now(ZoneOffset.UTC));

                  String requestBody = "{\n" +
                      "  \"orderId\": \"ORD_1737021000\",\n" +
                      "  \"currency\": \"INR\",\n" +
                      "  \"productinfo\": \"Flight Tickets\",\n" +
                      "  \"paymentSource\": \"direct\",\n" +
                      "  \"order\": { \"amount\": 550.00, \"productinfo\": \"Order description\" },\n" +
                      "  \"customer\": { \"firstName\": \"John\", \"lastName\": \"Doe\", \"email\": \"john.doe@example.com\", \"phoneNumber\": \"9886575652\" },\n" +
                      "  \"callBackActions\": { \"successUrl\": \"https://merchant.com/payment/success/", \"failureUrl\": \"https://merchant.com/payment/failure/" },\n" +
                      "  \"merchantCacheExpiry\": 3600\n" +
                      "}";

                  String hashString = requestBody + "|" + dateHeader + "|" + merchantSecret;
                  String signature = getSha512Hash(hashString);
                  String authHeader = String.format("hmac username=\"%s\", algorithm=\"sha512\", headers=\"date\", signature=\"%s\"", merchantKey, signature);

                  HttpRequest request = HttpRequest.newBuilder()
                      .uri(URI.create(url))
                      .header("Content-Type", "application/json")
                      .header("Accept", "application/json")
                      .header("Date", dateHeader)
                      .header("Authorization", authHeader)
                      .POST(HttpRequest.BodyPublishers.ofString(requestBody, StandardCharsets.UTF_8))
                      .build();

                  HttpClient client = HttpClient.newHttpClient();
                  HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

                  System.out.println("Response Status: " + response.statusCode());
                  System.out.println("Response Body: " + response.body());
              } catch (Exception e) {
                  e.printStackTrace();
              }
          }
      }
      ```
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  ### Successful Order Creation (`200 OK`)
  ```json
  {
    "paymentMethods": {
      "emi": {
        "cc": { "all": [], "top": [] }
      },
      "nb": { "all": [], "top": [] },
      "cc": { "all": [] },
      "dc": { "all": [] },
      "upi": { "all": [] }
    },
    "merchant": {
      "key": "rM5M43",
      "merchantId": "180012",
      "scMerchantId": "180012",
      "enableNewOffersEngine": true,
      "name": "MERCHANT NAME",
      "merchantParams": {}
    },
    "broker": "PAYU",
    "order": {
      "amount": "550.0",
      "orderId": "ORD_1737021000"
    },
    "transaction": {
      "accessToken": "FFF3D2D1-5B20-C1BC-728B-08E47A374D00",
      "encryptedOrderId": "c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312",
      "orderid": "ORDUAT0017",
      "txnId": "mtx1754396543709"
    },
    "customer": {
      "firstName": "John",
      "email": "john.doe@example.com",
      "phoneNumber": "9886575652"
    },
    "bankLogosUrl": "https://web-assets.payu.in/web/images/assets/bankLogo/"
  }
  ```
</Accordion>

---

## Request Parameters

### Request Headers

| Header | Type | Required | Description & Constraints |
| :--- | :--- | :--- | :--- |
| `Content-Type` | `String` | **Mandatory** | Must be `application/json`. |
| `Accept` | `String` | Optional | Set to `application/json`. |
| `Date` | `String` | **Mandatory** | Current timestamp in UTC formatted strictly to RFC 1123 / RFC 7231 (e.g. `Wed, 15 Jan 2026 10:30:00 GMT`). Must match the date used in signature generation. |
| `Authorization` | `String` | **Mandatory** | HMAC-SHA512 authorization header formatted as:<br>`hmac username="{merchantKey}", algorithm="sha512", headers="date", signature="{hash}"` |

### Top-Level Request Body

| Parameter | Type | Required | Description & Constraints |
| :--- | :--- | :--- | :--- |
| `orderId` | `String` | **Mandatory** | Unique merchant order identifier generated by your system. |
| `currency` | `String` | **Mandatory** | ISO 4217 currency code. Set to `INR`. |
| `paymentSource` | `String` | **Mandatory** | Channel identifier. Must be set to `direct` for Checkout Elements integration. *(Note: If not set to `direct` or `SDK`, the API returns an HTTP 302 web redirect).* |
| `productinfo` | `String` | **Mandatory** | Brief description or title of the order / product purchased. |
| `order` | `Object` | **Mandatory** | JSON container object for order details and charges. |
| `customer` | `Object` | **Mandatory** | JSON container object holding buyer profile and address details. |
| `callBackActions` | `Object` | **Mandatory** | JSON container holding redirect and notification callback URLs. |
| `merchantCacheExpiry` | `Long / Integer` | Conditional | Cache time-to-live (TTL) in seconds. Defaults to `3600` (1 hour). |
| `udf1` – `udf5` | `String` | Optional | Custom merchant user-defined metadata fields. Maximum 255 characters each. |
| `additionalPaymentParams` | `Object` | Optional | Optional container for pre-configured payment options such as Recurring Payments (Standing Instructions). |

---

### `order` Object

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `order.amount` | `Number` | **Mandatory** | Final payable amount for the order (e.g. `550.00`). Must be greater than `0`. |
| `order.productinfo` | `String` | Optional | Line-item description displayed to the customer. |
| `order.skus` | `Array<Object>` | Optional | Array of SKU item details for SKU-level discount/cashback offers. |
| `order.skus[].skuId` | `String` | Optional | Unique SKU product identifier. |
| `order.skus[].skuName` | `String` | Optional | Product or SKU name. |
| `order.skus[].amountPerSku` | `Number` | Optional | Unit price per item. |
| `order.skus[].quantity` | `Integer` | Optional | Number of units purchased. |
| `order.skus[].enforcedOfferKeys`| `Array<String>` | Optional | Specific offer keys to enforce on this individual SKU. |
| `order.enforcedOfferKeys` | `Array<String>` | Optional | Global offer keys to pre-apply/enforce on this order. |
| `order.extraCharges` | `Object` | Optional | Breakup of additional charges (shipping, COD, taxes). |
| `order.extraCharges.shippingCharges` | `Number` | Optional | Shipping charge component. |
| `order.extraCharges.codFee` | `Number` | Optional | Cash on delivery surcharge if applicable. |
| `order.extraCharges.otherCharges` | `Number` | Optional | Ancillary fees or packaging charges. |
| `order.extraCharges.taxInfo` | `Object` | Optional | Tax information object containing breakup (e.g. CGST, SGST) and `total`. |

---

### `customer` Object

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `customer.firstName` | `String` | **Mandatory** | Customer's first name. |
| `customer.lastName` | `String` | Optional | Customer's last name. |
| `customer.email` | `String` | **Mandatory** | Customer's valid email address. |
| `customer.phoneNumber` | `String` | **Mandatory** | Customer's 10-digit mobile phone number (regex validated). |
| `customer.address` | `Object` | Optional | Container for billing and shipping addresses. |
| `customer.address.billingAddress` | `Object` | Optional | Billing address object (`name`, `email`, `addressLine`, `addressLine2`, `addressPhoneNumber`, `pincode`, `city`, `state`, `country`). |
| `customer.address.shippingAddress` | `Object` | Optional | Shipping address object (`name`, `email`, `addressLine`, `addressLine2`, `addressPhoneNumber`, `pincode`, `city`, `state`, `country`). |
| `customer.deviceInfoDetails` | `Object` | Optional | Client device metadata (`userAgent`, `ipAddress`, `screenResolution`). |

---

### `callBackActions` Object

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `callBackActions.successUrl` | `String` | **Mandatory** | HTTPS merchant redirection URL after successful 3DS authentication / payment. |
| `callBackActions.failureUrl` | `String` | **Mandatory** | HTTPS merchant redirection URL after failed authentication / payment. |
| `callBackActions.cancelUrl` | `String` | Optional | HTTPS URL if user cancels transaction. |
| `callBackActions.webhookUrl` | `String` | Optional | HTTPS endpoint for PayU asynchronous server-to-server transaction notifications. |
| `callBackActions.notifyUrl` | `String` | Optional | Merchant notification endpoint. |

---

### `additionalPaymentParams` Object (Recurring Payments / SI)

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `si` | `Integer` | Optional | Set to `1` to enable Standing Instruction (Recurring Mandate) for this order. |
| `si_details.billingAmount` | `String / Number` | Conditional | Recurring debit amount (e.g. `"500.00"`). |
| `si_details.billingCurrency` | `String` | Conditional | ISO currency code for recurring debit (e.g. `"INR"`). |
| `si_details.billingCycle` | `String` | Conditional | Recurring frequency: `DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`, `ADHOC`, `ONCE`. |
| `si_details.billingInterval` | `Integer` | Conditional | Cycle interval multiplier (e.g. `1` for every month). |
| `si_details.paymentStartDate` | `String` | Conditional | Mandate start date in `YYYY-MM-DD` format. |
| `si_details.paymentEndDate` | `String` | Conditional | Mandate expiry date in `YYYY-MM-DD` format. |
| `si_details.siTokenRequestor` | `Integer` | Optional | Token requestor identifier. |

---

## Response Parameters

<Accordion title="Response Fields Breakdown" icon="fa-list-check">
  | Field Name | Type | Description |
  | :--- | :--- | :--- |
  | `paymentMethods` | `Object` | Dictionary of available payment methods enabled for the merchant account and order amount (`cc`, `dc`, `nb`, `upi`, `emi`). |
  | `broker` | `String` | Payment broker identifier (e.g. `PAYU`). |
  | `merchant` | `Object` | Merchant account metadata including `key`, `merchantId`, and `name`. |
  | `order` | `Object` | Echo of order details, including `orderId` and payable `amount`. |
  | `transaction` | `Object` | Session transaction metadata required by client-side Checkout Elements. |
  | `transaction.accessToken` | `String` | **Session Access Token**. Passed to subsequent APIs or retained for session context. |
  | `transaction.encryptedOrderId` | `String` | **Encrypted Order ID**. Mandatory parameter passed into `PayuCheckout.init({ orderId: encryptedOrderId })` on your frontend checkout page. |
  | `transaction.orderid` | `String` | Internal order reference ID. |
  | `transaction.txnId` | `String` | PayU transaction reference ID (e.g. `mtx1754396543709`). |
  | `customer` | `Object` | Customer profile echo (`firstName`, `email`, `phoneNumber`). |
  | `bankLogosUrl` | `String` | Base URL for accessing PayU bank and issuer logos. |
  | `downInfo` | `Object` | Optional object containing real-time issuing bank outage information. |
</Accordion>

---

## Authentication Signature Calculation

To compute the HMAC-SHA512 signature for the `Authorization` header:

1. Format the current time in UTC using RFC 1123 format (e.g. `Wed, 15 Jan 2026 10:30:00 GMT`).
2. Construct the raw hash string by concatenating the exact JSON request body, a pipe (`|`), the formatted date, another pipe (`|`), and your merchant secret:
   ```
   hashString = JSON_STRING + "|" + DATE_HEADER + "|" + MERCHANT_SECRET
   ```
3. Generate the SHA-512 cryptographic digest of `hashString`.
4. Ensure the output is formatted as a 128-character lowercase hexadecimal string (zero-padded to 128 characters if necessary).
5. Build the `Authorization` header:
   ```
   Authorization: hmac username="{merchantKey}", algorithm="sha512", headers="date", signature="{hash}"
   ```