---
title: UPI Integration
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
title: UPI Flow - v2 Payment API
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
The UPI Seamless Integration allows merchants to process UPI payments directly through a server-to-server (S2S) flow without redirecting customers to external payment pages. This integration provides a smooth payment experience by handling UPI transactions programmatically using customer Virtual Payment Address (VPA) for UPI Collect or generating payment intents for mobile UPI apps.

## When to Use UPI Seamless Integration
Use this integration when:

* You want to accept UPI payments without redirecting customers away from your checkout interface
* You support UPI Intent on mobile apps (directly invoking Google Pay, PhonePe, Paytm, BHIM, etc.)
* You support UPI Collect by soliciting the customer's VPA and sending a collect request
* You want faster transaction processing and direct programmatic control over UPI payments

### Environment
<V2_payment_envrionment />

## Request header
<V2_payment_header_params />

## Request parameters
The table has 8 rows, so here it is in **HTML format**:

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
      <td><code>424.38</code></td>
    </tr>
    <tr>
      <td><code>paymentMethod</code></td>
      <td><code>Object</code> Details about the payment method used. For UPI, specify name as "UPI" and bankCode as "UPI".</td>
      <td><code>{"name": "UPI", "bankCode": "UPI"}</code></td>
    </tr>
    <tr>
      <td><code>order</code></td>
      <td><code>Object</code> Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to <a href="#order-object-fields-description">order object fields description</a>.</td>
      <td></td>
    </tr>
    <tr>
      <td><code>additionalInfo</code></td>
      <td><code>Object</code> Additional information including S2S flow configuration and customer VPA. For more information, refer to <a href="#additionalinfo-object-fields-description">additionalInfo object fields description</a>.</td>
      <td></td>
    </tr>
    <tr>
      <td><code>callBackActions</code></td>
      <td><code>Object</code> Actions to perform on the payment server in different scenarios. For more information, refer to <a href="#callbackactions-object-fields-description">callBackActions object fields description</a>.</td>
      <td></td>
    </tr>
    <tr>
      <td><code>billingDetails</code></td>
      <td><code>Object</code> Billing details of the customer including name, phone number, and email. For more information, refer to <a href="#billingdetails-object-fields-description">billingDetails object fields description</a>.</td>
      <td></td>
    </tr>
  </tbody>
</table>
## paymentMethod object fields description
**Mandatory parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `name` | `String` Payment mode name. Must be set to `"UPI"`. | `UPI` |
| `bankCode` | `String` Bank code for UPI transactions. Must be set to `"UPI"` (or specific UPI handle code if instructed by PayU). | `UPI` |

**Optional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `upi` | `Object` Object containing customer VPA for UPI Collect transactions. | `{"vpa": "customer@upi"}` |

### order object fields description
<V2_order_object />

### additionalInfo object fields description
**Mandatory parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `txnS2sFlow` | `String` Indicates the S2S flow type. Must be set to `"4"` for UPI seamless flow. | `4` |

**Conditional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `vpa` | `String` Customer's Virtual Payment Address. **Mandatory** for UPI Collect flow. Leave omitted or empty for UPI Intent flow. | `customer@okhdfcbank` |

**Optional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `createOrder` | `Boolean` Set to `true` to create an order identifier in PayU system. | `true` |

### callBackActions object fields description
**Mandatory parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `successAction` | `String` URL where merchant receives notification or redirects customer upon success. | `<redacted URL>` |
| `failureAction` | `String` URL where merchant receives notification or redirects customer upon failure. | `<redacted URL>` |

**Optional parameters**

| Parameter | Description | Example |
| :--- | :--- | :--- |
| `cancelAction` | `String` URL where customer is redirected if transaction is cancelled. | `<redacted URL>` |

### billingDetails object fields description
<BillingDetails_object />

## Sample request

