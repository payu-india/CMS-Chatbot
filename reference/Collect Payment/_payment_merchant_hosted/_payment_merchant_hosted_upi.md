---
title: UPI
api:
  file: updated_upi_merchant_hosted.json
  operationId: MerchantHostedCheckout-UPI
hidden: false
metadata:
  title: UPI - Merchant Hosted Checkout
  description: >-
    Discover comprehensive integration guides and API references for Merchant
    Hosted UPI payments with PayU. Learn how to seamlessly integrate UPI payment
    solutions into your website or app, enabling secure and efficient
    transactions for your customers.
---
PayU allows you to collect payments using UPI handles. For the list of UPI providers supported, refer to [UPI Handles](doc:upi-handles).

### Recommended prerequisite before initiating payment

When your customer makes payment through UPI, you can validate the customer's Virtual Payment Address (VPA) and then initiate payment. The validateVpa API is used to validate the UPI handle.

Validate the VPA (UPI handle) using the validateVpa API.  For more information, refer to [Validate VPA Handle API](ref:validate_vpa_api).

**Environment**

|                            |                                                                        |
| -------------------------- | ---------------------------------------------------------------------- |
| **Test Environment**       | [https://test.payu.in/_payment>](https://test.payu.in/_payment%3E)     |
| **Production Environment** | [https://secure.payu.in/_payment>](https://secure.payu.in/_payment%3E) |

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=VPA-anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ```
  Array
  (
      [mihpayid] => 403993715523409521
      [mode] => UPI
      [status] => success
      [unmappedstatus] => captured
      [key] => JPM7Fg
      [txnid] => 5jJ9xRceXX1ydT
      [amount] => 10.00
      [discount] => 0.00
      [net_amount_debit] => 1000
      [addedon] => 2021-07-02 15:03:50
      [productinfo] => iPhone
      [firstname] => PayU User
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
      [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
      [field1] => vpa-anything@payu
      [field2] => 5jJ9xRceXX1ydT
      [field3] => 
      [field4] => PayU User
      [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
      [field6] => 
      [field7] => Transaction completed successfully
      [field8] => 
      [field9] => Transaction completed successfully
      [payment_source] => payu
      [PG_TYPE] => UPI-PG
      [bank_ref_num] => 5jJ9xRceXX1ydT
      [bankcode] => UPI
      [error] => E000
      [error_Message] => No Error
  )
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  | **Parameter**      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                            |
  | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | mihpayid           | It is a unique reference number created for each transaction at PayU's end which is used to identify a transaction in case of a refund.                                                                                                                                                                                                                                                                                    |
  | mode               | This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are: • Credit Card – CC • Debit Card – DC • Net Banking – NB • Cash Card – CASH • EMI – EMI • Cardless EMI – CLEMI • Buy Now Pay Later - BNPL                                                                                                                                                   |
  | bankcode           | This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.                                                                                                                                                                                                                                                                    |
  | status             | This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. The significance of the values for these values are: • **Success**: If the value of status parameter is 'success', the transaction is successful. • **Failed**: If the value of status parameter is 'failure' or 'pending', must only be treated as a failed transaction. |
  | unmappedstatus     | This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to  [Payment State Explanations](ref:payment-state-explanations).                                                                                          |
  | key                | This parameter contains the merchant key.                                                                                                                                                                                                                                                                                                                                                                                  |
  | error              | For the failed transactions, this parameter provides the reason for failure.                                                                                                                                                                                                                                                                                                                                               |
  | error\_message     | This parameter contains the error message. For the list of error message, refer to [Error Codes](ref:error-codes).                                                                                                                                                                                                                                                                                                         |
  | bank\_ref\_num     | For each successful transaction – this parameter contains the bank reference number generated by the bank.                                                                                                                                                                                                                                                                                                                 |
  | txnid              | This parameter contains the transaction ID value posted by the merchant during the transaction request.                                                                                                                                                                                                                                                                                                                    |
  | amount             | This parameter contains the original amount which was sent in the transaction request by the merchant.                                                                                                                                                                                                                                                                                                                     |
  | cardCategory       | This parameter contains the card category to indicate whether it is domestic or international.                                                                                                                                                                                                                                                                                                                             |
  | discount           | This parameter contains the discount amount by the merchant.                                                                                                                                                                                                                                                                                                                                                               |
  | net\_amount\_debit | This parameter contains the net amount debited.                                                                                                                                                                                                                                                                                                                                                                            |
  | addedon            | The transaction date and time of the transaction.                                                                                                                                                                                                                                                                                                                                                                          |
  | productinfo        | This parameter contains the same value of product information which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                   |
  | firstname          | This parameter contains the same value of first name which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                            |
  | lastname           | This parameter contains the same value of last name which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                             |
  | email              | This parameter contains the same value of email which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                                 |
  | phone              | This parameter contains the same value of phone which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                                 |
  | hash               | This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).                                                                                                                                                                                                                                         |
  | PG\_TYPE           | This parameter gives information on the payment gateway used for the transaction.                                                                                                                                                                                                                                                                                                                                          |
  | udf1               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf2               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf3               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5 which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                       |
  | udf4               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf5               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf6               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf7               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf8               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf9               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | success\_at        | This parameter contains the date and timestamp when the transaction was successful.                                                                                                                                                                                                                                                                                                                                        |
  | cardnum            | The parameter contains the card number masked and only last 4 digits are returned.                                                                                                                                                                                                                                                                                                                                         |
  | issuing\_bank      | The parameters contains the card issuing bank.                                                                                                                                                                                                                                                                                                                                                                             |
</Accordion>

## Request parameters

### Additional info for request parameters

<Additional_paymentRequestParams />

> 📘 Reference
>
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

> 🚧 You can test UPI only with the anything@payu or [9999999999@payu.in](mailto:9999999999@payu.in) as VPA.

> ❗️ Error handling
>
> If any error message is displayed with an error code, refer to the <a href="error-codes" target="_blank">Error Codes</a> section to understand the reason for these error codes.