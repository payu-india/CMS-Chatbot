---
title: APIs for BBPS Agent API Integration
excerpt: ''
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
### Token API

| API name                                | Description                                                              |
| --------------------------------------- | ------------------------------------------------------------------------ |
| [Get Token API](ref:get-token-api-bbps) | Generates an authentication token using the client ID and client secret. |

### Biller APIs

| API name                                                               | Description                                                           |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------- |
| [Get Biller Categories API](ref:get-biller-categories-api)             | Fetches all biller categories from PayU.                              |
| [Get All Billers By Category API](ref:get-all-billers-by-category-api) | Fetches all billers for the biller category specified in the request. |
| [Get All Billers By Region API](ref:get-all-billers-by-region-api)     | Fetches all billers for a specified region.                           |

### Bill APIs

| API name                                             | Description                                                                                                      |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [Bill Fetch API](ref:bill-fetch-api)                 | Fetches bill details, including pending amounts and other information, from the biller.                          |
| [Get Payment Status API](ref:get-payment-status-api) | Retrieves the status of a bill payment transaction, including when the Bill Payment API response is interrupted. |
| [Bill Validation API](ref:bill-validation-api)       | Validates bill details for BBPS and Connect billers that support optional or mandatory validation.               |
| [Biller Plans API](ref:biller-plans-api)             | Fetches the plans available for a biller.                                                                        |

### Complaint-related APIs

| API name                                                     | Description                                                                               |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| [Raise BBPS Complaint API](ref:raise-bbps-complaint-api)     | Raises a biller-related or transaction-related complaint for a specific BBPS transaction. |
| [Check Complaint Status API](ref:check-complaint-status-api) | Retrieves the status of a complaint using its complaint ID.                               |

### Health Check API

| API name                                               | Description                                   |
| ------------------------------------------------------ | --------------------------------------------- |
| [Check Health Status API](ref:check-health-status-api) | Checks the working status of the PayU server. |

<br />