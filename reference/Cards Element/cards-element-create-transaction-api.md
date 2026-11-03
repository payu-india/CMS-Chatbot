---
title: Cards Element - Create Transaction API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Create Transaction API** initiates payment for an existing order using card details (raw physical card or tokenized/stored card). For merchants integrating PayU Checkout Elements, payment orchestration can be handled either directly in the browser via the client-side `PayuCheckout.processPayment()` SDK method, or server-to-server via this endpoint.

When 3D Secure (3DS) authentication is required, this API returns an HTML authentication form (`acsTemplate`) encoded in Base64. Your backend or frontend decodes this template to render the bank's authentication challenge to the customer.

<Cards_PayU_Labs />

<br />

## Postman Collection

<Postman_collection />

<Callout icon="📘" theme="info">
  ### **Prerequisites & Headers**

  - An active order must be created first via the [Create Order API](doc:api-cards-element-create-order).
  - Use either the `encOrderId` + `accessToken` header combination OR `orderId` + `X-Credential-Username` + `accessToken`.
  - For plain raw card payments, ensure your integration complies with applicable card security and regulatory standards. In PCI-scoped integrations, use the PayU Checkout JS SDK iframe element so that raw card details never touch your servers.
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
    <Tab title="cURL (Physical Card)">
      ```curl
      curl --location '<redacted URL>' \
      --header 'Content-Type: application/json' \
      --header 'encOrderId: c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312' \
      --header 'accessToken: FFF3D2D1-5B20-C1BC-728B-08E47A374D00' \
      --data-raw '{
        "txnId": "TXN_1737021500",
        "paymentMethod": {
          "name": "CreditCard",
          "bankCode": "CC",
          "paymentCard": {
            "cardNumber": "5123456789012346",
            "ownerName": "John Doe",
            "validThrough": "12/2028",
            "cvv": "123"
          },
          "storeCard": true
        },
        "additional_info": {
          "language": "en"
        }
      }'
      ```
    </Tab>

    <Tab title="cURL (Tokenized / Stored Card)">
      ```curl
      curl --location '<redacted URL>' \
      --header 'Content-Type: application/json' \
      --header 'orderId: ORD_1737021000' \
      --header 'X-Credential-Username: YOUR_MERCHANT_KEY' \
      --header 'accessToken: FFF3D2D1-5B20-C1BC-728B-08E47A374D00' \
      --data-raw '{
        "txnId": "TXN_1737021501",
        "paymentMethod": {
          "name": "CreditCard",
          "bankCode": "CC",
          "storeCard": false,
          "storeCardToken": "4e76a91d2938a9e083...",
          "storecardTokenType": "1"
        },
        "offerKeys": [
          "HDFC_10_PERCENT"
        ]
      }'
      ```
    </Tab>

    <Tab title="Node.js">
      ```javascript
      const axios = require("axios");

      async function createCardTransaction() {
        const url = "<redacted URL>";

        const headers = {
          "Content-Type": "application/json",
          "encOrderId": "c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312",
          "accessToken": "FFF3D2D1-5B20-C1BC-728B-08E47A374D00"
        };

        const payload = {
          txnId: "TXN_" + Date.now(),
          paymentMethod: {
            name: "CreditCard",
            bankCode: "CC",
            paymentCard: {
              cardNumber: "5123456789012346",
              ownerName: "John Doe",
              validThrough: "12/2028",
              cvv: "123"
            },
            storeCard: true
          },
          additional_info: {
            language: "en"
          }
        };

        try {
          const response = await axios.post(url, payload, { headers });
          console.log("Transaction Initiated:", response.data);

          // Handle 3DS ACS template redirection
          if (response.data.result && response.data.result.acsTemplate) {
            const htmlForm = Buffer.from(response.data.result.acsTemplate, "base64").toString("utf-8");
            console.log("Decoded 3DS ACS Form:", htmlForm);
          }
          return response.data;
        } catch (error) {
          console.error("Payment Initiation Error:", error.response ? error.response.data : error.message);
        }
      }

      createCardTransaction();
      ```
    </Tab>

    <Tab title="Python">
      ```python
      import requests
      import base64
      import time

      def initiate_card_payment():
          url = "<redacted URL>"

          headers = {
              "Content-Type": "application/json",
              "encOrderId": "c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312",
              "accessToken": "FFF3D2D1-5B20-C1BC-728B-08E47A374D00"
          }

          payload = {
              "txnId": f"TXN_{int(time.time())}",
              "paymentMethod": {
                  "name": "CreditCard",
                  "bankCode": "CC",
                  "paymentCard": {
                      "cardNumber": "5123456789012346",
                      "ownerName": "John Doe",
                      "validThrough": "12/2028",
                      "cvv": "123"
                  },
                  "storeCard": True
              },
              "additional_info": {
                  "language": "en"
              }
          }

          response = requests.post(url, headers=headers, json=payload)
          data = response.json()
          print("Status Code:", response.status_code)
          print("Response:", data)

          # Decode 3DS Challenge Form
          if "result" in data and "acsTemplate" in data["result"]:
              decoded_html = base64.b64decode(data["result"]["acsTemplate"]).decode("utf-8")
              print("Decoded 3DS Form:\n", decoded_html)

          return data

      initiate_card_payment()
      ```
    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  ### 3DS Authentication Challenge Response

  ```json
  {
    "result": {
      "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vYXBpLnBheXUuaW4vcHVibGljLyMvZTJkYSIgbWV0aG9kPSJwb3N0Ij48c2NyaXB0PnZhciBmPWRvY3VtZW50LnBheW1lbnRfcG9zdDtmLnN1Ym1pdCgpOzwvc2NyaXB0PjwvZm9ybT48L2JvZHk+PC9odG1sPg=="
    },
    "metaData": {
      "txnId": "TXN_1737021500",
      "txnStatus": "Enrolled",
      "unmappedStatus": "pending",
      "referenceId": "550e8400-e29b-41d4-a716-446655440000"
    }
  }
  ```
