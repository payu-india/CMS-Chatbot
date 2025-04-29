---
title: PayU Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: >-
    PayU Hosted Checkout integration for International Payments or Dynamic
    Currency Conversion
  description: >-
    Learn how to integrate PayU’s Hosted Checkout feature with Dynamic Currency
    Conversion (DCC) to offer your customers a seamless and secure payment
    experience in their preferred currency. Follow the step-by-step procedure to
    set up your integration and start accepting international payments with
    PayU.
  keywords:
    - Dynamic Currency Conversion with PayU Hosted Checkout
    - DCC with Non-Seamless Integration
    - ' Currency Conversion with PayU Hosted Checkout'
    - Non-Seamless Integration for Currency Conversion
    - >-
      Multi-Currency Payment Integration with PayU Hosted Checkout.International
      Payments with PayU Hosted Integration
    - Foreign Currency Payment with PayU Hosted Integration
  robots: index
next:
  description: ''
---
The following diagram depicts the steps involved in the end-to-end integration process of International payments.

> 📘 Note:
> 
> You need to contact your PayU Key Account Manager to enable Dynamic Currency Conversion.

> 👍 Before you begin:
> 
> Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/07/International-Payments-E2E-Payment-Exp-1024x518.png)

***

### Steps to Integrate:

1. [Make the transaction request to PayU and check the response from PayU](#step-1-make-the-transaction-request-to-payu-and-check-the-response)
2. [Verify the payment](#step-2-verify-the-payment)

***

## Step 1: Make the transaction request to PayU and check the response

With the **POST REQUEST**, the customer will be redirected to the PayU’s payment page. The customer now selects the credit card payment option on PayU’s page and clicks the Pay Now button. PayU redirects the customer to the chosen payment method. The customer enters an international credit card number, and PayU displays the conversion. For the description of the request and response parameters, refer to Response Parameters section of <a href="_payment_payu_hosted_checkout" target="_blank">Collect Payments API</a>.

PayU marks the transaction status based on the response received from the bank. PayU provides the final transaction response string to the merchant through a POST RESPONSE. The parameters in this response are covered in the subsequent sections.

> 📘 Reference:
> 
> For a list of card details for testing dynamic currency conversion, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

> 📘 Notes:
> 
> - For DCC eligible transactions, no changes are required in the existing integration of Query transactions or Refund transactions. In case of refunds, the merchant can initiate refunds in INR (original amount and currency) only. PayU will internally convert the same into the final amount and currency charged to the consumer using the FX rate, which was applied on the date of sale.
> - There is no change required in handling the response from PayU as the response parameters are similar to the regular transaction
> - It is recommended to collect the customer’s e-mail address, phone, address, city, state, and country and then post those details along with the payment request with PayU. This will help in checking the risk of the transaction based on these data.

### Sample request

```
curl -X POST "https://test.payu.in/_payment"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00
&firstname=PayU User&email=test@gmail.com&phone=9876543210
&productinfo=iPhone&surl=
https://apiplayground-response.herokuapp.com/
&furl=https://apiplayground-response.herokuapp.com
&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
```

<br />

### Sample response

```
Array
(
    [mihpayid] => 403993715527769337
    [mode] => CC
    [status] => success
    [unmappedstatus] => captured
    [key] => smsplus
    [txnid] => 86e836b84be8dc6f7894
    [amount] => 10.00
    [cardCategory] => domestic
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2022-11-25 11:30:36
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
    [hash] => df565fdcbdd0172c42bf1ba1429c3f48e7215933574f932f37bb133ec4ac89d93535a1bf7674ec4514ffd238ec36e39524142b8d2415554ac7ced49707ea6940
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
    [PG_TYPE] => CC-PG
    [bank_ref_num] => e0e4a0ca-e356-412a-8f3a-9d69cede5a04
    [bankcode] => MASTCC
    [error] => E000
    [error_Message] => No Error
    [success_at] => 2022-11-25 11:33:41
    [cardnum] => XXXXXXXXXXXX1287
    [cardhash] => This field is no longer supported in postback params.
)
```

## Step 2: Verify the payment

Verify the transaction details using the **Verification Payment** API. For more information, For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>.

> 📘 Note:
> 
> The transaction ID that you posted in Step 1 with PayU must be used here.