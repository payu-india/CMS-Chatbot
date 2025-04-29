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
        merchant\_Id
        **mandatory**
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
        from\_date\
        **optional**
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
        to\_date\
        **optional**
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

| Parameter  | Description                                                                                                                                                                |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id         | This parameter contains the  merchant ID.                                                                                                                                  |
| type       | The parameter contains the **chargebacks** as type.                                                                                                                        |
| attributes | This parameter contains the chargeback details in a JSON format. For more information, refer to  [attributes JSON field descriptions](attributes-json-field-descriptions). |

### attributes JSON field descriptions

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>

      <th>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        id
      </td>

      <td>
        The field contains the merchant ID.
      </td>

      <td>
        1295751
      </td>
    </tr>

    <tr>
      <td>
        chargeback-amount
      </td>

      <td>
        The field contains the chargeback amount.
      </td>

      <td>
        1.0
      </td>
    </tr>

    <tr>
      <td>
        chargeback-type
      </td>

      <td>
        The field contains the chargeback type.
      </td>

      <td>
        CB
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        The field contains the chargeback status.
      </td>

      <td>
        Closed Customer Favour
      </td>
    </tr>

    <tr>
      <td>
        reply-before
      </td>

      <td>
        The field contains the date before which the merchant must reply.
      </td>

      <td>
        24-Feb-2023
      </td>
    </tr>

    <tr>
      <td>
        chargeback-reason
      </td>

      <td>
        The field contains the chargeback reason.
      </td>

      <td>
        Non Receipt of Goods or Services
      </td>
    </tr>

    <tr>
      <td>
        bank-case-no
      </td>

      <td>
        The field contains the bank case number for the chargeback.
      </td>

      <td>
        30008130343023154997151
      </td>
    </tr>

    <tr>
      <td>
        debit-date
      </td>

      <td>
        The field contains the chargeback debit date.
      </td>

      <td>
        24-Jul-2023
      </td>
    </tr>

    <tr>
      <td>
        debit-status
      </td>

      <td>
        The field contains the chargeback debit status.
      </td>

      <td>
        Chargeback Debited
      </td>
    </tr>

    <tr>
      <td>
        credit-date
      </td>

      <td>
        The field contains the chargeback credit date.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        customer-dispute-docs
      </td>

      <td>
        The field contains the location of the docs or additional information provided to bank support about the disputed transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        transaction-details
      </td>

      <td>
        This field contains the transaction details in a JSON format.
      </td>

      <td>
         \{\
                        "payu-id": "16652223102",\
                        "transaction-id": "c0bb0c2107f53e791cb4",\
                        "transaction-date": "23-Jan-2023",\
                        "transaction-amount": "1.0",\
                        "pg-name": "HPYIndusInd",\
                        "card-number": "XXXXXXXXXXXX7559",\
                        "refunded": false,\
                        "refund-amount": null,\
                        "bank-reference-number": "302315499715",\
                        "settlement-date": "NA",\
                        "merchant-utr": null,\
                        "product-info": "Product Info",\
                        "additional-charges": "0.0",\
                        "transaction-fee": "1.0",\
                        "udf-1": "",\
                        "udf-5": null,\
                        "card-scheme": null\
                    }
      </td>
    </tr>
  </tbody>
</Table>

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
