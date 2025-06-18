---
title: Customer Journey - PayU Hosted Checkout with LRS Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
This section outlines the customer journey for Cross Border Liberalised Remittance Scheme (LRS) transactions using PayU Hosted Checkout (non-seamless integration). The journey incorporates the mandatory LRS declarations that customers must acknowledge before completing their payment.

The typical customer journey for PayU Hosted Checkout with LRS involves:

1. Customer selects products/services on the merchant website and proceeds to checkout
2. Merchant prepares the payment request including the LRS parameters:
   * `lrs_mandatory_limit_declaration`
   * `lrs_tnc`
   * `lrs_tcs_declaration_under_limit` (optional)
3. Merchant initiates the API call to PayU with these parameters.
4. Customer is redirected to the PayU Hosted Checkout page where they begin the payment process.
5. Customer provides the LRS details and does the declaration:
   * Fills their personal details (name, PAN, DOB, etc.)
   * Selects the **Individual Buyer** or **Buying for Business**.
   * Selects the **LRS Declaration Checkbox** (at the bottom of the page) to acknowledge the LRS declaration. This check box label from the `lrs_mandatory_limit_declaration` or` lrs_tnc` parameter value.
6. Customer provides the tax details and tax limit declaration for LRS:
   * Shows TCS (Tax Collected at Source) options
   * Selects **Tax Declaration Text** at the bottom of the page to acknowledge the LRS tax declaration. This check box label is from the `lrs_tcs_declaration_under_limit` parameter value.