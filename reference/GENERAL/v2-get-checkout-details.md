---
title: Get Checkout Details API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Get Checkout Details** API enables merchants to retrieve configuration and health metadata required to construct dynamic, custom checkout experiences. This endpoint returns active payment methods, credit/debit card downtime indicators, net banking availability, and eligible EMI tenures.

HTTP Method: **POST**

**Environment**

| Environment                | URL                                           |
| :------------------------- | :-------------------------------------------- |
| **Test Environment**       | `https://apitest.payu.in/v3/checkout/details` |
| **Production Environment** | `https://api.payu.in/v3/checkout/details`     |

## Request Headers

<V2_payment_header_params />

| Header          | Type   | Description                                                   |
| :-------------- | :----- | :------------------------------------------------------------ |
| `Content-Type`  | String | Must be `application/json`.                                   |
| `Date`          | String | Current GMT timestamp (e.g. `Tue, 17 Jun 2025 06:48:55 GMT`). |
| `Authorization` | String | Standard PayU HMAC authorization header.                      |

***

## Request Body Parameters

The table has 6 rows, so per the formatting rules, here it is in **HTML format**:

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
      <td><code>requestId</code></td>
      <td><code>String</code> A unique merchant request identifier for this checkout query.</td>
      <td><code>REQ_CHK_12345678</code></td>
    </tr>
    <tr>
      <td><code>transactionDetails.amount</code></td>
      <td><code>Number</code> Transaction order amount to evaluate minimum and maximum limits per payment option.</td>
      <td><code>12345.00</code></td>
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
      <td><code>useCase.getExtendedPaymentDetails</code></td>
      <td><code>Boolean</code> Set to <code>true</code> to retrieve extended bank downtime status and health messages. Default is <code>true</code>.</td>
      <td><code>true</code></td>
    </tr>
    <tr>
      <td><code>useCase.checkCustomerEligibility</code></td>
      <td><code>Boolean</code> Set to <code>true</code> to check customer-specific credit/debit eligibility (e.g. Cardless EMI / BNPL).</td>
      <td><code>true</code></td>
    </tr>
    <tr>
      <td><code>customerDetails.mobile</code></td>
      <td><code>String</code> Customer mobile number used for eligibility checks.</td>
      <td><code>9876543210</code></td>
    </tr>
    <tr>
      <td><code>filters.paymentOptions</code></td>
      <td><code>Object</code> Restrict query to specific payment instruments or EMI bank codes.</td>
      <td><code>{"emi": {"dc": "SBIN,KKBK,ICIC"}}</code></td>
    </tr>
  </tbody>
</table>

***

## Sample Request

```bash
curl --location 'https://api.payu.in/v3/checkout/details' \
--header 'Content-Type: application/json' \
--header 'Date: Tue, 17 Jun 2025 06:48:55 GMT' \
--header 'Authorization: hmac username="<YOUR_MERCHANT_KEY>", algorithm="sha512", headers="date", signature="<YOUR_SIGNATURE>"' \
--data '{
  "requestId": "REQ_CHK_12345678",
  "transactionDetails": {
    "amount": 12345.00
  },
  "useCase": {
    "getExtendedPaymentDetails": true,
    "checkCustomerEligibility": true
  },
  "customerDetails": {
    "mobile": "9876543210"
  },
  "filters": {
    "paymentOptions": {
      "emi": {
        "dc": "SBIN,KKBK,ICIC"
      }
    }
  }
}'
```
```python
import requests
import json

url = "https://api.payu.in/v3/checkout/details"

headers = {
    "Content-Type": "application/json",
    "Date": "Tue, 17 Jun 2025 06:48:55 GMT",
    "Authorization": "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
}

payload = {
    "requestId": "REQ_CHK_12345678",
    "transactionDetails": {
        "amount": 12345.00
    },
    "useCase": {
        "getExtendedPaymentDetails": True,
        "checkCustomerEligibility": True
    },
    "customerDetails": {
        "mobile": "9876543210"
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```
```php
<?php
$url = "https://api.payu.in/v3/checkout/details";

$payload = json_encode([
    "requestId" => "REQ_CHK_12345678",
    "transactionDetails" => [
        "amount" => 12345.00
    ],
    "useCase" => [
        "getExtendedPaymentDetails" => true,
        "checkCustomerEligibility" => true
    ],
    "customerDetails" => [
        "mobile" => "9876543210"
    ]
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "Content-Type: application/json",
    "Date: Tue, 17 Jun 2025 06:48:55 GMT",
    "Authorization: hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
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

public class PayURequest {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();
        
        String payload = "{\"requestId\": \"REQ_CHK_12345678\", \"transactionDetails\": {\"amount\": 12345.00}, \"useCase\": {\"getExtendedPaymentDetails\": true}}";
        
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://api.payu.in/v3/checkout/details"))
            .header("Content-Type", "application/json")
            .header("Date", "Tue, 17 Jun 2025 06:48:55 GMT")
            .header("Authorization", "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\"")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();
        
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```
```javascript
const url = "https://api.payu.in/v3/checkout/details";

const payload = {
  requestId: "REQ_CHK_12345678",
  transactionDetails: {
    amount: 12345.00
  },
  useCase: {
    getExtendedPaymentDetails: true,
    checkCustomerEligibility: true
  },
  customerDetails: {
    mobile: "9876543210"
  }
};

const options = {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    "Date": "Tue, 17 Jun 2025 06:48:55 GMT",
    "Authorization": "hmac username=\"<YOUR_MERCHANT_KEY>\", algorithm=\"sha512\", headers=\"date\", signature=\"<YOUR_SIGNATURE>\""
  },
  body: JSON.stringify(payload)
};

fetch(url, options)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
```

