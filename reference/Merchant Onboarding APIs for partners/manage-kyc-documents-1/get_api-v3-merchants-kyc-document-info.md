---
title: Info KYC document
excerpt: >-
  # **Get KYC Document Info API Documentation**


  ## **API Overview**


  **Method:** `GET`  

  **Content-Type:** `application/x-www-form-urlencoded`  

  **Purpose:** Retrieve the list of KYC docs required for a specific merchant.
  This API can be used to get a list of all docs that are needed for onboarding
  a merchant. This API will return an empty list when all docs are uploaded.


  ---


  ## **Endpoints**


  | Environment | Endpoint | Description | Usage |

  | --- | --- | --- | --- |

  | **Test** | `https://test-partner.payu.in/api/v3/merchants/kyc_document/info`
  | Testing/Sandbox environment | Development, testing, and integration purposes
  |

  | **Production** |
  `https://partner.payu.in/api/v3/merchants/kyc_document/info` | Live production
  environment | Live transactions and production use |


  ---


  ## **Query Parameters**


  | Parameter | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `merchant_id` | Number | ✅ Yes | Unique identifier for the merchant whose
  KYC documents need to be retrieved. The MID is returned in the repsonse of the
  Create merchant API | `760068860` |


  ---


  ## **Headers**


  | Header | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `Authorization` | String | ✅ Yes | Bearer token for authentication | `Bearer
  {your_token_here}` |

  | `Content-Type` | String | ✅ Yes | Content type specification (optional for
  GET requests) | `application/x-www-form-urlencoded` |


  ---


  ---


  ## **Validation Rules**


  - Merchant ID must be a valid numeric identifier
      
  - Merchant must be referred by the partner
      

  ---


  ## **Expected Responses**


  - **Success:** `200 OK` with KYC document information
      
  - **Unauthorized:** `401 Unauthorized` (if bearer token is invalid or missing)
      
  - **Not Found:** `404 Not Found` (if merchant_id doesn't exist)
      

  ## **Sample Response**


  Merchant type - Individual


  ``` json

  {
      "PAN Card of Signing Authority": [
          "PAN Card"
      ],
      "Address Proof of Signing Authority": [
          "Passport",
          "Aadhar",
          "Voter's ID",
          "Driving Licence",
          "Utilities Bill (electricity, water, landline, gas connection)",
          "Address Verification Letter from Bank"
      ],
      "Bank Account Proof": [
          "Cancelled Cheque",
          "Bank Verification Letter",
          "Bank Statement",
          "Passbook"
      ],
      "Service Agreement": [
          "Service Agreement"
      ]
  }

   ```
api:
  file: Merchant Onboarding APIs for partners.postman_collection_updated.json
  operationId: get_api-v3-merchants-kyc-document-info
hidden: false
---