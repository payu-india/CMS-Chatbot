---
title: UPI Autopay Integration - Bonds
deprecated: false
hidden: true
metadata:
  robots: index
---
Merchants can set up automated subscription billing through various payment methods including UPI Autopay for Bonds Payments. This section explains how to implement the `_payment` API for by Online Bond Platform Provider (OBPP) merchants to collect UPI recurring payments using seamless integration.

***

## Initiate the Consent Transaction

<PaymentAPIEnvironment />

<Accordion title="Request Parameters" icon="fa-exchange">
  | Parameter                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                               |
  | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | key<br />`mandatory`                            | `String` This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to Generate Merchant Key and Salt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 8488225                                                                                                                                                               |
  | txnid<br />`mandatory`                          | `Varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn't been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID'). | fd3e847h2                                                                                                                                                             |
  | amount<br />`mandatory`                         | `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 10                                                                                                                                                                    |
  | productinfo<br />`mandatory`                    | `Varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice).                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | T-shirt                                                                                                                                                               |
  | firstname<br />`mandatory`                      | `Varchar` This parameter must contain the first name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Ankit                                                                                                                                                                 |
  | email<br />`mandatory`                          | `Varchar` This parameter must contain the email of the customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [test@gmail.com](mailto:test@gmail.com)                                                                                                                               |
  | phone<br />`mandatory`                          | `Integer` Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.                                                                                                                                                                                                                                                                                                                                                                                                                                            | 9876543210                                                                                                                                                            |
  | pg<br />`mandatory`                             | `String` This parameter contains the payment method to be enabled to collect payment from your customer. For the list of payment methods and their codes, refer to Payment Mode Codes. For UPI, use UPI.                                                                                                                                                                                                                                                                                                                                                                                                                                     | NB                                                                                                                                                                    |
  | bankcode<br />`mandatory`                       | `string` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For UPI Autopay, use INTTPV.                                                                                                                                                                                                                                                                                                                                                                                                                                | INTTPV                                                                                                                                                                |
  | surl<br />`mandatory`                           | `string` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                             | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                                        |
  | furl<br />`mandatory`                           | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                                 | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                                        |
  | api_version<br />`mandatory`                    | API version must be posted as `21`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 21                                                                                                                                                                    |
  | si<br />`mandatory`                             | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.<br />**Notes**: You can modify or cancel existing recurring payment registration as described in the following sections: <br />\- Manage Recurring Payment for Cards <br />\- Manage UPI Recurring Transaction                                                                                                                                                                                                                   | 1                                                                                                                                                                     |
  | free_trial<br />`optional`                      | This is mandatory only if the merchant wants to support free trial use cases. In this case, PayU adjusts the transaction amount as INR 2.00 for cards and UPI and INR 0.00 for Net Banking irrespective of what amount is passed against the amount field in the request.                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                       |
  | si_details<br />`mandatory`                     | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.<br />**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0) ) This is a JSON object and it includes a set of fields. For more information, refer to SI Parameter JSON Details                                      | \{"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"\} |
  | hash<br />`mandatory`                           | `String` The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: sha512(key\\\|txnid\\\|amount\\\|productinfo\\\|firstname\\\|email\\\|udf1\\\|udf2\\\|udf3\\\|udf4\\\|udf5\\\|\\\|\\\|\\\|\\\|\\\|\\\|beneficiarydetail\\\|si_details\\\|\\\|\\\|\\\|\\\|products\\\|salt) For more information, refer to Generate Hash.                                                                                                                                                                                                                                                          | a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0                                                                                                                              |
  | products<br />`mandatory for Bonds`             | `JSON` This parameter contains various fields including the Products object (**wtParams**). For more information on Products object field, refer to the Products object section.                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Refer to the Products object section.                                                                                                                                 |
  | txn_s2s_flow <br />`mandatory`                  | `String` This parameter must be passed with the value as 4 for Decoupled flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 4                                                                                                                                                                     |
  | lastname<br />`optional`                        | `String` The last name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Sharma                                                                                                                                                                |
  | address1<br />`optional`                        | `String` The first line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 123 Main Street                                                                                                                                                       |
  | address2<br />`optional`                        | `String` The second line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Apartment 4B                                                                                                                                                          |
  | city<br />`optional`                            | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Mumbai                                                                                                                                                                |
  | state<br />`optional`                           | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Maharashtra                                                                                                                                                           |
  | country<br />`optional`                         | `String` The country where your customer resides.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | India                                                                                                                                                                 |
  | zipcode<br />`optional`                         | `String` Billing address zip code is mandatory for the cardless EMI option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 400001                                                                                                                                                                |
  | udf1<br />`mandatory for Cross-Border Payments` | `String` This parameter has been made for you to keep any information corresponding to the transaction. **Note**: This parameter must contain buyer's PAN number for Cross-Border Payments.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | ABCDE1234F                                                                                                                                                            |
  | udf2<br />`optional`                            | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 1                                                                                                                                                     |
  | udf3<br />`mandatory for Cross-Border Payments` | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | GSTIN123456                                                                                                                                                           |
  | udf4<br />`optional`                            | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 2                                                                                                                                                     |
  | udf5<br />`optional`                            | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 3                                                                                                                                                     |
  | beneficiarydetail<br />`mandatory`              | This is a JSON format text and there should be key named **beneficiaryAccountNumber** with the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key).                                                                                                                                                                                                                                                                                                                                                                                   | Refer to the beneficiarydetail JSON Object Fields section.                                                                                                            |

  <Accordion title="beneficiarydetail JSON Object Fields" icon="fa-code">
    It must contain the account number and the ifscCode key. For example:

    ```json
    {
       "beneficiaryName":"Sachin Tendulkar",
       "beneficiaryAccountNumber":"1211450021",
       "beneficiaryAccountType":"SAVINGS",
       "beneficiaryIfscCode":"ICIC0000046"
    }
    ```

    **Checksum Logic for Hash**

    The following hash logic must be used for the parameters posted:

    <Callout icon="📘" theme="info">
      ### si_details parameter in Hashing:

      The **si_details** parameter value will be at last or the last value to be appended.

      ```plaintext Hash Formula
      sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||||beneficiarydetail|si_details|||||products|salt)
      ```
    </Callout>
  </Accordion>

  #### Products Object

  <Accordion title="Sample JSON" icon="fad fa-code">
    ```json
    {
       "wtParams":[
          {
             "type":"bond",
             "amount":"1000.00",
             "receipt":"77407",
             "mf_member_id":"12345",
             "mf_user_id":"77407",
             "mf_partner":"nse_bonds",
             "mf_investment_type":"L"
          }
       ]
    }
    ```
  </Accordion>

  <Accordion title="Parameter and Description" icon="fad fa-table">
    | Parameter                                          | Required | Format                                    | Description                                    |
    | -------------------------------------------------- | -------- | ----------------------------------------- | ---------------------------------------------- |
    | `type`                                             | Yes      | String                                    | Must be `bond`.                                |
    | `mf_partner`                                       | Yes      | String                                    | Must be `nse_bonds`.                           |
    | `amount`                                           | Yes      | Numeric string — e.g. `5000` or `5000.50` | Must be equal to the order `amount`.           |
    | `receipt`                                          | Yes      | Alphanumeric, max. 25 characters          | Your unique reference number for this payment. |
    | `mf_member_id`                                     | Yes      | Max. 20 characters                        | Your member ID on the exchange.                |
    | `mf_user_id`                                       | Yes      | Alphanumeric, max. 10 characters          | Unique client code (UCC) of the customer.      |
    | `mf_investment_type`                               | Yes      | `L`                                       | Send `L` (lump sum).                           |
    | `plan`, `option`, `scheme`, `folio`, `mf_amc_code` | No       | String                                    | Not used for bonds. You can omit these fields. |
  </Accordion>

  <Accordion title="Validation Rules" icon="fad fa-code">
    | Field                          | Description                                          | Example         |
    | ------------------------------ | ---------------------------------------------------- | --------------- |
    | type                           | Must always be `"mutual_fund"`                       | `"mutual_fund"` |
    | amount                         | Must match the overall order value                   | \-              |
    | receipt                        | Must be unique across transactions                   | \-              |
    | mf_member_id                   | Must be numeric with length between 5-20 characters  | \-              |
    | mf_user_id                     | Maximum 10 characters allowed                        | \-              |
    | mf_partner                     | Must be one of: `"cams"`, `"kfin"`, `"bse"`, `"nse"` | `"cams"`        |
    | mf_investment_type             | Only `"L"` (Lump Sum) or `"S"` (SIP) allowed         | `"L"`           |
    | **Optional Field Validations** |                                                      |                 |
    | mf_amc_code                    | Maximum 5 characters                                 | \-              |
    | receipt                        | Maximum 25 characters for SIP registration ID        | \-              |
  </Accordion>

  <Accordion title="Hash Calculation" icon="fa-key">
    Concatenate fields in this exact sequence, then <Glossary>SHA</Glossary>-512:

    ```plaintext
    sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||||beneficiarydetail|si_details|||||products|salt)
    ```

    * Use empty strings for missing udf\*.
    * Compute on your server and include the lowercase hex digest as hash.

    For more information, refer to  <a href="generate-hash-payu-hosted" target="_blank"> Generate Hash</a>.
  </Accordion>
</Accordion>

<Accordion title="Sample Request" icon="fa-exchange">
  ```curl

  curl --location 'https://test.payu.in/_payment' \
  --header 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
  --header 'content-type: application/x-www-form-urlencoded' \
  --header 'Cookie: PHPSESSID=kdihrj6ld6mbevful3ii02rqme; USERTXNINFO=698071743e9724.85896500; PHPSESSID=69ba93505906f' \
  --data-urlencode 'key=j6Bb3k' \
  --data-urlencode 'txnid=Txn_098f7189' \
  --data-urlencode 'amount=50000' \
  --data-urlencode 'productinfo=Mutual Fund' \
  --data-urlencode 'firstname=John' \
  --data-urlencode 'email=john@example.com' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'pg=UPI' \
  --data-urlencode 'bankcode=INTTPV' \
  --data-urlencode 'surl=https://apiplayground-response.herokuapp.com/' \
  --data-urlencode 'furl=https://apiplayground-response.herokuapp.com/' \
  --data-urlencode 'api_version=21' \
  --data-urlencode 'hash={{hash}}' \
  --data-urlencode 'products={"wtParams":[{"type":"bond","amount":"101.00","receipt":"1234556789012","mf_member_id":"12345","mf_user_id":"77407","mf_partner":"nse_bonds","mf_investment_type":"L"}]}' \
  --data-urlencode 'txn_s2s_flow=4' \
  --data-urlencode 'beneficiarydetail={"beneficiaryAccountNumber":"1111111111","ifscCode":"111111189HSBB001"}'
  ```
</Accordion>

## Check Response from PayU

<Accordion title="Success Response" icon="fa-exchange">
  #### Initial response

  ```json
  {
      "metaData": {
          "message": null,
          "referenceId": "18bd0c0c619ec09ad676dca7bf65225f242e20a983521934215c4074cb763518",
          "statusCode": null,
          "txnId": "Txn_098f7189",
          "txnStatus": "pending",
          "unmappedStatus": "pending"
      },
      "result": {
          "paymentId": "403993715537012547",
          "merchantName": "Merchant",
          "merchantVpa": "kk.payutest@hdfcbank",
          "amount": "50000.00",
          "intentURIData": "pa=kk.payutest@hdfcbank&pn=&tr=403993715537012547&tid=PPPL4039937155370125471803261728086&am=50000.00&cu=INR&tn=UPIIntent",
          "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vdGVzdC5wYXl1LmluLzE4YmQwYzBjNjE5ZWMwOWFkNjc2ZGNhN2JmNjUyMjVmNzg5YWZjNjBmZGYzYzE1OGNhYjdhMDUxZGY4MTUzOWIvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0b2tlbiIgdmFsdWU9IjY5NjAzMEQwLUI5QTAtRTMxQS1CRUVFLTlGOEI5RDc0MDc0OCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYW1vdW50IiB2YWx1ZT0iNTAwMDAuMDAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9Im1paHBheWlkIiB2YWx1ZT0iMThiZDBjMGM2MTllYzA5YWQ2NzZkY2E3YmY2NTIyNWYyNDJlMjBhOTgzNTIxOTM0MjE1YzQwNzRjYjc2MzUxOCI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iZGlzYWJsZUludGVudFNlYW1sZXNzRmFpbHVyZSIgdmFsdWU9IjAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InBheWVlVnBhIiB2YWx1ZT0ia2sucGF5dXRlc3RAaGRmY2JhbmsiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InBheWVlTmFtZSIgdmFsdWU9Ik1lcmNoYW50Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJhZGRpdGlvbmFsQ2hhcmdlcyIgdmFsdWU9IiI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0idHJhbnNhY3Rpb25GZWUiIHZhbHVlPSI1MDAwMC4wMCI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1sncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+",
          "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
      }
  }
  ```

  <Callout icon="📘" theme="info">
    ### **Note:**

    You must redirect the customer and authorize the charges as described in Decoupled Flow Integration. For more information, refer to [Decoupled Flow Integration](doc:integrate-with-decoupled-flow-s2s). The final response is in plain text and when it is parsed, it is similar to the following [Parsed response](#parsed-response).
  </Callout>

  #### Parsed response

  ```json
  (
      [mihpayid] => 403993715537012547
      [mode] => UPI
      [status] => success
      [key] => j6Bb3k
      [txnid] => Txn_098f7189
      [amount] => 50000.00
      [addedon] => 2026-03-18 17:28:08
      [productinfo] => Mutual Fund
      [firstname] => John
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => john@example.com
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
      [card_token] => 
      [card_no] => 
      [field0] => 
      [field1] => 
      [field2] => 1773835213026
      [field3] => kk@okhdfcbank
      [field4] => 
      [field5] => HDF4MKR1WHMFEO978JSAE5FKVK3NZTC3G5PY
      [field6] => State Bank of India!098765432211!SBIN0011111!+917985392982
      [field7] => APPROVED OR COMPLETED SUCCESSFULLY|00
      [field8] => 
      [field9] => SUCCESS|Completed Using Callback
      [payment_source] => payuPureS2S
      [cardToken] => 
      [authenticaticationMethod] => 
      [PG_TYPE] => UPI-PG
      [error] => E000
      [error_Message] => No Error
      [net_amount_debit] => 50000
      [discount] => 0.00
      [offer_key] => 
      [offer_availed] => 
      [unmappedstatus] => captured
      [hash] => e14b51c229ad8853074a008bff66f4421238517ad7bd409de60b6ff63be68e7f08425c2101a0774bd57ac95ec5d63e9f385e4cb25d41fd50d8b03b3cfafb0c7d
      [bank_ref_no] => 886917606513
      [bank_ref_num] => 886917606513
      [bankcode] => INTTPV
      [surl] => https://apiplayground-response.herokuapp.com/
      [curl] => https://apiplayground-response.herokuapp.com/
      [furl] => https://apiplayground-response.herokuapp.com/
  )

  ```
</Accordion>

<Accordion title="Hash Verification" icon="fa-key">
  Verify response using reverse hash calculation:

  ```
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||||beneficiarydetail|si_details|||||products|salt
  ```
</Accordion>

***

## Verify the Payment

<Verify_Payment_Tabs />

***

## Pre-Debit Notification

<GENERALAPIsEnvironment />

<Accordion title="Request parameters" icon="fa-table">
  | Parameter      | Description                                                                                            |           |        |                                                                                                   |
  | :------------- | :----------------------------------------------------------------------------------------------------- | --------- | ------ | ------------------------------------------------------------------------------------------------- |
  | key `string`   | `mandatory` This parameter is the unique Merchant Key provided by PayU                                 |           |        |                                                                                                   |
  | var1 `object`  | The variable 1 object details.                                                                         |           |        |                                                                                                   |
  | hash `string`  | `mandatory` It is used to avoid the possibility of transaction tampering. Hash formula: \`sha512(key\\ | command\\ | var1\\ | salt)\`. Please regenerate hash at the end every time you make a change to the request parameters |
  | command `enum` | `mandatory` The command name for this REST API call is pre_debit_SI.                                   |           |        |                                                                                                   |

  <Accordion title="var1 Object parameters" icon="fa-table">
    | Parameter                     | Description                                                                                                                                                                                    |
    | :---------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | authPayuId `string`           | `mandatory` The value of mihpayid returned in the payment response of Registration transaction when transaction is successfully completed.                                                     |
    | requestId `string`            | `mandatory` Unique request value generated at merchant’s end to distinguish independent request call.                                                                                          |
    | debitDate `string`            | `mandatory` This field contains the date of debit when the recurring would be charged by merchant.                                                                                             |
    | invoiceDisplayNumber `string` | `optional` This field is required for cards. A unique display number by merchant for every subsequent invoice/recurring charge. This can be displayed on the merchant’s panel to the customer. |
    | amount `number`               | `mandatory` The transaction amount which will be deducted from the customer’s payment instrument.                                                                                              |
    | action `number`               | `optional` Pass "Retrieve" or "Delete" according to the action need to be performed. For more information, refer to Additional Information table.                                              |
  </Accordion>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data 'form=2&key=smsplus&command=pre_debit_si&var1={"authpayuid": "25600438037", "requestId": "REQ-2024-001-SEQ2", "debitDate": "2024-12-20", "amount": "100.00", "invoiceDisplayNumber": "INV-12345", "mandateSeqNo": 2}&hash=d9e184476637002a3c2db99a7324673647a313de96e574b7a9812e99153dc1a47f0f9da9b32e3a7382bb46dce09a5eb8d4471c85e1bfc1b0dac380a67ff07b43'
  ```
