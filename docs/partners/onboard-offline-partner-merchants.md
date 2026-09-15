---
title: Onboard Offline Partner Merchants
deprecated: false
hidden: false
metadata:
  robots: index
---
This section describes the complete merchant onboarding workflow using PayU Partner APIs. You'll implement a **16-step sequential process** that adapts dynamically based on merchant type, entity structure, and business category.

<Note>
**Prerequisites**

Before starting, ensure you have completed:
- ✅ [Authentication & Setup](./authentication-and-setup) — OAuth token generation
- ✅ Partner credentials (`client_id` and `client_secret`)
- ✅ Understanding of merchant types: Individual vs. Non-Individual, Online vs. Offline
</Note>

***

## Overview: The 16-Step Onboarding Workflow

The Partner Onboarding workflow is **sequential but adaptive**. Not all merchants follow all 16 steps. The system dynamically determines required steps based on:

**Merchant Classification:**

- **Entity Type**: Individual | Private Limited | Partnership | Public Limited | Proprietorship | LLP | Trust | NGO | HUF
- **Merchant Type**: Online (eCommerce/digital services) | Offline (physical stores)
- **Product Category**: POS vs. standard payment acceptance
- **Ownership Structure**: UBO (Ultimate Beneficial Owner) requirements

**Complete Step Sequence:**

| Step   | Operation                | API Reference                                                                                                    | Applies To              |
| ------ | ------------------------ | ---------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **00** | Generate OAuth Token     | [Get Token API](../onboarding-and-kyc-apis/step-00-authentication/get_token_partner_integration)                 | All merchants           |
| **01** | Create Merchant Account  | [Create Merchant API](../onboarding-and-kyc-apis/step-01-create-merchant-1/createmerchant)                       | All merchants           |
| **02** | Update PAN, DOB & Entity | [Update PAN/DOB API](../onboarding-and-kyc-apis/step-02-update-pan-dob/updatemerchant_pan_dob_entity)            | All merchants           |
| **03** | CKYC Verification        | [CKYC APIs](../onboarding-and-kyc-apis/step-03-ckyc-verification-1/) (4 APIs)                                    | Conditional             |
| **04** | Update Business Details  | [Update Business API](../onboarding-and-kyc-apis/step-04-update-business-details/updatemerchant_businessdetails) | All merchants           |
| **05** | Update Bank Details      | [Update Bank API](../onboarding-and-kyc-apis/step-05-update-bank-details/updatemerchant_bankdetails)             | All merchants           |
| **06** | Upload Bank Proof        | [Upload Bank Proof API](../onboarding-and-kyc-apis/step-06-upload-bank-proof-conditional/uploadbankproof)        | POS merchants only      |
| **07** | Update Website Details   | [Update Website API](../onboarding-and-kyc-apis/step-07-update-website-details/updatemerchant_websitedetails)    | All merchants           |
| **08** | Add Signatory Details    | [Add Signatory API](../onboarding-and-kyc-apis/step-08-add-signatory-details/addsignatorydetails)                | All merchants           |
| **09** | DigiLocker Verification  | [DigiLocker API](../onboarding-and-kyc-apis/step-09-digilocker-verification-1/generatedigilockerlink)            | Conditional             |
| **10** | Update Addresses         | [Update Addresses API](../onboarding-and-kyc-apis/step-10-update-addresses-1/updatemerchant_addresses)           | All merchants           |
| **11** | Video KYC (VKYC)         | [VKYC API](../onboarding-and-kyc-apis/step-11-video-kyc-vkyc-1/createvkycprofile)                                | Conditional             |
| **12** | Add/Update UBO           | [UBO API](../onboarding-and-kyc-apis/step-12-addupdate-ubo-1/addupdateubo)                                       | Conditional             |
| **13** | Submit Business Members  | [Business Members APIs](../onboarding-and-kyc-apis/step-13-business-members-kmp-1/) (2 APIs)                     | Non-individual entities |
| **14** | Fetch Required KYC Docs  | [Fetch Docs API](../onboarding-and-kyc-apis/step-14-fetch-required-kyc-documents-1/fetchrequireddocs)            | All merchants           |
| **15** | Upload KYC Documents     | [KYC Upload APIs](../onboarding-and-kyc-apis/step-15-upload-kyc-documents-1/) (3 APIs)                           | All merchants           |
| **16** | Generate eSign Agreement | [eSign API](../onboarding-and-kyc-apis/step-16-e-sign-agreement-1/generateagreementforesign)                     | All merchants           |

<Info>
**Important Notes**

- Steps 02, 04, 05, 07, 10, 12 all use the **same endpoint** (`PUT /api/v1/merchants/{uuid}/update`) with different request body fields
- Step 01 returns both `mid` (Merchant ID) and `uuid` (Merchant UUID)
- Most steps use `{uuid}` parameter; Step 15 (KYC upload) uses `{mid}`
- CKYC (Step 03), DigiLocker (Step 09), VKYC (Step 11), and UBO (Step 12) are **conditional** based on merchant type
</Info>

***

## Step 1: Start Integration

### Step 1.1: Understand Prerequisites

**What you need:**

