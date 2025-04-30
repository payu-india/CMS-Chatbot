---
title: Payouts Webhooks
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Payouts Webhooks
  description: >-
    Learn how to set up and use PayU Payouts Webhooks to receive real-time
    notifications for your transactions. Our detailed guide covers webhook
    configuration, integration, and security measures to automate and streamline
    your payout processes effectively with PayU.
  keywords:
    - payouts webhooks
    - Webhooks integration for Payouts
    - Payouts webhook notifications
    - Automate payouts notifications
    - PayU API webhooks
    - Real-time payouts updates PayU
    - Payouts event notifications
    - Webhooks for payouts PayU
    - PayU payouts API callbacks
    - PayU automated payment alerts
  robots: index
next:
  description: ''
---
Webhook is the http call-back or a way to be notified about the status of an event. These webhooks are maintained at third party users who don’t always hold any connection with the originator of the event.

- **Individual Webhook**: You can set an individual webhook to listen to a particular event. 
- **Default Webhook**: PayU offers a solution for setting up a default webhook to listen events for which individual webhook has not been set.

**Example**:

If you want to listen to Payouts transfer success event, You need to create an _HTTP_ POST API at the merchant’s server end. If you have IP whitelisting enabled at your end, do not forget to whitelist PayU IP address so PayU can access your webhook URL. 

## PayU IP addresses for webhooks

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"></th>
  <th style="border: 1px solid #ddd; padding: 8px;"></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><h3>PayU Production IP Addresses</h3></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Existing IP’s</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>180.179.168.225</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>New IP’s</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>180.179.168.225<br>13.71.57.148<br>52.140.8.68<br>180.179.174.1</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><h3>PayU Test IP Address</h3></td>
  <td style="border: 1px solid #ddd; padding: 8px;"></td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Existing IPs</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>180.179.165.250<br>13.71.57.148</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>New IP</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>13.235.110.253</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>


> 📘 Note:
> 
> If you are facing issues with setting up webhooks, contact PayU Support.

## How webhooks works?

When an event is initiated at PayU’s end, a webhook (that is, an API maintained at your end) is called to check and notify you about the status of the event. You can either create a separate webhook for each event or choose to listen to all events using a default webhook.

## Types of events

You can create webhooks for following events so that you can obtain the callback from PayU. For more information on how to configure webhoooks using **Set Webhook API**, refer to [Set Webhook API](https://devguide.payu.in/payouts-api/set-webhook-api/).

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/07/webhook_events.png)

## Things you should know

- If you do not set any webhooks, that is, neither individual nor default webhook then you will not get any events.
- If you set only the default webhook then you will get all the events on the default webhook.
- If you set a few webhooks along with the default webhook, you will get individual events to the set webhooks and default webhook will be called for the events that have not been set by you. 

For example, If you have set the default webhooks, transfer success and transfer failed webhooks only, the transfer success/failed events will be pushed to the set webhooks corresponding to transfer success/failure . The remaining events such as deposit, low balance will be sent to the default webhooks.

- If you set the certain webhooks but not the default webhook, you will receive the events on individual webhooks. Unset events will not be pushed as default webhook is not known to us.

## Webhooks events

There are various events for which you can configure webhooks. You can either create Individual Webhook URLs for each event or listen to them using the Default Webhook.

Following table describes such events:

| Webhook Event                      | Notifies that the…                                                    |
| ---------------------------------- | --------------------------------------------------------------------- |
| **deposit\_\_success**             | Amount is successfully deposited/credited in the account              |
| **transfer_success  **             | Transfer is completed successfully                                    |
| **transfer_failed **               | Failure is observed while completing the Transfer                     |
| **transfer_reversed **             | Transfer is reversed by the beneficiary bank                          |
| **smart_send_detail_submitted **   | Customer has filled in the details and submitted successfully         |
| **request_processing_failed **     | Failure is observed while raising a transaction request               |
| **low_balance_alert  **            | Payouts account is on low balance                                     |
| **downtime_notification**          | Bank has scheduled downtime                                           |
| **bulk_smart_send_file_processed** | Smart send file upload is processed                                   |
| **transfer_success**               | Signal that a Penny with name match verification has been successful. |
| **smart_send_expired**             | Triggered to notify about the Smart Send link expiration.             |
| **smart_send_cancelled**           | Triggered to notify about the Smart Send link cancellation.           |
| **smart_send_rejected**            | Triggered to notify about the Smart Send link rejection.              |

## Types of Webhooks

Webhooks are of various types and each webhook has a distinct body. 

|                  |                  |
| ---------------- | ---------------- |
| **Method**       | Post             |
| **Content-Type** | application/json |

> 📘 Note: Webhook retry
> 
> On trigger of webhooks, merchants are expected to return http status code 200 within 10 seconds window. If any other response codes received or the request times out, it is considered as failure. On failure, the webhook is re-tried maximum 2 more times with same protocol.

### Low balance webHook

WebHook event is generated when the merchant account has a low balance. The event signals to deposit money in the merchant virtual account so that upcoming transfer requests can be quickly processed

#### Sample payload

```plaintext
{
  "event": "LOW_BALANCE_ALERT","msg": "Low Balance",
  "currentBalance": "4806229.19",
  "alertTime": "28 September 2023 05:41 PM",
  "authorization": "",
  "payoutMerchantId": "1117587"
}
```

### Deposit webhook

WebHook event is generated to signal that a deposit has been successfully processed in the merchant virtual account. The money in the account can be used to do payouts to various beneficiary accounts.

