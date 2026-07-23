---
title: APIs for Recharge Integration
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

### Biller and Payment APIs

| API name                                                               | Description                                                                                                      |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [Get Biller Categories API](ref:get-biller-categories-api)             | Fetches all biller categories from PayU.                                                                         |
| [Get All Billers By Category API](ref:get-all-billers-by-category-api) | Fetches all billers for the biller category specified in the request.                                            |
| [Get All Billers By Region API](ref:get-all-billers-by-region-api)     | Fetches all billers for a specified region.                                                                      |
| [Bill Payment API](ref:bill-payment-api)                               | Sends payment information to make a bill payment.                                                                |
| [Bill Validation API](ref:bill-validation-api)                         | Validates bill details for BBPS and Connect billers that support optional or mandatory validation.               |
| [Get Payment Status API](ref:get-payment-status-api)                   | Retrieves the status of a bill payment transaction, including when the Bill Payment API response is interrupted. |

### Prepaid APIs

| API name                                                                                     | Description                                                                            |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [Get Circle List API](ref:get-circle-list-api)                                               | Retrieves a list of all available circles.                                             |
| [Get Operators List API](ref:get-operators-list-api)                                         | Retrieves all available mobile prepaid recharge operators and their basic information. |
| [Get Prepaid Recharge Plans API](ref:get-prepaid-recharge-plans-api)                         | Retrieves prepaid recharge plans for a specified agent, circle, and operator.          |
| [Get Operator and Circle By Mobile Number API](ref:get-operator-circle-by-mobile-number-api) | Identifies the operator and circle associated with a mobile number.                    |
| [Get Custom Recharge Plans API](ref:get-custom-recharge-plans-api)                           | Retrieves the available prepaid recharge plans for a mobile number.                    |

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
