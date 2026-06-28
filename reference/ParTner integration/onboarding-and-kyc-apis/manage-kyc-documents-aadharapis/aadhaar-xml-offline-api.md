---
api:
  file: Partner_Onboarding_APIs_with_Aadhaar_APIs.json
  operationId: post_api-v3-merchants-kyc-document-aadhaar-xml-offline
hidden: false
---
The **Aadhar XML Offline** API allows merchants to submit Aadhaar XML files (obtained from DigiLocker or UIDAI) for KYC verification purposes.

<PartnerAuthenticationEnvironement />

## Request parameters

### Authorization header

Authorization Bearer token must be generated using **Aaadaar OTP Generation API** with the scope as . For more information, refer to [Aadhaar OTP Generation API](ref:aadhaar-otp-generation-api).

### Body parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        aadhaar\_share\_code
        `mandatory`
      </td>

      <td>
        The share code provided when downloading the Aadhaar XML file
      </td>

      <td>
        3456
      </td>
    </tr>

    <tr>
      <td>
        merchant\_id
        `mandatory`
      </td>

      <td>
        Unique identifier for the merchant
      </td>

      <td>
        8390925
      </td>
    </tr>

    <tr>
      <td>
        aadhaar\_file
        `mandatory`
      </td>

      <td>
        The XML file downloaded from DigiLocker or UIDAI website
      </td>

      <td>
        \[FILE]
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```
curl --location 'https://partner.payu.in/api/v3/merchants/kyc_document/aadhaar_xml_offline' \
--header 'Authorization: Bearer 1e3ca62936ab9565d88cca21ffa1a8f614340cb94f1b7f15bef62193931b916c' \
--form 'aadhaar_share_code="3456"' \
--form 'merchant_id="8390925"' \
--form 'aadhaar_file=@"/path/to/your/aadhaar_xml_file.xml"'

```

## Sample response

### Success scenario

```
{
  "status": "success",
  "code": 200,
  "message": "Aadhaar XML processed successfully",
  "data": {
    "reference_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "verification_status": "completed",
    "merchant_id": "8390925",
    "timestamp": "2023-05-27T10:15:30Z"
  }
}

```

### Failure scenarios

- Invalid share code

```
{
  "status": "error",
  "code": 400,
  "message": "Invalid share code",
  "data": null
}

```

- Invalid XML file

```
{
  "status": "error",
  "code": 400,
  "message": "Invalid XML file",
  "data": null
}

```

- Unauthorized access

```
{
  "status": "error",
  "code": 401,
  "message": "Unauthorized access",
  "data": null
}

```

<br />
