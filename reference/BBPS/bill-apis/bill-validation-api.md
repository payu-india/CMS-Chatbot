---
title: Bill Validation API
excerpt: ''
api:
  file: bbps-apis-agent-share-7.json
  operationId: BillValidationAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API can be used by all the BBPS and Connect billers who support the following validation options:  

- Optional
- Mandatory

<BBPSEnvironment />

> 📘 Note:
> 
> Send the scope of the Get Token API as **create_transactions** to obtain the access_token for this request. For more information, refer to  [Get Token API - BBPS](ref:get-token-api-bbps).

<details><summary>Sample request</summary>

```
curl --location -g --request POST 'https://<hostName>/payu-nbc/v2/nbc/paymentValidation?agentId={agentId}&billerId={billerId}&customerName={customerName}'&customerParams={ "<param1>": <value1>", "<param2>": "<value2>" }&customer&PhoneNumber={contact number}&deviceDetails={ "INITIATING_CHANNEL": "INT", "IP": "<ip>","MAC": "<mac>" }&"customerPhoneNumber": "<contact number>&deviceDetails={ "INITIATING_CHANNEL": "INT","IP": "<ip>", "MAC": "<mac>" } 
 \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{access_token}}' 
```

</details>

<details><summary>Sample response</summary>

### Success scenario

```
{  
  "code": 200, 
  "status": "SUCCESS", 
  "payload": { 
    "refId": "<reference ID>", 
    "timeStamp": "<yyyy-MM-dd hh:mm:ss>", 
    "amount": "<amount to be paid>" 
  } 
} 
```

### Failure scenario

```
{ 
  "code": 600, 
  "status": "FAILURE", 
  "payload": { 
    "errors": [ 
      { 
        "reason": "<error Message>", 
        "errorCode": "<Error Code>" 
      } 
    ], 
    "refId": <Reference Id>, 
    "type": "payment_validation ", 
    "message": "payment_validation_request_failed ", 
    "additionalParams": null 
  } 
} 

```

</details>

## Request Parameters