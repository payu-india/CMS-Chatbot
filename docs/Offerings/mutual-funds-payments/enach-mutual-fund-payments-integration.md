---
title: ENACH Integration -Mutual Funds
deprecated: false
hidden: true
metadata:
  robots: index
---
Merchants can set up automated subscription billing through various payment methods including Net Banking (e-NACH) for Mutual Fund Payments. This section describes how to integrate mutual fund subscription for ENACH using seamless integration.

<Cards columns={2}>
  <Card title="1. Consent Transaction" href="#consent-transaction">
    Initiate the recurring payment process by capturing user consent for the mandate with required parameters including key, txnid, amount, productinfo, customer details, and si\_details JSON object

    <br />
  </Card>

  <Card title="2. Verify the Payment" href="#verify-the-payment">
    Ensure the initial consent transaction or registration is successfully processed before proceeding with recurring charges

    <br />
  </Card>

  <Card title="3. Pre-Debit Notification" href="#pre-debit-notification">
    Send advance notifications to customers about upcoming recurring payments, essential for UPI and Cards per RBI guidelines with authpayuid and debitDate parameters

    <br />
  </Card>

  <Card title="4. Recurring Payment Transaction" href="#recurring-payment-transaction">
    Execute recurring payments automatically without additional customer involvement using server-to-server integration with authpayuid and invoiceDisplayNumber

    <br />
  </Card>

  <br />
</Cards>

## Step 1: Consent Transaction

HTTP Method: **POST**

**Environment**

