---
title: Go SDK
deprecated: false
hidden: true
metadata:
  robots: index
---
Use the PayU Go SDK to integrate PayU payments into your website built using Go. The PayU Go SDK handles low-level API integration details, enabling you to start collecting payments with just a few lines of code and a function call.

***

## Payment Workflow with PayU Go SDK

The PayU Go SDK supports the complete payment lifecycle—from payment initiation to post-payment operations.

<Accordion title="1. Accept Payments" icon="fa-money-check-dollar">
Start collecting payments from customers by creating a payment form.
</Accordion>

<Accordion title="2. Verify Payment Status" icon="fa-circle-check">
After payment completion, verify whether the transaction was successful or check its current status.
</Accordion>

<Accordion title="3. Handle Post-Payment Operations" icon="fa-receipt">
Manage these payment-related operations after a transaction is completed.
- **Handle Refunds:** Initiate or cancel refunds and check refund status.
- **Manage Invoices:** Create or expire invoice links through SDK functions.
</Accordion>

<Accordion title="4. Reconcile Payments" icon="fa-scale-balanced">
Track settlements and ensure payments are settled correctly to your account.
</Accordion>

<Accordion title="5. Optimize Payment Experience" icon="fa-gauge-high">
Improve payment success rates by checking payment availability and offering eligible payment options.
- **Check Bank Downtime Status:** Get information on eligible payment options and PG/bank downtime details.
- **Check Eligibility:** Check customer eligibility for EMI and get the amount according to EMI interest.
</Accordion>

### When to Use This SDK

You can use this SDK when:

- Your Backend is Go
- You want PayU-hosted payment form
- You need server-side payment verification

These are some of the use cases:

<Accordion title="E-commerce Order Fulfillment Gated on Verified Payment (UrbanCart)" icon="fa-box-open">
UrbanCart, a D2C e-commerce marketplace processing 50,000 orders a day through Go microservices, needs to confirm that a customer's payment has been verified server-side before it reserves inventory permanently and triggers shipment. This happens at the boundary between checkout completion and order fulfillment, and it matters because releasing inventory or shipping against an unconfirmed or reversible payment creates direct financial loss and inventory discrepancies at scale.<br/>

Using PayU Go SDK UrbanCart can:<br/>
- Generate the request hash and build hosted checkout payment requests to securely collect payments at high volume.
- Independently verify transaction status and validate the reverse hash on every callback, rather than trusting the browser redirect alone to confirm a payment before fulfilling an order.
- Use the PayU Go SDK's refund initiation and refund status check to support returns and cancellations.
</Accordion>

<Accordion title="EdTech Enrollment Activation Gated on Confirmed Payment (LearnSphere)" icon="fa-user-graduate">
earnSphere, an EdTech platform selling certification courses priced between ₹15,000–₹1,20,000, needs to activate a learner's enrollment and unlock course content only once payment — including EMI-based payment — is confirmed. This happens between checkout and content access, and it matters because EMI transactions can confirm with a delay, and premature activation risks granting access without settled payment or regulatory-compliant refund handling.<br/>

Using PayU Go SDK LearnSphere can:<br/>
- Check EMI eligibility for the customer's card/bank before checkout to offer EMI as a payment option.
- Generate the hash and create the checkout request for the selected plan to collect payment for a course
- Validate the reverse hash and verify transaction status before touching enrollment state to activate enrollment only on confirmed payment.
- Honor cooling-off-period refund policies by using Go SDK's refund initiation.
</Accordion>

<Accordion title="Travel Booking Confirmation Synchronized with Payment and Supplier Hold (TripWing)" icon="fa-plane-departure">
TripWing, an online travel aggregator booking flights and hotels through a Go orchestration service, needs to confirm payment within a supplier's time-boxed inventory hold window and only then confirm the booking with the airline or hotel. This happens between the inventory hold and supplier confirmation, and it matters because travel inventory is finite and time-sensitive — a slow or unverified payment can mean a customer is charged without a seat or room, or vice versa.<br/>

Using PayU Go SDK TripWing can:<br/>
- Generate the hash and create a checkout request with expiry aligned to that window to collect payment within a supplier hold window.
- Validate the reverse hash and check transaction status before calling the supplier's confirm-booking API to confirm a booking only on verified payments.
- Automatically compensate the customer if a supplier confirmation later fails.
- Check bank/PG downtime status and route customers accordingly to reduce failed payments during peak booking periods.
</Accordion>

***

## Other Integration Options

If you want:

- Frontend JavaScript integration → You can choose Web SDK.
- Mobile app → You can choose Android/iOS SDK.

***

## Supported Payment Methods

_Need Content Here._

<br />
