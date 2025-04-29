---
title: Payment Consent Transaction using PayU Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Payment Consent Transaction using PayU Hosted Checkout
  description: >-
    Learn how to set up a Payment Consent or Registration transaction using PayU
    Hosted Checkout. This API documentation provides detailed instructions for
    integrating PayU's payment consent feature, enabling seamless recurring and
    subscription payments.
  keywords:
    - PayU Payment Consent API
    - ' PayU Hosted Checkout Subscription Registration Transaction'
    - ' Payment Consent Transaction for PayU Hosted Checkout'
    - ' PayU recurring payments registration transaction'
    - ' PayU hosted checkout subscription payments registration'
    - ' PayU hosted checkout subscription transaction consent'
    - ' Prebuilt Autopay integration'
    - ' Autopay for UPI non-PACB flow'
    - ' Pre-built Autopay Consent Transaction'
    - ' PayU Hosted Autopay'
    - ' Autopay for PayU Hosted non-PACB flow'
    - ' PayU Hosted Autopay Consent Transaction'
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
    - type: basic
      slug: introduction-recurring-payments-integration
      title: Introduction
---
This section describes the how set up a Payment Consent or <<glossary:Registration transaction>> transaction using PayU Hosted Checkout integration.

HTTP Method: **POST**

**Environment**

|                            |                                   |
| :------------------------- | :-------------------------------- |
| **Production Environment** | <https://secure.payu.in/_payment> |
| **Test Environment**       | <https://test.payu.in/_payment>   |

## Request parameters

In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.

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
    "2-1": "`float` This parameter should contain the payment amount of the particular transaction.  \n  \n**Note**: Type-cast the amount to float type  \nDepending upon the merchant use case, this value will vary.  \n  \n- It can be either 0 INR (for Net Banking) or min 1 INR (for Cards & UPI) in penny transaction use case.\n- In the case of first instalment use cases, this amount can be equal to initiate setup amount, but this use case will be supported only against selected Net Banking (ICICI and HDFC), all Credit / Debit Cards, and UPI",
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
    "7-0": "surl  \n**mandatory**",
    "7-1": "surL is the acronym for Success URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is successful.",
    "7-2": "",
    "8-0": "furl  \n**mandatory**",
    "8-1": "furl is the acronym for for Failure URL. This parameter must contain the URL on which PayU will redirect the final response if the transaction is failed.",
    "8-2": "",
    "9-0": "api_version  \n**mandatory**",
    "9-1": "This parameter must always needs to be passed as 7.",
    "9-2": "7",
    "10-0": "si  \n**mandatory**",
    "10-1": "This parameter signifies a successful consent taken from the user by the merchant. This parameter must contain 1 for a successful consent. Without this parameter sent as 1, subscription cannot be set up.  \n**Notes**: You can modify or cancel existing recurring payment registration as described in the following sections:  \n_.   [Manage Recurring Payment for Cards](ref:manage-recurring-payment-for-cards)  \n_.   [Manage UPI Recurring Transaction](ref:api-commands-to-manage-upi-recurring-transaction)",
    "10-2": "1",
    "11-0": "free_trial  \n**optional**",
    "11-1": "This is mandatory only if the merchant wants to support free trial use case with card and net banking together that too on PayU Hosted Checkout integration.  \n  \nIn this case, PayU adjusts the transaction amount as INR 2.00 for cards. INR 0.00 for Net Banking and UPI registration irrespective of what amount is passed against the amount field in the request.  \nThis parameter has no significance in the case of seamless flow.",
    "11-2": "",
    "12-0": "si_details  \n**mandatory**",
    "12-1": "This parameter represents mandatory details which need to be passed to during registration transaction from merchant system to PayU.  \n  \n**Note**: It is mandatory as per the latest RBI guidelines to pass this information to the payment processor so that same can be forwarded to acquirers and issuers ( for more details refer – <https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=11668&Mode=0> )  \n  \nThis is a JSON object and it includes a set of fields. For more information,  refer to [SI Parameter JSON Details](ref:si-parameter-json-details)",
    "12-2": "{“billingAmount”: “100.00”,”billingCurrency”: “INR”,”billingCycle”: “MONTHLY”,”billingInterval”: 1,”paymentStartDate”: “2019-09-01″,”paymentEndDate”: “2019-12-01”}",
    "13-0": "hash  \n**mandatory**",
    "13-1": "Hash is a crucial parameter used to ensure that any date is not tampered while redirecting customer from the merchant website to PayU’s payment interface while registration transactions.  \n  \nIt is SHA512 hash generated by encrypting values of merchant key, txnid, amount, productinfo, firstname, email, udf and si_details by merchant salt.  \n  \nIn the case of registration transaction, the formula is used to calculate this hash is similar to the following:  \n`HASH = SHA512(key\\|txnid\\|amount\\|productinfo\\|firstname\\|email\\|udf1\\|udf2\\|udf3\\|udf4\\|udf5\\||\\||\\||si_details\\|SALT)`",
    "13-2": ""
  },
  "cols": 3,
  "rows": 14,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


## Sample request

```curl
curl -X \
 POST "https://test.payu.in/_payment"-H "Content-Type: application/x-www-form-urlencoded" -d"key=JP***g&txnid=fM3O2HnkpJ8XEC&amount=100.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc#bankcode=AIRPENCC&si=1&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&si_details={“billingAmount”: “100.00”,”billingCurrency”: “INR”,”billingCycle”: “MONTHLY”,”billingInterval”: 1,”paymentStartDate”: “2022-09-01″,”paymentEndDate”: “2022-12-01”}&hash=2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5"
```

Characters allowed for parameters

For parameters address1, address2, city, state, country, product info, email, and phone following characters are allowed:

- Characters: A to Z, a to z, 0 to 9
- – (Minus)
- \_ (Underscore)
- @ ()
- / (Slash)
- (Space)
- . (Dot)

## Sample response

The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

### Parsed response

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