---
title: Verify and Link Merchant API
excerpt: >-
  This api is used to link an existing merchant to a partner account.


  In the above request, the checksum is a hash value generated as described
  below.


  checksum = Digest::SHA512.hexdigest(data)


  where


  data = [reseller_uuid|product|mid|prod_key|prod_salt].


  Here reseller_uuid is available on the profile section in your partner
  dashboard, the product is always 'payumoney', mid is the merchant id of the
  merchant who is attempting to verify, prod_key is the merchant key of the
  merchant who is attempting to verify and prod_salt is the merchant salt of the
  merchant who is attempting to verify.


  Test Environment: `https://uat-partner.payu.in`


  Production Environment: `https://partner.payu.in`


  Scope present in Token: `refer_merchant`
api:
  file: partner-apis-6.json
  operationId: VerifyandLinkmerchant
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Verify and Link Merchant** API is used to:

- Used to link an existing merchant account to a partner account
- Authorized via client token generated using Client ID and Client Secret

The merchant ID in the request header must be included as a query parameter in the** mid **field.

> 📘 Note:
> 
> The access token with the scope as **refer_merchant** is required on the header. For more information on getting the access token, refer to [User Token APIs](ref:user-token-apis).

<PARTNEROnboardingEnvironment />

<details><summary>Sample request</summary>

```
curl --location --request POST 'https://test-partner.payu.in/api/v1/merchants/720043/verify' \
--header 'Authorization: Bearer w0282c38b64e072f3d66e4e6efee9789ffe1250f0cd04c20753d6e6f25df9cc7' \
--form 'checksum="20a63e957430787affb22c897ef5d919bdd3245945aa3d725ef2cd9e5f6f38e949aa6d471c2f6369d980e1d5d0ee8bff66444838409e09bf6b73aa7cf614670e"' \
--form 'merchant_key="rpt4fzcr"'
```

</details>

<details><summary>Sample response</summary>

```
{
  "message": "Successfully linked to the Partner"
}
```

</details>

## Request parameters