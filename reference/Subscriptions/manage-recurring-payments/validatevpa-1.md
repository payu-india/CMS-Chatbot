---
api:
  file: validate-vpa-api.yaml
  operationId: validateVPA
hidden: true
---
Use this API to check whether a VPA is valid. For UPI Autopay or recurring payments, pass `var2` with a JSON string containing `validateAutoPayVPA` as `1`.

<Callout icon="👍" theme="okay">
  **Handy Tips**

  You should poll this API after a customer enters a VPA on the merchant page to check for its validation. If VPA is valid only then, the second call should be made.
</Callout>

## Sample Request

<Accordion title="Request Payload" icon="fa-code">
  <Validate_VPA />
</Accordion>

### Sample Request - Recurring Payments

Below is the validate VPA sample code for recurring payments.

<Accordion title="Request Payload" icon="fa-code">
  Lorem ipsum dolor sit amet, **consectetur adipiscing elit.** Ut enim
  ad minim veniam, quis nostrud exercitation ullamco. Excepteur sint
  occaecat cupidatat non proident!
</Accordion>