</Accordion>

***

## Request Parameters

### Request Headers

Merchants must provide authentication headers using either **Option A** (Session Tokens) or **Option B** (Order Reference):

#### Option A (Recommended)

| Header         | Type     | Required      | Description                                                                                   |
| :------------- | :------- | :------------ | :-------------------------------------------------------------------------------------------- |
| `Content-Type` | `String` | **Mandatory** | Must be `application/json`.                                                                   |
| `accessToken`  | `String` | **Mandatory** | Session access token returned in `transaction.accessToken` from the Create Order response.    |
| `encOrderId`   | `String` | **Mandatory** | Encrypted order ID returned in `transaction.encryptedOrderId` from the Create Order response. |

#### Option B

| Header                  | Type     | Required      | Description                                                                   |
| :---------------------- | :------- | :------------ | :---------------------------------------------------------------------------- |
| `Content-Type`          | `String` | **Mandatory** | Must be `application/json`.                                                   |
| `accessToken`           | `String` | **Mandatory** | Session access token returned in `transaction.accessToken` from Create Order. |
| `orderId`               | `String` | **Mandatory** | The original merchant `orderId` sent during Create Order.                     |
| `X-Credential-Username` | `String` | **Mandatory** | Your PayU Merchant Key.                                                       |

***

### Request Body

| Parameter         | Type            | Required      | Description & Constraints                                                                          |
| :---------------- | :-------------- | :------------ | :------------------------------------------------------------------------------------------------- |
| `txnId`           | `String`        | Optional      | Unique merchant transaction reference for this payment attempt. If omitted, defaults to `orderId`. |
| `paymentMethod`   | `Object`        | **Mandatory** | Container object defining payment instrument details.                                              |
| `offerKeys`       | `Array<String>` | Optional      | One or more promo/offer keys selected by the customer to apply at payment time.                    |
| `promocode`       | `Array<String>` | Optional      | Array of coupon/promo codes entered by the customer.                                               |
| `additional_info` | `Object`        | Optional      | Contextual payment metadata (e.g. `{"language": "en"}`).                                           |
| `customer`        | `Object`        | Optional      | Optional customer and address override details.                                                    |

