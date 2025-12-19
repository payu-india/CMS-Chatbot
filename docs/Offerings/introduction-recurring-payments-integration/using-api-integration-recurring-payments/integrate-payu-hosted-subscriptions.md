---
title: Integrate PayU Hosted - Subscriptions
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Integrate PayU Hosted Subscriptions
excerpt: >-
  Learn how to integrate PayU Hosted Subscriptions workflow for recurring payments. This guide covers the complete integration process from consent transaction to recurring payment execution.
deprecated: false
hidden: false
metadata:
  title: Integrate PayU Hosted Subscriptions
  description: >-
    Complete integration guide for PayU Hosted Subscriptions workflow including Payment Consent Transaction, Pre-Debit Notification, and Recurring Payment APIs.
  keywords:
    - PayU Hosted Subscriptions Integration
    - PayU Hosted Recurring Payments
    - PayU Hosted Subscription Workflow
    - PayU Hosted Checkout Subscriptions
  robots: index
---

This section describes the complete integration workflow for PayU Hosted Subscriptions. The workflow involves three main steps: setting up a payment consent transaction, sending pre-debit notifications, and executing recurring payments.

<Cards columns={3}>
  <Card title="1. Payment Consent Transaction" href="#step-1-payment-consent-transaction">
    Post the required parameters to PayU for payment consent transaction using PayU Hosted Checkout

    <br />
  </Card>

  <Card title="2. Pre-Debit Notification" href="#step-2-pre-debit-notification">
    Send pre-debit notification to customer before recurring payment execution

    <br />
  </Card>

  <Card title="3. Recurring Payment Transaction" href="#step-3-recurring-payment-transaction">
    Execute the recurring payment transaction using the registered mandate
  </Card>
</Cards>

## Step 1: Payment Consent Transaction

This step describes how to set up a Payment Consent or Registration transaction using PayU Hosted Checkout integration.

<Callout icon="👍" theme="okay">
  Automatically generate code including hashing for your eCommerce website to integrate Consent Transaction - PayU Hosted Checkout with zero coding knowledge:

  <HTMLBlock>{`
            <style>
            .tooltip-btn {
                position: relative;
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold; /* Added this line */
            }
            .tooltip-btn:hover::after {
                content: attr(data-tooltip);
                position: absolute;
                bottom: 125%;
                left: 50%;
                transform: translateX(-50%);
                background-color: #333;
                color: white;
                padding: 5px 10px;
                border-radius: 4px;
                white-space: nowrap;
                font-size: 12px;
                z-index: 1;
            }
            </style>

            <button onclick="window.open('https://payu.in/integrationlab/subscription', '_blank')" 
                    class="tooltip-btn" 
                    data-tooltip="Automatically generate code including hashing for your eCommerce website to integrate Registration Consent - PayU Hosted Checkout with zero coding knowledge.">
                Click Here to Generate Code
            </button>
  `}</HTMLBlock>
</Callout>

<br />

HTTP Method: **POST**

**Environment**

