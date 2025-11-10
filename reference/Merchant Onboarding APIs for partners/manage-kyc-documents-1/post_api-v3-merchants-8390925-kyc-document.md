---
title: Create KYC Document
excerpt: >-
  # **Upload KYC Document API Documentation**


  ## **API Overview**


  **Method:** `POST`  

  **Content-Type:** `multipart/form-data`  

  **Purpose:** Upload KYC documents for merchant verification including document
  files and metadata


  ---


  ## **Endpoints**


  | Environment | Endpoint | Description | Usage |

  | --- | --- | --- | --- |

  | **Test** |
  `https://test-partner.payu.in/api/v3/merchants/{merchant_id}/kyc_document` |
  Testing/Sandbox environment | Development, testing, and integration purposes |

  | **Production** |
  `https://partner.payu.in/api/v3/merchants/{merchant_id}/kyc_document` | Live
  production environment | Live transactions and production use |


  ---


  ## **Path Parameters**


  | Parameter | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `merchant_id` | Number | ✅ Yes | Unique identifier for the merchant
  uploading KYC documents. The MID is returned in the response of the create
  merchant API. | `8390925` |


  ---


  ## **Headers**


  | Header | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `Authorization` | String | ✅ Yes | Bearer token for authentication. Use the
  Get Token API with the scope 'refer merchant' to obtain the token |
  `{{vault:bearer-token}}` |


  ---


  ## **KYC Document Upload API Parameter Description Table**


  | Parameter | Data Type | Example Value | Description |

  | --- | --- | --- | --- |

  | **Document Information** |  |  |  |

  | `merchant[document_category]` | String | PAN Card of Signing Authority |
  Category classification of the document being uploaded |

  | `merchant[document_type]` | String | PAN Card | Specific type of document
  (must match category) |

  | `merchant[processed_document]` | File |
  @"/Users/Shared/Wallpaper2024/MandatoryComplianceTraining.jpg" | Physical
  document file to be uploaded for verification |


  ## **Document Categories & Types**


  For the KYC docs, thier categories, & types, use the [Info KYC document
  API](https://myteam-9319.postman.co/workspace/95e119fc-00c3-4a81-849c-e4798133bacb/example/32344985-0ab2a3ea-11b1-4b2a-9045-70606cabd34b?action=share&source=copy-link&creator=32344985&ctx=documentation)


  Example of document categories & types are,


  | Category | Document Type |

  | --- | --- |

  | `PAN Card of Signing Authority` | PAN card document for authorized signatory
  |

  | Address Proof of Signing Authority" | Aadhar |

  | Bank Account Proof | Cancelled Cheque |


  ## **File Requirements**


  | Requirement | Specification |

  | --- | --- |

  | **File Formats** | JPG, JPEG, PNG, PDF |

  | **File Size** | Maximum 5MB per file |

  | **Image Quality** | Clear, readable, well-lit |

  | **File naming** | No spaces or special characters allowed |


  ---


  ## **Validation Rules**


  - Document category and document type must be compatible
      
  - File must be in supported format (JPG, PNG, PDF)
      
  - File size must not exceed maximum limit
      
  - Document must be clear and readable
      

  ---


  ## **Expected Responses**


  - **Success:** `200 OK` with document upload confirmation and reference ID
      
  - **Validation Error:** `422 Unprocessable Entity` with specific field errors
      
  - **Unauthorized:** `401 Unauthorized` (if bearer token is invalid)
      
  - **Not Found:** `404 Not Found` (if merchant_id doesn't exist)
      
  - **Bad Request:** `400 Bad Request` (if file format is unsupported)
      
  - **Payload Too Large:** `413 Payload Too Large` (if file exceeds size limit)
      

  ## **Sample Response**


  ``` json

  merchant": {
          "mid": "8390925",
          "kyc_document_name": "PAN Card of Signing Authority",
          "kyc_document_uuid": "11ef-587e-43837330-95b0-021ec077a271",
          "kyc_document_status": "DOCUMENT_SUBMITTED",
          "error_message": null,
          "created_at": "2024-08-12T07:41:19.000Z"
      }

   ```
api:
  file: Merchant Onboarding APIs for partners.postman_collection_updated.json
  operationId: post_api-v3-merchants-8390925-kyc-document
hidden: false
---