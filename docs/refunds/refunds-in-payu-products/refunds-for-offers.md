---
title: Refunds for Offers
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
PayU would refund the exact amount passed by you in the Refund request for instant discount or cashback offers.

## Refunds

PayU would refund the exact amount passed by the merchant in the Refund request. The merchant needs to adjust the discount amount before calling the [Refund Transaction API](ref:refund_transaction_api). Any refund request where the refund amount exceeds the actual amount deducted from the customer will fail. For more information, refer to [Refund Transaction API](ref:refund_transaction_api).

## Full Refund

To initiate a full refund the net debit amount needs to be passed in the refund request. For example, if the amount was INR 100 and the discount was INR 10, and if you wish to process a full refund, you will need to pass INR 90 as the refund amount. In case of a full refund, user velocity/user limits will be reset and the customer would be able to avail the offer again 

## Partial Refund

For partial refunds, the merchant needs to decide whether to deduct the discount amount or not. Whatever value the merchant passes in the refund request will be refunded back to the user. In case of a partial refund, user velocity/user limits will not be reset and the customer will not be able to avail the offer again 

## Refunds for Cashback Offer Transactions

There is no need for adjustment of refunds where cashback was applied earlier with the transaction. If the cashback has been processed by the bank, the cashback amount will not be refunded.

For example, if the amount was INR 100 and the cashback was ₹10 and if you wish to process a full refund, you will need to pass ₹100 as the refund amount.

In case you wish to adjust the cashback amount, reduce the cashback amount from the refund amount and submit it in the request.

In the above example, pass ₹90 as the refund amount 

## Instant Discount

You would need to adjust the discount amount before calling the **Cancel Refund Transaction** API. Any refund request where the refund amount exceeds the actual amount deducted from the customer will fail. For more information on **Cancel Refund Transaction** API, refer to [Refund Transaction API](ref:refund_transaction_api)

 

### **Example**

If the amount was ₹100 and the discount was ₹10, and if you wish to process a full refund, you will need to pass ₹90 as the refund amount.   
For partial refunds, you can decide whether to deduct the discount amount or not. You need to pass the exact value to be refunded back to the user.

## **Cashback Transactions**

There is no need to adjust refunds where cashback was applied earlier with the transaction. The cashback amount will not be refunded if the bank has processed the cashback. 

### **Example**

If the amount was ₹100 and the cashback was ₹10, and if you wish to process a full refund, you will need to pass ₹100 as the refund amount.  
If you wish to adjust the cashback amount, reduce it from the refund amount and submit it in the request.  
In the above example, pass ₹90 as the refund amount.