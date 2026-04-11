---
title: Start Here
deprecated: false
hidden: false
metadata:
  title: 'PayU Hosted Checkout Integration: Start Here Guide for Developers'
  description: >-
    Get started with PayU Hosted Checkout integration. Learn when to use it, how
    it works, and follow the right steps to begin accepting payments quickly.
  robots: index
---
## When to Use PayU Hosted Checkout

Use this approach if you want to:

* Go live quickly
* Avoid handling card or payment data
* Use a ready-made payment experience

Know More about PayU Hosted Checkout and how the payment flow works.

<Callout icon="📘" theme="info">
  **Other Integration Options:**

  Consider other integrations if you need:

  * Full control over payment UI
  * In-page checkout experience
  * Backend-only payment processing
</Callout>

## Prerequisites

Before you begin with PayU Hosted Checkout integration:

* Create a PayU account.
* Get your merchant key and salt for test and production environment.
* Make sure https success (surl) and failure (furl) URLs are reachable from the public internet.
* Ability to generate SHA-512 on the server (not recommended in browser).

## Integration Steps Overview

Below is the overview of the PayU Hosted Checkout integration:

1. Generate a payment request
2. Create a secure hash
3. Redirect user to PayU
4. Handle success/failure response (reverse hashing)
5. Verify the Payment

## Next Steps

Go to Quick Start Guide to create a first payment.