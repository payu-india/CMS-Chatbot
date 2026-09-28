---
api:
  file: pl-test-oas.yaml
  operationId: SharePaymentLinkAPI
hidden: false
metadata:
  title: Share a Payment Link
next:
  description: Explore related information and resources.
---
Use this endpoint to resend a payment link notification to a customer. At least one of `viaEmail`,`viaSms`, or `viaWhatsapp` must be `true`. The customer's contact details are taken from the values stored on the link creation time.
