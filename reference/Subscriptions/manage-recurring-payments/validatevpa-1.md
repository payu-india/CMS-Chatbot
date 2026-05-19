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

<Accordion title="Sample Payload" icon="fa-code">

<Validate_VPA />

</Accordion>

###
