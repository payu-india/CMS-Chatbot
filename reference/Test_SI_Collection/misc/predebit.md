---
api:
  file: pre-debit-notification(13-10-2026).json
  operationId: predebit
hidden: true
link:
  new_tab: false
---
The **Pre-Debit Notification** API allows the merchants to send a pre-debit notification to the customer regarding an upcoming payment which will be deducted from the customer’s account as part of the registration. There is a mandate to send this notification to the customer at least 48 hours before the actual debit, that is, 48 hours before calling the Recurring API.

<KeyHashForGeneralParametersDescription />

<br />

<Callout icon="❗️" theme="error">
  ### Reminder

  * Check the mandate status before calling the **Pre-Debit Notification** API.
  * Unless the Pre-Debit notification API is implemented, the **Recurring Payment Transaction** API will not work, and you will not be able to charge the customer for the given billing cycle.
  * Pre-Debit notification is necessary only for Cards and UPI and works for only these two payment modes
</Callout>

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
  --form 'hash="{{hash_value}}"' \
  --form 'var1="{
    \"authpayuid\": \"25511473084\",
    \"requestId\": \"9a900b2f-85e2-4034-aaa9-9c71e1d2af14\",
    \"amount\": \"100.00\",
    \"debitDate\": \"2026-03-20\",
    \"invoiceDisplayNumber\": \"19976ec0-c01f-4f6f-886b-8ea614f5fd83\",
    \"additional_charges\": \"CCSI:10,DCSI:20,AMEXSI:30,HDFCDCSI:40\",
    \"percentage_additional_charges\": \"CCSI:100,DCSI:90,AMEXSI:80,HDFCDCSI:70\"
  }"' \
  --form 'salt="{{salt_value}}"' 
  ```

  #### UPI

  ```curl
  curl --location 'https://info.payu.in/merchant/postservice.php' \
  --header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642' \
  --form 'form="2"' \
  --form 'key="smsplus"' \
  --form 'command="pre_debit_SI"' \
  --form 'hash="{{hash_value}}"' \
  --form 'var1="{
    \"authpayuid\": \"25600438037\",
    \"requestId\": \"c03f0265-b802-4cd9-8a09-1f679957e02e\",
    \"amount\": \"100.00\",
    \"debitDate\": \"2026-03-20\",
    \"invoiceDisplayNumber\": \"ad52cb45-76ae-4aad-8245-b2eb5e737f17\"
  }"' \
  --form 'salt="{{salt_value}}"'
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
    "amount": "100.00",
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
  | action                               | Always returned as "MANDATE_PRE_DEBIT" to highlight the type of action.                                                                                                                                                                                                                                                                                                                                                          |
  | message                              | Description of the pre-debit notification process                                                                                                                                                                                                                                                                                                                                                                                |
  | invoiceId<br />`only for cards`      | This is an acknowledgment ID that a pre debit notification has been sent for processing.                                                                                                                                                                                                                                                                                                                                         |
  | amount                               | The transaction amount for which the pre-debit notification has been sent.                                                                                                                                                                                                                                                                                                                                                       |
  | invoiceStatus<br />`only for cards`  | This is the status of the invoice whether it has been charged for recurring or not. Values can be:<br />\- Paid<br />\- Unpaid<br />\- Deleted<br />Since these statuses come from a third-party vendor, so these can vary if there is an addition of new status at the vendor end                                                                                                                                               |
  | approvedStatus<br />`only for cards` | This is for cases where the transaction is above 15000 as RBI guideline says approval is required through AFA (Additional Factor authentication). Values can be:<br />\- Pending<br />\- Approved<br />\- Not_applicable<br />Since these statuses come from third-party vendors, so these can vary if there is an addition of new status at the vendor end.                                                                     |

  **var1 JSON fields description**

  The **var1** variable is in JSON format and comprises of the following parameters:

  | JSON Field                                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | authpayuid<br />`mandatory`                                 | The value of mihpayid returned in the payment response of Registration transaction when transaction is successfully completed. You need to map this value against the customer profile so that the correct authPayuid is passed in the request.                                                                                                                                                                                                                                                                      |
  | requestId<br />`mandatory`                                  | Unique request value generated at merchant's end to distinguish independent request calls.                                                                                                                                                                                                                                                                                                                                                                                                                           |
  | debitDate<br />`mandatory for cards and UPI`                | The date of debit when the recurring charge will be applied.<br />**In UPI:** For all frequencies (other than Daily and Adhoc), the merchant must send the notification 48 hours before the debit. For Daily and Adhoc frequency, the merchant must send the notification 24 hours before the debit. If the notification is sent after these durations, the debit will fail.                                                                                                                                         |
  | invoiceDisplayNumber<br />`mandatory only for cards`        | A unique display number by merchant for every subsequent invoice/recurring charge. This can be displayed on the merchant's panel to the customer. This same value needs to be sent in the Recurring Payment API as well.                                                                                                                                                                                                                                                                                             |
  | amount<br />`mandatory for cards and UPI`                   | The transaction amount which will be deducted from the customer's payment instrument.<br />**For Cards:** In case of a Fixed billing plan, this amount should be the same as the `billingAmount` sent during the Registration transaction. In case of an Adhoc billing plan, this amount should be equal to or lesser than the `billingAmount` sent during Registration.<br />**Note:** For UPI, the amount must match the next execution amount exactly — otherwise the next recurring execution request will fail. |
  | action<br />`optional`                                      | Any of the following actions can be performed:<br />**Retrieve** — Query the status of the pre-debit notification. Only `authpayuid` and `invoiceDisplayNumber` are mandatory for this action.<br />**Delete** — Delete the already generated pre-debit. Only `authpayuid` and `invoiceDisplayNumber` are mandatory for this action.                                                                                                                                                                                 |
  | additional_charges<br />`optional` {/* [NEW] */}            | Flat convenience fee per SI card type, expressed as a comma-separated string of `IBIBOCODE:value` pairs (e.g., `CCSI:10,DCSI:20,AMEXSI:30,HDFCDCSI:40`). Applicable only for Cards SI mandates when the `enableSIPredebitConvFee` and `enableCardsSiDynamicConv` flags are active on the MID.<br />Allowed ibibocodes: **CCSI** (Credit Card SI), **DCSI** (Debit Card SI), **AMEXSI** (American Express SI), **HDFCDCSI** (HDFC Debit Card SI), **VISASI** (Visa SI).                                               |
  | percentage_additional_charges<br />`optional` {/* [NEW] */} | Percentage-based convenience fee per SI card type, expressed as a comma-separated string of `IBIBOCODE:value` pairs (e.g., `CCSI:100,DCSI:90,AMEXSI:80,HDFCDCSI:70`). Uses the same ibibocodes as `additional_charges`. Applicable only when `enableSIPredebitConvFee` and `enableCardsSiDynamicConv` flags are active on the MID.                                                                                                                                                                                   |
</Accordion>

## UPI Sequencing

You may attempt multiple pre-debits and executions simultaneously in certain scenarios. To address such scenarios, **mandateSeqNo** field in var1 parameter in the **Pre Debit Notification** API. This is applicable only for UPI autopay transactions.
A sequence is posted based on Mandate creation. When consent is taken, the first execution is carried out in real-time, and the execution sequence is set to 1. The subsequent pre-debit will start from 2.

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data 'form=2' \
  --data 'key=smsplus' \
  --data 'command=pre_debit_si' \
  --data 'var1={
    "authpayuid": "25600438037",
    "requestId": "REQ-2024-001-SEQ2",
    "debitDate": "2026-03-20",
    "amount": "100.00",
    "invoiceDisplayNumber": "INV-12345",
    "mandateSeqNo": 2
  }' \
  --data 'hash={{hash_value}}'
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
  | _Failure Scenarios_\*    |                                                                                                                                        |
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

* `authPayuId`: `10731087875`
* `requestId`: `23123abut12123osd14`
* `debitDate`: `2020-03-20`
* `amount`: `100.00`