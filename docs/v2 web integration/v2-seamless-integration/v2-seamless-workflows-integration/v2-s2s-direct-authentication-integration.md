---
title: Direct Authorization Integration
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
---
title: Cards Direct Authorization Flow - v2 Payment API
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
PayU enables merchants to process direct authorization for pre-authenticated transactions (external MPI/3DSS). This section describes how to integrate with PayU's direct authorization flow. Initiate an authorization request with the payment details provided post a successful authentication through the MPI/3DSS as explained in this API Reference.

In the Direct Authorization Flow, 3DS authentication has already been performed outside PayU. PayU receives the authentication verification values (such as CAVV/ECI) and directly requests transaction authorization from the acquiring bank, bypassing customer redirection.

> 📘 **Note:**
>
> This API is backward compatible and you can continue to use the existing integration parameters to process 3DS 1.0.2 transactions.

### Environment
<V2_payment_envrionment />

## Request header
<V2_payment_header_params />

## Request body
**Mandatory parameters**

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Description</th>
      <th align="left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>accountId</code></td>
      <td><code>String</code> The merchant key provided by PayU during onboarding.</td>
      <td><code>&lt;YOUR_TEST_KEY&gt;</code></td>
    </tr>
    <tr>
      <td><code>txnId</code></td>
      <td><code>String</code> Transaction ID provided by the merchant and this must be unique for every transaction.</td>
      <td><code>ZP6267f0d2996ce</code></td>
    </tr>
    <tr>
      <td><code>amount</code></td>
      <td><code>Number</code> The transaction amount to be charged.</td>
      <td><code>10</code></td>
    </tr>
    <tr>
      <td><code>paymentMethod</code></td>
      <td><code>Object</code> Details about the payment method used. For Direct Authorization Flow:<br/>• name: "CreditCard" or "DebitCard"<br/>• bankCode: Card type code<br/>• paymentCard: Card details object</td>
      <td><code>{"name": "CreditCard", "bankCode": "CC"}</code></td>
    </tr>
    <tr>
      <td><code>order</code></td>
      <td><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a>.</td>
      <td></td>
    </tr>
    <tr>
      <td><code>additionalInfo</code></td>
      <td><code>Object</code> Additional information including S2S flow configuration. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a>.</td>
      <td></td>
    </tr>
    <tr>
      <td><code>callBackActions</code></td>
      <td><code>Object</code> Actions to perform on the payment server in different scenarios. For more information, refer to <a href="#callbackactions-object-fields-description">callBackActions object fields description</a>.</td>
      <td></td>
    </tr>
    <tr>
      <td><code>billingDetails</code></td>
      <td><code>Object</code> Billing details of the customer including name, address, phone number, email, etc. For more information, refer to <a href="#billingdetails-object-fields-description">billingDetails object fields description</a>.</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Conditional parameters**

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Description</th>
      <th align="left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>authorization</code></td>
      <td><code>Object</code> 3DS authorization information received from MPI/3DSS for direct authentication. Mandatory for S2S Direct Auth. For more information, refer to <a href="#authorization-object-fields-description">authorization object fields description</a>.</td>
      <td></td>
    </tr>
  </tbody>
</table>

**Optional parameters**

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Description</th>
      <th align="left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>threeDS2RequestData</code></td>
      <td><code>Object</code> 3DS2 protocol request data for 3DS 2.x transactions. For more information, refer to <a href="#threeds2requestdata-object-fields-description">threeDS2RequestData object fields description</a>.</td>
      <td></td>
    </tr>
  </tbody>
</table>

### paymentMethod object fields description
<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>name<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the payment mode code. Use "CreditCard" or "DebitCard". For more information, refer to <a href="https://docs.payu.in/v1/docs/payment-mode-codes">Payment Mode Codes</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>CreditCard</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankCode<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> This field must contain the card type code. For more information, refer to <a href="https://docs.payu.in/v1/docs/card-type-codes-and-supported-banks-for-cards">Card Type Codes and Supported Banks for Cards</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>CC</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentCard<br><code>mandatory for cards</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> This object contains physical card details or saved card token details. For more information, refer to <a href="#paymentcard-object-fields-description">paymentCard object fields description</a>.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### paymentCard object fields description
<V2_paymentCard />