```bash
curl --location '<redacted URL>' \
--header 'date: <CURRENT_DATE_GMT>' \
--header 'authorization: hmac username="<YOUR_TEST_KEY>", algorithm="sha512", headers="date", signature="<YOUR_SIGNATURE>"' \
--header 'Content-Type: application/json' \
--data-raw '{
  "accountId": "<YOUR_TEST_KEY>",
  "txnId": "ZP6267f0d2996ce",
  "amount": 424.38,
  "paymentMethod": {
    "name": "UPI",
    "bankCode": "UPI",
    "upi": {
      "vpa": "customer@okhdfcbank"
    }
  },
  "order": {
    "productInfo": "Example Product",
    "paymentChargeSpecification": {
      "price": 424.38,
      "netAmountDebit": 424.38
    }
  },
  "additionalInfo": {
    "vpa": "customer@okhdfcbank",
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
    "phone": "9876543210",
    "email": "john_doe@example.com"
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
    "amount": 424.38,
    "paymentMethod": {
        "name": "UPI",
        "bankCode": "UPI",
        "upi": {
            "vpa": "customer@okhdfcbank"
        }
    },
    "order": {
        "productInfo": "Example Product",
        "paymentChargeSpecification": {
            "price": 424.38,
            "netAmountDebit": 424.38
        }
    },
    "additionalInfo": {
        "vpa": "customer@okhdfcbank",
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
        "phone": "9876543210",
        "email": "john_doe@example.com"
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
    "amount" => 424.38,
    "paymentMethod" => [
        "name" => "UPI",
        "bankCode" => "UPI",
        "upi" => [
            "vpa" => "customer@okhdfcbank"
        ]
    ],
    "order" => [
        "productInfo" => "Example Product",
        "paymentChargeSpecification" => [
            "price" => 424.38,
            "netAmountDebit" => 424.38
        ]
    ],
    "additionalInfo" => [
        "vpa" => "customer@okhdfcbank",
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
        "phone" => "9876543210",
        "email" => "john_doe@example.com"
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

public class UpiRequest {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        
        String payload = """
        {
            "accountId": "<YOUR_TEST_KEY>",
            "txnId": "ZP6267f0d2996ce",
            "amount": 424.38,
            "paymentMethod": {
                "name": "UPI",
                "bankCode": "UPI",
                "upi": {
                    "vpa": "customer@okhdfcbank"
                }
            },
            "order": {
                "productInfo": "Example Product",
                "paymentChargeSpecification": {
                    "price": 424.38,
                    "netAmountDebit": 424.38
                }
            },
            "additionalInfo": {
                "vpa": "customer@okhdfcbank",
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
                "phone": "9876543210",
                "email": "john_doe@example.com"
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
    amount: 424.38,
    paymentMethod: {
        name: "UPI",
        bankCode: "UPI",
        upi: {
            vpa: "customer@okhdfcbank"
        }
    },
    order: {
        productInfo: "Example Product",
        paymentChargeSpecification: {
            price: 424.38,
            netAmountDebit: 424.38
        }
    },
    additionalInfo: {
        vpa: "customer@okhdfcbank",
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
        phone: "9876543210",
        email: "john_doe@example.com"
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
    "paymentId": "21667772394",
    "authAction": "https://api.payu.in/payments/21667772394/otps",
    "upi": {
      "amount": "424.38",
      "merchantVpa": "<MERCHANT_VPA>", 
      "intentURIData": "upi://pay?pa=<MERCHANT_VPA>&pn=<MERCHANT_NAME>&tr=ZP6267f0d2996ce&am=424.38&cu=INR",
      "merchantName": "<MERCHANT_NAME>"
    }
  },
  "orderId": "b5f2d8785768087678f4"
}
```

## Response Parameters
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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Status of transaction initiation (PENDING until customer approves payment in UPI app).</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PENDING</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.paymentId</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PayU's unique payment identifier.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>21667772394</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.upi.amount</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Transaction amount formatted for UPI.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>424.38</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.upi.merchantVpa</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchant VPA handle where the funds are transferred.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payu.merchant@hdfcbank</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.upi.intentURIData</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Standard UPI intent URI used to launch installed UPI apps on customer devices.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>upi://pay?pa=...</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result.upi.merchantName</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchant legal/display name shown in the customer UPI app.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>PayU Merchant</p></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>orderId</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique order identifier generated by PayU if createOrder was true.</p></td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>b5f2d8785768087678f4</p></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Implementation Steps
### Step 1: Select Flow & Collect VPA
* **UPI Intent (Mobile)**: Do not require customer to enter VPA. Omit `vpa` in the request. PayU returns `intentURIData` which your app passes to mobile OS intents.
* **UPI Collect (Web / Desktop)**: Solicit customer's Virtual Payment Address (e.g., `user@upi`) and pass it in `additionalInfo.vpa` and `paymentMethod.upi.vpa`.

### Step 2: Create Payment Request
Submit the payment request with `txnS2sFlow: "4"` and `bankCode: "UPI"`.

### Step 3: Handle UPI Response
* For **UPI Collect**: Inform customer that a collect request notification has been sent to their UPI app. Prompt them to open their UPI app and enter their MPIN.
* For **UPI Intent**: Launch the UPI intent URL (`intentURIData`) via Android Intent or iOS deep link.

### Step 4: Verify Payment Status
Poll or call the Verify Payment API to confirm transaction outcome:

```bash
curl --location '<redacted URL>' \
--header 'date: <CURRENT_DATE_GMT>' \
--header 'authorization: hmac username="<YOUR_TEST_KEY>", algorithm="sha512", headers="date", signature="<YOUR_SIGNATURE>"' \
--header 'Content-Type: application/json' \
--data-raw '{
  "txnId": [
    "ZP6267f0d2996ce"
  ]
}'
```

## Sample Responses

### Success Response

```json
{
  "status": "SUCCESS",
  "result": {
    "paymentId": "21667772394",
    "orderId": "ZP6267f0d2996ce",
    "amount": 424.38,
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
    "upi": {
      "amount": "424.38",
      "merchantVpa": "payu.merchant@hdfcbank"
    }
  },
  "message": "Awaiting customer approval in UPI app"
}
```

### Failure Response

```json
{
  "status": "FAILED",
  "error": {
    "code": "PAYMENT_DECLINED",
    "message": "Customer rejected collect request or transaction timed out"
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
| `INVALID_VPA` | 400 | Invalid UPI VPA handle | Ensure VPA follows `user@bank` format |
| `AUTHENTICATION_FAILED` | 401 | Invalid signature or key | Verify HMAC credentials and signature header |
| `DUPLICATE_REFERENCE` | 409 | Reference ID already used | Use unique transaction reference ID |
| `PAYMENT_DECLINED` | 422 | Payment declined or expired | Customer declined request or bank timeout |

> For complete error code list, see [Error Codes Reference](ref:error-codes).

## Next Steps

1. **Verify transaction** using [Verify Payment API](ref:v2_verify_payment_api)
2. **Handle webhooks** for asynchronous status updates
3. **Check Dashboard** for reconciliation

> ⚠️ Always verify payment status before order fulfillment.
