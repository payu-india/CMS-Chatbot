---
title: Using Network Tokens
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Collecting Payments from Saved card using Tokens
  description: >-
    Discover how to use the _payment API to process payments with saved card
    tokens. This guide provides detailed instructions, request parameters, and
    sample responses for collecting payment with saved card tokens.
  robots: index
next:
  description: ''
---
This scenario is applicable if you wanted to collect payments using network tokens.

HTTP Method: **POST**

## Applicable scenarios

* Merchant has the card token, TAVV(Cryptogram), and the last four digits of the card 
* The token could be created by the merchant or through another partner 

<Callout icon="📘" theme="info">
  **Note**: This scenario is applicable if you are PCI compliant and got the network token and TAVV from any other aggregator or schemes and then sending the card transaction request in the form of authentication.
</Callout>

## Request headers

<V2_payment_header_params />

## Request Parameters



### `paymentMethod` Object (Network Token)

The table has 7 rows, so here it is in **HTML format**:

**Mandatory parameters**

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>name</code></td>
      <td><code>String</code> Set to <code>"CreditCard"</code> or <code>"DebitCard"</code>.</td>
    </tr>
    <tr>
      <td><code>paymentCard</code></td>
      <td><code>Object</code> Token details issued by the card network.</td>
    </tr>
    <tr>
      <td><code>paymentCard.cardToken</code></td>
      <td><code>String</code> Network token string issued by Visa, Mastercard, or RuPay.</td>
    </tr>
    <tr>
      <td><code>paymentCard.cardTokenType</code></td>
      <td><code>String</code> Set to <code>"NETWORK"</code>.</td>
    </tr>
    <tr>
      <td><code>paymentCard.tavv</code></td>
      <td><code>String</code> Dynamic cryptogram generated for the transaction (obtained via <strong><a href="./v2-get-payment-details-api.md">Get Payment Details API</a></strong>).</td>
    </tr>
    <tr>
      <td><code>paymentCard.last4Digits</code></td>
      <td><code>String</code> Last 4 digits of the underlying primary account number (e.g. <code>"2346"</code>).</td>
    </tr>
  </tbody>
</table>

**Optional parameters**

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>paymentCard.cvv</code></td>
      <td><code>String</code> 3-digit CVV (if required by merchant terminal profile).</td>
    </tr>
  </tbody>
</table>

### Sample Request
```bash
curl --location --request POST '<redacted URL>' \
--header 'Content-Type: application/json' \
--header 'Date: Mon, 05 Oct 2026 08:30:00 GMT' \
--header 'Authorization: hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"' \
--data-raw '{
  "accountId": "merchant_key",
  "txnId": "TXN_NETTOK_1728135000",
  "order": {
    "currency": "INR",
    "paymentChargeSpecification": {
      "price": 1000.00
    }
  },
  "customer": {
    "email": "customer@example.com",
    "phone": "9876543210",
    "name": "Jane Smith"
  },
  "paymentMethod": {
    "name": "CreditCard",
    "paymentCard": {
      "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
      "cardTokenType": "NETWORK",
      "tavv": "/wAAAAAAPtP+g6IAmbSeg1gAAAA=",
      "last4Digits": "2346",
      "cvv": "123"
    }
  },
  "billingDetails": {
    "address1": "456 Commerce Avenue",
    "city": "Mumbai",
    "state": "Maharashtra",
    "country": "India",
    "postalCode": "400001"
  },
  "callBackActions": {
    "successAction": "<redacted URL>",
    "failureAction": "<redacted URL>",
    "cancelAction": "<redacted URL>",
    "termAction": "<redacted URL>"
  },
  "additionalInfo": {
    "txnS2sFlow": "4"
  }
}'
```
```python
import requests
import json

url = "<redacted URL>"

payload = {
    "accountId": "merchant_key",
    "txnId": "TXN_NETTOK_1728135000",
    "order": {
        "currency": "INR",
        "paymentChargeSpecification": {
            "price": 1000.00
        }
    },
    "customer": {
        "email": "customer@example.com",
        "phone": "9876543210",
        "name": "Jane Smith"
    },
    "paymentMethod": {
        "name": "CreditCard",
        "paymentCard": {
            "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
            "cardTokenType": "NETWORK",
            "tavv": "/wAAAAAAPtP+g6IAmbSeg1gAAAA=",
            "last4Digits": "2346",
            "cvv": "123"
        }
    },
    "billingDetails": {
        "address1": "456 Commerce Avenue",
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India",
        "postalCode": "400001"
    },
    "callBackActions": {
        "successAction": "<redacted URL>",
        "failureAction": "<redacted URL>",
        "cancelAction": "<redacted URL>",
        "termAction": "<redacted URL>"
    },
    "additionalInfo": {
        "txnS2sFlow": "4"
    }
}

headers = {
    "Content-Type": "application/json",
    "Date": "Mon, 05 Oct 2026 08:30:00 GMT",
    "Authorization": 'hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```