***

### `paymentMethod` Object

| Parameter                  | Type      | Required      | Description & Constraints                                                                                         |
| :------------------------- | :-------- | :------------ | :---------------------------------------------------------------------------------------------------------------- |
| `name`                     | `String`  | **Mandatory** | Payment mode name. Set to `CreditCard` or `DebitCard`.                                                            |
| `bankCode`                 | `String`  | **Mandatory** | Card bank code identifier. Set to `CC` for Credit Cards or `DC` for Debit Cards.                                  |
| `paymentCard`              | `Object`  | Conditional   | Required when processing payment using a raw physical card. Container for card number, CVV, and expiration.       |
| `paymentCard.cardNumber`   | `String`  | Conditional   | 13–19 digit card Primary Account Number (PAN). Required if `paymentCard` is used.                                 |
| `paymentCard.ownerName`    | `String`  | Optional      | Name of cardholder as printed on card.                                                                            |
| `paymentCard.validThrough` | `String`  | Conditional   | Card expiration date formatted as `MM/YYYY` or `MM/YY` (e.g. `12/2028`).                                          |
| `paymentCard.cvv`          | `String`  | Conditional   | 3 or 4-digit card verification code.                                                                              |
| `storeCard`                | `Boolean` | Optional      | Set to `true` if the customer has consented to tokenize and save this card with PayU for future checkout.         |
| `storeCardToken`           | `String`  | Conditional   | Card token identifier. Required when processing payment using a saved/tokenized card instead of raw card numbers. |
| `storecardTokenType`       | `String`  | Conditional   | Token classification identifier. Set to `"1"` for PayU tokens, or `"0"` depending on vault tokenization rules.    |

***

## Response Parameters

<Accordion title="Response Fields Breakdown" icon="fa-list-check">
  | Field Name                | Type     | Description                                                                                                                                                                                   |
  | :------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `result`                  | `Object` | Action payload container.                                                                                                                                                                     |
  | `result.acsTemplate`      | `String` | Base64-encoded HTML form used to initiate 3D Secure bank authentication. Decode this string into HTML and auto-submit the form to redirect the customer to their bank's OTP / challenge page. |
  | `metaData`                | `Object` | Transaction status tracking metadata.                                                                                                                                                         |
  | `metaData.txnId`          | `String` | The transaction reference ID passed in the request or resolved by PayU.                                                                                                                       |
  | `metaData.txnStatus`      | `String` | High-level transaction stage (e.g. `Enrolled`, `pending`, `success`, `failed`).                                                                                                               |
  | `metaData.unmappedStatus` | `String` | Detailed underlying transaction state (e.g. `pending`, `failure`).                                                                                                                            |
  | `metaData.referenceId`    | `String` | Unique PayU transaction tracking UUID.                                                                                                                                                        |
</Accordion>

***

## 3DS Challenge Redirection Handling

When `result.acsTemplate` is returned in the response:

1. **Base64 Decode**: Decode the Base64 string into standard UTF-8 HTML.
2. **Render HTML Form**: Inject the decoded form into a browser window or hidden DOM iframe.
3. **Auto-Submit**: The decoded template contains an embedded JavaScript auto-submission snippet (`document.payment_post.submit()`) which posts the 3DS parameters to the issuer's Access Control Server (ACS).
4. **Customer Completes 3DS**: Customer enters their OTP or biometrics on the issuing bank's secure page.
5. **Callback Redirect**: Upon completion or cancellation, PayU redirects the browser back to your configured `callBackActions.successUrl` or `callBackActions.failureUrl` supplied during [Create Order](doc:api-cards-element-create-order).