- PayU Partner credentials (obtained via partnership agreement)
- Server-side application with HTTPS support
- Understanding of your target merchant segments (entity types, business categories)

**Key Concepts:**

- `uuid`: Merchant UUID returned from Step 01, used in most update operations (Steps 02-14, 16)
- `mid`: Merchant ID returned from Step 01, used in Step 15 (KYC upload) and utility endpoints
- **Conditional Steps**: Not all merchants require CKYC, DigiLocker, VKYC, or UBO steps
- **Single Update Endpoint**: Many steps use the same `PUT /api/v1/merchants/{uuid}/update` endpoint

**Checkpoint:** ✅ You have partner credentials and understand the workflow structure

***

### Step 1.2: Generate OAuth Access Token (Step 00)

**What you need:**

- `client_id` and `client_secret` from PayU partnerships team
- OAuth endpoint: `https://uat-accounts.payu.in/oauth/token` (test) or `https://accounts.payu.in/oauth/token` (production)

**Overview:**
Generate a Bearer token that will be used in the `Authorization` header for all subsequent API calls. Tokens expire after approximately 2 hours (7199 seconds).

**Quick Example:**

```bash
curl --location 'https://uat-accounts.payu.in/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={{client_id}}' \
--data-urlencode 'client_secret={{client_secret}}' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'scope=refer_merchant'
```

**Response:**

```json
{
  "access_token": "7b5843b39e5532bc...",
  "token_type": "Bearer",
  "expires_in": 7199,
  "scope": "refer_merchant"
}
```

**Detailed Documentation:**
👉 [Get Token API Reference](../onboarding-and-kyc-apis/step-00-authentication/get_token_partner_integration)

**Checkpoint:** ✅ You have a valid `access_token` to use in all subsequent requests

***

### Step 1.3: Create Merchant Account (Step 01)

**What you need:**

- Valid OAuth token from Step 1.2
- Merchant basic information: display name, email, mobile, product type, entity type
- For QR/POS merchants: Additional location and configuration parameters

**Overview:**
This is the **entry point** of onboarding. It creates a merchant shell account and returns two critical identifiers:

- `mid`: Merchant ID (numeric) — use in Step 15 (KYC upload)
- `uuid`: Merchant UUID — use in Steps 02-14 and Step 16

***

#### Sample Request

##### QR/Offline Merchant (POS Device)