***

## Response Parameters

| Parameter                          | Type   | Description                                                                     | Example                             |
| :--------------------------------- | :----- | :------------------------------------------------------------------------------ | :---------------------------------- |
| `status`                           | Number | Status code of the response: `1` for success, `0` for failure.                  | `1`                                 |
| `message`                          | String | Status description message.                                                     | `Success`                           |
| `result.requestId`                 | String | Merchant request identifier passed in the request.                              | `REQ_CHK_12345678`                  |
| `result.paymentOptions.cards`      | Object | Enabled card instruments (Credit & Debit) with bank downtime indicators.        | See schema below.                   |
| `result.paymentOptions.netBanking` | Object | Enabled Net Banking options with live status flags (`isDown`).                  | See schema below.                   |
| `result.paymentOptions.emi`        | Object | Supported Credit Card and Debit Card EMI tenures and minimum amount thresholds. | See schema below.                   |
| `result.paymentOptions.upi`        | Object | UPI payment mode status.                                                        | `{"status": true, "isDown": false}` |
| `result.paymentOptions.wallet`     | Object | Enabled digital wallet instruments (Payzapp, Mobikwik, etc.).                   | See schema below.                   |

***

## Sample Response

```json
{
  "status": 1,
  "message": "Success",
  "result": {
    "requestId": "REQ_CHK_12345678",
    "paymentOptions": {
      "cards": {
        "status": true,
        "credit": {
          "status": true,
          "details": [
            {
              "bankCode": "HDFC",
              "bankName": "HDFC Bank",
              "isDown": false,
              "downSince": "",
              "expectedUpTime": "",
              "downMessage": ""
            }
          ]
        },
        "debit": {
          "status": true,
          "details": [
            {
              "bankCode": "SBIN",
              "bankName": "State Bank of India",
              "isDown": false,
              "downSince": "",
              "expectedUpTime": "",
              "downMessage": ""
            }
          ]
        }
      },
      "netBanking": {
        "status": true,
        "details": [
          {
            "bankCode": "HDFC",
            "bankName": "HDFC Bank",
            "isDown": false,
            "downSince": "",
            "expectedUpTime": "",
            "downMessage": ""
          }
        ]
      },
      "emi": {
        "status": true,
        "credit": {
          "status": true,
          "details": [
            {
              "bankCode": "ICIC",
              "bankName": "ICICI Bank",
              "isDown": false,
              "tenures": [3, 6, 9, 12],
              "minAmount": 3000.00
            }
          ]
        },
        "debit": {
          "status": true,
          "details": [
            {
              "bankCode": "SBIN",
              "bankName": "State Bank of India",
              "isDown": false,
              "tenures": [3, 6, 9],
              "minAmount": 5000.00
            }
          ]
        }
      },
      "upi": {
        "status": true,
        "isDown": false
      },
      "wallet": {
        "status": true,
        "details": [
          {
            "walletCode": "PAYZ",
            "walletName": "Payzapp",
            "isDown": false
          }
        ]
      }
    }
  }
}
```

## Next Steps

1. **Render Dynamic Checkout Options**:
   - Dynamically display only active payment options returned in `paymentOptions` and suppress or flag banks marked with `isDown: true`.
2. **Display Applicable Offers & Affordability**:
   - Render eligible bank discounts, cashback offers, and supported EMI tenure options returned in the response.
3. **Proceed to Payment Collection**:
   - When the customer selects their preferred instrument, pass the relevant method details to the Payment. For more information, refer to any of the following:
     - &#x20;[Collect Payment API - PayU Hosted v2 Payment](ref:collect-payment-api-payu-hosted-v2-_payment)
     - [Collect Payment API - Merchant Hosted & S2S v2 Payment](ref:v2_payment_seamless_integration)
