---
title: Create Transaction API
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Create Transaction** API initiates payment for the order using the customer's selected payment method (Net Banking, UPI Intent, UPI Collect, Cards, or EMI).

After the customer selects their payment method and enters required credentials (e.g. card details, VPA, or bank selection), your client or server submits this request.

- For **Net Banking & 3DS Cards**: PayU returns an `acsTemplate` containing a Base64-encoded HTML redirection form. Merchant decodes and auto-submits this form in the customer's browser.
- For **UPI Intent**: PayU returns intent URI/payloads to trigger installed UPI applications (Google Pay, PhonePe, Paytm).
- For **UPI Collect**: PayU dispatches a collect request to the customer's UPI app.

**Environment**

|                            |                                      |
| -------------------------- | ------------------------------------ |
| **Test Environment**       | `https://apitest.payu.in/v1/payment` |
| **Production Environment** | `https://api.payu.in/v1/payment`     |
## Sample Request

```bash
curl -X POST "https://apitest.payu.in/v1/payment" \
  -H "Content-Type: application/json" \
  -H "encOrderId: c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312" \
  -H "accessToken: FFF3D2D1-5B20-C1BC-728B-08E47A374D00" \
  -d '{
    "txnId": "txn123",
    "offerKeys": ["OFFER_KEY_1"],
    "paymentMethod": {
      "bankCode": "ICIB",
      "name": "NetBanking"
    },
    "additionalPaymentParams": { "language": "en" }
  }'
```
```python
import requests
import json

url = "https://apitest.payu.in/v1/payment"

headers = {
    "Content-Type": "application/json",
    "encOrderId": "c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312",
    "accessToken": "FFF3D2D1-5B20-C1BC-728B-08E47A374D00",
}

payload = json.dumps({
    # Add your request payload here
})

response = requests.post(url, headers=headers, data=payload)

print(f'Status Code: {response.status_code}')
print(f'Response: {response.text}')
```
```javascript
const axios = require('axios');

const url = 'https://apitest.payu.in/v1/payment';

const headers = {
  'Content-Type': 'application/json',
  'encOrderId': 'c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312',
  'accessToken': 'FFF3D2D1-5B20-C1BC-728B-08E47A374D00',
};

const data = {
  // Add your request payload here
};

axios.post(url, data, { headers })
  .then(response => {
    console.log('Status Code:', response.status);
    console.log('Response:', response.data);
  })
  .catch(error => {
    console.error('Error:', error.response ? error.response.data : error.message);
  });
```
```java
import java.io.*;
import java.net.HttpURLConnection;
import java.net.URL;

public class PayUAPIRequest {
    public static void main(String[] args) {
        try {
            URL url = new URL("https://apitest.payu.in/v1/payment");
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("Content-Type", "application/json");
            conn.setRequestProperty("encOrderId", "c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312");
            conn.setRequestProperty("accessToken", "FFF3D2D1-5B20-C1BC-728B-08E47A374D00");
            conn.setDoOutput(true);

            String jsonInputString = "{}"; // Add JSON payload

            try (OutputStream os = conn.getOutputStream()) {
                byte[] input = jsonInputString.getBytes("utf-8");
                os.write(input, 0, input.length);
            }

            int responseCode = conn.getResponseCode();
            System.out.println("Status Code: " + responseCode);

            BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String inputLine;
            StringBuilder response = new StringBuilder();

            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();

            System.out.println("Response: " + response.toString());

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```
```php
<?php

$url = 'https://apitest.payu.in/v1/payment';

$headers = array(
    'Content-Type: application/json',
    'encOrderId: c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312',
    'accessToken: FFF3D2D1-5B20-C1BC-728B-08E47A374D00',
);

$data = json_encode(array(
    // Add your request payload
));

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);

curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";

?>
```
## Request Parameters

### Request Headers

#### Option 1: Session Token Authentication (Recommended)

| Header                                        | Description                                                     | Example                                                                                  |
| :-------------------------------------------- | :-------------------------------------------------------------- | :--------------------------------------------------------------------------------------- |
| <Glossary>encOrderId</Glossary> `mandatory`   | `String` Encrypted order identifier from Create Order response. | c422540c33ef9<br />f1259f15f7b9164<br />69b7227dc1d41a<br />7679653688547<br />4ddadf312 |
| <Glossary>accessToken</Glossary> `mandatory`  | `String` Session access token from Create Order response.       | FFF3D2D1-5B20-C1BC-728B-08E47A374D00                                                     |
| <Glossary>Content-Type</Glossary> `mandatory` | `String` Content type.                                          | application/json                                                                         |

#### Option 2: Order ID & Merchant Key Authentication