|                            |                                                                    |
| :------------------------- | :----------------------------------------------------------------- |
| **Production Environment** | [https://secure.payu.in/_payment](https://secure.payu.in/_payment) |
| **Test Environment**       | [https://test.payu.in/_payment](https://test.payu.in/_payment)     |

### Request parameters

<Accordion title="Request parameters" icon="fa-table">
  In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

  <HTMLBlock>{`
  <style>
  /* Target only the second column in the table */
  .markdown-body table td:nth-child(2) {
    word-break: break-word !important;
  }

  /* Keep the first column from breaking unnecessarily */
  .markdown-body table td:nth-child(1) {
    word-break: normal;
    white-space: nowrap;
  }
  </style>
  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          Parameter
        </th>

        <th style={{ textAlign: "left" }}>
          Description
        </th>

        <th style={{ textAlign: "left" }}>
          Example
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          key <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>varchar</code> This parameter is the unique Merchant Key provided by PayU for your merchant account.
        </td>

        <td style={{ textAlign: "left" }}>
          Your Test Key
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          txnid <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>varchar</code> This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction. <code>Character limit</code>: 25 <br/><strong>Note</strong>: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.'
        </td>

        <td style={{ textAlign: "left" }}>
          fd3e847h2
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          amount <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>float</code> This parameter should contain the payment amount of the particular transaction.
          <br/><strong>Note</strong>: Type-cast the amount to float type Depending upon the merchant use case, this value will vary. <br/>- It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case. <br/>- In the case of first instalment use cases, this amount can be equal to initiate setup amount, but this use case will be supported only against selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI
        </td>

        <td style={{ textAlign: "left" }}>
          1000
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          productinfo <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>varchar</code> This parameter should contain a brief product description. It should be a string describing the product. <code>Character limit</code>: 100
        </td>

        <td style={{ textAlign: "left" }}>
          Time Magazine Subscription
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          firstname <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>varchar</code> Must contain the first name of the customer. <code>Character limit</code>: 60
        </td>

        <td style={{ textAlign: "left" }}>
          Ashish
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          email <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>varchar</code> Must contain the email of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information. Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. <code>Character limit</code>: 50
        </td>

        <td style={{ textAlign: "left" }}>
          <a href="mailto:Ashish@test.com">Ashish@test.com</a>
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          phone <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          <code>varchar</code> Must contain the phone number of the customer. This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions. <code>Character limit</code>: 50
        </td>

        <td style={{ textAlign: "left" }}>
          9843176540
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          surl <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.
        </td>

        <td style={{ textAlign: "left" }}>

        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          furl <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.
        </td>

        <td style={{ textAlign: "left" }}>

        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          api_version <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter must always needs to be passed as 7.
        </td>

        <td style={{ textAlign: "left" }}>
          7
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          si <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.
          <br/><strong>Notes</strong>: You can modify or cancel existing recurring payment registration as described in the following sections: <br/>- <a href="ref:manage-recurring-payment-for-cards">Manage Recurring Payment for Cards</a> <br/>- <a href="ref:api-commands-to-manage-upi-recurring-transaction">Manage UPI Recurring Transaction</a>
        </td>

        <td style={{ textAlign: "left" }}>
          1
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          free_trial <br/>
          <code>optional</code>
        </td>

        <td style={{ textAlign: "left" }}>
          This is mandatory only if the merchant wants to support free trial use cases.
          In this case, PayU adjusts the transaction amount as INR 2.00 for cards and UPI and INR 0.00 for Net Banking irrespective of what amount is passed against the amount field in the request.
        </td>

        <td style={{ textAlign: "left" }}>

        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          si_details <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.
          <br/><strong>Note</strong>: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer <a href="https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0">https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0</a> ) This is a JSON object and it includes a set of fields. For more information, refer to <a href="ref:https://docs.payu.in/reference/si-parameter-json-details/">SI Parameter JSON Details</a>
        </td>

        <td style={{ textAlign: "left" }}>
          {"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          hash <br/>
          <code>mandatory</code>
        </td>

        <td style={{ textAlign: "left" }}>
          Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions. It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt. In the case of registration transaction. The formula is used to calculate this hash is similar to the following:<br/>
          <code>HASH = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)</code>
        </td>

        <td style={{ textAlign: "left" }}>
          txnid
        </td>
      </tr>
    </tbody>
  </Table>
  `}</HTMLBlock>
</Accordion>

### Sample request

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X \
   POST "https://test.payu.in/_payment" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=fM3O2HnkpJ8XEC&amount=100.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc#bankcode=AIRPENCC&si=1&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&si_details={\"billingAmount\": \"100.00\",\"billingCurrency\": \"INR\",\"billingCycle\": \"MONTHLY\",\"billingInterval\": 1,\"paymentStartDate\": \"2022-09-01\",\"paymentEndDate\": \"2022-12-01\"}&hash=2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5"
  ```

  Characters allowed for parameters

  For parameters address1, address2, city, state, country, product info, email, and phone following characters are allowed:

  * Characters: A to Z, a to z, 0 to 9
  * – (Minus)
  * \_ (Underscore)
  * @ ()
  * / (Slash)
  * (Space)
  * . (Dot)
</Accordion>

### Sample response

<Accordion title="Sample response" icon="fa-download">
  The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

  #### Parsed response

  ```
  Array
  (
      [mihpayid] => 403993715525331373
      [mode] => ENACH
      [status] => success
      [unmappedstatus] => captured
      [key] => JPM7Fg
      [txnid] => oRWSUMU4XSQBZn
      [amount] => 100.00
      [discount] => 0.00
      [net_amount_debit] => 0
      [addedon] => 2022-02-03 19:06:55
      [productinfo] => iPhone
      [firstname] => Ashish
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@gmail.com
      [phone] => 9876543210
      [udf1] => 
      [udf2] => 
      [udf3] => 
      [udf4] => 
      [udf5] => 
      [udf6] => 
      [udf7] => 
      [udf8] => 
      [udf9] => 
      [udf10] => 
      [hash] => f3f8e4088231b190930fc4b87d3f39397d1a1d02622ef4683a983244e1cd5158f39adbb67c3d87dcb4da25ae4a941ebbf55918e4575fa1c39677a774d02c0d2d
      [field1] => ENACH285259747472911093
      [field2] => 337026657857179355
      [field3] => 
      [field4] => 
      [field5] => 
      [field6] => 
      [field7] => 
      [field8] => 
      [field9] => Mandate successfully scheduled at bank end: Your payment is scheduled successfully
      [payment_source] => sist
      [PG_TYPE] => ENACH-PG
      [bank_ref_num] => 450699821592111537
      [bankcode] => ICICENCC
      [error] => E000
      [error_Message] => No Error
  )
  ```
</Accordion>

## Step 2: Pre-Debit Notification

The **Pre-Debit Notification** API allows the merchants to send a pre-debit notification to the customer regarding an upcoming payment which will be deducted from the customer's account as part of the registration. There is a mandate to send this notification to the customer at least 48 hours before the actual debit, that is, 48 hours before calling the Recurring API.

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

### Request parameters

<Accordion title="Request parameters" icon="fa-table">
  <KeyHashForGeneralParametersDescription />

  <Accordion title="var1 JSON fields description" icon="fa-table">
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
                                <td style="border: 1px solid #ddd; padding: 8px;"><p>The value of mihpayid returned in the payment response of Registration transaction when transaction is successfully completed. As explained earlier in the document, you need to map this value against customer profile at his end so that correct authPayuid will be passed in the request.</p>
                              </td>
                              </tr>
                              <tr>
                                <td style="border: 1px solid #ddd; padding: 8px;"><p>requestId<br/><strong>mandatory</strong></p>
                              </td>
                                <td style="border: 1px solid #ddd; padding: 8px;"><p>Unique request value generated at merchant's end to distinguish independent request call.</p>
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
                                <td style="border: 1px solid #ddd; padding: 8px;"><p>A unique display number by merchant for every subsequent invoice/recurring charge. This can be displayed on the merchant's panel to the customer. This same value needs to be sent in the recurring api also.</p>
                              </td>
                              </tr>
                              <tr>
                                <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br/><strong>mandatory for cards and UPI</strong></p>
                              </td>
                                <td style="border: 1px solid #ddd; padding: 8px;"><p>The transaction amount which will be deducted from the customer's payment instrument.<br/><strong>For Cards:</strong>  </p>
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
</Accordion>

### Sample request

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location --request POST 'https://test.info.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data
  'key=JF****g&hash=9f5faabedb7f5d41f519db3a223cf5318ecc0b7e669f49e0a699d4c4879e1ccaed5b99f5cd
  8be4f2cbddefe5272ec983abd8f38480d9c2609a29447f750a3158&command=check_action_status_txnid&var
  1=7043873219"
  ```
</Accordion>

### Sample response

<Accordion title="Sample response" icon="fa-download">
  **Successful scenario**

  ```json
  (
    "invoiceid": "76323425",
    "approvedStatus": "na",
    "invoiceStatus": "unpaid",
    "amount": "1.00",
    "status": 1,
    "message": "Invoice Created Successfully",
    "action": "MANDATE_PRE_DEBIT"
  }
  ```

  **Failure Scenarios**

  * Mandate is active in PayU DB and Pre-Debit gets declined from Bank/NPCI

  ```json
  {
  "status":  "QC"   ----- >> Bank/NPCI Error Code
  "action": "MANDATE_PRE_DEBIT",
  "message": "MANDATE HAS BEEN REVOKED". ---- >> Description against error code
  }
  ```

  Where, the **message** parameter in the response will display error code according to the scenario

  * Mandate is already Paused/ Revoked in PayU DB

  ```json
  {
  "status": 0,
  "action": "MANDATE_PRE_DEBIT",
  "message": "Mandate is not active" --- >> Description will change based on Scenario
  }
  ```

  Where, the **message** parameter in the response will display according to the scenario.

  <Accordion title="Response parameters" icon="fa-table">
    | Parameter Name                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
    | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | status                               | Status defines acknowledgment from PayU. Possible values are :<br />· **1**- This value indicates that pre-debit notification is triggered successfully for customer or deleted successfully in case of action delete.<br /><br />· **0** – This value indicates pre-debit notification failed to get triggered and merchant should retry after some time to trigger the same or failed to get deleted in case of action delete. |
    | action                               | Always returned as "MANDATE\_PRE\_DEBIT" to highlight the type of action.                                                                                                                                                                                                                                                                                                                                                        |
    | message                              | Description of the pre-debit notification process                                                                                                                                                                                                                                                                                                                                                                                |
    | invoiceId<br />`only for cards`      | This is an acknowledgment ID that a pre debit notification has been sent for processing.                                                                                                                                                                                                                                                                                                                                         |
    | amount                               | The transaction amount for which the pre-debit notification has been sent.                                                                                                                                                                                                                                                                                                                                                       |
    | invoiceStatus<br />`only for cards`  | This is the status of the invoice whether it has been charged for recurring or not. Values can be:<br />- Paid<br />- Unpaid<br />- Deleted<br />Since these statuses come from a third-party vendor, so these can vary if there is an addition of new status at the vendor end                                                                                                                                                  |
    | approvedStatus<br />`only for cards` | This is for cases where the transaction is above 15000 as RBI guideline says approval is required through AFA (Additional Factor authentication). Values can be:<br />- Pending<br />- Approved<br />- Not\_applicable<br />Since these statuses come from third-party vendors, so these can vary if there is an addition of new status at the vendor end.                                                                       |
  </Accordion>
</Accordion>

## Step 3: Recurring Payment Transaction

All successful registration transactions are charged over the recurring interface with server-to-server API without any additional 2FA or the customers' involvement. This section describes how to achieve the Recurring Transaction for Net Banking, Cards, and UPI through the common platform.

<Callout icon="📘" theme="info">
  **Notes**:

  * Banks do not support refunds for Net Banking Recurring Payment transactions (or e-NACH transaction) so you will get an error message, "Refund not accepted for txn" or Error 232. For the list of banks supporting e-NACH, refer to Recurring Payments Bank Codes.
  * Check the mandate status, call the **Pre-Debit Notification** API before calling the **Recurring Payment Transaction** API to make a recurring payment transaction.
</Callout>

<Callout icon="🚧" theme="warn">
  **Assumptions**: If the merchant has already performed a successful registration transaction with Net Banking/UPI/Card and mihpayid is received in response to the registration transaction captured successfully and mapped to the customer at the merchant's end.
</Callout>

### Environment

|                        |                                                                      |
| :--------------------- | :------------------------------------------------------------------- |
| Production Environment | \<[https://info.payu.in/merchant/>](https://info.payu.in/merchant/>) |
| Test Environment       | \<[https://test.payu.in/merchant/>](https://test.payu.in/merchant/>) |

### Request parameters

<Accordion title="Request parameters" icon="fa-table">
  <Accordion title="Reference information" icon="fa-book">
    <HTMLBlock>{`
                      <table style="width: 100%; border-collapse: collapse;">
                      <thead>
                      <tr>
                        <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
                        <th style="border: 1px solid #ddd; padding: 8px;">Reference</th>
                      </tr>
                      </thead>
                      <tbody>
                      <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><p>&lt;&lt;glossary:key&gt;&gt;</p>
                      </td>
                        <td style="border: 1px solid #ddd; padding: 8px;"><p>For more information on how to generate the Key and Salt, refer to any of the following:  </p>
                      <ul>
                      <li><strong>Production</strong>: <a href="http://docs.payu.in/docs/generate-merchant-key-and-salt-on-payu-dashboard">Generate Merchant Key and Salt</a></li>
                      <li><strong>Test</strong>: <a href="http://docs.payu.in/docs/generate-test-merchant-key-and-salt">Generate Test Merchant Key and Salt</a></li>
                      </ul>
                      </td>
                      </tr>
                      <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><p>&lt;&lt;glossary:hash&gt;&gt;</p>
                      </td>
                        <td style="border: 1px solid #ddd; padding: 8px;"><p>Hash logic for this API is:<br>sha512(key|command|var1|salt)sha512</p>
                      </td>
                      </tr>
                      <tr>
                        <td style="border: 1px solid #ddd; padding: 8px;"><p>var1</p>
                      </td>
                        <td style="border: 1px solid #ddd; padding: 8px;"><p>For JSON fields description, refer to <a href="http://docs.payu.in/reference/addl_info-payment-apis#/">Additional Info. Payment APIs</a></p>
                      </td>
                      </tr>
                      </tbody>
                      </table>
    `}</HTMLBlock>
  </Accordion>
</Accordion>

### Sample request

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&command=si_transaction&var1={\"authpayuid\": \"6611192557\",\"invoiceDisplayNumber\":\"12345678910\",\"amount\": 3,\"txnid\": \"REC15113506209\",\"phone\": \"9999999999\",\"email\": \"chota.bheem@gmail.com\",\"udf2\": \"\",\"udf3\": \"\",\"udf4\": \"\",\"udf5\": \"\"}&hash=jbUS07Og8BToVZ"
  ```
</Accordion>

### Sample response

<Accordion title="Sample response" icon="fa-download">
  **Success scenario**

  Here is a sample response object returned against recurring payment API when the transaction is successfully charged.

  ```json
  {
    "status": 1,
    "message": "Transaction Processed successfully",
    "details": {
        "REC15113506209": {
            "authpayuid": "25600342065",
            "transactionid": "REC15113506209",
            "amount": "1.00",
            "user_credentials": "",
            "card_token": "",
            "payuid": "",
            "status": "captured",
            "udf1": "",
            "field9": "Transaction Completed Successfully",
            "udf2": "",
            "udf3": "",
            "udf4": "",
            "udf5": "",
            "phone": "9999999999",
            "email": "chota.bheem@gmail.com"
        }
    }
  }
  ```

  **Failure scenarios**

  * Invalid hash

  ```json
  {
      "status": 0,
      "msg": "Invalid Hash."
  }
  ```

  * Basic authentication check failed

  ```json
  {
      "status": 1,
      "message": "Transaction Processed successfully",
      "details": {
          "REC9812123123": {
              "authpayuid": "6611192559",
              "transactionid": "REC9812123123",
              "amount": "1",
              "user_credentials": " ",
              "card_token": " ",
              "payuid": "",
              "status": "failed",
              "field9": "Basic authentication check failed",
              "phone": "",
              "email": ""
          }
      }
  }
  ```

  <Accordion title="Response parameters" icon="fa-table">
    **JSON fields description of the Details parameter**

    | JSON Field    | Description                                                                                                                                                                       |
    | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | transactionid | This field contains the value of transaction ID parameter which is echoed back in the response. This is unique transaction ID generated by merchant during calling recurring API. |
    | amount        | This field contains the requested transaction amount is echoed back in the payment response.                                                                                      |
    | payuid        | This field contains the PayU's transaction ID for processed recurring transaction. Merchant can use this field for reference point in the settlement report.                      |
    | status        | This field gives the status of the transaction. Hence, the value of this field depends on whether the transaction was successful or not.                                          |
    | field9        | This field returns the description of transaction status which can help the merchant in providing better customer communication.                                                  |
    | phone         | The mobile number of the customer echoed back.                                                                                                                                    |
    | email         | Email ID of the customer echoed back.                                                                                                                                             |
    | udf1          | Extra information received in the request echoed back.                                                                                                                            |
    | udf2          | Extra information received in the request echoed back.                                                                                                                            |
    | udf3          | Extra information received in the request echoed back.                                                                                                                            |
    | udf4          | Extra information received in the request echoed back.                                                                                                                            |
    | udf5          | Extra information received in the request echoed back.                                                                                                                            |

    #### status field description

    This field gives the status of the transaction. Hence, the value of this field depends on whether the transaction was successful or not.\
    You must map the order status using this parameter only. The possible values of this parameter are:

    * **captured**: If the transaction is successful, the value will be captured. In some cases, the response of Net banking recurring can be captured over real-time basis (ICICI bank in the specific scenario).
    * **pending**: This is common with most Net Banking (except ICICI in the specific scenario) or UPI recurring transaction. In that case, the merchant should consider this as successful initiation of payment with bank / NPCI. The status will be notified back to the merchant over payment processing with individual bank gets completed.\
      For UPI, "pending" transactions get usually get converted into captured or failed within 10 mins from the time of initiation. The Query API can be called post 10 mins from initiation, whereas for Net Banking, it can be called up to T+2 once a day. For more information, refer to [Capture response of Recurring Transaction](#capture-response-of-recurring-transaction-for-net-banking-and-upi).\
      For Net Banking, "pending" transaction gets converted into "captured" or "failed" from the same day till T+2 anytime, depending upon the bank account used by the customer in setting up registration.
    * **failed**: The value of the status as "failed" or blank must be treated as a failed transaction only.
    * **in-progress**: The status of transaction is in progress.

    To capture the final status of "pending" transaction to either "captured" or "failed", PayU recommends merchants to either implement Webhook URL or call **verify\_payment** API after regular intervals. For more information on:

    * Webhook: Refer to [Webhooks](doc:webhooks)
    * **verify\_payment** API: Refer to [Verify Payment API](ref:verify_payment_api)

    > 📘 Note:
    >
    > For UPI, call the **verify\_settlement** API after 10 mins from time of initiation whereas for Net Banking it can be called up to T+2 once in a day.
  </Accordion>
</Accordion>
