---
title: Get Real-Time Merchant Status using Webhooks
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
Partners can refer many merchants as they want, and every merchant has their own onboarding journey with PayU. To get the real-time merchant status update, resellers can integrate with PayU with their webhooks, where PayU will notify the reseller about the merchant onboarding status in real-time.

**Note**: Partners need to contact PayU or their Key Account Manager to enable the real-time merchant status service.

To configure webhooks:

1. If real-time merchant status service is enabled for Partner, PayU will hit the partner webhook URL. It will be a POST request which will consist of an authorization header and request payload. For more information on registering webhooks for real-time merchant status, refer to [Register Webhooks API to Get Real-Time Merchant Status](ref:register-webhooks-api-to-get-real-time-merchant-status).
2. The Authorization header will be generated using the following criteria:
   * HMAC will be generated using the SHA-256 function using request payload passed to webhook URL, and a **client\_secret** of partner application will be used as secret key to sign it and get a hashed string. This hashed string will be passed in the Authorization header.

* The formula for HMAC:

```plaintext
OpenSSL::HMAC.hexdigest("SHA256", client_secret, payload.sort.join)
```

* Sample HMAC:

```plaintext
"d59e5be387204e8c37bc8f46306f5013197b2f9d082ec859da1b09f9bc703036"
```

When the following payload is sent:

```plaintext
{ 
"previous_status": "Pending", 
"current_status": "Success", 
"change_timestamp": 18548123746 
"mid": 123456 
"merchant_uuid": "123-abcd-5678-gcjsa" 
"event_name": "Document status update" 
"error": "NA" 
"remarks": "NA" 
} 
```

`payload.sort.join` returns the following:

```plaintext
"change_timestamp18548123746current_statusSuccesserrorNAevent_nameDocument status updatemerchant_uuid123-abcd-5678-gcjsamid123456previous_statusPendingremarksNA" 
```

1. Partner needs to verify this hashed string on its end before consuming the webhook’s data.
2. Partner needs to return an empty response with status 200 on receiving webhooks.
3. PayU will retry five times, waiting exponentially till it gets the **200** response from the partner. After which, it will be considered failed. Wait time after each retry will be 3, 9, 27, 81 and 243 seconds, respectively.

The payload will contain the following data:

```plaintext
{
"previous_status": "Pending",
"current_status": "Success",
"change_timestamp": 18548123746
"mid": 123456
"merchant_uuid": "123-abcd-5678-gcjsa"
"event_name": <"Document status update"/ "Website status update"/ "Nodal status update"/ "Bank verification status update"/ "Settlement status update"/ "Agreement status update"/ "SIGNED_AUTHORISATION_LETTER status update"/ "PATNERSHIP_PAN_CARD status update"/ "GOVT_ISSUED_CERTIFICATE status update"/ "BANK_PROOF status update"/ "ADDRESS_PROOF_SIGNED_AUTHORITY status update"/ "PANCARD_SIGNED_AUTHORITY status update">
"error": "NA"
"remarks": "NA"
}
```

Possible values of status in case of KYC document update (`SIGNED_AUTHORISATION_LETTER` /`PATNERSHIP_PAN_CARD` /`GOVT_ISSUED_CERTIFICATE` /`BANK_PROOF` /`ADDRESS_PROOF_SIGNED_AUTHORITY` /`PANCARD_SIGNED_AUTHORITY`) are:

* Pending
* Received
* Approved
* Declined
* Reuploaded
* Exceptionally

> 📘 Note:
>
> For errors or remarks, refer to [KYC Errors and Solutions](ref:kyc-errors-and-solutions).
