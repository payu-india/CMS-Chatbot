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
   * `lrs_service_type`
   * `lrs_mandatory_limit_declaration`
   * `lrs_tnc`
   * `lrs_tcs_declaration_under_limit` (optional)
3. Merchant initiates the API call to PayU with these parameters.
4. Customer is redirected to the PayU Hosted Checkout page where they begin the payment process.
5. Customer provides the LRS details and does the declaration:

   * Fills their personal details (name, PAN, DOB, etc.)
   * Selects the **Individual Buyer** or **Buying for Business**.
   * Selects the **LRS Declaration** check box (at the bottom of the page) to acknowledge the LRS declaration. This check box label from the `lrs_mandatory_limit_declaration` or` lrs_tnc` parameter value.

   <Image align="center" src="https://files.readme.io/df74b10d4fb401c9658c26ff593905ee625cc2bde4720d127293d8786ec9a74c-cb-lrs-payu-hosted-amt-declaration.png" />
6. Customer provides the tax details and tax limit declaration for LRS:

   * Shows TCS (Tax Collected at Source) options
   * Selects the **Tax Declaration** check box at the bottom of the page to acknowledge the LRS tax declaration. This check box label is from the `lrs_tcs_declaration_under_limit` parameter value.

   <Image align="center" src="https://files.readme.io/db14893cec45b3b796b2a6932703001c95b2caec1a63f4889485a8553bc79e8c-cb-lrs-payu-hosted-tax-declaration.png" />
7. The rest of workflow involves the collecting payment details. For more information, refer to[ PayU Hosted Checkout > Customer Journey](doc:prebuilt-checkout-payu-hosted#customer-journey).