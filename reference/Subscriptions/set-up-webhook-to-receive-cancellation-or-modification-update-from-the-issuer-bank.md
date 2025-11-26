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

## Net Banking or eNACH

### Cancellation Mandate

This webhook implementation for handling PayU payment notifications, specifically for mandate cancellation events. The webhook is integrated to process eNACH (Electronic National Automated Clearing House) payment status updates.

**Endpoint**

| Parameter                     | Description                                                                                                           | Example                                                            |
| :---------------------------- | :-------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------- |
| URL<br />`mandatory`          | `String` - URL configured under the merchant param: notifyMandateRevoke. Contact PayU support to get this configured. | [https://your-domain.com/webhook](https://your-domain.com/webhook) |
| Method<br />`mandatory`       | `String` - HTTP method for the webhook                                                                                | POST                                                               |
| Content-Type<br />`mandatory` | `String` - Content type of the request                                                                                | application/json                                                   |

#### Request Specification

**Content-Type**

```
"Content-Type": "application/json"
```

**Request Body Structure**

```json
{
  "statusCode": 1,
  "notificationType": "MANDATE_CANCELLATION",
  "status": "CANCEL_SUCCESS",
  "authPayuid": "26108200310"
}
```

#### Request Parameters

| Parameter                         | Description                                     | Example              |
| :-------------------------------- | :---------------------------------------------- | :------------------- |
| statusCode<br />`mandatory`       | `Integer` - Numeric status indicator            | 1                    |
| notificationType<br />`mandatory` | `String` - Type of notification event           | MANDATE_CANCELLATION |
| status<br />`mandatory`           | `String` - Current status of the operation      | CANCEL_SUCCESS       |
| authPayuId<br />`mandatory`       | `String` - Unique PayU authorization identifier | 26108200310          |

#### Sample Test Request

```bash
curl -X POST [your_https_url_here]/ \
-H "Content-Type: application/json" \
-d '{
  "statusCode": 1,
  "notificationType": "MANDATE_CANCELLATION",
  "status": "CANCEL_SUCCESS",
  "authPayuId": "[your_mandate_auth_payuid_here]"
}'
```

> 📘 **Note**
>
> Replace `[your_https_url_here]` with your actual webhook URL and `[your_mandate_auth_payuid_here]` with the actual mandate authorization PayU ID.

## Mandate for Cards

### Payload of Mandate

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        status
      </td>

      <td>
        The status of the SI. The status can be any of the following:

        * active
        * deleted
      </td>

      <td>
        active
      </td>
    </tr>

    <tr>
      <td>
        authpayuid  
        `mandatory`
      </td>

      <td>
        The value of mihpayid returned in the response of mandate registration transaction once the transaction is successfully completed.
      </td>

      <td>
        6611192557
      </td>
    </tr>

    <tr>
      <td>
        notificationType
      </td>

      <td>
        The action that is taken on the mandate by the bank. The action can be either of the following:

        * _MANDATE_MODIFICATION_*: Indicates that the mandate is modified .
        * _MANDATE_CANCELLATION_*: Indicates that the mandate is cancelled.
        * _MANDATE_CANCELLATION_TOKEN_DELETION_*: Indicates that the mandate token is deleted.
      </td>

      <td>
        MANDATE_MODIFICATION
      </td>
    </tr>

    <tr>
      <td>
        si_details
      </td>

      <td>
        Contains the following fields about the SI in a JSON format:  
        billingAmount: Billing amount of the SI transaction.  
        paymentStartDate: Start date of SI  
        paymentEndDate: : End date of SI
      </td>

      <td>
         \{  
        “billingAmount”:”10”,  
        “paymentStartDate”:”20-06-2022”,  
        “paymentEndDate”:”30-06-2023”  
        }
      </td>
    </tr>

    <tr>
      <td>
        eventDate
      </td>

      <td>
        Event date of the modification.
      </td>

      <td>
        30-11-2022
      </td>
    </tr>

    <tr>
      <td>
        message
      </td>

      <td>
        Message for the webhook
      </td>

      <td>
        Request Successful
      </td>
    </tr>

    <tr>
      <td>
        hash `mandatory`
      </td>

      <td>
        Unique hash string to validate the authenticity of the Webhook payload. The hash logic is as follows: sha512(status|authpayuId|notificationType|billingAmount|paymentStartDate|paymentEndDate|message|eventDate|key|udf1|udf2|udf3|udf4|udf5|salt)
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

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
> * This webhook is crucial and it’s mandatory to implement the same to get the latest updates about the consumer actions.
> * The webhook does not support a retry mechanism

Status defines acknowledgement from PayU. Possible values are:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        status
      </td>

      <td>
        Returns the status of the transactions and can be any of the following:

        * **active** –Mandate is in active state
        * **revoked** – Mandate is cancelled
        * **pause** – Mandate is paused
      </td>

      <td>
        paused
      </td>
    </tr>

    <tr>
      <td>
        authpayuid
      </td>

      <td>
        This parameter returns the consent transaction Id
      </td>

      <td>
        700010006213657
      </td>
    </tr>

    <tr>
      <td>
        action
      </td>

      <td>
        This parameter returns the action of the mandate and can be any of the following:

        * MANDATE_PAUSE: Indicates that the mandate is paused .
        * MANDATE_\UNPAUSE: Indicates that the mandate is unpaused
        * MANDATE_REVOKE: Indicates that the mandate is cancelled.
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        dateTime
      </td>

      <td>
        This parameter returns the start date of the mandate
      </td>

      <td>
        "2020-09-16 18:18:21"
      </td>
    </tr>

    <tr>
      <td>
        amount
      </td>

      <td>
        This parameter returns the amount of the mandate created
      </td>

      <td>
        159.00
      </td>
    </tr>

    <tr>
      <td>
        endDate
      </td>

      <td>
        This parameter returns the last date of the mandate
      </td>

      <td>
        "2021-09-16 18:18:21"
      </td>
    </tr>

    <tr>
      <td>
        mandateNumber
      </td>

      <td>
        This parameter returns the unique mandate number (UMN)
      </td>

      <td>
        700010006213657@mybank
      </td>
    </tr>

    <tr>
      <td>
        pauseStartDate
      </td>

      <td>
        This parameter returns from when the pause is started by the customer.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        pauseEndDate
      </td>

      <td>
        This parameter returns from when the mandate was resumed by the customer.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        hash
      </td>

      <td>
         Unique hash string to validate the authenticity of the Webhook payload. The hash logic is as follows: `status|action|authpayuid|dateTime|amount|endDate|salt`
      </td>

      <td>
         
      </td>
    </tr>
  </tbody>
</Table>

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

<br />

### Mandate Pause webhook

> 📘 Notes:
>
> * For every mandate pause, Payu will be able to trigger the mandate unpause webhook, since it is being sent by the ecosystem, post which the Mandate becomes ACTIVE, and further operations can be done for that mandate.
> * No unpause webhook will be triggered automatically after the mandate gets unpause. These webhooks are subject to the action taken by the customer from their PSP app only (pause, unpause, revoke).

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

<br />

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

<br />
