---
title: (DEPRECTATED)Settlement Reconciliation API
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
> 🛑 **Deprecated — do not use for new integrations**
>
> The **Settlement Reconciliation API** is deprecated.
>
> **Use instead:**
>
> - **[Settlement Detail Range API:](https://docs.payu.in/reference/settlement-detail-range-api)&#x20;**&#x52;ecommended for date-range reconciliation (transaction + UTR level, paginated).
> - [**Settlement Detail Range API - CB Payments:**](https://docs.payu.in/reference/settlement-detail-range-api-for-cross-border) Recommended for cross-border payments.

This API reconciles the settlements for a given parent mid and specified period (date range).

HTTP Method: **POST**

**Environment**

|                        |                                                                      |
| :--------------------- | :------------------------------------------------------------------- |
| Test Environment       | \<[https://test.payu.in/merchant/>](https://test.payu.in/merchant/>) |
| Production Environment | \<[https://info.payu.in/merchant/>](https://info.payu.in/merchant/>) |

## Request parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchant key<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> The merchant key is included in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Your Test Key</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>command<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> The API command name <strong>get_settlement_details_range</strong> must be included in this parameter.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>get_settlement_details_range</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>hash<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> The hash string encryption is specified in this parameter. The format of the hash is:<br><code>string key\|command\|var1\|salt   </code>Where var1 is the date is the date range.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>string tXjTgO</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var1: datefrom<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> The parameter contains the date on which the range starts or particular date.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2022-08-22</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var2: dateTo<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>varchar</code> The parameter contains the end date until which the statement is required.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2022-08-25</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> var3: aggregator<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>boolean</code> This parameter can contain any of the following values:  </p>
<ul>
<li><strong>true</strong>: It will return the information of the children as well.  </li>
<li><strong>false</strong>: It will return the information of the parent only.</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>true</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>var4: page<br><strong>optional</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> <code>integer</code>This parameter can include the page number that is used if the API returns several pages as a result </p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample request

```curl
curl -X POST "https://info.payu.in/merchant/postservice?form=2"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&command=get_settlement_details_range&var1=2022-07-23&hash=259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8var2=2021-08-12"
```

## Response parameters

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>rows</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The number of rows returned.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>message</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The summary of the response that includes the number of settlements and date of them.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2 Settlements found for the 2022-07-23T00:00 and 2022-07-26T23:59:59.999999999</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This response can contain any of the following:  </p>
<ul>
<li><strong>1</strong> if API call is a success  </li>
<li><strong>0</strong> in case of failure you&#39;ll get system handled failure reasons in this case</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>result</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the settlements in a JSON format. For detailed information, refer to <a href="#resul-json-fields-description">result JSON Fields Description</a>.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> Refer to <a href="#sample_response">Sample Response</a></p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>guid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> This parameter contains the geographically unique ID of the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>sessionId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> This parameter contains the session ID of the transaction</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>errorCode</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the error code if the transaction had failed. The error can be any of the following: | Please pass valid merchant key</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

<br />

### result JSON fields description

The **result** parameter contains the following fields in a JSON format:

| **Field**               | **Description**                                                                                                                                                           | **Example**                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| settlementId            | This field contains the settlement ID                                                                                                                                     | 8599910202207241245                          |
| settlementCompletedDate | This field contains the settlement completion date and time.                                                                                                              | 2022-07-23 17:35:06                          |
| settlementAmount        | This field contains the settlement amount to the child merchant.                                                                                                          | 122185.00                                    |
| merchantId              | This field contains the child merchant ID.                                                                                                                                | 8599910                                      |
| utrNumber               | This field contains the merchant Unique Transaction Reference (UTR) number.                                                                                               | ijklmn                                       |
| transaction             | This field contains the transaction details in a JSON format. For more information, refer to [transaction JSON Fields Description](#transaction_json-fields-description). | Refer to [Sample Response](#sample_response) |
| utrnumber               | This field contains the unique transaction number of the transaction.                                                                                                     | 123456                                       |

### transaction JSON fields description

The **transaction** field contains the following fields in a JSON format:

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
  <td style="border: 1px solid #ddd; padding: 8px;"><p>action</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the purpose of the transaction. This field can contain any of the following values:  </p>
<ul>
<li>Capture  </li>
<li>Adjustment_credit  </li>
<li>Adjustment_debit  </li>
<li>Refund  </li>
<li>Failed</li>
</ul>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Adjustment_credit</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payuId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the PayU ID of the child merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ADJ122538</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionAmount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the transaction amount that needs to be settled.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>6942.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantServiceFee</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the merchant service fee.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>8.0000</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantServiceTax</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains merchant service tax.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>8.0000</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantNetAmount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the net amount settled to the merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cgst</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the CGST amount part of the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>igst</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the IGST amount pat of the transation</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionsgst</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the SGST part of the transaction</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantTransactionId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the merchant transaction ID</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>ADJ122538</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><h3>For Adjustment Status Transactions</h3></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>adjustmentType</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the adjustment type</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>credit</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>referenceId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the reference ID.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>blockType</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the block type.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>adjustmentAction</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>TDR Adjustment</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><h3>For Adjustment Credit Status Transactions</h3></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>mode</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the payment mode for the tranaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>credit</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>cardType</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the card type used for the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentStatus</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the payment status to the child merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>inProgress</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>transactionDate</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the transaction date and time.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2022-07-23 01:45:43</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>requestedAmount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the amount requested by the child merchant.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>6942.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>requestDate</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the date when the child merchant requested the amount.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2022-07-23 01:45:43</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>bankName</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the bank involved in card, Net Banking or UPI transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>token</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the card token if the card is tokenised.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p> </p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><h3>For Refund Status Transactions</h3></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the payment ID of the transaction.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>58871981</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>refundStatus</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the refund status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>refundinprogress</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentAddedOn</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the date when the payment was added on.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>2017-12-08</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentAmount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the payment amount.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>200.00</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>saleAmount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This field contains the original sale amount.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>200.00</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Sample response

```plaintext
{
  "rows": 2,
  "message": "2 Settlements found for the 2022-07-23T00:00 and 2022-07-26T23:59:59.999999999",
  "status": 1,
  "result": [
    {
      "settlementId": "8599910202207241245",
      "settlementCompletedDate": "2022-07-23 17:35:06",
      "settlementAmount": "122185.00",
      "merchantId": 8599910,
      "utrNumber": "ijklmn",
      "transaction": [
        {
          "action": "Adjustment_credit",
          "payuId": "ADJ122538",
          "transactionAmount": "6942.00",
          "merchantNetAmount": "",
          "cgst": "",
          "igst": "",
          "sgst": "",
          "merchantTransactionId": "ADJ122538",
          "mode": "credit",
          "cardType": "",
          "paymentStatus": "inProgress",
          "transactionDate": "2022-07-23 01:45:43",
          "requestedAmount": "6942.00",
          "requestDate": "2022-07-23 01:45:43",
          "bankName": "",
          "token": ""
        }
      ]
    },
    {
      "settlementId": "8597923202207251245",
      "settlementCompletedDate": "2022-07-23 17:40:06",
      "settlementAmount": "18.88",
      "merchantId": 8593059,
      "utrNumber": "abcdef",
      "transaction": [
        {
          "action": "capture",
          "payuId": "15553396797",
          "parentPayuId": "15553211345",
          "requestId": "10801247706",
          "transactionAmount": "4.72",
          "merchantServiceFee": "8.0000",
          "merchantServiceTax": "8.0000",
          "merchantNetAmount": "4.7200",
          "cgst": "0.00000",
          "igst": "1.44000",
          "sgst": "0.00000",
          "merchantTransactionId": "216245453",
          "paymentStatus": "captured",
          "transactionDate": "2022-07-23 10:15:43",
          "requestedAmount": "14.16",
          "requestDate": "2022-07-23 10:15:38",
          "bankName": "IDBB"
        },
        {
          "action": "capture",
          "payuId": "15553398000",
          "parentPayuId": "15553287497",
          "requestId": "10801248633",
          "transactionAmount": "4.72",
          "merchantServiceFee": "8.0000",
          "merchantServiceTax": "8.0000",
          "merchantNetAmount": "4.7200",
          "cgst": "0.00000",
          "igst": "1.44000",
          "sgst": "0.00000",
          "merchantTransactionId": "216249103",
          "paymentStatus": "captured",
          "transactionDate": "2022-07-23 10:15:53",
          "requestedAmount": "14.16",
          "requestDate": "2022-07-23 10:15:48",
          "bankName": "BOIB"
        }
      ]
    }
  ]
}

```

<br />