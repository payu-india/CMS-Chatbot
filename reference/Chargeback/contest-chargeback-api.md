---
title: Contest Chargeback API
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
The **Contest Chargeback** API allows the merchant to contest the chargeback by providing the appropriate reasons in the request body against the chargeback and merchant ID.

HTTP Method: **PATCH**

<ChargebackEnvironment />

## Request parameters

This must contain the header with token you get using the Get Token API in the following format: 

```
\--header 'X-Optimus-API-Key: <Bearer token>'
```

**Form data**

| Parameter     | Description                                                                                                                                                                                          | Example                              |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| chargeback_id | This parameter must contain the chargeback ID that customer received from PayU.                                                                                                                      | 1035881                              |
| merchant_id   | The merchant ID provided to merchant while onboarding.                                                                                                                                               | 2                                    |
| identifier    | The identifier that was received in response when you used the **Read Reasons** API. For more information, refer to [Read Reasons API](ref:read-reasons-api).                                        | 6f92dad0-4446-4465-bfea-17f587e973d4 |
| value         | The response that you wish to send (to the frontend). The value can be any of the responses from the **Read Reasons** API. For more information, refer to [Read Reasons API](ref:read-reasons-api) . | 1                                    |

## Sample request

```curl
curl --location --globoff --request PATCH 'https://chbuat.payu.in/api/v1/chargebacks/contest' \
--header 'X-Optimus-API-Key: MERCHANT KEY' \
--header 'Content-Type: multipart/form-data' \
--form 'chargeback_id="1035881"' \
--form 'merchant_id="2"' \
--form 'reason_code[0][uuid]="9c2c093c-648a-40b5-8b79-461466578b0c"' \
--form 'reason_code[0][form_data	][0][identifier]="9c2c093c-648a-40b5-8b79-461466578b0c-comments"' \
--form 'reason_code[0][form_data][0][value]="Test Comment"' \
--form 'reason_code[1][uuid]="07b310c2-8c63-4b82-9b87-53a4b963adac"' \
--form 'reason_code[1][form_data][0][identifier]="9b466317-5041-42f9-b6d8-084d5d988465"' \
--form 'reason_code[1][form_data][0][value]="Test Product detail"' \
--form 'reason_code[1][form_data][1][identifier]="c9820d99-f515-4e16-93d2-e5032b454286"' \
--form 'reason_code[1][form_data][1][value]=@"/home/work/Pictures/Screenshot from 2022-06-29 17-33-41.png"'
```

<br />

## Response parameters

| Parameter  | Description                                                                                                                                                                |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id         | This parameter contains the  merchant ID.                                                                                                                                  |
| type       | The parameter contains the **chargeback-details ** as type.                                                                                                                |
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