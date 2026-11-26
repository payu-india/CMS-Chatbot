# Partner payment API docs

Functional files: `reference/Partner Integration/partner-payment-integration-apis/` and the three edited pages under `reference/Partner Integration/collect-payment-for-partners/`.

## 1. Decision summary

- **Decision being made:** Publish partner payment endpoint pages whose fields match `PartnerController` and the Java DTOs in partnerintegration-master, and correct the three live pages that still disagreed with those DTOs.
- **Decider:** Technical writer for the files. The user (Publisher) decides whether to merge.
- **Reversibility:** two-way medium for the new pages. Two-way medium for the parameter rows added to hosted checkout, UPI S2S, and refund. One-way if a merchant treats a forwarded EMI or offers response field as a stable schema. Those responses are documented as pass-through JSON.
- **Cost if wrong:** merchant rework. A required field that the service does not accept fails the call. A required field that was left optional fails later, inside the downstream service.

## 2. Cognitive pre-work

- **Reader base rate:** Partner platform developer who already has a bearer token or HMAC headers and is calling `/partner/*` for a referred merchant.
- **Falsifiers:** `PartnerController.java`, `PartnerTxnDTO.java`, `RefundTxnDto.java`, `FetchOfferDTO.java`, `ValidateOfferDTO.java`, `SubmitCardOtpDTO.java`, `ResendCardOtpDTO.java`, `PartnerPaymentLinkTxnDTO.java`, `BoltHashRequestDTO.java`, `BoltHashUtil.java`, `PartnerUtils.validateStaticQrHash`, and the published Partner QR pages under `reference/Partner Integration/partner-qr-integration-apis/`.
- **Pre-mortem:** An integrator shipped the wrong flow because this page required `pg` and `bankcode` on fetch offer, or `txnid` on submit OTP, or treated `/partner/paymentSuccess` as a URL they host. The service rejects or ignores those shapes.
- **Inversion:** A page that copies the outline's field list without the DTO fails the first sandbox call. These pages use the DTO and the controller, and they say when a body is only forwarded.

## 3. Quantitative method

- Parameters documented / parameters in the named spec: 22 new operations. Each required field was taken from a `@NotEmpty` / `@NotNull` annotation or from an explicit null check in `PartnerService`. Forwarded-only fields are marked as forwarded.
- Error codes documented / matching entries in `payment-error-codes.json`: not applicable because these partner routes return handler messages (`errors`, `error`) rather than rows in `payment-error-codes.json`. Messages quoted from `ValidationExceptionHandler` and the service methods.
- Recipe fields that match the parameter table: not applicable because this change does not add files under `recipes/`. Curl samples on the new pages use the required fields from the same schema.
- Internal links checked against repo paths: new pages do not link to missing slugs. Static QR hash text quotes `PartnerUtils.validateStaticQrHash`. Bolt hash text quotes `BoltHashUtil` and matches `custom_blocks/HashingSample.md`.

## 4. Red-team pass

- **Wrong integrator:** Hosted-checkout fields were added on `new-partner-payment-using-hosted-checkout-integration.md`, not on a second checkout page. QR initiate, dynamic QR, and verify status follow the existing Partner QR pages, which already document those paths.
- **Stale contract:** The outline's fetch-offer, validate-offer, OTP, payment-link, static QR, and Bolt response shapes disagree with the DTOs. The pages follow the DTOs. EMI `type` and `var2` are required by `getEligibleBins` but their business meaning is not named in that method.
- **Secret leakage:** Samples use `YOUR_ACCESS_TOKEN`, `YOUR_RESELLER_UUID`, `YOUR_HASH`, and `YOUR_MERCHANT_KEY`.
- **Support load:** `<PartnerAPIEnvironment />` does not exist, so each page has an environment table instead. Partner QR guides use `apitest.payu.in` and `api.payu.in/apilayer`. These pages use `api.payu.in` and `test-partnerapilayer.payu.in/apilayer`, which is what the hosted-checkout page already uses. Refund status still says "WhatsApp's reseller uuid". That file was left unchanged because the request said no other edits there.

## 5. Tripwires and rollback

- A new page whose required field is not in the DTO or the service check.
- A curl sample that omits a required field from its schema.
- `_order.yaml` entry `partner-payment-integration-apis` whose directory is missing.
- A hash string other than the payment hash or the static-QR string quoted from `validateStaticQrHash`.

**Rollback owner:** the user. Close the pull request. The agent does not push `v1`.

## 6. Frameworks applied

- WR-1: each page is one endpoint and one job.
- WR-3: Bolt hash points at the payment hash in `HashingSample.md`. No new custom block was added. The missing `PartnerAPIEnvironment` block was not invented.
- WR-5: existing pages were edited in place. Nothing was deleted or marked deprecated.
- Counter-metric: a sandbox call rejected for a field this page marks required, or accepted only when a field this page omits is sent.
- Decision requested of the Publisher: merge the pull request, or name the page whose field list should follow the outline instead of the DTO.
- `Writer-OS-Metrics: skill_id=writer-restructure, date=2026-11-24`
