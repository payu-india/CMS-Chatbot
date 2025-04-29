---
title: >-
  Set up WebHook to Receive Cancellation or Modification Update from the Issuer
  Bank
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: >-
    Set up WebHook to Receive Cancellation or Modification Update from the
    Issuer Bank
  description: >-
    Learn how to set up a webhook to receive cancellation or modification
    updates using webhooks from the issuer bank using PayU's API. This
    documentation provides instructions for integrating webhook notifications,
    ensuring you stay informed about mandate changes in real-time
  keywords:
    - Webhook for Mandate Cancellation Update
    - ' Webhook for Mandate Modification Update'
    - ' PayU mandate updates webhook'
    - Webhook notifications for Recurring Payment cancellation
    - ' Webhook notifications for Recurring Payment modification'
    - ' Cancel Recurring Payment Webhook'
    - ' Modify Recurring Payment Webhook'
  robots: index
next:
  description: ''
---
When an action is taken on the mandate for SI by the issuing bank for cards, such as canceling or Modifying the mandate, PayU sends an HTTP payload to the webhook URL ( shared by the merchant) which contains a payload of information that describes the action that was taken. For more information on what is webhooks and the IP address to be whitelisted for the PayU webhooks, refer to [Webhooks](doc:webhooks).

| **API Request Type** | **POST**                           |
| -------------------- | ---------------------------------- |
| Content-Type         | application/json                   |
| URL                  | URL that you have shared with PayU |

## Mandate for Cards

### Payload of Mandate

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "The status of the SI. The status can be any of the following:  \n- active  \n- deleted",
    "0-2": "active",
    "1-0": "authpayuid  \n`mandatory`",
    "1-1": "The value of mihpayid returned in the response of mandate registration transaction once the transaction is successfully completed.",
    "1-2": "6611192557",
    "2-0": "notificationType",
    "2-1": "The action that is taken on the mandate by the bank. The action can be either of the following:  \n**MANDATE_MODIFICATION**: Indicates that the mandate is modified .  \n**MANDATE_CANCELLATION**: Indicates that the mandate is cancelled.  \n**MANDATE_CANCELLATION_TOKEN_DELETION**: Indicates that the mandate token is deleted.",
    "2-2": "MANDATE\\_MODIFICATION",
    "3-0": "si\\_details",
    "3-1": "Contains the following fields about the SI in a JSON format:  \nbillingAmount: Billing amount of the SI transaction.  \npaymentStartDate: Start date of SI  \npaymentEndDate: : End date of SI",
    "3-2": " {  \n“billingAmount”:”10”,  \n“paymentStartDate”:”20-06-2022”,  \n“paymentEndDate”:”30-06-2023”  \n}",
    "4-0": "eventDate",
    "4-1": "Event date of the modification.",
    "4-2": "30-11-2022",
    "5-0": "message",
    "5-1": "Message for the webhook",
    "5-2": "Request Successful",
    "6-0": "hash `mandatory`",
    "6-1": "Unique hash string to validate the authenticity of the Webhook payload. The hash logic is as follows: sha512(status|authpayuId|notificationType|billingAmount|paymentStartDate|paymentEndDate|message|eventDate|key|udf1|udf2|udf3|udf4|udf5|salt)",
    "6-2": ""
  },
  "cols": 3,
  "rows": 7,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


#### Verify the WebHook Payload

The ensure that you are receiving the payload from PayU, you must hash the parameters using the following algorithm and check whether the hash that is sent in the payload matches with it.

```plaintext
sha512(status|authpayuId|notificationType|billingAmount|paymentStartDate|paymentEndDate|message|eventDate|key|udf1|udf2|udf3|udf4|udf5|salt)
```

> 📘 **Note**:
> 
> PayU recommends you to generate the hash at your server for security purposes.

### Sample Payloads

#### Modify SI Mandate