</Accordion>

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

***

## Initiate Recurring Payment

<GENERALAPIsEnvironment />

<Accordion title="Request parameters" icon="fa-key">
  | Parameter                | Description                                                                                                                                        | Example                                                                                                                                                                                                                                                                                                                                                                                                        |
  | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | key<br />`mandatory`     | `String` The merchant key provided by PayU                                                                                                         | JPM7Fg                                                                                                                                                                                                                                                                                                                                                                                                         |
  | command<br />`mandatory` | `String` Command to execute the recurring transaction API. Must be si_transaction                                                                  | si_transaction                                                                                                                                                                                                                                                                                                                                                                                                 |
  | var1<br />`mandatory`    | `JSON Object` JSON-format object containing transaction details and optional fields. For more information, refer to var1 object field descriptions | \{"authpayuid":"403993715537049175","invoiceDisplayNumber":"IN_403993715537049175","amount":"1","txnid":"tx_403993715537049175","phone":"9988776655","email":"[chota.bheem@gmail.com](mailto:chota.bheem@gmail.com)","more_info":\[{"wtParams":[{"type":"bond","amount":"101.00","receipt":"1234556789012","mf_member_id":"12345","mf_user_id":"77407","mf_partner":"nse_bonds","mf_investment_type":"L"}]}]\} |
  | hash<br />`mandatory`    | `String` SHA512 hash generated by concatenating key\\\|command\\\|var1\\\|salt for request authentication                                          | jbUS07Og8BToVZ                                                                                                                                                                                                                                                                                                                                                                                                 |

  ### var1 Object

  <Accordion title="Sample JSON" icon="fad fa-code">
    ```json
    {
       "authpayuid":"403993715537049175",
       "invoiceDisplayNumber":"IN_403993715537049175",
       "amount":"1",
       "txnid":"tx_403993715537049175",
       "phone":"9988776655",
       "email":"chota.bheem@gmail.com",
       "more_info":[
          {
             "wtParams":[
                {
                   "type":"bond",
                   "amount":"101.00",
                   "receipt":"1234556789012",
                   "mf_member_id":"12345",
                   "mf_user_id":"77407",
                   "mf_partner":"nse_bonds",
                   "mf_investment_type":"L"
                }
             ]
          }
       ]
    }
    ```
  </Accordion>

  <Accordion title="Parameter and Description" icon="fad fa-table">
    | Parameter                        | Description                                                                                                                             | Example                                               |
    | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
    | authpayuid `mandatory`           | `String` Authorization PayU ID (mihpayid from successful registration)                                                                  | 403993715537049175                                    |
    | invoiceDisplayNumber `mandatory` | `String` Display invoice number for the recurring charge                                                                                | IN_403993715537049175                                 |
    | amount `mandatory`               | `String` Transaction amount to be debited                                                                                               | 1                                                     |
    | txnid `mandatory`                | `String` Unique transaction ID generated by the merchant                                                                                | tx_403993715537049175                                 |
    | phone `mandatory`                | `String` Customer phone number                                                                                                          | 9988776655                                            |
    | email `mandatory`                | `String` Customer email address                                                                                                         | [chota.bheem@gmail.com](mailto:chota.bheem@gmail.com) |
    | more_info `mandatory`            | `JSON` Array containing the Products object (wtParams). Mandatory for Bonds. For wtParams field descriptions, refer to the table below. | See the above JSON                                    |
  </Accordion>

  <Accordion title="Products Object Parameters" icon="fad fa-table">
    | Parameter                                          | Required | Format                                    | Description                                    |
    | -------------------------------------------------- | -------- | ----------------------------------------- | ---------------------------------------------- |
    | `type`                                             | Yes      | String                                    | Must be `bond`.                                |
    | `mf_partner`                                       | Yes      | String                                    | Must be `nse_bonds`.                           |
    | `amount`                                           | Yes      | Numeric string — e.g. `5000` or `5000.50` | Must be equal to the order `amount`.           |
    | `receipt`                                          | Yes      | Alphanumeric, max. 25 characters          | Your unique reference number for this payment. |
    | `mf_member_id`                                     | Yes      | Max. 20 characters                        | Your member ID on the exchange.                |
    | `mf_user_id`                                       | Yes      | Alphanumeric, max. 10 characters          | Unique client code (UCC) of the customer.      |
    | `mf_investment_type`                               | Yes      | `L`                                       | Send `L` (lump sum).                           |
    | `plan`, `option`, `scheme`, `folio`, `mf_amc_code` | No       | String                                    | Not used for bonds. You can omit these fields. |
  </Accordion>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location 'https://test.payu.in/merchant/postservice?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --header 'Cookie: PHPSESSID=69c253779decd' \
  --data-urlencode 'key=j6Bb3k' \
  --data-urlencode 'command=si_transaction' \
  --data-urlencode 'hash={{hash}}' \
  --data-urlencode 'var1={"authpayuid":"403993715537049175","invoiceDisplayNumber":"IN_403993715537049175","amount":"1","txnid":"tx_403993715537049175","phone":"9988776655","email":"chota.bheem@gmail.com","more_info":[{"wtParams":[{"type":"mutual_fund","plan":"GD","amount":"1000.00","option":"G","scheme":"LT","receipt":"77407","mf_member_id":"12345","mf_user_id":"77407","mf_partner":"cams","mf_investment_type":"L","mf_amc_code":"UTB"}]}]}'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
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
</Accordion>