### order object fields description
<V2_order_object />

### additionalInfo object fields description
<AdditionalI_Info_object />

**Direct Authorization Flow-specific parameters:**

**Conditional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `txnS2sFlow` | `String` Indicates the transaction S2S flow type. Must be set to `"3"` for Direct Authorization Flow. Mandatory for Direct Auth. | `3` |

**Optional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `createOrder` | `Boolean` Whether to create an order during the payment process. | `false` |
| `placeOrder` | `Boolean` Use to indicate if saved order details should be utilized. | `false` |

### callBackActions object fields description
<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>successAction<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> URL where the customer is redirected upon successful transaction.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><redacted URL></p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>failureAction<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> URL where the customer is redirected upon failed transaction.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><redacted URL></p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cancelAction<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> URL where the customer is redirected if the transaction is cancelled.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><redacted URL></p></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### billingDetails object fields description
<BillingDetails_object />

### authorization object fields description
<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>eci<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Electronic Commerce Indicator returned by the directory server/MPI.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>05</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cavv<br><code>mandatory</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Cardholder Authentication Verification Value generated by the issuing bank.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>AAABAWFlmQAAAABjRWWZEEFgFz</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>flowType<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Authentication flow type: "Frictionless" or "Challenge".</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Frictionless</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>threeDSTransID<br><code>mandatory for 3DS2</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Universally unique transaction identifier assigned by the 3DS Server.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>67b4c71f-19bf-4d97-bd09-4e3687dc9e42</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>threeDSServerTransID<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> 3DS Server transaction ID.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>eea30d14-71cf-41af-b961-f95b7d67dc93</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>threeDSTransStatus<br><code>mandatory for 3DS2</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Transaction status from the 3DS authentication (e.g., "Y", "A").</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Y</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>threeDSTransStatusReason<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Status reason code provided if transaction status is not "Y".</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>01</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>acquirer_bin<br><code>optional</code></p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Acquiring bank Bank Identification Number (BIN).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>401200</p></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### threeDS2RequestData object fields description
<ThreeDSRequestData_object />

## Sample request

