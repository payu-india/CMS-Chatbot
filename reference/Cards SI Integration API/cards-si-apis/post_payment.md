---
api:
  file: cards-si-api.yaml
  operationId: post_payment
hidden: true
link:
  new_tab: false
metadata:
  robots: noindex
---
Initiates a card payment request and begins the 3DS authentication process formandate creation. PayU selects the acquiring bank, submits the authenticationinitiation request, and returns an `acsTemplate` (Base64-encoded HTML) to redirectthe customer to the OTP page.After the customer submits the OTP, use the `bankData` from the OTP response(plus `siTokenDetails`) as `authentication_info` in the `AuthorizeTransaction` API.**Authentication Flows:**- **New card via PayU** — Send `auth_only=1`, `txn_s2s_flow=4`, `authentication_flow=REDIRECT`,  and plain card details (`ccnum`, `ccname`, etc.).- **Saved card via PayU** — Send `auth_only=1`, `txn_s2s_flow=4`, and  `storecard_token_type=1` with a stored network token (`store_card_token`).  `siTokenDetails` in the subsequent `AuthorizeTransaction` call is optional for this flow\.- **Authentication not via PayU** — Send `txn_s2s_flow=3` with `authentication_info`  already containing the 3DS result (cavv, eci, etc.) and `additional_info` with  network token details. The mandate is registered in this single call.**Hash formula:**`SHA512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)`Use empty strings for any `udf` fields not included. Include the serialised`si_details` JSON string at position 16 (after six trailing pipes).
