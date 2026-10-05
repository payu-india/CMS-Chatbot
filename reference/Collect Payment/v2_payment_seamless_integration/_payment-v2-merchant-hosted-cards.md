---
title: Cards  - v2 Payment API
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
You can collect payments from customers with credit and debit cards using the Merchant Hosted (seamless) integration.

You need to pass `"CreditCard"` or `"DebitCard"` for `paymentMethod.name`, the card provider code (e.g. `CC`, `MAST`, `VISA`, `RUPAY`) for `paymentMethod.bankCode`, and the card details or saved card token in `paymentMethod.paymentCard`.

<Callout icon="📘" theme="info">
  **International Cards**: PayU accepts domestic and international cards. International card processing must be enabled for your account by the PayU Integration and Risk teams.
</Callout>

**Environment**

<V2_payment_envrionment />

## Request header

<V2_payment_header_params />

## Request body

Here is the converted table, split into **Mandatory** and **Optional** parameters with the `mandatory`/`optional` labels removed from the Parameter column:

***

**Mandatory parameters**

| Parameter       | Description                                                                                                                                    | Example           |
| :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- | :---------------- |
| accountId       | The unique merchant key provided by PayU. Character limit: 50.                                                                                 | MERCHANT123       |
| txnId           | Transaction ID for transaction tracking. Must be unique for every transaction. Character limit: 50.                                            | TXN_CARD_20261005 |
| currency        | Three-letter ISO currency code. Must be `"INR"`.                                                                                               | INR               |
| paymentMethod   | Card payment details including card number, expiry, CVV, or saved token. See [paymentMethod object](#paymentmethod-object-fields-description). | Object            |
| order           | Transaction order details such as product info and price. See [order object](#order-object-fields-description).                                | Object            |
| additionalInfo  | Transaction flow options and order flags. See [additionalInfo object](#additionalinfo-object-fields-description).                              | Object            |
| callBackActions | Redirection URLs following 3DS authentication. See [callBackActions object](#callbackactions-object-fields-description).                       | Object            |
| billingDetails  | Customer billing details including name, phone, email, and address. See [billingDetails object](#billingdetails-object-fields-description).    | Object            |

**Optional parameters**

| Parameter     | Description                                                                                                                                                                                                                            | Example |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| authorization | Pre-authenticated 3DS 2.0 metadata (ECI, CAVV, 3DS Trans ID) if the merchant performs 3DS authentication directly. For more information, refer to [authorization object fields description.](#authorization-object-fields-description) | Object  |

### paymentMethod object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>name</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card instrument type. Set to <code>"CreditCard"</code> or <code>"DebitCard"</code>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CreditCard</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>bankCode</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card network/provider code. Valid values: <code>CC</code> (generic credit), <code>DC</code> (generic debit), <code>MAST</code>, <code>VISA</code>, <code>RUPAY</code>, <code>AMEX</code>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CC</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>paymentCard</strong><br/><code>mandatory for cards</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Contains physical card or saved card token details. See <a href="#paymentcard-object-fields-description">paymentCard object</a>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">Object</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentCard object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Field</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">cardNumber<br/><code>mandatory for new card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card number (13–19 digits). Must pass Luhn check. Omit when using saved card token.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">5497774415170603</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">validThrough<br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card expiry date formatted as <code>MM/YYYY</code>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">12/2026</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">ownerName<br/><code>mandatory for new card</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Cardholder name as printed on card.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">John Doe</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">cvv<br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Card verification code (3 digits; 4 digits for AMEX).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">123</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">cardToken<br/><code>mandatory for saved cards</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Network or PayU token string. Replaces <code>cardNumber</code> and <code>ownerName</code>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">token_123456</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">cardTokenType<br/><code>mandatory for saved cards</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Token type: <code>PAYU</code>, <code>NETWORK</code>, or <code>ISSUER</code>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">NETWORK</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### order object fields description

<V2_order_object />

### additionalInfo object fields description

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Description</th>
  <th style="border: 1px solid #ddd; padding: 8px; background-color: #f2f2f2;">Example</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>txnS2sFlow</strong><br/><code>mandatory</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Flow configuration. Set to <code>"4"</code> for seamless 3DS redirection.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">4</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><strong>createOrder</strong><br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Flag to store order details in PayU (<code>true</code> / <code>false</code>).</td>
  <td style="border: 1px solid #ddd; padding: 8px;">true</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;">enforcePaymethod<br/><code>optional</code></td>
  <td style="border: 1px solid #ddd; padding: 8px;">Enforces card mode. Set to <code>"CC"</code> or <code>"DC"</code>.</td>
  <td style="border: 1px solid #ddd; padding: 8px;">CC</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### callBackActions object fields description

<CallbackActions_object />

### billingDetails object fields description

<BillingDetails_object />

### authorization object fields description

**Mandatory parameters**

| Parameter            | Description                                                                                       | Example                                  |
| :------------------- | :------------------------------------------------------------------------------------------------ | :--------------------------------------- |
| eci                  | Electronic Commerce Indicator returned by Access Control Server (ACS) / Directory Server (DS).    | `"05"`                                   |
| cavv                 | Cardholder Authentication Verification Value (cryptogram validating 3DS authentication).          | `"AAABAWFlmQAAAABjRWWZEEFgFz"`           |
| threeDSTransID       | Universally unique 3DS Transaction Identifier assigned by Directory Server (DS).                  | `"67b4c71f-19bf-4d97-bd09-4e3687dc9e42"` |
| threeDSServerTransID | Transaction ID assigned by the merchant's 3DS Server (MPI).                                       | `"eea30d14-71cf-41af-b961-f95b7d67dc93"` |
| threeDSTransStatus   | Authentication outcome code: `Y` (Authenticated), `A` (Attempted), `C` (Challenge), `N` (Failed). | `"Y"`                                    |
| threeDSenrolled      | Card 3DS enrollment flag: `Y` (Enrolled), `N` (Not Enrolled), `U` (Unable to Verify).             | `"Y"`                                    |
| threeDSstatus        | 3DS 1.x payer authentication status (e.g. `SUCCESS`).                                             | `"SUCCESS"`                              |
| xid                  | Transaction identifier for 3D Secure 1.x protocol (Base64 encoded).                               | `"MDAwMDAwMDAwMDAwMDAwMDEyMzQ="`         |
| pares                | Payer Authentication Response received from issuing bank ACS.                                     | `"eJzVWFmTokoWfrMABXXOtgSL..."`          |

**Optional parameters**

| Parameter                | Description                                                                           | Example                                                                |
| :----------------------- | :------------------------------------------------------------------------------------ | :--------------------------------------------------------------------- |
| threeDSTransStatusReason | Diagnostic reason code explaining why authentication was not successful or exempt.    | `"01"`                                                                 |
| flowType                 | 3DS authentication flow type (`Frictionless` or `Challenge`).                         | `"Frictionless"`                                                       |
| messageDigest            | Security digest value for 3DS 1.x message integrity verification (used with `pares`). | `"3a4df2b5c8e7f9a1d6b0c3e9"`                                           |
| bankData                 | Additional bank-specific authorization payload returned by issuing banks.             | `"fGpDiuSMy8FjxQHDla5kFwVr"`                                           |
| additionalInfo           | Additional MPI metadata: `paymentGatewayIdentifier` and `authenticationFlow`.         | `{"paymentGatewayIdentifier": "MPI_01", "authenticationFlow": "3DS2"}` |

## Sample request

```bash
curl -X POST 'https://apitest.payu.in/v2/payments' \
  -H 'date: Mon, 05 Oct 2026 10:00:00 GMT' \
  -H 'authorization: hmac username="<YOUR_TEST_KEY>", algorithm="sha512", headers="date", signature="<SIGNATURE>"' \
  -H 'content-type: application/json' \
  -d '{
    "accountId": "<YOUR_TEST_KEY>",
    "txnId": "TXN_CARD_20261005",
    "currency": "INR",
    "paymentMethod": {
        "name": "CreditCard",
        "bankCode": "CC",
        "paymentCard": {
            "cardNumber": "5497774415170603",
            "validThrough": "12/2026",
            "cvv": "123",
            "ownerName": "John Doe"
        }
    },
    "order": {
        "productInfo": "Electronics Purchase",
        "paymentChargeSpecification": {
            "price": 1000.00
        },
        "userDefinedFields": {
            "udf1": "card_seamless",
            "udf2": "web_store"
        }
    },
    "additionalInfo": {
        "txnS2sFlow": "4",
        "createOrder": true
    },
    "callBackActions": {
        "successAction": "<redacted URL>",
        "failureAction": "<redacted URL>",
        "cancelAction": "<redacted URL>"
    },
    "billingDetails": {
        "firstName": "John",
        "lastName": "Doe",
        "phone": "9876543210",
        "email": "john.doe@example.com",
        "address1": "123 Main Street",
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India",
        "zipCode": "400001"
    }
}'
```
```python
import requests
import json

url = "https://apitest.payu.in/v2/payments"

headers = {
    "date": "Mon, 05 Oct 2026 10:00:00 GMT",
    "authorization": 'hmac username="<YOUR_TEST_KEY>", algorithm="sha512", headers="date", signature="<SIGNATURE>"',
    "content-type": "application/json"
}

payload = {
    "accountId": "<YOUR_TEST_KEY>",
    "txnId": "TXN_CARD_20261005",
    "currency": "INR",
    "paymentMethod": {
        "name": "CreditCard",
        "bankCode": "CC",
        "paymentCard": {
            "cardNumber": "5497774415170603",
            "validThrough": "12/2026",
            "cvv": "123",
            "ownerName": "John Doe"
        }
    },
    "order": {
        "productInfo": "Electronics Purchase",
        "paymentChargeSpecification": {
            "price": 1000.00
        },
        "userDefinedFields": {
            "udf1": "card_seamless"
        }
    },
    "additionalInfo": {
        "txnS2sFlow": "4",
        "createOrder": True
    },
    "callBackActions": {
        "successAction": "<redacted URL>",
        "failureAction": "<redacted URL>",
        "cancelAction": "<redacted URL>"
    },
    "billingDetails": {
        "firstName": "John",
        "lastName": "Doe",
        "phone": "9876543210",
        "email": "john.doe@example.com",
        "address1": "123 Main Street",
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India",
        "zipCode": "400001"
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```
```php
<?php
$url = "https://apitest.payu.in/v2/payments";

$payload = json_encode([
    "accountId" => "<YOUR_TEST_KEY>",
    "txnId" => "TXN_CARD_20261005",
    "currency" => "INR",
    "paymentMethod" => [
        "name" => "CreditCard",
        "bankCode" => "CC",
        "paymentCard" => [
            "cardNumber" => "5497774415170603",
            "validThrough" => "12/2026",
            "cvv" => "123",
            "ownerName" => "John Doe"
        ]
    ],
    "order" => [
        "productInfo" => "Electronics Purchase",
        "paymentChargeSpecification" => [
            "price" => 1000.00
        ]
    ],
    "additionalInfo" => [
        "txnS2sFlow" => "4",
        "createOrder" => true
    ],
    "callBackActions" => [
        "successAction" => "<redacted URL>",
        "failureAction" => "<redacted URL>",
        "cancelAction" => "<redacted URL>"
    ],
    "billingDetails" => [
        "firstName" => "John",
        "lastName" => "Doe",
        "phone" => "9876543210",
        "email" => "john.doe@example.com",
        "address1" => "123 Main Street",
        "city" => "Mumbai",
        "state" => "Maharashtra",
        "country" => "India",
        "zipCode" => "400001"
    ]
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "date: Mon, 05 Oct 2026 10:00:00 GMT",
    "authorization: hmac username=\"<YOUR_TEST_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<SIGNATURE>\"",
    "content-type: application/json"
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

public class PayUCardRequest {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        
        String payload = """
            {
              "accountId": "<YOUR_TEST_KEY>",
              "txnId": "TXN_CARD_20261005",
              "currency": "INR",
              "paymentMethod": {
                "name": "CreditCard",
                "bankCode": "CC",
                "paymentCard": {
                  "cardNumber": "5497774415170603",
                  "validThrough": "12/2026",
                  "cvv": "123",
                  "ownerName": "John Doe"
                }
              },
              "order": {
                "productInfo": "Electronics Purchase",
                "paymentChargeSpecification": {
                  "price": 1000.00
                }
              },
              "additionalInfo": {
                "txnS2sFlow": "4",
                "createOrder": true
              },
              "callBackActions": {
                "successAction": "<redacted URL>",
                "failureAction": "<redacted URL>",
                "cancelAction": "<redacted URL>"
              },
              "billingDetails": {
                "firstName": "John",
                "lastName": "Doe",
                "phone": "9876543210",
                "email": "john.doe@example.com",
                "address1": "123 Main Street",
                "city": "Mumbai",
                "state": "Maharashtra",
                "country": "India",
                "zipCode": "400001"
              }
            }
            """;
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://apitest.payu.in/v2/payments"))
            .header("date", "Mon, 05 Oct 2026 10:00:00 GMT")
            .header("authorization", "hmac username=\"<YOUR_TEST_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<SIGNATURE>\"")
            .header("content-type", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```
```javascript
const url = "https://apitest.payu.in/v2/payments";

const payload = {
  accountId: "<YOUR_TEST_KEY>",
  txnId: "TXN_CARD_20261005",
  currency: "INR",
  paymentMethod: {
    name: "CreditCard",
    bankCode: "CC",
    paymentCard: {
      cardNumber: "5497774415170603",
      validThrough: "12/2026",
      cvv: "123",
      ownerName: "John Doe"
    }
  },
  order: {
    productInfo: "Electronics Purchase",
    paymentChargeSpecification: {
      price: 1000.00
    }
  },
  additionalInfo: {
    txnS2sFlow: "4",
    createOrder: true
  },
  callBackActions: {
    successAction: "<redacted URL>",
    failureAction: "<redacted URL>",
    cancelAction: "<redacted URL>"
  },
  billingDetails: {
    firstName: "John",
    lastName: "Doe",
    phone: "9876543210",
    email: "john.doe@example.com",
    address1": "123 Main Street",
    city: "Mumbai",
    state: "Maharashtra",
    country: "India",
    zipCode: "400001"
  }
};

fetch(url, {
  method: "POST",
  headers: {
    "date": "Mon, 05 Oct 2026 10:00:00 GMT",
    "authorization": 'hmac username="<YOUR_TEST_KEY>", algorithm="sha512", headers="date", signature="<SIGNATURE>"',
    "content-type": "application/json"
  },
  body: JSON.stringify(payload)
})
  .then(res => res.json())
  .then(data => console.log(data))
  .catch(err => console.error("Error:", err));
```

## Sample response

The card payment response returns a `checkoutUrl` to redirect the customer to their bank's 3DS OTP verification page:

```json
{
  "status": "PENDING",
  "result": {
    "checkoutUrl": "<redacted URL>"
  },
  "txnId": "TXN_CARD_20261005",
  "paymentId": "1999110000001769",
  "message": "Redirect customer to checkoutUrl for 3DS authentication"
}
```

## Response parameters

<V2_payment_response_params />

<Callout icon="📘" theme="info">
  ### **Reference:**

  To check the final status of the transaction following 3DS redirection, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api).
</Callout>

## Error Codes

| Code                    | HTTP Status | Description                             | Resolution                                  |
| :---------------------- | :---------- | :-------------------------------------- | :------------------------------------------ |
| `INVALID_CARD_NUMBER`   | 400         | Card number failed Luhn validation      | Check card number formatting                |
| `INVALID_EXPIRY`        | 400         | Expiry date expired or format incorrect | Use `MM/YYYY` format with valid future date |
| `INVALID_AMOUNT`        | 400         | Invalid amount value                    | Ensure `price` is positive number           |
| `INVALID_CURRENCY`      | 400         | Unsupported currency                    | Set `currency: "INR"`                       |
| `AUTHENTICATION_FAILED` | 401         | Invalid token / signature               | Verify HMAC SHA512 signature                |
| `DUPLICATE_REFERENCE`   | 409         | `txnId` already used                    | Use unique transaction ID                   |
| `PAYMENT_DECLINED`      | 422         | Card issuer declined transaction        | Customer should contact issuing bank        |

## Next Steps

## Next Steps

1. **Handle Customer 3DS Authentication**:
   - Inspect the `result.paymentUrl` or redirection payload returned in the API response.
   - Redirect the customer or render the 3D Secure ACS challenge screen in an in-app browser/webview to complete two-factor authentication (OTP / Biometric).
2. **Process Post-Authentication Callback**:
   - Listen on your configured `callBackActions.termAction` or `callBackActions.successAction` for the final transaction response from the issuing bank.
3. **Verify Transaction Integrity**:
   - Calculate and verify the response hash to confirm authenticity.
   - Perform a server-to-server transaction status check using the [Verify Payment API](ref:v2_verify_payment_api) before fulfilling the order.
4. **Support Saved Cards & Tokenization**:
   - If the customer opted to save their card, store the returned `cardToken` and `cardTokenType` to enable seamless one-click checkouts for future visits.
