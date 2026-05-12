---
api:
  file: updated_s2s_classic_flow.json
  operationId: ClassicIntegration-S2S
hidden: false
link:
  new_tab: false
---
You can collect card payments using Server-to-Server integration. This section provides the request and response parameters used in Step 1 of  [Classic Integration for Cards](doc:integrate-with-s2s-for-cards-classic-integration). You can get the sample request and response when use the "Try It" experience. For the complete integration steps, refer to [Classic Integration for Cards](doc:integrate-with-s2s-for-cards-classic-integration).

<Cards_PayU_Labs />

<br />

## Postman Collection

<Postman_collection />

<Callout icon="📘" theme="info">
  **Reference:** For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Callout>

<Accordion_Collect_Fraud_Detection />

**Environment**

|                            |                                                                    |
| :------------------------- | :----------------------------------------------------------------- |
| **Test Environment**       | [https://test.payu.in/_payment](https://test.payu.in/_payment)     |
| **Production Environment** | [https://secure.payu.in/_payment](https://secure.payu.in/_payment) |

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location --request POST 'https://secure.payu.in/_payment' --header 'Content-Type: application/x-www-form-urlencoded' --header 'Cookie: PHPSESSID=mj185cifujktpv1igu9tmuoaal; PAYUID=eac5648ac59712238883a78e71f35717; PHPSESSID=638b1b5173542' --data-urlencode 'hash=d89e7d88863617baf01e504c50aa58e94d6ff3371c2ed409ca1f139cfee75d67e85ce7e91c4224790b6cc1b59bb149fc98b0272e27b335225a9d288a34290e42' --data-urlencode 'key=s*****s' --data-urlencode 'txnid=payuTestTransaction3818940' --data-urlencode 'amount=1.0' --data-urlencode 'firstname=Ashish' --data-urlencode 'email=test@payu.in' --data-urlencode 'phone=9988776655' --data-urlencode 'productinfo=Product Info' --data-urlencode 'surl=https://admin.payu.in/test_response' --data-urlencode 'furl=https://admin.payu.in/test_response' --data-urlencode 'notifyurl=https://admin.payu.in/test_response' --data-urlencode 'codurl=https://admin.payu.in/test_response' --data-urlencode 'ipurl=https://admin.payu.in/test_response' --data-urlencode 'lastname=' --data-urlencode 'udf1=' --data-urlencode 'udf2=' --data-urlencode 'udf3=' --data-urlencode 'udf4=' --data-urlencode 'udf5=' --data-urlencode 'pg=CC' --data-urlencode 'bankcode=DC' --data-urlencode 'ccnum=XXXXXXXXXXX8811' --data-urlencode 'ccname=Ashish' --data-urlencode 'ccvv=XXX' --data-urlencode 'ccexpmon=12' --data-urlencode 'ccexpyr=2023' --data-urlencode 'txn_s2s_flow=4' --data-urlencode 'authentication_flow=REDIRECT' 
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ```json
  {
     "metaData":{
        "message":null,
        "referenceId":"a74a67e965537b0f817e925e45321194",
        "statusCode":null,
        "txnId":"payuTestTransaction3818940",
        "txnStatus":"Enrolled",
        "unmappedStatus":"pending"
     },
     "result":{
        "otpPostUrl":"",
        "acsTemplate":"PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vYWNzLmZzc25ldC5jby5pbi9hY3NhdXRoc2VydmVyL1VCSS9WL3BhcmVxLmh0bSIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJQYVJlcSIgdmFsdWU9ImVKeFVVdUZ1c2pBVWZSWGpBOUNXaWdaemJjTEViR1JEaVp2NWZuZHdveVFDV3NwRW4zNnRnTzRqSWJubjlIQTRQUzE4SFJSaStJbHBvMUJBakhVdDl6aktzOFdZY3NyWnpQVTVHd3RJZ2kyZUJmeWdxdk9xRk15aGpndGtnT1k3bFI1a3FRWEk5UHdTcmNXRVRiazdCZEpES0ZCRm9lQitzcVBkWTh3NWtJNkdVaFlvRW5uZGpWNGJ0WmRWQ2VST1FWbzFwVlpYd1Qzak5RQm8xRkVjdEQ3TkNibGNMbzdHV2hkOUFDZXRDZ0xFK29BOFV5V05uV3JqMk9hWmlKYkIvdkdHd1MwTzQzWjlpN3o0dGxvQXNRcklwRWJoVXRkbEx1VWo2czhuc3ptblFPNDh5TUpHRWR2YVlRNHpiSS9oWkg4VGRJRFpoYjhFbUlvVmx1bXdtd0VCdHFlcVJLTXdqVDVtSU0vTXl6ZmJhNnBOVlZQNTdudmZiWVBOZXZZdnE0cGp2ZHA4S085cnRiSFJlNUYxekUxUkxtZWRwUVZBckEzcEQ5SjBjejlwTS8xM0EzNEJBQUQvL3dYQWdRQUFBQUFBa1A5ckFHTkhyZkk9Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJUZXJtVXJsIiB2YWx1ZT0iaHR0cHM6Ly9zZWN1cmUucGF5dS5pbi83OGIxN2YyZWJkYmUyNjgwNjMzNDY3NzA0MjAzMzgyYS9Db21tb25QZ1Jlc3BvbnNlSGFuZGxlci5waHAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9Ik1EIiB2YWx1ZT0iMDMwMzE3MzA1NSI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1sncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+"
     },
     "binData":{
        "pureS2SSupported":false,
        "issuingBank":"UBI",
        "category":"debitcard",
        "cardType":"VISA",
        "isDomestic":true
     }
  }
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  | **Parameter**            | **Description**                                                                                                                                                                                                                                                                             |
  | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | metaData                 | `JSON` It is a JSON object containing more information about the response.                                                                                                                                                                                                                  |
  | metaData.referenceId     | `String` This is the PayU reference ID which we will be sending to merchant so that they can send us this back in second call.                                                                                                                                                              |
  | binData                  | `JSON` This is a JSON object containing information about card number or token number.                                                                                                                                                                                                      |
  | binData.pureS2SSupported | `Boolean` The value for this parameter will be returned **false** for REDIRECT.                                                                                                                                                                                                             |
  | result                   | `JSON` This is a JSON object containing response of the request and to be used in subsequent steps.                                                                                                                                                                                         |
  | result.otpPostUrl        | `String` The parameter will have null value in case of REDIRECT.                                                                                                                                                                                                                            |
  | result.acsTemplate       | `String` acsTemplate is a **base64 encoded** string. The merchant needs to decode acsTemplate, which is an HTML format with auto submit, which then needs to be shown on the customer's browser. The HTML being auto submit, it will take the customer to the bank page for authentication. |

  For the response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Accordion>

## Request parameters

> 🚧 Error Handling:
>
> A list of error message with corresponding error code and reason for the error is listed in . PayU recommends you to handle these errors when you process the transactions. For more information, refer to [Error Codes](ref:error-codes)

<Accordion title="Values to be used in Test environment" icon="fa-flask">
  For values to be used in Test environment, refer to <a href="test-cards-upi-id-and-wallets#web-checkout" target="_blank">Test Cards</a>.
</Accordion>
