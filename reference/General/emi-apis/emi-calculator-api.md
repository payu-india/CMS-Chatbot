---
title: EMI Calculator API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: EMI Calculator API version 2.0
  description: >-
    This document provides information on an API that can be used to display EMI
    plans and offers on checkout pages or product pages, allowing merchants to
    fetch EMI amounts, rates of interest, and total amounts to be paid across
    eligible banks.
  keywords:
    - EMI calculator API version 2.0
    - Calculate EMI API 2.0
    - ' EMI interest rate calculation API'
    - ' Loan EMI calculator API'
    - Get EMI According to Interest API version 2.0
  robots: index
next:
  description: ''
---
You can use this API to display the EMI plans along with all offers on the checkout page. This API may also be used to display the EMI plans on Product Page or any other screen the merchant may deem fit. You can use it for the following:

- Fetch EMI plans: You can use this API to fetch EMI Amounts, rate of interest, total amount to be paid across eligible banks.
- Fetch EMI plans for a particular bank
- Fetch EMI plan for a particular bank & tenure
- Fetch EMI plans with best offers applicable
- Fetch EMI plans with one offer applied
- Fetch EMI plans with SKU based offers

## Environment

<Table>
  <thead>
    <tr>
      <th>Environment</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>**Test Environment**</td>
      <td>https://apitest.payu.in/calculateEmi/v2</td>
    </tr>
    <tr>
      <td>**Production Environment**</td>
      <td>https://api.payu.in/calculateEmi/v2</td>
    </tr>
  </tbody>
</Table>

## Header parameters

<Table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>accept</td>
      <td>application/json</td>
    </tr>
    <tr>
      <td>content-type</td>
      <td>application/json</td>
    </tr>
    <tr>
      <td>x-credential-username</td>
      <td>OADt8R</td>
    </tr>
  </tbody>
</Table>

## Request parameters

<Table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>amount<br/><code>mandatory</code></td>
      <td>This parameter must include the principal amount that needs to be converted into EMI.</td>
    </tr>
    <tr>
      <td>additional_charges<br/><code>optional</code></td>
      <td>This parameter must include the convenience fee if the merchant wants to collect.</td>
    </tr>
    <tr>
      <td>offer_key<br/><code>optional</code></td>
      <td>This parameter must contain the offer key for the transaction-level offer.</td>
    </tr>
    <tr>
      <td>autoApplyOffer<br/><code>optional</code></td>
      <td>This parameter must be set to **true** if the merchant wants to apply best offer when no transaction offer keys specified.</td>
    </tr>
    <tr>
      <td>skus<br/><code>optional</code></td>
      <td>This parameter must include the SKU data.</td>
    </tr>
    <tr>
      <td>skus.skuAmount<br/><code>mandatory</code></td>
      <td>This parameter must contain the amount per SKU.</td>
    </tr>
    <tr>
      <td>skus.quantity<br/><code>mandatory</code></td>
      <td>This parameter must contain the SKU quantity.</td>
    </tr>
    <tr>
      <td>skus.skuName<br/><code>mandatory</code></td>
      <td>This parameter must contain the name of SKU.</td>
    </tr>
    <tr>
      <td>skus.offerKeys<br/><code>optional</code></td>
      <td>This parameter must contain the offer key for SKU.</td>
    </tr>
    <tr>
      <td>skus.autoApplyOffer</td>
      <td>This parameter must be set to **true** if the merchant wants to apply best offer when no SKU offer keys specified.</td>
    </tr>
    <tr>
      <td>bankCodes<br/><code>optional</code></td>
      <td>This parameter must contain the bank codes for filtering.</td>
    </tr>
    <tr>
      <td>emiCodes<br/><code>optional</code></td>
      <td>This parameter must contain the EMI bankcodes for filtering.</td>
    </tr>
    <tr>
      <td>disableOverrideNceConfig<br/><code>optional</code></td>
      <td>This parameter must be set to **true** PayU will not consider NCE through merchant parameters for the merchant.</td>
    </tr>
  </tbody>
