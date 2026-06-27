---
excerpt: ''
api:
  file: paritalgeneral-apis-13.json
  operationId: SmartSendDetailsAPI
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API for fetching the details of a particular Smart Send using payoutMerchantId and merchantRefId.

**Environment**

|                            |                                                                                                                                     |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Test Environment**       | \<[https://uatoneapi.payu.in/payout/merchant/smartSend/details](https://uatoneapi.payu.in/payout/merchant/smartSend/details)>       |
| **Production Environment** | \<[https://payout.payumoney.com/payout/merchant/smartSend/details](https://payout.payumoney.com/payout/merchant/smartSend/details)> |

<details>
  <summary>Sample request</summary>

```
curl --location 'https://payout.payumoney.com/payout/merchant/smartSend/details?payoutMerchantId=2212618&merchantRefId=abcde' \
--header 'accept: application/json, text/plain, */*' \
--header 'content-type: application/json' \
--header 'authorization: Bearer 89fec7522b42cfe5387672a4eb9c8f568bf1da59304c3ee54bcf77db7ef23e22'
```

</details>

<details>
  <summary>Response parameter description</summary>

| Key                  | Description                                                                                                                                                                                                                                         | Data Type        | Possible Values                       |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------- |
| merchantRefId        | Unique reference Id used while creating smart send                                                                                                                                                                                                  | String           | "abcde"                               |
| payoutMerchantId     | Specify the payout merchant id provided while onboarding or creating Payout account.                                                                                                                                                                | Long             | 2212618                               |
| smartSendStatus      | Current status of Smart send. For the list of status, refer to [Smart Send Status Descriptions](#smart-send-status-descriptions)                                                                                                                    | String           | "EXPIRED"                             |
| addedOn              | Creation time of Smart send                                                                                                                                                                                                                         | Timestamp in UTC | "2023-11-06T20:16:39.000+0000"        |
| expiryDate           | Expiry Time of Smart Send                                                                                                                                                                                                                           | Timestamp in UTC | "2023-11-09T00:00:00.000+0000"        |
| description          | Purpose of smart send                                                                                                                                                                                                                               | String           | "Test"                                |
| amount               | Amount of Smart send                                                                                                                                                                                                                                | Double           | 10.0                                  |
| updatedOn            | Last updated timestamp of smart send                                                                                                                                                                                                                | Timestamp in UTC | "2023-11-09T00:00:03.000+0000"        |
| transferType         | Smart Send Payout mode basis beneficiary's choice of receiving funds into Account or VPA                                                                                                                                                            | String           | "UPI" , "IMPS" etc.                   |
| bankTransactionRefNo | Contains the bank transfer reference number                                                                                                                                                                                                         | String           | "U8712301293"                         |
| payuTransactionRefNo | Contains the PayU transaction reference number.                                                                                                                                                                                                     | String           | "PAYOUT1702966295695uQNG9eyN84z"      |
| txnStatus            | Contains the transaction status for this transaction. For list of transaction status, refer to [Transaction Status](https://devguide.payu.in/payouts-api/payouts-initiation-and-tracking/check-transfer-status-api/#Transaction_Status) sub-section | String           | "SUCCESS"                             |
| txnSubStatus         | Contains the sub-status of the transaction                                                                                                                                                                                                          | String           |                                       |
| lastStatusUpdateDate | Last updated on transaction                                                                                                                                                                                                                         | Timestamp in UTC | "2023-11-09T00:00:00.000+0000"        |
| custName             | Indicates the Beneficiary name to which the link is to be sent                                                                                                                                                                                      | String           | "ABC"                                 |
| custEmail            | Indicates the email address of the beneficiary                                                                                                                                                                                                      | String           | [xyz@email.com](mailto:xyz@email.com) |
| custMobile           | Indicates the mobile number of the beneficiary                                                                                                                                                                                                      | String           | 9999999999                            |
| msg                  | Contains the response message for transaction                                                                                                                                                                                                       | String           |                                       |
| link                 | Contains the Smart pay link                                                                                                                                                                                                                         | String           |                                       |
| succeedOn            | Timestamp when Transaction got succeeded                                                                                                                                                                                                            | Timestamp in UTC | "2023-11-09T00:00:01.000+0000"        |
| txnSource            | Contains source of transcation                                                                                                                                                                                                                      | String           | "API"                                 |

### Smart Send Status Descriptions

| Status            | Description                                                                    |
| ----------------- | ------------------------------------------------------------------------------ |
| PENDING           | Smart Send Link Created Successfully but yet to be filled details by customer. |
| INITIATED         | Payment Initiated, wait for sometime for payment to be competed.               |
| FAILED            | Smart Send Payment failed, Can be reinitiated after sometime.                  |
| SUCCESS           | Payout is initiated, wait for sometime for the payout to be completed.         |
| REJECTED          | Smart Send approval rejected, check with the approver.                         |
| EXPIRED           | Smart send link expired, create a new link.                                    |
| CANCELLED         | Smart Send Link cancelled by the merchant, create a new link.                  |
| APPROVAL\_PENDING | Link Approval is pending, contact your approver.                               |
| APPROVED          | Link is approved by the approver.                                              |

</details>

<details>
  <summary>Sample response</summary>

**Success Scenario**

```
{
    "status": 0,
    "msg": null,
    "code": null,
    "data": {
        "merchantRefId": "abcde",
        "payoutMerchantId": 2212618,
        "smartSendStatus": "SUCCESS",
        "addedOn": "2023-12-19T06:10:37.000+0000",
        "expiryDate": "2023-12-25T06:10:45.000+0000",
        "description": "Cashback",
        "linkId": "61362222-a29a-4191-8157-88a87a9d30d1",
        "amount": 25.0,
        "bankTransactionRefNo": "PAYOUT1702966295695uQNG9eyN84z",
        "payuTransactionRefNo": "PAYOUT1702966295695uQNG9eyN84z",
        "txnStatus": "SUCCESS",
        "txnSubStatus": null,
        "lastStatusUpdateDate": "2023-12-19T07:55:02.000+0000",
        "transferType": "IMPS",
        "custName": "sara",
        "custEmail": null,
        "custMobile": "9888883254",
        "msg": "Success",
        "link": "https://test.payumoney.com/url/OIuMXJR5ZL6d",
        "succeedOn": "2023-12-19T07:55:02.000+0000",
        "txnSource": "SMART_SEND"
    }
}
```

**Failure scenario**

- No record found:The Smart Send Details cannot be fetched and to considered as unidentified or Pending by merchant.

```
{
    "status": 1,
    "msg": "Smart Send Record not found with merchant reference id - xyz. for Payout Merchant Id - 2212618. Kindly fetch details after some time.",
    "code": null,
    "data": {
        "merchantRefId": "12",
        "payoutMerchantId": 1117371,
        "smartSendStatus": null,
        "addedOn": null,
        "expiryDate": null,
        "description": null,
        "linkId": null,
        "amount": null,
        "bankTransactionRefNo": null,
        "payuTransactionRefNo": null,
        "txnStatus": null,
        "txnSubStatus": null,
        "lastStatusUpdateDate": null,
        "transferType": null,
        "custName": null,
        "custEmail": null,
        "custMobile": null,
        "msg": null,
        "link": null,
        "succeedOn": null,
        "txnSource": null
    }
}
```

</details>

## Request header and parameters

<Callout icon="📘" theme="info">
  ### Note:

  The **pid** is **payoutMerchantId**, however it is different from the PayU merchant id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your **payoutsMerchantID**.
</Callout>

<br />
