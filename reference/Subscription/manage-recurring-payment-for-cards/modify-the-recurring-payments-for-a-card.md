---
title: Modify Recurring Payments for a Card
excerpt: 'Resource: **_payment**'
deprecated: false
hidden: false
metadata:
  title: Modify the Recurring Payments for a Card
  description: >-
    Learn how to modify existing recurring payment details for a card using
    PayU's API. This documentation provides detailed instructions for updating
    recurring payment information, ensuring compliance with RBI guidelines and
    enabling seamless management of subscription payments.
  keywords:
    - PayU Modify Recurring Payments API
    - ' Update Recurring Payment for Cards'
    - '  PayU recurring billing updation'
    - ' Update PayU subscription payments for cards'
    - ' Update PayU subscription payments for UPI'
    - ' Modify recurring transactions for Cards'
    - ' _payment modify card recurring'
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: using-api-integration-recurring-payments
      title: Using API Integration
    - type: endpoint
      slug: cancel-the-recurring-payment-for-cards
      title: Cancel the Recurring Payment for a Card
---
This section describes how to use the **\_payment** API to update an existing recurring payment for a card.

> 📘 Note:
> 
> As per RBI guidelines while modifying the recurring payment, taking consent from the customer and doing an additional factor of authentication is mandatory. You must ensure this is done before using this API. You need to pass **authPayuId** and **action** fields to modify the billing details as part of JSON using this API as described in this section.

HTTP Method: **POST**

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
    "8-1": "This parameter must be passed with the value as 2 to modify an already existing subscription/consent.",
    "8-2": "3",
    "9-0": "pg  \n**mandatory**",
    "9-1": "`String` This parameter defines the payment category that the merchant wants the customer to see by default on the PayU’s payment page. In this example, \"CC\" must be specified. For more information, refer to Payment Mode Codes.",
    "9-2": "",
    "10-0": "bankcode  \n**mandatory**",
    "10-1": "Each payment option is identified with a String unique bank code at PayU. The merchant must post this parameter with the corresponding payment option’s bank code value in it. For more information, refer to [Card Type Codes and Supported Banks for Cards](doc:card-type-codes-and-supported-banks-for-cards)",
    "10-2": "",
    "11-0": "user_credentials  \n**mandatory**",
    "11-1": "`String` This parameter must contain the user credentials.",
    "11-2": "a:b",
    "12-0": "store_card_token  \n**mandatory**",
    "12-1": "`String` This must include the Network token generated at your end.",
    "12-2": "1234 4567 2456 3566",
    "13-0": "free_trial  \n**optional**",
    "13-1": "This is mandatory only if the merchant wants to support free trial use case with card and net banking together that too on PayU Hosted Checkout integration.  \n  \nIn this case, PayU adjusts the transaction amount as INR 2.00 for cards. INR 0.00 for Net Banking and UPI registration irrespective of what amount is passed against the amount field in the request.  \nThis parameter has no significance in the case of seamless flow.",
    "13-2": "",
    "14-0": "si_details  \n**mandatory**",
    "14-1": "This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.  \n  \n**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer – <https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0> )  \n  \nThis is a JSON object and it includes a set of parameters are described in the the si_details Parameter Description table.",
    "14-2": "Refer the example below the si_details Parameter Description table.",
    "15-0": "hash  \n**mandatory**",
    "15-1": "Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU’s payment interface while registration transactions.  \n  \nIt is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt.  \n  \nIn the case of registration transaction, the formula is used to calculate this hash is similar to the following:  \nHASH = SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)",
    "15-2": ""
  },
  "cols": 3,
  "rows": 16,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### For network tokens

This is applicable for the following scenarios:

- Merchant has the card token, TAVV(Cryptogram), and the last four digits of the card
- The token could be created by the merchant or through another partner

