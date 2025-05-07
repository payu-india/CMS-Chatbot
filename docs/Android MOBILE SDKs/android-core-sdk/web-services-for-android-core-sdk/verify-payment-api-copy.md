---
title: Verify Payment API (COPY)
deprecated: false
hidden: true
metadata:
  title: Verify Payment API - Android Core SDK
  robots: index
---
The **Verify Payment** API is used to reconcile the transaction with PayU. When PayU posts back the final response to you (merchant), PayU provides a list of parameters (including the status of the transaction). For example, success, failure, etc. On a few occasions, the transaction response is initiated from our end, but it does not reach you due to network issues or user activity (like refreshing the browser, etc.).

> 📘 Note:
>
> PayU strongly recommends that this API is used to reconcile with PayU’s database once you receive the response. This will protect you from any tampering by the user and help in ensuring safe and secure transaction experience.

## Step 1: Set parameters

For this API, you need to set transactionID inside your payment parameters for instance:

```Text Java
MerchantWebService merchantWebService = new MerchantWebService();
merchantWebService.setKey(merchantKey);
merchantWebService.setCommand(PayuConstants.VERIFY_PAYMENT);
merchantWebService.setVar1(txnId); // In this parameter, you can put all the transaction IDs, that is, txnid (your transaction ID/order ID) values separated by pipe or PayU ID.
merchantWebService.setHash(<Api Command Hash>) // Pass the Hash value, and use the below formula
```

> 📘 **Note**:
>
> You can send multiple txnIDs (transaction IDs) using the pipe symbol(|) as a separator.

## Step 2: Handle response

```Text Java
@Override
public void onVerifyPaymentResponse(PayuResponse payuResponse) {
    Log.d(TAG, "onVerifyPaymentResponse: " + payuResponse.getRawResponse());
}
```