---
title: Check Action Status with PayU ID
excerpt: >-
  Check the action status of a transaction using PayU Transaction ID (mihpayid).


  This API returns all actions related to a specified PayUID (mihpayid),
  including:

  - Transaction capture status

  - Refund actions and their statuses  

  - Settlement information

  - Payment mode details

  - Complete transaction timeline


  **Important:** This API will return comprehensive transaction history, not
  limited to refunds but including captures and other transaction statuses.
api:
  file: payu_check_action_status_payuid_oas31.json
  operationId: checkActionStatusWithPayUId
hidden: true
---