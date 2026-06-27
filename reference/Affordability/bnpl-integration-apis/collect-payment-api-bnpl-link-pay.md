---
title: Collect Payment API - BNPL Link & Pay
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can collect payments with BNPL using Link and Pay. This section provides the request and response parameter with sample request and response..For more information on integration, refer to [Collect Payments with BNPL using Link and Pay](doc:collect-payments-with-bnpl-using-link-and-pay).

<Payment_Environment />

## Request parameters

<Callout icon="📘" theme="info">
  ### Reference

  For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Callout>

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
        <Glossary>key</Glossary>
        `mandatory`
      </td>

      <td>
        `String` This parameter is the unique merchant key provided by PayU for your merchant account. For more information, refer to [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).
      </td>

      <td>
        8488225
      </td>
    </tr>

    <tr>
      <td>
        txnid<br />`mandatory`
      </td>

      <td>
        `varchar` This parameter is known as Transaction ID (or OrderID). It is the order reference number generated at your (Merchant’s) end. It is an identifier which you(merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of same Transaction ID again would fail. Hence, it is essential that you post us a unique transaction ID for every new transaction (Please make sure that the transaction ID being sent to us hasn’t been successful earlier. In case of this duplication, the customer would get an error of ‘duplicate Order ID’).
      </td>

      <td>
        fd3e847h2
      </td>
    </tr>

    <tr>
      <td>
        amount<br />`mandatory`
      </td>

      <td>
        `float` This parameter should contain the payment amount of the particular transaction. Note: Type-cast the amount to float type
      </td>

      <td>
        10
      </td>
    </tr>

    <tr>
      <td>
        productinfo<br />`mandatory`
      </td>

      <td>
        `varchar` This parameter should contain a brief product description. It should be a string describing the product (The description type is entirely your choice).
      </td>

      <td>
        T-shirt
      </td>
    </tr>

    <tr>
      <td>
        firstname<br />`mandatory`
      </td>

      <td>
        `varchar` This parameter must contain the first name of the customer.
      </td>

      <td>
        Ankit
      </td>
    </tr>

    <tr>
      <td>
        email<br />`mandatory`
      </td>

      <td>
        `varchar` This parameter must contain the email of the customer)
      </td>

      <td>
        [test@gmail.com](mailto:test@gmail.com)
      </td>
    </tr>

    <tr>
      <td>
        phone<br />`mandatory`
      </td>

      <td>
        `integer` Merchant needs to take the customer’s GPay registered phone number and pass in this field. This field will be used for further mapping the customer VPA and initiate a collect request.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        <Glossary>pg</Glossary><br />`mandatory`
      </td>

      <td>
        `string` The payment gateway is specified in this parameter. For BNPL,  specifiy **BNPL**.
      </td>

      <td>
        QR
      </td>
    </tr>

    <tr>
      <td>
        <Glossary>bankcode</Glossary><br />`mandatory`
      </td>

      <td>
        `string` Each payment option is identified with a unique bank code at PayU. You must use any of the following bank code for BNPL:

        - **LAZYPAY** for accepting payments with LAZYPAY card.
        - **SIMPL** for accepting payments with Simpl
      </td>

      <td>
        UPIQR
      </td>
    </tr>

    <tr>
      <td>
        surl<br />`mandatory`
      </td>

      <td>
        `string` The "surl" field is the success URL, which is the page PayU will redirect to if the transaction is successful. The merchant can handle the response at this URL after the customer is redirected there.
      </td>

      <td>
        [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)
      </td>
    </tr>

    <tr>
      <td>
        furl<br />`mandatory`
      </td>

      <td>
        `string`The "furl" field is the Failure URL, which is the page PayU will redirect to if the transaction is failed. The merchant can handle the response at this URL after the customer is redirected there.
      </td>

      <td>
        [https://apiplayground-response.herokuapp.com/](https://apiplayground-response.herokuapp.com/)
      </td>
    </tr>

    <tr>
      <td>
        storecard\_token\_type<br />`mandatory for Saved cards`
      </td>

      <td>
        `string`This parameter is used to specify the store card token type. For this scenario, you must include 0.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        store\_card\_token<br />`mandatory for Saved cards`
      </td>

      <td>
        `string`  This must include the token generated by PayU for the payment instrument.

        - _Note_\*: Either pass PayU token or user credentials with mobile number for customer identification
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        txn\_s2s\_flow<br />`mandatory`
      </td>

      <td>
        `string`This parameter must contain the value as 4 for Link & Pay
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        LinkAndPayFlowType<br />`mandatory`
      </td>

      <td>
        `string`This parameter must contain any of the following:

        - **1**:  auto-debit will be preferred if customer is found already linked for the payment instrument basis result of the API and final captured / failure response will be returned
        - **0**:  the request will be considered as a standard native OTP request and transaction in progress response will be returned with OTP sent to the customer by the issuer
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        LinkAndPayFlowDetails<br />`mandatory`
      </td>

      <td>
        This field is to include additional details are required from merchant for any payment instrument.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        user\_credentials<br />`mandatory`
      </td>

      <td>
        `string`This parameter must contain an unique user credential mapped against each user, to be passed by the merchant.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        <Glossary>hash</Glossary><br />`mandatory`
      </td>

      <td>
        `string` The hash calculated by the merchant using the key and salt provided by PayU. The format for calculating the hash: \`\`\`
        sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)

        `For more information, refer to [Generate Hash](doc:hashing-request-and-response).`
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        lastname<br />`optional`
      </td>

      <td>
        `string`The last name of the customer.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        address1<br />`optional`
      </td>

      <td>
        `string`The first line of the billing address.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        address2<br />`optional`
      </td>

      <td>
        `string`The second line of the billing address.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        city<br />`optional`
      </td>

      <td>
        `string`The city where your customer resides as part of the billing address.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        state<br />`optional`
      </td>

      <td>
        `string`The state where your customer resides as part of the billing address,
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        country<br />`optional`
      </td>

      <td>
        `string`The country where your customer resides.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        zipcode<br />`optional`
      </td>

      <td>
        `string`Billing address zip code is mandatory for the cardless EMI option.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf1
      </td>

      <td>
        `string`This parameter has been made for you to keep any information corresponding to the transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf2<br />`optional`
      </td>

      <td>
        `string` This parameter has been made for you to keep any information corresponding to the transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf3<br />`optional`
      </td>

      <td>
        `string` This parameter has been made for you to keep any information corresponding to the transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf4<br />`optional`
      </td>

      <td>
        `string` This parameter has been made for you to keep any information corresponding to the transaction.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        udf5<br />`optional`
      </td>

      <td>
        `string` This parameter has been made for you to keep any information corresponding to the transaction.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

<Callout icon="📘" theme="info">
  ### Note:

  Collecting the information for the following parameters from customers is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is required to provide the correct information:

  - email
  - phone
  - address1
  - s2s\_client\_ip
  - s2s\_device\_info
</Callout>

## Sample request

```
curl --request POST \
     --url https://test.payu.in/_payment \
     --header 'accept: application/json' \
     --header 'content-type: application/x-www-form-urlencoded' \
     --data key=JPM7Fg \
     --data pg=BNPL \
     --data txn_s2s_flow=4 \
     --data LinkAndPayFlowType=1 \
     --data LinkAndPayFlowDetails=1 \
     --data txnid=951bccfde0ac54f75612 \
     --data amount=100 \
     --data productinfo=Product Info \
     --data firstname=Ashish \
     --data 'email=test@example.com,' \
     --data phone=9123412345 \
     --data surl=https://apiplayground-response.herokuapp.com/ \
     --data furl=https://apiplayground-response.herokuapp.com/ \
     --data hash=02647d079d45737aede205a5bf0060ffcf32b5104facebaf901b479b958d80a0e0e88c9edd4f5c9a0576c7bc1688cce15957759029a0e58f5699b8a696c98d10 \
     --data user_credentials=abc:xyz
```

## Response parameters

### First Time User Flow

This is the case where customer has not linked his payment instrument to your user account and will need to authenticate to complete the linking:

```
{ "metaData": { "message": null, "referenceId": "748e033af87f1bb7b6aefd405bec9473", "statusCode": null, "txnId": "951bccfde0ac54f75612", "txnStatus": "pending", "unmappedStatus": "pending" }, "result": { "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vc2VjdXJlLnBheXUuaW4vX3BheW1lbnRfb3B0aW9ucz9taWhwYXlpZD03NDhlMDMzYWY4N2YxYmI3YjZhZWZkNDA1YmVjOTQ3MyZyZXNlbmRFbGlnaWJpbGl0eVJlcz0zNTk0YzczYjE4ZjdjYTllODE0NmYwYmIzZDBiZDg0MjllNWEyMGMyZjYxZDc3OGJmZDBmYjRiMGQ0MzBlYmQyMWE4ZDhmZjIwZTc3NzU4YzkwM2E3MWZlMjJkMzlkMTQ5NDEyNzAzNGVkN2Q1MDUyMzdjYjZmN2JmODBjYzMxMDdhMDJjYmQyMjIxN2MxOWY2NjYyZWZhYzhlOGY4M2RjYTkwMjQ3MGE5ODFiZGQwYTBjMDM4NDdkNTQ2ZjQxYWQ4ZjMwNjZiMmNjYzhhMzU5ZTAzMDMyOTUzZjM2MTEyZDBlNTUxZWMxOWJhNzE5NTRkZmU3ODhkMThhMjhhYzc2MDliYTUzYmQ3NzU0OGNmZmI4MTg4MjM0N2ZjOGI5NzMxNTUwOWFmZGY4YTA4OTQ0NDNjZjkxZTBiMWZkZTg0NTk0YmVlNmZjOWQzOWRhODg0ZjMwMjFlYjIyMjQ2MThlMmM3ZjExNWEwMjA1NzA1MTk4NzIyMGVjNzg2NGVjYzQ0YTAxMjQxN2U0ODgwYjE4N2VlMWYxMjM2M2EyNWE0YmEzNmQ3YjI5MjcxNmUyYjNiNDkzZDhlNzAxNGNiOTIyM2Q1YmUzNjg4N2YyYzViNTNkNTI1MjM1NWU4MjA5NTBiMzllZDk3OWNiMzY3ZTVlNDc0YzBiMTVjOTJjNzJiOWE2Y2E3MTk0OWQ2YTYyYTNjYTlmNDMyY2VjMDY0MWY5ODIyYmM4OGI2NTUwODcwZGU5ZTE4MzQxMGY3YzI0YmVlYjk1ZjNjMTkzN2ZjN2U4N2YzZDRjYmVjNWEyYTFmNiIgbWV0aG9kPSJwb3N0Ij48L2Zvcm0+PHNjcmlwdCB0eXBlPSd0ZXh0L2phdmFzY3JpcHQnPgogICAgICAgICAgICAgICAgICAgICAgICAgICAgd2luZG93Lm9ubG9hZD1mdW5jdGlvbigpewogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRvY3VtZW50LmZvcm1zWydwYXltZW50X3Bvc3QnXS5zdWJtaXQoKTsKICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICAgICAgICAgPC9zY3JpcHQ+PC9ib2R5PjwvaHRtbD4=", "otpPostUrl": "https:\\/\\/secure.payu.in\\/ResponseHandler.php" } } 
```

#### Handling Payment Response

This sub-section describes the components of the payment response received with Native OTP or Zero Redirection flow. It contains the metaData and result JSON as described in this subsection:

### metaData JSON Fields Description

| **Field**      | **Description**                                                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| message        | This field contains any additional message about the transaction.                                                                                                                  |
| referenceId    | This field contains the reference ID of the transaction.                                                                                                                           |
| statusCode     | This field contains the status code for the transaction.                                                                                                                           |
| txnId          | This field contains the transaction ID of the transaction that was posted in the request.                                                                                          |
| unmappedStatus | This field contains the unmapped status of the transaction. For more information, refer to [Status Explanations](https://devguide.payu.in/api/miscellaneous/status-explanations/). |

#### Decrypted ACS template

The result JSON contains the acsTemplate with base64 encoding.

| Field          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mihpayid       | It is a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| mode           | This parameter describes the payment category by which the transaction was completed or attempted by the customer. For the payment categories, refer to [Payment Mode Codes](https://devguide.payu.in/merchant-integration/bank-and-card-codes-for-integration/payment-mode-codes/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| status         | This parameter gives the status of the transaction as either success, failed or pending. Possible values: success, failure, pending If the value of the ‘status’ parameter is ’success’, the transaction is successful. If the value of ‘status’ is ‘failure’ or ‘pending’, must be treated as a failed transaction only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| key            | This parameter contains the merchant key for the merchant’s account at PayU. It would be the same as the key used while the transaction request is being posted from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| txnid          | This parameter would contain the transaction ID value posted by the merchant during the transaction request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| amount         | This parameter would contain the original amount which was sent in the transaction request by the merchant.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| productinfo    | This parameter would contain the same value of product information which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| firstname      | This parameter would contain the same value of first name which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| lastname       | This parameter would contain the same value of last name which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| email          | This parameter would contain the same value of email which was sent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| phone          | This parameter would contain the same value of phone which was sent in the transaction request from the merchant’s end to PayU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| udf            | This parameter would contain the same value of udf values that were sent in the transaction request from the merchant’s end to PayU. It ranges from udf1 to udf5.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| hash           | PayU calculates the hash using a string of other parameters and returns it to the merchant. The merchant must verify the hash, and only then mark a transaction as success/failure. This is to make sure that the transaction hasn’t been tampered with. The calculation is as follows: sha512(SALT\|status\|udf5\|udf4\|udf3\|udf2\|udf1\|email\|firstname\|productinfo\|amount\|txnid\|key)    <br />**Note**: The handling of udf1 – udf5 parameters remains similar to the hash calculation when the merchant sends it in the transaction request to PayU. If any of the udf (udf1-udf5) was posted in the transaction request, it must be taken in hash calculation also. If none of the udf parameters were posted in the transaction request, they should be left empty in the hash calculation too. |
| error          | For the failed transactions, this parameter provides the reason for  failure.    <br />**Note**: The reason for failure depends upon the error codes provided by different banks and hence the detailing of error reasons may differ from one transaction to another. The merchant can use this parameter to retrieve the reason for failure for a particular transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| bankcode       | This parameter contains the code indicating the payment option used for the transaction. For example, in the Debit Card mode, there are different options like Visa Debit Card, Mastercard, Maestro etc. For each option, a unique bank code exists. It would be returned in this bank code parameter. For example, Visa Debit Card – VISA, Master Debit Card – MAST.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PG\_TYPE       | This parameter gives information on the payment gateway used for the transaction. For example, if CC PG was used, it would contain the value CC-PG. Similarly, it would have a unique value for all different types of payment gateways.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| bank\_ref\_num | For each successful transaction – this parameter would contain the bank reference number generated by the bank.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| unmappedstatus | This parameter contains the status of a transaction as per the internal database of PayU. PayU’s system has several intermediate status which are used for tracking various activities internal to the system. For more information, refer to [Status Explanations](https://devguide.payu.in/api/miscellaneous/status-explanations/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| customerLinked | This parameter contains the status of the customer linking on the merchant. The values can be: <br /><br />True: If customer is linked  <br /><br />False: If customer is not linked                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| payuToken      | This is the value of the payu token which is mapped against a payment instrument                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

<Callout icon="📘" theme="info">
  ### Requesting OTP:

  To request OTP on a page, you can utilize the URLs in the response itself. There are two URLs to use:

  - otpPostUrl (Merchant Hosted OTP page)
  - acsTemplate (PayU Hosted OTP page) which acts as a fallback

  If you are getting a URL in otpPostUrl, use otpPostUrl, otherwise, you can use acsTemplate, which acts as a fallback. In this scenario, use PayU (or WebView or Checkout) OTP page as this is a fallback case.

  Hence, for cases where the above response is not successful, it could either be Failed or Pending. In the Pending state, you can send a fallback URL (as above) which can be shown to the customer.
</Callout>

## Sample response

### Success scenario

<Callout icon="🚧" theme="warn">
  ### Error Handling:

  A list of error\_message with corresponding error code and reason for the error is listed in . PayU recommends you to handle these errors when you process the transactions. For more information, refer to [Error Codes for - S2S Link and Pay](ref:error-codes-for-s2s-link-and-pay).
</Callout>

- Repeat User Flow: Auto-debit Successful

This is the case where Customer’s account is liked & Auto debit is also successful

```
{
  "metaData": {
    "message": "No Error",
    "referenceId": "748e033af87f1bb7b6aefd405bec9473",
    "statusCode": "E000",
    "txnId": "951bccfde0ac54f75612",
    "unmappedStatus": "success",
    "submitOtp": {
      "status": "success"
    }
  },
  "result": {
    "link_and_pay": {
      "customerLinked": "true",
      "payuToken": "token12345"
    },
    "mihpayid": "18828133385",
    "mode": "BNPL",
    "status": "success",
    "key": "smsplus",
    "txnid": "951bccfde0ac54f75612",
    "amount": "2.00",
    "addedon": "2023-12-27 18:13:41",
    "productinfo": "Product Info",
    "firstname": "Ashish",
    "lastname": "",
    "address1": "",
    "address2": "",
    "city": "",
    "state": "",
    "country": "",
    "zipcode": "",
    "email": "test@example.com",
    "phone": "9123412345",
    "udf1": "",
    "udf2": "",
    "udf3": "",
    "udf4": "",
    "udf5": "",
    "udf6": "",
    "udf7": "",
    "udf8": "",
    "udf9": "",
    "udf10": "",
    "card_token": "",
    "card_no": "",
    "field0": "",
    "field1": "9582567614",
    "field2": "EMI1014338639070843702",
    "field3": "Transaction is successful",
    "field4": "bnpl",
    "field5": "VFhOMzk2MjA3ODY2",
    "field6": "TXN396207866",
    "field7": "PAYMENT_SUCCESSFUL",
    "field8": "SUCCESS",
    "field9": "Transaction is successful",
    "payment_source": "payuPureS2S",
    "PG_TYPE": "BNPL-PG",
    "error": "E000",
    "error_Message": "No Error",
    "net_amount_debit": "2.07",
    "discount": "0.00",
    "offer_key": "",
    "offer_availed": "",
    "additionalCharges": "0.07",
    "unmappedstatus": "captured",
    "hash": "3a7742e5d9284e4f43d349bf1a5ff04353a099920ced98330fab15728841b6c772f00f83163c491d8954ead0c9a1dee7af94d67ddc539ff6cb2d0246baed8148",
    "bank_ref_no": "TXN396207866",
    "bank_ref_num": "TXN396207866",
    "bankcode": "LAZYPAY",
    "surl": "https://admin.payu.in/test_response",
    "curl": "https://admin.payu.in/test_response",
    "furl": "https://admin.payu.in/test_response"
  }
}

```

### Failure scenario

- Repeat User Flow: Auto-debit Failed

```
{
  "metaData": {
    "message": "The customer is not eligible for this transaction",
    "referenceId": "423fe9bfebdb2f92b8ae95a125aff397",
    "statusCode": "E2401",
    "txnId": "4223974b64f88ab4e3a1",
    "txnStatus": "failed",
    "unmappedStatus": "failure"
  },
  "result": {
    "link_and_pay": {
      "customerLinked": "true",
      "payuToken": "token12345"
    }
  }
}
```

- Failed at Payment option’s end

```
{
  "metaData": {
    "message": "Transaction Failed at bank end.",
    "referenceId": "ea68a970115a9d87c6ece8d0218e6c2a",
    "statusCode": "E308",
    "txnId": "54d2d883f8e4a3fff6ba",
    "txnStatus": "failed",
    "unmappedStatus": "failure"
  },
  "result": {
    "link_and_pay": {
      "customerLinked": "true",
      "payuToken": "token12345" // can be null or "" <empty string>
    }
  }
}
```

<br />
