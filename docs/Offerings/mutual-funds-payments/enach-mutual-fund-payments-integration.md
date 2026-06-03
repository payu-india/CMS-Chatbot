---
title: ENACH Integration -Mutual Funds
deprecated: false
hidden: true
metadata:
  robots: index
---
Merchants can set up automated subscription billing through various payment methods including Net Banking (e-NACH) for Mutual Fund Payments. This section describes how to integrate mutual fund subscription for ENACH using seamless integration.

<Cards columns={2}>
  <Card title="1. Consent Transaction" href="#step-1-consent-transaction">
    Initiate the recurring payment process by capturing user consent for the mandate with required parameters including key, txnid, amount, productinfo, customer details, and si\_details JSON object

    <br />
  </Card>

  <Card title="2. Verify the Payment" href="#step-2-verify-the-payment">
    Ensure the initial consent transaction or registration is successfully processed before proceeding with recurring charges

    <br />
  </Card>

  <Card title="3. Recurring Payment Transaction" href="#step-3-recurring-payment-transaction">
    Execute recurring payments automatically without additional customer involvement using server-to-server integration with authpayuid and invoiceDisplayNumber

    <br />
  </Card>

  <br />
</Cards>

## Step 1: Consent Transaction

HTTP Method: **POST**

**Environment**

|                        |                                                                     |
| :--------------------- | :------------------------------------------------------------------ |
| Test Environment       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |
| Production Environment | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |

<Accordion title="Request Parameters" icon="fa-table">
  | Parameter                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Example                                                                                                                                                                     |
  | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | key<br />`mandatory`                            | `String` This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to Generate Merchant Key and Salt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | 8488225                                                                                                                                                                     |
  | txnid<br />`mandatory`                          | `Varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant's) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn't been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID'). | fd3e847h2                                                                                                                                                                   |
  | amount<br />`mandatory`                         | `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | 10                                                                                                                                                                          |
  | productinfo<br />`mandatory`                    | `Varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice).                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | T-shirt                                                                                                                                                                     |
  | firstname<br />`mandatory`                      | `Varchar` This parameter must contain the first name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Ankit                                                                                                                                                                       |
  | email<br />`mandatory`                          | `Varchar` This parameter must contain the email of the customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | [test@gmail.com](mailto:test@gmail.com)                                                                                                                                     |
  | phone<br />`mandatory`                          | `Integer` Merchant needs to take the customer's GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.                                                                                                                                                                                                                                                                                                                                                                                                                                            | 9876543210                                                                                                                                                                  |
  | pg<br />`mandatory`                             | `String` This parameter contains the payment method to be enabled to collect payment from your customer. For the list of payment methods and their codes, refer to Payment Mode Codes. For ENACH, use ENACH.                                                                                                                                                                                                                                                                                                                                                                                                                                 | ENACH                                                                                                                                                                       |
  | bankcode<br />`mandatory`                       | `string` Each payment option is identified with a unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For the list of bankcodes for Net Banking, refer to (Net Banking Codes)\[doc:bank-codes-recurring-payments].                                                                                                                                                                                                                                                                                                                                                | ICICENCC                                                                                                                                                                    |
  | surl<br />`mandatory`                           | `string` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                             | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                                              |
  | furl<br />`mandatory`                           | `String` The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.                                                                                                                                                                                                                                                                                                                                                                                                                                 | [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)                                                                              |
  | api\_version<br />`mandatory`                   | API version must be posted as `21`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | 21                                                                                                                                                                          |
  | si<br />`mandatory`                             | This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.<br />**Notes**: You can modify or cancel existing recurring payment registration as described in the following sections: <br />- Manage Recurring Payment for Cards <br />- Manage UPI Recurring Transaction                                                                                                                                                                                                                     | 1                                                                                                                                                                           |
  | free\_trial<br />`optional`                     | This is mandatory only if the merchant wants to support free trial use cases. In this case, PayU adjusts the transaction amount as INR 2.00 for cards and UPI and INR 0.00 for Net Banking irrespective of what amount is passed against the amount field in the request.                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                             |
  | si\_details<br />`mandatory`                    | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.<br />**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer [https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0](https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668\&Mode=0) ) This is a JSON object and it includes a set of fields. For more information, refer to SI Parameter JSON Details                                      | \{"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"\}        |
  | hash<br />`mandatory`                           | `String` The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: sha512(key\\\|txnid\\\|amount\\\|productinfo\\\|firstname\\\|email\\\|udf1\\\|udf2\\\|udf3\\\|udf4\\\|udf5\\\|\\\|\\\|\\\|\\\|\\\|\\\|beneficiarydetail\\\|si\_details\\\|\\\|\\\|\\\|\\\|products\\\|salt) For more information, refer to Generate Hash.                                                                                                                                                                                                                                                                | a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0                                                                                                                                    |
  | products<br />`mandatory for Wealth Tech`       | `JSON` This parameter contains various fields including the Wealth Tech object (**wtParams**). For more information on wtParams object field, refer to [Wealth Tech object wtparams fields description](https://docs.payu.in/docs/enach-mutual-fund-payments-integration#wealth-tech-object-wtparams-fields-description).                                                                                                                                                                                                                                                                                                                    | Refer to [Wealth Tech object wtparams fields description](https://docs.payu.in/docs/enach-mutual-fund-payments-integration#wealth-tech-object-wtparams-fields-description). |
  | txn\_s2s\_flow <br />`mandatory`                | `String` This parameter must be passed with the value as 4 for Decoupled flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | 4                                                                                                                                                                           |
  | lastname<br />`optional`                        | `String` The last name of the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Sharma                                                                                                                                                                      |
  | address1<br />`optional`                        | `String` The first line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 123 Main Street                                                                                                                                                             |
  | address2<br />`optional`                        | `String` The second line of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Apartment 4B                                                                                                                                                                |
  | city<br />`optional`                            | `String` The city where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Mumbai                                                                                                                                                                      |
  | state<br />`optional`                           | `String` The state where your customer resides as part of the billing address.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Maharashtra                                                                                                                                                                 |
  | country<br />`optional`                         | `String` The country where your customer resides.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | India                                                                                                                                                                       |
  | zipcode<br />`optional`                         | `String` Billing address zip code is mandatory for the cardless EMI option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | 400001                                                                                                                                                                      |
  | udf1<br />`mandatory for Cross-Border Payments` | `String` This parameter has been made for you to keep any information corresponding to the transaction. **Note**: This parameter must contain buyer's PAN number for Cross-Border Payments.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | ABCDE1234F                                                                                                                                                                  |
  | udf2<br />`optional`                            | `string` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 1                                                                                                                                                           |
  | udf3<br />`mandatory for Cross-Border Payments` | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | GSTIN123456                                                                                                                                                                 |
  | udf4<br />`optional`                            | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 2                                                                                                                                                           |
  | udf5<br />`optional`                            | `String` This parameter has been made for you to keep any information corresponding to the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Additional Info 3                                                                                                                                                           |
  | beneficiarydetail<br />`mandatory`              | This is a JSON format text and there should be key named **beneficiaryAccountNumber** with the list of account numbers and the ifscCode key with the list of corresponding IFSC codes (in the same order as provided in the beneficiaryAccountNumber key). You can post up to five account details in this parameter.                                                                                                                                                                                                                                                                                                                        | Refer to the beneficiarydetail JSON Object Fields section.                                                                                                                  |

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

  #### Wealth Tech Object wtparams Fields Description

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

  <Callout icon="📘" theme="info">
    *Note*:  You must redirect the customer and authorize the charges as described in Decoupled Flow Integration. For more information, refer to [Decoupled Flow Integration](doc:integrate-with-decoupled-flow-s2s). The final response is in plain text and when it is parsed, it is similar to the following [Parsed response](#parsed-response).
  </Callout>

  #### Parsed response

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

## Step 4: Recurring Payment Transaction

All successful registration transactions are charged over the recurring interface with server-to-server API without any additional 2FA or the customers' involvement.

> 📘 **Notes**:
>
> - Banks do not support refunds for Net Banking Recurring Payment transactions (or e-NACH transaction) so you will get an error message, "Refund not accepted for txn" or Error 232. For the list of banks supporting e-NACH, refer to Recurring Payments Bank Codes.
> - Check the mandate status, call the **Pre-Debit Notification** API before calling the **Recurring Payment Transaction** API to make a recurring payment transaction.

> 🚧 **Assumptions**: If the merchant has already performed a successful registration transaction with Net Banking/UPI/Card and mihpayid is received in response to the registration transaction captured successfully and mapped to the customer at the merchant's end.

**Environment**

|                        |                                                                  |
| :--------------------- | :--------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/merchant/](https://info.payu.in/merchant/) |
| Test Environment       | [https://test.payu.in/merchant/](https://test.payu.in/merchant/) |

<Accordion title="Request parameters" icon="fa-key">
  | Parameter                                 | Description                                                                                                                                                                                                                                                | Example                                                                                                                                                                               |
  | ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | key<br />`mandatory`                      | `String` The merchant key provided by PayU                                                                                                                                                                                                                 | JPM7Fg                                                                                                                                                                                |
  | command<br />`mandatory`                  | `String` Command to execute the recurring transaction API. Must be si\_transaction                                                                                                                                                                         | si\_transaction                                                                                                                                                                       |
  | var1<br />`mandatory`                     | `JSON Object` JSON-format object containing transaction details and optional fields. For more information, refer to [var1 object field descriptions](https://docs.payu.in/docs/enach-mutual-fund-payments-integration#var1-object-field-descriptions) | \{"authpayuid":"403993715537049175","invoiceDisplayNumber":"IN_403993715537049175","amount":"1","txnid":"tx_403993715537049175","phone":"9988776655","email":"chota.bheem@gmail.com","more_info":[{"wtParams":[{"type":"mutual_fund","plan":"GD","amount":"1000.00","option":"G","scheme":"LT","receipt":"77407","mf_member_id":"12345","mf_user_id":"77407","mf_partner":"cams","mf_investment_type":"L","mf_amc_code":"UTB"}]}]\} |
  | hash<br />`mandatory`                     | `String` SHA512 hash generated by concatenating key\\\|command\\\|var1\\\|salt for request authentication                                                                                                                                                  | jbUS07Og8BToVZ                                                                                                                                                                        |

  <Accordion title="var1 object field descriptions" icon="fa-cog">
    ### var1 object field descriptions

    <HTMLBlock>{/*RDMX_HTMLBLOCK:CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIDx0YWJsZSBpZD0idmFyMS1wYXJhbWV0ZXJzIj4gPHRyPiA8dGg+UGFyYW1ldGVyPC90aD4gPHRoPkRlc2NyaXB0aW9uPC90aD4gPHRoPkV4YW1wbGU8L3RoPiA8L3RyPiA8dHI+IDx0ZCBjb2xzcGFuPSIzIj48c3Ryb25nPkZpZWxkcyB3aXRoaW4gdGhlIHZhcjEgSlNPTiBvYmplY3Q8L3N0cm9uZz4gLSA8YSBocmVmPSIjbWFpbi1wYXJhbWV0ZXJzIj5CYWNrIHRvIG1haW4gcGFyYW1ldGVyczwvYT48L3RkPiA8L3RyPiA8dHI+IDx0ZD5hdXRocGF5dWlkIDxici8+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvdGQ+IDx0ZD48Y29kZT5TdHJpbmc8L2NvZGU+IC0gQXV0aG9yaXphdGlvbiBQYXlVIElEPC90ZD4gPHRkPjQwMzk5MzcxNTUzNzA0OTE3NTwvdGQ+IDwvdHI+IDx0cj4gPHRkPmludm9pY2VEaXNwbGF5TnVtYmVyIDxici8+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvdGQ+IDx0ZD48Y29kZT5TdHJpbmc8L2NvZGU+IC0gRGlzcGxheSBpbnZvaWNlIG51bWJlcjwvdGQ+IDx0ZD5JTl80MDM5OTM3MTU1MzcwNDkxNzU8L3RkPiA8L3RyPiA8dHI+IDx0ZD5hbW91bnQgPGJyLz48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC90ZD4gPHRkPjxjb2RlPlN0cmluZzwvY29kZT4gLSBUcmFuc2FjdGlvbiBhbW91bnQ8L3RkPiA8dGQ+MTwvdGQ+IDwvdHI+IDx0cj4gPHRkPnR4bmlkIDxici8+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvdGQ+IDx0ZD48Y29kZT5TdHJpbmc8L2NvZGU+IC0gVHJhbnNhY3Rpb24gSUQgZ2VuZXJhdGVkIGJ5IHRoZSBtZXJjaGFudDwvdGQ+IDx0ZD50eF80MDM5OTM3MTU1MzcwNDkxNzU8L3RkPiA8L3RyPiA8dHI+IDx0ZD5waG9uZSA8YnIvPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3RkPiA8dGQ+PGNvZGU+U3RyaW5nPC9jb2RlPiAtIEN1c3RvbWVyJ3MgcGhvbmUgbnVtYmVyPC90ZD4gPHRkPjk5ODg3NzY2NTU8L3RkPiA8L3RyPiA8dHI+IDx0ZD5lbWFpbCA8YnIvPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3RkPiA8dGQ+PGNvZGU+U3RyaW5nPC9jb2RlPiAtIEN1c3RvbWVyJ3MgZW1haWwgYWRkcmVzczwvdGQ+IDx0ZD5jaG90YS5iaGVlbUBnbWFpbC5jb208L3RkPiA8L3RyPiA8dHI+IDx0ZD5tb3JlX2luZm8gPGJyLz48Y29kZT5tYW5kYXRvcnkgZm9yIFdlYWx0aCBUZWNoPC9jb2RlPjwvdGQ+IDx0ZD48Y29kZT5KU09OPC9jb2RlPiAtIEFycmF5IGNvbnRhaW5pbmcgdGhlIFdlYWx0aCBUZWNoIG9iamVjdCAoPGNvZGU+d3RQYXJhbXM8L2NvZGU+KS4gRm9yIGZpZWxkIGRlc2NyaXB0aW9ucywgcmVmZXIgdG8gPGEgaHJlZj0iI3dlYWx0aC10ZWNoLW9iamVjdC13dHBhcmFtcy1maWVsZHMtZGVzY3JpcHRpb24iPldlYWx0aCBUZWNoIG9iamVjdCAod3RQYXJhbXMpIGZpZWxkcyBEZXNjcmlwdGlvbjwvYT48L3RkPiA8dGQ+W3sid3RQYXJhbXMiOlt7InR5cGUiOiJtdXR1YWxfZnVuZCIsInBsYW4iOiJHRCIsImFtb3VudCI6IjEwMDAuMDAiLC4uLn1dfV08L3RkPiA8L3RyPiA8dHI+IDx0ZD51ZGYyIDxici8+PGNvZGU+b3B0aW9uYWw8L2NvZGU+PC90ZD4gPHRkPjxjb2RlPlN0cmluZzwvY29kZT4gLSBVc2VyLWRlZmluZWQgZmllbGQgZm9yIGFkZGl0aW9uYWwgaW5mb3JtYXRpb248L3RkPiA8dGQ+IiI8L3RkPiA8L3RyPiA8dHI+IDx0ZD51ZGYzIDxici8+PGNvZGU+b3B0aW9uYWw8L2NvZGU+PC90ZD4gPHRkPjxjb2RlPlN0cmluZzwvY29kZT4gLSBVc2VyLWRlZmluZWQgZmllbGQgZm9yIGFkZGl0aW9uYWwgaW5mb3JtYXRpb248L3RkPiA8dGQ+IiI8L3RkPiA8L3RyPiA8dHI+IDx0ZD51ZGY0IDxici8+PGNvZGU+b3B0aW9uYWw8L2NvZGU+PC90ZD4gPHRkPjxjb2RlPlN0cmluZzwvY29kZT4gLSBVc2VyLWRlZmluZWQgZmllbGQgZm9yIGFkZGl0aW9uYWwgaW5mb3JtYXRpb248L3RkPiA8dGQ+IiI8L3RkPiA8L3RyPiA8dHI+IDx0ZD51ZGY1IDxici8+PGNvZGU+b3B0aW9uYWw8L2NvZGU+PC90ZD4gPHRkPjxjb2RlPlN0cmluZzwvY29kZT4gLSBVc2VyLWRlZmluZWQgZmllbGQgZm9yIGFkZGl0aW9uYWwgaW5mb3JtYXRpb248L3RkPiA8dGQ+IiI8L3RkPiA8L3RyPiA8L3RhYmxlPiAKICAgIA==:RDMX_HTMLBLOCK*/}</HTMLBlock>
  </Accordion>
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
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
  ```json
  {
      "status": 1,
      "message": "Transaction Processed successfully",
      "details": {
          "tx_403993715537049175": {
              "authpayuid": "403993715537049175",
              "transactionid": "tx_403993715537049175",
              "amount": "1",
              "user_credentials": "j6Bb3k:txn_235898u",
              "card_token": "",
              "payuid": "403993715537049210",
              "status": "captured",
              "udf1": "",
              "field9": "Payment Successful",
              "udf2": "",
              "udf3": "",
              "udf4": "",
              "udf5": "",
              "phone": "9988776655",
              "email": "chota.bheem@gmail.com",
              "fileName": "",
              "paymentgatewayid": 268,
              "addedon": "2026-03-24 14:36:23",
              "card_no": null
          }
      }
  }
  ```
</Accordion>

<Accordion title="Response Parameters" icon="fa-table">
  **JSON fields description of the Details parameter**

  | JSON Field                                | Description                                                                                                                                                                                     |                                                          |
  | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
  | transactionid                             | This field contains the value of transaction ID parameter which is echoed back in the response. This is unique transaction ID generated by merchant during calling recurring API.               |                                                          |
  | amount                                    | This field contains the requested transaction amount is echoed back in the payment response.                                                                                                    |                                                          |
  | payuid                                    | This field contains the PayU's transaction ID for processed recurring transaction. Merchant can use this field for reference point in the settlement report.                                    |                                                          |
  | status                                    | This field gives the status of the transaction. Hence, the value of this field depends on whether the transaction was successful or not.                                                        |                                                          |
  | field9                                    | This field returns the description of transaction status which can help the merchant in providing better customer communication.                                                                |                                                          |
  | phone                                     | The mobile number of the customer echoed back.                                                                                                                                                  |                                                          |
  | email                                     | Email ID of the customer echoed back.                                                                                                                                                           |                                                          |
  | udf1                                      | Extra information received in the request echoed back.                                                                                                                                          |                                                          |
  | udf2                                      | Extra information received in the request echoed back.                                                                                                                                          |                                                          |
  | udf3                                      | Extra information received in the request echoed back.                                                                                                                                          |                                                          |
  | udf4                                      | Extra information received in the request echoed back.                                                                                                                                          |                                                          |
  | udf5                                      | Extra information received in the request echoed back.                                                                                                                                          |                                                          |

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

<br />