```bash
curl --request POST \
     --url https://uat-partner.payu.in/api/v3/merchants \
     --header 'accept: application/json' \
     --header 'authorization: Bearer {{access_token}}' \
     --header 'content-type: multipart/form-data' \
     --form 'merchant[onboarding_type]=offline' \
     --form 'merchant[pos_merchant]=true' \
     --form 'merchant[business_entity_sub_type]=company_owned' \
     --form 'merchant[display_name]=Awesome Retail Pvt Ltd' \
     --form 'merchant[email]=awesomeretail@gmail.com' \
     --form 'merchant[mobile]=9876543210' \
     --form 'merchant[product]=PayUbiz' \
     --form 'merchant[business_details][business_entity_type]=Private Limited' \
     --form 'merchant[latitude]=22.5726' \
     --form 'merchant[longitude]=88.3639'
```
```python
import requests

url = "https://uat-partner.payu.in/api/v3/merchants"

headers = {
    "accept": "application/json",
    "authorization": "Bearer {{access_token}}"
}

form_data = {
    "merchant[onboarding_type]": (None, "offline"),
    "merchant[pos_merchant]": (None, "true"),
    "merchant[business_entity_sub_type]": (None, "company_owned"),
    "merchant[display_name]": (None, "Awesome Retail Pvt Ltd"),
    "merchant[email]": (None, "awesomeretail@gmail.com"),
    "merchant[mobile]": (None, "9876543210"),
    "merchant[product]": (None, "PayUbiz"),
    "merchant[business_details][business_entity_type]": (None, "Private Limited"),
    "merchant[latitude]": (None, "22.5726"),
    "merchant[longitude]": (None, "88.3639")
}

try:
    response = requests.post(url, headers=headers, files=form_data)
    response.raise_for_status()
    print("Status Code:", response.status_code)
    print("Response:", response.json())
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    print("Response:", response.text)
except requests.exceptions.ConnectionError:
    print("Error: Failed to connect to the server.")
except requests.exceptions.Timeout:
    print("Error: The request timed out.")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
```
```javascript
const url = "https://uat-partner.payu.in/api/v3/merchants";

const formData = new FormData();
formData.append("merchant[onboarding_type]", "offline");
formData.append("merchant[pos_merchant]", "true");
formData.append("merchant[business_entity_sub_type]", "company_owned");
formData.append("merchant[display_name]", "Awesome Retail Pvt Ltd");
formData.append("merchant[email]", "awesomeretail@gmail.com");
formData.append("merchant[mobile]", "9876543210");
formData.append("merchant[product]", "PayUbiz");
formData.append("merchant[business_details][business_entity_type]", "Private Limited");
formData.append("merchant[latitude]", "22.5726");
formData.append("merchant[longitude]", "88.3639");

const options = {
    method: "POST",
    headers: {
        "accept": "application/json",
        "authorization": "Bearer {{access_token}}"
    },
    body: formData
};

(async () => {
    try {
        const response = await fetch(url, options);
        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`HTTP error! Status: ${response.status} - ${errorText}`);
        }
        const data = await response.json();
        console.log("Status Code:", response.status);
        console.log("Response:", data);
    } catch (error) {
        console.error("Request failed:", error.message);
    }
})();
```
```java
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.UUID;

public class CreateMerchant {

    public static void main(String[] args) {
        String url = "https://uat-partner.payu.in/api/v3/merchants";
        String accessToken = "{{access_token}}";
        String boundary = UUID.randomUUID().toString();

        String formBody = buildMultipartBody(boundary);

        HttpClient client = HttpClient.newHttpClient();

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("authorization", "Bearer " + accessToken)
                .header("content-type", "multipart/form-data; boundary=" + boundary)
                .POST(HttpRequest.BodyPublishers.ofString(formBody))
                .build();

        try {
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println("Status Code: " + response.statusCode());
            System.out.println("Response: " + response.body());
        } catch (java.io.IOException e) {
            System.err.println("I/O error occurred: " + e.getMessage());
        } catch (InterruptedException e) {
            System.err.println("Request was interrupted: " + e.getMessage());
            Thread.currentThread().interrupt();
        }
    }

    private static String buildMultipartBody(String boundary) {
        String[][] fields = {
            {"merchant[onboarding_type]", "offline"},
            {"merchant[pos_merchant]", "true"},
            {"merchant[business_entity_sub_type]", "company_owned"},
            {"merchant[display_name]", "Awesome Retail Pvt Ltd"},
            {"merchant[email]", "awesomeretail@gmail.com"},
            {"merchant[mobile]", "9876543210"},
            {"merchant[product]", "PayUbiz"},
            {"merchant[business_details][business_entity_type]", "Private Limited"},
            {"merchant[latitude]", "22.5726"},
            {"merchant[longitude]", "88.3639"}
        };

        StringBuilder body = new StringBuilder();
        for (String[] field : fields) {
            body.append("--").append(boundary).append("\r\n");
            body.append("Content-Disposition: form-data; name=\"").append(field[0]).append("\"\r\n\r\n");
            body.append(field[1]).append("\r\n");
        }
        body.append("--").append(boundary).append("--\r\n");
        return body.toString();
    }
}
```
```php
<?php

$url = "https://uat-partner.payu.in/api/v3/merchants";
$accessToken = "{{access_token}}";

$formData = [
    "merchant[onboarding_type]"                              => "offline",
    "merchant[pos_merchant]"                                 => "true",
    "merchant[business_entity_sub_type]"                     => "company_owned",
    "merchant[display_name]"                                 => "Awesome Retail Pvt Ltd",
    "merchant[email]"                                        => "awesomeretail@gmail.com",
    "merchant[mobile]"                                       => "9876543210",
    "merchant[product]"                                      => "PayUbiz",
    "merchant[business_details][business_entity_type]"       => "Private Limited",
    "merchant[latitude]"                                     => "22.5726",
    "merchant[longitude]"                                    => "88.3639"
];

$ch = curl_init();

curl_setopt_array($ch, [
    CURLOPT_URL            => $url,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => $formData,
    CURLOPT_HTTPHEADER     => [
        "accept: application/json",
        "authorization: Bearer " . $accessToken
    ]
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curlError = curl_error($ch);
curl_close($ch);

if ($curlError) {
    echo "cURL Error: " . $curlError . PHP_EOL;
} elseif ($httpCode >= 200 && $httpCode < 300) {
    echo "Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
} else {
    echo "HTTP Error. Status Code: " . $httpCode . PHP_EOL;
    echo "Response: " . $response . PHP_EOL;
}
?>
```

***

#### Sample Response

**Success (200 OK)**

```json
{
  "merchant": {
    "mid": "760070201",
    "uuid": "11ef-3f42-e5fe-a0b6-0242ac130006",
    "name": "AWESOME RETAIL PVT LTD",
    "email": "awesomeretail@gmail.com",
    "mobile": "9876543210",
    "onboarding_type": "offline",
    "pos_merchant": true,
    "business_entity_sub_type": "company_owned",
    "latitude": "22.5726",
    "longitude": "88.3639"
  }
}
```

***

#### Request Parameters

**Mandatory parameters**

<table>
  <thead>
    <tr>
      <th align="left">Parameter</th>
      <th align="left">Type</th>
      <th align="left">Description</th>
      <th align="left">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>merchant[display_name]</td>
      <td>string</td>
      <td>Merchant display name.</td>
      <td>Awesome Retail Pvt Ltd</td>
    </tr>
    <tr>
      <td>merchant[email]</td>
      <td>string</td>
      <td>Merchant primary email.</td>
      <td>awesomeretail@gmail.com</td>
    </tr>
    <tr>
      <td>merchant[mobile]</td>
      <td>string</td>
      <td>Merchant mobile number (10 digits, no country code).</td>
      <td>9876543210</td>
    </tr>
    <tr>
      <td>merchant[product]</td>
      <td>string</td>
      <td>Product type. Always use <Glossary>PayUbiz</Glossary>.</td>
      <td>PayUbiz</td>
    </tr>
    <tr>
      <td>merchant[business_details][business_entity_type]</td>
      <td>string</td>
      <td>
        Business <Glossary>entity type</Glossary>. Supported values:
        Individual, Private Limited, Partnership, Public Limited,
        Proprietorship, LLP, Trust, NGO, HUF.
      </td>
      <td>Private Limited</td>
    </tr>
    <tr>
      <td>merchant[onboarding_type]</td>
      <td>string</td>
      <td>
        Merchant <Glossary>onboarding</Glossary> type.
        Supported values: online, offline.
      </td>
      <td>offline</td>
    </tr>
  </tbody>
