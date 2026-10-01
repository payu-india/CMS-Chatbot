---
title: PayU v2 DevGuide page-level change report
deprecated: false
hidden: true
metadata:
  robots: index
---
This report compares the supplied original archive with the remediated source tree. It lists every changed source file and summarizes the detected change categories. It does not claim API behaviour was validated.

## How to read this report

- **Modified lines** are approximate counts from a text diff.
- Categories are inferred from changed text and the remediation tracker.
- A page may still have pending API, authentication, endpoint, schema, or security-owner decisions.

## custom_blocks

### `custom_blocks/BillingDetails_object.md`

- **Change:** modified; approximately 1 lines removed and 1 lines added (66 → 66 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `custom_blocks/ChargebackEnvironment.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (9 → 8 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `custom_blocks/DynamicHashGeneration.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (122 → 120 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `custom_blocks/HashingRequestParameters.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (12 → 11 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `custom_blocks/HeaderAuthentication.md`

- **Change:** modified; approximately 6 lines removed and 9 lines added (52 → 55 lines).
- **Detected areas:** redaction/security, editorial, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Editorial wording or documentation artefacts were cleaned up.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `custom_blocks/PayoutEvents.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (20 → 19 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `custom_blocks/ProductionKeyAndSaltProcedure.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (11 → 10 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `custom_blocks/ReverseHashing.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (12 → 11 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `custom_blocks/TestKeyAndSaltProcedure.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (10 → 9 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `custom_blocks/V2_order_object.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (36 → 34 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `custom_blocks/V2_paymentCard.md`

- **Change:** modified; approximately 2 lines removed and 2 lines added (56 → 56 lines).
- **Detected areas:** redaction/security, code samples.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.

### `custom_blocks/V2_payment_envrionment.md`

- **Change:** modified; approximately 1 lines removed and 1 lines added (7 → 7 lines).
- **Detected areas:** endpoint.
- Endpoint formatting or a known malformed URL character was corrected; unresolved host/path conflicts remain pending.

### `custom_blocks/V2_payment_header_params.md`

- **Change:** modified; approximately 11 lines removed and 12 lines added (49 → 50 lines).
- **Detected areas:** redaction/security, editorial, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Editorial wording or documentation artefacts were cleaned up.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `custom_blocks/V2_payment_response_params.md`

- **Change:** modified; approximately 1 lines removed and 1 lines added (28 → 28 lines).
- **Detected areas:** editorial, code samples.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Editorial wording or documentation artefacts were cleaned up.

### `custom_blocks/WalletHeader.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (99 → 98 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

## custom_pages

### `custom_pages/how-to-choose-the-best-payment-gateway-integration-for-your-business.md`

- **Change:** modified; approximately 15 lines removed and 0 lines added (82 → 67 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

## docs

### `docs/Affordability/emi-api-integration/cardless-emi-s2s-integration.md`

- **Change:** modified; approximately 10 lines removed and 2 lines added (606 → 598 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/emi-api-integration/collect-payments-with-cardless-emi-using-merchant-hosted-checkout.md`

- **Change:** modified; approximately 10 lines removed and 5 lines added (555 → 550 lines).
- **Detected areas:** redaction/security, code samples, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `docs/Affordability/emi-api-integration/collect-payments-with-emi-using-credit-card.md`

- **Change:** modified; approximately 27 lines removed and 4 lines added (1096 → 1073 lines).
- **Detected areas:** code samples, fields/schema.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `docs/Affordability/emi-api-integration/collect-payments-with-emi-using-debit-card.md`

- **Change:** modified; approximately 10 lines removed and 5 lines added (566 → 561 lines).
- **Detected areas:** redaction/security, code samples, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `docs/Affordability/emi-api-integration/emi-codes-bckup.md`

- **Change:** modified; approximately 6 lines removed and 1 lines added (239 → 234 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/emi-api-integration/emi-codes-copy.md`

- **Change:** modified; approximately 6 lines removed and 1 lines added (239 → 234 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/emi-api-integration/emi-codes.md`

- **Change:** modified; approximately 6 lines removed and 1 lines added (239 → 234 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/emi-api-integration/index.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (81 → 77 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/emi-api-integration/native-otp-flow-integration/collect-payments-with-cardless-emi-native-otp-flow.md`

- **Change:** modified; approximately 5 lines removed and 1 lines added (124 → 120 lines).
- **Detected areas:** redaction/security.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.

### `docs/Affordability/emi-api-integration/native-otp-flow-integration/collect-payments-with-debit-card-native-otp-flow.md`

- **Change:** modified; approximately 5 lines removed and 1 lines added (60 → 56 lines).
- **Detected areas:** redaction/security.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.

### `docs/Affordability/emi-api-integration/native-otp-flow-integration/index.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (39 → 38 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/introduction-to-affordability/co-funded-offer.md`

- **Change:** modified; approximately 6 lines removed and 0 lines added (92 → 86 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/introduction-to-affordability/low-cost-emi-offer.md`

- **Change:** modified; approximately 5 lines removed and 0 lines added (104 → 99 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/introduction-to-affordability/offers-advanced-features.md`

- **Change:** modified; approximately 10 lines removed and 0 lines added (65 → 55 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/introduction-to-affordability/pre-discounted-offer.md`

- **Change:** modified; approximately 5 lines removed and 0 lines added (97 → 92 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/offers-integration/index.md`

- **Change:** modified; approximately 5 lines removed and 0 lines added (89 → 84 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/offers-integration/integrate-with-merchant-hosted-checkout-offers/collect-payments-with-sku-based-offer-using-merchant-hosted-checkout-offers-integration.md`

- **Change:** modified; approximately 14 lines removed and 0 lines added (466 → 452 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/offers-integration/integrate-with-merchant-hosted-checkout-offers/instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (254 → 252 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/offers-integration/payu-hosted-checkout-integration-with-offers.md`

- **Change:** modified; approximately 11 lines removed and 0 lines added (575 → 564 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/payu-bnpl-integration-introduction/bnpl-workflow-payu-hosted-checkout.md`

- **Change:** modified; approximately 10 lines removed and 0 lines added (88 → 78 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/payu-bnpl-integration-introduction/collect-payments-with-bnpl-merchant-hosted-checkout/general-flow-bnpl-integration-with-merchant-hosted.md`

- **Change:** modified; approximately 11 lines removed and 3 lines added (505 → 497 lines).
- **Detected areas:** code samples, fields/schema.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `docs/Affordability/payu-bnpl-integration-introduction/collect-payments-with-bnpl-merchant-hosted-checkout/native-otp-flow-bnpl-integration-with-merchant-hosted.md`

- **Change:** modified; approximately 14 lines removed and 1 lines added (728 → 715 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/payu-bnpl-integration-introduction/index.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (53 → 52 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Affordability/payu-bnpl-integration-introduction/link-and-pay/collect-payments-with-bnpl-using-link-and-pay.md`

- **Change:** modified; approximately 22 lines removed and 6 lines added (597 → 581 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `docs/Affordability/payu-bnpl-integration-introduction/link-and-pay/index.md`

- **Change:** modified; approximately 5 lines removed and 0 lines added (77 → 72 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Developer Tools/plugins-for-development-environment/index.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (44 → 40 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Developer Tools/plugins-for-development-environment/intellij-idea-plugin.md`

- **Change:** modified; approximately 16 lines removed and 0 lines added (142 → 126 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Developer Tools/plugins-for-development-environment/visual-studio-code-plugin.md`

- **Change:** modified; approximately 9 lines removed and 0 lines added (103 → 94 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Developer Tools/webhooks-copy/create-and-manage-webhooks-1/index.md`

- **Change:** modified; approximately 3 lines removed and 0 lines added (32 → 29 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Developer Tools/webhooks-copy/create-and-manage-webhooks.md`

- **Change:** modified; approximately 9 lines removed and 0 lines added (66 → 57 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Developer Tools/webhooks-copy/index.md`

- **Change:** modified; approximately 7 lines removed and 1 lines added (52 → 46 lines).
- **Detected areas:** redaction/security.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.

### `docs/Developer Tools/webhooks-copy/payouts-webhooks-1/index.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (25 → 23 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Developer Tools/webhooks-copy/payouts-webhooks-1/sample-payloads-payout-webhooks.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (27 → 26 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Developer Tools/webhooks-copy/subscription-webhooks/index.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (28 → 26 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Pre-Authorize payments/auth-and-capture-pre-authorize-credit-card-payments.md`

- **Change:** modified; approximately 6 lines removed and 0 lines added (60 → 54 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Pre-Authorize payments/merchant-hosted-integration-pre-authorize-payment.md`

- **Change:** modified; approximately 18 lines removed and 7 lines added (726 → 715 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Pre-Authorize payments/payu-hosted-integration-pre-authorize-payments.md`

- **Change:** modified; approximately 13 lines removed and 1 lines added (758 → 746 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Pre-Authorize payments/s2s-pre-authorize-payment.md`

- **Change:** modified; approximately 6 lines removed and 0 lines added (143 → 137 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Refunds/refund-apis.md`

- **Change:** modified; approximately 1 lines removed and 1 lines added (13 → 13 lines).
- **Detected areas:** editorial.
- Editorial wording or documentation artefacts were cleaned up.

### `docs/Refunds/v2-refunds-introduction.md`

- **Change:** modified; approximately 9 lines removed and 2 lines added (64 → 57 lines).
- **Detected areas:** editorial.
- Editorial wording or documentation artefacts were cleaned up.

### `docs/Third-party verification/introduction-to-payu-tpv.md`

- **Change:** modified; approximately 3 lines removed and 0 lines added (68 → 65 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/Third-party verification/seamless-integration-tpv/neftrtgs-integration-for-tpv.md`

- **Change:** modified; approximately 26 lines removed and 11 lines added (313 → 298 lines).
- **Detected areas:** redaction/security, code samples, authentication, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `docs/Third-party verification/seamless-integration-tpv/net-banking-integration-for-tpv.md`

- **Change:** modified; approximately 25 lines removed and 11 lines added (303 → 289 lines).
- **Detected areas:** redaction/security, code samples, authentication, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `docs/Third-party verification/seamless-integration-tpv/upi-integration-for-tpv.md`

- **Change:** modified; approximately 27 lines removed and 11 lines added (275 → 259 lines).
- **Detected areas:** redaction/security, code samples, authentication, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `docs/Third-party verification/tpv-non-seamless-integration.md`

- **Change:** modified; approximately 2 lines removed and 1 lines added (162 → 161 lines).
- **Detected areas:** redaction/security.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.

### `docs/cross-border payments/introduction-cross-border-payments-import/index.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (66 → 64 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/cross-border payments/steps-to-integrate-cross-border-payments-import/integrate-cross-border-payments-for-payubiz.md`

- **Change:** modified; approximately 7 lines removed and 2 lines added (532 → 527 lines).
- **Detected areas:** redaction/security.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.

### `docs/cross-border payments/upi-autopay-integration-cross-border-payments-import/integrate-import-with-upi-autopay-for-payubiz.md`

- **Change:** modified; approximately 6 lines removed and 2 lines added (478 → 474 lines).
- **Detected areas:** redaction/security.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.

### `docs/cross-border payments/upi-autopay-integration-cross-border-payments-import/integrate-mandate-registration-flow-with-upi-autopay.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (270 → 268 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/check-api-key-and-salt.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (34 → 32 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/choose-your-integration.md`

- **Change:** modified; approximately 9 lines removed and 0 lines added (119 → 110 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/choose-your-payment-gateway.md`

- **Change:** modified; approximately 9 lines removed and 0 lines added (154 → 145 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/complete-your-kyc/documents-checklist-for-account-activation.md`

- **Change:** modified; approximately 27 lines removed and 5 lines added (899 → 877 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/complete-your-kyc/index.md`

- **Change:** modified; approximately 9 lines removed and 0 lines added (180 → 171 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/introduction.md`

- **Change:** modified; approximately 22 lines removed and 16 lines added (370 → 364 lines).
- **Detected areas:** redaction/security, editorial, code samples, authentication, navigation/link.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Editorial wording or documentation artefacts were cleaned up.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Links or navigation-related text was adjusted only where safe; broad slug/navigation changes remain pending.

### `docs/getting started/payu-dashboard/banking-dashboard.md`

- **Change:** modified; approximately 8 lines removed and 0 lines added (162 → 154 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/payu-dashboard/beneficiary-dashboard.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (87 → 83 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/payu-dashboard/configure-user-settings/update-profile-before-onboarding-completion.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (68 → 66 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/payu-dashboard/configure-user-settings/update-profile-on-dashboard.md`

- **Change:** modified; approximately 3 lines removed and 0 lines added (93 → 90 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/payu-dashboard/faqs-for-dashboard.md`

- **Change:** modified; approximately 10 lines removed and 0 lines added (374 → 364 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/payu-dashboard/generate-merchant-key-and-salt-on-payu-dashboard.md`

- **Change:** modified; approximately 3 lines removed and 0 lines added (85 → 82 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/payu-dashboard/generate-merchant-key-and-salt-on-payubiz-dashboard.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (60 → 58 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/payu-dashboard/generate-test-merchant-key-and-salt.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (48 → 46 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/payu-dashboard/integrations-dashboard.md`

- **Change:** modified; approximately 5 lines removed and 0 lines added (76 → 71 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/payu-dashboard/sales-and-earnings-dashboard.md`

- **Change:** modified; approximately 3 lines removed and 0 lines added (91 → 88 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/payu-dashboard/settlements-dashboard/download-monthly-tdr-report.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (38 → 37 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/payu-dashboard/settlements-dashboard/priority-settlements.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (64 → 60 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/getting started/why-integrate-payu-v2-apis.md`

- **Change:** modified; approximately 7 lines removed and 4 lines added (333 → 330 lines).
- **Detected areas:** redaction/security, code samples.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.

### `docs/save cards/collect-payments-using-a-saved-card.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (77 → 73 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/save cards/introduction-save-cards/what-is-tokenization.md`

- **Change:** modified; approximately 5 lines removed and 0 lines added (70 → 65 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/save cards/introduction-save-cards/which-model-you-should-choose.md`

- **Change:** modified; approximately 10 lines removed and 0 lines added (82 → 72 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/save cards/push-tokenization.md`

- **Change:** modified; approximately 11 lines removed and 0 lines added (80 → 69 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/save cards/save-card-non-seamles-integration-with-vault-model-1.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (52 → 50 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/save cards/simple-rest-apis-for-vault-integration-model-3.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (49 → 47 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/save cards/zero-code-change-for-vault-integration-model-2.md`

- **Change:** modified; approximately 12 lines removed and 0 lines added (152 → 140 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/split Settlements/introduction-split-settlements/convenience-fee-handling.md`

- **Change:** modified; approximately 3 lines removed and 0 lines added (110 → 107 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/split Settlements/introduction-split-settlements/create-the-split.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (33 → 32 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/split Settlements/introduction-split-settlements/fetch-child-merchants-details-1.md`

- **Change:** modified; approximately 6 lines removed and 0 lines added (504 → 498 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/split Settlements/introduction-split-settlements/index.md`

- **Change:** modified; approximately 14 lines removed and 1 lines added (405 → 392 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `docs/split Settlements/split-settlments/aggregator-or-marketplace-settlement-solution.md`

- **Change:** modified; approximately 3 lines removed and 0 lines added (49 → 46 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/split Settlements/split-settlments/index.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (34 → 33 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/subscription/customer-experience-and-workflow-recurring-payments/index.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (77 → 76 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/subscription/customer-experience-and-workflow-recurring-payments/net-banking-experience.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (113 → 109 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/subscription/customer-experience-and-workflow-recurring-payments/one-time-mandate-experience.md`

- **Change:** modified; approximately 6 lines removed and 0 lines added (149 → 143 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/subscription/customer-experience-and-workflow-recurring-payments/recurring-payments-experience-for-cards.md`

- **Change:** modified; approximately 6 lines removed and 0 lines added (175 → 169 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/subscription/customer-experience-and-workflow-recurring-payments/upi-recurring-payment-experience-for-upi.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (80 → 76 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/subscription/introduction-recurring-payments-integration.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (54 → 53 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/subscription/subscription-dashboard/create-a-subscription-payment-link-using-dashboard.md`

- **Change:** modified; approximately 10 lines removed and 5 lines added (119 → 114 lines).
- **Detected areas:** editorial.
- Editorial wording or documentation artefacts were cleaned up.

### `docs/subscription/subscription-dashboard/upload-recurring-transactions-in-bulk.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (84 → 82 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/subscription/subscription-dashboard/upload-registration-transactions-in-bulk.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (510 → 508 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/subscription/using-api-integration-recurring-payments.md`

- **Change:** modified; approximately 3 lines removed and 0 lines added (52 → 49 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/v2 web integration/v2-non-seamless-integration/enforce-pay-method-or-remove-category.md`

- **Change:** modified; approximately 6 lines removed and 0 lines added (121 → 115 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/v2 web integration/v2-non-seamless-integration/index.md`

- **Change:** modified; approximately 3 lines removed and 0 lines added (64 → 61 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/v2 web integration/v2-non-seamless-integration/v2-non-seamless-api-integration-steps.md`

- **Change:** modified; approximately 36 lines removed and 11 lines added (291 → 266 lines).
- **Detected areas:** redaction/security, code samples, authentication, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `docs/v2 web integration/v2-seamless-integration/index.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (78 → 74 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `docs/v2 web integration/v2-seamless-integration/v2-bnpl-merchant-hosted-integration.md`

- **Change:** modified; approximately 16 lines removed and 3 lines added (289 → 276 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `docs/v2 web integration/v2-seamless-integration/v2-cards-merchant-hosted-integration.md`

- **Change:** modified; approximately 41 lines removed and 16 lines added (483 → 458 lines).
- **Detected areas:** redaction/security, code samples, authentication, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `docs/v2 web integration/v2-seamless-integration/v2-emi-merchant-hosted-integration.md`

- **Change:** modified; approximately 17 lines removed and 4 lines added (258 → 245 lines).
- **Detected areas:** redaction/security, code samples, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `docs/v2 web integration/v2-seamless-integration/v2-net-banking-integration.md`

- **Change:** modified; approximately 23 lines removed and 7 lines added (313 → 297 lines).
- **Detected areas:** redaction/security, code samples, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `docs/v2 web integration/v2-seamless-integration/v2-seamless-workflows-integration/v2-s2s-classic-integration.md`

- **Change:** modified; approximately 26 lines removed and 9 lines added (435 → 418 lines).
- **Detected areas:** redaction/security, code samples, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `docs/v2 web integration/v2-seamless-integration/v2-seamless-workflows-integration/v2-s2s-direct-authentication-integration.md`

- **Change:** modified; approximately 24 lines removed and 6 lines added (372 → 354 lines).
- **Detected areas:** redaction/security, code samples, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `docs/v2 web integration/v2-seamless-integration/v2-seamless-workflows-integration/v2-s2s-upi-integration.md`

- **Change:** modified; approximately 51 lines removed and 17 lines added (605 → 571 lines).
- **Detected areas:** redaction/security, code samples, authentication, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `docs/v2 web integration/v2-seamless-integration/v2-upi-merchant-hosted-integration.md`

- **Change:** modified; approximately 16 lines removed and 3 lines added (262 → 249 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `docs/v2 web integration/v2-seamless-integration/v2-wallets-merchant-hostede-integration.md`

- **Change:** modified; approximately 13 lines removed and 3 lines added (220 → 210 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

## recipes

### `recipes/_payment-request-java-code-walkthrough.md`

- **Change:** modified; approximately 7 lines removed and 0 lines added (82 → 75 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `recipes/_payment-request-php-code-walkthrough-1.md`

- **Change:** modified; approximately 8 lines removed and 0 lines added (91 → 83 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `recipes/_payment-request-python-code-walkthrough.md`

- **Change:** modified; approximately 14 lines removed and 0 lines added (62 → 48 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `recipes/android-checkoutpro-integration.md`

- **Change:** modified; approximately 8 lines removed and 0 lines added (155 → 147 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `recipes/cross-border-payments-import-plugin-integration.md`

- **Change:** modified; approximately 12 lines removed and 1 lines added (132 → 121 lines).
- **Detected areas:** redaction/security.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.

### `recipes/curl-walkthrough.md`

- **Change:** modified; approximately 5 lines removed and 1 lines added (62 → 58 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `recipes/encoding-header-with-keysalt.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (65 → 61 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `recipes/parse-the-_payment-json-response-using-java.md`

- **Change:** modified; approximately 12 lines removed and 0 lines added (129 → 117 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `recipes/parse-the-json-response-from-verify-payment-api.md`

- **Change:** modified; approximately 5 lines removed and 0 lines added (166 → 161 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `recipes/parse-the-verify-payment-api-response.md`

- **Change:** modified; approximately 9 lines removed and 0 lines added (174 → 165 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `recipes/payu-hosted-checkout-curl-request-walkthrough.md`

- **Change:** modified; approximately 3 lines removed and 0 lines added (111 → 108 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `recipes/submitting-payment-request-on-your-website.md`

- **Change:** modified; approximately 11 lines removed and 0 lines added (233 → 222 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

## reference

### `reference/Collect Payment/addl_info-payment-apis.md`

- **Change:** modified; approximately 20 lines removed and 2 lines added (947 → 929 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Collect Payment/cards-v2-payment-api-copy.md`

- **Change:** modified; approximately 15 lines removed and 5 lines added (383 → 373 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Collect Payment/collect-payment-api-payu-hosted-v2-_payment.md`

- **Change:** modified; approximately 22 lines removed and 9 lines added (165 → 152 lines).
- **Detected areas:** redaction/security, code samples, authentication, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `reference/Collect Payment/v2_payment_seamless_integration/_payment-v2-merchant-hosted-cards.md`

- **Change:** modified; approximately 27 lines removed and 13 lines added (241 → 227 lines).
- **Detected areas:** redaction/security, editorial, code samples, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Editorial wording or documentation artefacts were cleaned up.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `reference/Collect Payment/v2_payment_seamless_integration/_payment_v2_merchant_hosted_netbanking.md`

- **Change:** modified; approximately 23 lines removed and 9 lines added (297 → 283 lines).
- **Detected areas:** redaction/security, authentication, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `reference/Collect Payment/v2_payment_seamless_integration/_payment_v2_merchant_hosted_upi.md`

- **Change:** modified; approximately 15 lines removed and 3 lines added (223 → 211 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Collect Payment/v2_payment_seamless_integration/bnpl-v2_payment-merchant-hosted.md`

- **Change:** modified; approximately 14 lines removed and 3 lines added (219 → 208 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Collect Payment/v2_payment_seamless_integration/collect-payments-with-emi-v2_payment.md`

- **Change:** modified; approximately 16 lines removed and 4 lines added (241 → 229 lines).
- **Detected areas:** redaction/security, code samples, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Collect Payment/v2_payment_seamless_integration/collect_v2_payment_wallet.md`

- **Change:** modified; approximately 15 lines removed and 4 lines added (224 → 213 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Collect Payment/v2_payment_seamless_integration/v2_seamless_payment_flows/cards-classic-integration.md`

- **Change:** modified; approximately 17 lines removed and 5 lines added (308 → 296 lines).
- **Detected areas:** redaction/security, code samples, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Collect Payment/v2_payment_seamless_integration/v2_seamless_payment_flows/cards-decoupled-flow-s2s-v2-_payment.md`

- **Change:** modified; approximately 21 lines removed and 6 lines added (305 → 290 lines).
- **Detected areas:** redaction/security, code samples, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Collect Payment/v2_payment_seamless_integration/v2_seamless_payment_flows/cards-direct-authorization-flow-s2s-v2-_payment.md`

- **Change:** modified; approximately 20 lines removed and 6 lines added (346 → 332 lines).
- **Detected areas:** redaction/security, code samples, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Collect Payment/v2_payment_seamless_integration/v2_seamless_payment_flows/upi-s2s-_payment-v2.md`

- **Change:** modified; approximately 35 lines removed and 13 lines added (255 → 233 lines).
- **Detected areas:** redaction/security, authentication, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `reference/Downtime/fetch-merchant-downtime-information.md`

- **Change:** modified; approximately 10 lines removed and 0 lines added (222 → 212 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Downtime/fetch-platform-downtime-information.md`

- **Change:** modified; approximately 9 lines removed and 0 lines added (196 → 187 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Downtime/fetch-schedule-maintenance-activities-info.md`

- **Change:** modified; approximately 10 lines removed and 0 lines added (228 → 218 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/GENERAL/bin-apis/eligible-bin-for-emi-api-v2.md`

- **Change:** modified; approximately 17 lines removed and 3 lines added (620 → 606 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/GENERAL/bin-apis/emi-calculator-api.md`

- **Change:** modified; approximately 9 lines removed and 1 lines added (249 → 241 lines).
- **Detected areas:** redaction/security.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.

### `reference/GENERAL/bin-apis/v2-check-is-domestic-card-api.md`

- **Change:** modified; approximately 12 lines removed and 5 lines added (114 → 107 lines).
- **Detected areas:** editorial, authentication, navigation/link.
- Editorial wording or documentation artefacts were cleaned up.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Links or navigation-related text was adjusted only where safe; broad slug/navigation changes remain pending.

### `reference/GENERAL/bin-apis/v2-get-bin-info-api.md`

- **Change:** modified; approximately 6 lines removed and 0 lines added (228 → 222 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/GENERAL/bin-apis/v2-issuing-bank-status-api.md`

- **Change:** modified; approximately 7 lines removed and 0 lines added (219 → 212 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/GENERAL/bin-apis/v2_s2s-eligible-bins-api.md`

- **Change:** modified; approximately 5 lines removed and 0 lines added (73 → 68 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/GENERAL/refund-apis/index.md`

- **Change:** modified; approximately 1 lines removed and 1 lines added (11 → 11 lines).
- **Detected areas:** editorial.
- Editorial wording or documentation artefacts were cleaned up.

### `reference/GENERAL/refund-apis/v2-refund-status-api.md`

- **Change:** modified; approximately 14 lines removed and 7 lines added (265 → 258 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/GENERAL/refund-apis/v2-refund-transaction-api.md`

- **Change:** modified; approximately 24 lines removed and 13 lines added (320 → 309 lines).
- **Detected areas:** redaction/security, editorial, authentication, endpoint.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Editorial wording or documentation artefacts were cleaned up.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Endpoint formatting or a known malformed URL character was corrected; unresolved host/path conflicts remain pending.

### `reference/GENERAL/v2-check-transaction-apis/v2_verify_payment_api.md`

- **Change:** modified; approximately 17 lines removed and 9 lines added (188 → 180 lines).
- **Detected areas:** redaction/security, editorial, authentication, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Editorial wording or documentation artefacts were cleaned up.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `reference/GENERAL/v2-generate-upi-intent-api.md`

- **Change:** modified; approximately 5 lines removed and 0 lines added (87 → 82 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/GENERAL/v2-get-checkout-details.md`

- **Change:** modified; approximately 9 lines removed and 0 lines added (206 → 197 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/GENERAL/v2-get-transaction-details-api.md`

- **Change:** modified; approximately 13 lines removed and 4 lines added (696 → 687 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/GENERAL/v2-validate-vpa-api.md`

- **Change:** modified; approximately 7 lines removed and 1 lines added (161 → 155 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/IN-PERSON Payment/generate-upi-qr.md`

- **Change:** modified; approximately 15 lines removed and 2 lines added (230 → 217 lines).
- **Detected areas:** redaction/security.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.

### `reference/IN-PERSON Payment/v2-dbqr-upi-api.md`

- **Change:** modified; approximately 14 lines removed and 1 lines added (263 → 250 lines).
- **Detected areas:** redaction/security.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.

### `reference/PreAuthorize Payment/payment-api-preauth-seamless.md`

- **Change:** modified; approximately 13 lines removed and 4 lines added (238 → 229 lines).
- **Detected areas:** redaction/security, authentication, endpoint.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Endpoint formatting or a known malformed URL character was corrected; unresolved host/path conflicts remain pending.

### `reference/PreAuthorize Payment/v2-capture-transaction-api.md`

- **Change:** modified; approximately 7 lines removed and 1 lines added (70 → 64 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/PreAuthorize Payment/v2-payment-api-preauth-non-seamless.md`

- **Change:** modified; approximately 22 lines removed and 9 lines added (511 → 498 lines).
- **Detected areas:** redaction/security, authentication, endpoint.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Endpoint formatting or a known malformed URL character was corrected; unresolved host/path conflicts remain pending.

### `reference/Save Cards/additional-info-for-model3-parameters.md`

- **Change:** modified; approximately 13 lines removed and 1 lines added (787 → 775 lines).
- **Detected areas:** editorial.
- Editorial wording or documentation artefacts were cleaned up.

### `reference/Save Cards/collect-payments-save-card/complete-card-details-payment.md`

- **Change:** modified; approximately 16 lines removed and 6 lines added (399 → 389 lines).
- **Detected areas:** redaction/security, code samples, authentication, endpoint.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Endpoint formatting or a known malformed URL character was corrected; unresolved host/path conflicts remain pending.

### `reference/Save Cards/collect-payments-save-card/index.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (85 → 81 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Save Cards/collect-payments-save-card/using-card-a-decoupled-flow-with-network-token-or-other-partner-tokenization.md`

- **Change:** modified; approximately 3 lines removed and 1 lines added (383 → 381 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Save Cards/collect-payments-save-card/using-card-on-a-decoupled-flow-with-payu-tokenization.md`

- **Change:** modified; approximately 3 lines removed and 1 lines added (455 → 453 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Save Cards/collect-payments-save-card/using-card-tokenized-with-payu.md`

- **Change:** modified; approximately 4 lines removed and 1 lines added (460 → 457 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Save Cards/collect-payments-save-card/using-issuer-tokens.md`

- **Change:** modified; approximately 3 lines removed and 1 lines added (500 → 498 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Save Cards/collect-payments-save-card/using-network-tokens.md`

- **Change:** modified; approximately 20 lines removed and 7 lines added (359 → 346 lines).
- **Detected areas:** redaction/security, code samples, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Save Cards/collect-payments-save-card/zero-code-change-payment.md`

- **Change:** modified; approximately 19 lines removed and 2 lines added (335 → 318 lines).
- **Detected areas:** redaction/security.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.

### `reference/Save Cards/model-2-zero-code-change-for-vault-integration/process-transaction-with-a-saved-card.md`

- **Change:** modified; approximately 20 lines removed and 4 lines added (360 → 344 lines).
- **Detected areas:** redaction/security, code samples.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.

### `reference/Save Cards/model-2-zero-code-change-for-vault-integration/v2_get_user_cards_api.md`

- **Change:** modified; approximately 9 lines removed and 0 lines added (270 → 261 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Save Cards/model-3-simple-rest-apis/v2-delete-payment-instrument.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (129 → 125 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Save Cards/model-3-simple-rest-apis/v2-get-payment-details-api.md`

- **Change:** modified; approximately 11 lines removed and 2 lines added (400 → 391 lines).
- **Detected areas:** redaction/security, editorial, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Editorial wording or documentation artefacts were cleaned up.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Save Cards/model-3-simple-rest-apis/v2-get-payment-instrument-api.md`

- **Change:** modified; approximately 13 lines removed and 1 lines added (187 → 175 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Save Cards/model-3-simple-rest-apis/v2_delete-card-api.md`

- **Change:** modified; approximately 9 lines removed and 1 lines added (103 → 95 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Save Cards/model-3-simple-rest-apis/v2_save_card_api.md`

- **Change:** modified; approximately 19 lines removed and 2 lines added (228 → 211 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Save Cards/push-tokenization-1/account-discovery-api.md`

- **Change:** modified; approximately 3 lines removed and 0 lines added (88 → 85 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Subscription/api-commands-to-manage-upi-recurring-transaction/cancel-the-recurring-payment-for-upi.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (113 → 109 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Subscription/api-commands-to-manage-upi-recurring-transaction/get-mandate-status-api-for-upi-only.md`

- **Change:** modified; approximately 3 lines removed and 0 lines added (134 → 131 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Subscription/api-commands-to-manage-upi-recurring-transaction/modify-the-recurring-payment-for-upi.md`

- **Change:** modified; approximately 6 lines removed and 0 lines added (285 → 279 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Subscription/api-commands-to-manage-upi-recurring-transaction/validate_vpa_api-old.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (232 → 231 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Subscription/api-commands-to-manage-upi-recurring-transaction/validate_vpa_api.md`

- **Change:** modified; approximately 1 lines removed and 0 lines added (265 → 264 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Subscription/manage-recurring-payment-for-cards/cancel-the-recurring-payment-for-cards.md`

- **Change:** modified; approximately 9 lines removed and 3 lines added (896 → 890 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Subscription/manage-recurring-payment-for-cards/check-mandate-status-api.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (163 → 159 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Subscription/manage-recurring-payment-for-cards/modify-the-recurring-payments-for-a-card.md`

- **Change:** modified; approximately 9 lines removed and 3 lines added (774 → 768 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Subscription/manage-recurring-payments-for-net-banking/cancel-the-recurring-payment-for-net-banking.md`

- **Change:** modified; approximately 8 lines removed and 0 lines added (358 → 350 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Subscription/manage-recurring-payments-for-net-banking/net_banking_mandate_status_api.md`

- **Change:** modified; approximately 6 lines removed and 0 lines added (157 → 151 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Subscription/si-parameter-json-details.md`

- **Change:** modified; approximately 2 lines removed and 0 lines added (430 → 428 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/Subscription/v2-payment-consent-transaction-seamless/v2-credit-card-recurring-payment-consent-transaction.md`

- **Change:** modified; approximately 18 lines removed and 3 lines added (442 → 427 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Subscription/v2-payment-consent-transaction-seamless/v2-netbanking-recurring-payment-consent-transaction.md`

- **Change:** modified; approximately 20 lines removed and 6 lines added (515 → 501 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Subscription/v2-payment-consent-transaction-seamless/v2-upi-recurring-payment-consent-transaction.md`

- **Change:** modified; approximately 14 lines removed and 4 lines added (303 → 293 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Subscription/v2-payment-consent-transaction-with-non-seamless-checkout.md`

- **Change:** modified; approximately 12 lines removed and 3 lines added (265 → 256 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Third-Party Verification/seamless-integration-tpv/v2_payment_tpv_merchant_hosted_v2_integration-1.md`

- **Change:** modified; approximately 4 lines removed and 4 lines added (282 → 282 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Third-Party Verification/seamless-integration-tpv/v2_payment_tpv_merchant_hosted_v2_integration.md`

- **Change:** modified; approximately 16 lines removed and 5 lines added (295 → 284 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/Third-Party Verification/v2_tpv_collect_payment_api_non_seamless.md`

- **Change:** modified; approximately 22 lines removed and 8 lines added (229 → 215 lines).
- **Detected areas:** redaction/security, authentication, fields/schema.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Field/sample cleanup was limited; conflicting names, types, and requiredness remain pending API-owner confirmation.

### `reference/introduction/introduction-api-reference.md`

- **Change:** modified; approximately 9 lines removed and 0 lines added (91 → 82 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/introduction/v2_authentication_with_payu_apis.md`

- **Change:** modified; approximately 6 lines removed and 3 lines added (83 → 80 lines).
- **Detected areas:** redaction/security.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.

### `reference/split settlements/v2-refund-status-for-split-settlements-api.md`

- **Change:** modified; approximately 9 lines removed and 1 lines added (213 → 205 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/split settlements/v2-split-during-transaction-using-_payment/absolute-split-during-transaction-v2_payment.md`

- **Change:** modified; approximately 20 lines removed and 3 lines added (448 → 431 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/split settlements/v2-split-during-transaction-using-_payment/index.md`

- **Change:** modified; approximately 4 lines removed and 0 lines added (151 → 147 lines).
- **Detected areas:** content cleanup.
- A conservative documentation cleanup was applied; see the tracker for the specific audit item and dependency.

### `reference/split settlements/v2-split-during-transaction-using-_payment/split-by-percentage-during-transaction-v2_payment.md`

- **Change:** modified; approximately 19 lines removed and 3 lines added (467 → 451 lines).
- **Detected areas:** redaction/security, authentication.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.

### `reference/storecard-6.json`

- **Change:** modified; approximately 1 lines removed and 1 lines added (2 → 2 lines).
- **Detected areas:** redaction/security, code samples, authentication, endpoint.
- Sensitive or credential-like sample values were replaced with placeholders or redaction markers where covered by the audit.
- Sample syntax, code-fence labels, or illustrative values were adjusted where the change was safe without selecting API behaviour.
- Authentication-related text was cleaned or flagged as unresolved; no conflicting scheme was selected as authoritative.
- Endpoint formatting or a known malformed URL character was corrected; unresolved host/path conflicts remain pending.

## Important limitation

The report describes documentation changes, not API certification. Authentication, endpoints, request fields, response contracts, credential ownership, and CI/schema controls remain pending where the audit identified contradictions or required external confirmation.
