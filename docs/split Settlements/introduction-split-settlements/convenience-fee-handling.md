---
title: Convenience Fee Handling
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
A convenience fee is a fee charged by a business for payments made through an alternative channel, that is, credit card or online payment instead of cash or cheque. For example, movie tickets booked online on a movie ticket aggregator website comes with a convenience fee, an extra charge the consumers have to pay for doing the bookings from the comforts of their home. 

This section describes convenience fee handling in Aggregator Flow and sample Split Settlement JSON with convenience fee.

The parent merchant can be on any one of the following models:

* TDR Model
* Convenience Fee Model

> 📘 Note:
>
> The convenience fee will not be refunded to the parent when refund is requested for a transaction.

## Split details for Convenience fee

* The convenience fee will be applied to parent only.\
  For example, if a transaction T is Rs 100 and the convenience is Rs 10 and there is a split as follows:
  * **T1**: INR 40 (transaction fee: 40, amount:40) on C1(normal child)
  * **T2**: INR 60 (transaction fee: 60, amount:60) on C2(normal child).
  * **T3**: INR 10(transaction fee: 0, amount: 10)

> 📘 Notes:
>
> * PayU will automatically calculate the convenience fee (T3 as in the above list) as own child transaction. The convenience fee is based on configuration during onboarding. For more information, contact your PayU Key Account Manager (KAM). 
> * In this case, to adjust convenience, one parent’s own child transaction would be created T3 with INR 10 (transaction fee: 0, amount: 10) which contains the convenience fee.

## Sample request

Split JSON request for the example described in [Split Details for Convenience Fee](#split-details-for-convenience-fee). For a list of request parameters for split payment requests, refer to the following sections:

* [Split During Payment](ref:splitduringpayment)
* [Split After Transaction API](ref:split_after_transaction_api)

For a complete list of request parameters, refer to [Merchant Hosted Checkout Integration](doc:custom-checkout-merchant-hosted)

> 📘 Note:
>
> When you making a payment request to PayU, there is no request parameter to specify the convenience fee in the request and convenience fee is completely handled by PayU back-end.

```curl
{
  "type": "absolute",
  "splitInfo": {
    "merchantKey1": {
      "aggregatorSubTxnId": "T1",
      "aggregatorSubAmt": "40"
    },
    "merchantKey2": {
      "aggregatorSubTxnId": "T2",
      "aggregatorSubAmt": "60"
    }
  }
}
```

## Sample response

The **splitStatus** parameter in JSON format of response for the Split Details for Convenience Fee with Example. The additionalCharges field in the JSON contains the convenience fee details and it is applied only for parent own child. The transaction\_fee field in the JSON contains the amount split for each child.

```
{
  "splitStatus": "success",
  "splitSegments": [
    {
      "merchantKey": "merchantKey1",
      "amount": 40,
      "subvention_amount": 0,
      "txnId": "T1",
      "discount": 0, 
      "additionalCharges": 0, 
      "transaction_fee": 40 
    },
    {
      "merchantKey": "merchantKey2",
      "amount": 60,
      "subvention_amount": 0,
      "txnId": "T2",
      "discount": 0,
      "additionalCharges": 0,
      "transaction_fee": 60
    },
    {
      "merchantKey": "parentMerchantKey",
      "amount": 10,
      "subvention_amount": 0,
      "txnId": "T3",
      "discount": 0,
      "additionalCharges": 10,
      "transaction_fee": 0
    }
  ]
}
```

> 📘 Notes:
>
> * A single transaction can not work on both models (TDR + Convenience Fee). So, a transaction can be on either TDR flow or Convenience Fee Flow.
> * Convenience fee will not work along with subvention.
