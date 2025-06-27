---
title: Update Merchant Details
api:
  file: payu_update_merchant_api_updated.json
  operationId: updateMerchant
hidden: true
---
This API allows you to update or add information about a merchant, including PAN details, operating information, and more. The **Update Merchant Details** API is used to:

* Add or update any information about the merchant
* Update PAN details
* Authorized through User token (merchant token), obtained using Send OTP and Verify OTP APIs.

> 📘 Notes:
>
> * The Update Merchant API uses the uuid value as the path parameter. Use the uuid value that is in the \*\*Create Merchant \*\*API  response for the corresponding merchant. For more information, refer to [Create Merchant API](ref:create_merchant_api).
> * The PAN verification will happen asynchronously, and the status will be made available in the Get Merchant API.
> * PAN name has to be the same as the business name for successful verification
> * Partner needs to create a form within the application to collect this information
> * All the fields in this API are not mandatory except the GST details, but when you are using this API, you must update atleast one merchant's detail using a parameter.
> * The entire payload needs to be submitted for update requests as well
> * No updates are allowed after successful PAN verification. PAN verification status is available in the get merchant API. If the merchant wants to update any information after PAN verification, you need to contact the PayU Care team through help.payu.in

> 📘 Bearer Token:
>
> The bearer token is required on the header that is generated using the following APIs:
>
> * [Send OTP API](ref:send_otp_api) with the send\_sign\_in\_otp as the scope.
> * [Verify OTP API](ref:verify_otp_api) with the verify\_sign\_in\_otp as the scope

<PARTNEROnboardingEnvironment />


\<details>
&#x20; \<summary>Sample request\</summary>

&#x20; \`\`\`curl
&#x20; curl --location --request PUT 'https\://uat-partner.payu.in/api/v1/merchants/11ec-ed65-770862dc-8758-026e3e71538e/update' \\
&#x20; \--header 'Authorization: Bearer 5a0260ef08e0a6e7b925b350521f10073a3d4713442e62c489c74e804938843d' \\
&#x20; \--form 'merchant\[business\_sub\_category]="Flowers and Gifts"' \\
&#x20; \--form 'merchant\[business\_category]="Ecommerce"' \\
&#x20; \--form 'merchant\[business\_entity]="Sole Proprietorship"' \\
&#x20; \--form 'merchant\[business\_name]="Harsh Agarwal"' \\
&#x20; \--form 'merchant\[pancard\_number]="AUKPA1386M"' \\
&#x20; \--form 'merchant\[signing\_authority\_details]\[email]="kycsanity9\@yopmail.com"' \\
&#x20; \--form 'merchant\[signing\_authority\_details]\[name]="Harsh Agarwal"' \\
&#x20; \--form 'merchant\[signing\_authority\_details]\[pancard\_number]="AUKPA1386M"' \\
&#x20; \--form 'merchant\[signing\_authority\_details]\[email]="ashsih\@payu.in"' \\
&#x20; \--form 'merchant\[signing\_authority\_details]\[name]="Ashish Kumar"' \\
&#x20; \--form 'merchant\[signing\_authority\_details]\[pancard\_number]="OPSPS0921B"' \\
&#x20; \--form 'merchant\[signing\_authority\_details]\[cin\_number]="U72400MH2006PTC293037"' \\
&#x20; \--form 'merchant\[director1\_details]\[name]="John Doe"' \\
&#x20; \--form 'merchant\[director1\_details]\[email]="john\_dir\@payu.in"' \\
&#x20; \--form 'merchant\[director2\_details]\[name]="Jane Doe"' \\
&#x20; \--form 'merchant\[director2\_details]\[email]="jane\_dir\@payu.in"' \\
&#x20; \--form 'merchant\[monthly\_expected\_volume]="60000"' \\
&#x20; \--form 'merchant\[operating\_address]\[address\_line]="Sector 98"' \\
&#x20; \--form 'merchant\[operating\_address]\[city]="Noida"' \\
&#x20; \--form 'merchant\[operating\_address]\[state]="UTTAR PRADESH"' \\

## Request parameters