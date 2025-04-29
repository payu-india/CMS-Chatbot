---
title: EMI
excerpt: ''
api:
  file: merchant-hosted-21.json
  operationId: MerchantHostedCheckout-EMI
deprecated: false
hidden: false
metadata:
  title: Collect Payment using EMI with Merchant Hosted Checkout
  description: >-
    Explore PayU's Merchant Hosted EMI solutions, enabling easy integration of
    EMI payment options for e-commerce platforms. Learn about API integration,
    supported banks, and flexible installment plans to enhance customer
    experience and boost sales.
  keywords:
    - EMI Merchant Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - EMI Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for EMI Merchant Hosted Checkout
    - _payment API for EMI Merchant Hosted Checkout
    - _payment API simulation for EMI Custom Checkout
    - _payment API simulation for EMI Merchant Hosted Checkout
    - "Equated Monthly Installment\_Merchant Hosted Checkout Collect Payment API"
    - Simulator for PayU payment collection
    - "Equated Monthly Installment\_Custom Checkout integration with PayU"
    - "Collect Payment API for Equated Monthly Installment\_Merchant Hosted Checkout"
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: create-a-no-cost-emi-offer
      title: Create a No-Cost EMI Offer
    - type: basic
      slug: create-a-low-cost-emi-offer
      title: Create a Low-Cost EMI Offer
---
EMI as a payment option gives your customers the freedom and affordability to purchase expensive items without having to deal with banks or NBFCs as intermediaries. 

You can collect payments from customers in EMI using the Merchant Hosted integration. You need to ensure that **EMI** for the **pg** parameter and EMI code based on the card issuer and tenure for the **bankcode** parameter is posted.

<PaymentAPIEnvironment />

<details>

<summary>Sample request</summary>

```curl
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=H6mUfE0ccAY94j&amount=20000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=EMI&bankcode=EMIA3&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=&hash=782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
```

</details>

<details>  

<summary>Sample response</summary>

```
Array
(
    [mihpayid] => 403993715523602563
    [status] => success
    [unmappedstatus] => captured
    [key] => JP***g
    [txnid] => v2tWbbdUOuacK9
    [amount] => 20000.00
    [discount] => 0.00
    [net_amount_debit] => 20000.00
    [addedon] => 2021-07-27 11:14:44
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
    [phone] => 1234567890
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
    [hash] => 10f8ead10cdf5f9b7bf9046987de046d63d62d6679dded9d5da8145f459066943570eec4aa184494ae77f99a8bcd55452af3c4eff0d7a7d3ba809c97b7c73045
    [field1] => 
    [field2] => 
    [field3] => 
    [field4] => 
    [field5] => 
    [field6] => 
    [field7] =>
    [field8] => 
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => EMI-PG
    [bank_ref_num] => 3d7cc4a4-00c8-4705-a0e7-5708d2c2bb75
    [bankcode]=> EMIA3
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => payu
    [cardnum] =>512345XXXXXX2346
)
```

</details>

