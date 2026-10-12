---
title: Buy Now Pay Later (BNPL)
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
---
title: Buy Now Pay Later (BNPL)
excerpt: >-
  Let customers buy now and pay later with LazyPay, Simpl, HDFC FlexiPay, and
  other BNPL lenders through a single PayU integration. Choose PayU Hosted
  Checkout, Merchant Hosted Checkout, or Link and Pay one-click checkout.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  title: Buy Now Pay Later (BNPL) Payments | PayU Docs
  description: >-
    Accept Buy Now Pay Later (BNPL) payments with PayU. Check customer
    eligibility, support LazyPay, Simpl, and HDFC FlexiPay, and enable one-click
    repeat checkout with Link and Pay.
  keywords:
    - payu bnpl integration
    - buy now pay later payment gateway india
    - payu lazypay simpl integration
    - payu pay later checkout
    - bnpl eligibility check api
    - bnpl link and pay one click checkout
    - payu bnpl merchant hosted native otp
    - hdfc flexipay payu
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: bnpl-workflow
      title: How BNPL Works
      type: basic
    - slug: bnpl-payu-hosted-integration
      title: BNPL with PayU Hosted Checkout
      type: basic
    - slug: bnpl-merchant-hosted-integration
      title: BNPL with Merchant Hosted Checkout
      type: basic
    - slug: bnpl-link-and-pay-merchant-hosted
      title: BNPL Link and Pay (Merchant Hosted)
      type: basic
    - slug: bnpl-test-integration
      title: Test BNPL Integration
      type: basic
    - slug: bnpl-errors-and-troubleshooting
      title: BNPL Errors and Troubleshooting
      type: basic
    - slug: bnpl-faqs
      title: BNPL FAQs
      type: basic
---
<Banner
  isInline={true}
  message="Integration effort: Minimal (PayU Hosted) to moderate (Merchant Hosted and Link and Pay)"
  color="#FFC107"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

Buy Now Pay Later (BNPL) lets your customers buy goods or services now and pay the lender later. PayU brings several BNPL lenders together behind one integration. PayU handles routing, eligibility checks, and lender authentication for you.

<Callout icon="📘" theme="info">
  ### **Before You Start**

  Register for a PayU merchant account before you integrate. See [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard). BNPL isn't enabled by default. Contact your PayU Key Account Manager or [PayU Support](https://help.payu.in/raise-ticket) to enable it.
</Callout>

***

## Why Use BNPL?

<Accordion title="One Integration, Multiple Lenders" icon="fa-layer-group">
  Offer LazyPay, Simpl, HDFC FlexiPay, and other supported lenders through the same `_payment` API. To switch lenders, you only change the `bankcode`.
</Accordion>

<Accordion title="Show BNPL Only to Eligible Customers" icon="fa-user-check">
  Check a customer's eligibility before you show the BNPL option. This prevents failed attempts at the last step of checkout.
</Accordion>

<Accordion title="One-Click Repeat Checkout with Link and Pay" icon="fa-bolt">
  After a customer links their BNPL account once, later payments can go through without an OTP. If the saved link is no longer valid, PayU falls back to OTP automatically.
</Accordion>

<Accordion title="Native OTP on Your Own Page" icon="fa-mobile-screen-button">
  With Merchant Hosted Checkout, you can collect the lender OTP on your own UI instead of redirecting the customer.
</Accordion>

***

## Is BNPL Right for Me?

| I want to…                                                       |                                Works?                                |
| ---------------------------------------------------------------- | :------------------------------------------------------------------: |
| Add pay later as an option on PayU's checkout page               |            ✅ [PayU Hosted](doc:bnpl-payu-hosted-integration)          |
| Show BNPL lenders on my own checkout page                        |       ✅ [Merchant Hosted](doc:bnpl-merchant-hosted-integration)       |
| Capture the lender OTP on my own UI                              |   ✅ [Merchant Hosted (native OTP)](doc:bnpl-merchant-hosted-integration) |
| Let returning customers pay without entering an OTP each time    |       ✅ [Link and Pay](doc:bnpl-link-and-pay-merchant-hosted)         |
| Offer EMI on credit or debit cards                               |                 ⚠️ Use [EMI](doc:emi-integration)                    |
| Set up recurring auto-debits or subscriptions                    |         ⚠️ Use [Recurring Payments](doc:recurring-payments)          |

{/* REVIEW: Confirm the EMI slug `emi-integration` before publishing. */}

<Callout icon="far fa-face-thinking" theme="warn">
  ### **Not Sure Which PayU Solution Is Right for You?**

  <Anchor target="_blank" href="https://docs.payu.in/docs/start-here">Find the Right Product for You</Anchor> →
</Callout>

***

## Common Use Cases

