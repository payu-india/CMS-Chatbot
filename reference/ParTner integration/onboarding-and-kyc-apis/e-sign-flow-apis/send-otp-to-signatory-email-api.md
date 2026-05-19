---
api:
  file: Send_OTP_To_Signatory_Email_API.json
  operationId: SendOtpToSignatoryEmail
hidden: false
metadata:
  title: Send OTP to Signatory Email API
---
This API is used to send OTP to the signatory email, and this OTP is used by the **E-Sign Merged Agreement** API to sign the document. This API sends both mobile and email OTP, where the mobile number is the merchant’s registered mobile number. For more information on the **E-Sign Merged Agreement** API, refer to [E-Sign Merchant Agreement API](ref:e-sign-merchant-agreement-api).

<br />

<Partner_Postman />

<br />

**Environment**

|                            |                                                           |
| :------------------------- | :-------------------------------------------------------- |
| **Test Environment**       | \<[https://uatoneapi.payu.in](https://uatoneapi.payu.in)> |
| **Production Environment** | \<[https://oneapi.payu.in](https://oneapi.payu.in)>       |

## Request Headers

> 📘 Note:
>
> * The access token with the scope as **client_manage_agreement** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).
> * uuid value can be found in the response of the **Create Merchant** API that must be used as the path parameter. For more information, refer to [Create Merchant API](ref:create_merchant_api).

|               |                         |
| ------------- | ----------------------- |
| Authorization | Bearer `{access_token}` |
| Content-Type  | multipart/form-data     |

## Sample Request

```curl
curl --location --request GET '{`{onboarding_url}`}/api/v3/merchants/{`{uuid}`}/generate_merged_document_for_esign' \
--header 'Authorization: Bearer `{access_token}`'
```

Where **`{onboarding\_url}`** is substituted with the URL specified in the Test or Production environment as mentioned in the _Environment_ section.

## Sample Response

### Success Scenario

Successful response

```plaintext
{
  "otp": {
    "message": "sent"
  }
}
```

### Failure Scenarios

* Unauthorized response

Unauthorized response

```plaintext
{
  "status": "Unauthorized"
}
```

* Merchant is not found with the given merchant_uuid

Agreement not found

```plaintext
{
  "status": "NotFound"
}
```

* KYC document not found with the given **`{merged\_document\_uuid}`**

```plaintext
{
  "status": "NotFound"
}
```
