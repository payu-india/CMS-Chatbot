---
title: Create Merchant API
excerpt: >-
  # **Create Merchant API Documentation**


  ## **API Overview**


  **Method:** `POST`  

  **Endpoint:** `/api/v3/merchants`  

  **Content-Type:** `multipart/form-data`  

  **Purpose:** Create a new merchant account with basic business details and
  website information.


  ---


  ## **API Environment**


  | Environment | Base URL |

  | --- | --- |

  | **Production** | `https://partner.payu.in` |

  | **Test** | `https://test-partner.payu.in` |


  ---


  ## **Headers**


  | Header | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `Authorization` | String | ✅ Yes | Bearer token for authentication. Use the
  Get Token API with scope 'refer merchant' to ontain the scope | `Bearer
  {your_token_here}` |


  ---


  ## **Form Data Parameters**


  ### **Basic Merchant Information**


  | Parameter | Data Type | Required | Example Value | Description |

  | --- | --- | --- | --- | --- |

  | `[merchant][display_name]` | String | ✅ Yes | `PAYU PAYMENTS PRIVATE
  LIMITED` | Display name for the merchant |

  | `merchant[email]` | String | ✅ Yes | `boro21@yomail.com` | Primary email
  address for the merchant |

  | `merchant[mobile]` | String | ✅ Yes | `6296578770` | Primary mobile number
  for the merchant |

  | `merchant[business_details][business_entity_type]` | String | ✅ Yes |
  Individual | The entity type of the Merchant's business. |


  ---


  ## **Complete Request Example**


  ``` curl

  --header 'Authorization: Bearer ' \

  --form '[merchant][display_name]="PAYU PAYMENTS PRIVATE LIMITED"' \

  --form 'merchant[email]="boro21@yomail.com"' \

  --form 'merchant[mobile]="6296578770"'

  --form 'merchant[business_details][business_entity_type]="Individual"'

   ```

  ---


  ## **Complete response Example**


  ``` json

  {
    "merchant": {
      "name": "DIVY HARESHKUMAR SHAH",
      "email": "boro15@yomail.com",
      "registered_mobile": "9916965913",
      "mid": 8791796,
      "product": "PayUbiz",
      "business_type": "LongTail",
      "business_name": null,
      "pancard_name": null,
      "pancard_number": null,
      "website_url": null,
      "android_url": null,
      "ios_url": null,
      "gst_number": null,
      "created_at": "2025-06-26T07:16:25.000Z",
      "mobile": "9916965913",
      "blocked": false,
      "first_name": "DIVY",
      "last_name": "HARESHKUMAR SHAH",
      "bank_detail": {
        "bank_account_number": null,
        "ifsc_code": null,
        "holder_name": null,
        "nodal_code": null,
        "nodal_status": null
      },
      "operating_address": {
        "address_line": null,
        "city": null,
        "state": null,
        "pincode": null
      },
      "registration_address": {
        "address_line": null,
        "city": null,
        "state": null,
        "pincode": null
      },
      "business_entity": "Sole Proprietorship",
      "status": "account_created",
      "partner_source": "Create Merchant API",
      "pan_verification_status": "Pending",
      "website_approval_status": null,
      "notification_email": "boro15@yomail.com",
      "settlement_status": "Active",
      "is_service_agreement_accepted": false,
      "is_authorisation_letter_required": false,
      "monthly_expected_volume": null,
      "business_category": null,
      "business_sub_category": null,
      "bank_verification_status": null,
      "uuid": "11f0-525d-76182ba4-954a-021ec077a271",
      "penny_deposit_status": null,
      "document_status": "Docs Approved",
      "kyc_status": {
        "status": "LOCKED",
        "kyc_status": "LOCKED"
      },
      "agreement_status": "Approved",
      "integration_type": "Not Selected",
      "service_intent": "default"
    }
  }

   ```
api:
  file: Merchant Onboarding APIs for partners.postman_collection (5).json
  operationId: post_api-v3-merchants
hidden: false
---