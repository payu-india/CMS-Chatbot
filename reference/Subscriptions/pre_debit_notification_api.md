---
title: Predebit Notification API
api:
  file: pre-debit-notification.json
  operationId: predebit
hidden: false
link:
  new_tab: false
metadata:
  title: Predebit Notification API
  description: >-
    Learn how to set up the Pre Debit Notification API using PayU Hosted
    Checkout. This API documentation provides detailed instructions for
    integrating PayU's pre debit notification feature, enabling timely alerts
    and notifications for upcoming transactions.
  keywords:
    - PayU Pre Debit Notification API
    - Pre Debit Notification API
    - PayU pre-debit transaction notification API
    - PayU pre debit alerts API
    - Send Notification Before SI
    - SI Notification
---
The **Pre-Debit Notification** API allows the merchants to send a pre-debit notification to the customer regarding an upcoming payment which will be deducted from the customer’s account as part of the registration. There is a mandate to send this notification to the customer at least 48 hours before the actual debit, that is, 48 hours before calling the Recurring API.

<KeyHashForGeneralParametersDescription />

<br />

> ❗️ Reminder
>
> * Check the mandate status before calling the **Pre-Debit Notification** API.
> * Unless the Pre-Debit notification API is implemented, the **Recurring Payment Transaction** API will not work, and you will not be able to charge the customer for the given billing cycle.
> * Pre-Debit notification is necessary only for Cards and UPI and works for only these two payment modes

### Environment