```
{
  "status": “active”,
  "authPayuId": "16538344237",
  "si_details": {
    "billingAmount": 101,
    "paymentStartDate": "2023-01-06",
    "paymentEndDate": "2030-01-03"
  },
  "message": "Mandate modified",
  "eventDate": "2023-01-24",
  "notificationType": "MANDATE_MODIFICATION",
  "key": "Merchant_KEY",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "",
  "hash": "3913bec8ea34394844ffeb94cf59938b659102223bc0f1eae5a1c954cXXXXXXXXXXXX278745aea4b44fcccd12af085f4a24cc7e493849b5b38190ff30f444b87db"
}
```

#### Delete SI Mandate

```
{
  "status": “deleted”,
  "authPayuId": "16538344237",
  "si_details": {
    "billingAmount": 101,
    "paymentStartDate": "2023-01-06",
    "paymentEndDate": "2030-01-03"
  },
  "message": "Mandate Deleted",
  "eventDate": "2023-01-24",
  "notificationType": "MANDATE_DELETION",
  "key": "Merchant_KEY",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "",
  "hash": "3913bec8ea34394844ffeb94cf59938b659102223bc0f1eae5a1c954cXXXXXXXXXXXX278745aea4b44fcccd12af085f4a24cc7e493849b5b38190ff30f444b87db"
}
```

### Webhook for Token Deletion

```
{
  "status": “deleted”,
  "authPayuId": "16538344237",
  "si_details": {
    "billingAmount": 101,
    "paymentStartDate": "2023-01-06",
    "paymentEndDate": "2030-01-03"
  },
  "message": "Mandate Deleted",
  "eventDate": "2023-01-24",
  "notificationType": "MANDATE_CANCELLATION_TOKEN_DELETION",
  "key": "Merchant_Key",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf4": "",
  "udf5": "",
  "hash": "3913bec8ea34394844ffeb94cf59938b659102223bc0f1eae5a1c954cXXXXXXXXXXXX278745aea4b44fcccd12af085f4a24cc7e493849b5b38190ff30f444b87db"
}
```

## Mandate for UPI

Merchant needs to expose a webhook and needs to request Integration team/PayU team. If this webhook is configured, merchant will receive the response object over HTTP form:

> 📘 Notes:
> 
> - This webhook is crucial and it’s mandatory to implement the same to get the latest updates about the consumer actions.
> - The webhook does not support a retry mechanism

Status defines acknowledgement from PayU. Possible values are:

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "status",
    "0-1": "Returns the status of the transactions and can be any of the following:  \n- **active** –Mandate is in active state  \n- **revoked** – Mandate is cancelled  \n- **pause** – Mandate is paused",
    "0-2": "paused",
    "1-0": "authpayuid",
    "1-1": "This parameter returns the consent transaction Id",
    "1-2": "700010006213657",
    "2-0": "action",
    "2-1": "This parameter returns the action of the mandate and can be any of the following:  \n- MANDATE\\_PAUSE: Indicates that the mandate is paused .  \n- MANDATE\\_\\\\UNPAUSE: Indicates that the mandate is unpaused  \n- MANDATE\\_REVOKE: Indicates that the mandate is cancelled.",
    "2-2": " ",
    "3-0": "dateTime",
    "3-1": "This parameter returns the start date of the mandate",
    "3-2": "\"2020-09-16 18:18:21\"",
    "4-0": "amount",
    "4-1": "This parameter returns the amount of the mandate created",
    "4-2": "159.00",
    "5-0": "endDate",
    "5-1": "This parameter returns the last date of the mandate",
    "5-2": "\"2021-09-16 18:18:21\"",
    "6-0": "mandateNumber",
    "6-1": "This parameter returns the unique mandate number (UMN)",
    "6-2": "700010006213657@mybank",
    "7-0": "pauseStartDate",
    "7-1": "This parameter returns from when the pause is started by the customer.",
    "7-2": "",
    "8-0": "pauseEndDate",
    "8-1": "This parameter returns from when the mandate was resumed by the customer.",
    "8-2": "",
    "9-0": "hash",
    "9-1": " Unique hash string to validate the authenticity of the Webhook payload. The hash logic is as follows: `status\\|action\\|authpayuid\\|dateTime\\|amount\\|endDate\\|salt`",
    "9-2": " "
  },
  "cols": 3,
  "rows": 10,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Sample Payload

