---
title: Integrate Merchant Hosted Checkout
deprecated: false
hidden: false
metadata:
  title: Integrate Merchant Hosted Checkout - Cross Border Transaction under LRS
  keywords:
    - Integrate Merchant Hosted Checkout for Cross Border Transaction under LRS
    - Integrate Merchant Hosted Checkout for CB LRS
  robots: index
---
PayU’s **\_payment** API supports LRS implementation using the following parameters mandatorily in an S2S transaction:

- lrs_service_type
- lrs_mandatory_limit_declaration
- lrs_tnc
- tcs_amount
- lrs_tcs_declaration_under_limit
- buyer_type_business (optional)

For detailed steps to integrate in each payment mode for LRS, refer to the following sections:

- [NetBanking Integration for CB LRS](https://docs.payu.in/docs/netbanking-integration-for-cb-lrs)
- [Cards Integration for CB LRS](https://docs.payu.in/docs/cards-integration-for-cb-lrs)
- [UPI Integration for CB LRS](https://docs.payu.in/docs/upi-integration-for-cb-lrs)