> 📘 Note:
> 
> This scenario is applicable if you are PCI compliant and got the network token and TAVV from any other aggregator or schemes and then sent the card transaction request in the form of authentication.

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Value**",
    "0-0": "store\\_card\\_token  \n**mandatory**",
    "0-1": "`String` This must include the Network token generated at your end.",
    "0-2": "1234 4567 2456 3566",
    "1-0": "storecard\\_token\\_type  \n**mandatory**",
    "1-1": "`integer` This parameter is used to specify the store card token type. For this scenario, you must include **1**.",
    "1-2": "1",
    "2-0": "additional\\_info  \n**mandatory**",
    "2-1": "`String` This parameter will contain the additional information in the following JSON format:  \n`{“last4Digits”: “1234”, “tavv”: “ABCDEFGH”,”trid”:”1234567890”, “tokenRefNo”:”abcde123456”}`",
    "2-2": "`{“last4Digits”: “1234”, “tavv”: “ABCDEFGH”,”trid”:”1234567890”, “tokenRefNo”:”abcde123456”}`"
  },
  "cols": 3,
  "rows": 3,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


> 📘 Notes for **additional_info** parameter:
> 
> The JSON format contains the following fields:  
> 
> - **trid** (Token Requestor ID) is the identity given by the networks for creating the tokens. You should be able to get the same from your token provider.
> - **tokenRefNo** (Token Reference Number) is generated along with the network token. . You should be able to get the same from your token provider.
> - **TAVV** is a token authentication verification value given by schemes or interchange. Also, known as cryptogram.
> 
> Additional notes:
> 
> - The last 4 digits of cards is mandatory for all transactions. 
> - Some payment gateways require the Token Requester ID (trid) and Token Reference Number (tokenRefNo) to be passed for processing the transaction. Not passing these values will restrict the number of payment gateways available for processing the transaction.
> - Token Requester ID (trid) and Token Reference Number (tokenRefNo) are mandatory for Diners token transactions.

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
    "0-0": "billingCycle  \n**mandatory**",
    "0-1": "Billing Cycle defines whether the customer needs to be charged over Daily, Weekly basis, Monthly or Yearly basis or one time.  ",
    "0-2": "ONCE",
    "1-0": "billingInterval  \n**mandatory**",
    "1-1": "Billing Interval is closely coupled with the **billingCycle** field and denotes at what frequency, the subscription plan needs to be executed. For monthly subscriptions, parameter values need to be sent in the request are:  \n_ billingCycle = MONTHLY  \n_ billingInterval = 1  \nSimilarly, by keeping the following values, customer will be charged once in every 3 days:  \n_ billingCycle = DAILY  \n_ billingInterval = 3",
    "1-2": "_ billingCycle = MONTHLY  \n_ billingInterval = 1 ",
    "2-0": "billingAmount  \n**mandatory**",
    "2-1": "The billing amount is passed in XX. XX format.  \nIn use cases where **billingCycle = ADHOC**, amount passed is treated as maximum amount since billing amount and billing cycle varies as per the usage of the subscription service.  In this case, the merchant is free to charge any amount for customer up to the amount specified in the defined subscription call.  For UPI, **billingAmount** should not be more than INR 15000 as it is the maximum limit allowed for UPI currently.",
    "2-2": "INR 2000",
    "3-0": "billingCurrency  \n**mandatory**",
    "3-1": "This field must be passed as “INR” .",
    "3-2": "INR",
    "4-0": "paymentStartDate  \n**mandatory**",
    "4-1": "The start date of the billing plan is specified in this field with the YYYY-MM-DD format.  \n**Note**: All the subsequent recurring transactions will be processed from this date onwards as per **billingCycle** and **billingInterval** fields combination. This date acts as reference point for recurring payments. **Note**: In case of UPI, send the current date here and any other value will be ignored.",
    "4-2": "2022-02-14",
    "5-0": "paymentEndDate  \n**mandatory**",
    "5-1": "The end date of the billing plan is specified in this field with the YYYY-MM-DD format.  \n**Note**: Pass the correct end date to PayU. Depending upon start date and end date, number of payment iterations are internally calculated and same information is passed to acquirers or banks.",
    "5-2": "2023-01-14",
    "6-0": "siTokenRequestor  \n**mandatory for saved cards**",
    "6-1": "This is optional and is only needed before 30th September, 2022 to activate new mandate setups in a controlled manner than activating it completely on all users. This involves creating token at the time of susbcription set. You can include any of the following values::  \n_ **1** : PayU will tokenise the card and share it in same subscription setup call with issuers for subscription setup.  \n_ **2**: PayU will do the authorization on plain card. Later, the same response will be shared to merchant. ",
    "6-2": "1",
    "7-0": "remarks  \n**optional**",
    "7-1": "This field is used to provide remarks on PSP applications during the registration transaction of UPI.  For cards and Net Banking, this parameter has no significance.  Character limit = 50.   \n**Note**: This field is applicable only for UPI.",
    "7-2": "Subscription for a year",
    "8-0": "billingLimit  \n**optional**",
    "8-1": "For UPI, this field is used to decide the period corresponding which the debit from the mandate recurring date can happen and this mandate registration date is confirmed during registration transaction of UPI.  \n **Note**: This field is applicable only for UPI.  \nThe possible values are:  \n_  **ON** = Use this parameter to deduct on a specific date  \n_  **BEFORE** = Use this parameter to deduct before and on a specific date  \n\\*  **AFTER** = Use this parameter to After and on the specific date  \n  \n**Note**: If no value is passed, ‘AFTER’ is considered by default.",
    "8-2": "ON = 2022-02-20",
    "9-0": "billingRule  \n**optional**",
    "9-1": "For UPI, this field is used to decide the limitation on the amount of recurring debit against the mandate amount which is set during registration transaction of UPI.  \n**Note**: This field is applicable only for UPI.  \nThe possible values are:  \n_  **MAX** = This is the maximum amount that a merchant can debit, that is, merchant can debit lesser or equal to this amount for a recurring transaction.  \n_  **EXACT**= This the exact amount that a merchant can debit in recurring debits.  \n  \nNote: If no value is passed, ‘MAX’ is considered by default.",
    "9-2": "MAX = 5000",
    "10-0": "billingDate  \n**optional**",
    "10-1": "**Applicable for UPI only**: This field is used to decide the date/day, basis which the recurring debit should happen. This can be ignored and the debit will happen as per the start date in every cycle.",
    "10-2": "FORTNIGHTLY = 7",
    "11-0": "authpayuid  \n**mandatory for modifying subscription with cards**",
    "11-1": "This field is used only to modify an existing subscription/consent. Modification means modifying billing details like startDate, endDate, billing cycle, billing interval, billing amount.",
    "11-2": " ",
    "12-0": "action  \n**mandatory for cards**",
    "12-1": "This field is used to modify or cancel an existing subscription. Include **modify** to modify a subscription.",
    "12-2": "modify"
  },
  "cols": 3,
  "rows": 13,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### **si\_details JSON example**

