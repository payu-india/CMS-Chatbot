---
title: Cancel Recurring Payment for a Card
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Cancel the Recurring Payment for a Card
  description: >-
    Learn how to cancel recurring payment registrations for cards using PayU's
    API. This documentation provides detailed instructions for revoking
    mandates, ensuring compliance with RBI guidelines and enabling seamless
    management of subscription cancellations.
  keywords:
    - PayU Cancel Recurring Payments for Cards API
    - ' Revoke Recurring Payment for Cards'
    - ' PayU recurring billing cancellation for Cards'
    - ' PayU subscription cancellation for Cards'
    - ' Cancel recurring transactions for Cards API'
    - ' _payment cancel card recurring'
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: using-api-integration-recurring-payments
      title: Using API Integration
    - type: endpoint
      slug: modify-the-recurring-payments-for-a-card
      title: Modify the Recurring Payments for a Card
    - type: endpoint
      slug: check-mandate-status-api
      title: Check Mandate Status for Cards API
---
This section describes how to use the \_payment API to cancel a recurring payment registration for card.

> 📘 Notes:
> 
> - This API is mandatory for merchants to go live with all cards.
> - The 2FA is required for cancelling recurring payment with AMEX cards.

**HTTP Method**: POST

<PaymentAPIEnvironment />

## Request parameters

The following table describes the parameters for modifying the recurring payment details for a card.

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "key  \n**mandatory**",
    "0-1": "`varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account.",
    "0-2": "Your Test Key",
    "1-0": "txnid  \n**mandatory**",
    "1-1": "`varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant’s) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.  \n`Character limit`: 25  \n**Note**: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of ‘duplicate Order ID.’",
    "1-2": "fd3e847h2",
    "2-0": "amount  \n**mandatory**",
    "2-1": "`float` This parameter should contain the payment amount of the particular transaction.  \n  \n**Note**: Type-cast the amount to float type  \nDepending upon the merchant use case, this value will vary.  \n  \n\\- It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case.  \n  \n- In the case of first instalment use cases, this amount can be equal to initiate setup amount, but this use case will be supported only against selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI",
    "2-2": "1000",
    "3-0": "productinfo  \n**mandatory**",
    "3-1": "`varchar` This parameter should contain a brief product description. It should be a string describing the product.  \n`Character limit`: 100",
    "3-2": "Time Magazine Subscription",
    "4-0": "firstname  \n**mandatory**",
    "4-1": "`varchar` Must contain the first name of the customer.  \n`Character limit`: 60",
    "4-2": "Ashish",
    "5-0": "email  \n**mandatory**",
    "5-1": "`varchar` Must contain the email of the customer.  \nThis information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.  \nAlso, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.  \nCharacter limit: 50",
    "5-2": "[Ashish@test.com](mailto:Ashish@test.com)",
    "6-0": "phone  \n**mandatory**",
    "6-1": "`varchar` Must contain the phone number of the customer.  \n  \nThis information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.  \nCharacter limit: 50",
    "6-2": "9843176540",
    "7-0": "api_version  \n**mandatory**",
    "7-1": "This parameter must always needs to be passed as 7.",
    "7-2": "7",
    "8-0": "si  \n**mandatory**",
    "8-1": "This parameter must be passed with the value as 3 to cancel an already existing subscription/consent.",
    "8-2": "3",
    "9-0": "pg  \n**mandatory**",
    "9-1": "`String` This parameter defines the payment category that the merchant wants the customer to see by default on the PayU’s payment page. In this example, \"CC\" must be specified. For more information, refer to Payment Mode Codes.",
    "9-2": "AMEXSI",
    "10-0": "bankcode  \n**mandatory**",
    "10-1": "Each payment option is identified with a String unique bank code at PayU. The merchant must post this parameter with the corresponding payment option’s bank code value in it. For more information, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards)",
    "10-2": "AMEXSI",
    "11-0": "ccnum  \n**mandatory**",
    "11-1": "This parameter must contain the 13 to 19-digit  card number for credit or debit cards in general.",
    "11-2": "",
    "12-0": "ccname  \n**mandatory**",
    "12-1": "This parameter must contain the name on card – as entered by the customer for the transaction.",
    "12-2": "",
    "13-0": "ccvv  \n**mandatory**",
    "13-1": "This parameter must contain the 3-digit CVV number for credit cards or debit cards. For AMEX cards, 4-digit security code (4DBC) number of the card must be posted. Also, known as CID (Card Identification) number.",
    "13-2": "",
    "14-0": "ccexpmon  \n**mandatory**",
    "14-1": "This parameter must contain the card’s expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format.  \nFor months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively.",
    "14-2": "",
    "15-0": "ccexpyr  \n**mandatory**",
    "15-1": "This parameter must contain the card’s expiry year – as entered by the customer for the transaction. It must be of four digits.",
    "15-2": "",
    "16-0": "si_details  \n**mandatory**",
    "16-1": "This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.  \n  \n**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer – <https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0> )  \n  \nThis is a JSON object and it includes a set of parameters are described in the the [si\\_details Parameter – JSON Details](si_details-parameter-–-json-details) table.",
    "16-2": "Refer the example below the si_details Parameter Description table.",
    "17-0": "hash  \n**mandatory**",
    "17-1": "Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU’s payment interface while registration transactions.  \n  \nIt is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt.  \n  \nIn the case of registration transaction, the formula is used to calculate this hash is similar to the following:  \n`SHA512(key\\|txnid\\|amount\\|productinfo\\|firstname\\|email\\|udf1\\|udf2\\|udf3\\|udf4\\|udf5\\||\\||\\||si_details\\|SALT)`",
    "17-2": ""
  },
  "cols": 3,
  "rows": 18,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### si\_details Parameter – JSON Details

