---
title: Pay and Subscribe Consent Transaction using PayU Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: >-
    Pay and Subscribe Consent Transaction using PayU Hosted Checkout or
    Redirection-based Checlout
  description: >-
    Discover how to set up a Pay and Subscribe Consent Transaction using PayU
    Hosted Checkout. This API documentation provides detailed instructions for
    integrating PayU's one-time mandate feature, enabling flexible and secure
    payment options for your customers.
  keywords:
    - PayU One-Time Mandate API
    - ' One-Time Mandate Consent API'
    - ' PayU mandate transaction API'
    - ' PayU API for One-time mandate consent tranaction'
    - ' PayU recurring payments'
    - ' PayU one-time mandate for subscription payments'
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
---
To make an Pay and Subscribe consent transaction, you must post the **SI=4** instead of **SI=1** in case of payment consent transaction. You will share the billing details such as billing amount, start date, end date, billing interval, billing currency, billing cycle, etc. using the **_payment** API. After your user is redirected to the PayU Checkout page, all the eligible autopay payment modes will have **Register AutoDebit** option in specific section along with the enabled payment modes.

> 📘 Notes:
>
> * You need to enable the Pay and Subscribe on PayU Dashboard as per your requirements. For example, you want only UPI and cards instead of ENACH to be listed for the register auto-debit feature.
> * The request parameters includes **SI=4**, but rest of the parameters and response remains the same as in Payment Consent Transaction. For more information, refer to [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted).

## Request Parameters

The request parameters for the one-time mandate includes **SI=4** and rest of the parameter remains the same. For more information, refer to [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted#request-parameters).

## Sample Request

```curl
curl -X POST "https://test.payu.in/_payment" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=fM3O2HnkpJ8XEC&amount=100.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&si=4&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&si_details={"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2022-09-01","paymentEndDate": "2022-12-01"}&hash=2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5"
```

## Sample Response

The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

**Parsed response**

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