</table>

**Conditional parameters**

| Parameter                           | Type    | Description                                                                                                                                     | Example       |
| :---------------------------------- | :------ | :---------------------------------------------------------------------------------------------------------------------------------------------- | :------------ |
| merchant\[pos_merchant]             | boolean | Set to `true` for <Glossary>QR</Glossary>/<Glossary>POS</Glossary> device merchants. Required when `onboarding_type` is set to `offline`.       | true          |
| merchant\[business_entity_sub_type] | string  | Business ownership model. Supported values: `company_owned`, `franchise`, `partnership_owned`. Required for <Glossary>POS</Glossary> merchants. | company_owned |
| merchant\[latitude]                 | string  | Store or outlet latitude in decimal degrees. Required for <Glossary>POS</Glossary> merchants.                                                   | 22.5726       |
| merchant\[longitude]                | string  | Store or outlet longitude in decimal degrees. Required for <Glossary>POS</Glossary> merchants.                                                  | 88.3639       |

<Note>
**QR/POS Merchant Requirements**

For QR code or POS device merchants, you MUST include:
- `merchant[onboarding_type]=offline`
- `merchant[pos_merchant]=true`
- `merchant[business_entity_sub_type]` (ownership model)
- `merchant[latitude]` and `merchant[longitude]` (store GPS coordinates)

These parameters trigger additional verification steps (Step 06 - Bank Proof upload).
</Note>

***

<Warning>
**Critical: Save Both `mid` and `uuid`**

Store these identifiers in your database:
- **`uuid`**: Required for Steps 02-14, 16 (most operations)
- **`mid`**: Required for Step 15 (KYC document upload) and utility endpoints

For QR/POS merchants, also store:
- **`onboarding_type`**: Determines conditional steps
- **`pos_merchant`**: Triggers Step 06 (bank proof upload requirement)
</Warning>

**Detailed Documentation:**
👉 [Create Merchant API Reference](../onboarding-and-kyc-apis/step-01-create-merchant-1/createmerchant)

**Checkpoint:** ✅ You have both `mid` and `uuid` stored securely

***

***

***

### Step 1.4: Update PAN, DOB & Entity Type (Step 02)

**What you need:**

- Merchant `uuid` from Step 1.3
- PAN number (business PAN for companies, proprietor PAN for individuals)
- Date of birth (individuals) or incorporation date (companies)

**Overview:**
This step validates and stores the merchant's PAN card details. For individuals, submit date of birth; for companies, submit incorporation date.

**Quick Example:**

```bash
curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/update' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "merchant": {
    "business_details": {
      "business_entity_type": "Private Limited",
      "pancard_number": "ABCDE1234F",
      "date_of_birth": "2015-01-15"
    }
  }
}'
```

**Detailed Documentation:**
👉 [Update PAN/DOB API Reference](../onboarding-and-kyc-apis/step-02-update-pan-dob/updatemerchant_pan_dob_entity)

**Checkpoint:** ✅ PAN number and entity type validated and stored

***

### Step 1.5: CKYC Verification (Step 03 - Conditional)

**What you need:**

- Merchant PAN from Step 1.4
- Mobile number for OTP verification

**Overview:**
CKYC (Central KYC) verification is **optional but recommended**. If the merchant has existing CKYC records, this step can:

- Pre-fill KYC data automatically
- Reduce manual document upload requirements
- Speed up onboarding

**Workflow:**

1. Send CKYC OTP to merchant's registered mobile
2. Merchant provides OTP for verification
3. Fetch CKYC data if verification succeeds
4. Submit CKYC with GSTIN (if applicable)

**Quick Example (Send OTP):**

```bash
curl --location 'https://uat-partner.payu.in/api/v3/merchants/kyc_document/send_ckyc_otp' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "mid": "{{mid}}",
  "pan": "ABCDE1234F"
}'
```

<Info>
**When to Skip CKYC**

CKYC is conditional. Skip this step if:
- Merchant does not have existing CKYC records
- CKYC OTP fails or times out
- You prefer to collect KYC documents manually (Step 15)

Skipping CKYC does not block onboarding — it just means you'll upload documents in Step 15.
</Info>

**Detailed Documentation:**
👉 [CKYC Verification APIs](../onboarding-and-kyc-apis/step-03-ckyc-verification-1/) (4 APIs)

**Checkpoint:** ✅ CKYC completed successfully (if applicable) or confirmed to skip

***

### Step 1.6: Update Business Details (Step 04)

