---
title: BNPL FAQs
deprecated: false
hidden: true
metadata:
  robots: index
---
## General

<Accordion title="How do I enable BNPL on my account?" icon="far fa-toggle-on">
  BNPL isn't enabled by default. Contact your PayU Key Account Manager or [PayU Support](https://help.payu.in/raise-ticket), and tell them which lenders you want.
</Accordion>

<Accordion title="Which lenders are supported?" icon="far fa-building-columns">
  LazyPay (`LAZYPAY`), Simpl (`SIMPL`), HDFC FlexiPay (`HDFCF15`, `HDFCF30`, `HDFCF60`, `HDFCF90`), and others. See [BNPL Codes](doc:bnpl-codes) for the full list.
</Accordion>

<Accordion title="Which integration should I choose?" icon="far fa-signs-post">
  - **PayU Hosted Checkout** if you want the fastest go-live with minimal code.
  - **Merchant Hosted Checkout** if you want BNPL on your own checkout page, with optional native OTP.
  - **Link and Pay** if you have many repeat customers and want one-click checkout.

  See [Choose Your Integration](doc:bnpl#choose-your-integration).
</Accordion>

***

## Eligibility

<Accordion title="Do I need to check eligibility before every payment?" icon="far fa-user-check">
  It's strongly recommended for Merchant Hosted, and it's part of the Link and Pay flow. Eligibility can change between payments (for example, because of overdue bills or credit limits). Checking first avoids showing lenders the customer can't use.
</Accordion>

<Accordion title="Why must the phone number match between the eligibility check and the payment?" icon="far fa-phone">
  The lender checks eligibility and links accounts using the mobile number. If the `phone` in `_payment` is different, the payment may fail or not match the linked account.
</Accordion>

***

## OTP and Native OTP

<Accordion title="What's the difference between otpPostUrl and acsTemplate?" icon="far fa-mobile-screen-button">
  With `txn_s2s_flow=4`, PayU may return both. If `otpPostUrl` is present, collect the OTP on your UI and submit it there. If it's missing, Base64-decode `acsTemplate` and render it to open PayU's OTP page.
</Accordion>

<Accordion title="Can I use txn_s2s_flow=2 for BNPL?" icon="far fa-ban">
  No. Use `txn_s2s_flow=4` for native OTP, or leave it out for the redirect flow.
</Accordion>

<Accordion title="What happens if the customer enters a wrong OTP?" icon="far fa-rotate-right">
  The Submit OTP response returns `submitOtp.status=in progress` with `retryAttemptCount` (attempts left). Let the customer retry with the same `referenceId`.
</Accordion>

***

## Link and Pay

<Accordion title="Will repeat customers never see an OTP?" icon="far fa-bolt">
  Not always. Repeat payments skip the OTP while the saved link is valid. If the link has expired or was de-linked, or the transaction needs extra verification, the OTP flow runs. Your integration must always handle an OTP step.
</Accordion>

<Accordion title="What value should I pass in linkAndPayFlowType?" icon="far fa-hashtag">
  Always pass `1` for Link and Pay, on first-time and repeat payments alike, together with `txn_s2s_flow=4`.
</Accordion>

<Accordion title="Where do I pass the payuToken on repeat payments?" icon="far fa-key">
  Pass it in the `store_card_token` parameter of the `_payment` request.
</Accordion>

<Accordion title="How does a customer remove a linked BNPL account?" icon="far fa-link-slash">
  Call the [Delete Payment Instrument API](ref:delete_payment_instrument) with `user_credentials` and the `payuToken`. Customers can also de-link from the lender's app. After de-linking, the next payment needs an OTP.
</Accordion>

***

## Testing and Going Live

<Accordion title="Which phone number should I use for testing?" icon="far fa-flask">
  Use `9876543210` in the test environment. See [Test BNPL Integration](doc:bnpl-test-integration).
</Accordion>

<Accordion title="What's the production payment URL?" icon="far fa-globe">
  `https://secure.payu.in/_payment`. The test URL is `<redacted URL>`.
</Accordion>

<Accordion title="How are refunds handled for BNPL payments?" icon="far fa-arrow-rotate-left">
  BNPL refunds use the standard PayU refund flow. See the [Refund API](ref:cancel_refund_transaction).
</Accordion>

{/* REVIEW: Confirm the Refund API reference slug. */}
