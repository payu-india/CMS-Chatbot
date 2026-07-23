---
title: Native OTP Flow Integration
deprecated: false
hidden: false
icon: far fa-stopwatch-20
metadata:
  title: Integrate with Native OTP Flow for EMI
  description: ''
  robots: index
next:
  description: ''
---
Native OTP Flow is a method of capturing transaction OTPs that happens on the merchant or PayU Payment page, rather than on a bank’s page through multiple hops. This means that customers stay on the merchant or PayU website to complete the card authentication process, entering the OTP on the same page where they are making the purchase, rather than being redirected to a 3D-secure page. This reduces the number of steps in the checkout process, resulting in a faster and smoother experience for customers and a higher success rate for merchants. As a result, Native OTP Flow is preferred over OTP on a bank’s page.

This flow supports the latest native OTP generation flow (server-to-server) via Initiate Payment API, followed by the Submit OTP API, to initiate an S2S=4 transaction.

<Callout icon="👍" theme="okay">
  ### Before you begin:

  Register for a account with PayU before you start integration. Enable Native OTP Flow on the PayU Dashboard under checkout payment modes, or contact your PayU Key Account Manager to enable it. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard) and [Configure Checkout Settings](doc:checkout-payment-modes).
</Callout>

## Integration guides

The following sections describe how to integrate Native OTP Flow with PayU:

- [Collect Payments with Card – Native OTP Flow](doc:collect-payments-with-card-native-otp-flow)
- [Collect Payments with Debit Card EMI – Native OTP Flow](doc:collect-payments-with-debit-card-native-otp-flow)
- [Collect Payments with Cardless EMI – Native OTP Flow](doc:collect-payments-with-cardless-emi-native-otp-flow)

## Benefits

<Accordion title="Why integrate Native OTP Flow?" icon="fa-bolt">
  * **Increase Success Rates** — Native OTP flow improves Success Rates of card transactions by 3-5% depending upon the source of transactions.
  * **Less Redirection** — It improves the overall user experience since multiple redirections are removed. Also, the customer never leaves the merchant website, which helps in providing a seamless experience. It also reduces drop rates due to users' fluctuating internet speed issues.
  * **PayU supports all major banks** — 15+ banks including HDFC, AXIS, ICICI, SBI, KOTAK, RBL, etc. – on this flow for Cards, cardless, CC EMI, DC EMI's, and BNPLs.
</Accordion>

<Accordion title="Native OTP transaction flow" icon="fa-diagram-project">
  1. **Initiate payment** — Post card and transaction details to PayU using the Server-to-Server `_payment` API with `s2s=4`.
  2. **Display OTP page** — Render the OTP capture UI on your checkout using the `postUrl` or `acsTemplate` from the initiate response.
  3. **Submit OTP** — Call the Submit OTP API with the OTP entered by the customer.
  4. **Resend OTP (if needed)** — Use the Resend OTP API when the customer requests a new OTP or enters an invalid OTP.
  5. **Verify payment** — Reconcile the final transaction status using Verify Payment API or webhooks.

  For EMI flows, check customer eligibility with Get Checkout Details API before Step 1.
</Accordion>

<br />
