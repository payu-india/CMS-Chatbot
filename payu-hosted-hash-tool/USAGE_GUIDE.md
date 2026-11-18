# PayU Hash Generator - Comprehensive Usage Guide (CLI + Web)

This document explains how to use the hash generator in both:

- **Web UI** (`index.html`)
- **CLI (Node package workflow)**

It also explains **when to use each hash logic**, required fields, and links to relevant docs in this repository.

---

## 1) What this tool is for

`payu-hosted-hash-tool/index.html` is a unified PayU hash utility with a product/flow-wise dropdown.

It supports hash patterns found across this repo for:

- Collect Payments (Hosted / Merchant Hosted / S2S)
- Split settlements
- SI/Subscription / TPV
- Offers / v19 / PACB cross-border
- Partner integrations
- Decoupled callback verification
- MCP lookup signature
- Zion subscription signatures

---

## 2) Web usage (fastest for humans)

### Option A - Open directly

1. Open `payu-hosted-hash-tool/index.html` in a browser.
2. Select a logic from **Hash logic** dropdown.
3. Fill fields shown for that logic.
4. Click **Generate hash**.
5. Use **Copy** buttons to copy hash or plain concatenated string.

### Option B - Serve locally (recommended)

```bash
cd /path/to/repo/payu-hosted-hash-tool
python3 -m http.server 8080
```

Open: `http://localhost:8080`

> Why this is better: avoids file:// browser quirks and keeps behavior closer to production/static hosting.

---

## 3) CLI usage

If your npm package is already published, users can run via `npx`.

## 3.1 For consumers (others using your package)

### Run without install

```bash
npx <your-package-name> --help
```

### Install in a project

```bash
npm install <your-package-name>
npx payu-hash --help
```

## 3.2 For maintainers (you)

From package folder:

```bash
cd /path/to/payu-hosted-hash-tool
npm version patch
npm publish --access public
```

If publish fails due to auth:

```bash
npm logout
npm login --registry=https://registry.npmjs.org/
npm whoami
```

---

## 4) Logic selection guide (which mode to use)

Below are mode IDs in the tool with intent and formula summaries.

### A. Standard payment request modes

1. **`forward-hosted-standard`**  
   Use for regular `_payment` flows in hosted/merchant/S2S.
   - Formula: `key|txnid|amount|productinfo|firstname|email|udf1|...|udf5||||||SALT`

2. **`forward-v19`**  
   Use when `_payment` has `api_version=19`.
   - Includes `udf1..udf10`, `user_token`, `offer_key`, `offer_auto_apply`, `cart_details`, `extra_charges`, `phone`

3. **`forward-offers-v10`**  
   Offer integration pattern with `offer_key` and `offer_auto_apply`.
   - Formula: `...|udf10|offer_key|offer_auto_apply|SALT`

### B. Split and pricing variants

4. **`forward-split-request`**  
   For split settlement during transaction.
   - Appends `|splitRequest`

5. **`forward-subvention`**  
   For subvention amount transactions.
   - Appends `|SubventionAmount`

### C. SI / TPV / recurring variants

6. **`forward-si-details`**  
   SI hash with `si_details`

7. **`forward-si-free-trial`**  
   SI hash variant with `free_trial`

8. **`forward-beneficiary-tpv`**  
   TPV hash with `beneficiarydetail`

9. **`forward-si-beneficiary-ios`**  
   iOS naming variant with `siDetail` and `beneficiaryDetail`

### D. Mutual funds variants

10. **`forward-mutual-funds-basic`**  
    Includes `beneficiarydetail` and `products`

11. **`forward-mutual-funds-si`**  
    Includes `beneficiarydetail`, `si_details`, and `products`

### E. Cross-border PACB variants

12. **`forward-pacb-additional`**  
    Includes `additional_charges` and `buyer_type_business`

13. **`forward-pacb-si-udfparams`**  
    Includes `si_details`, `udf_params`, `buyer_type_business`

14. **`forward-pacb-v7-additional`**  
    Legacy chain with SI + additional + buyer type

15. **`forward-pacb-v7-udfparams`**  
    Legacy chain with SI + udf_params + buyer type

### F. Reverse hash verification modes

16. **`reverse-standard`**  
    Standard reverse hash (`SALT|status...|key`)

17. **`reverse-additional`**  
    Reverse hash with `additional_charges`

18. **`reverse-split`**  
    Reverse hash with `splitInfo`

19. **`reverse-split-additional`**  
    Reverse hash with both split and additional charges

20. **`reverse-si-details`**  
    Reverse hash variant with `si_details`

21. **`reverse-beneficiary`**  
    Reverse hash variant with `beneficiarydetail`

### G. Command-style API hashes

22. **`api-command-var1`**  
    Generic API pattern: `sha512(key|command|var1|salt)`  
    Used in validateVPA / verify_payment / refund-related command calls.

23. **`api-mihpayid-admin-date`**  
    Pattern: `sha512(key|mihpayid|admin|date)`

