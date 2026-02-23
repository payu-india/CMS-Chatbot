---
title: Get Checkout Details – NTB Seamless Journey
deprecated: false
hidden: true
metadata:
  robots: index
---
This is used in the **NTB Seamless Journey** flow.

<br />

### Body parameters

| Parameter | Description                                                                                                                                                | Example              |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| key       | <code>String</code> Merchant key provided by PayU.                                                                                                         | JPM7Fg               |
| command   | <code>String</code> Must be <code>get_checkout_details</code> (name of the web-service).                                                                   | get_checkout_details |
| var1      | <code>String</code> JSON string containing requestId, transactionDetails, useCase, and optionally customerDetails and filters. See var1 JSON fields below. | See                  |

<br />

### var1 JSON fields (inside var1)

| Parameter          | Description                                                                                                                                                                                                                                                                                                                                                                                       | Example                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| requestId          | <code>String</code> Request ID.                                                                                                                                                                                                                                                                                                                                                                   | 12345678                                       |
| transactionDetails | <code>Object</code> Must contain <code>amount</code> (transaction amount) and optionally <code>txnid</code> (transaction ID).                                                                                                                                                                                                                                                                     | \{"amount": "100.00", "txnid": "TXN123"}       |
| useCase            | <code>Object</code> Flags for which information to return: <code>getExtendedPaymentDetails</code>, <code>getAdditionalCharges</code>, <code>getTaxSpecification</code>, <code>checkDownStatus</code>, <code>checkCustomerEligibility</code>. Optionally <code>filters</code> (e.g. <code>paymentOptions.emi.dc</code>, <code>cc</code>, <code>cardless</code>; <code>paymentOptions.bnpl</code>). | \{"getExtendedPaymentDetails": true}           |
| customerDetails    | <code>Object</code> Optional. Customer info (e.g. <code>mobile</code>) for eligibility checks.                                                                                                                                                                                                                                                                                                    | \{"mobile": "9098765432"}                      |
| filters            | <code>Object</code> Optional. Filter response by <code>paymentOptions</code> (emi.dc, cc, cardless; bnpl). Include "all" for all banks in a category.                                                                                                                                                                                                                                             | \{"paymentOptions": \{"emi": \{"dc": "ICIC"}}} |

### useCase flags (inside useCase)

| Field                     | Description                                                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| getExtendedPaymentDetails | <code>Boolean</code> Set <code>true</code> to check EMI eligibility (mobile/card) and “Buy Now Pay Later” modes; returns title, EMI breakup, etc. |
| getAdditionalCharges      | <code>Boolean</code> Set <code>true</code> to return additional charges for all payment options.                                                  |
| getTaxSpecification       | <code>Boolean</code> Set <code>true</code> to return tax specification from backend for splitting additional charges.                             |
| checkDownStatus           | <code>Boolean</code> Set <code>true</code> to return downtime of payment options.                                                                 |
| checkCustomerEligibility  | <code>Boolean</code> Set <code>true</code> to return customer eligibility.                                                                        |

## Sample request

```cUrl
curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
--form 'key="0d5aDh"' \
--form 'command="get_checkout_details"' \
--form 'var1="{\"requestId\":\"9920371372_38\",\"transactionDetails\":{\"amount\":8000},\"useCase\":{\"getExtendedPaymentDetails\":true}}"' \
--form 'hash="5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a"'
```

## Sample response

```json
{
  "status": 1,
  "details": {
    "paymentOptions": {
      "emi": {
        "all": {
          "dc": {
            "hasEligible": true,
            "all": {
              "UTIB": {
                "title": "Axis Bank",
                "shortName": "Axis",
                "minimumAmount": 1000,
                "maximumAmount": null,
                "eligibility": {"status": true},
                "tenureOptions": {
                  "AXISD03": {
                    "tenure": 3,
                    "interestRate": 10.5,
                    "interestCharged": 200.45,
                    "monthlyEmi": 400.5,
                    "minimumAmount": 1000,
                    "maximumAmount": null,
                    "eligibility": {"status": true}
                  }
                }
              }
            },
            "minimumAmount": 1000,
            "maximumAmount": null
          }
        }
      },
      "nb": { "all": { "SBIB": { "title": "State Bank of India" } } },
      "dc": { "all": { "MAST": { "title": "MasterCard Debit Cards" } } },
      "cc": { "all": { "CC": { "title": "Credit Card" } } },
      "cash": { "all": { "PAYTM": { "title": "Paytm" } } }
    }
  }
}
```
