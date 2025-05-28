---
title: 'Upload Aadhaar XML Offline API '
deprecated: false
hidden: false
metadata:
  robots: index
---
This API is used to submit the Aadhaar details in an XML file. The access token is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get-token-api).

## Steps to get Aadhar XML

1. Go to URL [https://myaadhaar.uidai.gov.in/en\_IN](https://myaadhaar.uidai.gov.in/en_IN).
2. Click on login. Enter Aadhaar Number or VID and mentioned Security Code in the screen, then click on Send OTP.
3. Enter the OTP received by registered mobile number for the given Aadhaar Number
4. Click on Offline Ekyc Option & enter a share code which will be the password for the ZIP file and click on the Download button.
5. The Zip file containing the digitally signed XML will be downloaded.

## Endpoints

<PARTNEROnboardingEnvironment />

<details>
  <summary>Sample request</summary>

  ```curl
  curl --location -g --request POST '{{onboarding_url}}/api/v3/merchants/kyc_document/ckyc_data' \
  --header 'Authorization: Bearer {{access_token}}' \
  --header 'Content-Type: application/json' \
  --data-raw '{
      "dob": "01-01-1990",
      "merchant_id": "{{merchant_id}}"
  }'
  ```
</details>

<details>
  <summary>Sample request</summary>

  ```
  {
    "name": "Sardar Khan",
    "gender": "M",
    "dob": "1996-02-14",
    "address": " rz-276,ph-2, gopal nagar, NAJAFGARH, South West Delhi, Delhi, India, 110043",
    "pincode": 110043
  }
  ```
</details>

## Request parameters