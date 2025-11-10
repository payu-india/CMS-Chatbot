---
title: Add/update UBO
excerpt: >-
  # **Update UBO Details API Documentation**


  ## **API Overview**


  **Method:** `PUT`  

  **Content-Type:** `multipart/form-data`  

  **Purpose:** Update existing Ultimate Beneficial Owner (UBO) information for a
  merchant account


  ---


  ## **Endpoints**


  | Environment | Endpoint | Description | Usage |

  | --- | --- | --- | --- |

  | **Test** |
  `https://test-partner.payu.in/api/v1/merchants/{product_account_uuid}/signatory_details`
  | Testing/Sandbox environment | Development, testing, and integration purposes
  |

  | **Production** |
  `https://partner.payu.in/api/v1/merchants/{product_account_uuid}/signatory_details`
  | Live production environment | Live transactions and production use |


  ---


  ## **Path Parameters**


  | Parameter | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `product_account_uuid` | String | ✅ Yes | Unique identifier for the
  merchant's product account. The product_account_uuid is returned as `uuid` in
  the response of the create merchant API |
  `11f0-8976-5bf48f4c-baa1-02975f21d323` |


  ---


  ## **Headers**


  | Header | Data Type | Required | Description | Example |

  | --- | --- | --- | --- | --- |

  | `Authorization` | String | ✅ Yes | Bearer token for authentication. Get the
  token using the GET token API with the scope refer_merchant |
  `{{vault:bearer-token}}` |


  ---


  ## **UBO Update API Parameter Description Table**


  | Parameter | Field Name | Data Type | Example Value | Description |

  | --- | --- | --- | --- | --- |

  | **Ultimate Beneficial Owner (UBO) - Entry 1** |  |  |  |  |

  | `merchant[ubo[0][id]]` | UBO 1 ID | Number | 1178 | **UPDATE ONLY:**
  Required for UBO updates. Used to identify existing UBO record for update |

  | `merchant[ubo[0][beneficiary_name]]` | UBO 1 Name | String | Harsh Agarwal |
  Full name of the first ultimate beneficial owner |

  | `merchant[ubo[0][address][address_line]]` | UBO 1 Address | String | C-37,
  Block 24, Munekollal | Complete address of the first UBO |

  | `merchant[ubo[0][address][pincode]]` | UBO 1 Pincode | String | 560070 |
  Postal code of the first UBO's address |

  | `merchant[ubo[0][dob]]` | UBO 1 Date of Birth | Date | 1992-10-18 | Date of
  birth in YYYY-MM-DD format |

  | `merchant[ubo[0][nationality]]` | UBO 1 Nationality | String | IN | Country
  code (IN for India) |

  | `merchant[ubo[0][ownership_percent]]` | UBO 1 Ownership % | Number | 21.0 |
  Percentage of ownership in the business. Allowed upto two decimal places |

  | `merchant[ubo[0][ubo_pan_number]]` | UBO 1 PAN Number | String | AUKPA1386M
  | PAN card number of the first UBO |

  | **Ultimate Beneficial Owner (UBO) - Entry 2** |  |  |  |  |

  | `merchant[ubo[1][id]]` | UBO 2 ID | Number | 1169 | **UPDATE ONLY:**
  Required for UBO updates. Used to identify existing UBO record for update |

  | `merchant[ubo[1][beneficiary_name]]` | UBO 2 Name | String | Ayantika
  Pramanick | Full name of the second ultimate beneficial owner |

  | `merchant[ubo[1][address][address_line]]` | UBO 2 Address | String | C-37,
  Block 24, Munekollal | Complete address of the second UBO |

  | `merchant[ubo[1][address][pincode]]` | UBO 2 Pincode | String | 122001 |
  Postal code of the second UBO's address |

  | `merchant[ubo[1][dob]]` | UBO 2 Date of Birth | Date | 2000-02-14 | Date of
  birth in YYYY-MM-DD format |

  | `merchant[ubo[1][nationality]]` | UBO 2 Nationality | String | IN | Country
  code (IN for India) |

  | `merchant[ubo[1][ownership_percent]]` | UBO 2 Ownership % | Number | 45.0 |
  Percentage of ownership in the business. Allowed upto two decimal places |

  | `merchant[ubo[1][email]]` | UBO 2 Email | String |
  [ubo@yopmail.com](https://mailto:ubo@yopmail.com) | Email address of the
  second UBO (optional field) |

  | `merchant[ubo[1][ubo_pan_number]]` | UBO 2 PAN Number | String | GKVPP9366K
  | PAN card number of the second UBO |

  | **UBO Configuration** |  |  |  |  |

  | `merchant[ubo_exist]` | UBO Exists Flag | Number | 1 | Indicates whether UBO
  data need to be added (1 = Yes, 0 = No) |


  ---


  ## **API Validation Rules**


  ### **Update Operation Rules**


  | Scenario | UBO Status | ID Requirement | Result |

  | --- | --- | --- | --- |

  | **Update Existing** | Already exists | ✅ Required | ✅ UBO details updated
  successfully |

  | **Mixed Update** | Some exist, some new | ✅ ID for existing only | ✅
  Existing updated, new created |


  ### **UBO Business Rules**


  | Rule | Requirement | Description |

  | --- | --- | --- |

  | **Ownership Threshold** | \>10% | Only members with more than 10% ownership
  can be added as UBO |

  | **Maximum Ownership** | ≤100% | Total cumulative ownership of all UBOs must
  not exceed 100% |

  | **Update Requirement** | All fields | When updating UBO with ID, all UBO
  fields must be included |

  | **Current Ownership** | 21.0% + 45% = 66% | Total ownership in this example
  is 66% (valid) |


  ---


  ## **Expected Responses**


  - **Success:** `200 OK` with updated UBO details
      

  - **Unauthorized:** `401 Unauthorized` (if bearer token is invalid)
      
  - **Not Found:** `404 Not Found` (if product_account_uuid or UBO IDs don't
  exist)
      

  ## **Sample Response**


  ``` json

  {
      "merchant": {
          "signing_authority_details": [
              {
                  "id": 2184210,
                  "uuid": "11f0-92bd-13b91ee6-8666-023e56ad7fcb",
                  "name": "Ayantika",
                  "email": "uatprod14@yopmail.com",
                  "pancard_number": "AUKPA1386M",
                  "authorised_signatory": true,
                  "contact_detail_type": "Signing Authority",
                  "active": true
              }
          ],
          "ultimate_beneficiaries": [
              {
                  "id": 44004,
                  "uuid": "11f0-92bd-c464590e-87f0-02a5a32ea4dd",
                  "name": "Spoorthi Mohan Naik",
                  "ubo_pan_number": "BXWPN2524C",
                  "type": "UltimateBeneficiary",
                  "ownership_percent": "10.0",
                  "dob": "2001-02-24",
                  "active": true,
                  "address": {
                      "id": 2707067,
                      "address_line": "C-37, Block 24, Munekollal",
                      "city": "Gurgaon",
                      "state": "HARYANA",
                      "pincode": 122001
                  }
              },
              {
                  "id": 44005,
                  "uuid": "11f0-92bd-c49a9280-87f0-02a5a32ea4dd",
                  "name": "Ayantika Pramanick",
                  "ubo_pan_number": "GKVPP9366K",
                  "type": "UltimateBeneficiary",
                  "ownership_percent": "45.0",
                  "dob": "2000-02-14",
                  "active": true,
                  "address": {
                      "id": 2707068,
                      "address_line": "C-37, Block 24, Munekollal",
                      "city": "Gurgaon",
                      "state": "HARYANA",
                      "pincode": 122001
                  }
              }
          ]
      }
  }

   ```
api:
  file: Merchant Onboarding APIs for partners.postman_collection_updated.json
  operationId: put_api-v1-merchants-11f0-8976-5bf48f4c-baa1-02975f21d323-signatory-details
hidden: false
---