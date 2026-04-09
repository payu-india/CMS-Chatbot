---
title: Read Chargeback API
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
The **Read Chargeback** API responds with the all the chargebacks corresponding to the merchant. The chargebacks are filtered out on the basis of dispute received date and pagination.

<ChargebackEnvironment />

## Request parameters

## Without date

This must contain the header with token you get using the Chargeback Dashboard in the following format:

<Callout icon="📘" theme="info">
  **Generate Token**: Use the Chargeback Dashboard to easily generate token in the Chargeback Dashboard. For more information, refer to [Generate Token on Chargeback Dashboard](ref:get_token_chargeback_dashboard).
</Callout>

```
\--header 'X-Optimus-API-Key: <Bearer token>'
```

**Query parameters**

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
        merchant_Id
        `mandatory`
      </td>

      <td>
        This parameter must contain the PayU ID provided by PayU.
      </td>

      <td>
        143419
      </td>
    </tr>
  </tbody>
</Table>

<Callout icon="📘" theme="info">
  #### Notes:

  * The maximum allowed chargebacks in a single request is 500 chargebacks.
  * The maximum time period for which the chargebacks can be retrieved is 20 days.
</Callout>

## With date

This must contain the header with token you get using the Get Token API in the following format:

```
\--header 'X-Optimus-API-Key: <Bearer token>'
```

**Query parameters**

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
        merchant_Id
        `mandatory`
      </td>

      <td>
        This parameter must contain the PayU ID provided by PayU.
      </td>

      <td>
        143419
      </td>
    </tr>

    <tr>
      <td>
        from_date
        `mandatory`
      </td>

      <td>
        This parameter must contain the from date from when the charge back is required.
      </td>

      <td>
        20-02-2023
      </td>
    </tr>

    <tr>
      <td>
        to_date
        `optional`
      </td>

      <td>
        This parameter must contain the to date of charge back.
      </td>

      <td>
        21-02-2023
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

### Without date range

```
curl --location 'https://bankportal.payu.in/api/v1/chargebacks/16652223102' \
--header 'X-Optimus-API-Key: MerchantToken' \
--header 'Cookie: PHPSESSID=uq1sm7npk9dmid33bbe9dvdtcn'
```

### With date range

```
curl --location 'https://bankportal.payu.in/api/v1/chargebacks?from_date=20-02-2023&to_date=21-02-2023&merchant_id=143419' \
--header 'X-Optimus-API-Key: MerchantToken' \
--header 'Cookie: PHPSESSID=uq1sm7npk9dmid33bbe9dvdtcn'
```

## Response parameters