**What you need:**

- Merchant `uuid`
- Business name, category, sub-category
- GST number (if turnover >₹20 lakhs)

**Overview:**
This step captures detailed business information including legal name, business category/sub-category, and GST registration.

**Quick Example:**

```bash
curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/update' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "merchant": {
    "business_details": {
      "business_name": "Awesome Retail Pvt Ltd",
      "business_category": "Retail",
      "business_sub_category": "Electronics",
      "gst_number": "29ABCDE1234F1Z5"
    }
  }
}'
```

<Warning>
**Business Category Validation**

The `business_category` and `business_sub_category` must match PayU's master list. Invalid categories will result in HTTP 422 errors. Contact your PayU account manager for the complete approved list.
</Warning>

**Detailed Documentation:**
👉 [Update Business Details API Reference](../onboarding-and-kyc-apis/step-04-update-business-details/updatemerchant_businessdetails)

**Checkpoint:** ✅ Business details validated and stored

***

### Step 1.7: Update Bank Details (Step 05)

**What you need:**

- Merchant `uuid`
- Bank account number, IFSC code, account holder name

**Overview:**
This step captures the merchant's settlement bank account where PayU will transfer collected payments.

**Quick Example:**

```bash
curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/update' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "merchant": {
    "bank_detail": {
      "bank_account_number": "1234567890",
      "ifsc_code": "HDFC0001234",
      "holder_name": "Awesome Retail Pvt Ltd"
    }
  }
}'
```

**Detailed Documentation:**
👉 [Update Bank Details API Reference](../onboarding-and-kyc-apis/step-05-update-bank-details/updatemerchant_bankdetails)

**Checkpoint:** ✅ Bank account details stored and will be verified later

***

### Step 1.8: Upload Bank Proof (Step 06 - POS Merchants Only)

**What you need:**

- Merchant `mid` (not uuid!)
- Bank statement PDF (last 3 months)

**Overview:**
This step is **required ONLY for POS device merchants**. Standard online merchants can skip to Step 1.9.

**Quick Example:**

```bash
curl --location 'https://uat-partner.payu.in/api/v3/merchants/{{mid}}/kyc_document' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: multipart/form-data' \
--form 'merchant[document_category]="Bank Statement"' \
--form 'merchant[document_type]="Bank Statement"' \
--form 'merchant[processed_document]=@"/path/to/bank_statement.pdf"'
```

**Detailed Documentation:**
👉 [Upload Bank Proof API Reference](../onboarding-and-kyc-apis/step-06-upload-bank-proof-conditional/uploadbankproof)

**Checkpoint:** ✅ Bank statement uploaded (POS merchants) or step skipped (non-POS merchants)

***

### Step 1.9: Update Website Details (Step 07)

**What you need:**

- Merchant `uuid`
- Website URL, Android/iOS app URLs (if applicable)

**Overview:**
This step captures the merchant's online presence (website and mobile apps).

**Quick Example:**

```bash
curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/update' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "merchant": {
    "website_url": "https://www.awesomeretail.com",
    "android_url": "https://play.google.com/store/apps/details?id=com.awesomeretail",
    "ios_url": "https://apps.apple.com/app/awesome-retail/id123456789"
  }
}'
```

**Detailed Documentation:**
👉 [Update Website Details API Reference](../onboarding-and-kyc-apis/step-07-update-website-details/updatemerchant_websitedetails)

**Checkpoint:** ✅ Website and app details stored

***

### Step 1.10: Add Signatory Details (Step 08)

**What you need:**

- Merchant `uuid`
- Authorized signatory information: name, PAN, email, mobile

**Overview:**
This step registers the authorized signatory who will execute the digital agreement (eSign) in Step 16.

**Quick Example:**

```bash
curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/signatory_details' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "merchant": {
    "signatory": {
      "name": "Rajesh Kumar",
      "pan": "ABCPK1234D",
      "email": "rajesh@awesomeretail.com",
      "mobile": "9876543210"
    }
  }
}'
```

<Info>
**Signatory PAN Validation**

For companies: Signatory PAN must match a director listed in MOA/AOA  
For partnerships: Signatory PAN must match a partner in Partnership Deed  
For individuals: Signatory PAN typically matches business PAN
</Info>

**Detailed Documentation:**
👉 [Add Signatory Details API Reference](../onboarding-and-kyc-apis/step-08-add-signatory-details/addsignatorydetails)

**Checkpoint:** ✅ Authorized signatory registered

***

### Step 1.11: DigiLocker Verification (Step 09 - Conditional)

**What you need:**

- Merchant `mid`
- Merchant consent to fetch documents from DigiLocker

**Overview:**
DigiLocker is an **optional digital document locker** maintained by the Government of India. If the merchant consents, PayU can automatically fetch PAN and Aadhaar documents, eliminating manual uploads.

**Quick Example:**

```bash
curl --location 'https://uat-partner.payu.in/api/v1/merchants/digilocker_link' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "mid": "{{mid}}",
  "consent": true
}'
```

**Merchant Action:**

- System generates a DigiLocker authorization URL
- Merchant clicks URL and logs into DigiLocker
- Merchant authorizes PayU to fetch documents
- Documents automatically uploaded to merchant profile