```bash
curl --location 'https://apitest.payu.in/v2/payments' \
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
        "productInfo": "Direct Authorization Payment",
        "orderedItem": [
            {
                "itemId": "1",
                "description": "Product Description",
                "quantity": 1,
                "amount": 10.0
            }
        ],
        "paymentChargeSpecification": {
            "price": 10,
            "netAmountDebit": 10
        }
    },
    "additionalInfo": {
        "createOrder": false,
        "placeOrder": false,
        "txnS2sFlow": "3"
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
    },
    "authorization": {
        "eci": "05",
        "cavv": "AAABAWFlmQAAAABjRWWZEEFgFz",
        "flowType": "Frictionless",
        "threeDSTransID": "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
        "threeDSServerTransID": "eea30d14-71cf-41af-b961-f95b7d67dc93",
        "threeDSTransStatus": "Y",
        "threeDSTransStatusReason": "01",
        "acquirer_bin": "401200"
    },
    "threeDS2RequestData": {
        "threeDSVersion": "2.2.0",
        "deviceChannel": "APP"
    }
}'
```
```python
import requests
import json

url = "https://apitest.payu.in/v2/payments"

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
        "productInfo": "Direct Authorization Payment",
        "orderedItem": [
            {
                "itemId": "1",
                "description": "Product Description",
                "quantity": 1,
                "amount": 10.0
            }
        ],
        "paymentChargeSpecification": {
            "price": 10,
            "netAmountDebit": 10
        }
    },
    "additionalInfo": {
        "createOrder": False,
        "placeOrder": False,
        "txnS2sFlow": "3"
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
    },
    "authorization": {
        "eci": "05",
        "cavv": "AAABAWFlmQAAAABjRWWZEEFgFz",
        "flowType": "Frictionless",
        "threeDSTransID": "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
        "threeDSServerTransID": "eea30d14-71cf-41af-b961-f95b7d67dc93",
        "threeDSTransStatus": "Y",
        "threeDSTransStatusReason": "01",
        "acquirer_bin": "401200"
    },
    "threeDS2RequestData": {
        "threeDSVersion": "2.2.0",
        "deviceChannel": "APP"
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
        "productInfo" => "Direct Authorization Payment",
        "orderedItem" => [
            [
                "itemId" => "1",
                "description" => "Product Description",
                "quantity" => 1,
                "amount" => 10.0
            ]
        ],
        "paymentChargeSpecification" => [
            "price" => 10,
            "netAmountDebit" => 10
        ]
    ],
    "additionalInfo" => [
        "createOrder" => false,
        "placeOrder" => false,
        "txnS2sFlow" => "3"
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
    ],
    "authorization" => [
        "eci" => "05",
        "cavv" => "AAABAWFlmQAAAABjRWWZEEFgFz",
        "flowType" => "Frictionless",
        "threeDSTransID" => "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
        "threeDSServerTransID" => "eea30d14-71cf-41af-b961-f95b7d67dc93",
        "threeDSTransStatus" => "Y",
        "threeDSTransStatusReason" => "01",
        "acquirer_bin" => "401200"
    ],
    "threeDS2RequestData" => [
        "threeDSVersion" => "2.2.0",
        "deviceChannel" => "APP"
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

public class DirectAuthRequest {
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
                "productInfo": "Direct Authorization Payment",
                "paymentChargeSpecification": {
                    "price": 10,
                    "netAmountDebit": 10
                }
            },
            "additionalInfo": {
                "createOrder": false,
                "placeOrder": false,
                "txnS2sFlow": "3"
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
            },
            "authorization": {
                "eci": "05",
                "cavv": "AAABAWFlmQAAAABjRWWZEEFgFz",
                "flowType": "Frictionless",
                "threeDSTransID": "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
                "threeDSTransStatus": "Y",
                "acquirer_bin": "401200"
            }
        }
        """;
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://apitest.payu.in/v2/payments"))
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
const url = "https://apitest.payu.in/v2/payments";

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
        productInfo: "Direct Authorization Payment",
        paymentChargeSpecification: {
            price: 10,
            netAmountDebit: 10
        }
    },
    additionalInfo: {
        createOrder: false,
        placeOrder: false,
        txnS2sFlow: "3"
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
    },
    authorization: {
        eci: "05",
        cavv: "AAABAWFlmQAAAABjRWWZEEFgFz",
        flowType: "Frictionless",
        threeDSTransID: "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
        threeDSTransStatus: "Y",
        acquirer_bin: "401200"
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
    "status": "SUCCESS",
    "result": {
        "paymentId": "21667772394",
        "referenceId": "ZP6267f0d2996ce"
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Direct authorization outcome status (SUCCESS, FAILED).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>SUCCESS</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.paymentId</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique identifier for the payment transaction generated by PayU.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>21667772394</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.referenceId</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchant transaction reference identifier corresponding to the txnId provided in the request.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ZP6267f0d2996ce</p></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

> 📘 **Reference:**
>
> To check the transaction status, refer to [Verify Payment API](https://docs.payu.in/v2/reference/v2_verify_payment_api). The Verify Payment API provides complete transaction confirmation and settlement status.

## Sample Responses

### Success Response

```json
{
  "status": "SUCCESS",
  "result": {
    "paymentId": "21667772394",
    "referenceId": "ZP6267f0d2996ce"
  }
}
```

### Pending Response

```json
{
  "status": "PENDING",
  "result": {
    "paymentId": "21667772394",
    "referenceId": "ZP6267f0d2996ce"
  },
  "message": "Awaiting final confirmation from bank"
}
```

### Failure Response

```json
{
  "status": "FAILED",
  "error": {
    "code": "PAYMENT_DECLINED",
    "message": "Declined by issuing bank"
  },
  "result": {
    "paymentId": "21667772394",
    "referenceId": "ZP6267f0d2996ce"
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

1. **Verify transaction** using [Verify Payment API](ref:v2_verify_payment_api)
2. **Handle webhooks** for asynchronous transaction status updates
3. **Check Dashboard** for settlement and reconciliation

> ⚠️ Always verify payment status before order fulfillment.