The description for the **si\_details** parameter (JSON format):

> 📘 **Note**:
> 
> If the request was to modify a subscription,  **si_consent_action** parameter needs to be validated in the response. The field must return values modify based on the action sent in billing details JSON. Also, the payment source returned in such cases will be payu.

[block:parameters]
{
  "data": {
    "h-0": "**JSON Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "authpayuid  \n**mandatory for modifying subscription with cards**",
    "0-1": "This parameter is used only to modify an existing subscription/consent. Modification means modifying billing details like startDate, endDate, billing cycle, billing interval, billing amount.",
    "0-2": " ",
    "1-0": "action  \n**mandatory for cards**",
    "1-1": "This parameter is used to cancel an existing subscription. Pass the values as **delete** to cancel an existing subscription or consent.",
    "1-2": "delete"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


<br />

## Sample request

```curl
curl -X POST "https://test.payu.in/_payment-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d”key=JP\*\*\*g&txnid=56bb2e3fcb510f1c1521&amount=10000&firstname=Payu-Admin&email=test@example.com&phone=1234567890&productinfo=iPhone&api\_version=7&si=2&pg=CC&bankcode=UTIBENCC&surl=https://test.payu.in/admin/test_response/&furl=https://test.payu.in/admin/test_response
&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=Test User&si\_details={“authpayuid" : "403993715525316543" , "action": "cancel"}&hash=e36568b2dfc460eab0eb3387fb7d90543ed861154f273b9593d6fcc152ed93a91e529c2f4be0965eeb57104e82d58889fa5efb52811ec78cbd1ad646e39c29a0”
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "mihpayid",
    "0-1": "It is a unique reference number created for each transaction at PayU’s end which is used to identify a transaction in case of a refund.",
    "1-0": "mode",
    "1-1": "This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:    \n\t•\tCredit Card – CC   \n\t•\tDebit Card – DC ",
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
    "33-1": "The parameters contains the card issuing bank.",
    "34-0": "si_consent_action",
    "34-1": "This parameter will be returned only if a modify subscription request has been received. In other cases, this field will not be returned.  \nValues can be  \n  \n- **modify**\n- **delete**  \n  If, in billing details, the action was to modify, then to validate whether the subscription was modified, this fields need to be validated in response. If this field is not sent in response of modify request, then even if transaction is success, then money would have got deducted but the subscription would not have been modified."
  },
  "cols": 2,
  "rows": 35,
  "align": [
    null,
    null
  ]
}
[/block]


## Sample response

- Sample response for successful cancellation of a card mandate:

Cancelling Recurring Registration - Success Response

```plaintext
Array
(
    [mihpayid] => 22316057587
    [mode] => DC
    [status] => success
    [unmappedstatus] => captured
    [key] => BmTY3G
    [txnid] => bf058fc87e608aeaeabe
    [amount] => 1.00
    [cardCategory] => domestic
    [discount] => 0.00
    [additionalCharges] => 0.02
    [net_amount_debit] => 1.02
    [addedon] => 2025-01-30 16:28:15
    [productinfo] => Product Info
    [firstname] => Payu-Admin
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => test@example.com
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
    [hash] => eacfebb41dff9c3ff58ba5857a5f70b8b368afa424a5d5044dc3f148c8cfdfc8da9d0f4d5e7c7e53b01d2ea1d0f1c8f537527b16494cb65cfec16785d7373097
    [field1] => 7382347150366494405959
    [field2] => 431242
    [field3] => 1.02
    [field4] => 
    [field5] => 00
    [field6] => 05
    [field7] => AUTHPOSITIVE
    [field8] => AUTHORIZED
    [field9] => Transaction is Successful
    [payment_source] => payu
    [meCode] => {"MID":"hdfc_89051842","TKey":"0wMbyodmbgzwIOejqyUOpAkCJdBC01zQGwHS+Pm1rGGxBki5xPR60G948KUmnPR5l7xDpxYOWIOLfE1q0z5ezIA7dG/yVAkp4nZmbddhWyNpdLusIKmiJzXH6ASAMJKZJ0dH3NyQypy9w51PfUKAz80I4y4Udq8zCKB+yiDP3JqkOfz366Y5SjKI/BWNMXCMXOXIvzVNSinDVi4bVW+WtimdJ1BS9WACx8zkYjPjTkuGB6TMYeJGYt0JJ6oSQce4xk4yW3al+fFABVC26S+2wNuHYMMFvhd09AK4nUvFMh9SHjhWWw6T81miW2kqxi0o+rdvCCYEO3Aa3R5kH8kmIw=="}
    [PG_TYPE] => DC-PG
    [bank_ref_num] => 7382347150366494405959
    [bankcode] => VISA
    [error] => E000
    [error_Message] => No Error
    [cardnum] => XXXXXXXXXXXX6579
    [cardhash] => This field is no longer supported in postback params.
)
```

- Sample Response for failed cancellation

Cancelling Recurring Registration - Failure Response

```plaintext
{
	"action": "MANDATE_REVOKE",
	"statusCode": 0,
	"Message": "Mandate is not active”
}
```