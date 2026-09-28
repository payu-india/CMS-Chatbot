---
api:
  file: pl-test-oas.yaml
  operationId: GetTransactionDetailsAPI
hidden: false
---
Use this endpoint to fetch all payment attempts such as successful, failed, and pending recorded against a payment link.<br />

Use this to verify payment completion, reconcile partial payments, or displaypayment history. An empty `result` array is a valid success response when no payments have been attempted yet.
