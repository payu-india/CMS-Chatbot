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

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "merchant_Id  \n**mandatory**",
    "0-1": "This parameter must contain the PayU ID provided by PayU.",
    "0-2": "143419",
    "1-0": "from_date  \n**optional**",
    "1-1": "This parameter must contain the from date from when the charge back is required.",
    "1-2": "20-02-2023",
    "2-0": "to_date  \n**optional**",
    "2-1": "This parameter must contain the to date of charge back.",
    "2-2": "21-02-2023"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


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
| type       | The parameter contains the **chargebacks ** as type.                                                                                                                       |
| attributes | This parameter contains the chargeback details in a JSON format. For more information, refer to  [attributes JSON field descriptions](attributes-json-field-descriptions). |

### attributes JSON field descriptions

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "h-2": "",
    "0-0": "id",
    "0-1": "The field contains the merchant ID.",
    "0-2": "1295751",
    "1-0": "chargeback-amount",
    "1-1": "The field contains the chargeback amount.",
    "1-2": "1.0",
    "2-0": "chargeback-type",
    "2-1": "The field contains the chargeback type.",
    "2-2": "CB",
    "3-0": "status",
    "3-1": "The field contains the chargeback status.",
    "3-2": "Closed Customer Favour",
    "4-0": "reply-before",
    "4-1": "The field contains the date before which the merchant must reply.",
    "4-2": "24-Feb-2023",
    "5-0": "chargeback-reason",
    "5-1": "The field contains the chargeback reason.",
    "5-2": "Non Receipt of Goods or Services",
    "6-0": "bank-case-no",
    "6-1": "The field contains the bank case number for the chargeback.",
    "6-2": "30008130343023154997151",
    "7-0": "debit-date",
    "7-1": "The field contains the chargeback debit date.",
    "7-2": "24-Jul-2023",
    "8-0": "debit-status",
    "8-1": "The field contains the chargeback debit status.",
    "8-2": "Chargeback Debited",
    "9-0": "credit-date",
    "9-1": "The field contains the chargeback credit date.",
    "9-2": "",
    "10-0": "customer-dispute-docs",
    "10-1": "The field contains the location of the docs or additional information provided to bank support about the disputed transaction.",
    "10-2": "",
    "11-0": "transaction-details",
    "11-1": "This field contains the transaction details in a JSON format.",
    "11-2": " {  \n                \"payu-id\": \"16652223102\",  \n                \"transaction-id\": \"c0bb0c2107f53e791cb4\",  \n                \"transaction-date\": \"23-Jan-2023\",  \n                \"transaction-amount\": \"1.0\",  \n                \"pg-name\": \"HPYIndusInd\",  \n                \"card-number\": \"XXXXXXXXXXXX7559\",  \n                \"refunded\": false,  \n                \"refund-amount\": null,  \n                \"bank-reference-number\": \"302315499715\",  \n                \"settlement-date\": \"NA\",  \n                \"merchant-utr\": null,  \n                \"product-info\": \"Product Info\",  \n                \"additional-charges\": \"0.0\",  \n                \"transaction-fee\": \"1.0\",  \n                \"udf-1\": \"\",  \n                \"udf-5\": null,  \n                \"card-scheme\": null  \n            }"
  },
  "cols": 3,
  "rows": 12,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


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