---
title: Accept Chargeback API
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
The **Accept Chargeback** API allows the merchant user to accept the chargeback by providing the appropriate reasons in the request body against the chargeback and merchant ID.

HTTP Method: **PATCH**

<ChargebackEnvironment />

## Request parameters

This must contain the header with token you get using the Get Token API in the following format: 

```
\--header 'X-Optimus-API-Key: <Bearer token>'
```

**Form data**

| Parameter  | Description                                                                                                                                                   | Example                              |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------- |
| identifier | The identifier that was received in response when you used the **Read Reasons** API. For more information, refer to [Read Reasons API](ref:read-reasons-api). | 6f92dad0-4446-4465-bfea-17f587e973d4 |
| value      | The value that was received in response when you used the **Read Reasons** API. For more information, refer to [Read Reasons API](ref:read-reasons-api) .     | 1                                    |

## Sample request

```
curl --location --request PATCH 'https://bankportal.payu.in//api/v1/chargebacks/accept' \
--header 'X-Optimus-API-Key: MERCHANT KEY' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--form 'reason_code[0][uuid]="bb10e1bb-f128-4ace-ab0f-59881f11fa4d"' \
--form 'reason_code[0][form_data][0][identifier]="6f92dad0-4446-4465-bfea-17f587e973d4"' \
--form 'reason_code[0][form_data][0][value]="1"' \
--form 'reason_code[0][form_data][1][identifier]="bb10e1bb-f128-4ace-ab0f-59881f11fa4d-comments"' \
--form 'reason_code[0][form_data][1][value]="Test Comment"' \
--form 'reason_code[0][form_data][2][identifier]="200edfd3-84b6-4311-8486-23887f167772"' \
--form 'reason_code[0][form_data][2][value]=@"/Users/ankit.dagar/Pictures/Screenshots/Screenshot 2022-11-04 at 11.07.06 AM.png"' \
--form 'chargeback_id="1128897"' \
--form 'merchant_id="2"'
```

### Partially accept chargeback

```
curl --location --request PATCH 'https://bankportal.payu.in//api/v1/chargebacks/partially_accept' \
--header 'X-Optimus-API-Key: MERCHANT KEY' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--form 'reason_code[0][uuid]="bb10e1bb-f128-4ace-ab0f-59881f11fa4d"' \
--form 'reason_code[0][form_data][0][identifier]="6f92dad0-4446-4465-bfea-17f587e973d4"' \
--form 'reason_code[0][form_data][0][value]="1"' \
--form 'reason_code[0][form_data][1][identifier]="bb10e1bb-f128-4ace-ab0f-59881f11fa4d-comments"' \
--form 'reason_code[0][form_data][1][value]="Test Comment"' \
--form 'reason_code[0][form_data][2][identifier]="200edfd3-84b6-4311-8486-23887f167772"' \
--form 'reason_code[0][form_data][2][value]=@"/Users/ankit.dagar/Pictures/Screenshots/Screenshot 2022-11-04 at 11.07.06 AM.png"' \
--form 'chargeback_id="1128897"' \
--form 'merchant_id="2"'
```

## Response parameters

| Parameter  | Description                                                                                                                                                                |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id         | This parameter contains the  merchant ID.                                                                                                                                  |
| type       | The parameter contains the **chargeback-details** as type.                                                                                                                 |
| attributes | This parameter contains the chargeback details in a JSON format. For more information, refer to  [attributes JSON field descriptions](attributes-json-field-descriptions). |

### attributes JSON field descriptions

| Field   | Description                                       | Example            |
| :------ | :------------------------------------------------ | :----------------- |
| id      | This field contains the  merchant ID.             | 1035881            |
| payu-id | The field contains the PayU ID of the merchant.   | 15420278029        |
| status  | This field contains the status of the chargeback. | Pending Doc Review |

## Sample response

```
{
    "data": {
        "id": "1035881",
        "type": "chargeback-details",
        "attributes": {
            "id": 1035881,
            "payu-id": "15420278029",
            "status": "Pending Doc Review"
        }
    }
}
```
