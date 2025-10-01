---
title: PayPal Integration
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
Integrate PayU with PayPal wallets to facilitate international payments. PayPal can be seamlessly integrated with your PayU Hosted or Merchant Hosted Checkout integration. Customers have the option to utilize PayPal Currency Conversion to convert international payments from INR (or other currencies) to their chosen currency. This ensures businesses can continue accepting payments via PayPal. Payments made through PayPal are directly transferred to your PayPal wallet, with settlements processed in INR.

You can accept payments within the transaction limits of your PayU account. Discover more about alternative payment methods and their respective transaction limits. This section describes the following:

* [Customer journey](#customer-journey)
* [Benefits](#benefits)
* [Steps to Integrate](#steps-to-integrate)
  * [Step 1: Initiate the payment with PayU](https://docs.payu.in/docs/paypal-integration#step-1-initiate-the-payment-with-payu)
  * [Step 2: Verify the payment](#step-2-verify-the-payment)

## Customer journey

1. Customer is redirected to PayU Payment page.
2. Customer selects the **Wallets** option.

<Image align="center" border={true} src="https://files.readme.io/429e564-payu_payment_pagE_wallets_list.png" className="border" />

3. Customer selects the **Paypal** option.

<Image align="center" border={true} src="https://files.readme.io/44bffcc-payu_payment_paypal_page.png" className="border" />

4. Customer selects the preferred currency and clicks **PayPal**.

   The success or failure response is sent back to you by PayU after vaerfication.

## Benefits

Incorporating PayU into your Checkout system offers several benefits:

* Improved Success Rates: Experience success rates up to 20% higher.
* Accelerated Settlement: Receive payments on a T+1 settlement schedule.
* Extensive User Base: Access over 30 Crore PayPal users worldwide.
* No Extra Charges: Transaction rates are determined by PayPal.
* Currency Conversion: Facilitate currency conversions from INR to your customers' preferred currencies.

## Steps to Integrate

This section describes the request parameters with sampe request and response to integrate the Paypal.

### Step 1: Initiate the payment with PayU

Along the request parameters listed in the [Collect Payments using Merchant Hosted Checkout > Wallets](ref:_payment_merchant_hosted_wallets), you need use the following **bankcode** with the **pg** as CASH.

**Environment**

|                            |                                                                         |
| :------------------------- | :---------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

<Callout icon="📘" theme="info">
  **Reference**: For the complete list of parameters (with **Try It** experience ) and response, refer to <a href="https://docs.payu.in/reference/_payment_merchant_hosted_wallets" target="_blank">Collect Payments API</a> under API Reference.
</Callout>

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        pg
        **mandatory**
      </td>

      <td>
        _String_ It defines the payment category using the Merchant Hosted Checkout integration. For a Wallet payment, "**PAYPAL**" must be specified in the **pg** parameter.
      </td>

      <td>
        PAYPAL
      </td>
    </tr>

    <tr>
      <td>
        bankcode **mandatory**
      </td>

      <td>
        _String_ The merchant must post  **PAYPAL** as the value for this parameter.
      </td>

      <td>
        PAYPAL
      </td>
    </tr>
  </tbody>
</Table>

#### Sample request

```curl
curl -X \
POST "
https://test.payu.in/_payment-H
"accept: application/json" -H \
"Content-Type: application/x-www-form-urlencoded" -d"key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=PAYPAL&bankcode=PAYPAL&surl=
https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```

#### Sample response

You must look for the following:

* PG_TYPE:  PAYPAL-PG
* bankcode: PAYPAL
* field4: Amount collected in the foreign currency
* field5: Foreign currency used
* net_amount_debit: Amount debited in INR

```
Array
(
    [mihpayid] => 403993715527518775
    [mode] => PAYPAL
    [status] => success
    [unmappedstatus] => captured
    [key] => J*****g
    [txnid] => HC13glcAkssIkl
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 10
    [addedon] => 2022-10-21 17:45:24
    [productinfo] => iPhone
    [firstname] => Ashish
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => US
    [zipcode] => 
    [email] => test@gmail.com
    [phone] => 9876543210
    [udf1] => 
    [udf2] => 
    [udf3] => 
    [udf4] => 
    [udf5] => 
    [udf6] => 
    [udf7] => 
    [udf8] => 
    [udf9] => 
    [udf10] => 
    [hash] => 007435a716982c7f5eec5cff95701f65eb1bdbff8f852e461224e3b5e17126ad26bb3a3ffdb95cded6a87d3515fe86fc58925cad024595a4a6825adfed2dc436
    [field1] => 
    [field2] => 
    [field3] => MCP8405944934679133147
    [field4] => 0.12
    [field5] => USD
    [field6] => 
    [field7] => 
    [field8] => 
    [field9] => Transaction Completed Successfully
    [payment_source] => payu
    [PG_TYPE] => PAYPAL-PG
    [bank_ref_num] => 540898ed-72e7-40a8-a96e-f17de621cbb4
    [bankcode] => PAYPAL
    [error] => E000
    [error_Message] => No Error
    [splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":[]}
)
```

> 📘 Note:
>
> Ensure your PayPal account maintains sufficient funds before initiating a refund. Refunds can be initiated either through the PayU Dashboard or the **Refund Transasction** API. Refunded amounts are deducted from your PayPal account and credited to your customer's PayPal account. For more information, refer to:
>
> * [Refunds Dashboard](doc:refunds-dashboard)
> * [Refund Transaction API](ref:refund_transaction_api)

### Step 2: Verify the payment

<Verify_Payment_Tabs />