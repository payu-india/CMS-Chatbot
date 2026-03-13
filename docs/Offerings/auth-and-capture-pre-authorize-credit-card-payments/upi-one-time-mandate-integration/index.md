---
title: UPI One-Time Mandate Integration
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
UPI is continuously expanding with various use cases being developed to support UPI payments. One such feature is the UPI One-Time Mandate (OTM). 

In UPI One-Time Mandate, funds are temporarily blocked in the customer's account at the time of the transaction for a specified period (up to a maximum of 60 days). The actual debit from the customer's account is made only when the merchant initiates the request to capture the payment. Else, amount will be released back in the customer’s account. 

## Use Cases of UPI OTM

There are several scenarios for adjusting an authorization. Some examples include: 

**Hospitality Industry**

Hotels can pre-authorize payments for rooms that guests have pre-booked. If a guest decides to cancel one of the pre-booked rooms before arrival, the hotel can adjust these expenses from the pre-authorized amount. Upon check-out, the hotel can capture the final adjusted amount using partial capture. 

**Travel**

A self-drive car rental platform often collects security deposits along with variable expenses. The merchant can pre-authorize the payment with an extra margin. At the end of the trip, the merchant can adjust the authorized amount and perform a partial or full capture based on the expenses incurred. 

**Insurance**

As per recent IRDAI guidelines, for health and term life insurance, funds can’t be debited from the customer’s account till the time policy is issued. Since health and term insurance requires 5-10 days as pre-check, and then only insurance agencies are sure for issuance, OTM helps them solve the payment flow. When customer applies for policy, it can block the amount and only for the cases where policy is issued, debit can happen after issuance. 

**Ecommerce**: 

For any product, a mandate can be set up for the product amount. The amount will be deducted only when the product is delivered.

## How UPI OTM Works

1. **Authorization**: When a customer places an order, the merchant can temporarily block a specific amount of funds in the customer's account. The merchant is thus assured of receiving the funds at the time of rendering the service on a future date. 
2. **Capture**: Once the merchant decides to capture the amount (usually after the goods or services are delivered), the blocked amount is debited from the customer's account. In case of partial capture, the balance is auto unblocked in the customer's account. 
3. **Cancellation**: If the order is canceled by the customer within a specific time frame, the transaction can be marked as canceled. In this case, the blocked amount is immediately released and returned to the customer's original payment source. 

## Features of UPI OTM

* **Fund Assurance**: Unlike 7 days for cards, funds are held by the customer’s account for up to 60 days. 
* **Enhanced Customer Experience**: If a transaction is canceled, the amount is instantly credited back to the payer’s source account, ensuring a smoother refund process. 
* **Seamless Merchant Experience**: UPI OTM allows merchants to block a specific amount in the customer's account at the time of order placement and capture the payment only when needed. The capture confirmation is also received real-time, providing additional factor of confidence to the customer. This helps in scenarios like pre-orders, reservations, and delayed deliveries. 

##  Workflow of UPI OTM: 

**Block:** 

* UPI OTM allows merchants to block funds in a customer's account without actually debiting the funds. 
* The merchant can set the block period for up to 60 days (can be shorter, but not longer). 
* Guaranteed availability of funds as long as the block is 'Active.' 

**Capture:** 

* The merchant can choose to activate the fund flow once the service is rendered by using 'Capture.' 
* When 'Capture' is invoked, a real-time debit from the customer's account occurs. 
* If 'Capture' fails, the merchant can retry, providing an opportunity to improve the success rate. 

**Release:** 

* In cases where the service was not provided, the merchant can choose not to activate the fund flow by using 'Release.' 
* The merchant can release the funds any time before the set period. 
* Funds are automatically released after the period expires or after 60 days, whichever is earlier. 

**Refunds:** 

* For successfully captured funds, refunds are supported similar to standard UPI transactions. 

> 📘 Note:
>
> Currentyly, NPCI is not allowing PA'a to support multiple captures on a single authorization request. It supports single capture only - either full or partial.

UPI OTM is supported for below flows with various integrations: 

* Merchant Hosted Integration (seamless flow)
  * [UPI Intent](doc:upi-intent-one-time-mandate-integration)
  * [UPI Collect](doc:upi-collect-one-time-mandate-integration)

For checking the UPI OTM status, use the [UPI OTM Status Check API](ref:upi-otm-status-check-api).