| Parameter | Description                                                                                                                                                   |
| :-------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| data      | This parameter contains the chargeback details as a JSON array. For more information, refer to [data JSON field descriptions](#data-json-field-descriptions). |
| meta      | This parameter contains the pagination details as a JSON object. For more information, refer to [meta JSON field descriptions](#meta-json-field-descriptions) |

### data JSON field descriptions

| Feild      | Description                                                                                                                                                                 |
| :--------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id         | This parameter contains the  chargeback ID.                                                                                                                                 |
| type       | The parameter contains the **chargebacks** as type.                                                                                                                         |
| attributes | This parameter contains the chargeback details in a JSON format. For more information, refer to  [attributes JSON field descriptions](#attributes-json-field-descriptions). |

### attributes JSON field descriptions

| Field                 | Description                                                                                                                                              |                                  |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------- |
| id                    | The field contains the chargeback ID.                                                                                                                    | 1295751                          |
| chargeback-amount     | The field contains the chargeback amount.                                                                                                                | 1.0                              |
| chargeback-type       | The field contains the chargeback type.                                                                                                                  | CB                               |
| status                | The field contains the chargeback status. For more information, refer to [Chargeback Status](doc:chargeback-status).                                     | Closed Customer Favour           |
| reply-before          | The field contains the date before which the merchant must reply.                                                                                        | 24-Feb-2023                      |
| chargeback-reason     | The field contains the chargeback reason.                                                                                                                | Non Receipt of Goods or Services |
| bank-case-no          | The field contains the bank case number for the chargeback.                                                                                              | 30008130343023154997151          |
| debit-date            | The field contains the chargeback debit date.                                                                                                            | 24-Jul-2023                      |
| debit-status          | The field contains the chargeback debit status.                                                                                                          | Chargeback Debited               |
| credit-date           | The field contains the chargeback credit date.                                                                                                           |                                  |
| customer-dispute-docs | The field contains the location of the docs or additional information provided to bank support about the disputed transaction.                           |                                  |
| transaction-details   | This field contains the transaction details in a JSON format. For sample and description, refer to [transaction-details JSON](#transaction-details-json) |                                  |

### transaction-details JSON

#### Sample JSON

```
\{  
"payu-id": "16652223102",
"transaction-id": "c0bb0c2107f53e791cb4",
"transaction-date": "23-Jan-2023",
"transaction-amount": "1.0",
"pg-name": "HPYIndusInd",
"card-number": "XXXXXXXXXXXX7559",
"refunded": false,
"refund-amount": null,
"bank-reference-number": "302315499715",
"settlement-date": "NA",
"merchant-utr": null,
"product-info": "Product Info",
"additional-charges": "0.0",
"transaction-fee": "1.0",
"udf-1": "",
"udf-5": null,
"card-scheme": null
}
```

#### JSON field descriptions

| Field                 | Description                                                                                                                                                       |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| payu-id               | Unique identifier assigned by PayU for the transaction (also known as mihpayid). This serves as the primary reference for all future actions on this transaction. |
| transaction-id        | Merchant's transaction identifier that was used when initiating the payment. This is the unique reference provided by the merchant system.                        |
| transaction-date      | The date when the transaction was processed, typically in the format DD-MMM-YYYY (e.g., "23-Jan-2023").                                                           |
| transaction-amount    | The monetary value of the transaction. This is the original amount that was charged to the customer.                                                              |
| pg-name               | Payment Gateway name used for processing the transaction (e.g., "HPYIndusInd" indicates HDFC Bank Payment Gateway).                                               |
| card-number           | Masked card number used for the transaction, with most digits replaced by X for security (e.g., "XXXXXXXXXXXX7559").                                              |
| refunded              | Boolean flag indicating whether the transaction has been refunded (true/false).                                                                                   |
| refund-amount         | The amount that has been refunded from the transaction, if applicable. Shows null if no refund has been processed.                                                |
| bank-reference-number | Reference number provided by the bank for the transaction. This is used for reconciliation and serves as proof of transaction at the bank's end.                  |
| settlement-date       | The date when the transaction amount was settled to the merchant's account. Shows "NA" if settlement is pending.                                                  |
| merchant-utr          | Unique Transaction Reference number for merchant settlement. Used to track the settlement transaction in the merchant's bank account.                             |
| product-info          | Information about the product or service purchased in the transaction, as provided during payment initiation.                                                     |
| additional-charges    | Any additional charges applied to the transaction beyond the base transaction amount.                                                                             |
| transaction-fee       | The fee charged by PayU for processing the transaction. This is typically a percentage of the transaction amount plus any fixed fees.                             |
| udf-1                 | User-defined field 1 that can be used by merchants for storing custom data related to the transaction.                                                            |
| udf-5                 | User-defined field 5 that can be used by merchants for storing custom data related to the transaction.                                                            |
| card-scheme           | The card network or scheme associated with the payment card (e.g., Visa, Mastercard, RuPay, etc.).                                                                |

### meta JSON field descriptions

| Field      | Description                                                                                                                                                                                                                                                     |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pagination | Contains pagination information for the response. This object provides details about how the results are paginated and the total count of chargebacks. For more information, refer to [pagination JSON field descriptions](#pagination-json-field-descriptions) |

#### pagination JSON field descriptions

| Field             | Description                                                                                                                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| pagination        | Contains pagination information for the response. This object provides details about how the results are paginated and the total count of chargebacks.                                                        |
| per-page          | The number of chargeback records displayed per page in the response. In the example, this is set to 500, meaning up to 500 chargeback records can be displayed on a single page.                              |
| total-chargebacks | The total number of chargeback records that match the query criteria. This indicates how many chargebacks exist in total, regardless of pagination. In the example, there are 3 total chargebacks.            |
| total-pages       | The total number of pages available based on the per-page setting and the total number of chargebacks. In the example, there is 1 page since the total chargebacks (3) is less than the per-page limit (500). |

## Sample response

### Without date range

```
{
    "data": {
        "id": "1295751",
        "type": "chargebacks",
        "attributes": {
            "id": 1295751,
            "chargeback-amount": "1.0",
            "chargeback-type": "CB",
            "chargeback-date": "20-Feb-2023",
            "status": "Closed Customer Favour",
            "reply-before": "24-Feb-2023",
            "chargeback-reason": "Non Receipt of Goods or Services",
            "bank-case-no": "30008130343023154997151",
            "debit-date": "24-Jul-2023",
            "comments": null,
            "debit-status": "Chargeback Debited",
            "credit-date": "NA",
            "customer-dispute-docs": [],
            "transaction-details": {
                "payu-id": "16652223102",
                "transaction-id": "c0bb0c2107f53e791cb4",
                "transaction-date": "23-Jan-2023",
                "transaction-amount": "1.0",
                "pg-name": "HPYIndusInd",
                "card-number": "XXXXXXXXXXXX7559",
                "refunded": false,
                "refund-amount": null,
                "bank-reference-number": "302315499715",
                "settlement-date": "NA",
                "merchant-utr": null,
                "product-info": "Product Info",
                "additional-charges": "0.0",
                "transaction-fee": "1.0",
                "udf-1": "",
                "udf-5": null,
                "card-scheme": null
            },
            "customer-details": {
                "first-name": "Payu-Admin",
                "last-name": "",
                "email": "test@example.com",
                "phone-number": "1234567890"
            }
        }
    }
}
```

### With date range

```
{
    "data": [
        {
            "id": "1295751",
            "type": "chargebacks",
            "attributes": {
                "id": 1295751,
                "chargeback-amount": "1.0",
                "chargeback-type": "CB",
                "chargeback-date": "20-Feb-2023",
                "status": "Closed Customer Favour",
                "reply-before": "24-Feb-2023",
                "chargeback-reason": "Non Receipt of Goods or Services",
                "bank-case-no": "30008130343023154997151",
                "debit-date": "24-Jul-2023",
                "comments": null,
                "debit-status": "Chargeback Debited",
                "credit-date": "NA",
                "customer-dispute-docs": [],
                "transaction-details": {
                    "payu-id": "16652223102",
                    "transaction-id": "c0bb0c2107f53e791cb4",
                    "transaction-date": "23-Jan-2023",
                    "transaction-amount": "1.0",
                    "pg-name": "HPYIndusInd",
                    "card-number": "XXXXXXXXXXXX7559",
                    "refunded": false,
                    "refund-amount": null,
                    "bank-reference-number": "302315499715",
                    "settlement-date": "NA",
                    "merchant-utr": null,
                    "product-info": "Product Info",
                    "additional-charges": "0.0",
                    "transaction-fee": "1.0",
                    "udf-1": "",
                    "udf-5": null,
                    "card-scheme": null
                },
                "customer-details": {
                    "first-name": "Payu-Admin",
                    "last-name": "",
                    "email": "test@example.com",
                    "phone-number": "1234567890"
                }
            }
        },
        {
            "id": "1295752",
            "type": "chargebacks",
            "attributes": {
                "id": 1295752,
                "chargeback-amount": "1.0",
                "chargeback-type": "CB",
                "chargeback-date": "20-Feb-2023",
                "status": "Closed Customer Favour",
                "reply-before": "24-Feb-2023",
                "chargeback-reason": "Non Receipt of Goods or Services",
                "bank-case-no": "30008130343023159959693",
                "debit-date": "24-Jul-2023",
                "comments": null,
                "debit-status": "Chargeback Debited",
                "credit-date": "NA",
                "customer-dispute-docs": [],
                "transaction-details": {
                    "payu-id": "16652143419",
                    "transaction-id": "0d344315b040a777f30a",
                    "transaction-date": "23-Jan-2023",
                    "transaction-amount": "1.0",
                    "pg-name": "HPYIndusInd",
                    "card-number": "XXXXXXXXXXXX7559",
                    "refunded": false,
                    "refund-amount": null,
                    "bank-reference-number": "302315995969",
                    "settlement-date": "NA",
                    "merchant-utr": null,
                    "product-info": "Product Info",
                    "additional-charges": "0.0",
                    "transaction-fee": "1.0",
                    "udf-1": "",
                    "udf-5": null,
                    "card-scheme": null
                },
                "customer-details": {
                    "first-name": "Payu-Admin",
                    "last-name": "",
                    "email": "test@example.com",
                    "phone-number": "1234567890"
                }
            }
        },
        {
            "id": "1295753",
            "type": "chargebacks",
            "attributes": {
                "id": 1295753,
                "chargeback-amount": "1.0",
                "chargeback-type": "CB",
                "chargeback-date": "20-Feb-2023",
                "status": "Closed Customer Favour",
                "reply-before": "24-Feb-2023",
                "chargeback-reason": "Non Receipt of Goods or Services",
                "bank-case-no": "30008130343019172078172",
                "debit-date": "24-Jul-2023",
                "comments": null,
                "debit-status": "Chargeback Debited",
                "credit-date": "NA",
                "customer-dispute-docs": [],
                "transaction-details": {
                    "payu-id": "16626771711",
                    "transaction-id": "f73f8ee2567488b03269",
                    "transaction-date": "19-Jan-2023",
                    "transaction-amount": "1.0",
                    "pg-name": "HPYIndusInd",
                    "card-number": "XXXXXXXXXXXX7559",
                    "refunded": false,
                    "refund-amount": null,
                    "bank-reference-number": "301917207817",
                    "settlement-date": "NA",
                    "merchant-utr": null,
                    "product-info": "Product Info",
                    "additional-charges": "0.0",
                    "transaction-fee": "1.0",
                    "udf-1": "",
                    "udf-5": null,
                    "card-scheme": null
                },
                "customer-details": {
                    "first-name": "Payu-Admin",
                    "last-name": "",
                    "email": "test@example.com",
                    "phone-number": "1234567890"
                }
            }
        }
    ],
    "meta": {
        "pagination": {
            "per-page": 500,
            "total-chargebacks": 3,
            "total-pages": 1
        }
    }
}
```
