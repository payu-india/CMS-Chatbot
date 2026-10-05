---
title: Classic Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
table_of_contents: true
---
---
title: Cards Classic Integration - v2 Payment API
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
You can collect card payments using classic seamless integration. For seamless Classic integration, the **additionalInfo.txnS2sFlow** field is set to **4**.

The Classic Seamless Integration supports both physical card details and saved card tokens, providing a complete server-to-server payment solution with 3DS authentication redirection.

## Environment
<V2_payment_envrionment />

## Request header
<V2_payment_header_params />

## Request body
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

### paymentMethod object fields description
**Mandatory parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `name` | `String` This field must contain the payment mode code. For Classic Integration, use "CreditCard" or "DebitCard". For more information, refer to [Payment Mode Codes](https://docs.payu.in/v1/docs/payment-mode-codes). | `CreditCard` |
| `bankCode` | `String` This field must contain the card type code. For more information, refer to [Card Type Codes and Supported Banks for Cards](https://docs.payu.in/v1/docs/card-type-codes-and-supported-banks-for-cards). | `CC` |

**Conditional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `paymentCard` | `Object` This object contains the physical card or saved card token details. For more information, refer to [paymentCard object fields description](#paymentcard-object-fields-description). Mandatory for cards. | |

### paymentCard object fields description
<V2_paymentCard />

### order object fields description
<V2_order_object />

### additionalInfo object fields description

**Conditional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `txnS2sFlow` | `String` Indicates the transaction S2S flow type and must be set to `"4"` for Classic Integration. Mandatory for S2S. | `4` |

**Recommended parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `authenticationFlow` | `String` Indicates the authentication flow type. Set to `"REDIRECT"` for Classic 3DS redirection. | `REDIRECT` |

**Optional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `createOrder` | `Boolean` Whether to create an order during the payment process. | `false` |
| `preAuthorize` | `String` Set to `"1"` for authorization-only transactions. | `1` |

### callBackActions object fields description
**Mandatory parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `successAction` | `String` URL where the customer is redirected upon successful payment. | `<redacted URL>` |
| `failureAction` | `String` URL where the customer is redirected upon failed payment. | `<redacted URL>` |

**Optional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `cancelAction` | `String` URL where the customer is redirected if the transaction is cancelled. | `<redacted URL>` |

### billingDetails object fields description
<BillingDetails_object />

## Sample request

```curl
curl --location '<redacted URL>' \
--header 'date: <CURRENT_DATE_GMT>' \
--header 'authorization: hmac username="<YOUR_TEST_KEY>", algorithm="sha512", headers="date", signature="<YOUR_SIGNATURE>"' \
--header 'Content-Type: application/json' \
--data-raw '{
    "accountId": "<YOUR_TEST_KEY>",
    "txnId": "ZP6267f0d2996ce",
    "amount": 10,
    "paymentMethod": {
        "name": "CreditCard",
        "bankCode": "CC",
        "paymentCard": {
            "cardNumber": "5004461234560000",
            "validThrough": "<SANDBOX_CARD_EXPIRY_MM_YY>",
            "ownerName": "John Doe",
            "cvv": "987"
        }
    },
    "order": {
        "productInfo": "Classic Integration Payment",
        "orderedItem": [
            {
                "itemId": "1",
                "description": "Product Description",
                "quantity": 1,
                "amount": 10.0
            }
        ],
        "userDefinedFields": {
            "udf1": "",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": ""
        },
        "paymentChargeSpecification": {
            "price": 10,
            "netAmountDebit": 10
        }
    },
    "additionalInfo": {
        "txnS2sFlow": "4",
        "authenticationFlow": "REDIRECT",
        "createOrder": false
    },
    "callBackActions": {
        "successAction": "<redacted URL>",
        "failureAction": "<redacted URL>",
        "cancelAction": "<redacted URL>"
    },
    "billingDetails": {
        "firstName": "John",
        "lastName": "Doe",
        "address1": "123 Main Street",
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India",
        "zipCode": "400001",
        "phone": "9876543210",
        "email": "john.doe@example.com"
    }
}'
```
```python
import requests
import json

url = "<redacted URL>"

headers = {
    "Content-Type": "application/json",
    "date": "<CURRENT_DATE_GMT>",
    "authorization": "hmac username=\"<YOUR_TEST_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
}

payload = {
    "accountId": "<YOUR_TEST_KEY>",
    "txnId": "ZP6267f0d2996ce",
    "amount": 10,
    "paymentMethod": {
        "name": "CreditCard",
        "bankCode": "CC",
        "paymentCard": {
            "cardNumber": "5004461234560000",
            "validThrough": "<SANDBOX_CARD_EXPIRY_MM_YY>",
            "ownerName": "John Doe",
            "cvv": "987"
        }
    },
    "order": {
        "productInfo": "Classic Integration Payment",
        "paymentChargeSpecification": {
            "price": 10,
            "netAmountDebit": 10
        }
    },
    "additionalInfo": {
        "txnS2sFlow": "4",
        "authenticationFlow": "REDIRECT",
        "createOrder": False
    },
    "callBackActions": {
        "successAction": "<redacted URL>",
        "failureAction": "<redacted URL>",
        "cancelAction": "<redacted URL>"
    },
    "billingDetails": {
        "firstName": "John",
        "lastName": "Doe",
        "address1": "123 Main Street",
        "city": "Mumbai",
        "state": "Maharashtra",
        "country": "India",
        "zipCode": "400001",
        "phone": "9876543210",
        "email": "john.doe@example.com"
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```
```php
<?php
$url = "<redacted URL>";

$payload = json_encode([
    "accountId" => "<YOUR_TEST_KEY>",
    "txnId" => "ZP6267f0d2996ce",
    "amount" => 10,
    "paymentMethod" => [
        "name" => "CreditCard",
        "bankCode" => "CC",
        "paymentCard" => [
            "cardNumber" => "5004461234560000",
            "validThrough" => "<SANDBOX_CARD_EXPIRY_MM_YY>",
            "ownerName" => "John Doe",
            "cvv" => "987"
        ]
    ],
    "order" => [
        "productInfo" => "Classic Integration Payment",
        "paymentChargeSpecification" => [
            "price" => 10,
            "netAmountDebit" => 10
        ]
    ],
    "additionalInfo" => [
        "txnS2sFlow" => "4",
        "authenticationFlow" => "REDIRECT",
        "createOrder" => false
    ],
    "callBackActions" => [
        "successAction" => "<redacted URL>",
        "failureAction" => "<redacted URL>",
        "cancelAction" => "<redacted URL>"
    ],
    "billingDetails" => [
        "firstName" => "John",
        "lastName" => "Doe",
        "address1" => "123 Main Street",
        "city" => "Mumbai",
        "state" => "Maharashtra",
        "country" => "India",
        "zipCode" => "400001",
        "phone" => "9876543210",
        "email" => "john.doe@example.com"
    ]
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json",
    "date: <CURRENT_DATE_GMT>",
    "authorization: hmac username=\"<YOUR_TEST_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
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

public class ClassicRequest {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        
        String payload = """
        {
            "accountId": "<YOUR_TEST_KEY>",
            "txnId": "ZP6267f0d2996ce",
            "amount": 10,
            "paymentMethod": {
                "name": "CreditCard",
                "bankCode": "CC",
                "paymentCard": {
                    "cardNumber": "5004461234560000",
                    "validThrough": "<SANDBOX_CARD_EXPIRY_MM_YY>",
                    "ownerName": "John Doe",
                    "cvv": "987"
                }
            },
            "order": {
                "productInfo": "Classic Integration Payment",
                "paymentChargeSpecification": {
                    "price": 10,
                    "netAmountDebit": 10
                }
            },
            "additionalInfo": {
                "txnS2sFlow": "4",
                "authenticationFlow": "REDIRECT",
                "createOrder": false
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
                "email": "john.doe@example.com"
            }
        }
        """;
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("<redacted URL>"))
            .header("Content-Type", "application/json")
            .header("date", "<CURRENT_DATE_GMT>")
            .header("authorization", "hmac username=\"<YOUR_TEST_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\"")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();
        
        HttpResponse<String> response = client.send(request,
            HttpResponse.BodyHandlers.ofString());
        
        System.out.println(response.body());
    }
}
```
```javascript
const url = "<redacted URL>";

const payload = {
    accountId: "<YOUR_TEST_KEY>",
    txnId: "ZP6267f0d2996ce",
    amount: 10,
    paymentMethod: {
        name: "CreditCard",
        bankCode: "CC",
        paymentCard: {
            cardNumber: "5004461234560000",
            validThrough: "<SANDBOX_CARD_EXPIRY_MM_YY>",
            ownerName: "John Doe",
            cvv: "987"
        }
    },
    order: {
        productInfo: "Classic Integration Payment",
        paymentChargeSpecification: {
            price: 10,
            netAmountDebit: 10
        }
    },
    additionalInfo: {
        txnS2sFlow: "4",
        authenticationFlow: "REDIRECT",
        createOrder: false
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
        email: "john.doe@example.com"
    }
};

const options = {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "date": "<CURRENT_DATE_GMT>",
        "authorization": "hmac username=\"<YOUR_TEST_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
    },
    body: JSON.stringify(payload)
};

fetch(url, options)
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error("Error:", error));
```

## Sample response
```json
{
    "status": "PENDING",
    "result": {
        "redirectUrl": "https://secure.payu.in/ResponseHandler.php",
        "paymentId": "21667772394",
        "redirectTemplate": "<EXAMPLE_BASE64_REDIRECT_FORM>",
        "card": {
            "binData": {
                "pureS2SSupported": false,
                "issuingBank": "ICICI",
                "category": "creditcard",
                "cardType": "MAST",
                "isDomestic": true
            }
        }
    }
}
```

## Response parameters
<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Status of the initial request (typically PENDING while awaiting redirection and 3DS completion).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PENDING</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.redirectUrl</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>URL where the customer's browser is directed to complete 3DS authentication.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>https://secure.payu.in/ResponseHandler.php</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.paymentId</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique identifier for the payment transaction generated by PayU.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>21667772394</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.redirectTemplate</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Auto-posting HTML/JavaScript form snippet for directing customer browser to bank ACS page.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>&lt;form ...&gt;</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.card.binData.issuingBank</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Name of the issuing bank for the card.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ICICI</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.card.binData.category</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Card category (creditcard, debitcard).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>creditcard</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.card.binData.cardType</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Card scheme/network (VISA, MAST, RUPAY, AMEX).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>MAST</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.card.binData.isDomestic</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Indicates if card was issued domestically.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

> 📘 **Reference:**
>
> To check the transaction status, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api). The Verify Payment API is **mandatory** for Classic Integration to obtain final transaction status.

## Sample Responses

### Success Response (Post 3DS Authentication)

```json
{
  "status": "SUCCESS",
  "result": {
    "paymentId": "21667772394",
    "orderId": "ZP6267f0d2996ce",
    "amount": 10.00,
    "currency": "INR"
  },
  "message": "Transaction successful"
}
```

### Pending Response

```json
{
  "status": "PENDING",
  "result": {
    "paymentId": "21667772394",
    "redirectUrl": "https://secure.payu.in/ResponseHandler.php"
  },
  "message": "Awaiting customer authentication"
}
```

### Failure Response

```json
{
  "status": "FAILED",
  "error": {
    "code": "PAYMENT_DECLINED",
    "message": "Transaction declined by issuing bank"
  },
  "result": {
    "paymentId": "21667772394"
  }
}
```

## Error Codes

| Code | HTTP Status | Description | Resolution |
| ---- | ----------- | ----------- | ---------- |
| `INVALID_AMOUNT` | 400 | Invalid amount value | Check amount format and value |
| `INVALID_CURRENCY` | 400 | Unsupported currency | Use supported currency codes |
| `AUTHENTICATION_FAILED` | 401 | Invalid signature or key | Verify HMAC credentials and signature header |
| `DUPLICATE_REFERENCE` | 409 | Reference ID already used | Use unique transaction reference ID |
| `PAYMENT_DECLINED` | 422 | Payment declined | Issuing bank declined authorization |

> For complete error code list, see [Error Codes Reference](ref:error-codes).

## Next Steps

1. **Redirect Customer** to `redirectUrl` or render `redirectTemplate` to complete 3DS authentication
2. **Verify transaction** using [Verify Payment API](ref:v2_verify_payment_api)
3. **Handle webhooks** for status updates
4. **Check Dashboard** for settlement and reconciliation

> ⚠️ Always verify payment status before order fulfillment.