<Cards>
  <Card title="Quick Commerce and Grocery" icon="fa-basket-shopping">
    Small, frequent orders where one-click repeat payments reduce checkout drop-off.
  </Card>

  <Card title="Food Delivery" icon="fa-utensils">
    Returning customers pay through a linked BNPL account in a single tap.
  </Card>

  <Card title="Telecom and Recharges" icon="fa-tower-cell">
    High-repeat, low-ticket payments where speed matters.
  </Card>

  <Card title="Fashion and E-commerce" icon="fa-bag-shopping">
    Give customers a pay-later option at checkout without changing your payment stack.
  </Card>
</Cards>

***

## What Will I Need?

<Columns layout="fixed">
  <Column>
    **A PayU merchant account** with BNPL enabled. <Anchor target="_blank" href="https://docs.payu.in/docs/set-up-your-account">Sign up here</Anchor> if you don't have an account.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Merchant key and salt:** test credentials for the sandbox and production credentials to go live. See [Generate Test Key and Salt](https://docs.payu.in/docs/generate-test-merchant-key-and-salt).
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **A backend server** that generates the SHA-512 hash and verifies PayU's response. Never generate the hash on the client.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **The customer's mobile number:** BNPL lenders use it for eligibility checks and OTP authentication.
  </Column>
</Columns>

<Columns layout="fixed">
  <Column>
    **Link and Pay only:** PayU (and the lender) must approve Link and Pay for your account. Contact your PayU Key Account Manager.
  </Column>
</Columns>

***

## Choose Your Integration

| Integration                                                       | Who hosts the payment UI | OTP handling                                    | Best for                                         |
| ----------------------------------------------------------------- | ------------------------ | ----------------------------------------------- | ------------------------------------------------ |
| [PayU Hosted Checkout](doc:bnpl-payu-hosted-integration)          | PayU                     | PayU's page                                     | Fastest go-live, minimal code                    |
| [Merchant Hosted Checkout](doc:bnpl-merchant-hosted-integration)  | You                      | Redirect to lender/PayU page, or native OTP     | Full control over your checkout UI               |
| [Link and Pay](doc:bnpl-link-and-pay-merchant-hosted)             | You                      | OTP on first payment, no OTP on repeat payments | High-repeat businesses that want one-click checkout |

***

## Customer Journey

### First-Time Customer

1. **Eligibility check:** Your server checks whether the customer is eligible for BNPL lenders.
2. **Lender selection:** The customer picks a lender (for example, LazyPay) and confirms their mobile number.
3. **OTP authentication:** The lender sends an OTP. The customer enters it on your page (native OTP) or on PayU's page.
4. **Payment result:** PayU returns the result. With Link and Pay, the customer's BNPL account is also linked for future payments.

<Callout icon="📘" theme="info">
  ### **Simpl First-Time Linking**

  On a customer's first Simpl payment, the customer links their account on Simpl's own page. After that, Simpl payments work like other lenders.
</Callout>

### Repeat Customer (Link and Pay)

1. **Eligibility check:** Your server confirms the customer is still eligible and linked.
2. **One-click payment:** The customer selects their linked BNPL account.
3. **Payment without OTP:** PayU debits the linked account directly.

<Callout icon="⚠️" theme="warn">
  ### **OTP Fallback**

  A repeat payment falls back to the OTP flow if the saved link has expired, is missing, or the transaction needs extra verification. Your integration must always be able to handle an OTP step.
</Callout>

***

## Supported Lenders

Common BNPL bank codes include:

| Lender        | `bankcode`                                   | Notes                                                       |
| ------------- | -------------------------------------------- | ----------------------------------------------------------- |
| LazyPay       | `LAZYPAY`                                    | Supports Link and Pay                                       |
| Simpl         | `SIMPL`                                      | First payment needs account linking on Simpl's page         |
| HDFC FlexiPay | `HDFCF15`, `HDFCF30`, `HDFCF60`, `HDFCF90`   | Needs the customer's credit card number in `ccnum`          |

For the full list, see [BNPL Codes](doc:bnpl-codes).

***

## Next Steps

<Cards columns="2">
  <Card title="How BNPL Works" href="doc:bnpl-workflow" icon="fa-diagram-project">
    The end-to-end flow, what PayU handles, and what your application handles.
  </Card>

  <Card title="PayU Hosted Checkout" href="doc:bnpl-payu-hosted-integration" icon="fa-window-maximize">
    Turn on BNPL on PayU's checkout page with minimal code.
  </Card>

  <Card title="Merchant Hosted Checkout" href="doc:bnpl-merchant-hosted-integration" icon="fa-code">
    Show BNPL on your own checkout page, with optional native OTP.
  </Card>

  <Card title="Link and Pay" href="doc:bnpl-link-and-pay-merchant-hosted" icon="fa-link">
    One-click repeat checkout for linked BNPL customers.
  </Card>
</Cards>