### H. Partner integration hashes

24. **`partner-forward-hosted`**  
    Partner forward hash with `merchant_id ... CLIENT_SECRET`

25. **`partner-verify-payment`**  
    `sha512(merchant_id|command|txnid|client_secret)`

26. **`partner-refund-status`**  
    `sha512(merchant_id|payu_id|client_secret)`

27. **`partner-refund-transaction`**  
    `sha512(merchant_id|refund_id|amount|client_secret)`

### I. Other product signatures

28. **`callback-decoupled`**  
    Decoupled callback verification:
    `authenticationStatus|bankData|rawBankData|referenceId|salt`

29. **`mcp-lookup-v2`**  
    MCP Lookup V2 signature:
    `key|baseAmount.value|baseAmount.currency|ccNum|merchantOrderId|productType|salt`

30. **`zion-create-subscription`**  
    Zion create subscription signature

31. **`zion-manage-subscription`**  
    Zion update/cancel/list signature

32. **`zion-create-invoice`**  
    Zion create invoice signature

33. **`subscriptions-webhook`**  
    Subscription webhook authenticity hash

---

## 5) Validation behavior in the tool

- Required fields are validated per selected mode.
- Email format is validated for email fields.
- Decimal fields are validated for amount-like values.
- Errors show inline beneath fields.

---

## 6) Security guidance

- Use this tool for **debugging/integration testing/documentation**.
- In production:
  - Generate hashes server-side only.
  - Never expose `salt` / `client_secret` in frontend.
  - Verify reverse hash before marking transaction success.

---

## 7) Reference links in this repo

### Core hash docs

- Hosted hash:  
  `docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/generate-hash-payu-hosted.md`
- Merchant hosted hash:  
  `docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/generate-hash-merchant-hosted.md`
- S2S hash request/response:  
  `docs/Collect Payments/introduction-web/server-to-server-integration/hashing-request-and-response.md`

### Split settlement

- `docs/Offerings/split-settlments/introduction-split-settlements/create-the-split.md`
- `docs/Offerings/split-settlments/api-integration-for-split-settlements/split-during-transaction-integration.md`

### Offers and v19

- `docs/Offerings/introduction-to-affordability/offers-integration/payu-hosted-checkout-integration-with-offers.md`
- `docs/Offerings/introduction-to-affordability/offers-integration/integrate-with-payu-hosted-checkout-integration-low-cost-emi.md`

### SI / TPV / subscriptions

- `docs/Offerings/introduction-to-payu-tpv/neftrtgs-integration-for-tpv.md`
- `docs/Offerings/introduction-to-payu-tpv/collect-payments-with-tpv-merchant-hosted-checkout/upi-intent-autopay-tpv-integration.md`
- `docs/Offerings/internal-subscripions-or-recurring-payments/subscriptions-integration/payu-hosted-integration-subscriptions.md`

### Mutual funds

- `docs/Offerings/mutual-funds-payments/payu-hosted-integration-mutual-funds-payment.md`
- `docs/Offerings/mutual-funds-payments/merchant-hosted-integration-mutual-fund-payments.md`

### Cross-border PACB

- `docs/Offerings/introduction-cross-border-payments-import/integrate-cross-border-payments-for-payubiz/plain-cards-integration-one-time-pacb.md`
- `docs/Offerings/introduction-cross-border-payments-import/integrate-cross-border-payments-for-payubiz/netbanking-integration-merchant-hosted-integration-cb.md`

### Partner integration

- `reference/ParTner integration/partner-payment-integration-apis/hosted-checkout-api-partner-integration.md`
- `reference/ParTner integration/partner-payment-integration-apis/upi-s2s-partner-integration-api.md`
- `reference/ParTner integration/partner-payment-integration-apis/refund-status-api-partner-integration.md`
- `reference/ParTner integration/partner-payment-integration-apis/refund-transaction-api-partner-integration.md`

### MCP / International

- `reference/international payments/mcp-lookup-api.md`

### Zion signatures

- `reference/ZION/manage-subscriptions/create-a-subscription.md`
- `reference/ZION/manage-subscriptions/update-subscription-api.md`
- `reference/ZION/manage-invoice-apis-for-zion/create-invoice-api-zion.md`
- `reference/Subscriptions/set-up-webhook-to-receive-cancellation-or-modification-update-from-the-issuer-bank.md`

---

## 8) Suggested sharing template (for internal teams)

Use this in email/Slack:

```text
PayU Hash Generator (web + CLI)

Web:
- Open index.html from payu-hosted-hash-tool or host it on Netlify
- Select logic in dropdown and generate hash

CLI:
- npx <package-name> --help
- npm install <package-name> (optional)

Supported:
- Hosted/Merchant/S2S, v19, Offers, Split, SI, TPV, PACB, Partner, MCP, Zion, webhook hashes

Docs:
- See payu-hosted-hash-tool/USAGE_GUIDE.md
```

