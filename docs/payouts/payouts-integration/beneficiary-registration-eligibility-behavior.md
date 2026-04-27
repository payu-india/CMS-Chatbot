---
title: Beneficiary Registration Eligibility & Behavior
deprecated: false
hidden: true
metadata:
  robots: index
---
Manual Beneficiary registration provides control but increases effort. Auto registration simplifies integration and improves success rates when supported.

## Prerequisites

* Merchant is enabled for the feature
* Bank and payout method support auto registration

If these conditions are not met, payouts may require manual beneficiary registration or in some cases no beneficiary registration is required.

<Callout icon="📘" theme="info">
  **Enable Eligibility & Behavior**: To enable this feature in Beneficiary Registration, contact your PayU Key Account Manager (KAM) to check it is applicable for your case.
</Callout>

## Error Handling & Troubleshooting

* Invalid details (e.g., malformed IFSC or VPA): Beneficiary Registration might fail for such cases.
* Duplicate beneficiary attempt: In case of duplicate beneficiary registration attempts, payouts ignore the beneficiary registration and proceeds with the Payouts directly.
* Transient failures during inline creation: Retry with backoff is implemented at payouts hence there are almost no cases of this happening.
