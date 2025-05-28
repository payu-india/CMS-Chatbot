---
title: Cancel Recurring Payment for a Card
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
This section describes how to use the **_payment** API to cancel a recurring payment registration for card.

> 📘 Notes:
>
> * This API is mandatory for merchants to go live with all cards.
> * The 2FA is required for cancelling recurring payment with AMEX cards.

# Mandate Revoke (Cancel Recurring Payment)

This section describes how to use the **mandate\_revoke** command to cancel a recurring payment registration for card.

> 📘 Notes:
>
> * This API is mandatory for merchants to go live with all cards.
> * The 2FA is required for cancelling recurring payment with AMEX cards.

Method: **POST**

**Environment**

| | |
| :------------------------- | :-------------------------------- |
| **Test Environment**       | https://test.payu.in/_payment     |
| **Production Environment** | https://secure.payu.in/_payment   |

## Request parameters

The following table describes the parameters for modifying the recurring payment details for a card.

| Parameter | Description | Example |
| :-------- | :---------- | :------ |
| **key** *(mandatory)* | `varchar` This parameter is the unique Merchant Key provided by PayU for your merchant account. | Your Test Key |
| **txnid** *(mandatory)* | `varchar` This parameter is known as Transaction ID (or Order ID). It is the order reference number generated at your (Merchant's) end. It is an identifier that you (merchant) would use to track a particular order. If a transaction using a particular transaction ID has already been successful at PayU, the usage of the same Transaction ID again would fail. Hence, you must post us a unique transaction ID for every new transaction.  
`Character limit`: 25  
**Note**: Ensure that the transaction ID sent to us has not been successful earlier. In case of this duplication, the customer would get an error of 'duplicate Order ID.' | fd3e847h2 |
| **amount** *(mandatory)* | `float` This parameter should contain the payment amount of the particular transaction.  
  
**Note**: Type-cast the amount to float type  
Depending upon the merchant use case, this value will vary.  
  
- It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case.  
  
- In the case of first instalment use cases, this amount can be equal to initiate setup amount, but this use case will be supported only against selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI | 1000 |
| **productinfo** *(mandatory)* | `varchar` This parameter should contain a brief product description. It should be a string describing the product.  
`Character limit`: 100 | Time Magazine Subscription |
| **firstname** *(mandatory)* | `varchar` Must contain the first name of the customer.  
`Character limit`: 60 | Ashish |
| **email** *(mandatory)* | `varchar` Must contain the email of the customer.  
This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is a must to provide the correct information.  
Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.  
Character limit: 50 | Ashish@test.com |
| **phone** *(mandatory)* | `varchar` Must contain the phone number of the customer.  
  
This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information Also, MIS reporting is shared with few issuing banks where email and mobile number is used to keep track of users using SI transactions.  
Character limit: 50 | 9843176540 |
| **api_version** *(mandatory)* | This parameter must always needs to be passed as 7. | 7 |
| **si** *(mandatory)* | This parameter must be passed with the value as 3 to cancel an already existing subscription/consent. | 3 |
| **pg** *(mandatory)* | `String` This parameter defines the payment category that the merchant wants the customer to see by default on the PayU's payment page. In this example, "CC" must be specified. For more information, refer to Payment Mode Codes. | AMEXSI |
| **bankcode** *(mandatory)* | Each payment option is identified with a String unique bank code at PayU. The merchant must post this parameter with the corresponding payment option's bank code value in it. For more information, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards) | AMEXSI |
| **ccnum** *(mandatory)* | This parameter must contain the 13 to 19-digit card number for credit or debit cards in general. | |
| **ccname** *(mandatory)* | This parameter must contain the name on card – as entered by the customer for the transaction. | |
| **ccvv** *(mandatory)* | This parameter must contain the 3-digit CVV number for credit cards or debit cards. For AMEX cards, 4-digit security code (4DBC) number of the card must be posted. Also, known as CID (Card Identification) number. | |
| **ccexpmon** *(mandatory)* | This parameter must contain the card's expiry month – as entered by the user for the transaction. It must always be in 2 digits or in MM format.  
For months 1-9, this parameter must be appended with 0 – like 01, 02…09. For months 10-12, this parameter must not be appended – It should be 10,11 and 12 respectively. | |
| **ccexpyr** *(mandatory)* | This parameter must contain the card's expiry year – as entered by the customer for the transaction. It must be of four digits. | |
| **si_details** *(mandatory)* | This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.  
  
**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer – https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0 )  
  
