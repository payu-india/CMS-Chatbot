---
title: Payment Link TPV Complete Guide
deprecated: false
hidden: false
metadata:
  robots: index
---
Overview

TPV flow enables merchants to specify beneficiary account details for payment links. This document covers the complete flow from payment link creation to payment processing.

1.Create Payment Link – Beneficiary Details Format

Request Structure

{
 "amount": 5000.00,
 "maxPaymentsAllowed": 1,
 "beneficiarydetail": {
   "beneficiaryAccountNumber": ["917732227242", "72522762", "283228235"],   "ifscCode": ["SBIN0007001", "HDFC0001234", "ICIC0002522"]
 } 
}

| Field                    | Type         | Max Count | Format                                   | Example                         |
| ------------------------ | ------------ | --------- | ---------------------------------------- | ------------------------------- |
| beneficiaryAccountNumber | List<string> | 4         | Alphanumeric, max 50 chars               | \["917732227242", "72522762"]   |
| ifscCode                 | List<string> | 4         | Exactly 11 chars: \[A-Z]{4}0\[A-Z0-9]{6} | \["SBIN0007001", "HDFC0001234"] |

Constraints

• Equal Count: Account numbers and IFSC codes must have equal count

• maxPaymentsAllowed: Must be 1 (single payment only)

• Both Required: If provided, both fields must be present

• Optional: Entire beneficiarydetail object can be omitted

2.Intermediate/Prepayment Page - Data Format

Endpoint: GET /pay/{id}/intermediate

Backend sends beneficiary details to prepayment page (Frontend does not currently consume this data):

{
 "beneficiarydetail": {
   "beneficiaryAccountNumber": ["917732227242", "72522762", "283228235"],   "ifscCode": ["SBIN0007001", "HDFC0001234", "ICIC0002522"]
 } 
}

Format: Lists (same as create payment link format)

Note: Frontend displays these beneficiary accounts on the checkout page for user visibility.

3.Data Format Passed to \_payment API

When payment is initiated, backend converts beneficiary details to pipe-separated format and sends to \_payment API:

Format

{
 "beneficiarydetail": {
   "beneficiaryAccountNumber": "917732227242|72522762|283228235",   "ifscCode": "SBIN0007001|HDFC0001234|ICIC0002522"
 },
 "api_version": 20 
}

Conversion Logic

• Input: Lists from database (same format as create payment link)

• Processing: Join each list with pipe separator (|)

• Output: Pipe-separated strings in JSON object

Hash Generation Format

key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10 |beneficiarydetail|si\_details|user\_token|offer\_key|offer\_auto\_apply|cart\_details|SALT

Where beneficiarydetail is the JSON string representation: {"beneficiaryAccountNumber":"acc1|acc2","ifscCode":"IFSC1|IFSC2"}

5.Validation Rules

| Validation        | Rule                                     | Error Code |
| ----------------- | ---------------------------------------- | ---------- |
| Max Payments      | maxPaymentsAllowed = 1                   | 400        |
| Max Beneficiaries | ≤ 4 beneficiaries                        | 400        |
| Equal Count       | Account numbers = IFSC codes count       | 400        |
| Account Format    | Alphanumeric, max 50 chars               | 400        |
| IFSC Format       | Exactly 11 chars: \[A-Z]{4}0\[A-Z0-9]{6} | 400        |

6.Complete Flow Summary

1.Create Payment Link

  POST /paymentlink/create
  → beneficiarydetail: { beneficiaryAccountNumber: ["acc1", "acc2"], ifscCode: ["IFSC1", "IFSC2"] }
  → Stored in database (normalized table)

2.Intermediate Page

  GET /pay/{id}/intermediate
  → Backend sends: beneficiarydetail: { beneficiaryAccountNumber: ["acc1", "acc2"], ifscCode: ["IFSC1", "IFSC2"] }
  → Frontend displays accounts on checkout page

3.Payment Initiation

POST /payment (form-urlencoded)
→ email, phone, invoiceNumber, amount, firstName, lastName → Backend fetches beneficiary details from database

4.Payment Processing

  → Backend converts to pipe-separated format
  → POST to \_payment API: beneficiarydetail: { beneficiaryAccountNumber: "acc1|acc2", ifscCode: "IFSC1|IFSC2" }
  → api\_version: 20

7.Key Limitations

• Max Beneficiaries: 4 per payment link

• Max Payments: maxPaymentsAllowed = 1 (single payment only)

• Partial Payment: Not supported with TPV flow

• API Version: Version 20 required when beneficiary details present

8.Example Request/Response

Create Payment Link Request

{
"amount": 5000.00,
"maxPaymentsAllowed": 1,
"invoiceNumber": "INV123456789012",
"description": "Payment for services",
"customerName": "John Doe",
"customerEmail": "",
"customerPhone": "9876543210",
"beneficiarydetail": {
Number": ["917732227242", "72522762"],   "ifscCode": ["SBIN0007001", "HDFC0001234"]
,
"source": "API"

}

Intermediate Page Response

{
 "status": "SUCCESS",
 "data": {
   "invoiceNumber": "INV123456789012",
   "amount": 5000.00,
   "beneficiarydetail": {
    "beneficiaryAccountNumber": ["917732227242", "72522762"],    "ifscCode": ["SBIN0007001", "HDFC0001234"]
   }
 } 
}

Data Sent to \_payment API

{
 "key": "merchant_key",
 "txnid": "TXN123456",
 "amount": "5000.00",
 "productinfo": "Payment for services",
 "firstname": "John",
 "email": "",
 "beneficiarydetail": {
   "beneficiaryAccountNumber": "917732227242|72522762",   "ifscCode": "SBIN0007001|HDFC0001234"
 },
 "api_version": 20,
 "hash": "<generated_hash>" 
}