</Table>

## Sample request

```bash
curl --location --request POST 'https://apitest.payu.in/calculateEmi/v2' \
--header 'x-credential-username: smsplus' \
--header 'Content-Type: application/json' \
--data-raw '{
    "txnAmount": 10000,
    "additionalCharges": 0,
    "offerKeys": null,
    "autoApplyOffer": true,
    "bankCodes":null,
    "emiCodes":null,
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

## Response parameters

<Table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>message</td>
      <td>Response message indicating success or failure of the API call.</td>
      <td>Success</td>
    </tr>
    <tr>
      <td>status</td>
      <td>Status code indicating the result of the API call (1 for success, 0 for failure).</td>
      <td>1</td>
    </tr>
    <tr>
      <td>result</td>
      <td>The result is in JSON format with an array of EMI options. For example, EMI6, EMI12, EMI18, etc. For more information, refer to <a href="#emi-json-fields-description">EMI JSON fields description</a>.</td>
      <td>10000.0</td>
    </tr>
    <tr>
      <td>nceDiscount.total</td>
      <td>In NCE (No-Cost EMI), total non-cash equivalent discount amount.</td>
      <td>1266.78</td>
    </tr>
    <tr>
      <td>nceDiscount.instant</td>
      <td>In NCE (No-Cost EMI), instant non-cash equivalent discount applied.</td>
      <td>1266.78</td>
    </tr>
    <tr>
      <td>nceDiscount.cashback</td>
      <td>In NCE (No-Cost EMI), cashback from non-cash equivalent discount.</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>sku</td>
      <td>SKU details in a JSON format. For more information, refer to <a href="#sku-json-fields-description">sku JSON fields description</a>.</td>
      <td>Product1</td>
    </tr>
    <tr>
      <td>totalPayableAmount</td>
      <td>Total amount payable after discounts and EMI.</td>
      <td>10000.0</td>
    </tr>
    <tr>
      <td>nceDiscountAmount</td>
      <td>Total non-cash equivalent discount amount applied.</td>
      <td>1266.78</td>
    </tr>
    <tr>
      <td>revisedPrincipal</td>
      <td>Revised principal loan amount.</td>
      <td>10000.0</td>
    </tr>
    <tr>
      <td>subventionAmount</td>
      <td>Subvention amount considered for the transaction.</td>
      <td>10000.0</td>
    </tr>
    <tr>
      <td>gstSubvention</td>
      <td>Indicates if GST is included in subvention.</td>
      <td>true</td>
    </tr>
    <tr>
      <td>nceViaConfig</td>
      <td>Indicates if NCE discount is via configuration.</td>
      <td>true</td>
    </tr>
    <tr>
      <td>bankCode</td>
      <td>Bank code of the bank providing EMI. For more information, refer to <a href="doc:emi-codes">EMI Codes</a>.</td>
      <td>YESB</td>
    </tr>
    <tr>
      <td>emi_value</td>
      <td>EMI value calculated.</td>
      <td>555.55</td>
    </tr>
    <tr>
      <td>emi_interest_paid</td>
      <td>Total interest paid over the EMI tenure.</td>
      <td>1266.78</td>
    </tr>
  </tbody>
</Table>

### EMI JSON fields description

<Table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>transactionAmount</td>
      <td>The total transaction amount for which the EMI is calculated.</td>
      <td>10000.0</td>
    </tr>
    <tr>
      <td>payBackAmount</td>
      <td>The amount to be paid back over the EMI tenure, including interest.</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>emiAmount</td>
      <td>The EMI amount to be paid in each installment.</td>
      <td>555.56</td>
    </tr>
    <tr>
      <td>additionalCost</td>
      <td>Any additional costs apart from the EMI amount.</td>
      <td>"0.0"</td>
    </tr>
    <tr>
      <td>emiMdrNote</td>
      <td>Merchant discount rate note related to EMI.</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>emiBankInterest</td>
      <td>Interest rate charged by the bank for the EMI.</td>
      <td>15.0</td>
    </tr>
    <tr>
      <td>bankRate</td>
      <td>Bank's rate for the EMI calculation.</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>bankCharge</td>
      <td>Additional bank charges associated with the EMI.</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>amount</td>
      <td>Amount per EMI installment including any charges.</td>
      <td>555.56</td>
    </tr>
    <tr>
      <td>cardType</td>
      <td>Type of card used for the transaction.</td>
      <td>credit card</td>
    </tr>
    <tr>
      <td>tenure</td>
      <td>Duration of the EMI plan.</td>
      <td>18 months</td>
    </tr>
    <tr>
      <td>loanAmount</td>
      <td>Principal loan amount for EMI.</td>
      <td>10000.0</td>
    </tr>
    <tr>
      <td>offerKeys</td>
      <td>Keys associated with any offers applied.</td>
      <td>null</td>
    </tr>
    <tr>
      <td>offerDiscount.total</td>
      <td>Total discount amount provided as part of the offer.</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>offerDiscount.instant</td>
      <td>Instant discount amount applied.</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>offerDiscount.cashback</td>
      <td>Cashback amount provided as part of the offer.</td>
      <td>0.0</td>
    </tr>
  </tbody>
</Table>

### sku JSON fields description

<Table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>skuId</td>
      <td>SKU identifier for the product.</td>
      <td>Product1</td>
    </tr>
    <tr>
      <td>amountPerSku</td>
      <td>Amount per SKU for the product.</td>
      <td>8000.0</td>
    </tr>
    <tr>
      <td>amount</td>
      <td>Total amount for the SKUs provided.</td>
      <td>8000.0</td>
    </tr>
    <tr>
      <td>quantity</td>
      <td>Quantity of the SKU.</td>
      <td>1</td>
    </tr>
    <tr>
      <td>offerKeys</td>
      <td>Keys associated with any offers on SKU.</td>
      <td>null</td>
    </tr>
    <tr>
      <td>emiAmount</td>
      <td>EMI amount specific to SKU.</td>
      <td>444.44</td>
    </tr>
    <tr>
      <td>emiBankInterest</td>
      <td>EMI bank interest for SKU.</td>
      <td>15.0</td>
    </tr>
    <tr>
      <td>emiValue</td>
      <td>EMI value calculated for SKU.</td>
      <td>444.44</td>
    </tr>
    <tr>
      <td>emiInterestPaid</td>
      <td>Interest paid for EMI on SKU.</td>
      <td>1013.42</td>
    </tr>
    <tr>
      <td>offerDiscount.total</td>
      <td>Total offer discount on SKU.</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>offerDiscount.instant</td>
      <td>Instant offer discount on SKU.</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>offerDiscount.cashback</td>
      <td>Cashback offer on SKU.</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>nceDiscount.total</td>
      <td>Total non-cash equivalent discount on SKU.</td>
      <td>1013.42</td>
    </tr>
    <tr>
      <td>nceDiscount.instant</td>
      <td>Instant non-cash equivalent discount on SKU.</td>
      <td>1013.42</td>
    </tr>
    <tr>
      <td>nceDiscount.cashback</td>
      <td>Cashback from non-cash equivalent discount on SKU.</td>
      <td>0.0</td>
    </tr>
    <tr>
      <td>totalPayableAmount</td>
      <td>Total amount payable for the SKU.</td>
      <td>7999.92</td>
    </tr>
    <tr>
      <td>nceDiscountAmount</td>
      <td>NCE discount amount applied on SKU.</td>
      <td>1013.42</td>
    </tr>
    <tr>
      <td>subventionAmount</td>
      <td>Subvention amount for SKU.</td>
      <td>8000.0</td>
    </tr>
    <tr>
      <td>revisedPrincipal</td>
      <td>Revised principal amount for SKU.</td>
      <td>8000.0</td>
    </tr>
    <tr>
      <td>additionalCharge</td>
      <td>Additional charge applicable to SKU.</td>
      <td>0.0</td>
    </tr>
  </tbody>
</Table>

## Sample response

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