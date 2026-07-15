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
To make an Pay and Subscribe consent transaction, you must post the **SI=4** instead of **SI=1** in case of payment consent transaction. You will share the billing details such as billing amount, start date, end date, billing interval, billing currency, billing cycle, etc. using the **\_payment** API. After your user is redirected to the PayU Checkout page, all the eligible autopay payment modes will have **Register AutoDebit** option in specific section along with the enabled payment modes.

<Callout icon="📘" theme="info">
  ###

  **Notes**:

  - You need to enable the Pay and Subscribe on PayU Dashboard as per your requirements. For example, you want only UPI and cards instead of ENACH to be listed for the register auto-debit feature.
  - The request parameters includes **SI=4**, but rest of the parameters and response remains the same as in Payment Consent Transaction. For more information, refer to [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted).
</Callout>

## Request Parameters

The request parameters for the one-time mandate includes **SI=4** and rest of the parameter remains the same. For more information, refer to [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted#request-parameters).

## Sample Request

```curl
curl --location 'https://secure.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642; PHPSESSID=68ed52caaaf5e' \
--data-urlencode 'key=BmTY3G' \
--data-urlencode 'txnid=my_order_49428' \
--data-urlencode 'amount=1' \
--data-urlencode 'firstname=PayU User' \
--data-urlencode 'email=test@gmail.com' \
--data-urlencode 'phone=9876543210' \
--data-urlencode 'productinfo=my_order_49428' \
--data-urlencode 'si=4' \
--data-urlencode 'surl=https://apiplayground-response.herokuapp.com/' \
--data-urlencode 'furl=https://apiplayground-response.herokuapp.com/' \
--data-urlencode 'si_details={billingAmount: 1.00,billingCurrency: INR,billingCycle: MONTHLY,billingInterval: 1,paymentStartDate: 2025-10-14,paymentEndDate: 2027-12-01}' \
--data-urlencode 'hash=67de5db43d30293e715969e6d7d849cea689b189509488c3a2b5615865f886559848bac2b1ddad5a53a5b38daaf48cd2bf9c06366c416c3da52ca47e96020cbb'
```

## Sample Response

The response URL returned from PayU is in the form URL format (application/x-www-form-urlencoded).

**Parsed response**

```json
Array
(
    [mihpayid] => 25630643428
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => BmTY3G
    [txnid] => 6af8cb1dd0d57b2b4761
    [amount] => 1.00
    [cardCategory] => signature_premium
    [discount] => 0.00
    [net_amount_debit] => 1
    [addedon] => 2025-10-16 13:06:55
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
    [hash] => c07e7e3d551445962778d801f9ef414cf75819d3cde63c3911ccacacda8981099e42806c0bf56f9bcd417b7d42873f46ae52a2102d7ca9f850d19d3ecdb7240b
    [field1] => CBC1016073720213F90DXW1
    [field2] => 120330
    [field3] => 
    [field4] => 
    [field5] => 
    [field6] => 05
    [field7] => AUTHPOSITIVE
    [field8] => 0 | Transaction Completed
    [field9] => Transaction Completed
    [payment_source] => payu
    [meCode] => {"wibmo_merchant_id":"16329672","hash_key":"b5b013c18d762b6ccbe8d2e8b1e9ec02fe642013524ed02b91846978f8eafa70","acquirer_merchant_id":"175645866049780","mcc":"5499"}
    [PG_TYPE] => CC-PG
    [bank_ref_num] => 528907093881
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
    [cardToken] => 2be916cfaeddc64a196988
    [card_token] => 2be916cfaeddc64a196988
    [cardnum] => XXXXXXXXXXXX4879
)
```

<Callout icon="📘" theme="info">
  ### **Note:**

  The combination of `unmappedstatus`, `status`, and `payment_source` determines the mandate and transaction outcome in the above response.

  | Mandate Status | Transaction Status | unmappedstatus | status  | payment_source |
  | -------------- | ------------------ | -------------- | ------- | -------------- |
  | Successful     | Successful         | captured       | success | sist           |
  | Failed         | Successful         | captured       | success | payu           |
  | Failed         | Failed             | failed         | failure | payu           |
  | Successful     | Failed             | Not possible   | N/A     | N/A            |
</Callout>

<br />
