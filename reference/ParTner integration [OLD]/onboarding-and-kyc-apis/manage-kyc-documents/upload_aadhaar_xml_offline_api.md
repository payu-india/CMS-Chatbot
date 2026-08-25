---
title: 'Upload Aadhaar XML Offline API '
deprecated: false
hidden: true
metadata:
  title: Upload Aadhaar XML Offline API
  robots: index
---
This API is used to submit the Aadhaar details in an XML file. The access token is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get-token-api).

## Steps to get Aadhar XML

1. Navigate to the following URL for My Aadhaar website:
   * [https://myaadhaar.uidai.gov.in/en\_IN](https://myaadhaar.uidai.gov.in/en_IN).
2. Enter the child merchant Aadhaar number or VID and Security Code mentioned in the screen.
3. Click **Send OTP**.
4. Enter the OTP received by registered mobile number for the given Aadhaar Number.
5. Click **Login**.
6. Click the **Offline Ekyc Option** & enter a share code which will be the password for the ZIP file and click on the Download button.
7. The Zip file containing the digitally signed XML will be downloaded.

## Authentication

The access token with the scope as **refer\_merchant** from is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

## Endpoints

<PARTNEROnboardingEnvironment />

<br />

## Request parameters

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        aadhaar\_file
        `mandatory`
      </td>

      <td>
        `String` This field must contain the Aadhaar xml/zip file location
      </td>
    </tr>

    <tr>
      <td>
        aadhaar\_share\_code
        `mandatory`
      </td>

      <td>
        `String` This field must contain the Aadhaar share code.
      </td>
    </tr>

    <tr>
      <td>
        merchant\_id
        `mandatory`
      </td>

      <td>
        `String` The merchant ID that was provided by PayU.
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```curl
curl -X POST \
  'https://api.example.com/v3/merchants/kyc_document/aadhaar_xml_offline' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: multipart/form-data' \
  -F 'merchant_id=123456789' \
  -F 'aadhaar_share_code=1234-5678-9012' \
  -F 'aadhaar_file=@/path/to/your/aadhaar_file.xml'

```

## Sample response

```
{
    "name": "Sardar Khan",
    "gender": "M",
    "dob": "1996-02-14",
    "address": " rz-276,ph-2, gopal nagar, NAJAFGARH, South West Delhi, Delhi, India, 110043",
    "pincode": 110043
  }
```