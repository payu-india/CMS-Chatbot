---
title: Create signatory_details
excerpt: >-
  # **Submit Signatory Details API Documentation**


  ## **API Overview**


  **Method:** `PUT`  

  **Endpoint:** `/api/v1/merchants/{product_account_uuid}/signatory_details`  

  **Content-Type:** `multipart/form-data`  

  **Purpose:** Submit or update signatory contact details and Ultimate
  Beneficial Owner (UBO) information for a merchant


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


  ## **Signatory Contact Details & UBO API Parameter Description Table**


  | Parameter | Field Name | Data Type | Example Value | Description |

  | --- | --- | --- | --- | --- |

  | **Signatory Contact Details** |  |  |  |  |

  | `merchant[signatory_contact_details_attributes[0][name]]` | Signatory Name |
  String | Ayantika | Name of the authorized signing authority |

  | `merchant[signatory_contact_details_attributes[0][pancard_number]]` |
  Signatory PAN | String | AUKPAXXXXX | PAN card number of the signing authority
  |

  | `merchant[signatory_contact_details_attributes[0][cin_number]]` | Signatory
  CIN | String | U15492HR2012PTC0XXXXX | CIN number ⚠️ **DO NOT SEND this if
  this is already updated using the update merchant API. Else, it will update
  existing value** |

  | `merchant[signatory_contact_details_attributes[0][email]]` | Signatory Email
  | String | [uatprod14@yopmail.com](https://mailto:uatprod14@yopmail.com) |
  Email address of the signing authority |

  | `merchant[signatory_contact_details_attributes[0][contact_detail_type]]` |
  Contact Detail Type | String | Signing Authority | Type of contact detail
  (fixed value) |

  | **Ultimate Beneficial Owner (UBO) - Entry 1** |  |  |  |  |

  | `merchant[ubo[0][id]]` | UBO 1 ID | Number | 1168 | **UPDATE ONLY:**
  Required only for UBO updates. Not needed for creation. Returned in response
  body after creation for subsequent updates |

  | `merchant[ubo[0][beneficiary_name]]` | UBO 1 Name | String | Spoorthi Mohan
  Naik | Full name of the first ultimate beneficial owner |

  | `merchant[ubo[0][address][address_line]]` | UBO 1 Address | String | C-37,
  Block 24, Munekollal | Complete address of the first UBO |

  | `merchant[ubo[0][address][pincode]]` | UBO 1 Pincode | String | 122001 |
  Postal code of the first UBO's address |

  | `merchant[ubo[0][dob]]` | UBO 1 Date of Birth | Date | 2001-02-24 | Date of
  birth in YYYY-MM-DD format |

  | `merchant[ubo[0][nationality]]` | UBO 1 Nationality | String | IN | Country
  code (IN for India) |

  | `merchant[ubo[0][ownership_percent]]` | UBO 1 Ownership % | Number | 10.0 |
  Percentage of ownership in the business |

  | `merchant[ubo[0][ubo_pan_number]]` | UBO 1 PAN Number | String | BXWPN2524C
  | PAN card number of the first UBO |

  | **Ultimate Beneficial Owner (UBO) - Entry 2** |  |  |  |  |

  | `merchant[ubo[1][id]]` | UBO 2 ID | Number | 1169 | **UPDATE ONLY:**
  Required only for UBO updates. Not needed for creation. Returned in response
  body after creation for subsequent updates |

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

  | `merchant[ubo[1][ownership_percent]]` | UBO 2 Ownership % | Number | 15 |
  Percentage of ownership in the business |

  | `merchant[ubo[1][ubo_pan_number]]` | UBO 2 PAN Number | String | GKVPPXXXXX
  | PAN card number of the second UBO |

  | **UBO Configuration** |  |  |  |  |

  | `merchant[ubo_exist]` | UBO Exists Flag | Number | 1 | Indicates whether UBO
  to be creaate(1 = Yes, 0 = No) |


  ## **API Validation Rules**


  ### **Request Combination Rules**


  | Scenario | UBO Status | Signing Authority Status | Result |

  | --- | --- | --- | --- |

  | **Creation** | New | New | ✅ Both created successfully |

  | **Mixed Update** | New | Already exists | ❌ UBO will **NOT** be updated -
  send UBO only |

  | **UBO Only** | New/Update | Not included | ✅ UBO processed normally |


  ### **UBO Business Rules**


  | Rule | Requirement | Description |

  | --- | --- | --- |

  | **Ownership Threshold** | \>10% | Only members with more than 10% ownership
  can be added as UBO |

  | **Maximum Ownership** | ≤100% | Total cumulative ownership of all UBOs must
  not exceed 100% |

  | **Creation Limit** | Unlimited | No maximum limit on number of UBOs that can
  be created |

  | **Update Requirement** | All fields | When updating UBO with ID, all UBO
  fields must be included |


  ---


  ## **Expected Responses**


  - **Success:** `200 OK` with updated signatory and UBO details
      
  - **Validation Error:** `422 Unprocessable Entity` with error details
      
  - **Unauthorized:** `401 Unauthorized` (if bearer token is invalid)
      
  - **Not Found:** `404 Not Found` (if product_account_uuid doesn't exist)
api:
  file: >-
    Merchant Onboarding APIs - Business members & signing authority
    details.postman_collection.json
  operationId: put_api-v1-merchants-product-account-uuid-signatory-details
hidden: false
---