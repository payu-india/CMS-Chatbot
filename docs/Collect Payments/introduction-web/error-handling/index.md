---
title: Error Handling
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
When you are integrating with PayU Hosted Checkout, at times you may encounter some errors due to missing mandatory parameters or hash mismatch. This section describes how to fix these issues while integrating. For a complete list of error codes, refer to [Error Codes](ref:error-codes)

> 📘 Note:
>
> If you encounter any other issues or errors and are unable to resolve them, contact [PayU Support.](https://help.payu.in/)

## Hash Mismatch

**Error summary**: Transaction failed due to incorrectly calculated hash parameter.

<Image align="center" width="520px" src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/Screenshot-2021-06-25-at-5.16.36-PM-1024x379.png" />

**Solution**: To calculate the hash parameter correctly, refer to [Generate Hash](doc:generate-hash-merchant-hosted).

## Duplicate Transaction ID (txnid)

**Error summary**: The transaction ID (txnid) has been used previously or was successfully captured.

<Image align="center" width="520px" src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/Screenshot-2021-06-25-at-5.27.34-PM-1024x664.png" />

**Solution**: Try using a new txnid which has not been tried earlier.

> 📘 Note:
>
> The txnid value must be unique for every new request made to PayU.

## Invalid Amount

**Error summary**: Invalid amount or amount parameter was not passed.

<Image align="center" width="520px" src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/Screenshot-2021-06-25-at-5.14.39-PM-1024x861.png" />

**Solution**: Ensure that all the mandatory parameters are passed in the transaction request to PayU. For more information on mandatory parameters, refer to [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) or [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted) based on the integration you are using.

## Incorrect Payment Details

**Error summary**: The debit card or credit card details passed are incorrect.

<Image align="center" width="520px" src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/Screenshot-2021-06-25-at-5.33.54-PM-1024x734.png" />

**Solution**: Ensure that the accurate debit card or credit card details are passed with mandatory parameters in the transaction request to PayU.

## Mandatory Parameters Missing

**Error summary**: One or more mandatory parameters are missing in the transaction request.

<Image align="center" width="520px" src="https://devguide.payu.in/wordpress/wp-content/uploads/2021/06/Screenshot-2021-06-25-at-5.10.53-PM-1024x763.png" />

**Solution**: Ensure that all the mandatory parameters are passed in the transaction request to PayU. For more information on mandatory parameters, refer to <Anchor label="Collect Payment API - PayU Hosted Checkout" target="_blank" href="ref:_payment_payu_hosted_checkout">Collect Payment API - PayU Hosted Checkout</Anchor> or <Anchor label="Collect Payment API - Merchant Hosted Checkout" target="_blank" href="ref:_payment_merchant_hosted">Collect Payment API - Merchant Hosted Checkout</Anchor> based on the integration you are using.

<br />
