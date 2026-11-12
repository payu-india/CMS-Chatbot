---
api:
  file: payu-hosted-checkout_v2026-11.yaml
  operationId: CollectPayment-PayUHostedCheckout
hidden: true
link:
  new_tab: false
metadata:
  description: >-
    Streamline your payment process with PayU’s Hosted Checkout API. Utilize our
    simulator to test and understand payment collection seamlessly. Access
    comprehensive API references for a smooth integration
  keywords:
    - PayU Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - Pre-built Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for PayU Hosted Checkout
    - _payment API for PayU Hosted Checkout
    - _payment API simulation for Pre-built Checkout
    - _payment API simulation for PayU Hosted Checkout
  robots: index
---
Submit a payment initiation request to PayU's Hosted Checkout. On receiving the request, PayU validates the hash and redirects the customer to the PayU payment page where they select their payment method and complete authentication. After payment, PayU POSTs the transaction result to the merchant's `surl` or `furl`.