| Header                                                 | Description                                               | Example                              |
| :----------------------------------------------------- | :-------------------------------------------------------- | :----------------------------------- |
| <Glossary>orderId</Glossary> `mandatory`               | `String` Order ID supplied during order creation.         | ORD123446789                         |
| <Glossary>X-Credential-Username</Glossary> `mandatory` | `String` Merchant key.                                    | smsplus                              |
| <Glossary>accessToken</Glossary> `mandatory`           | `String` Session access token from Create Order response. | FFF3D2D1-5B20-C1BC-728B-08E47A374D00 |

### Body Parameters

**Mandatory Parameters**

| Parameter     | Description                                                                                                                                                                                                                 | Example                                         |
| :------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------- |
| encOrderId    | `String` Encrypted order ID from Create Order response (header).                                                                                                                                                            | c422540c33<br />ef9f1259f15f7<br />b916469b7... |
| accessToken   | `String` Access token from Create Order response (header).                                                                                                                                                                  | FFF3D2D1-5B20-C1BC-728B-08E47A374D00            |
| Content-Type  | `String` Media type of the request body.                                                                                                                                                                                    | application/json                                |
| paymentMethod | `Object` Payment method details including payment type, bank code, and additional parameters. For more information, refer to [paymentMethod JSON Object Fields Description](#paymentmethod-json-object-fields-description). | See below                                       |

**Optional Parameters**

| Parameter               | Description                                                                             | Example                                            |
| :---------------------- | :-------------------------------------------------------------------------------------- | :------------------------------------------------- |
| txnId                   | `String` Transaction ID returned from Create Order.                                     | mtx1754396543709                                   |
| offerKeys               | `Array<String>` List of offer keys to apply.                                            | \["OFFER_KEY_1"]                                   |
| promocode               | `Array<String>` List of promo codes to apply.                                           | \["PROMO123"]                                      |
| customer                | `Object` Customer details (if not already provided in Create Order).                    | {"firstName": "John", "email": "john@example.com"} |
| additionalPaymentParams | `Object` Additional payment-specific parameters (e.g., `si` for standing instructions). | {"si": 1}                                          |
| additional_info         | `Object` Extra metadata for the transaction.                                            | {"key": "value"}                                   |

***

## paymentMethod JSON Object Fields Description

**Mandatory Fields**

| Field                  | Description                                                           | Example    |
| :--------------------- | :-------------------------------------------------------------------- | :--------- |
| paymentMethod.name     | `String` Payment method name (e.g., "NetBanking", "UPI", "CC", "DC"). | NetBanking |
| paymentMethod.bankCode | `String` Bank code or payment provider code.                          | ICIB       |

**Optional Fields**

| Field                            | Description                                         | Example    |
| :------------------------------- | :-------------------------------------------------- | :--------- |
| paymentMethod.storeCard          | `Boolean` Whether to store the card for future use. | true       |
| paymentMethod.storeCardToken     | `String` Token for stored card.                     | token123   |
| paymentMethod.storecardTokenType | `String` Type of stored card token.                 | user_opted |

**Conditional Fields**

| Field                     | Description                                                                                                                                    | Example                                          |
| :------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------- |
| paymentMethod.vpa         | `String` UPI Virtual Payment Address. Required for UPI Collect payments.                                                                       | user\@paytm                                      |
| paymentMethod.paymentCard | `Object` Card details object. Required for card payments (CC/DC). Contains `cardNumber`, `cardholderName`, `cvv`, `expiryMonth`, `expiryYear`. | {"cardNumber": "4111111111111111", "cvv": "123"} |

<br />

## Response Parameters

| Parameter               | Description                                                                                                                                   | Example                              |
| :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| result.acsTemplate      | `String` Base64-encoded HTML authentication form. Decode and submit automatically to redirect the customer to the bank/3DS verification page. | PGh0bWw+...                          |
| metaData.txnId          | `String` Merchant transaction ID.                                                                                                             | ORD123                               |
| metaData.txnStatus      | `String` Transaction status (e.g. `Enrolled`, `Initiated`, `Success`).                                                                        | Enrolled                             |
| metaData.unmappedStatus | `String` Internal PayU processing state (e.g. `pending`).                                                                                     | pending                              |
| metaData.referenceId    | `String` PayU unique reference ID.                                                                                                            | 9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d |

<br />

## Sample Response

```json
{
  "result": {
    "acsTemplate": "PGh0bWw+..."
  },
  "metaData": {
    "txnId": "ORD123",
    "txnStatus": "Enrolled",
    "unmappedStatus": "pending",
    "referenceId": "uuid"
  }
}
```

