---
title: EMI Calculator API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: EMI Calculator API
deprecated: false
hidden: false
metadata:
  robots: index
---

You can use this API to display the EMI plans along with all offers on the checkout page. This API may also be used to display EMI plans on product pages or any other screen deemed fit.

You can use it for the following:
* **Fetch EMI plans**: Retrieve EMI amounts, interest rates, and total payable amounts across eligible banks.
* **Filter by bank**: Retrieve EMI plans for a specific bank code.
* **Filter by tenure**: Retrieve EMI plans for a specific bank and tenure.
* **Offers integration**: Fetch EMI plans with the best applicable offer, a specific transaction offer, or SKU-based offers.

---

## Environment

| Environment | URL |
| :--- | :--- |
| **Test Environment** | `https://apitest.payu.in/calculateEmi/v2` |
| **Production Environment** | `https://api.payu.in/calculateEmi/v2` |

---

## Request Headers

| Header | Type | Required | Description | Example |
| :--- | :--- | :--- | :--- | :--- |
| `Accept` | String | Mandatory | Expected response format. | `application/json` |
| `Content-Type` | String | Mandatory | Media type of the request body. | `application/json` |
| `x-credential-username` | String | Mandatory | Your PayU merchant key. | `<YOUR_MERCHANT_KEY>` |

---

## Request Parameters

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :--- | :--- | :--- |
| `txnAmount` | Number | Mandatory | Principal transaction amount that needs to be converted into EMI. | `10000` |
| `additionalCharges` | Number | Optional | Convenience fee or additional charges to collect with the transaction. Defaults to `0`. | `0` |
| `offerKeys` | Array of Strings | Optional | List of offer keys for transaction-level discount/cashback offers. Pass `null` if none. | `["OFFER123"]` |
| `autoApplyOffer` | Boolean | Optional | Set to `true` to automatically apply the best available transaction offer when no `offerKeys` are specified. | `true` |
| `bankCodes` | Array of Strings | Optional | List of bank codes to filter plans (e.g. `["HDFC", "ICICI"]`). Pass `null` to return all eligible banks. | `["HDFCB", "ICICI"]` |
| `emiCodes` | Array of Strings | Optional | List of specific EMI plan codes to filter (e.g. `["EMIH3", "EMIH6"]`). Pass `null` for all tenures. | `["EMIH6"]` |
| `disableOverrideNceConfig` | Boolean | Optional | When set to `true`, PayU will not consider No-Cost EMI (NCE) overrides passed via merchant parameters. | `true` |
| `skus` | Array of Objects | Optional | Product SKU details for SKU-level discount/offer calculations. | Array |
| `skus[].skuId` | String | Mandatory (if `skus` passed) | Unique SKU identifier. | `"Product1"` |
| `skus[].skuAmount` | Number | Mandatory (if `skus` passed) | Unit price of the SKU. | `8000` |
| `skus[].quantity` | Integer | Mandatory (if `skus` passed) | Quantity of this SKU item. | `1` |
| `skus[].offerKeys` | Array of Strings | Optional | List of SKU-specific offer keys. | `null` |
| `skus[].autoApplyOffer` | Boolean | Optional | Set to `true` to auto-apply the best offer on this SKU when no SKU offer key is passed. | `false` |

---

## Sample Request

### cURL

```bash
curl --location --request POST 'https://apitest.payu.in/calculateEmi/v2' \
--header 'x-credential-username: <YOUR_MERCHANT_KEY>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "txnAmount": 10000,
  "additionalCharges": 0,
  "offerKeys": null,
  "autoApplyOffer": true,
  "bankCodes": null,
  "emiCodes": null,
  "disableOverrideNceConfig": true,
  "skus": [
    {
      "skuId": "Product1",
      "skuAmount": 8000,
      "quantity": 1,
      "offerKeys": null,
      "autoApplyOffer": false
    },
    {
      "skuId": "Product2",
      "skuAmount": 1000,
      "quantity": 2,
      "offerKeys": null,
      "autoApplyOffer": false
    }
  ]
}'
```

### Python

```python
import requests
import json

url = "https://apitest.payu.in/calculateEmi/v2"

headers = {
    "x-credential-username": "<YOUR_MERCHANT_KEY>",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "txnAmount": 10000,
    "additionalCharges": 0,
    "offerKeys": None,
    "autoApplyOffer": True,
    "bankCodes": None,
    "emiCodes": None,
    "disableOverrideNceConfig": True,
    "skus": [
        {
            "skuId": "Product1",
            "skuAmount": 8000,
            "quantity": 1,
            "offerKeys": None,
            "autoApplyOffer": False
        },
        {
            "skuId": "Product2",
            "skuAmount": 1000,
            "quantity": 2,
            "offerKeys": None,
            "autoApplyOffer": False
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### PHP

```php
<?php
$url = "https://apitest.payu.in/calculateEmi/v2";

