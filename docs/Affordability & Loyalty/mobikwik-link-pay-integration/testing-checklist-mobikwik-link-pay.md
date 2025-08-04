---
title: Testing Checklist -  Mobikwik Link & Pay
deprecated: false
hidden: false
metadata:
  robots: index
---
## Testing Checklist

* [ ] API response validation for all endpoints
* [ ] Checksum generation and verification
* [ ] Token generation and storage
* [ ] Auto-debit success and failure scenarios
* [ ] OTP flow for new users
* [ ] Add Money & Debit flow
* [ ] Transaction status verification
* [ ] Refund processing
* [ ] Error handling for all scenarios

### Best Practices

<Accordion title="User Experience" icon="fa-user">
  * Minimize user interactions for repeat customers
  * Provide clear error messages
  * Implement smooth fallback flows
</Accordion>

<Accordion title="Performance" icon="fa-tachometer-alt">
  * Cache wallet link status
  * Implement timeout handling for API calls
  * Use async processing where applicable
</Accordion>

<Accordion title="Monitoring" icon="fa-chart-line">
  * Track wallet usage metrics
  * Monitor auto-debit failure rates
  * Alert on API response anomalies
</Accordion>