---
title: On-Hold Settlements - Cross-Border Payments
deprecated: false
hidden: true
metadata:
  robots: index
---
When processing outward settlements from India, authorized banks (AD-1) require additional information as per RBI regulations. Sometimes, settlements are **put on hold** or **rejected by the bank**. This guide explains:

* Why settlements may be on hold
* How to identify such transactions
* Steps to resolve and unblock them

## Transaction Statuses & Next Steps

| Transaction Status   | Description                                                                                                         | Next Steps                                                                                                                                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Needs Response**   | Settlement is temporarily on hold because mandatory information is missing.                                         | Provide the missing details before the due date shown in the **Submit before** column. For more information, refer to [Types of Settlement Holds](types-of-settlement-holds) table. |
| **Rejected by Bank** | The bank identified an anti-money laundering or sanction screening match on the buyer. Settlement is non-compliant. | Refund the transaction.                                                                                                                                                             |
| **Due Date Expired** | The time window (~7 days) for providing information has elapsed.                                                    | Contact your Account Manager for deadline extension.                                                                                                                                |
| **Settled**          | Settlement is completed. You can check the "Unique Transaction Reference."                                          | No action needed.                                                                                                                                                                   |

## Types of Settlement Holds

If the transaction status is **Needs Response**, additional information is required. Below are common scenarios and resolution steps:

| **Scenario**                                   | **Description**                                                         | **Required Information & Resolution Steps**                                                                                                                                                                                |
| ---------------------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Provide valid invoice number**               | Invoice number is mandatory for compliance on imports to India.         | You can provide the invoice number via:<br />1. **PayU Dashboard** → **On-hold Settlements** tab<br />2. Update `udf-5` (one-time payment) or `udf-3` parameters using the UDF Update API. <br />3. Use Invoice Upload API |
| **Provide complete name of buyer**             | Missing first name or last name of the buyer.                           | Update buyer details in your system and resubmit.                                                                                                                                                                          |
| **Provide complete name and address of buyer** | Missing buyer's full name or address.                                   | Ensure full name and address are captured and updated.                                                                                                                                                                     |
| **Provide PAN and DOB of buyer**               | Required for compliance verification.                                   |                                                                                                                                                                                                                            |
| **Non-Individual cases cannot be processed**   | Transactions involving entities other than individuals are not allowed. |                                                                                                                                                                                                                            |
| **Amlock match found and cannot be processed** |                                                                         |                                                                                                                                                                                                                            |

### **Key Tips for Merchants**

* Always ensure **buyer details** (name, address, PAN, DOB) are accurate before initiating settlements.
* Keep **invoice numbers** ready and update them promptly.
* Monitor the **PayU dashboard** for any "Needs Response" alerts.
* Act within the **7-day window** to avoid delays or expired deadlines.
