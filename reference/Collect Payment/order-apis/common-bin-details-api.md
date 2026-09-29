---
title: 'Common Bin Details API '
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Common Bin Details** API is a unified endpoint that returns card BIN information, convenience fee, and optional offer validation in a single call. Use this API for both Web checkout and SDK integrations once a customer starts entering their card details.

When the customer enters the first 6 or more digits of their card:

- PayU identifies the card issuing bank, network/scheme (VISA, MasterCard, RuPay), and category (Credit, Debit, Prepaid).
- PayU checks whether the card is allowed for the merchant and computes applicable convenience fees and GST.
- If `validateOfferRequestDTO` is provided, PayU concurrently validates eligible offers for the card.

**Environment**

|                            |                                                  |
| -------------------------- | ------------------------------------------------ |
| **Test Environment**       | `https://apitest.payu.in/common/binBasedDetails` |
| **Production Environment** | `https://api.payu.in/common/binBasedDetails`     |

## Sample Request

```bash
curl -X POST "https://apitest.payu.in/common/binBasedDetails" \
  -H "Content-Type: application/json" \
  -H "encOrderId: c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312" \
  -H "accessToken: FFF3D2D1-5B20-C1BC-728B-08E47A374D00" \
  -d '{
    "cardNumber": "411111XXXXXX1111",
    "isEncrypted": "N",
    "convenienceFeesFlag": "1",
    "bin": "411111",
    "bankCode": "HDFC",
    "validateOfferRequestDTO": {
      "autoApply": true,
      "offerKeys": ["OFFER_KEY_1"],
      "userDetail": {
        "mobile": "9876543210"
      },
      "paymentDetail": {
        "cardBin": "411111"
      }
    }
  }'
```
```python
import requests
import json

url = "https://apitest.payu.in/common/binBasedDetails"

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

const url = 'https://apitest.payu.in/common/binBasedDetails';

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
            URL url = new URL("https://apitest.payu.in/common/binBasedDetails");
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

$url = 'https://apitest.payu.in/common/binBasedDetails';

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

| Header                                        | Description                                                                                                   | Example                                                          |
| :-------------------------------------------- | :------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------- |
| <Glossary>encOrderId</Glossary> `mandatory`   | `String` Encrypted order identifier obtained from the Create Order response (`transaction.encryptedOrderId`). | c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312 |
| <Glossary>accessToken</Glossary> `mandatory`  | `String` Session access token obtained from Create Order response (`transaction.accessToken`).                | FFF3D2D1-5B20-C1BC-728B-08E47A374D00                             |
| <Glossary>Content-Type</Glossary> `mandatory` | `String` Content type.                                                                                        | application/json                                                 |

### Body Parameters

**Mandatory Parameters**

| Parameter    | Description                                                                                                   | Example                                                          |
| :----------- | :------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------- |
| encOrderId   | `String` Encrypted order identifier obtained from the Create Order response (`transaction.encryptedOrderId`). | c422540c33ef9f1259f15f7b916469b7227dc1d41a76796536885474ddadf312 |
| accessToken  | `String` Session access token obtained from Create Order response (`transaction.accessToken`).                | FFF3D2D1-5B20-C1BC-728B-08E47A374D00                             |
| Content-Type | `String` Content type of the request body.                                                                    | application/json                                                 |
| cardNumber   | `String` Card number or card prefix (minimum 6 digits required for BIN lookup).                               | 411111XXXXXX1111                                                 |

**Optional Parameters**

| Parameter               | Description                                                                                                                                                     | Example            |
| :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------- |
| isEncrypted             | `String` Encryption indicator: `N` for plain card number, `Y` for RSA-encrypted (default is `Y`).                                                               | N                  |
| convenienceFeesFlag     | `String` Pass `"1"` to compute convenience fees for this card. Default is `"1"`.                                                                                | 1                  |
| bin                     | `String` First 6 digits of the card number.                                                                                                                     | 411111             |
| cardToken               | `String` Tokenized card reference when processing saved/tokenized cards.                                                                                        | token123           |
| userCredentials         | `String` Merchant identifier and customer user ID in format `merchantkey:userid`.                                                                               | smsplus:user_456   |
| bankCode                | `String` Bank code for the card (replaces legacy `bank_code`).                                                                                                  | HDFC               |
| cccat                   | `String` Card category (e.g. `emi`).                                                                                                                            | emi                |
| validateOfferRequestDTO | `Object` Sub-object to simultaneously validate offers against the card BIN. Contains `autoApply`, `offerKeys`, `userDetail`, `paymentDetail`, and `skusDetail`. | See sample request |

## Sample Response

```json
{
  "convenienceFee": "536.35",
  "gst": "96.54",
  "category": "CreditCard",
  "bankCode": "CC",
  "binLevel": false,
  "issuingBank": "HDFC",
  "scheme": "VISA",
  "isDomestic": true,
  "allowCard": true,
  "isOtpOnTheFly": "0.0",
  "message": "Success",
  "validateOfferResponseDTO": {
    "code": "200",
    "message": "Offer Validated Successfully",
    "status": 1,
    "result": {
      "clientId": 42693,
      "mid": 180012,
      "amount": 10000,
      "paymentCode": "CC",
      "category": "CREDITCARD",
      "isValid": true,
      "isSkuOffer": false,
      "isSubventedOffer": false,
      "autoApply": true,
      "offerDiscount": {
        "offerKey": "OFFER_KEY_1",
        "offerType": "INSTANT",
        "discount": 1000,
        "discountedAmount": 9000,
        "discountType": "PERCENTAGE"
      },
      "offerDetail": {
        "offerId": 127770,
        "offerKey": "OFFER_KEY_1",
        "offerType": "INSTANT",
        "title": "10% Off",
        "description": "10% instant discount",
        "validFrom": "2026-01-01 00:00:00",
        "validTo": "2026-12-31 23:59:59",
        "discountType": "PERCENTAGE",
        "offerPercentage": 10,
        "maxDiscountPerTxn": 9999999999,
        "minTxnAmount": 100,
        "maxTxnAmount": 9999999999,
        "status": "ACTIVE",
        "isNce": false,
        "isSkuOffer": false,
        "isSubventedOffer": false,
        "isBaseOffer": false,
        "amount": 10000,
        "discount": 1000,
        "discountedAmount": 9000,
        "isValid": true,
        "recordType": "OFFER"
      },
      "offers": [],
      "totalDiscountDetail": {
        "totalCashbackDiscount": 0,
        "totalInstantDiscount": 1000,
        "totalDiscountedAmount": 9000
      },
      "skusDetail": null
    }
  }
}
```
## Response Parameters

| Parameter                | Description                                                                                         | Example    |
| :----------------------- | :-------------------------------------------------------------------------------------------------- | :--------- |
| convenienceFee           | `String` Convenience fee amount applicable on this card.                                            | 536.35     |
| gst                      | `String` Applicable GST on the convenience fee.                                                     | 96.54      |
| category                 | `String` Card category (e.g., `CreditCard`, `DebitCard`).                                           | CreditCard |
| bankCode                 | `String` Payment code or ibibo code for routing.                                                    | CC         |
| binLevel                 | `Boolean` `true` if configuration is at BIN level, `false` if at category level.                    | false      |
| issuingBank              | `String` Name of the issuing bank (e.g., `HDFC`, `ICICI`).                                          | HDFC       |
| scheme                   | `String` Card network/scheme (e.g., `VISA`, `MASTERCARD`, `RUPAY`).                                 | VISA       |
| isDomestic               | `Boolean` Indicates whether the card was issued in India (`true`) or internationally (`false`).     | true       |
| allowCard                | `Boolean` Indicates if this card is enabled/permitted for the merchant account.                     | true       |
| isOtpOnTheFly            | `String` OTP-on-the-fly capability flag.                                                            | 0.0        |
| message                  | `String` Status message of the BIN evaluation.                                                      | Success    |
| validateOfferResponseDTO | `Object` Offer validation result containing discount details if `validateOfferRequestDTO` was sent. |            |

## Error Responses

| HTTP Status | Message                                              | Condition                                              |
| :---------- | :--------------------------------------------------- | :----------------------------------------------------- |
| `400`       | Invalid request                                      | `cardNumber` missing or shorter than 6 characters.     |
| `400`       | Order ID and Merchant ID is required in request body | Missing `encOrderId` or invalid session headers.       |
| `400`       | Card Not Allowed                                     | Card type or BIN is blocked for this merchant account. |
| `401`       | Order Expired                                        | Order session has exceeded TTL.                        |
| `500`       | Error while calculating convenience fee              | Internal pricing engine calculation failure.           |
