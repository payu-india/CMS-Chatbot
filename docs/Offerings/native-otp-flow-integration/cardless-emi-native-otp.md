---
title: Cardless EMI - Native OTP
deprecated: false
hidden: false
metadata:
  robots: index
---
The steps involved in cardless EMI with Native OTP:

1. [Check pre-EMI eligibility](#step-1-check-pre-emi-eligibility)
2. [Initiate the payment request](#step-2-initiate-the-payment-to-payu)
3. [Submit the OTP](#step-3-submit-the-OTP)

### Step 1: Check pre-EMI eligibility

Before initiating a payment request for a customer, it is necessary to check their eligibility using the **Get Checkout Details** API. For more information, refer to [Get Checkout Details API](ref:get_checkout_details#check-customer-eligibility).

### Step 2: Initiate the payment request

<Accordion title="Request parameters" icon="fa-table">
  Send the following additional parameters to PayU through a server-to-server curl request to initiate the payment. As a result of this API call, the customer will receive the OTP. For sample request and response, refer to [Collect Payment API - Server-to-Server](ref:_payment_server_to_server).

  | **Parameter**                 | **Description**                                                  | **Example**  |
  | ----------------------------- | ---------------------------------------------------------------- | ------------ |
  | panNumber `mandatory`         | `String` PAN number of the customer.                             | ABCDE1234A   |
  | s2s\_device\_info `mandatory` | `String` This parameter must have the customer agent's device.   | Mozilla      |
  | s2s\_client\_ip `mandatory`   | `String` This parameter must have the source IP of the customer. | 10.11.101.11 |
  | txn\_s2s\_flow `mandatory`    | `String` This parameter must be passed with the value as 4.      | 4            |

  📘 **Notes for panNumber**:

  * **Only 4-digit number of the PAN**: Pass the 4-digit numeral in a sequential order as in the PAN.
  * This parameter is mandatory for ICICI Bank and HDFC Bank Cardless EMI. Not mandatory for other banks.
  * The data validation performed is either the whole PAN card number or 4-digit number of the PAN:
    * **Whole PAN card number**: For validating the whole PAN card number:
      * It should be ten characters long.
      * The first five characters should be any uppercase alphabets.
      * The next four characters should be any number from 0 to 9.
      * The last (tenth) character should be any uppercase alphabet. It should not contain white spaces.
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  Below is a sample cURL request for initiating the payment.

  ```curl
  curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "txnid=EaE4ZO3vU4iPsp" \
  -d "amount=10.00" \
  -d "firstname=Ashish" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "productinfo=iPhone" \
  -d "pg=EMI" \
  -d "bankcode=EMI03" \
  -d "surl=https://apiplayground-response.herokuapp.com/" \
  -d "furl=https://apiplayground-response.herokuapp.com/" \
  -d "ccnum=1234" \
  -d "ccexpmon=05" \
  -d "ccexpyr=2022" \
  -d "ccvv=123" \
  -d "ccname=undefined" \
  -d "store_card_token=1234 4567 2456 3566" \
  -d "storecard_token_type=1" \
  -d 'additional_info={"last4Digits": "1234", "tavv": "ABCDEFGH","trid":"1234567890", "tokenRefNo":"abcde123456"}' \
  -d "panNumber=ABCDE1234A" \
  -d "s2s_device_info=Mozilla" \
  -d "s2s_client_ip=10.11.101.11" \
  -d "txn_s2s_flow=4" \
  -d "hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
  ```

  Additional examples for this request have been provided in **JavaScript, Python, PHP, Java**, and **C#**. Each programming language script includes detailed API integration examples for initiating a Cardless EMI payment.
</Accordion>

### Step 3: Submit the OTP

Once your customer enters the OTP on the payment page (postUrl/acsTemplate), pass the OTP using the **Submit OTP** API. For more information, refer to [Submit OTP API](ref:submit-otp-to-payu).

#### Resend OTP

If the customer enters the incorrect OTP or an expired OTP, use [Resend OTP API](ref:resend-otp-api) to handle the **Resend OTP** request made by the customer.

### Step 4: Verify Payment

<Verify_Payment_Tabs />
