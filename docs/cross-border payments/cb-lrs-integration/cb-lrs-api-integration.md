---
title: CB LRS API Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
PayU’s **\_payment** API supports LRS implementation using the following parameters:

* buyer\_type\_business
* lrs\_mandatory\_limit\_declaration
* lrs\_tnc
* lrs\_tcs\_declaration\_under\_limit

## Integration Flow

* **Identify Transaction Type**:
  * Determine if the transaction falls under LRS (cross-border, individual buyer)
  * Set **buyer\_type\_business** appropriately
* **Collect Buyer PAN Information**:
  * For individual buyers, capture and validate PAN details
  * Ensure PAN is linked to Aadhaar for successful transaction processing
* **Present LRS Declarations**:
  * Display and capture acceptance of lrs\_mandatory\_limit\_declaration
  * Display and capture acceptance of lrs\_tnc
  * If applicable, capture lrs\_tcs\_declaration\_under\_limit
* **Proceed with Payment**:
  * Include all required LRS parameters in the payment API call
  * Process transaction through PayU gateway