$payload = json_encode([
    "txnAmount" => 10000,
    "additionalCharges" => 0,
    "offerKeys" => null,
    "autoApplyOffer" => true,
    "bankCodes" => null,
    "emiCodes" => null,
    "disableOverrideNceConfig" => true,
    "skus" => [
        [
            "skuId" => "Product1",
            "skuAmount" => 8000,
            "quantity" => 1,
            "offerKeys" => null,
            "autoApplyOffer" => false
        ],
        [
            "skuId" => "Product2",
            "skuAmount" => 1000,
            "quantity" => 2,
            "offerKeys" => null,
            "autoApplyOffer" => false
        ]
    ]
]);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    "x-credential-username: <YOUR_MERCHANT_KEY>",
    "Content-Type: application/json",
    "Accept: application/json"
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```

### Java

```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class CalculateEmi {
    public static void main(String[] args) throws Exception {
        HttpClient client = HttpClient.newHttpClient();

        String payload = """
        {
          "txnAmount": 10000,
          "additionalCharges": 0,
          "offerKeys": null,
          "autoApplyOffer": true,
          "bankCodes": null,
          "emiCodes": null,
          "disableOverrideNceConfig": true,
          "skus": [
            {
              "skuId": "Product1",
              "skuAmount": 8000,
              "quantity": 1,
              "offerKeys": null,
              "autoApplyOffer": false
            },
            {
              "skuId": "Product2",
              "skuAmount": 1000,
              "quantity": 2,
              "offerKeys": null,
              "autoApplyOffer": false
            }
          ]
        }
        """;

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://apitest.payu.in/calculateEmi/v2"))
            .header("x-credential-username", "<YOUR_MERCHANT_KEY>")
            .header("Content-Type", "application/json")
            .header("Accept", "application/json")
            .POST(HttpRequest.BodyPublishers.ofString(payload))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }
}
```

### JavaScript (Node.js)

```javascript
const url = "https://apitest.payu.in/calculateEmi/v2";

const payload = {
  txnAmount: 10000,
  additionalCharges: 0,
  offerKeys: null,
  autoApplyOffer: true,
  bankCodes: null,
  emiCodes: null,
  disableOverrideNceConfig: true,
  skus: [
    {
      skuId: "Product1",
      skuAmount: 8000,
      quantity: 1,
      offerKeys: null,
      autoApplyOffer: false
    },
    {
      skuId: "Product2",
      skuAmount: 1000,
      quantity: 2,
      offerKeys: null,
      autoApplyOffer: false
    }
  ]
};

fetch(url, {
  method: "POST",
  headers: {
    "x-credential-username": "<YOUR_MERCHANT_KEY>",
    "Content-Type": "application/json",
    "Accept": "application/json"
  },
  body: JSON.stringify(payload)
})
  .then(res => res.json())
  .then(data => console.log(JSON.stringify(data, null, 2)))
  .catch(err => console.error("Error:", err));