**Detailed Documentation:**
👉 [DigiLocker Verification API Reference](../onboarding-and-kyc-apis/step-09-digilocker-verification-1/generatedigilockerlink)

**Checkpoint:** ✅ DigiLocker link generated and shared, or step skipped

***

### Step 1.12: Update Addresses (Step 10)

**What you need:**

- Merchant `uuid`
- Registered address and communication address

**Overview:**
This step captures the merchant's legal registered address and communication address (can be the same).

**Quick Example:**

```bash
curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/update' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "merchant": {
    "addresses": {
      "registered_address": {
        "address_line_1": "123 MG Road",
        "city": "Bangalore",
        "state": "Karnataka",
        "pincode": "560001"
      }
    }
  }
}'
```

**Detailed Documentation:**
👉 [Update Addresses API Reference](../onboarding-and-kyc-apis/step-10-update-addresses-1/updatemerchant_addresses)

**Checkpoint:** ✅ Addresses captured and stored

***

### Step 1.13: Video KYC (VKYC) (Step 11 - Conditional)

**What you need:**

- Merchant `mid` and `uuid`
- Merchant availability for live video call

**Overview:**
VKYC (Video KYC) is a **live video verification** where a PayU agent verifies the merchant's identity via video call. This is **conditional** and may not be required for all merchants.

**Quick Example:**

```bash
curl --location 'https://uat-partner.payu.in/api/v1/merchants/create_vkyc_profile' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "mid": "{{mid}}",
  "uuid": "{{uuid}}"
}'
```

**Merchant Action:**

- System generates a VKYC link
- Merchant schedules and joins video call
- PayU agent verifies identity and documents live
- Status updates to `completed` upon success

**Detailed Documentation:**
👉 [Video KYC (VKYC) API Reference](../onboarding-and-kyc-apis/step-11-video-kyc-vkyc-1/createvkycprofile)

**Checkpoint:** ✅ VKYC link generated and call scheduled, or step skipped

***

### Step 1.14: Add/Update UBO Details (Step 12 - Conditional)

**What you need:**

- Merchant `uuid`
- Ultimate Beneficial Owner (UBO) information

**Overview:**
UBO disclosure is **required for certain entity types** (Private Limited, Public Limited, LLP) when any individual owns >25% of the business.

**Quick Example:**

```bash
curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/update' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "merchant": {
    "ubo_details": {
      "name": "John Doe",
      "pan": "ABCDE1234F",
      "ownership_percentage": "51"
    }
  }
}'
```

**Detailed Documentation:**
👉 [Add/Update UBO API Reference](../onboarding-and-kyc-apis/step-12-addupdate-ubo-1/addupdateubo)

**Checkpoint:** ✅ UBO details submitted (if applicable) or step skipped

***

### Step 1.15: Submit Business Members (KMP) (Step 13 - Non-Individual Entities)

**What you need:**

- Merchant `uuid`
- List of directors (companies) or partners (partnerships)

**Overview:**
For non-individual entities, submit the list of **Key Management Personnel** (directors, partners, trustees).

**Workflow:**

1. **List existing members**: `GET /api/v1/merchants/{uuid}/business_members`
2. **Submit/update members**: `PUT /api/v1/merchants/{uuid}/update`

**Quick Example:**

```bash
curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/update' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
  "merchant": {
    "business_members": [
      {
        "name": "Rajesh Kumar",
        "designation": "Director",
        "pan": "ABCPK1234D",
        "din": "01234567"
      }
    ]
  }
}'
```

**Detailed Documentation:**
👉 [Business Members APIs](../onboarding-and-kyc-apis/step-13-business-members-kmp-1/)

**Checkpoint:** ✅ Business members submitted (non-individual entities) or step skipped (individuals)

***

### Step 1.16: Fetch Required KYC Documents (Step 14)

**What you need:**

- Merchant `uuid`

**Overview:**
This **utility endpoint** returns the dynamic list of KYC documents required for the merchant based on entity type and business category. **Never hardcode document lists** — always fetch from this API.

**Quick Example:**

```bash
curl --location 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}' \
--header 'Authorization: Bearer {{access_token}}'
```

**Response Example:**

```json
{
  "merchant": {
    "required_documents": [
      {"document_category": "PAN Card of Signing Authority", "is_mandatory": true},
      {"document_category": "Address Proof", "is_mandatory": true},
      {"document_category": "MOA", "is_mandatory": true},
      {"document_category": "AOA", "is_mandatory": true}
    ]
  }
}
```

**Detailed Documentation:**
👉 [Fetch Required Documents API Reference](../onboarding-and-kyc-apis/step-14-fetch-required-kyc-documents-1/fetchrequireddocs)

**Checkpoint:** ✅ You have the dynamic list of required documents

***

### Step 1.17: Upload KYC Documents (Step 15)

**What you need:**

- Merchant `mid` (not uuid!)
- Document files from Step 1.16 list (JPG/PNG/PDF, max 5MB each)

**Overview:**
Upload each required document using this endpoint. Call **once per document category**.

**Quick Example (Upload PAN):**

