---
title: StoreCard Webhook Events and Sample Payloads [Internal Review]
excerpt: List of webhook events along with sample payloads.
deprecated: false
hidden: true
metadata:
  description: >-
    Configure PayU Dashboard webhooks to receive payment, refund, and dispute
    notifications. Create, update, and monitor webhook events with sample
    payloads for merchant integrations. Covers Webhook Events and Sample
    Payloads.
  keywords:
    - payu dashboard webhooks setup guide
    - configure payment webhooks payu merchant dashboard
    - payu webhook events sample payloads
    - payu dashboard create update webhook
    - payment notification webhook payu dashboard
    - payu webhook logs dashboard guide
    - merchant webhook integration payu dashboard
    - payu dashboard webhook refund dispute events
    - payment gateway webhooks payu vs razorpay cashfree
    - payu dashboard webhook configuration india
  robots: index
---
You can accept customer payments using PayU products. By subscribing to payments webhook events you can get notified about payment state changes. Know more about <Anchor target="_blank" href="https://docs.payu.in/docs/manage-webhooks-using-dashboard">managing webhooks using the dashboard</Anchor>.

## List of Webhook Events

The table below lists the available webhook events.

| **Event Name**            | **Description**                                               | Merchant Action                      |
| :------------------------ | :------------------------------------------------------------ | ------------------------------------ |
| `ACTIVE`                  | Determines that a card token is active.                       | Token activation                     |
| `DELETED`                 | Triggered when a card token is deleted.                       | Token deleted by a User              |
| `SUSPENDED`               | Triggered when a card token is suspended.                     | Token suspended by a user or network |
| `Redigitization Complete` | Triggered when a re-digitization of a card token is complete. | Token expiry extended  by network    |
| `UPDATED`                 | Triggered when a card token is updated.                       | Token updation request by a user.    |

***

## Sample Payloads

The following are the sample payloads for webhook events.

### Card Token Is Active

```json
{
   "merchantId": 2,
   "cardToken": "26b4ce096d1",
   "tokenProvisioningStatus": "ACTIVE",
   "userCredential": "smsplus:test",
   "notificationType": "CARD_LIFE_CYCLE_DELETE",
   "issuerToken": null,
   "networkToken": {
     "token_value": "123456787191",
     "token_exp_mon": "02",
     "token_exp_yr": "2028",
     "error_code": null,
     "error_desc": null,
     "tokenRefId": "b5a1de1d1d5240b"
   },
   "additionalInfo": {
     "par": "V00100139"
   },
   "tokenReferenceId": "b5a1de1d1d5240b",
   "clientReferenceId": null
 }
```

***

### Card Token Is Deleted

```json
{
   "merchantId": 2,
   "cardToken": "26b4ce096d1",
   "tokenProvisioningStatus": "DELETED",
   "userCredential": "smsplus:test",
   "notificationType": "CARD_LIFE_CYCLE_DELETE",
   "issuerToken": null,
   "networkToken": {
     "token_value": "123456787191",
     "token_exp_mon": "02",
     "token_exp_yr": "2028",
     "error_code": null,
     "error_desc": null,
     "tokenRefId": "b5a1de1d1d5240b"
   },
   "additionalInfo": {
     "par": "V00100139"
   },
   "tokenReferenceId": "b5a1de1d1d5240b",
   "clientReferenceId": null
 }
```

***

### Re-degitization of a Card Token Is Complete

```json
{
   "merchantId": 2,
   "cardToken": "26b4ce096d1",
   "tokenProvisioningStatus": "Redigitization Complete",
   "userCredential": "smsplus:test",
   "notificationType": "CARD_LIFE_CYCLE_DELETE",
   "issuerToken": null,
   "networkToken": {
     "token_value": "123456787191",
     "token_exp_mon": "02",
     "token_exp_yr": "2028",
     "error_code": null,
     "error_desc": null,
     "tokenRefId": "b5a1de1d1d5240b"
   },
   "additionalInfo": {
     "par": "V00100139"
   },
   "tokenReferenceId": "b5a1de1d1d5240b",
   "clientReferenceId": null
 }
```

***

### Card Token Is Suspended

```json
{
   "merchantId": 2,
   "cardToken": "26b4f701ce096d1",
   "tokenProvisioningStatus": "SUSPENDED",
   "userCredential": "smsplus:test",
   "notificationType": "CARD_LIFE_CYCLE_DELETE",
   "issuerToken": null,
   "networkToken": {
     "token_value": "123456787191",
     "token_exp_mon": "02",
     "token_exp_yr": "2028",
     "error_code": null,
     "error_desc": null,
     "tokenRefId": "b5a1de1d1d5240b"
   },
   "additionalInfo": {
     "par": "V00100139"
   },
   "tokenReferenceId": "b5a1de1d1d5240b",
   "clientReferenceId": null
 }
```

***

### Card Token Is Updated

```json
{
   "merchantId": 2,
   "cardToken": "26b4f701ce096d1",
   "tokenProvisioningStatus": "UPDATED",
   "userCredential": "smsplus:test",
   "notificationType": "CARD_LIFE_CYCLE_DELETE",
   "issuerToken": null,
   "networkToken": {
     "token_value": "123456787191",
     "token_exp_mon": "02",
     "token_exp_yr": "2028",
     "error_code": null,
     "error_desc": null,
     "tokenRefId": "b5a1de1d1d5240b"
   },
   "additionalInfo": {
     "par": "V00100139"
   },
   "tokenReferenceId": "b5a1de1d1d5240b",
   "clientReferenceId": null
 }
```
