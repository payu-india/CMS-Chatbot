---
title: Cardless EMI - Native OTP Flow
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The steps involved in cardless EMI with Native OTP:

1. [Check pre-EMI eligibility](#step-1-check-pre-emi-eligibility)
2. [Initiate the payment request](#step-2-initiate-the-payment-to-payu)
3. [Submit the OTP](#step-3-submit-the-OTP)

## Step 1: Check pre-EMI eligibility

Before initiating a payment request for a customer, it is necessary to check their eligibility using the **Get Checkout Details** API. For more information, refer to [Get Checkout Details API](ref:get_checkout_details#check-customer-eligibility).

## Step 2: Initiate the payment request

Send the following additional parameters to PayU through a server-to-server curl request to initiate the payment. As a result of this API call, the customer will receive the OTP. For sample request and response, refer to [Collect Payment API - Server-to-Server](ref:_payment_server_to_server).

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "panNumber  \n`mandatory`",
    "0-1": "`String`  PAN number of the customer.",
    "0-2": "ABCDE1234A",
    "1-0": "s2s\\_device\\_info  \n`mandatory`",
    "1-1": "`String`  This parameter must have the customer agent’s device.",
    "1-2": "Mozilla",
    "2-0": "s2s\\_client\\_ip  \n`mandatory`",
    "2-1": "`String` This parameter must have the source IP of the customer.",
    "2-2": "10.11.101.11",
    "3-0": "txn\\_s2s\\_flow  \n`mandatory`",
    "3-1": "`StringString` This parameter must be passed with the value as 4.",
    "3-2": "4"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


> 📘 Notes for panNumber:
> 
> - **Only 4-digit number of the PAN**: Pass the 4-digit numeral in a sequential order as in the PAN.
> - This parameter is mandatory for ICICI Bank and HDFC Bank Cardless EMI. Not mandatory for other banks
> - The data validation performed is either the whole PAN card number or 4-dig-t number of the PAN.
>   - Whole PAN card Number: For validating the whole PAN Card number:
>     - It should be ten characters long.
>     - The first five characters should be any upper case alphabets.
>     - The next four-characters should be any number from 0 to 9.
>     - The last(tenth) character should be any upper case alphabet. It should not contain any white spaces.

## Step 3: Submit the OTP

Once your customer enters the OTP on the payment page (postUrl/acsTemplate), pass the OTP using the **Submit OTP** API. For more information, refer to [Submit OTP API](ref:submit-otp-to-payu).

#### Resend OTP

If the customer enters the incorrect OTP or an expired OTP, use [Resend OTP API](ref:resend-otp-api) to handle the **Resend OTP** request made by a customer.