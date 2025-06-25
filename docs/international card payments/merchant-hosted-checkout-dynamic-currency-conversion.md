---
title: Merchant Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: >-
    Merchant Hosted Checkout Integration for International Payments or Dynamic
    Currency Conversion
  description: >-
    Learn how to integrate PayU’s Merchant Hosted Checkout feature with Dynamic
    Currency Conversion (DCC) to offer your customers a customized and secure
    payment experience in their preferred currency. Follow the step-by-step
    procedure to set up your integration and start accepting international
    payments with PayU.
  keywords:
    - Dynamic Currency Conversion with Merchant Hosted Checkout
    - DCC with Seamless Integration
    - ' Currency Conversion with Merchant Hosted Checkout'
    - Seamless Integration for Currency Conversion
    - >-
      Multi-Currency Payment Integration with Merchant Hosted
      Checkout.International Payments with Merchant Hosted Integration
    - Foreign Currency Payment with Merchant Hosted Integration
  robots: index
next:
  description: ''
---
This section describes how to integrate Dynamic Currency Conversion with Merchant Hosted Checkout Integration (Seamless Integration).

> 📘 Note:
>
> You need to contact your PayU Key Account Manager to enable Dynamic Currency Conversion.

> 👍 Before you begin:
>
> Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

### Steps to Integrate:

1. [Check the Card BIN](#step-1-check-the-card-bin)
2. [Post the parameters to PayU](#step-2-post-the-parameters-to-payu)
3. [Check the response from PayU](#step-3-check-the-payment-response-from-payu)
4. [Verify the payment](#step-4-verify-the-payment)

***

## Step 1: Check the card BIN

Check if the card number of the customer is international or domestic using the **Check is Domestic** API. This is to avoid payment failure and validation of the card BIN. For more information, refer to [Check is Domestic API](ref:check_is_domestic_api) under API Reference.

## Step 2: Post the parameters to PayU

Make the transaction request with the payment details provided by the customer to PayU. For the description of the request and response parameters, refer to <a href="_payment_merchant_hosted" target="_blank">Collect Payments API</a>.

> 📘 Note:
>
> It is recommended to collect the customer’s e-mail address, phone, address, city, state, and country and then post those details along with the payment request with PayU. This will help in checking the risk of the transaction based on these data.

<HashingRequestParameters />

### Sample request

```curl
curl --request POST \
     --url https://test.payu.in/_payment \
     --header 'Content-Type: application/x-www-form-urlencoded' \
     --header 'accept: text/plain' \
     --data key=JPM7Fg \
     --data surl=https://test-payment-middleware.payu.in/simulatorResponse \
     --data furl=https://test-payment-middleware.payu.in/simulatorResponse \
     --data pg=CC \
     --data bankcode=CC \
     --data txnid=sdjkfd133 \
     --data amount=100 \
     --data productinfo=iPhone \
     --data firstname=Raghuram \
     --data email=abc@google.com \
     --data phone=9876543210 \
     --data ccnum=54265X5211123499 \
     --data ccvv=123 \
     --data ccname=Ashish \
     --data ccexpmon=05 \
     --data ccexpyr=2033 \
     --data hash=6f3a91964acc3788fbefee71f628e8924ca1dc06c6142aadf81b0311cea5e748f771d0d14a5daf6c6585de117b79612fb43a41e2eb3b0db1f0ae12b3f281d9fe
```

## Step 3: Check the response from PayU

<ReverseHashing />

### Sample response

```
Array
(
    [mihpayid] => 4***9371***40***25
    [mode] => NB
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => bvRCCBO4YiGGHE
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2021-09-06 13:59:39
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => abc@gmail.com
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
    [hash] => fa7bb889d25b2a60bcf32316d1c9346589ff3de012dd0c66aa47ec12f1349837163ef8a603bd8b357de610b768f08dc4fb3bb4702d1ca6d9751300667fd763a6
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
    [bank_ref_num] => ae67e632-f4eb-4121-b47b-2d35dce5ec2e
    [bankcode] => CC
    [error] => E000
    [error_Message] => No Error
)
```

## Step 4: Verify the payment

Verify the transaction details using the **Verification Payment** API. For more information, For API reference, refer to [Verify Payment API](refverify_payment_api)

> 📘 Note:
>
> The transaction ID that you posted in Step 1 with PayU must be used here.