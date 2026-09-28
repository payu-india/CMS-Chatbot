---
api:
  file: pl-test-oas.yaml
  operationId: UpdatePaymentLinkAPI
hidden: false
metadata:
  title: Update a Payment Link
next:
  description: Explore related information and resources.
---
Use this endpoint to modify the configuration of an existing active payment link.<br />

Only send the fields you want to change. Your omitted fields retain their current values.

<Callout icon="fad fa-brake-warning" theme="error">
  ### **Restrictions**

  You cannot:

  - Update a cancelled link (`active: false`).
  - Update a link that has been fully paid.
  - Reduce `subAmount` below the amount already collected on a partial payment link.
</Callout>
