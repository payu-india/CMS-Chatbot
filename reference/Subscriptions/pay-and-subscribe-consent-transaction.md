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

<Callout icon="📘" theme="info">
  **Notes**:

  * You need to enable the Pay and Subscribe on PayU Dashboard as per your requirements. For example, you want only UPI and cards instead of ENACH to be listed for the register auto-debit feature.
  * The request parameters includes **SI=4**, but rest of the parameters and response remains the same as in Payment Consent Transaction. For more information, refer to [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted).
</Callout>

## Request Parameters

The request parameters for the one-time mandate includes **SI=4** and rest of the parameter remains the same. For more information, refer to [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted#request-parameters).

## Sample Request

```curl
curl -X POST "https://test.payu.in/_payment" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=fM3O2HnkpJ8XEC&amount=100.00&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&si=4&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&si_details={"billingAmount": "100.00","billingCurrency": "INR","billingCycle": "MONTHLY","billingInterval": 1,"paymentStartDate": "2022-09-01","paymentEndDate": "2022-12-01"}&hash=2ad878f64de47c7c1149ff554cd00ee44555a8512a1d2cff9690d6ea3c9d9de0bc44b0e77c61dd60a3c64ef970612a9b71761559aa202d2a278d29dc87b998c5"
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
