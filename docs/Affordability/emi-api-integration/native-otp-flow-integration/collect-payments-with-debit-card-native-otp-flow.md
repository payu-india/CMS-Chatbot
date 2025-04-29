---
title: Debit Card EMI - Native OTP Flow
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
The steps involved in debit card integration with native OTP flow:

1. [Check Pre-EMI Eligibility](#step-1-check-pre-emi-eligibility)
2. [Initiate the payment request](#step-2-initiate-the-payment-request)
3. [Submit the OTP](#step-3-submit-the-otp)

## Step 1: Check Pre-EMI Eligibility

Before initiating a payment request for a customer, it is necessary to check their eligibility using the **Get Checkout Details** API. For more information, refer to [Get Checkout Details API](ref:get_checkout_details#check-customer-eligibility).

## Step 2: Initiate the payment request

Send the transaction information to PayU through a server-to-server curl request to initiate the transaction. As a result of this API call, the customer will receive the OTP. For more information, refer to [Collect Payment API - Server-to-Server](ref:_payment_server_to_server).

<Table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>s2s\_device\_info `mandatory`</td>
      <td>`String` This parameter must have the customer agent’s device.  <br>**Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.</td>
      <td>Mozilla</td>
    </tr>
    <tr>
      <td>s2s\_client\_ip\ `mandatory`</td>
      <td>`String` This parameter must have the source IP of the customer.  <br>**Note**: This information is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information.</td>
      <td>10.11.101.11</td>
    </tr>
    <tr>
      <td>txn\_s2s\_flow\ `mandatory`</td>
      <td>`String` This parameter must be passed with the value as 4.</td>
      <td>4</td>
    </tr>
  </tbody>
</Table>

## Step 3: Submit the OTP

Once your customer enters the OTP on the payment page (postUrl/acsTemplate), pass the OTP using the **Submit OTP** API. For more information, refer to [Submit OTP API](ref:submit-otp-to-payu).

#### Resend OTP

If the customer enters the incorrect OTP or an expired OTP, use [Resend OTP API](ref:resend-otp-api) to handle the Resend OTP request made by a customer.