<details>
  <summary>Response parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "mihpayid",
    "0-1": "It is a unique reference number created for each transaction at PayU’s end which is used to identify a transaction in case of a refund.",
    "1-0": "mode",
    "1-1": "This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:    \n\t•\tCredit Card – CC   \n\t•\tDebit Card – DC   \n\t•\tNet Banking – NB  \n\t•\tCash Card – CASH  \n\t•\tEMI – EMI   \n\t•\tCardless EMI – CLEMI  \n\t•\tBuy Now Pay Later - BNPL",
    "2-0": "bankcode",
    "2-1": "This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.",
    "3-0": "status",
    "3-1": "This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. The significance of the values for these values are:    \n\t•\t**Success**: If the value of status parameter is ’success’, the transaction is successful.   \n\t•\t**Failed**: If the value of status parameter is ‘failure’ or ‘pending’, must only be treated as a failed transaction.",
    "4-0": "unmappedstatus",
    "4-1": "This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to  [Payment State Explanations](ref:payment-state-explanations).",
    "5-0": "key",
    "5-1": "This parameter contains the merchant key.",
    "6-0": "error",
    "6-1": "For the failed transactions, this parameter provides the reason for failure.",
    "7-0": "error\\_message",
    "7-1": "This parameter contains the error message. For the list of error message, refer to [Error Codes](ref:error-codes).",
    "8-0": "bank\\_ref\\_num",
    "8-1": "For each successful transaction – this parameter contains the bank reference number generated by the bank.",
    "9-0": "txnid",
    "9-1": "This parameter contains the transaction ID value posted by the merchant during the transaction request.",
    "10-0": "amount",
    "10-1": "This parameter contains the original amount which was sent in the transaction request by the merchant.",
    "11-0": "cardCategory",
    "11-1": "This parameter contains the card category to indicate whether it is domestic or international.",
    "12-0": "discount",
    "12-1": "This parameter contains the discount amount by the merchant.",
    "13-0": "net_amount_debit",
    "13-1": "This parameter contains the net amount debited.",
    "14-0": "addedon",
    "14-1": "The transaction date and time of the transaction.",
    "15-0": "productinfo",
    "15-1": "This parameter contains the same value of product information which was sent in the transaction request from the merchant’s end to PayU.",
    "16-0": "firstname",
    "16-1": "This parameter contains the same value of first name which was sent in the transaction request from the merchant’s end to PayU.",
    "17-0": "lastname",
    "17-1": "This parameter contains the same value of last name which was sent in the transaction request from the merchant’s end to PayU.",
    "18-0": "email",
    "18-1": "This parameter contains the same value of email which was sent in the transaction request from the merchant’s end to PayU.",
    "19-0": "phone",
    "19-1": "This parameter contains the same value of phone which was sent in the transaction request from the merchant’s end to PayU.",
    "20-0": "hash",
    "20-1": "This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).",
    "21-0": "PG\\_TYPE",
    "21-1": "This parameter gives information on the payment gateway used for the transaction.",
    "22-0": "udf1",
    "22-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "23-0": "udf2",
    "23-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "24-0": "udf3",
    "24-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5 which was sent in the transaction request from the merchant’s end to PayU.",
    "25-0": "udf4",
    "25-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "26-0": "udf5",
    "26-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "27-0": "udf6",
    "27-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "28-0": "udf7",
    "28-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.\\*\\*\\*\\*",
    "29-0": "udf8",
    "29-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "30-0": "udf9",
    "30-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "31-0": "success_at",
    "31-1": "This parameter contains the date and timestamp when the transaction was successful.",
    "32-0": "cardnum",
    "32-1": "The parameter contains the card number masked and only last 4 digits are returned.",
    "33-0": "issuing_bank",
    "33-1": "The parameters contains the card issuing bank."
  },
  "cols": 2,
  "rows": 34,
  "align": [
    null,
    null
  ]
}
[/block]


</details>

## Request parameters

<details>
  <summary>Response parameters</summary> Additional info for request parameters

<Additional_paymentRequestParams />

</details>

> 📘 Reference
> 
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

> 🚧 

> 🚧 Values to be used in Test environment
> 
> - You can used any EMI code listed in the <a href="emi-codes" target="_blank">EMI Codes</a> section. section and test cards listed in the <a href="test-cards-upi-id-and-wallets#emi-test-cards" target="_blank">Test Cards</a> section. For example, the following values can be used:
> 
> |                   |                         |                   |
> | :---------------- | :---------------------- | :---------------- |
> | bankcode: EMIA3   | ccnum: 5123456789012346 | ccexpmon: 05      |
> | ccexpyr: 2025     | ccvv: 123               | ccname: Any value |
> | phone: 9123412345 |                         |                   |
> 
> - For the **amount** parameter, use **>=INR 1000 ** in the Test environment.

> ❗️ Error handling
> 
> If any error message is displayed with an error code, refer to the <a href="error-codes" target="_blank">Error Codes</a> section. to understand the reason for these error codes.