|                        |                                                                      |
| :--------------------- | :------------------------------------------------------------------- |
| Production Environment | \<[https://info.payu.in/merchant/>](https://info.payu.in/merchant/>) |
| Test Environment       | \<[https://test.payu.in/merchant/>](https://test.payu.in/merchant/>) |

<Accordion title="Sample request" icon="fa-upload">
  #### Cards

  ```curl
  curl --location 'https://info.payu.in/merchant/postservice.php' \
  --header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642' \
  --form 'form="2"' \
  --form 'key="BmTY3G"' \
  --form 'command="pre_debit_SI"' \
  --form 'hash="775f7fdbefedbb7d4b63d7c1f8da56d09d0d69be6b26643cec5fb8ef38d931a7109eef9d482bc7606ef5874ab799061441e9c71e137b9c8d982925f48f37c51a"' \
  --form 'var1="{\"authpayuid\":\"25511473084\",\"requestId\":\"9a900b2f-85e2-4034-aaa9-9c71e1d2af14\",\"amount\":\"1.00\",\"debitDate\":\"2025-10-14\",\"invoiceDisplayNumber\":\"19976ec0-c01f-4f6f-886b-8ea614f5fd83\"}"' \
  --form 'salt="MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCm/k3tcvyLiHH0075vrXkhkjfaC+MOPnjaJRul9JXCdsXqWuYw12OZZlVWjJpi+oNpX0Dn8bq2y7wGXa5sL80XTx25PKTXY0mVOmXIrfydWS0e/p1TsrPS7gwdoN73Zz2rUfIQTAdyhnyFI29NftaEB69Lnve3FN82Skn821HUeGrc3ItPHTSnPAksCHvgNIL9EWfY6vYULO8EtPSnQ4pGgkWuQqU/e4Lty7VlLqp+7v/m6djxedBzo7DQsoTdxf6FjXj2z/5UCIieoovP+8RQwL5z/zk7LjKxlDnzyhEDCHvudYx70lzGAp3m3LoLAjZCwrKZNY+fU6gzjixUm4XjAgMBAAECggEAGH/w0Ohw0svW5DN4mgvaXKmGFjBuRHW351FQaB2lJx2j1ck2Qm4nR6cy1/rS37ifNQNrk1vsp8rmMAzofSjaLxRFaRrTmGIRtpoVusaD7FXb/9MdI91w8n5IOsSSUbvM2WixWeC9qvi+Jg5X0wfL0x0Jg8+zyiF+yglGJ5nJvKEdWCyohM8z7qE2K/zuoMyqXIW316BbmAAmD8jNRiTSTgXn7sjiZl63wc2orkQYGOx46TeK6ez90wweGGDGf3+YxAQuoFWdakSW9bYV//kfgNdIHUdZBoDbdOnYPeJHiD7u7lmAFCn+U8inLS27s6gFe4IWekE4ziN0q7N/ebyiIQKBgQDYqPW8DS18CvQdk1gA78x8QpR0tTMPPkLsq1JXdfyZuStqY1fkTms7bpYLFRlh188vVo4ffqyHaxlYRvkxfFlWEJOgZy1eLsR75Rubq1DBAvSxuL/V51ddou81WsN5+IT8Qr6RxjKUlVBSXjPDXBtbKH3lrn8ySk7h6ShIjny+cQKBgQDFUK7ntqsJDJu29BBXNyQua+OGxC6rldWc2y+gH2i91eMQvMVJjE+rkRBglwuAsre3ELt29AQPSFXq1FuAlSeIRwySqBIVssclPQbutDNSD9HUHJOYULooesmfkBesFmcVxnzzsHvMZyUu6pbjbERAvjXxrUvc20gq7d8VE8hbkwKBgQDWgSmR/mX6+olIQtoNS11j5TM//SpJPDZcRR5n8yudMqRWV3bsVet60vkAjeosYdMBpitd6Td9dz6HlPUg1mFIgW73j09ugNUNaP6Vd96iyX9j+WsMp1drIGa+p1cDilZ3vskYYGcxjkcQ1a1gDPAUp5lF7iaGruU8a2/zrga5MQKBgGc9zzaYoqdqfHNfAsnPpVPQyc0zC0Rmcs3O9f1vUcu6hUO1sfjIvMsFbS9M+QzO9keILr6P8SvZ6nKjyHjgEj5BBrgZztShpYe7hcwSZ6PxeRXmGeghnTYfAS5HI8u8MRX4tFqBplUORytkPa0jchb6L5mT1lTqO7mSmx4ZKsWXAoGAGZuTuOd4lXKrQ4nM3NuG4qEfWc4sJgg1y+9C88Za2b6kKvQ8nBj97rFX1kfFKckkp5qGmdKsqCTDKbj/t6in7Cd/zsW8Zdf/lqWtbAA6j5S8hhUswYwIpt8ruJBtTDpTaRokIaw6wivTSLUMYfr1lWqfE9KBmvUOxS35kVA5rIM="'
  ```

  #### UPI

  ```curl
  curl --location 'https://info.payu.in/merchant/postservice.php' \
  --header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642' \
  --form 'form="2"' \
  --form 'key="smsplus"' \
  --form 'command="pre_debit_SI"' \
  --form 'hash="6e6a34a932bb56bc160cc6b3b40af72e7cfd6cfbf9153edce7b866fe9b87d6d03303e60f810bb7cf2559695bde8033c442e73a8adcfd0957bd8e6fee17b4df37"' \
  --form 'var1="{\"authpayuid\":\"25600438037\",\"requestId\":\"c03f0265-b802-4cd9-8a09-1f679957e02e\",\"amount\":\"1.00\",\"debitDate\":\"2025-10-15\",\"invoiceDisplayNumber\":\"ad52cb45-76ae-4aad-8245-b2eb5e737f17\"}"' \
  --form 'salt="1b1b0"'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-download">
  **Successful sceanario**

  #### Cards

  ```json
  {
    "invoiceid": "76323425",
    "approvedStatus": "na",
    "invoiceStatus": "unpaid",
    "amount": "1.00",
    "status": 1,
    "message": "Invoice Created Successfully",
    "action": "MANDATE_PRE_DEBIT"
  }
  ```

  #### UPI

  ```json
  {
      "status": 1,
      "action": "MANDATE_PRE_DEBIT",
      "message": "Request Processed Successfully"
  }
  ```

  **Failure Scenarios**

  *  Mandate is active in PayU DB and Pre-Debit gets declined from Bank/NPCI

  ```json
  {
  "status":  “QC”   ----- >> Bank/NPCI Error Code
  "action": "MANDATE_PRE_DEBIT",
  "message": “MANDATE HAS BEEN REVOKED”. ---- >> Description against error code
  }
  ```

  Where, the **message** parameter in the response will display error code according to the scenario

  * Mandate is already Paused/ Revoked in PayU DB

  ```json
  {
  "status": 0,
  "action": "MANDATE_PRE_DEBIT",
  "message": "Mandate is not active” --- >> Description will change based on Scenario
  }
  ```

  Where, the **message** parameter in the response will display according to the scenario.
</Accordion>

<Accordion title="Response parameters" icon="fa-download">
  | Parameter Name                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | status                               | Status defines acknowledgment from PayU. Possible values are :<br />· **1**- This value indicates that pre-debit notification is triggered successfully for customer or deleted successfully in case of action delete.<br /><br />· **0** – This value indicates pre-debit notification failed to get triggered and merchant should retry after some time to trigger the same or failed to get deleted in case of action delete. |
  | action                               | Always returned as "MANDATE\_PRE\_DEBIT" to highlight the type of action.                                                                                                                                                                                                                                                                                                                                                        |
  | message                              | Description of the pre-debit notification process                                                                                                                                                                                                                                                                                                                                                                                |
  | invoiceId<br />`only for cards`      | This is an acknowledgment ID that a pre debit notification has been sent for processing.                                                                                                                                                                                                                                                                                                                                         |
  | amount                               | The transaction amount for which the pre-debit notification has been sent.                                                                                                                                                                                                                                                                                                                                                       |
  | invoiceStatus<br />`only for cards`  | This is the status of the invoice whether it has been charged for recurring or not. Values can be:<br />- Paid<br />- Unpaid<br />- Deleted<br />Since these statuses come from a third-party vendor, so these can vary if there is an addition of new status at the vendor end                                                                                                                                                  |
  | approvedStatus<br />`only for cards` | This is for cases where the transaction is above 15000 as RBI guideline says approval is required through AFA (Additional Factor authentication). Values can be:<br />- Pending<br />- Approved<br />- Not\_applicable<br />Since these statuses come from third-party vendors, so these can vary if there is an addition of new status at the vendor end.                                                                       |

  **var1 JSON fields description**

  The **var1** variable is in JSON format and comprises of the following parameters:

  <HTMLBlock>{`
                                            <table style="width: 100%; border-collapse: collapse;">
                                            <thead>
                                            <tr>
                                              <th style="border: 1px solid #ddd; padding: 8px;">JSON Field</th>
                                              <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
                                            </tr>
                                            </thead>
                                            <tbody>
                                            <tr>
                                              <td style="border: 1px solid #ddd; padding: 8px;"><p>authpayuid<br/><strong>mandatory</strong></p>
                                            </td>
                                              <td style="border: 1px solid #ddd; padding: 8px;"><p>The value of mihpayid returned in the payment response of Registration transaction when transaction is successfully completed. As explained earlier in the document, you need to map this value against customer profile at his end so that correct authPayuid will be passed in the request.</p>
                                            </td>
                                            </tr>
                                            <tr>
                                              <td style="border: 1px solid #ddd; padding: 8px;"><p>requestId<br/><strong>mandatory</strong></p>
                                            </td>
                                              <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique request value generated at merchant’s end to distinguish independent request call.</p>
                                            </td>
                                            </tr>
                                            <tr>
                                              <td style="border: 1px solid #ddd; padding: 8px;"><p>debitDate<br/><strong>mandatory for cards and UPI</strong></p>
                                            </td>
                                              <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter contains the date of debit when the recurring would be charged by merchant.<br/>*In UPI:**  </p>
                                            <ul>
                                            <li>For all frequencies (other than Daily and Adhoc), the merchant must send the notification 48 hours before the debit.</li>
                                            <li>For Daily and Adhoc frequency, the merchant must send the notification 24 hours before the debit. If the notification is sent after these durations, then the debit will fail.</li>
                                            </ul>
                                            </td>
                                            </tr>
                                            <tr>
                                              <td style="border: 1px solid #ddd; padding: 8px;"><p>invoiceDisplayNumber<br/><strong>mandatory only for cards</strong></p>
                                            </td>
                                              <td style="border: 1px solid #ddd; padding: 8px;"><p>A unique display number by merchant for every subsequent invoice/recurring charge. This can be displayed on the merchant’s panel to the customer. This same value needs to be sent in the recurring api also.</p>
                                            </td>
                                            </tr>
                                            <tr>
                                              <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br/><strong>mandatory for cards and UPI</strong></p>
                                            </td>
                                              <td style="border: 1px solid #ddd; padding: 8px;"><p>The transaction amount which will be deducted from the customer’s payment instrument.<br/><strong>For Cards:</strong>  </p>
                                            <ul>
                                            <li>In case of Fixed billing plan, this amount should be same as<br/>billingAmount sent during Registration transaction.</li>
                                            <li>In case of Adhoc billing plan, this amount should be equal to or lesser than billingAmount sent during the Registration transaction.<br/><strong>*Note</strong>: The amount mentioned in the Pre-Debit notification API for UPI should be same as the next execution amount. Else, the next recurring execution request will fail.</li>
                                            </ul>
                                            </td>
                                            </tr>
                                            <tr>
                                              <td style="border: 1px solid #ddd; padding: 8px;"><p>action<br/><strong>optional</strong></p>
                                            </td>
                                              <td style="border: 1px solid #ddd; padding: 8px;"><p>Any of the following actions can be performed:<br/>* <strong>Retrieve</strong>: Query the status of the pre-debit notification. Only authpayuid and invoice display numbers are mandatory for this action.<br/>* <strong>Delete</strong>: Delete the already generated pre debit. Only authpayuid and invoice display numbers are mandatory for this action.</p>
                                            </td>
                                            </tr>
                                            </tbody>
                                            </table>
  `}</HTMLBlock>
</Accordion>

## UPI Sequencing

You may attempt multiple pre-debits and executions simultaneously in certain scenarios. To address such scenarios, **mandateSeqNo** field in var1 parameter in the **Pre Debit Notification** API. This is applicable only for UPI autopay transactions.
A sequence is posted based on Mandate creation. When consent is taken, the first execution is carried out in real-time, and the execution sequence is set to 1. The subsequent pre-debit will start from 2.

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data 'form=2&key=smsplus&command=pre_debit_si&var1={"authpayuid": "25600438037", "requestId": "REQ-2024-001-SEQ2", "debitDate": "2024-12-20", "amount": "100.00", "invoiceDisplayNumber": "INV-12345", "mandateSeqNo": 2}&hash=d9e184476637002a3c2db99a7324673647a313de96e574b7a9812e99153dc1a47f0f9da9b32e3a7382bb46dce09a5eb8d4471c85e1bfc1b0dac380a67ff07b43'
  ```
</Accordion>

## Error Codes

<Callout icon="📘" theme="info">
  **Status:** It defines acknowledgment from PayU. Possible values are :

  * **1**- This value indicates that pre-debit notification is triggered successfully for customer or deleted successfully in case of action delete.
  * **0** – This value indicates pre-debit notification failed to get triggered and merchant should retry after some time to trigger the same or failed to get deleted in case of action delete.
</Callout>

<Accordion title="Response in various scenarios" icon="fa-code">
  | Scenario                 | Response Payload                                                                                                                       |
  | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
  | **Success Cases**        |                                                                                                                                        |
  | Successful Pre-debit     | `{"status":1,"action":"MANDATE_PRE_DEBIT","message":"Request Processed Successfully"}`                                                 |
  | *Failure Scenarios*\*    |                                                                                                                                        |
  | Invalid mandateSeqNo     | `{"status":0,"message":"Invalid value for mandateSeqNo","action":"MANDATE_PRE_DEBIT"}`                                                 |
  | Duplicate Pre-debit      | `{"status":"E9254","action":"MANDATE_PRE_DEBIT","message":"Predebit notification already sent for the mandate sequence no.:2"}`        |
  | Execution Already Exists | `{"status":"E9256","action":"MANDATE_PRE_DEBIT","message":"Execution already sent for the mandate sequence no.:2"}`                    |
  | Too Far in Advance       | `{"status":"E9260","action":"MANDATE_PRE_DEBIT","message":"Predebit notification can only be sent for a maximum 30 days in advance."}` |
  | Incorrect Time Period    | `{"status":"E9263","action":"MANDATE_PRE_DEBIT","message":"Predebit for calculated sequence sent during incorrect period"}`            |
  | Mandate Revoked          | `{"status":"QC","action":"MANDATE_PRE_DEBIT","message":"MANDATE HAS BEEN REVOKED"}`                                                    |
  | Mandate Not Active       | `{"status":0,"action":"MANDATE_PRE_DEBIT","message":"Mandate is not active"}`                                                          |
</Accordion>

## Request parameters

<Accordion title="Reference information" icon="fa-book">
  <KeyHashForGeneralParametersDescription />
</Accordion>

Use the following sample values while trying out the API:

**Example values for fields in var1**:

* `authPayuId`: 10731087875
* `requestId`: 23123abut12123osd14
* `debitDate`: 2020-03-20
* `amount`: 100
