---
title: Settlement Detail Range API - CB Payments
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
Settlement Details APIs are build on top of settlement data that provides transaction level data for a given date or date range or UTR. These APIs returns paginated response for the given input page and page size.

<Callout icon="📘" theme="info">
  ### Notes:

  - Use this API for settlement date range where number of settled transactions are not more that 10K. In case if we are having more records, try to use other channel like settlement/billing report or Settlement Dashboard reports to fetch the data.
  - API will perform better if request is coming for single or non parent MID.
  - As timeout is 60 Seconds, try to keep page size not more that 500 and date range a single date (Try to avoid giving end date)
</Callout>

#### Environment

|            |                                                                                  |
| :--------- | :------------------------------------------------------------------------------- |
| Production | [https://info.payu.in/settlement/range/](https://info.payu.in/settlement/range/) |

## Request parameters

### Authorization header

<HeaderAuthentication />


### Query parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        dateFrom `mandatory`
      </td>

      <td>
        This parameter must contain from date for the settlement range is required is in YYYY-MM-DD format. 
      </td>

      <td>
        2024-03-26
      </td>
    </tr>

    <tr>
      <td>
        dateTo `optional`
      </td>

      <td>
        This parameter must contain date for the settlement range is required is in YYYY-MM-DD format. 

        - _Note_\*: Date range is cannot be more than 3 days, so**dateTo** value must be posted accordingly.
      </td>

      <td>
        2024-03-28
      </td>
    </tr>

    <tr>
      <td>
        pageSize<br />`optional`
      </td>

      <td>
        This parameter must contain the number of records to be paginated on each page is specified in this parameter. By default, the value is 100.
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        page<br />`optional`
      </td>

      <td>
        This parameter must contain the page to be displayed.
      </td>

      <td>
        1
      </td>
    </tr>
  </tbody>
</Table>

## Sample request/response

### Success scenarios

### Only Start date provided

**Request**

```
curl --location 'https://info.payu.in/settlement/range/?dateFrom=2023-06-20&pageSize=200&page=1' \--header 'Authorization: {{authorization}}' \--header 'Date: {{date}}'
```

**Response**

```
{
    "status": 0,
    "result": {
        "page": 1,
        "size": 2,
        "totalCount": 2,
        "data": [
            {
                "settlementId": "8763692202306200915",
                "settlementCompletedDate": "2023-06-20 11:00:03",
                "settlementAmount": "283079197.97",
                "merchantId": 8763692,
                "utrNumber": "UTIBR72023062000022728",
                "transaction": [
                    {
                        "action": "capture",
                        "payuId": "17577006305",
                        "parentPayuId": "17577001693",
                        "requestId": "12273055103",
                        "transactionAmount": "167334.00",
                        "merchantServiceFee": "0.00000",
                        "merchantServiceTax": "0.00000",
                        "merchantNetAmount": "167334.0",
                        "sgst": "0.00000",
                        "cgst": "0.00000",
                        "igst": "0.00000",
                        "merchantTransactionId": "16871992915354836",
                        "mode": "NB",
                        "paymentStatus": "captured",
                        "transactionDate": "2023-06-19 23:59:38",
                        "requestDate": "2023-06-19 23:59:38",
                        "requestedAmount": "167334.00",
                        "bankName": "SBIB",
                        "offerServiceFee": "0.00",
                        "offerServiceTax": "0.00",
                        "transferCurrency":"INR",
                        "transactionCurrency":"USD",
                        "forexRate":80.45,
                        "finalSettlement": 20000.45
                    },
                    {
                        "action": "capture",
                        "payuId": "17577005415",
                        "parentPayuId": "17577004788",
                        "requestId": "12273054470",
                        "transactionAmount": "17559.00",
                        "merchantServiceFee": "0.00000",
                        "merchantServiceTax": "0.00000",
                        "merchantNetAmount": "17559.0",
                        "sgst": "0.00000",
                        "cgst": "0.00000",
                        "igst": "0.00000",
                        "merchantTransactionId": "16871993385972302",
                        "mode": "UPI",
                        "paymentStatus": "captured",
                        "transactionDate": "2023-06-19 23:59:22",
                        "requestDate": "2023-06-19 23:59:22",
                        "requestedAmount": "17559.00",
                        "bankName": "INTENT",
                        "offerServiceFee": "0.00",
                        "offerServiceTax": "0.00",
                        "transferCurrency":"INR",
                        "transactionCurrency":"USD",
                        "forexRate":80.45,
                        "finalSettlement": 20000.45
                    }               ]
            }
        ]
    }
}
```

#### Start and end date provided

**Request**

```
curl --location 'https://info.payu.in/settlement/range/?dateFrom=2023-06-20&dateTo=2023-06-21&pageSize=200&page=1' \--header 'Authorization: {{authorization}}' \--header 'Date: {{date}}'
```

**Response**

```
{
    "status": 0,
    "result": {
        "page": 1,
        "size": 2,
        "totalCount": 2,
        "data": [
            {
                "settlementId": "8763692202306200915",
                "settlementCompletedDate": "2023-06-20 11:00:03",
                "settlementAmount": "283079197.97",
                "merchantId": 8763692,
                "utrNumber": "UTIBR72023062000022728",
                "transaction": [
                    {
                        "action": "capture",
                        "payuId": "17577006305",
                        "parentPayuId": "17577001693",
                        "requestId": "12273055103",
                        "transactionAmount": "167334.00",
                        "merchantServiceFee": "0.00000",
                        "merchantServiceTax": "0.00000",
                        "merchantNetAmount": "167334.0",
                        "sgst": "0.00000",
                        "cgst": "0.00000",
                        "igst": "0.00000",
                        "merchantTransactionId": "16871992915354836",
                        "mode": "NB",
                        "paymentStatus": "captured",
                        "transactionDate": "2023-06-19 23:59:38",
                        "requestDate": "2023-06-19 23:59:38",
                        "requestedAmount": "167334.00",
                        "bankName": "SBIB",
                        "offerServiceFee": "0.00",
                        "offerServiceTax": "0.00",
                        "transferCurrency":"INR",
                        "transactionCurrency":"USD",
                        "forexRate":80.45,
                        "finalSettlement": 20000.45
                    },
                    {
                        "action": "capture",
                        "payuId": "17577005415",
                        "parentPayuId": "17577004788",
                        "requestId": "12273054470",
                        "transactionAmount": "17559.00",
                        "merchantServiceFee": "0.00000",
                        "merchantServiceTax": "0.00000",
                        "merchantNetAmount": "17559.0",
                        "sgst": "0.00000",
                        "cgst": "0.00000",
                        "igst": "0.00000",
                        "merchantTransactionId": "16871993385972302",
                        "mode": "UPI",
                        "paymentStatus": "captured",
                        "transactionDate": "2023-06-19 23:59:22",
                        "requestDate": "2023-06-19 23:59:22",
                        "requestedAmount": "17559.00",
                        "bankName": "INTENT",
                        "offerServiceFee": "0.00",
                        "offerServiceTax": "0.00",
                        "transferCurrency":"INR",
                        "transactionCurrency":"USD",
                        "forexRate":80.45,
                        "finalSettlement": 20000.45
                    }               ]
            }
        ]
    }
}
```

### Failure scenario responses

#### Invalid response for invalid request: HTTP status 200

```
{
  "message": "Page size can't be more that 50000",
  "status": 1,
  "result": "Page size can't be more that 50000"
}
```

##### Authorization failed: HTTP status 401

```
{
    "message": "Unauthorized"
}
```

## Response parameters

The description of fields in the **data** JSON of the response:

| **Parameter**           | **Fields**                                                                                                                                                                                                   | **Sample Value**                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| settlementId            | This parameter contains a unique settlement ID generated by PayU.                                                                                                                                            | 8763692202306200915                           |
| settlementCompletedDate | This parameter contains settlement completion date.                                                                                                                                                          | 2023-06-20 11:00:03                           |
| settlementAmount        | This parameter contains settlement amount.                                                                                                                                                                   | 10.00                                         |
| merchantId              | This parameter contains a merchant ID that is provided by PayU.                                                                                                                                              | 8763692                                       |
| utrNumber               | This parameter contains an alphanumeric code generated by banks when a transaction is executed. This number serves as a reference code that helps track and identify specific transactions and their status. | UTIBR72023062000022728                        |
| transaction             | This parameter contains the transaction details in a JSON format. For more information, refer to [transaction JSON fields description](#transaction-json-fields-description).                                | Refer to [sample response](#sample-response). |

### transaction JSON fields description

The description of fields in the **transaction** JSON of the response:

| **Field**             | **Description**                                                                                                                                                                                                                            | **Example**         |
| :-------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| action                | This parameter contains the action taken on the transaction. For more information, refer to [List of Unmapped Status](#list-of-unmapped-status)  .                                                                                         | refund              |
| payuid                | This parameter contains a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund. | 403993715521937565  |
| parentPayuId          | This parameter contains a parent PayU ID in case of Split Payment transactions.                                                                                                                                                            |                     |
| requestid             | This parameter contains the request ID value posted by the merchant during the transaction request.                                                                                                                                        | 131278418           |
| transactionAmount     | This parameter contains the original amount which was sent in the transaction request by the merchant.                                                                                                                                     | 100                 |
| merchantServiceFee    | This parameter contains the service fee paid by the merchant to the bank. for the transaction                                                                                                                                              | 239.6000            |
| merchantServiceTax    | This parameter contains the tax on service fee paid by the merchant to the bank. for the transaction                                                                                                                                       | 43.1300             |
| merchantNetAmount     | This parameter contains the net amount to be settled by bank to merchant.                                                                                                                                                                  | 100                 |
| merchantTransactionId | This parameter contains the transaction ID of the transaction.                                                                                                                                                                             | 13818               |
| cgst                  | This parameter contains the CGST (Central GST) for the transaction.                                                                                                                                                                        | 43.13000            |
| igst                  | This parameter contains the IGST (Integrated GST) for the transaction.                                                                                                                                                                     | 43.13000            |
| sgst                  | This parameter contains the SGST (State GST) for the transaction where the supplier or merchant is from a different state of the customer.                                                                                                 | 43.13000            |
| mode                  | This parameter contains the mode of the transaction such as credit card, debit card, etc. For more information, refer to [Payment Mode Codes](doc:payment-mode-codes).                                                                     | CC                  |
| payementStatus        | This parameter contains the payment state of the transaction. For more information, refer to [Payment State Explanations](ref:payment-state-explanations).                                                                                 | captured            |
| transactionDate       | This parameter contains the date of the transaction.                                                                                                                                                                                       | 2021-08-10 23:46:25 |
| requestDate           | This parameter contains the request date and time stamp.                                                                                                                                                                                   | 2021-08-10 23:49:16 |
| requestedAmount       | The parameter contains the amount requested by the merchant to the bank.                                                                                                                                                                   | 100                 |
| bankName              | This parameter contains the bank name or the card type based on the transaction.                                                                                                                                                           | MAST                |
| offerServiceFee       | This parameter contains the service fee incurred for offer if the transaction involved offer.                                                                                                                                              | 2                   |
| offerServiceTax       | This parameter contains service tax incurred for offer if the transaction involved offer.                                                                                                                                                  | 0.36                |
| transferCurrency      | This parameter contain the currency to which conversion was done.                                                                                                                                                                          | INR                 |
| transactionCurrency   | This parameter contain the currency with which transaction was performed.                                                                                                                                                                  | USD                 |
| forexRate             | This parameter contain the foreign exchange rate for currency in the **transactionCurrency** to **transactionCurrency** parameter.                                                                                                         | 80.45               |
| finalSettlement       | This parameter contain the final settlement done to merchant.                                                                                                                                                                              | 20000.45            |

<br />

### List of Unmapped Status

| Unmapped Status    | Status  | Description                                                                                                                                                    |
| ------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| auth               | Success | Auth refers to a transaction that has been authorized by the bank, where the amount is blocked on the customer's account but not yet captured by the merchant. |
| capture            | Success | Capture refers to the transaction where the previously authorized amount is successfully collected from the customer, completing the payment.                  |
| cancel             | Failure | This status is used when an authorized transaction is canceled before capture, and the blocked amount is released back to the customer.                        |
| refund             | Success | Refund refers to the process where a captured (successful) transaction amount is returned back to the customer, either fully or partially.                     |
| refundreversal     | Failure | Refund Reversal occurs when a previously initiated refund is canceled or fails, resulting in the amount being retained by the merchant.                        |
| chargeback         | Failure | Chargeback occurs when a customer disputes a transaction with their bank, leading to the amount being debited from the merchant and returned to the customer.  |
| chargebackreversal | Success | Chargeback Reversal occurs when the merchant successfully contests a chargeback and the disputed amount is returned back to the merchant.                      |

<br />