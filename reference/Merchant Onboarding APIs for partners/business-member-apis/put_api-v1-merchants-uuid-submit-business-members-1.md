---
title: Add business member API
excerpt: >-
  # **Submit Business Members API Documentation**


  ## **API Overview**


  **Method:** `PUT`  

  **Content-Type:** `application/json`  

  **Purpose:** Submit or update business member details for a merchant. At least
  one Director/Partner (basis the entity) & one member for KMP (CEO, CFO, Senior
  Management, Company Secretory) must be added.


  ---


  ## **Endpoints**


  | Environment | Endpoint | Description | Usage |

  | --- | --- | --- | --- |

  | **Test** |
  `https://test-partner.payu.in/api/v1/merchants/{product_account_uuid}/submit_business_members`
  | Testing/Sandbox environment | Development, testing, and integration purposes
  |

  | **Production** |
  `https://partner.payu.in/api/v1/merchants/{product_account_uuid}/submit_business_members`
  | Live production environment | Live transactions and production use |


  ---


  ## **Path Parameters**


  | Parameter | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `product_account_uuid` | String | ✅ Yes | Unique identifier for the
  merchant's product account. The product_account_uuid is returned in the
  response of the create merchant API | `{{product_account_uuid}}` |


  ---


  ## **Headers**


  | Header | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `Authorization` | String | ✅ Yes | Bearer token for authentication. Get the
  token using the GET token API with the scope `refer_merchant` | `Bearer
  {{resellerToken}}` |

  | `Content-Type` | String | ✅ Yes | Request content type | `application/json`
  |


  ---


  ## **Request Body Parameters**


  ### **Business Member Object**


  | Parameter | Data Type | Required | Format | Example | Description |

  | --- | --- | --- | --- | --- | --- |

  | `name` | String | ✅ Yes | Full name | `Spoorthi Mohan Naik` | Full name of
  the business member |

  | `designation` | String | ✅ Yes | Job title/role | `Director` | Position or
  designation in the company. Allowed designations - Director (Private & Public
  limited), Partner (for Partnership & LLP), CEO, CFO, Senior Management,
  Company Secretory. |

  | `doj` | String | ✅ Yes | MM/YYYY | `09/2025` | Date of joining in MM/YYYY
  format |

  | `dob` | String | ✅ Yes | DD/MM/YYYY | `24/02/2001` | Date of birth in
  DD/MM/YYYY format |

  | `pincode` | String | ✅ Yes | 6 digits | `560070` | Postal code (6-digit
  Indian pincode) |

  | `pan_number` | String | ✅ Yes | PAN format | `XXXXXXXX4C` | PAN card number
  (10 alphanumeric characters) |


  ---


  ## **Complete Request Example**


  ``` bash

  curl --location --globoff --request PUT
  '{{prod_partnerUrl}}/api/v1/merchants/{{product_account_uuid}}/submit_business_members'
  \

  --header 'Authorization: Bearer {{resellerToken}}' \

  --header 'Content-Type: application/json' \

  --data '{
      "business_members": [
          {
              "name": "Spoorthi Mohan Naik",
              "designation": "Director",
              "doj": "09/2025",
              "dob": "24/02/2001",
              "pincode": "560070",
              "pan_number": "XXXXXXXX4C"
          }
      ]
  }'

   ```

  ---


  ## **Request Body Schema**


  ``` json

  {
      "business_members": [
          {
              "name": "string",
              "designation": "string", 
              "doj": "string (MM/YYYY)",
              "dob": "string (DD/MM/YYYY)",
              "pincode": "string (6 digits)",
              "pan_number": "string (10 chars)"
          }
      ]
  }

   ```

  ---


  ## **Validation Rules**


  | Field | Rule | Description |

  | --- | --- | --- |

  | `doj` | Format: MM/YYYY | Must be valid month/year combination |

  | `dob` | Format: DD/MM/YYYY | Must be valid date in DD/MM/YYYY format |

  | `pincode` | Length: 6 digits | Must be exactly 6 numeric characters |

  | `pan_number` | Format: PAN | Must follow Indian PAN card format (10
  alphanumeric) |

  | `business_members` | Array | Can contain multiple business member objects |


  ---
api:
  file: Merchant Onboarding APIs for partners.postman_collection (5).json
  operationId: put_api-v1-merchants-uuid-submit-business-members
hidden: false
---