For a yearly plan starting from 1st January 2019, having a monthly billing amount of INR 100, the plan details:

```plaintext
{
  "billingAmount": "10.00",
  "billingCurrency": "INR",
  "billingCycle": "MONTHLY",
  "billingInterval": 1,
  "paymentStartDate": "2022-02-04",
  "paymentEndDate": "2022-12-12",
  "action": "modify",
  "authPayuId": "123"
}
```

## **Sample request**

```curl
curl -X \
 POST "https://test.payu.in/_payment-H "accept: application/json" -H \
 "Content-Type: application/x-www-form-urlencoded" -d”key=JP**g&txnid=56bb2e3fcb510f1c1521&amount=10000&firstname=Payu-Admin&email=test@example.com&phone=1234567890&productinfo=iPhone&api_version=7&si=3&pg=CC&bankcode=UTIBENCC&surl=https://test.payu.in/admin/test_response
/&furl=https://test.payu.in/admin/test_response
&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=Test User&si_details={“billingAmount”: “100.00”,”billingCurrency”: “INR”,”billingCycle”: “MONTHLY”,”billingInterval”: 1,”paymentStartDate”: “2022-09-01″,”paymentEndDate”: “2022-12-01”,“authpayuid" : "403993715525316543","action":"modify"}
&hash=e36568b2dfc460eab0eb3387fb7d90543ed861154f273b9593d6fcc152ed93a91e529c2f4be0965eeb57104e82d58889fa5efb52811ec78cbd1ad646e39c29a0”
```

## Sample response

```
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