```bash
curl --location 'https://uat-partner.payu.in/api/v3/merchants/{{mid}}/kyc_document' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: multipart/form-data' \
--form 'merchant[document_category]="PAN Card of Signing Authority"' \
--form 'merchant[document_type]="PAN Card"' \
--form 'merchant[processed_document]=@"/path/to/pan.pdf"'
```

**Response:**

```json
{
  "merchant": {
    "kyc_document_uuid": "11ef-587e-4383-a0b6-0242ac130006",
    "kyc_document_status": "DOCUMENT_SUBMITTED"
  }
}
```

**Check Document Status:**

```bash
GET /api/v3/merchants/{{mid}}/kyc_document/{{kyc_document_uuid}}
```

**Status Values:**

- `DOCUMENT_SUBMITTED` — Awaiting verification
- `DOCUMENT_APPROVED` — Verified successfully ✅
- `DOCUMENT_REJECTED` — Rejected (re-upload required)

**Detailed Documentation:**
👉 [Upload KYC Documents APIs](../onboarding-and-kyc-apis/step-15-upload-kyc-documents-1/) (Upload, Show, Delete)

**Checkpoint:** ✅ All required documents uploaded and status is `DOCUMENT_APPROVED`

***

### Step 1.18: Generate eSign Agreement (Step 16)

**What you need:**

- Merchant `uuid`
- All previous steps (02-15) completed successfully

**Overview:**
This is the **final step** that generates a digital agreement signing link for the merchant. The signatory (from Step 08) will complete OTP-based eSign.

**Quick Example:**

```bash
curl --location 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/get_esign_link' \
--header 'Authorization: Bearer {{access_token}}'
```

**Response:**

```json
{
  "merchant": {
    "esign_link": "https://esign.payu.in/agreement/sign/abc123xyz",
    "esign_status": "link_generated",
    "expires_at": "2024-01-20T13:00:00Z"
  }
}
```

**Merchant Action:**

- Share the `esign_link` with the signatory
- Signatory clicks link, receives OTP, completes digital signature
- System updates `esign_status` to `completed`

**Check Merchant Status:**
Use the utility endpoint to verify completion:

```bash
GET /api/v3/merchants/{{mid}}
```

**Detailed Documentation:**
👉 [Generate eSign Agreement API Reference](../onboarding-and-kyc-apis/step-16-e-sign-agreement-1/generateagreementforesign)

**Checkpoint:** ✅ eSign completed and merchant onboarding is COMPLETE 🎉

***

## Step 2: Test Integration

### Step 2.1: Test Individual Merchant Flow

**Scenario:** Onboard an individual proprietor (simplest path)

**Steps to Test:**

1. ✅ Step 01: Create merchant with `business_entity_type: "Individual"`
2. ✅ Step 02: Update with proprietor's PAN and DOB
3. ⏭️ Step 03: Skip CKYC (optional)
4. ✅ Step 04: Update business details (no GST if \<₹20L turnover)
5. ✅ Step 05: Update bank details
6. ⏭️ Step 06: Skip bank proof (not POS merchant)
7. ✅ Step 07: Update website
8. ✅ Step 08: Add signatory (same as proprietor)
9. ⏭️ Step 09: Skip DigiLocker (optional)
10. ✅ Step 10: Update addresses
11. ⏭️ Step 11: Skip VKYC (optional)
12. ⏭️ Step 12: Skip UBO (not applicable to individuals)
13. ⏭️ Step 13: Skip business members (not applicable)
14. ✅ Step 14: Fetch required docs → Expect: PAN, Address Proof, Bank Proof
15. ✅ Step 15: Upload all 3 documents → Verify all reach `DOCUMENT_APPROVED`
16. ✅ Step 16: Generate eSign → Complete signing → Verify `esign_status: "completed"`

**Expected Result:** ✅ Merchant onboarded successfully in \~10 active steps

***

### Step 2.2: Test Private Limited Company Flow

**Scenario:** Onboard a Private Limited company (complex path)

**Steps to Test:**

1. ✅ Step 01: Create merchant with `business_entity_type: "Private Limited"`
2. ✅ Step 02: Update with company PAN and incorporation date
3. ✅ Step 03: Complete CKYC flow (if available)
4. ✅ Step 04: Update business details (include GST)
5. ✅ Step 05: Update bank details
6. ⏭️ Step 06: Skip (not POS)
7. ✅ Step 07: Update website
8. ✅ Step 08: Add signatory (director PAN)
9. ✅ Step 09: Generate DigiLocker link
10. ✅ Step 10: Update addresses
11. ✅ Step 11: Generate VKYC link
12. ✅ Step 12: Add UBO (if ownership >25%)
13. ✅ Step 13: Submit all directors with DIN
14. ✅ Step 14: Fetch required docs → Expect: PAN, Address, Bank, MOA, AOA
15. ✅ Step 15: Upload all 5+ documents → Verify all approved
16. ✅ Step 16: Generate eSign → Complete

**Expected Result:** ✅ Company onboarded with all conditional steps completed

***

### Step 2.3: Test Error Handling

**Test Case 1: Invalid PAN Format**

