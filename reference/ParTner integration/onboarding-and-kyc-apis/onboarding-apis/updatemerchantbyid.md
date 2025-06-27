---
title: Update Merchant API
excerpt: >-
  API to perform a full update of an existing merchant in the PayU system. Only
  the merchantId path parameter is required; all fields in the request body are
  optional.
api:
  file: payu_merchant_api_final.json
  operationId: updateMerchantById
hidden: true
---
This API allows you to update or add information about a merchant, including PAN details, operating information, and more. The **Update Merchant Details** API is used to:

* Add or update any information about the merchant
* Update PAN details
* Authorized through User token (merchant token), obtained using Send OTP and Verify OTP APIs.

> 📘 Notes:
>
> * The Update Merchant API uses the uuid value as the path parameter. Use the uuid value that is in the \*\*Create Merchant \*\* API  response for the corresponding merchant. For more information, refer to [Create Merchant API](ref:create_merchant_api).
> * All the fields in this API are not mandatory, but when you are using this API, you must update atleast one merchant's detail using a parameter.
> * The PAN verification will happen asynchronously, and the status will be made available in the Get Merchant API.
> * PAN name has to be the same as the business name for successful verification
> * Partner needs to create a form within the application to collect this information
> * The entire payload needs to be submitted for update requests as well
> * No updates are allowed after successful PAN verification. PAN verification status is available in the get merchant API. If the merchant wants to update any information after PAN verification, you need to contact the PayU Care team through help.payu.in

> 📘 Bearer Token:
>
> The bearer token is required on the header that is generated using the following APIs:
>
> * [Send OTP API](ref:send_otp_api) with the send\_sign\_in\_otp as the scope.
> * [Verify OTP API](ref:verify_otp_api) with the verify\_sign\_in\_otp as the scope

<PARTNEROnboardingEnvironment />

\<details>\
\<summary>Sample request\</summary>

```
```

## Request parameters