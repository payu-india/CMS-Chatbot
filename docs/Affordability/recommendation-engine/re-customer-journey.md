---
title: Customer Journey
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
In this document we shall see how payment modes are displayed on the PayU payment page when the Recommendation Engine is optimised for different goals.

## Goal: Success rate

In the following example the user is logged in and the RE is optimized for Sucecss Rate (SRT). Which means that the payment instrument with the higher success rate will be prioritised in both the L1 and L2 screens of the PayU payment page. 

Here, the SRT of Airtel Money wallet is higher for the given transaction amount. Hence, Airtel Money is priroritized on the L1 and L2 screen.

### L1 Screen

<Image align="center" width="50% " src="https://files.readme.io/49b5a7a-Screenshot_2023-08-28_at_1.00.07_AM.png" />

### L2 Screen

<Image align="center" width="50% " src="https://files.readme.io/8c81007-Screenshot_2023-08-28_at_1.00.44_AM.png" />

***

## Goal: Cost of the payment mode

In the following example the user is logged in and the RE is optimised for Cost. Which means that the payment mode with the lower cost will be prioritised on both the L1 and L2 screen of the PayU payment page. 

Here, the average cost of UPI payment is lower that the other payment modes. Hence, UPI is prioritised on the L1 screen. For example, If the average cost of processing is lower for Paytm wallet compared to Amazon Pay, Paytm wallet will be prioritised over Amazon Pay.

### L1 Screen

<Image align="center" width="50% " src="https://files.readme.io/9324886-Screenshot_2023-08-28_at_1.02.48_AM.png" />

### L2 Screen

<Image align="center" width="50% " src="https://files.readme.io/ddfa909-Screenshot_2023-08-28_at_1.03.43_AM.png" />

***

## Goal: Affordability

In the following example the user is logged in and the RE is optimised for Affordability. Hence, affordability is prioritised on both the L1 and L2 screen.

<Image align="center" width="50% " src="https://files.readme.io/3aca2d0-Screenshot_2023-08-28_at_1.05.22_AM.png" />