- Submit `pancard_number: "INVALID123"` in Step 02
- Expected: HTTP 422 with error message

**Test Case 2: Missing Required Field**

- Omit `business_name` in Step 04
- Expected: HTTP 422 validation error

**Test Case 3: Wrong Endpoint Parameter**

- Use `mid` instead of `uuid` in Step 02
- Expected: HTTP 404 or 422 error

**Test Case 4: Expired OAuth Token**

- Wait 2+ hours, then call any API
- Expected: HTTP 401
- Verify: Your code auto-refreshes token and retries

**Test Case 5: Document Upload File Size**

- Upload 6MB file in Step 15
- Expected: HTTP 422 "File size exceeds 5MB"

**Checkpoint:** ✅ All error scenarios handled gracefully with proper retry logic

***

## Step 3: Going Live — Your Final Checklist

### Step 3.1: Update to Production Credentials

**Generate Live Keys**

1. **Request Production Credentials**
   - Email: [partnerships@payu.in](mailto:partnerships@payu.in)
   - Include: Test completion confirmation, go-live date

2. **Update Environment Variables**
   ```bash
   PAYU_CLIENT_ID=partner_live_[id]
   PAYU_CLIENT_SECRET=sk_live_[key]
   PAYU_AUTH_URL=https://accounts.payu.in/oauth/token
   PAYU_PARTNER_V3_URL=https://partner.payu.in/api/v3
   PAYU_PARTNER_V1_URL=https://partner.payu.in/api/v1
   ```

3. **Update All Endpoint URLs**
   - Replace `uat-accounts.payu.in` → `accounts.payu.in`
   - Replace `test-partner.payu.in` → `partner.payu.in`
   - Replace `uat-partner.payu.in` → `partner.payu.in`

***

### Step 3.2: Final Integration Verification

**✅ Pre-Launch Checklist**

**Authentication**

- [ ] Production OAuth token generation works
- [ ] Tokens stored server-side securely
- [ ] Automatic token refresh implemented
- [ ] 401 error handling in place

**API Calls**

- [ ] All endpoints use production URLs
- [ ] Correct use of `uuid` vs `mid` parameters
- [ ] Proper handling of conditional steps (CKYC, VKYC, UBO)
- [ ] Dynamic document fetching (Step 14) implemented

**Document Upload**

- [ ] File size validation (\<5MB) client-side
- [ ] Accepted formats (JPG/PNG/PDF) enforced
- [ ] Document status polling implemented
- [ ] Re-upload flow for rejected documents

**eSign**

- [ ] eSign link shared via email/SMS
- [ ] Status polling for `esign_status: "completed"`
- [ ] Timeout handling (link expiry)

**Security**

- [ ] `client_secret` never in logs or client code
- [ ] HTTPS enforced for all API calls
- [ ] Sensitive fields (PAN, mobile) masked in logs
- [ ] OAuth tokens not exposed to frontend

**Monitoring**

- [ ] API error rate alerts configured
- [ ] Latency monitoring (baseline: \<500ms per call)
- [ ] Failed onboarding tracking
- [ ] Daily reconciliation with PayU dashboard

**✅ First Production Merchant**

- [ ] Successfully onboarded 1 test merchant in production
- [ ] All 16 steps completed without errors
- [ ] eSign status shows `completed`
- [ ] Merchant appears in PayU production dashboard

**Checkpoint:** ✅ Production deployment complete and verified

***

## Utilities & Helper Endpoints

### Get Merchant Status

**Endpoint:** `GET /api/v3/merchants/{mid}`

Use this to check overall merchant onboarding progress at any time.

**Response Fields:**

- `mid`, `uuid`, `email`, `mobile`
- `kyc_status`, `esign_status`, `vkyc_status`, `ckyc_status`
- `required_documents[]`

👉 [Get Merchant API Reference](../onboarding-and-kyc-apis/utilities-1/getmerchant)

***

## Troubleshooting Common Issues

### Issue 1: "Invalid UUID" Error

**Cause:** Using `mid` where `uuid` is required (or vice versa)<br />**Solution:**

- Steps 02-14, 16 use `{uuid}`
- Step 15 uses `{mid}`

### Issue 2: "Business category not allowed"

**Cause:** Invalid `business_category` or `business_sub_category`<br />**Solution:** Contact PayU for approved category list

### Issue 3: Document Upload Fails

**Cause:** File size >5MB or wrong format<br />**Solution:** Compress to \<5MB, convert to JPG/PNG/PDF

### Issue 4: eSign Link Expired

**Cause:** Merchant did not complete within validity period<br />**Solution:** Call Step 16 again to generate new link

***

## Additional Resources

- 📘 [Authentication & Setup Guide](./authentication-and-setup)
- 📘 [Merchant Onboarding Decision Tree](./merchant-onboarding-decision-tree)
- 📘 [Error Codes Reference](./error-codes-reference)
- 📘 [Document Requirements Guide](./document-requirements-guide)
- 📘 [All API References](../onboarding-and-kyc-apis/)

***

**Support:**<br />For technical issues, contact: [partnerships@payu.in](mailto:partnerships@payu.in)<br />For API credentials: Your PayU account manager

***
