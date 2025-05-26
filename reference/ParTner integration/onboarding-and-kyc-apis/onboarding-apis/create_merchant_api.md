---
title: Create Merchant API
excerpt: ''
api:
  file: partner-apis-26.json
  operationId: create_merchantv3
deprecated: false
hidden: false
metadata:
  title: Create Merchant API
  description: >-
    Learn how to use the PayU Create Merchant API to create new merchant
    accounts. This API reference page provides detailed instructions, request
    parameters, and sample responses for efficient merchant onboarding
  keywords:
    - Create Merchant API
    - ' merchant onboarding'
    - ' KYC details'
    - ' secure merchant creation'
    - ' tokenization'
    - ' manage merchants'
    - ' create merchant accounts'
  robots: index
next:
  description: ''
---
The **Create Merchant** API creates a new merchant account on PayU and posts all KYC details. This API returns the Merchant ID (MID) in the response.

## Authentication

This API is authorised through a client token generated using the client ID and secret. To create a token, call the get token API with `refer merchant` as a scope.  Refer to the  [Get Token API](ref:get_token_api) doc for more information.

> ❗️ Important considerations for using this API
>
> 1. The mobile, Pan number, GSTIN passed in the request has to be valid as checks are performed in real time.
> 2. If Business Entity type is passed in the create merchant API, ensure that the PAN also belong to the same entity.

<Accordion title="Endpoints" icon="fa-info-circle">
  endpoint
</Accordion>

## Request Parameters

<details>
  <summary>Reference information for request parameters</summary>

  | Parameter                          | Reference                                                                                                                  |
  | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
  | merchant\[business\_category]      | For the list of business categories, refer to [Business. Category List](ref:partner-category-list).                        |
  | merchant\[business\_entity\_type]  | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type).     |
  | merchant\[business\_sub\_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |
</details>