#### Sample payload

```plaintext
{
  "event": "DEPOSIT_SUCCESS",
  "msg": "Deposited",
  "transferId": "AXISCN0123456275",
  "referenceId": "573951",
  "amount": 740311.67,
  "authorization": "",
  "payoutMerchantId": "1117587"
}
```

### Request processing failed webhook

WebHook event is generated to signal that a transfer request has failed processing.

#### Sample payload

```plaintext
{
"event" : "REQUEST_PROCESSING_FAILED",
"msg" : "",
"payuRefId" : "3212312ds",
"merchantReferenceId" : "3212312ds"
}
```

### Transfer success webhook

WebHook event is generated to signal that a transfer has been successful.

#### Sample Payload

```plaintext
{
  "event": "TRANSFER_SUCCESS",
  "msg": "Success",
  "payuRefId": "16958123456787V",
  "merchantReferenceId": "991014001234592537",
  "bankReferenceId": "327012345470",
  "authorization": "",
  "payoutMerchantId": "1117587"
}
```

### Transfer failed webhook

WebHook event is generated to signal that a transfer has failed.

#### Sample Payload

```plaintext
{
  "event": "TRANSFER_FAILED",
  "msg": "Transfer failed due to technical decline. Please reinitiate the transaction",
  "payuRefId": "1691234569025s3",
  "merchantReferenceId": "116911131",
  "authorization": "",
  "payoutMerchantId": "1117587"
}
```

### Transfer reversed webhook

Webhook event is generated to signal that a transfer was successful but reversed after few days due to different reasons.

#### Sample Payload

```plaintext
{
  "event": "TRANSFER_REVERSED",
  "msg": "Transaction Successful",
  "payuRefId": "1667388287123QJ",
  "merchantReferenceId": "26387449",
  "bankReferenceId": "231234542261",
  "authorization": "",
  "payoutMerchantId": "1117587"
}
```

### Smart send detail submitted Webhook

WebHook event is generated to signal that a beneficiary has added their account details on the smart send link.

#### Sample payload

```plaintext

{
"event" : " SMART_SEND_DETAIL_SUBMITTED",
"msg" : "Detail filled",
"linkId" : "3212312ds",
"merchantReferenceId" : "3212312ds",
"merchantMiscId" : "3212312ds"
}
```

### Bulk smart send file processed webhook

Webhook event generated when file uploaded for smart send is successfully processed.

#### Sample payload

```plaintext
Webhook details
{
  "event": "BULK_SMART_SEND_FILE_PROCESSED",
  "msg": "File processed",
  "fileId": 136,
  "totalRows": 1001,
  "successfulRows": 1000,
  "failedRows": 1,
  "status": "COMPLETED",
  "authorization": "",
  "payoutMerchantId": "1111157"
}
```

### Transfer success webhook – Penny with name match

WebHook event is generated to signal that a Penny with name match verification has been successful.

#### Sample payload

```plaintext
{
   "event": "TRANSFER_SUCCESS",
   "msg": "Success",
   "payuRefId": "PAYOUT1686459872847Ahx610a8fKn",
   "merchantReferenceId": "4Y5MGYUGCXV8NLKJMIXC55XZXHR705",
   "bankReferenceId": "PAYOUT1686459872847Ahx610a8fKn",
   "nameMatch": 85,
   "nameWithBank": "CC",
   "authorization": "",
   "payoutMerchantId": "1111157"
}
```

### Transfer success webhook – Penny deposit

WebHook event is generated to signal that a Penny verification has been successful.

#### Sample payload

```plaintext
{
   "event": "TRANSFER_SUCCESS",
   "msg": "Success",
   "payuRefId": "PAYOUT1686459872847Ahx610a8fKn",
   "merchantReferenceId": "4Y5MGYUGCXV8NLKJMIXC55XZXHR705",
   "bankReferenceId": "PAYOUT1686459872847Ahx610a8fKn",
   "nameWithBank": "CC",
   "authorization": "",
   "payoutMerchantId": "1111157"
}
```

### Smart Send Expired Webhook

When the Smart Send link status changes to expired, a webhook will be triggered to notify the merchant about the Smart Send link expiration.

#### Sample Payload

```
{  
"event": "SMART_SEND_EXPIRED",  
  "msg": "Smart send link expired, create a new link.",  
  "expireOn": "2023-10-01 16: 45: 30",  
  "merchantReferenceId": "26383437449",  
  "authorization": "",  
  "payoutMerchantId": "1117587"  
  }
```

### Smart Send Cancelled Webhook

When the Smart Send link status changes to cancelled, a webhook will be triggered to notify the merchant about the Smart Send link cancellation.

#### Sample Payload

  

```
{  
  "event": "SMART_SEND_CANCELLED",  
  "msg": "Smart Send Link cancelled by the merchant, create a new link.",  
  "expireOn": "2023-10-01 16: 45: 30",  
  "merchantReferenceId": "26383437449",  
  "authorization": "",  
  "payoutMerchantId": "1117587"  
  }
```

### Smart Send Rejected Webhook

When the Smart Send link status changes to rejected, a webhook will be triggered to notify the merchant about the Smart Send link rejection.

#### Sample Payload

```
  {  
   "event": "SMART_SEND_REJECTED",  
  "msg": "Smart Send approval rejected, check with the approver.",  
  "expireOn": "2023-10-01 16: 45: 30",  
  "merchantReferenceId": "26383437449",  
  "authorization": "",  
  "payoutMerchantId": "1117587"  
  }
```