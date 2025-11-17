---
title: Native OTP Flow Integration
deprecated: false
hidden: false
metadata:
  title: Integrate with Native OTP Flow for EMI
  description: ''
  robots: index
next:
  description: ''
---
Native OTP Flow is a method of capturing transaction OTPs that happens on the merchant or PayU Payment page, rather than on a bank’s page through multiple hops. This means that customers stay on the merchant or PayU website to complete the card authentication process, entering the OTP on the same page where they are making the purchase, rather than being redirected to a 3D-secure page. This reduces the number of steps in the checkout process, resulting in a faster and smoother experience for customers and a higher success rate for merchants. As a result, Native OTP Flow is preferred over OTP on a bank’s page.

<Callout icon="📘" theme="info">
  **Note**: If you don’t have EMI enabled, try requesting using Dashboard. For more information, refer to [Configure Checkout Settings](doc:checkout-payment-modes). If you could not request through Dashboard, contact your PayU Key Account Manager or PayU Support.
</Callout>

## Benefits

What are the advantages and why should merchants integrate this flow with PayU?

* **Increase Success Rates** — Native OTP flow improves Success Rates of card transactions by 3-5% depending upon the source of transactions.
* **Less Redirection** — It improves the overall user experience since multiple redirections are removed. Also, the customer never leaves the merchant website, which helps in providing a seamless experience. It also reduces drop rates due to users’ fluctuating internet speed issues.
* **PayU supports all major banks** — 15+ banks including HDFC, AXIS, ICICI, SBI, KOTAK, RBL, etc. – on this flow for Cards, cardless, CC EMI, DC EMI’s, and BNPLs.

This flow supports the latest native OTP generation flow (server-to-server) via Initiate Payment API, followed by the Submit OTP API, to initiate an S2S=4 transaction.

PayU supports the following integrations:

* [Cards](https://docs.payu.in/docs/collect-payments-with-card-native-otp-flow)
* [Debit Card EMI](https://docs.payu.in/docs/collect-payments-with-debit-card-native-otp-flow)
* [Cardless EMI](https://docs.payu.in/docs/collect-payments-with-cardless-emi-native-otp-flow)