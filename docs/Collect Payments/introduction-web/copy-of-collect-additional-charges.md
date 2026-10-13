---
title: '[Internal Review]Collect Additional Charges'
deprecated: false
hidden: true
metadata:
  robots: index
---
The following are the different methods to implement additional charges for PayU Hosted Checkout or Merchant Hosted Checkout:

* [Enable additional charges from PayU backend](#enable-additional-charges-from-payu-backend)
* [Post additional charges along with amount](#post-additional-charges-along-with-amount)

<Callout icon="📘" theme="info">
  ### Reference:

  The hash algorithm indicated in the below procedures are for **\_payment** API for PayU Hosted Checkout and Merchant Hosted Checkout. For more information, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) or  [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted)  based on your integration.
</Callout>

## Enable additional charges from PayU backend

In this method, you will be posting only the transaction amount of the product in the transaction request. PayU adds the additional amount based on your request with PayU.

<Callout icon="📘" theme="info">
  ### Note:

  To enable the additional charges facility, you need to contact [PayU Support](https://help.payu.in/).
</Callout>

1. Customer clicks the **Pay Now** button and the additional amount will be added to the amount of the product by PayU (based upon the TDR values).

The **total amount** would be passed on to the bank’s page while re-directing.

2. PayU receives the status of the transaction from the bank.
3. PayU sends the response back to the merchant. In this response, the **amount** and **additional amount** can be differentiated with the following parameters:

| Parameter          | Description                                                                       |
| ------------------ | --------------------------------------------------------------------------------- |
| amount             | The original transaction amount is returned in this parameter as a response.      |
| additional_charges | The additional amount that is charged is returned in this parameter as a response |

4. Check the authenticity of the response by reverse hashing.

Here, if the **additionalCharges** parameter is posted in the transaction response, then the hash formula is:

```plaintext
sha512(additional_charges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname |productinfo|amount|txnid|key)
```

If additionalCharges parameter is not posted in the transaction response, then the hash formula is the generic reverse hash formula:

```plaintext
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amo unt|txnid|key)
```

## Post additional charges along with amount

To post additional charges along with the transaction amount:

1. Posting both the transaction amount and additional charges in the transaction request. The parameters used in this regard are:

| Parameter          | Description                                                                       |
| ------------------ | --------------------------------------------------------------------------------- |
| amount             | The original transaction amount is returned in this parameter as a response.      |
| additional_charges | The additional amount that is charged is returned in this parameter as a response |

The order of the parameters is as follows:

```plaintext
<bankcode1> :< additional charge value>, < bankcode2> :< additional charge value>
```

**Example**

```plaintext
CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55
```

> **Note**: In this method of applying additional charges, the hash sequence would be affected for both pre-Transaction and post-transaction.

You need to form the following hash sequence before posting the transaction to PayU:

```plaintext
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|||| ||SALT|additional_charges)
```

Where **additional_charges** parameter will be substituted with additional charges for each payment mode. For example, the additional charges for each payment mode can be found in the following code block:

```plaintext
CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55
```

After the transaction request hits the PayU server and re-direction, the customer lands on the PayU payment page. Based on the payment mode selected by the customer, the additional charge value will be added to the transaction amount. In the above example, the additional amount is charged according to the payment mode:

* Rs 12 for credit card
* Rs.19 for AMEX option
* Rs 98 for SBI Net Banking
* Rs 2 for Diners card
* Rs. 25 for debit card
* Rs. 55 for Net Banking with other banks

> **Note**: The additional charges would be added only once the customer clicks the **Pay Now** option.

2. PayU receives the response from the bank.
3. PayU makes a POST Response to the merchant. The hash sequence needs to be changed in this regard.

   You need to form the following hash sequence and verify it with the hash sent by PayU in the Post Response:

```plaintext
sha512(additionalCharges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname |productinfo|amount|txnid|key)
```

The **additionalCharges** value must be the same as the value posted from PayU to the merchant in the response.

4. Compare the hash value with the hash value posted by PayU to you.

If both match, you must process the order. If they don’t match, the transaction has been tampered with and should not be processed further.

## Additional Charges for Standing Instruction (SI) Card Transactions

When collecting dynamic convenience fees on **SI (recurring/subscription) card transactions**, use SI-specific ibibocodes instead of the regular bankcodes described above. The same two parameters apply — `additional_charges` and `percentage_additional_charges` — but with a different set of allowed values depending on the phase of the SI lifecycle.

<Callout icon="📘" theme="info">
  ### **Note**:&#x20;

  SI convenience fee support requires the following flags to be enabled on your MID by PayU. Contact your PayU Key Account Manager (KAM) to enable them:

  - `enableCardsSiDynamicConv`
  - `enableSIPredebitConvFee`
  - `DynamicConvFeeMerchant`
</Callout>

### SI Ibibocodes for Registration

Pass these in `additional_charges` and `percentage_additional_charges` during the SI **registration (consent) transaction**:

| Ibibocode | Description                           |
| --------- | ------------------------------------- |
| `CCSI`    | Credit Card Standing Instruction      |
| `DCSI`    | Debit Card Standing Instruction       |
| `VISASI`  | Visa Standing Instruction             |
| `AMEXSI`  | American Express Standing Instruction |

**Example (Registration)**:

```plaintext
additional_charges: CCSI:10,DCSI:20,AMEXSI:30
percentage_additional_charges: CCSI:100,DCSI:90,AMEXSI:80
```

### SI Ibibocodes for Pre-Debit Notification

Pass these in `additional_charges` and `percentage_additional_charges` in the `var1` JSON of the `pre_debit_SI` API call:

| Ibibocode  | Description                           |
| ---------- | ------------------------------------- |
| `CCSI`     | Credit Card Standing Instruction      |
| `DCSI`     | Debit Card Standing Instruction       |
| `AMEXSI`   | American Express Standing Instruction |
| `HDFCDCSI` | HDFC Debit Card Standing Instruction  |
| `VISASI`   | Visa Standing Instruction             |

**Example (Pre-Debit)**:

```plaintext
additional_charges: CCSI:10,DCSI:20,AMEXSI:30,HDFCDCSI:40,VISASI:50
percentage_additional_charges: CCSI:100,DCSI:90,AMEXSI:80,HDFCDCSI:70,VISASI:60
```

<Callout icon="⚠️" theme="warn">
  ### **Important**:&#x20;

  The ibibocode sets for Registration and Pre-Debit are different. `HDFCDCSI` is valid only in the Pre-Debit phase, not during Registration.
</Callout>
