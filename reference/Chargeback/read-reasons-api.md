---
title: Read Reasons API
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
The **Read Reason** API lists all the reasons required for the merchant to provide in order to accept or contest the chargeback.

<ChargebackEnvironment />

## Request parameters

This must contain the header with token you get using the Chargeback Dashboard in the following format:

<Callout icon="📘" theme="info">
  ###

  **Generate Token**: Use the Chargeback Dashboard to easily generate token in the Chargeback Dashboard. For more information, refer to [Generate Token on Chargeback Dashboard](ref:get_token_chargeback_dashboard).
</Callout>

```
\--header 'X-Optimus-API-Key: <Bearer token>'
```

## Sample request

```
curl --location 'https://bankportal.payu.in/api/v1/reasons' \
--header 'X-Optimus-API-Key: MerchantToken' \
--header 'Cookie: PHPSESSID=uq1sm7npk9dmid33bbe9dvdtcn'
```

## Response parameters

| Parameter  | Description                                                                                                                                                                        |
| :--------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id         | This parameter contains the  merchant ID.                                                                                                                                          |
| type       | The parameter contains the **reasons** as type. The Reasons mapping table provides reason-type, reason-text and identifier as in the [Sample response](#sample-response).          |
| attributes | This parameter contains the chargeback reason details in a JSON format. For more information, refer to  [attributes JSON field descriptions](#attributes-json-field-descriptions). |

### Reasons mapping

|                   |                                                                                                                                             |                                      |                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------------ |
| **Reason Type**   | **Reason Text**                                                                                                                             | **Identifier**                       | **Reason Mapping** |
| accept            | Customer cancelled the order                                                                                                                | 094fd3fe-4923-4819-becc-14d08054ff2d | Parent             |
| accept            | Product out of stock                                                                                                                        | b74af116-4521-4ce2-9d91-4b3a0ea0a3fc | Parent             |
| accept            | Product was returned by the customer                                                                                                        | 5989dee4-f764-4fcf-8e83-be53992c778e | Parent             |
| accept            | Product lost in transit                                                                                                                     | f3b35551-462f-457d-b3c2-ae3db3ce0c04 | Parent             |
| accept            | Product returned due to incorrect address                                                                                                   | fd5477bd-98a3-4a37-83da-903086a224b2 | Parent             |
| accept            | Order/Booking not successful                                                                                                                | 9b687337-beee-46d7-9ec0-60098121bbb5 | Parent             |
| accept            | Others                                                                                                                                      | 96ad8e74-c417-4ea7-a6ab-f768078d2c5c | Parent             |
| reject            | Product/Services delivered                                                                                                                  | 9c2c093c-648a-40b5-8b79-461466578b0c | Parent             |
| reject            | Product/Services Partially delivered                                                                                                        | 6972b1c2-e3e8-49f6-8e15-3801bfa5a01f | Parent             |
| reject            | Customer withdrawn the chargeback                                                                                                           | 3f67a066-b399-4070-9519-c34c357e9713 | Parent             |
| reject            | Transaction already refunded                                                                                                                | 1a17831a-ef36-4cc3-bb91-5190466b7000 | Parent             |
| reject            | Product is delivered. Option to upload delivered details of the courier company, shipping number, Invoice.                                  | 07b310c2-8c63-4b82-9b87-53a4b963adac | Child              |
| reject            | Service is delivered. Option to upload details of the service, claiming service fulfillment details, Invoice.                               | 1d3dc863-a2c5-4bde-95ee-66f6be9f7848 | Child              |
| reject            | Product is partially delivered. Option to upload partially delivered details of the courier company, shipping number, Invoice.              | 7e932855-5103-4610-8060-67258f48c1ef | Child              |
| reject            | Service is partially delivered. Option to upload partially delivered details of the service, claiming service fulfillment details, Invoice. | 1740b9ab-614f-4ffc-9764-adf777915dfe | Child              |
| reject            | Transaction refunded through PayU Panel (Status of the refund in PayU Panel)                                                                | 3ba427be-e1b7-44b1-84f1-95a48295bde8 | Child              |
| reject            | Transaction refunded outside PayU Panel                                                                                                     | 37980bbf-fb5e-42d7-9780-c5a9079e115d | Child              |
| reject            | Refund is in pending status.                                                                                                                | 2b4a6805-a2e1-4b8c-bf88-b8f52c68c6ce | Child              |
| reject            | Refund is requested through bank channel.                                                                                                   | 7f1d2c03-b893-4d88-bbee-8171c4759dc9 | Child              |
| reject            | Refund is successfully processed.                                                                                                           | 4d33236d-77ac-4d19-a257-8d63153ec10f | Child              |
| partially\_accept | Product/Services Partially delivered                                                                                                        | bb10e1bb-f128-4ace-ab0f-59881f11fa4d | Parent             |
| partially\_accept | Transaction partially refunded                                                                                                              | 20545060-e1e5-4718-b528-ea81436833ed | Parent             |
| partially\_accept | Transaction partially refunded outside PayU Panel                                                                                           | ae4b70b4-703e-41e8-bf70-3676b377ce9e | Parent             |
| partially\_accept | Product lost in transit                                                                                                                     | 084bd395-371c-4f76-9938-9e785e855ba1 | Parent             |
| partially\_accept | Product was returned by the customer                                                                                                        | 4bdfb55e-7a3e-4706-a653-072da2be7ebf | Parent             |
| partially\_accept | Customer cancelled the order                                                                                                                | 4e417a20-1cd3-47de-8bb7-34e2c002f126 | Parent             |
| partially\_accept | Full refund not due as per our T\&C                                                                                                         | 0cc9cead-d01e-47d7-8fc2-64e4627e2f72 | Parent             |
| partially\_accept | Others                                                                                                                                      | 8d55dc20-a304-4a0f-885d-0b05705986a5 | Parent             |

### attributes JSON field descriptions

| Field       | Description                                                                                                                                                               | Example                              |
| :---------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------- |
| identifier  | This field contains the reason identifier. This identified is used in [Accept Chargeback API](ref:accept-chargeback-api) to accept the chargeback.                        | 094fd3fe-4923-4819-becc-14d08054ff2d |
| parent-id   | This field contains the parent ID of the reason.                                                                                                                          |                                      |
| reason-text | This field contains the reason for the chargeback. For the list of reasons, refer to [Chargeback Closure Reasons](https://docs.payu.in/docs/chargeback-closure-reasons) . | Customer cancelled the order         |
| field-type  | This field contains the field type of the reason to be displayed on UI.                                                                                                   | radio-button                         |
| reason-type | This field contains the reason type. For the list of closure reason types, refer to [Chargeback Closure Reasons](https://docs.payu.in/docs/chargeback-closure-reasons) .  | accept                               |
| message     | This field contains the reason message.                                                                                                                                   | false                                |
| form-data   | This field contains the form data of the read reason.                                                                                                                     |                                      |

## Sample response

```
{
    "data": [
        {
            "id": "1",
            "type": "reasons",
            "attributes": {
                "identifier": "094fd3fe-4923-4819-becc-14d08054ff2d",
                "parent-id": null,
                "reason-text": "Customer cancelled the order",
                "field-type": "radio-button",
                "reason-type": "accept",
                "message": false,
                "form-data": []
            }
        },
        {
            "id": "2",
            "type": "reasons",
            "attributes": {
                "identifier": "b74af116-4521-4ce2-9d91-4b3a0ea0a3fc",
                "parent-id": null,
                "reason-text": "Product out of stock",
                "field-type": "radio-button",
                "reason-type": "accept",
                "message": false,
                "form-data": []
            }
        },
        {
            "id": "3",
            "type": "reasons",
            "attributes": {
                "identifier": "5989dee4-f764-4fcf-8e83-be53992c778e",
                "parent-id": null,
                "reason-text": "Product was returned by the customer",
                "field-type": "radio-button",
                "reason-type": "accept",
                "message": false,
                "form-data": []
            }
        },
        {
            "id": "4",
            "type": "reasons",
            "attributes": {
                "identifier": "f3b35551-462f-457d-b3c2-ae3db3ce0c04",
                "parent-id": null,
                "reason-text": "Product lost in transit",
                "field-type": "radio-button",
                "reason-type": "accept",
                "message": false,
                "form-data": []
            }
        },
        {
            "id": "5",
            "type": "reasons",
            "attributes": {
                "identifier": "fd5477bd-98a3-4a37-83da-903086a224b2",
                "parent-id": null,
                "reason-text": "Product returned due to incorrect address",
                "field-type": "radio-button",
                "reason-type": "accept",
                "message": false,
                "form-data": []
            }
        },
        {
            "id": "12",
            "type": "reasons",
            "attributes": {
                "identifier": "9c2c093c-648a-40b5-8b79-461466578b0c",
                "parent-id": null,
                "reason-text": "Product/Services delivered",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": [
                    {
                        "identifier": "9c2c093c-648a-40b5-8b79-461466578b0c-comments",
                        "form-data-text": "Comments",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    }
                ]
            }
        },
        {
            "id": "13",
            "type": "reasons",
            "attributes": {
                "identifier": "6972b1c2-e3e8-49f6-8e15-3801bfa5a01f",
                "parent-id": null,
                "reason-text": "Product/Services Partially delivered",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": [
                    {
                        "identifier": "6972b1c2-e3e8-49f6-8e15-3801bfa5a01f-comments",
                        "form-data-text": "Comments",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    }
                ]
            }
        },
        {
            "id": "14",
            "type": "reasons",
            "attributes": {
                "identifier": "3f67a066-b399-4070-9519-c34c357e9713",
                "parent-id": null,
                "reason-text": "Customer withdrawn the chargeback",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": [
                    {
                        "identifier": "3f67a066-b399-4070-9519-c34c357e9713-comments",
                        "form-data-text": "Comments",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "d26e3bc8-79ea-4812-9227-7a81e875547c",
                        "form-data-text": "Upload customer Email/letter",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    }
                ]
            }
        },
        {
            "id": "15",
            "type": "reasons",
            "attributes": {
                "identifier": "1a17831a-ef36-4cc3-bb91-5190466b7000",
                "parent-id": null,
                "reason-text": "Transaction already refunded",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": [
                    {
                        "identifier": "1a17831a-ef36-4cc3-bb91-5190466b7000-comments",
                        "form-data-text": "Comments",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    }
                ]
            }
        },
        {
            "id": "16",
            "type": "reasons",
            "attributes": {
                "identifier": "07b310c2-8c63-4b82-9b87-53a4b963adac",
                "parent-id": "9c2c093c-648a-40b5-8b79-461466578b0c",
                "reason-text": "Product",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": [
                    {
                        "identifier": "9b466317-5041-42f9-b6d8-084d5d988465",
                        "form-data-text": "Details of the product",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    },
                    {
                        "identifier": "78c41edb-61fa-463f-9e0d-bc149c7b8f45",
                        "form-data-text": "Product Delivered",
                        "field-type": "checkbox_tag",
                        "options": [
                            "yes"
                        ],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "d0d9b45c-077c-4cfd-8ec1-260d6ddfb0d1",
                        "form-data-text": "Name of the courier company used",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "e36f1635-3e16-40fe-bbe5-9cbf668e3e2e",
                        "form-data-text": "AWB/shipping number",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "c9820d99-f515-4e16-93d2-e5032b454286",
                        "form-data-text": "Upload screen-shot of the signed proof of delivery",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "4e6d4368-0dfc-4672-89ac-6cf35975f798",
                        "form-data-text": "Screen-shot of the invoice",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "4c031b62-884c-4369-ae02-78162eac2c5b",
                        "form-data-text": "Did the customer ever tried to return/cancel the order with you (Tick if Yes) ?",
                        "field-type": "checkbox_tag",
                        "options": [
                            "yes"
                        ],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "97f05d6c-22ab-4e3a-afdf-7d9cf1304421",
                        "form-data-text": "Provide Details of return/cancellation",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    }
                ]
            }
        },
        {
            "id": "17",
            "type": "reasons",
            "attributes": {
                "identifier": "1d3dc863-a2c5-4bde-95ee-66f6be9f7848",
                "parent-id": "9c2c093c-648a-40b5-8b79-461466578b0c",
                "reason-text": "Services",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": [
                    {
                        "identifier": "0463ef8c-5450-4616-a054-5ab51d4a4647",
                        "form-data-text": "Details of the services",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    },
                    {
                        "identifier": "222911cb-947b-46c4-bfb0-4d7045822b7f",
                        "form-data-text": "Proof of services",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "0ab3ef52-443d-4c6c-a3f7-62ae727f9d92",
                        "form-data-text": "Upload screen-shot of the claiming service fulfillment details",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "a7e2ba36-7723-44e6-bbe5-513865c88698",
                        "form-data-text": "Screen-shot of the invoice",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "20c219b1-7294-4073-9f0e-dd6ef76a44d4",
                        "form-data-text": "Upload any other relevant details",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    }
                ]
            }
        },
        {
            "id": "18",
            "type": "reasons",
            "attributes": {
                "identifier": "7e932855-5103-4610-8060-67258f48c1ef",
                "parent-id": "6972b1c2-e3e8-49f6-8e15-3801bfa5a01f",
                "reason-text": "Product",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": [
                    {
                        "identifier": "044126da-49cb-4666-9b6f-5bcf50e359a2",
                        "form-data-text": "Details of the product",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "95e74135-c2d1-4de6-9a3e-c49084cdde5f",
                        "form-data-text": "Which part of the order Delivered",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "26aef6db-7641-4950-a93b-45b0bd39fc5e",
                        "form-data-text": "Amount that needs to refund",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "0f71a35e-3794-4eaf-8bd2-c4dfb5d03776",
                        "form-data-text": "Name of the courier company used",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "88626cff-8a4b-4b96-96bb-11a698ebf798",
                        "form-data-text": "AWB/shipping number",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "56be7d9a-2467-4718-a106-9dd77d980d81",
                        "form-data-text": "Upload screen-shot of the signed proof of delivery",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "722f4b64-bc1a-430d-a1a3-cb21661702ac",
                        "form-data-text": "Screen-shot of the invoice",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    }
                ]
            }
        },
        {
            "id": "19",
            "type": "reasons",
            "attributes": {
                "identifier": "1740b9ab-614f-4ffc-9764-adf777915dfe",
                "parent-id": "6972b1c2-e3e8-49f6-8e15-3801bfa5a01f",
                "reason-text": "Services",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": [
                    {
                        "identifier": "18f071a8-76e8-429b-85d6-a101973ee26a",
                        "form-data-text": "Details of the services",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "5e7ec548-95d9-4d69-81b0-55deb45fa957",
                        "form-data-text": "Proof of services",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "75c065a1-9562-4e01-bc3b-83c6f9017fc7",
                        "form-data-text": "Upload screen-shot of the claiming service fulfillment details",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "63dc1d71-867e-4d52-b8bd-e98efb65d77b",
                        "form-data-text": "Screen-shot of the invoice",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "8f0eb9f9-ab3a-4852-9b9d-df91d0f85623",
                        "form-data-text": "Upload any other relevant details",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    }
                ]
            }
        },
        {
            "id": "20",
            "type": "reasons",
            "attributes": {
                "identifier": "3ba427be-e1b7-44b1-84f1-95a48295bde8",
                "parent-id": "1a17831a-ef36-4cc3-bb91-5190466b7000",
                "reason-text": "Transaction refunded through PayU Panel (Status of the refund in PayU Panel)",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": []
            }
        },
        {
            "id": "21",
            "type": "reasons",
            "attributes": {
                "identifier": "37980bbf-fb5e-42d7-9780-c5a9079e115d",
                "parent-id": "1a17831a-ef36-4cc3-bb91-5190466b7000",
                "reason-text": "Transaction refunded outside PayU Panel",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": [
                    {
                        "identifier": "aad0b645-ec3e-491e-b88b-406ec5ee0bcd",
                        "form-data-text": "Details of refund",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "cb47fb64-e2fc-49bd-a131-7632d3408522",
                        "form-data-text": "Amount of refund",
                        "field-type": "input_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "fc89bbf6-ce58-4b95-b430-5d8bf5abe491",
                        "form-data-text": "Upload screen-shot of the refund proof",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "ad7cad9f-e1f1-4377-b608-bacc9517f306",
                        "form-data-text": "Upload customer confirmation of the refund",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    }
                ]
            }
        },
        {
            "id": "22",
            "type": "reasons",
            "attributes": {
                "identifier": "2b4a6805-a2e1-4b8c-bf88-b8f52c68c6ce",
                "parent-id": "3ba427be-e1b7-44b1-84f1-95a48295bde8",
                "reason-text": "Queued",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": []
            }
        },
        {
            "id": "23",
            "type": "reasons",
            "attributes": {
                "identifier": "7f1d2c03-b893-4d88-bbee-8171c4759dc9",
                "parent-id": "3ba427be-e1b7-44b1-84f1-95a48295bde8",
                "reason-text": "Requested",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": []
            }
        },
        {
            "id": "24",
            "type": "reasons",
            "attributes": {
                "identifier": "4d33236d-77ac-4d19-a257-8d63153ec10f",
                "parent-id": "3ba427be-e1b7-44b1-84f1-95a48295bde8",
                "reason-text": "Successful",
                "field-type": "radio-button",
                "reason-type": "reject",
                "message": false,
                "form-data": []
            }
        },
        {
            "id": "26",
            "type": "reasons",
            "attributes": {
                "identifier": "9b687337-beee-46d7-9ec0-60098121bbb5",
                "parent-id": null,
                "reason-text": "Order/Booking not successfull",
                "field-type": "radio-button",
                "reason-type": "accept",
                "message": false,
                "form-data": []
            }
        },
        {
            "id": "28",
            "type": "reasons",
            "attributes": {
                "identifier": "bb10e1bb-f128-4ace-ab0f-59881f11fa4d",
                "parent-id": null,
                "reason-text": "Product/Services Partially delivered",
                "field-type": "radio-button",
                "reason-type": "partially_accept",
                "message": false,
                "form-data": [
                    {
                        "identifier": "6f92dad0-4446-4465-bfea-17f587e973d4",
                        "form-data-text": "Partially accept amount",
                        "field-type": "amount_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    },
                    {
                        "identifier": "bb10e1bb-f128-4ace-ab0f-59881f11fa4d-comments",
                        "form-data-text": "Comments",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "200edfd3-84b6-4311-8486-23887f167772",
                        "form-data-text": "Supporting documents",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    }
                ]
            }
        },
        {
            "id": "29",
            "type": "reasons",
            "attributes": {
                "identifier": "20545060-e1e5-4718-b528-ea81436833ed",
                "parent-id": null,
                "reason-text": "Transaction partially refunded",
                "field-type": "radio-button",
                "reason-type": "partially_accept",
                "message": false,
                "form-data": [
                    {
                        "identifier": "acd3c90e-9b72-4974-bda2-10ab2ed2bad9",
                        "form-data-text": "Partially accept amount",
                        "field-type": "amount_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    },
                    {
                        "identifier": "20545060-e1e5-4718-b528-ea81436833ed-comments",
                        "form-data-text": "Comments",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "483c9a7f-7bbd-46a8-adbd-783c8065b7bf",
                        "form-data-text": "Supporting documents",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    }
                ]
            }
        },
        {
            "id": "30",
            "type": "reasons",
            "attributes": {
                "identifier": "ae4b70b4-703e-41e8-bf70-3676b377ce9e",
                "parent-id": null,
                "reason-text": "Transaction partially refunded outside PayU Panel",
                "field-type": "radio-button",
                "reason-type": "partially_accept",
                "message": false,
                "form-data": [
                    {
                        "identifier": "d51189f9-fd6c-4d4d-b0a8-ba21a27f6769",
                        "form-data-text": "Partially accept amount",
                        "field-type": "amount_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    },
                    {
                        "identifier": "ae4b70b4-703e-41e8-bf70-3676b377ce9e-comments",
                        "form-data-text": "Comments",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "f672a8ec-c5bf-4e08-8608-03933845e03f",
                        "form-data-text": "File Element",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    }
                ]
            }
        },
        {
            "id": "31",
            "type": "reasons",
            "attributes": {
                "identifier": "084bd395-371c-4f76-9938-9e785e855ba1",
                "parent-id": null,
                "reason-text": "Product lost in transit",
                "field-type": "radio-button",
                "reason-type": "partially_accept",
                "message": false,
                "form-data": [
                    {
                        "identifier": "4c6ccb8f-9147-4ea1-8709-d5a64057a734",
                        "form-data-text": "Partially accept amount",
                        "field-type": "amount_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    },
                    {
                        "identifier": "084bd395-371c-4f76-9938-9e785e855ba1-comments",
                        "form-data-text": "Comments",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "add2ba5f-b2d1-40b0-87ea-a21181d3deb5",
                        "form-data-text": "Supporting documents",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    }
                ]
            }
        },
        {
            "id": "32",
            "type": "reasons",
            "attributes": {
                "identifier": "4bdfb55e-7a3e-4706-a653-072da2be7ebf",
                "parent-id": null,
                "reason-text": "Product was returned by the customer",
                "field-type": "radio-button",
                "reason-type": "partially_accept",
                "message": false,
                "form-data": [
                    {
                        "identifier": "82bc03d3-6c8a-4f50-9407-9b9adc7fa631",
                        "form-data-text": "Partially accept amount",
                        "field-type": "amount_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    },
                    {
                        "identifier": "4bdfb55e-7a3e-4706-a653-072da2be7ebf-comments",
                        "form-data-text": "Comments",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "d74125c8-f7c0-43b4-be35-39a03fdde5d2",
                        "form-data-text": "Supporting documents",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    }
                ]
            }
        },
        {
            "id": "33",
            "type": "reasons",
            "attributes": {
                "identifier": "4e417a20-1cd3-47de-8bb7-34e2c002f126",
                "parent-id": null,
                "reason-text": "Customer cancelled the order",
                "field-type": "radio-button",
                "reason-type": "partially_accept",
                "message": false,
                "form-data": [
                    {
                        "identifier": "39fd5391-a3fc-4e95-bcdc-0c9ef0fe604f",
                        "form-data-text": "Partially accept amount",
                        "field-type": "amount_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    },
                    {
                        "identifier": "4e417a20-1cd3-47de-8bb7-34e2c002f126-comments",
                        "form-data-text": "Comments",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "a466c196-a643-493a-bf15-6cba8de1a01b",
                        "form-data-text": "Supporting documents",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    }
                ]
            }
        },
        {
            "id": "35",
            "type": "reasons",
            "attributes": {
                "identifier": "0cc9cead-d01e-47d7-8fc2-64e4627e2f72",
                "parent-id": null,
                "reason-text": "Full refund not due as per our T&C",
                "field-type": "radio-button",
                "reason-type": "partially_accept",
                "message": false,
                "form-data": [
                    {
                        "identifier": "462138e7-0bf8-4358-b617-0659bbd907be",
                        "form-data-text": "Partially accept amount",
                        "field-type": "amount_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    },
                    {
                        "identifier": "0cc9cead-d01e-47d7-8fc2-64e4627e2f72-comments",
                        "form-data-text": "Comments",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "bc3e2b49-25d6-47f4-a0d2-3636edbce717",
                        "form-data-text": "Supporting documents",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    }
                ]
            }
        },
        {
            "id": "36",
            "type": "reasons",
            "attributes": {
                "identifier": "8d55dc20-a304-4a0f-885d-0b05705986a5",
                "parent-id": null,
                "reason-text": "Others",
                "field-type": "radio-button",
                "reason-type": "partially_accept",
                "message": false,
                "form-data": [
                    {
                        "identifier": "32a73e00-95f7-45c7-bb56-f34ca56ac6c1",
                        "form-data-text": "Partially accept amount",
                        "field-type": "amount_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    },
                    {
                        "identifier": "8d55dc20-a304-4a0f-885d-0b05705986a5-comments",
                        "form-data-text": "Comments",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": false
                    },
                    {
                        "identifier": "df9fdd4d-28a2-4d9e-bc24-ae143cf79d0f",
                        "form-data-text": "Reason for partially accepting chargeback",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    },
                    {
                        "identifier": "5aba75d8-79f3-4222-946a-f14a84deb362",
                        "form-data-text": "Supporting documents",
                        "field-type": "file_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    }
                ]
            }
        },
        {
            "id": "37",
            "type": "reasons",
            "attributes": {
                "identifier": "96ad8e74-c417-4ea7-a6ab-f768078d2c5c",
                "parent-id": null,
                "reason-text": "Others",
                "field-type": "radio-button",
                "reason-type": "accept",
                "message": false,
                "form-data": [
                    {
                        "identifier": "887a40ec-fd6e-4bd5-8287-fee5fe926318",
                        "form-data-text": "Reason for accepting chargeback",
                        "field-type": "text_area_tag",
                        "options": [],
                        "blank-allowed": false,
                        "mandatory": true
                    }
                ]
            }
        }
    ]
}
```

<br />