|                        |                                                                    |
| :--------------------- | :----------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/_payment](https://test.payu.in/_payment)     |
| Production Environment | [https://secure.payu.in/_payment](https://secure.payu.in/_payment) |

<Accordion title="Request Parameters" icon="fa-table">
  Now I'll create the cleaned table with only the necessary three columns and proper formatting:

  | Parameter                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                              |
  | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | key<br />`mandatory`                            | `String` This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to Generate Merchant Key and Salt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 8488225                                                                                                                                                              |
  | txnid<br />`mandatory`                          | `Varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn't been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID'). | fd3e847h2                                                                                                                                                            |
  | amount<br />`mandatory`                         | `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 10                                                                                                                                                                   |
  | productinfo<br />`mandatory`                    | `Varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice).                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | T-shirt                                                                                                                                                              |
  | firstname<br />`mandatory`                      | `Varchar` This parameter must contain the first name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Ankit                                                                                                                                                                |
  | email<br />`mandatory`                          | `Varchar` This parameter must contain the email of the customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [test@gmail.com](mailto:test@gmail.com)                                                                                                                              |
  | phone<br />`mandatory`                          | `Integer` Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.                                                                                                                                                                                                                                                                                                                                                                                                                                            | 9876543210                                                                                                                                                           |
  | pg<br />`mandatory`                             | `String` This parameter contains the payment method to be enabled to collect payment from your customer. For the list of payment methods and their codes, refer to Payment Mode Codes. For ENACH, use ENACH.                                                                                                                                                                                                                                                                                                                                                                                                                              | ENACH                                                                                                                                                                   |
  | bankcode<br />`mandatory`                       | `string` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For the list of bankcodes for Net Banking, refer to (Net Banking Codes)[doc:bank-codes-recurring-payments].                                                                                                                                                                                                                                                                                                                                                                                      | ICICENCC                                                                                                                                                                 |
  | surl<br />`mandatory`                           | `string` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                             | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                                       |
  | furl<br />`mandatory`                           | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                                 | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                                       |
  | api\_version<br />`mandatory`                   | API version must be posted as `21`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 21                                                                                                                                                                   |
  | si<br />`mandatory`                             | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.<br />**Notes**: You can modify or cancel existing recurring payment registration as described in the following sections: <br />- Manage Recurring Payment for Cards <br />- Manage UPI Recurring Transaction                                                                                                                                                                                                                     | 1                                                                                                                                                                    |
  | free\_trial<br />`optional`                     | This is mandatory only if the merchant wants to support free trial use cases. In this case, PayU adjusts the transaction amount as INR 2.00 for cards and UPI and INR 0.00 for Net Banking irrespective of what amount is passed against the amount field in the request.                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                      |
  | si\_details<br />`mandatory`                    | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.<br />**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0) ) This is a JSON object and it includes a set of fields. For more information, refer to SI Parameter JSON Details                                      | \{"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"} |
  | hash<br />`mandatory`                           | `String` The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: sha(key\\\|txnid\\\|amount\\\|productinfo\\\|firstname\\\|email\\\|udf1\\\|udf2\\\|udf3\\\|udf4\\\|udf5\\\|\\\|\\\|\\\|\\\|\\\|beneficiarydetail\\\|si\_details\\\|\\\|\\\|\\\|\\\|products\\\|salt) For more information, refer to Generate Hash.                                                                                                                                                                                                                                                                | a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0                                                                                                                             |
  | products<br />`mandatory for Wealth Tech`       | `JSON` This parameter contains various fields including the Wealth Tech object (**wtParams**). For more information on wtParams object field, refer to Wealth Tech object wtparams fields description.                                                                                                                                                                                                                                                                                                                                                                                                                                       | Refer to Wealth Tech object wtparams fields description.                                                                                                             |
  | txn_s2s_flow <br />`mandatory` | `String` This parameter must be passed with the value as 4 for Decoupled flow.| 4|
  | lastname<br />`optional`                        | `String` The last name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Sharma                                                                                                                                                               |
  | address1<br />`optional`                        | `String` The first line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 123 Main Street                                                                                                                                                      |
  | address2<br />`optional`                        | `String` The second line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Apartment 4B                                                                                                                                                         |
  | city<br />`optional`                            | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Mumbai                                                                                                                                                               |
  | state<br />`optional`                           | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Maharashtra                                                                                                                                                          |
  | country<br />`optional`                         | `String` The country where your customer resides.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | India                                                                                                                                                                |
  | zipcode<br />`optional`                         | `String` Billing address zip code is mandatory for the cardless EMI option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 400001                                                                                                                                                               |
  | udf1<br />`mandatory for Cross-Border Payments` | `String` This parameter has been made for you to keep any information corresponding to the transaction. **Note**: This parameter must contain buyer's PAN number for Cross-Border Payments.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | ABCDE1234F                                                                                                                                                           |
  | udf2<br />`optional`                            | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 1                                                                                                                                                    |
  | udf3<br />`mandatory for Cross-Border Payments` | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | GSTIN123456                                                                                                                                                          |
  | udf4<br />`optional`                            | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 2                                                                                                                                                    |
  | udf5<br />`optional`                            | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 3                                                                                                                                                    |
  | beneficiarydetail<br />`mandatory`              | This is a JSON format text and there should be key named **beneficiaryAccountNumber** with the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter.                                                                                                                                                                                                                                                                                                                        | Refer to the beneficiarydetail JSON Object Fields section.                                                                                                           |

  <Accordion title="Beneficiary Detail Fields Description" icon="fa-university">
    ### Sample object

    ```json
    {
      "beneficiaryName": "Sachin Tendulkar",
      "beneficiaryAccountNumber": "1211450021",
      "beneficiaryAccountType": "SAVINGS", 
      "beneficiaryIfscCode":"ICIC0000046", 
      "verificationMode":"DEBIT_CARD"
    }
    ```

    ### Description

    | Field                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | BeneficiaryName          | Registered name against customer's account                                                                                                                                                                                                                                                                                                                                                                                                           |
    | BeneficiaryAccountNumber | Account number against which recurring transactions need to be executed.                                                                                                                                                                                                                                                                                                                                                                             |
    | BeneficiaryAccountType   | SAVINGS or CURRENT                                                                                                                                                                                                                                                                                                                                                                                                                                   |
    | beneficiaryIfscCode      | 11-digit IFSC code of the customer bank                                                                                                                                                                                                                                                                                                                                                                                                              |
    | verificationMode         | The verification mode can be any of the following: <ul><li>**DEBIT\_CARD** – authentication will be done through a debit card. If no value is provided, then it will trigger Net Banking login password flow.</li><li>**AADHAAR** – authentication will be done through a Aadhaar card. If no value , then it will trigger net banking login password flow. If no value is provided, then it will trigger Net Banking login password flow.</li></ul> |
  </Accordion>

  <Mutual_Funds_Product_JSON />
</Accordion>

<Accordion title="Sample Request Examples" icon="fa-code">
  ### Sample request

  ```curl
  curl --location 'https://test.payu.in/_payment' \
--header 'accept: application/json' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: USERTXNINFO=696de147e75262.22575647; PHPSESSID=699bf05fe3f41; PHPSESSID=69ba5520d142f' \
--data-urlencode 'key=j6Bb3k' \
--data-urlencode 'txnid=txn_97718080' \
--data-urlencode 'amount=5000' \
--data-urlencode 'productinfo=iphone' \
--data-urlencode 'firstname=Sumit' \
--data-urlencode 'email=test@gmail.com' \
--data-urlencode 'phone=7715995865' \
--data-urlencode 'surl=https://localhost:8080/PayU/success' \
--data-urlencode 'furl=https://localhost:8080/PayU/failure' \
--data-urlencode 'hash={{hash}}' \
--data-urlencode 'pg=ENACH' \
--data-urlencode 'bankcode=ICICENCC' \
--data-urlencode 'surl=https://test.payu.in/admin/test_response' \
--data-urlencode 'furl=https://test.payu.in/admin/test_response' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'beneficiarydetail={"beneficiaryName": "Sachin Tendulkar","beneficiaryAccountNumber": "1211450021","beneficiaryAccountType": "SAVINGS", "beneficiaryIfscCode":"ICIC0000046", "verificationMode":"DEBIT_CARD"}' \
--data-urlencode 'free_trail=1' \
--data-urlencode 'si_details={"billingAmount":"50000.00","billingCurrency":"INR","billingCycle":"ADHOC","billingInterval":1,"paymentStartDate":"2026-03-20","paymentEndDate":"2026-07-20"}' \
--data-urlencode 'SI=1' \
--data-urlencode 'api_version=21' \
--data-urlencode 'products={"wtParams":[{"type":"mutual_fund","plan":"GD","amount":"50000","option":"G","scheme":"LT","receipt":"77407","mf_member_id":"123445","mf_user_id":"77407","mf_partner":"cams","mf_investment_type":"L","mf_amc_code":"UTB"}]}'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-reply">
  #### Initial response

  ```json
    {
    "metaData": {
        "message": null,
        "referenceId": "88ff908fb1a7ae9038499597bcd84e963ecea18adbfa0340c730156b8667f09d",
        "statusCode": null,
        "txnId": "txn_97718080",
        "txnStatus": "pending",
        "unmappedStatus": "pending"
    },
    "result": {
        "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vZW5hY2gtc2ltLnBheXUuaW4vc2ltdWxhdG9yL2NvcnAvQkFOS0FXQVkiIG1ldGhvZD0icG9zdCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iQkFZX0JBTktJRCIgdmFsdWU9IklDSSI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iRVMiIHZhbHVlPSJjTWprdHMzdDMvcmdHLzZ2eWF6dkZRTDZZMGRXVG05WHViSTcwdXdLMkFrNW5ua1U1d0tZSlppOHhaLytLVWlRV1k3NUlYTDlMc0xtZ1Nrc2R4THltNmYrTUxuK1Q1Q3hnV2huem1yWkRrVFZhMnJHNGl4QVRIdDltRzNuM3kySWd0d3pTTUh6cG5uNzdqNlZkdE14RFB0eWI4aVd6ckZPayt6QzNUUklvZHdBTGZjVmJMWGNHb0ZJMmJBTFgvTk9ZbkhoYlRXWVFqMHdwOFpmMkI5Q0JEOEFZcURQc1dPSWl4eVR4MjJxTTZZM2hwL1JKa3pQTHhCM1lOZE9NaHdISUhXV1FXbTFSL3l6QjB0STJuNGIwSFdiZ0NRQTc1K25VRnF4MzBWWVRTdFBJVXMyUmtQekFzSGJTK0VUV1NOOUJTMXMwYTlxcFVmbzYzU0JjNlppL0NCeTNjVy9JbnZFNjdKV0tjUWs0cWxDZXQ3SE1pRG1DckdNbWFwQzJ3d3FQdnBkdVByTHNDK05sMlRhZWdWL0pBPT0iPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9IklXUVJZVEFTS09CSk5BTUUiIHZhbHVlPSJiYXlfbWNfbG9naW4iPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9Ik1EIiB2YWx1ZT0iUCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iUElEIiB2YWx1ZT0iMDAwMDAwMDAwNzIyIj48L2Zvcm0+PHNjcmlwdCB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgd2luZG93Lm9ubG9hZD1mdW5jdGlvbigpewogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRvY3VtZW50LmZvcm1zWydwYXltZW50X3Bvc3QnXS5zdWJtaXQoKTsKICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICAgICAgICAgPC9zY3JpcHQ+PC9ib2R5PjwvaHRtbD4=",
        "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
    }
}


}

  ```

  You must redirect the customer and authorize the charges as described in Decoupled Flow Integration. For more information, refer to (Decoupled Flow Integration)\[doc:integrate-with-decoupled-flow-s2s]. The parsed response similar to the following.

####Parsed response

  ```json
(
      [mihpayid] => 403993715537008957
      [mode] => ENACH
      [status] => success
      [key] => j6Bb3k
      [txnid] => txn_97718080
      [amount] => 5000.00
      [addedon] => 2026-03-18 13:02:49
      [productinfo] => iphone
      [firstname] => Sumit
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@gmail.com
      [phone] => 7715995865
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
      [card_token] => 
      [card_no] => 
      [field0] => 
      [field1] => ENACH866231933150874704
      [field2] => 202859885067486788
      [field3] => 
      [field4] => 
      [field5] => 
      [field6] => 
      [field7] => 
      [field8] => 
      [field9] => Mandate successfully scheduled at bank end: Your payment is scheduled successfully
      [payment_source] => sist
      [cardToken] => 
      [authenticaticationMethod] => 
      [PG_TYPE] => ENACH-PG
      [error] => E000
      [error_Message] => No Error
      [net_amount_debit] => 5000
      [discount] => 0.00
      [offer_key] => 
      [offer_availed] => 
      [unmappedstatus] => captured
      [hash] => 2794739ed6ca0fdb00540b4cf76cd8d42146ce43596a49b79011214eb1cf72f525252a39c1db6a38c1e81724fc2f56542a383a57eaca262c7df6b62fcb92ac73
      [bank_ref_no] => 154710586635169646
      [bank_ref_num] => 154710586635169646
      [bankcode] => ICICENCC
      [surl] => https://test.payu.in/admin/test_response
      [curl] => https://test.payu.in/admin/test_response
      [furl] => https://test.payu.in/admin/test_response
      [IsStandingInstructionSet] => 1
)
  
  ```
</Accordion>

***

## Step 2: Verify the payment

The payment verification step ensures the transaction has been processed successfully before proceeding to subsequent recurring payments.

<Verify_Payment_Tabs />

***

## Step 3: Pre-Debit Notification

The **Pre-Debit Notification** API allows the merchants to send a pre-debit notification to the customer regarding an upcoming payment which will be deducted from the customer's account as part of the registration.

> ❗️ **Reminder**
>
> * Check the mandate status before calling the **Pre-Debit Notification** API.
> * Unless the Pre-Debit notification API is implemented, the **Recurring Payment Transaction** API will not work, and you will not be able to charge the customer for the given billing cycle.
> * Pre-Debit notification is necessary only for Cards and UPI and works for only these two payment modes

**Environment**

|                        |                                                                  |
| :--------------------- | :--------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/merchant/](https://info.payu.in/merchant/) |
| Test Environment       | [https://test.payu.in/merchant/](https://test.payu.in/merchant/) |

<Accordion title="Sample Request" icon="fa-upload">
  ```curl
  curl --location --request POST 'https://test.info.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data
  'key=JF****g&hash=9f5faabedb7f5d41f519db3a223cf5318ecc0b7e669f49e0a699d4c4879e1ccaed5b99f5cd8be4f2cbddefe5272ec983abd8f38480d9c2609a29447f750a3158&command=check_action_status_txnid&var1=7043873219'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-download">
  **Successful scenario**

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

  **Failure Scenarios**

  * Mandate is active in PayU DB and Pre-Debit gets declined from Bank/NPCI

  ```json
  {
    "status": "QC",
    "action": "MANDATE_PRE_DEBIT",
    "message": "MANDATE HAS BEEN REVOKED"
  }
  ```

  Where, the **message** parameter in the response will display error code according to the scenario

  * Mandate is already Paused/ Revoked in PayU DB

  ```json
  {
    "status": 0,
    "action": "MANDATE_PRE_DEBIT",
    "message": "Mandate is not active"
  }
  ```

  Where, the **message** parameter in the response will display according to the scenario.
</Accordion>

<Accordion title="Response Parameters" icon="fa-list">
  | Parameter Name                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
  | ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | status                               | Status defines acknowledgment from PayU. Possible values are :<br />• **1**- This value indicates that pre-debit notification is triggered successfully for customer or deleted successfully in case of action delete.<br /><br />• **0** – This value indicates pre-debit notification failed to get triggered and merchant should retry after some time to trigger the same or failed to get deleted in case of action delete. |
  | action                               | Always returned as "MANDATE\_PRE\_DEBIT" to highlight the type of action.                                                                                                                                                                                                                                                                                                                                                        |
  | message                              | Description of the pre-debit notification process                                                                                                                                                                                                                                                                                                                                                                                |
  | invoiceId<br />`only for cards`      | This is an acknowledgment ID that a pre debit notification has been sent for processing.                                                                                                                                                                                                                                                                                                                                         |
  | amount                               | The transaction amount for which the pre-debit notification has been sent.                                                                                                                                                                                                                                                                                                                                                       |
  | invoiceStatus<br />`only for cards`  | This is the status of the invoice whether it has been charged for recurring or not. Values can be:<br />- Paid<br />- Unpaid<br />- Deleted<br />Since these statuses come from a third-party vendor, so these can vary if there is an addition of new status at the vendor end                                                                                                                                                  |
  | approvedStatus<br />`only for cards` | This is for cases where the transaction is above 15000 as RBI guideline says approval is required through AFA (Additional Factor authentication). Values can be:<br />- Pending<br />- Approved<br />- Not\_applicable<br />Since these statuses come from third-party vendors, so these can vary if there is an addition of new status at the vendor end.                                                                       |

  **var1 JSON fields description**

  The **var1** variable is in JSON format and comprises of the following parameters:

  | JSON Field                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | authpayuid<br />**mandatory**                          | The value of mihpayid returned in the payment response of Registration transaction when transaction is successfully completed. As explained earlier in the document, you need to map this value against customer profile at his end so that correct authPayuid will be passed in the request.                                                                                                                                                                                                                                                                              |
  | requestId<br />**mandatory**                           | Unique request value generated at merchant's end to distinguish independent request call.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | debitDate<br />**mandatory for cards and UPI**         | This parameter contains the date of debit when the recurring would be charged by merchant.<br />**In UPI:** <ul><li>For all frequencies (other than Daily and Adhoc), the merchant must send the notification 48 hours before the debit.</li><li>For Daily and Adhoc frequency, the merchant must send the notification 24 hours before the debit. If the notification is sent after these durations, then the debit will fail.</li></ul>                                                                                                                                  |
  | invoiceDisplayNumber<br />**mandatory only for cards** | A unique display number by merchant for every subsequent invoice/recurring charge. This can be displayed on the merchant's panel to the customer. This same value needs to be sent in the recurring api also.                                                                                                                                                                                                                                                                                                                                                              |
  | amount<br />**mandatory for cards and UPI**            | The transaction amount which will be deducted from the customer's payment instrument.<br />**For Cards:** <ul><li>In case of Fixed billing plan, this amount should be same as billingAmount sent during Registration transaction.</li><li>In case of Adhoc billing plan, this amount should be equal to or lesser than billingAmount sent during the Registration transaction.<br />**Note**: The amount mentioned in the Pre-Debit notification API for UPI should be same as the next execution amount. Else, the next recurring execution request will fail.</li></ul> |
  | action<br />**optional**                               | Any of the following actions can be performed:<br />• **Retrieve**: Query the status of the pre-debit notification. Only authpayuid and invoice display numbers are mandatory for this action.<br />• **Delete**: Delete the already generated pre debit. Only authpayuid and invoice display numbers are mandatory for this action.                                                                                                                                                                                                                                       |
</Accordion>

***

## Step 4: Recurring Payment Transaction

All successful registration transactions are charged over the recurring interface with server-to-server API without any additional 2FA or the customers' involvement.

> 📘 **Notes**:
>
> * Banks do not support refunds for Net Banking Recurring Payment transactions (or e-NACH transaction) so you will get an error message, "Refund not accepted for txn" or Error 232. For the list of banks supporting e-NACH, refer to Recurring Payments Bank Codes.
> * Check the mandate status, call the **Pre-Debit Notification** API before calling the **Recurring Payment Transaction** API to make a recurring payment transaction.

> 🚧 **Assumptions**: If the merchant has already performed a successful registration transaction with Net Banking/UPI/Card and mihpayid is received in response to the registration transaction captured successfully and mapped to the customer at the merchant's end.

**Environment**

|                        |                                                                  |
| :--------------------- | :--------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/merchant/](https://info.payu.in/merchant/) |
| Test Environment       | [https://test.payu.in/merchant/](https://test.payu.in/merchant/) |

<Accordion title="Sample Request" icon="fa-terminal">
  ```curl
  curl -X POST "https://test.payu.in/merchant/postservice?form=2" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&command=si_transaction&var1={"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}&hash=jbUS07Og8BToVZ"
  ```
  ```python
  import requests
  import urllib.parse

  # PayU API endpoint
  url = "https://test.payu.in/merchant/postservice?form=2"

  # Headers
  headers = {
      "accept": "application/json",
      "Content-Type": "application/x-www-form-urlencoded"
  }

  # Form data
  form_data = {
      "key": "JP***g",
      "command": "si_transaction",
      "var1": '{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}',
      "hash": "jbUS07Og8BToVZ"
  }

  # Make the POST request
  try:
      response = requests.post(url, headers=headers, data=form_data)
      print(f"Status Code: {response.status_code}")
      print(f"Response: {response.text}")
  except requests.exceptions.RequestException as e:
      print(f"Error: {e}")
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.URLEncoder;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.nio.charset.StandardCharsets;
  import java.time.Duration;
  import java.util.HashMap;
  import java.util.Map;
  import java.util.stream.Collectors;

  public class PayUApiClient {
      
      private static final HttpClient client = HttpClient.newBuilder()
              .connectTimeout(Duration.ofSeconds(30))
              .build();
      
      public static void main(String[] args) {
          try {
              makePayURequest();
          } catch (Exception e) {
              System.err.println("Error: " + e.getMessage());
          }
      }
      
      public static void makePayURequest() throws IOException, InterruptedException {
          String url = "https://test.payu.in/merchant/postservice?form=2";
          
          // Prepare form data
          Map<String, String> formData = new HashMap<>();
          formData.put("key", "JP***g");
          formData.put("command", "si_transaction");
          formData.put("var1", "{\"authpayuid\": \"6611192557\",\"invoiceDisplayNumber\":\"12345678910\",\"amount\": 3,\"txnid\": \"REC15113506209\",\"phone\": \"9999999999\",\"email\": \"chota.bheem@gmail.com\",\"udf2\": \"\",\"udf3\": \"\",\"udf4\": \"\",\"udf5\": \"\"}");
          formData.put("hash", "jbUS07Og8BToVZ");
          
          // Convert to URL encoded string
          String formBody = formData.entrySet().stream()
                  .map(entry -> URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + 
                               "=" + URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8))
                  .collect(Collectors.joining("&"));
          
          // Build request
          HttpRequest request = HttpRequest.newBuilder()
                  .uri(URI.create(url))
                  .header("accept", "application/json")
                  .header("Content-Type", "application/x-www-form-urlencoded")
                  .POST(HttpRequest.BodyPublishers.ofString(formBody))
                  .build();
          
          // Send request
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          
          System.out.println("Status Code: " + response.statusCode());
          System.out.println("Response: " + response.body());
      }
  }
  ```
  ```javascript
  // PayU API call using modern Async/Await Fetch
  async function makePayURequest() {
      const url = "https://test.payu.in/merchant/postservice?form=2";
      
      // Headers
      const headers = {
          "accept": "application/json",
          "Content-Type": "application/x-www-form-urlencoded"
      };
      
      // Form data
      const formData = new URLSearchParams({
          "key": "JP***g",
          "command": "si_transaction",
          "var1": '{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}',
          "hash": "jbUS07Og8BToVZ"
      });
      
      try {
          const response = await fetch(url, {
              method: "POST",
              headers: headers,
              body: formData
          });
          
          const responseText = await response.text();
          
          console.log(`Status: ${response.status}`);
          console.log(`Response: ${responseText}`);
          
          return {
              status: response.status,
              data: responseText
          };
          
      } catch (error) {
          console.error("Error:", error);
          throw error;
      }
  }

  // Call the function
  makePayURequest()
      .then(result => console.log("Success:", result))
      .catch(error => console.error("Failed:", error));
  ```
  ```csharp
  using System;
  using System.Collections.Generic;
  using System.Net.Http;
  using System.Text;
  using System.Threading.Tasks;

  class Program
  {
      private static readonly HttpClient client = new HttpClient();

      static async Task Main(string[] args)
      {
          string url = "https://test.payu.in/merchant/postservice?form=2";
          
          // Set headers
          client.DefaultRequestHeaders.Add("accept", "application/json");
          
          // Prepare form data
          var formData = new List<KeyValuePair<string, string>>
          {
              new KeyValuePair<string, string>("key", "JP***g"),
              new KeyValuePair<string, string>("command", "si_transaction"),
              new KeyValuePair<string, string>("var1", "{\"authpayuid\": \"6611192557\",\"invoiceDisplayNumber\":\"12345678910\",\"amount\": 3,\"txnid\": \"REC15113506209\",\"phone\": \"9999999999\",\"email\": \"chota.bheem@gmail.com\",\"udf2\": \"\",\"udf3\": \"\",\"udf4\": \"\",\"udf5\": \"\"}"),
              new KeyValuePair<string, string>("hash", "jbUS07Og8BToVZ")
          };
          
          var formContent = new FormUrlEncodedContent(formData);
          
          try
          {
              HttpResponseMessage response = await client.PostAsync(url, formContent);
              string responseContent = await response.Content.ReadAsStringAsync();
              
              Console.WriteLine($"Status Code: {response.StatusCode}");
              Console.WriteLine($"Response: {responseContent}");
          }
          catch (HttpRequestException e)
          {
              Console.WriteLine($"Error: {e.Message}");
          }
      }
  }
  ```
  ```php
  // PayU API endpoint
  $url = "https://test.payu.in/merchant/postservice?form=2";

  // Form data
  $postData = [
      'key' => 'JP***g',
      'command' => 'si_transaction',
      'var1' => '{"authpayuid": "6611192557","invoiceDisplayNumber":"12345678910","amount": 3,"txnid": "REC15113506209","phone": "9999999999","email": "chota.bheem@gmail.com","udf2": "","udf3": "","udf4": "","udf5": ""}',
      'hash' => 'jbUS07Og8BToVZ'
  ];

  // Initialize cURL
  $ch = curl_init();

  // Set cURL options
  curl_setopt_array($ch, [
      CURLOPT_URL => $url,
      CURLOPT_POST => true,
      CURLOPT_POSTFIELDS => http_build_query($postData),
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_HTTPHEADER => [
          'accept: application/json',
          'Content-Type: application/x-www-form-urlencoded'
      ],
      CURLOPT_TIMEOUT => 30,
      CURLOPT_FOLLOWLOCATION => true,
      CURLOPT_SSL_VERIFYPEER => false, // Only for testing
  ]);

  // Execute request
  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  $error = curl_error($ch);

  // Close cURL
  curl_close($ch);

  // Handle response
  if ($error) {
      echo "cURL Error: " . $error . PHP_EOL;
  } else {
      echo "Status Code: " . $httpCode . PHP_EOL;
      echo "Response: " . $response . PHP_EOL;
  }
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-check-circle">
  \###Success Scenario

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

  ### Failure Scenarios

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
</Accordion>

<Accordion title="Response Parameters" icon="fa-list">
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

  ### status field description

  This field gives the status of the transaction. Hence, the value of this field depends on whether the transaction was successful or not.\
  You must map the order status using this parameter only. The possible values of this parameter are:

  * **captured**: If the transaction is successful, the value will be captured. In some cases, the response of Net banking recurring can be captured over real-time basis (ICICI bank in the specific scenario).
  * **pending**: This is common with most Net Banking (except ICICI in the specific scenario) or UPI recurring transaction. In that case, the merchant should consider this as successful initiation of payment with bank / NPCI. The status will be notified back to the merchant over payment processing with individual bank gets completed.\
    For UPI, "pending" transactions get usually get converted into captured or failed within 10 mins from the time of initiation. The Query API can be called post 10 mins from initiation, whereas for Net Banking, it can be called up to T+2 once a day. For more information, refer to Capture response of Recurring Transaction for Net Banking and UPI.\
    For Net Banking, "pending" transaction gets converted into "captured" or "failed" from the same day till T+2 anytime, depending upon the bank account used by the customer in setting up registration.
  * **failed**: The value of the status as "failed" or blank must be treated as a failed transaction only.
  * **in-progress**: The status of transaction is in progress.

  To capture the final status of "pending" transaction to either "captured" or "failed", PayU recommends merchants to either implement Webhook URL or call **verify\_payment** API after regular intervals. For more information on:

  * Webhook: Refer to [Webhooks](doc:webhooks)
  * **verify\_payment** API: Refer to [Verify Payment API](ref:verify_payment_api)

  > 📘 **Note**:
  >
  > For UPI, call the **verify\_settlement** API after 10 mins from time of initiation whereas for Net Banking it can be called up to T+2 once in a day.
</Accordion>

***