This is a JSON object and it includes a set of parameters are described in the the [si\_details Parameter – JSON Details](#si_details-parameter-json-details) table. | Refer the example below the si_details Parameter Description table. |
| **hash** *(mandatory)* | Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU's payment interface while registration transactions.  
  
It is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt.  
  
In the case of registration transaction, the formula is used to calculate this hash is similar to the following:  
`SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||si_details|SALT)` | |

## si\_details Parameter – JSON Details

The description for the **si\_details** parameter (JSON format):

> 📘 **Note**:
> 
> If the request was to modify a subscription, **si_consent_action** parameter needs to be validated in the response. The field must return values modify based on the action sent in billing details JSON. Also, the payment source returned in such cases will be payu.

| **JSON Field** | **Description** | **Example** |
| :------------- | :-------------- | :---------- |
| **authpayuid** *(mandatory for modifying subscription with cards)* | This parameter is used only to modify an existing subscription/consent. Modification means modifying billing details like startDate, endDate, billing cycle, billing interval, billing amount. | |
| **action** *(mandatory for cards)* | This parameter is used to cancel an existing subscription. Pass the values as **cancel** to cancel an existing subscription or consent. | cancel |

## si\_details Parameter Example Values

For a yearly plan starting from 1st January 2019, having a monthly billing amount INR 100, the plan details:

```plaintext
{"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2019-09-01","paymentEndDate": "2019-12-01"}
```

## Sample request

```curl
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=56bb2e3fcb510f1c1521&amount=10000&firstname=Payu-Admin&email=test@example.com&phone=1234567890&productinfo=iPhone&api_version=7&si=2&pg=CC&bankcode=UTIBENCC&surl=https://test.payu.in/admin/test_response/&furl=https://test.payu.in/admin/test_response&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=Test User&si_details={"authpayuid":"403993715525316543","action":"cancel"}&hash=e36568b2dfc460eab0eb3387fb7d90543ed861154f273b9593d6fcc152ed93a91e529c2f4be0965eeb57104e82d58889fa5efb52811ec78cbd1ad646e39c29a0"
```

## Response parameters

| **Parameter** | **Description** |
| :------------ | :-------------- |
| mihpayid | It is a unique reference number created for each transaction at PayU's end which is used to identify a transaction in case of a refund. |
| mode | This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:  
• Credit Card – CC  
• Debit Card – DC |
| bankcode | This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST. |
| status | This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. The significance of the values for these values are:  
• **Success**: If the value of status parameter is 'success', the transaction is successful.  
• **Failed**: If the value of status parameter is 'failure' or 'pending', must only be treated as a failed transaction. |
| unmappedstatus | This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to [Payment State Explanations](ref:payment-state-explanations). |
| key | This parameter contains the merchant key. |
| error | For the failed transactions, this parameter provides the reason for failure. |
| error\_message | This parameter contains the error message. For the list of error message, refer to [Error Codes](ref:error-codes). |
| bank\_ref\_num | For each successful transaction – this parameter contains the bank reference number generated by the bank. |
| txnid | This parameter contains the transaction ID value posted by the merchant during the transaction request. |
| amount | This parameter contains the original amount which was sent in the transaction request by the merchant. |
| cardCategory | This parameter contains the card category to indicate whether it is domestic or international. |
| discount | This parameter contains the discount amount by the merchant. |
| net_amount_debit | This parameter contains the net amount debited. |
| addedon | The transaction date and time of the transaction. |
| productinfo | This parameter contains the same value of product information which was sent in the transaction request from the merchant's end to PayU. |
| firstname | This parameter contains the same value of first name which was sent in the transaction request from the merchant's end to PayU. |
| lastname | This parameter contains the same value of last name which was sent in the transaction request from the merchant's end to PayU. |
| email | This parameter contains the same value of email which was sent in the transaction request from the merchant's end to PayU. |
| phone | This parameter contains the same value of phone which was sent in the transaction request from the merchant's end to PayU. |
| hash | This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted). |
| PG\_TYPE | This parameter gives information on the payment gateway used for the transaction. |
| udf1 | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU. |
| udf2 | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU. |
| udf3 | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5 which was sent in the transaction request from the merchant's end to PayU. |
| udf4 | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU. |
| udf5 | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU. |
| udf6 | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU. |
| udf7 | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU. |
| udf8 | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU. |
| udf9 | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU. |
| success_at | This parameter contains the date and timestamp when the transaction was successful. |
| cardnum | The parameter contains the card number masked and only last 4 digits are returned. |
| issuing_bank | The parameters contains the card issuing bank. |
| si_consent_action | This parameter will be returned only if a modify subscription request has been received. In other cases, this field will not be returned.  
Values can be  
modify  
cancel  
If, in billing details, the action was to modify, then to validate whether the subscription was modified, this fields need to be validated in response. If this field is not sent in response of modify request, then even if transaction is success, then money would have got deducted but the subscription would not have been modified. |

## Sample response

- Sample response for successful cancellation of a card mandate:

Cancelling Recurring Registration - Success Response

```plaintext
Array
(
    [mihpayid] => 403993715525316543
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => JP***g
    [txnid] => eF5yY4ArrynoIV
    [amount] => 10.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2022-02-02 15:15:07
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
    [hash] => 499fa5f6d9019cc7bda9750b18bf3ba52f161da42cb065cab094595cb9d1c90058a3f1c7f3fcb057c371baa077052522847826be269060140580a7c345206020
    [field1] => 4296837871969451239257
    [field2] => 601248
    [field3] => 10.00
    [field4] => 403993715525316543
    [field5] => 100
    [field6] => 02
    [field7] => AUTHPOSITIVE
    [field8] => 
    [field9] => Transaction is Successful
    [payment_source] => payu
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 4296837871969451239257
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [name_on_card] => payu
    [cardnum] => 512345XXXXXX2346
    [cardhash] => This field is no longer supported in postback params.
)
```

- Sample Response for failed cancellation

Cancelling Recurring Registration - Failure Response

```plaintext
{
    "action": "MANDATE_REVOKE",
    "statusCode": 0,
    "Message": "Mandate is not active"
}
```