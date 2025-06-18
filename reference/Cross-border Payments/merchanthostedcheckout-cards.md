---
title: PayU Hosted Checkout - CB LRS
api:
  file: PayU_Hosted_Checkout_Non_Seamless_API_Final.json
  operationId: MerchantHostedCheckout-Cards
hidden: true
---
## Step 1: Validate the PAN Card

The PAN Card Status Check API allows merchants to verify PAN (Permanent Account Number) card details. It validates whether a given PAN number is active, confirms if the provided name and date of birth match the official PAN records, and checks the seeding status of the PAN. This API is essential for KYC (Know Your Customer) processes, identity verification, and regulatory compliance.

**Endpoint**

```
https://test10-onboarding.payu.in/dvs/kyc/check_pan_card_status
```

## Request parameters

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
        pan\_number
        `mandatory`
      </td>

      <td>
        The PAN (Permanent Account Number) to be verified
      </td>

      <td>
        `"CYCPD2784G"`
      </td>
    </tr>

    <tr>
      <td>
        name
        `mandatory`
      </td>

      <td>
        The name of the PAN card holder as it appears on the PAN card
      </td>

      <td>
        `"AKASH DEEP"`
      </td>
    </tr>

    <tr>
      <td>
        dob
        `mandatory`
      </td>

      <td>
        Date of Birth of the PAN holder in DD/MM/YYYY format
      </td>

      <td>
        `"15/09/1993"`
      </td>
    </tr>
  </tbody>
</Table>

# Sample request

```bash
curl --location 'https://test10-onboarding.payu.in/dvs/kyc/check_pan_card_status' \
--header 'Content-Type: application/json' \
--header 'Date: Thu, 17 Jun 2025 08:17:59 GMT' \
--header 'Digest: DFXmqI0rFnXlmHLlsRwdDMw9vUSVzyYQzGP+MKLo8f8=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="7qjgpH9B4QALxDR0nVlHdEKEYMZ0XeJ0QpnvveSyqMo="' \
--header 'platformId: 1' \
--data '{
    "pan_number": "CYCPD2784G",
    "name": "AKASH DEEP",
    "dob": "15/09/1993"
}'
```

## Sample response

```json
{
    "id": 86235,
    "api_name": "pan_status_check",
    "identifier": "79c0d918a4f4661cb9cb17d96d24ac1cf04b6013d504cc766ac5235380bfc0d5",
    "response": {
        "result": {
            "status": "Active",
            "nameMatch": "Y",
            "dobMatch": "Y",
            "seedingStatus": "Y"
        }
    },
    "status": "success",
    "http_status": 200,
    "client_id": "195ab95fa4700eeaaf38b7f5b538d2979f0f281e0a4eaedca1aa675b79b331a2",
    "created_at": "2025-04-30T05:51:40.000Z",
    "updated_at": "2025-04-30T05:51:40.000Z",
    "client_name": "SignzyClient"
}
```

### Response parameters

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
        id
      </td>

      <td>
        Unique identifier for the verification request
      </td>

      <td>
        `86235`
      </td>
    </tr>

    <tr>
      <td>
        api\_name
      </td>

      <td>
        Identifier of the API that was called
      </td>

      <td>
        `"pan_status_check"`
      </td>
    </tr>

    <tr>
      <td>
        identifier
      </td>

      <td>
        A unique hash identifier for the verification request
      </td>

      <td>
        `"79c0d918a  
                        4f4661cb9cb  
                        17d96d24ac1  
                        cf04b6013d50
                        4cc766ac5235
                        380bfc0d5"`
      </td>
    </tr>

    <tr>
      <td>
        response
      </td>

      <td>
        Contains the verification results
      </td>

      <td>
        See result table below
      </td>
    </tr>

    <tr>
      <td>
        status
      </td>

      <td>
        Overall status of the API call
      </td>

      <td>
        `"success"`
      </td>
    </tr>

    <tr>
      <td>
        http\_status
      </td>

      <td>
        HTTP status code of the response
      </td>

      <td>
        `200`
      </td>
    </tr>

    <tr>
      <td>
        client\_id
      </td>

      <td>
        Unique identifier of the client making the request
      </td>

      <td>
        `"195ab95fa  
                        4700eeaaf38  
                        b7f5b538d29  
                        79f0f281e0
                        a4eaedca1a
                        a675b79b3
                        31a2"`
      </td>
    </tr>

    <tr>
      <td>
        created\_at
      </td>

      <td>
        Timestamp when the verification record was created
      </td>

      <td>
        `"2025-04-30T05:51:40.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        updated\_at
      </td>

      <td>
        Timestamp when the verification record was last updated
      </td>

      <td>
        `"2025-04-30T05:51:40.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        client\_name
      </td>

      <td>
        Name of the client account
      </td>

      <td>
        `"SignzyClient"`
      </td>
    </tr>
  </tbody>
</Table>

### Response Result Object

| Parameter     | Description                                                        | Example    |
| ------------- | ------------------------------------------------------------------ | ---------- |
| status        | Status of the PAN card                                             | `"Active"` |
| nameMatch     | Indicates if the provided name matches with PAN records (Y/N)      | `"Y"`      |
| dobMatch      | Indicates if the provided DOB matches with PAN records (Y/N)       | `"Y"`      |
| seedingStatus | Indicates if the PAN is seeded with additional verifications (Y/N) | `"Y"`      |

##