```
{
  "status": "pause",
  "authpayuid": "700010006213657",
  "action": "MANDATE_PAUSE",
  "key": "485nghu",
  "udf1": "",
  "udf2": "",
  "udf3": "",
  "udf5": "",
  "udf6": "",
  "dateTime": "2020-09-1618: 18: 21",
  "amount": "159.00",
  "endDate": "2022-10-0600: 00: 00",
  "mandateNumber": "700010006213657@mybank",
  "hash": "f94e3af697dc09879997ae0040d03b612abe739f701b5e1a3c4d7b5cecaddc7c446e7bb9fc44a854727e39e63c2059d1ba5d31defaff305a7627c7c4b1907044"
}
```

## Mandate for UPI

> 📘 Note:
> 
> No unpause webhook will be triggered automatically after the mandate gets unpause. These webhooks are subject to the action taken by the customer from their PSP app only (pause, unpause, revoke).

### Mandate Pause webhook

> 📘 Note:
> 
> For every mandate pause, Payu will be able to trigger the mandate unpause webhook, since it is being sent by the ecosystem, post which the Mandate becomes ACTIVE, and further operations can be done for that mandate.

```
{
   "status":"pause",
   "authpayuid":19188766234,
   "action":"MANDATE_PAUSE",
   "dateTime":"2024-02-15 16:41:16",
   "amount":"10.00",
   "endDate":"2025-12-01 00:00:00",
   "mandateNumber":"PTM3b0f23b1a4f1e98b25b7bdf34ad04@paytm",
   "key":"YQeVdc",
   "udf1":"",
   "udf2":"",
   "udf3":"",
   "udf5":"",
   "pauseStartDate":"2024-02-15",
   "pauseEndDate":"2024-02-16",
   "hash":"04fda68800f4004f403c336b7b304c92c59edcc6c99af91d8879e58abf3472091476428c8f733918f6397864ce3c58354385643e2e3af3b3c32f890e8b174b04"
}
```

### Mandate unpause webhook

```
{
   "status":"active",
   "authpayuid":19188766234,
   "action":"MANDATE_UNPAUSE",
   "dateTime":"2024-02-15 16:44:12",
   "amount":"10.00",
   "endDate":"2025-12-01 00:00:00",
   "mandateNumber":"PTM3b0f23b1a4f1e98b25b7bdf34ad04@paytm",
   "key":"YQeVdc",
   "udf1":"",
   "udf2":"",
   "udf3":"",
   "udf5":"",
   "hash":"fa48a38aca086b4bba2ff4dff0eb585c6c6f3d39c7515d54cb272d5abcd6db6564301db3de61f4ab6508338c302c2ce73ebc9bdd628c82833c2765c24f71571c"
}
```

<br>

### Mandate revoke webhook

```
{
   "status":"revoked",
   "authpayuid":19188766234,
   "action":"MANDATE_REVOKE",
   "dateTime":"2024-02-15 16:45:39",
   "amount":"10.00",
   "endDate":"2025-12-01 00:00:00",
   "mandateNumber":"PTM3b0f23b1a4f1e98b25b7bdf34ad04@paytm",
   "key":"YQeVdc",
   "udf1":"",
   "udf2":"",
   "udf3":"",
   "udf5":"",
   "hash":"a1ced2f53714b27827972b2d982bf2ff876b8571ecbbbcac202d2140661ea7d11466a03caac4fa3144185e7f55695d7eaf6b2820cd7a2725d1974858db7edec3"
}
```

<br>