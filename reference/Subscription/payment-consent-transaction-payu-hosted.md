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
    - slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
      type: basic
    - slug: introduction-recurring-payments-integration
      title: Introduction
      type: basic
---
This section describes how to set up a Payment Consent or Registration transaction using PayU Hosted Checkout integration.

HTTP Method: **POST**

**Environment**

|                            |                                                                     |
| :------------------------- | :------------------------------------------------------------------ |
| **Production Environment** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment) |
| **Test Environment**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment)     |

## Request parameters

In the merchant-initiated POST REQUEST, Hash is a mandatory parameter. It is critical to calculate the hash correctly and post it to PayU in the request.


## Sample request

```curl
curl -X \
 POST "https://test.payu.in/_payment" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=fM3O2HnkpJ8XEC&amount=100.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc#bankcode=AIRPENCC&si=1&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&si_details={\"billingAmount\": \"100.00\",\"billingCurrency\": \"INR\",\"billingCycle\": \"MONTHLY\",\"billingInterval\": 1,\"paymentStartDate\": \"2022-09-01\",\"paymentEndDate\": \"2022-12-01\"}&hash=2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5"
```

Characters allowed for parameters

For parameters address1, address2, city, state, country, product info, email, and phone following characters are allowed:

* Characters: A to Z, a to z, 0 to 9
* – (Minus)
* \_ (Underscore)
* @ ()
* / (Slash)
* (Space)
* . (Dot)

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