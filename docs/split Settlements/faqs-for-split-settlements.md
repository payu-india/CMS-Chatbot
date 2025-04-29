---
title: FAQs
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
## General

- **Does the Aggregator model support surcharge or convenience fee model?**

   Currently, TDR is supported. PayU will be adding a convenience fee to the Aggregator model soon.

- **Does the Aggregator model have a separate Dashboard for the aggregators to monitor the transactions, settlements and refunds?**

     Yes, there will be separate Dashboards for parent and child merchants. Parent merchants will be able to view the details regarding their transactions and that of child merchants’ but child merchants can view details of only their transactions.

- **Can the parent and child merchants download invoices from Dashboard?**

     Yes, the parent merchant can download for themselves and their child merchants. Child merchants will be able to download for themselves only.

- **Where can I find the test card details for split settlement transactions?**

     The test card for split settlement transactions is same as Web Checkout. For more information, refer to [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).

***

## Transactions

- **Is there a limit to the number of child merchants, one transaction can be split?**

     No, there is no limit on the number of child merchants linked to a parent merchant.

- **Are all the payment modes will be processed in the Aggregator flow?**

     Yes, the aggregator flow will support all the payment modes supported on PayUBiz.

- **Who must provide the split information?**

     Only the aggregator or parent merchant can provide the split information.

- **When can the aggregator give the split information?**

     The aggregator can share the split information at the time of the transaction or after the transaction.

- **Where can I find the APIs to share the split information?**

     For API documentation to split a transaction, refer to [Create the Split](doc:create-the-split)

- **How is PayU supporting the split payments? Does it support split by percentage?**

     Yes, PayU supports absolute split and split by percentage. For more information, refer to the following: 

  - [Split During Payment](ref:splitduringpayment)
  - [Split After Transaction API](ref:split_after_transaction_api)

- **What is the minimum amount to create a split? Can parent take no amount (Rs.0) and settle the whole amount to the child or vice-versa?**

     Yes, a 100:0 ratio is possible. For more information, refer to [Split During Payment](ref:splitduringpayment) > [Split transaction with only single child](/reference/split-during-transaction-using-_payment#split-transaction-with-only-single-child).

- **If two child MIDs have different TDRs to be configured, can that be done?**

     Currently, TDR applies only to parent merchants.

- **Can we make multiple split calls for a transaction?**

     No, only one successful split call is allowed for a transaction.

- **What should I do if the split fails?**

     You can resend the split information if you get a failure response when you try to split a transaction. You need to call the **Split After Transaction** API. For more information, refer to [Split After Transaction API](ref:split_after_transaction_api)

- **How can a split be cancelled?**

     No, you cannot cancel a split transaction. You need to consider the split call as necessary as the transaction value call.

- **Can we get to know without calling the Split API which Seller is selling the product/service?**

     Merchant has to send Split information, which is mandatory information for you to know which seller is selling the product/service.

- **When one split fails, does the entire split call be marked as failed?**

     Yes, split creation is an automatic process. Either all the splits passed would get created, or none would get created.

- **If** the split call is a failure at the **PayU end, how many times does PayU retry**? & After maximum attempts, what are the next steps when the status is a failure**? What is the process in place?**

 Split creation can fail due to multiple reasons, including validation errors and system faults. In case of a validation error, you must call the Split API again after correcting the request payload.

 If split creation got failed due to system faults(query execution failed etc.), PayU does retry internally before providing a success or failed response.

No internal retries are done after providing a failure response.

- **Can I split during the** transaction with 100% allocation for a **single child?**

     Yes, you can split with 100% allocation for a single child. For more information, refer to  [Split During Payment](ref:split-during-transaction-using-_payment#split-transaction-with-only-single-child)

***

## Settlement

- **I am getting the following error message while using release\_settllement API. What is the reason for this error?**

```plaintext
{"status":"1","msg":"No transactions found for the requested page 5008042","Txn_details":[]}
```

 When there is a typo or an invalid merchant ID is specified in the request, the value of the **status** field of response is **1**. For more information, refer to [Settlement API](https://devguide.payu.in/split-apis/settlement-api/release-payment-api#Response).

- **Is it possible to map multiple bank accounts for settlement in single-child MID?**

     A MID can be mapped to only to one bank account.

- **Can we make multiple split calls for Settlement APIs?**

     Settlement API (**release\_settlement** API) can be called individually for each split or can be called for multiple splits together. For more information on the **release\_settlement** API, refer to [Release Settlement API](ref:release_settlement_api).

- **In case of T+1 settlement time, for example, if the settlement time at PayU end is 10:00 AM daily, a transaction done at 9.55 AM on the same day will also be settled. In this case, a 5-minute interval. What is the time taken for settlement in case of T+0 settlement?**

     If it is of T+0 settlement, transactions happening after 00:00 hours will be settled in the settlement cycle of the next day only.

***

## Refunds

- **Where do I include the split information in the cancel\_refund\_transaction API when posting the cancellation of a transaction?**

     To post the split information, you must use the **var8** parameter in a JSON format (similar to the following example). For more information, refer to [Refund Transaction API](ref:refund_transaction_api)

```plaintext
{ "child_merchant_key_1": { "amount": 100, aggregatorRefundAmount: 40 }, "child_merchant_key_2": {"amount": 20, aggregatorRefundAmount: 0 }}
```

- **Who will be able to initiate the refunds?**

     Currently, only parent merchants can initiate the refunds for them and child merchants.

- **How can a refund be initiated?**

     You can use the refund APIs, and this functionality will be available soon on the PayU Dashboard. For more information on refund APIs, refer to [Refund APIs](ref:refund-apis-split-settlements).

- **For refund cases, can PayU use the parent entity account for processing the refunds without involving child entities?**

     The maximum refund a merchant can do is the amount available after the split in its share only.