```

---

## Response Parameters

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `status` | Integer | Indicates whether the request succeeded (`1`) or failed (`0`). | `1` |
| `message` | String | Status description message. | `"Success"` |
| `result` | Object | Map of bank codes containing all available EMI plans and tenures. | Object |

### Plan Details (`result.<BANK_CODE>.<PLAN_CODE>`)

| Parameter | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `transactionAmount` | Number | Total transaction amount for which EMI was calculated. | `10000.0` |
| `payBackAmount` | Number | Total amount to be repaid over the EMI tenure, including interest. | `0.0` |
| `emiAmount` | Number | Monthly installment amount to be paid by the customer. | `555.56` |
| `additionalCost` | String | Additional fee or cost associated with the plan. | `"0.0"` |
| `emiMdrNote` | Number | Merchant discount rate note related to EMI. | `0.0` |
| `emiBankInterest` | Number | Annual percentage rate (APR) charged by the issuing bank. | `15.0` |
| `bankRate` | Number | Bank's base rate for EMI calculation. | `0.0` |
| `bankCharge` | Number | Additional bank charge associated with the plan. | `0.0` |
| `amount` | Number | Amount per EMI installment including charges. | `555.56` |
| `cardType` | String | Card category supported for this plan (e.g. `credit card`, `debit card`). | `"credit card"` |
| `tenure` | String | Duration of the EMI repayment schedule. | `"18 months"` |
| `loanAmount` | Number | Principal loan amount financed by the bank. | `10000.0` |
| `totalPayableAmount` | Number | Total amount payable by the customer after discounts. | `10000.0` |
| `subventionAmount` | Number | Subvention amount considered for the transaction. | `10000.0` |
| `gstSubvention` | Boolean | Indicates if GST is included in the subvention calculation. | `true` |
| `nceViaConfig` | Boolean | Indicates if No-Cost EMI discount is applied via configuration. | `true` |
| `bankCode` | String | Bank code of the participating issuer. | `"YESB"` |
| `emi_value` | Number | Calculated monthly EMI value. | `555.55` |
| `emi_interest_paid` | Number | Total interest paid by the customer over the full tenure. | `1266.78` |
| `revisedPrincipal` | Number | Net principal loan amount after applying instant discounts. | `10000.0` |
| `offerDiscount` | Object | Discount details applied through merchant/bank offers. | Object |
| `offerDiscount.total` | Number | Total offer discount applied. | `0.0` |
| `offerDiscount.instant` | Number | Instant discount deducted from transaction amount. | `0.0` |
| `offerDiscount.cashback` | Number | Cashback credited back to the customer. | `0.0` |
| `nceDiscount` | Object | No-Cost EMI discount breakdown. | Object |
| `nceDiscount.total` | Number | Total No-Cost EMI interest discount provided. | `1266.78` |
| `nceDiscount.instant` | Number | Instant discount applied to offset the bank interest charges. | `1266.78` |
| `nceDiscount.cashback` | Number | Cashback credit for NCE subvention. | `0.0` |
| `sku` | Array of Objects | SKU-level calculations and discount distribution. | Array |

---

## Sample Response

```json
{
  "message": "Success",
  "status": 1,
  "result": {
    "YES": {
      "EMIY18": {
        "transactionAmount": 10000.0,
        "payBackAmount": 0.0,
        "emiAmount": 555.56,
        "additionalCost": "0.0",
        "emiMdrNote": 0.0,
        "emiBankInterest": 15.0,
        "bankRate": 0.0,
        "bankCharge": 0.0,
        "amount": 555.56,
        "cardType": "credit card",
        "tenure": "18 months",
        "loanAmount": 10000.0,
        "offerKeys": null,
        "offerDiscount": {
          "total": 0.0,
          "instant": 0.0,
          "cashback": 0.0
        },
        "nceDiscount": {
          "total": 1266.78,
          "instant": 1266.78,
          "cashback": 0.0
        },
        "sku": [
          {
            "skuId": "Product1",
            "amountPerSku": 8000.0,
            "amount": 8000.0,
            "quantity": 1,
            "offerKeys": null,
            "emiAmount": 444.44,
            "emiBankInterest": 15.0,
            "emiValue": 444.44,
            "emiInterestPaid": 1013.42,
            "offerDiscount": {
              "total": 0.0,
              "instant": 0.0,
              "cashback": 0.0
            },
            "nceDiscount": {
              "total": 1013.42,
              "instant": 1013.42,
              "cashback": 0.0
            },
            "totalPayableAmount": 7999.92,
            "nceDiscountAmount": 1013.42,
            "subventionAmount": 8000.0,
            "revisedPrincipal": 8000.0,
            "additionalCharge": 0.0
          },
          {
            "skuId": "Product2",
            "amountPerSku": 1000.0,
            "amount": 2000.0,
            "quantity": 2,
            "offerKeys": null,
            "emiAmount": 111.11,
            "emiBankInterest": 15.0,
            "emiValue": 111.11,
            "emiInterestPaid": 253.36,
            "offerDiscount": {
              "total": 0.0,
              "instant": 0.0,
              "cashback": 0.0
            },
            "nceDiscount": {
              "total": 1266.78,
              "instant": 1266.78,
              "cashback": 0.0
            },
            "totalPayableAmount": 1999.98,
            "nceDiscountAmount": 253.36,
            "subventionAmount": 2000.0,
            "revisedPrincipal": 2000.0,
            "additionalCharge": 0.0
          }
        ],
        "totalPayableAmount": 10000.0,
        "nceDiscountAmount": 1266.78,
        "revisedPrincipal": 10000.0,
        "subventionAmount": 10000.0,
        "gstSubvention": true,
        "nceViaConfig": true,
        "bankCode": "YESB",
        "emi_value": 555.55,
        "emi_interest_paid": 1266.78
      }
    }
  }
}
```

---

## Next Steps

1. **Present EMI Plans on Checkout UI**:
   Display monthly installments (`emiAmount`), tenure options, and annual interest rates (`emiBankInterest`) on your checkout page or product display screen.
2. **Promote No-Cost EMI (NCE)**:
   When `nceDiscount.total` is greater than `0`, highlight No-Cost EMI savings prominently to increase cart conversion.
3. **Verify Card BIN Eligibility**:
   Before initiating payment, optionally verify the cardholder's 6 or 8-digit BIN using the **[Eligible BIN for EMI API](ref:v2-eligible-bin-for-emi-api)**.
4. **Initiate EMI Payment**:
   Pass the selected bank code, tenure code, and card details into the **[Collect Payments with EMI (v2/payment) API](ref:collect-payments-with-emi-v2_payment)** to complete the payment.