```php
<?php
$curl = curl_init();

$payload = json_encode([
  "accountId" => "merchant_key",
  "txnId" => "TXN_NETTOK_1728135000",
  "order" => [
    "currency" => "INR",
    "paymentChargeSpecification" => [
      "price" => 1000.00
    ]
  ],
  "customer" => [
    "email" => "customer@example.com",
    "phone" => "9876543210",
    "name" => "Jane Smith"
  ],
  "paymentMethod" => [
    "name" => "CreditCard",
    "paymentCard" => [
      "cardToken" => "29850879bf39848ca078727b8e1a95165a41cea1",
      "cardTokenType" => "NETWORK",
      "tavv" => "/wAAAAAAPtP+g6IAmbSeg1gAAAA=",
      "last4Digits" => "2346",
      "cvv" => "123"
    ]
  ],
  "billingDetails" => [
    "address1" => "456 Commerce Avenue",
    "city" => "Mumbai",
    "state" => "Maharashtra",
    "country" => "India",
    "postalCode" => "400001"
  ],
  "callBackActions" => [
    "successAction" => "<redacted URL>",
    "failureAction" => "<redacted URL>",
    "cancelAction" => "<redacted URL>",
    "termAction" => "<redacted URL>"
  ],
  "additionalInfo" => [
    "txnS2sFlow" => "4"
  ]
]);

curl_setopt_array($curl, [
  CURLOPT_URL => '<redacted URL>',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_POSTFIELDS => $payload,
  CURLOPT_HTTPHEADER => [
    'Content-Type: application/json',
    'Date: Mon, 05 Oct 2026 08:30:00 GMT',
    'Authorization: hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
  ],
]);

$response = curl_exec($curl);
curl_close($curl);
echo $response;
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class NetworkTokenPayment {
    public static void main(String[] args) throws Exception {
        String payload = """
        {
          "accountId": "merchant_key",
          "txnId": "TXN_NETTOK_1728135000",
          "order": {
            "currency": "INR",
            "paymentChargeSpecification": {
              "price": 1000.00
            }
          },
          "customer": {
            "email": "customer@example.com",
            "phone": "9876543210",
            "name": "Jane Smith"
          },
          "paymentMethod": {
            "name": "CreditCard",
            "paymentCard": {
              "cardToken": "29850879bf39848ca078727b8e1a95165a41cea1",
              "cardTokenType": "NETWORK",
              "tavv": "/wAAAAAAPtP+g6IAmbSeg1gAAAA=",
              "last4Digits": "2346",
              "cvv": "123"
            }
          },
          "billingDetails": {
            "address1": "456 Commerce Avenue",
            "city": "Mumbai",
            "state": "Maharashtra",
            "country": "India",
            "postalCode": "400001"
          },
          "callBackActions": {
            "successAction": "<redacted URL>",
            "failureAction": "<redacted URL>",
            "cancelAction": "<redacted URL>",
            "termAction": "<redacted URL>"
          },
          "additionalInfo": {
            "txnS2sFlow": "4"
          }
        }
        """;

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("<redacted URL>"))
            .header("Content-Type", "application/json")
            .header("Date", "Mon, 05 Oct 2026 08:30:00 GMT")
            .header("Authorization", "hmac username=\"merchant_key\", algorithm=\"sha512\", headers=\"date\", signature=\"<SIGNATURE>\"")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();

        HttpClient client = HttpClient.newHttpClient();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```
```javascript
const axios = require('axios');

const data = {
  accountId: "merchant_key",
  txnId: "TXN_NETTOK_1728135000",
  order: {
    currency: "INR",
    paymentChargeSpecification: {
      price: 1000.00
    }
  },
  customer: {
    email: "customer@example.com",
    phone: "9876543210",
    name: "Jane Smith"
  },
  paymentMethod: {
    name: "CreditCard",
    paymentCard: {
      cardToken: "29850879bf39848ca078727b8e1a95165a41cea1",
      cardTokenType: "NETWORK",
      tavv: "/wAAAAAAPtP+g6IAmbSeg1gAAAA=",
      last4Digits: "2346",
      cvv: "123"
    }
  },
  billingDetails: {
    address1: "456 Commerce Avenue",
    city: "Mumbai",
    state: "Maharashtra",
    country: "India",
    postalCode: "400001"
  },
  callBackActions: {
    successAction: "<redacted URL>",
    failureAction: "<redacted URL>",
    cancelAction: "<redacted URL>",
    termAction: "<redacted URL>"
  },
  additionalInfo: {
    txnS2sFlow: "4"
  }
};

const config = {
  method: 'post',
  url: '<redacted URL>',
  headers: { 
    'Content-Type': 'application/json',
    'Date': 'Mon, 05 Oct 2026 08:30:00 GMT',
    'Authorization': 'hmac username="merchant_key", algorithm="sha512", headers="date", signature="<SIGNATURE>"'
  },
  data: data
};

axios(config)
  .then(response => console.log(JSON.stringify(response.data)))
  .catch(error => console.error(error));
```

***

## Response Parameters

| Parameter                  | Type   | Description                                            |
| :------------------------- | :----- | :----------------------------------------------------- |
| **status**                 | String | Transaction state: `PENDING`, `SUCCESS`, or `FAILURE`. |
| **message**                | String | Status description.                                    |
| **result**                 | Object | Execution metadata.                                    |
| **result.paymentId**       | String | PayU transaction identifier (`mihpayId`).              |
| **result.txnId**           | String | Merchant transaction identifier.                       |
| **result.authAction**      | Object | Redirection challenge metadata.                        |
| **result.authAction.type** | String | Method of challenge: `REDIRECT`.                       |
| **result.authAction.url**  | String | 3DS Access Control Server (ACS) redirection endpoint.  |

### Sample Response

```json
{
  "status": "PENDING",
  "message": "Payment initiated successfully. Please redirect the customer to complete 3D Secure authentication.",
  "result": {
    "paymentId": "403993715535615888",
    "txnId": "TXN_NETTOK_1728135000",
    "authAction": {
      "type": "REDIRECT",
      "url": "<redacted URL>"
    }
  }
}
```


## Next Steps

1. **Complete 3DS Authentication**:
   - Redirect the cardholder to `result.authAction.url` to complete issuing bank challenge verification.
2. **Handle Postbacks**:
   - Capture authentication response at `callBackActions.termAction` or `callBackActions.successAction`.
3. **Verify Transaction State**:
   - Query the **[Verify Payment API](./v2_verify_payment_api.md)** to verify payment capture.
