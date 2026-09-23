---
title: FAQs (Frequently Asked Questions)
excerpt: >-
  Answers to common questions about PayU Payment Links — creation, limits,
  customisation, payment methods, security, and API usage.
deprecated: false
hidden: true
metadata:
  title: Payment Links FAQs | PayU Developer Docs
  description: >-
    Answers to common PayU Payment Links questions — how they work, expiry,
    partial payments, supported methods, API authentication, and token scopes.
  keywords:
    - payu payment links faq
    - payment link questions answers
    - payu payment link how it works
    - payment link partial payment faq
    - payment link expiry faq
    - payment link api faq
    - payu oauth token faq
    - payment link supported methods
    - payment link security payu
    - payu payment link limits
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-links
      title: Payment Links
      type: basic
    - slug: manage-payment-links
      title: Manage Payment Links
      type: basic
    - slug: payment-links-errors-and-troubleshooting
      title: Errors and Troubleshooting
      type: basic
---
<Banner
  isInline={true}
  message="Integration effort: No code or website required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

***

## General

1. #### What is a payment link and how does it work?

<Accordion title="Answer" icon="fab fa-adn">
  A <Anchor target="_blank" href="https://docs.payu.in/docs/payment-links">payment link</Anchor> is a secure, shareable URL that lets your customer pay you without visiting your website or app. You <Anchor target="_blank" href="https://docs.payu.in/docs/create-a-payment-link">create the link</Anchor> in the PayU Dashboard or via <Anchor target="_blank" href="https://docs.payu.in/reference/create-payment-links">API</Anchor>, share it over any channel such as email, SMS, or WhatsApp. Your customer clicks it to pay on a PayU-hosted checkout page. Once paid, you receive a notification and the transaction appears in your Dashboard.<br />

  See <Anchor target="_blank" href="https://docs.payu.in/docs/payment-links-workflow">How Payment Links Works</Anchor> for the end-to-end flow.
</Accordion>

***

2. #### Do I need a developer or any code to create a Payment Link?

<Accordion title="Answer" icon="fab fa-adn">
  No. Payment Links is a no-code product. You can <Anchor target="_blank" href="https://docs.payu.in/docs/create-a-payment-link">create</Anchor>, <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links#what-can-i-do-with-a-payment-link-after-it-is-created">share</Anchor>, and manage links entirely from the PayU Dashboard. The <Anchor target="_blank" href="https://docs.payu.in/reference/manage-payment-links">Payment Links API</Anchor> is available for merchants who want to automate link creation inside their own systems, but it is optional.
</Accordion>

***

3. #### Should I integrate web checkout first to use Payment Links? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  No. <Anchor target="_blank" href="https://docs.payu.in/docs/payment-links">Payment Links</Anchor> is a completely standalone product. You do not need a website, app, or any prior PayU integration to start using it. You can create and share payment links directly from the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor> with out any code or technical setup.<br />

  If you later integrate <Anchor target="_blank" href="https://docs.payu.in/docs/prebuilt-checkout-payu-hosted">PayU Hosted Checkout</Anchor> or Merchant <Anchor target="_blank" href="https://docs.payu.in/docs/custom-checkout-merchant-hosted">Hosted Checkout</Anchor> on your website, Payment Links remains available alongside those integrations.
</Accordion>

***

4. #### Which payment methods can customers use to make payments?

<Accordion title="Answer" icon="fab fa-adn">
  Customers can pay using payment methods enabled on your merchant account:

  - Credit/Debit cards (Visa, Mastercard, RuPay, and Amex)
  - UPI (GPay, PhonePe, Paytm, etc.)
  - Net Banking (50+ banks)
  - Wallets (Paytm, Mobikwik, and Freecharge)
  - EMI (no-cost and standard)
  - BNPL

  Contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> to enable or disable specific methods on your account.
</Accordion>

***

5. #### Why is UPI not showing on the customer's payment page?

<Accordion title="Answer" icon="fab fa-adn">
  UPI must be enabled on your merchant account. If you can see UPI when you test the link and not your customer while making the payment, ask them to try a different browser or device.<br />

  If UPI is missing for all customers, contact <Anchor target="_blank" href="https://help.payu.in/raise-ticket">PayU support</Anchor> to confirm that UPI is active on your merchant account.<br />

  **UPI Intent (direct app redirect):** if you want to direct your customers straight into a UPI app without entering their VPA, you should enable UPI Intent. Contact your PayU KAM for guidance.
</Accordion>

***

6. #### Can I restrict payments to a specific bank or card type?

<Accordion title="Answer" icon="fab fa-adn">
  No. Payment Links do not support bank-level or card-issuer-level restrictions (for example, **Union Bank credit cards** only). The checkout page shows all payment methods active on your account.<br />

  If your use case requires restricting the checkout to a specific payment method or issuer, consider Server-to-Server (S2S) integration, which gives you more control over the checkout experience. Contact your PayU KAM for guidance.
</Accordion>

***

7. #### Can I create a payment link in an international currency or in USD?

<Accordion title="Answer" icon="fab fa-adn">
  Yes, but you should first enable international payments on your merchant account.

  **Steps:**

  1. Contact your PayU Key Account Manager to enable international payments for your MID.
  2. Once enabled, use the `currency` parameter in the <Anchor target="_blank" href="doc:api-create-share">Create Payment Link API</Anchor> to specify the currency (for example, `"currency": "USD"`).

  PayU supports card payments from over 150 countries and offers Dynamic Currency Conversion (DCC), which allows your international customers to pay in their preferred local currency.

  **Dashboard:** The currency selection option is not available in the Dashboard unless international payments are active on your account. If you do not see it, raise a request with your account manager.

  <Callout icon="📘" theme="info">
    International currency payments apply only to card transactions. UPI, Net Banking, and Wallets are INR-only.
  </Callout>
</Accordion>

***

8. #### Are Payment Links secure?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. PayU Payment Links are PCI DSS compliant. PayU uses advanced encryption and tokenisation to protect customer payment data. No card or bank details pass through your systems — the customer pays directly on PayU's hosted checkout page.
</Accordion>

***

## Creating and Configuring Links

1. #### Can I set a custom amount for each link?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Each link has its own amount field. You can also leave the amount flexible so the customer fills it in at checkout — useful for donations or open-ended collections.
</Accordion>

***

2. #### Can I collect customer information with the payment?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. You can add standard fields (name, email, phone, address) and fully custom fields (any label, any type) to the checkout page. See <Anchor target="_blank" href="doc:payment-link-options">Payment Link Options</Anchor> for details.
</Accordion>

***

3. #### My customer is being asked to re-enter their email and phone number at checkout — why? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  Even when you pass `customerEmail` and `customerPhone` in your create-link API request, PayU may still prompt the customer to enter them if the **Additional Customer Details** fields are configured to capture email and phone on the checkout page.

  To prevent this, do not add email and phone as custom checkout fields in your link configuration. If you are using the API, omit these fields from the **Additional Customer Details** section of the payload. If you created the link via the Dashboard, check that you have not toggled on the email/phone fields under **Additional Customer Details**.
</Accordion>

***

4. #### My custom fields are not visible on the customer's checkout page — why?

<Accordion title="Answer" icon="fab fa-adn">
  Custom fields are visible on the checkout page only when the link is opened in a browser. To confirm they are configured correctly:

  1. Open the link in a **browser** (not the Dashboard preview).
  2. Check that the fields were added under **Additional Customer Details → Add New Fields+** during creation.
  3. Confirm the field type is set correctly (Alphanumeric, Calendar, or Dropdown).

  If the fields are still missing, the most common cause is that they were added after the link was already created — **Payment Links cannot be edited after creation**. Duplicate the link, add the custom fields before clicking **Create and Send Payment Link**, then deactivate the original.

  See <Anchor target="_blank" href="doc:payment-link-options">Custom Checkout Fields</Anchor> for details.
</Accordion>

***

5. #### Can I set an expiry date on a payment link?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. The default expiry is 1 year. You can set any future date during creation. Once expired, the link cannot accept payments.

  To extend expiry after creation: via API, use the <Anchor target="_blank" href="doc:api-cancel-status">Cancel / Change Status API</Anchor> with an updated `expiryDate`. From the Dashboard, you cannot extend expiry directly — duplicate the link with a new expiry date and deactivate the original.
</Accordion>

***

6. #### What format and timezone should I use for `expiryDate` in the API? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  The `expiryDate` parameter must be in **IST (Indian Standard Time)** using the format `YYYY-MM-DD HH:MM:SS`.

  Example: `"expiryDate": "2026-12-31 23:59:59"`

  Do not use UTC or any other timezone offset. If you send a UTC timestamp, the link expiry will be calculated incorrectly and may expire earlier or later than you intended.
</Accordion>

***

7. #### Can I limit how many times a link can be used?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Use the **Max Transactions** field when <Anchor target="_blank" href="doc:send-a-payment-link">creating the link</Anchor>. Leave it blank for unlimited. Once the limit is reached, the link automatically deactivates.
</Accordion>

***

8. #### Can I edit a payment link after creating it?

<Accordion title="Answer" icon="fab fa-adn">
  You cannot edit a link's amount, description, or configuration from the Dashboard after creation. To correct a mistake, <Anchor target="_blank" href="doc:manage-payment-links">duplicate</Anchor> the link with the right details, then deactivate the original.

  Via API, you can update `active` status, `expiryDate`, `subAmount`, `tax`, `shippingCharge`, and `isPartialPaymentAllowed` using the <Anchor target="_blank" href="doc:api-cancel-status">Cancel / Change Status API</Anchor>.
</Accordion>

***

9. #### Can a customer pay in instalments?

<Accordion title="Answer" icon="fab fa-adn">
  Yes, if you enable **Partial Payment** on the link. The customer can pay any amount less than the total — you cannot specify a minimum partial amount. For structured auto-debiting, use <Anchor target="_blank" href="doc:recurring-payments">Recurring Payments</Anchor>.
</Accordion>

***

10. #### Can Payment Links be used for subscription or recurring payments (SI / eNACH)? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  Yes, but through a separate **Subscription Payment Link** flow — not the standard `/payment-links` API.

  **Using the Dashboard:**

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor>.
  2. Go to **Subscriptions → Create Subscription Link**.
  3. Set the purpose, billing type (Fixed Amount or Maximum Amount), and subscription period.
  4. Share the link — the customer completes mandate registration (eNACH or UPI Autopay) on the PayU-hosted checkout page.

  **Using the API:**
  You can pass `si=1` and `si_details` parameters when creating a payment link via API to register a UPI Mandate. This requires Standing Instruction (SI) to be enabled on your merchant account — contact your PayU account manager to activate it.

  **Key difference:** a standard Payment Link collects a one-time payment. A Subscription Payment Link registers a mandate that authorises PayU to auto-debit your customer on a recurring schedule.

  <Callout icon="📘" theme="info">
    SI / eNACH activation is required before using subscription links. Contact your PayU account manager or raise a request via the Dashboard Help section.
  </Callout>
</Accordion>

***

11. #### My personal name is appearing alongside my company name on the payment page — how do I fix it? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  This happens when your PayU account's **Display Name** is not set separately from your login name. To fix it:

  1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor>.
  2. Click the drop-down at the top-right corner (your login name).
  3. Select **Profile**.
  4. Go to the **Business Details** tab.
  5. Update the **Display Name** field to your company or business name.
  6. Save the changes.

  The updated Display Name will appear on all payment pages, including those opened via payment links.
</Accordion>

***

12. #### How many payment links can I create?

<Accordion title="Answer" icon="fab fa-adn">
  There is no hard limit on the number of payment links. For creating hundreds at once, use the <Anchor target="_blank" href="doc:manage-payment-links">Bulk Upload</Anchor> feature or the <Anchor target="_blank" href="doc:api-create-share">Create Payment Link API</Anchor>.
</Accordion>

***

## Sharing and Notifications

1. #### How do I share a payment link with a customer?

<Accordion title="Answer" icon="fab fa-adn">
  You can share a payment link in three ways:

  - Copy the URL from the Dashboard and share it over any channel (WhatsApp, email, etc.)
  - Send it directly from the Dashboard via SMS or email — enter the customer's phone/email at creation and toggle notifications on
  - Reshare an existing link at any time from **Actions → Share**
</Accordion>

***

2. #### Can the same link be shared with multiple customers?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. A single link can be opened and paid by different customers, up to the Max Transactions limit (unlimited by default). For a personalised link pre-filled with a specific customer's details, create one link per customer.
</Accordion>

***

3. #### Can I send a payment link directly via WhatsApp? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  Yes. You can manually copy the link URL from the Dashboard and share it over WhatsApp like any other URL — no special setup required.

  For automated WhatsApp delivery at scale, PayU offers **Enhanced Payment Links (EPL) on WhatsApp**, which sends an approved WhatsApp Cloud API template message with a "Pay Now" button that carries the PayU payment link. This requires a separate WhatsApp Business API integration.

  See <Anchor target="_blank" href="doc:whatsapp-payment-links">WhatsApp Payment Link Integration</Anchor> for setup details.
</Accordion>

***

4. #### My customer didn't receive the SMS — why?

<Accordion title="Answer" icon="fab fa-adn">
  The three most common causes:

  **1. Mobile number was not included.**
  For Dashboard links: confirm you entered the customer's mobile number in the Customer Details section and toggled **Notify via SMS** on before creating the link.
  For API links: confirm your request payload includes the `mobileNumber` field. PayU triggers SMS only when the mobile number is present in the create-link request — it is not optional if you want SMS delivery.

  **2. DND (Do Not Disturb) is active on the customer's number.**
  DND blocks all promotional and transactional SMS from every sender. Ask the customer to check their DND status with their mobile operator, or share the link via WhatsApp or email instead.

  **3. Notifications fire once at creation only.**
  SMS cannot be re-triggered for an existing link. To resend, go to **Actions → Share** in the Dashboard and send the link again manually, or share the URL directly.
</Accordion>

***

5. #### My customer didn't receive the payment link email — why?

<Accordion title="Answer" icon="fab fa-adn">
  Check the following:

  1. Confirm the customer's email address was entered correctly — open the link **Details** view in the Dashboard.
  2. Confirm **Notify via Email** was toggled on at the time of creation. Notifications fire once at creation only — they cannot be re-triggered.
  3. Ask the customer to check their spam or junk folder.

  To resend, go to **Actions → Share** in the Dashboard and re-send via email, or copy the URL and share manually.
</Accordion>

***

6. #### Can I configure a per-link Success URL or Failure URL from the Dashboard? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  No. When creating a payment link from the **Dashboard**, you cannot set a per-link `successUrl` or `failureUrl`. Dashboard-created links redirect customers using the merchant account-level redirect URLs configured in your PayU account settings.

  If you need per-link redirect URLs (for example, to redirect each customer to a different order confirmation page), use the <Anchor target="_blank" href="doc:api-create-share">Create Payment Link API</Anchor> and pass `successUrl` and `failureUrl` in the request payload.

  <Callout icon="🚧" theme="warning">
    The API uses `successUrl` and `failureUrl` — not `surl` and `furl`. Using the wrong names will cause redirect failures. See the API Usage section below.
  </Callout>
</Accordion>

***

## Payments and Reconciliation

1. #### How will I know when a customer has paid?

<Accordion title="Answer" icon="fab fa-adn">
  The link status in the Dashboard changes to **Paid** (or remains **Active** with a non-zero `totalRevenue` for partial-payment links). The transaction appears in the **Transactions** tab in the Dashboard.

  If you have webhooks configured, you receive a real-time `payment.success` event. See <Anchor target="_blank" href="doc:receive-and-verify-a-webhook">Webhooks: Receive & Verify</Anchor>.
</Accordion>

***

2. #### The Fetch Payment Link API returns no data immediately after I create a link — why? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  This is expected behaviour. A newly created payment link has no transactions yet, so status-related fields like `totalRevenue`, `totalAmountCollected`, and transaction counts will be empty or zero until a customer attempts a payment.

  The link itself is immediately **Active** after creation — use the <Anchor target="_blank" href="doc:api-fetch">Fetch Single Payment Link API</Anchor> (by invoice number) to confirm the link was created and check its current status.

  **"PENDING" status:** PENDING is a _transaction_ status (a payment in progress at the bank), not a link status. A link with no transactions will never return PENDING — it returns Active.

  If you get a completely empty response body with HTTP 200 on the create-link call, verify that all required fields in your payload are correctly formatted. Check the `invoiceNumber` uniqueness and ensure the `Authorization` header carries a valid, unexpired Bearer token.
</Accordion>

***

3. #### What happens if a customer's payment fails?

<Accordion title="Answer" icon="fab fa-adn">
  The link remains **Active** and the customer can try again — either immediately or later. A failed attempt does not count against the Max Transactions limit.
</Accordion>

***

4. #### The payment page shows a blank screen or a timeout — what do I do?

<Accordion title="Answer" icon="fab fa-adn">
  This is almost always a configuration issue with your redirect URLs. Check the following:

  **1. Confirm the parameter names are correct.**
  The Payment Links API uses `successUrl` and `failureUrl` — not `surl` and `furl`. Using the wrong names causes a blank screen or redirect failure after payment.

  **2. Confirm your redirect URLs are whitelisted.**
  Your `successUrl` and `failureUrl` domains must be registered in your PayU merchant account. Contact PayU support or your account manager to whitelist them.

  **3. Check the link status.**
  If the link is expired or deactivated, the payment page will not load. Verify the link is **Active** in the Dashboard.

  If the issue is intermittent, it may be a network or browser issue on the customer's end. Ask them to try on a different browser or device.
</Accordion>

***

5. #### I'm getting a hash mismatch on the payment response — how do I fix it?

<Accordion title="Answer" icon="fab fa-adn">
  Hash mismatch means the hash you are computing locally does not match what PayU sent in the response. The most common causes:

  **1. Wrong hash formula.**
  The Payment Links response hash uses the **reverse** of the payment request hash. The formula is:
  `sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)`

  **2. Extra spaces or encoding differences.**
  Compute the hash from the exact values in the response — do not trim or re-encode any field.

  **3. Using the wrong SALT.**
  Ensure you are using the SALT that corresponds to the `key` in the response.

  **4. Split payment payload.**
  If you are using `aggregatorSplitInfo` or `aggregatorCharges` in your create-link request, verify that **split settlement is enabled on your account**. Attempting split settlement on an account that hasn't been onboarded for it can produce unexpected response fields that break hash verification. Contact your PayU account manager to confirm it is activated.
</Accordion>

***

6. #### Why isn't my webhook receiving payment notifications?

<Accordion title="Answer" icon="fab fa-adn">
  Check these in order:

  **1. Webhook URL must be registered.**
  Your webhook endpoint must be configured in the PayU Dashboard under **Settings → Webhooks**, or whitelisted by your PayU account manager. PayU does not send events to unregistered URLs.

  **2. Your endpoint must return HTTP 200.**
  PayU retries delivery if it receives anything other than a `2xx` response. Check your server logs to confirm the endpoint is receiving the request and responding correctly.

  **3. Verify the webhook hash.**
  If your hash verification logic rejects the event, it will appear to "not arrive" in your app even though PayU sent it. To confirm whether PayU sent a webhook for a specific transaction, contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> with the `txnid` and `mihpayid` — the integration team can pull webhook delivery logs.

  **4. Check firewall rules.**
  Ensure your server allows inbound requests from PayU's IP ranges.
</Accordion>

***

7. #### Can I issue a refund for a payment made via a payment link?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Find the transaction in the **Transactions** tab and initiate a refund from there. The refund process is the same regardless of how the payment was collected.
</Accordion>

***

## API Usage

1. #### Do I need a special API key for Payment Links?

<Accordion title="Answer" icon="fab fa-adn">
  Payment Links APIs use **OAuth2 Bearer token** authentication — separate from your standard PayU `key` + `salt` + SHA-512 hash. You need a **Client ID** and **Client Secret** to generate a token.

  See <Anchor target="_blank" href="doc:api-auth-token">Authentication (Token)</Anchor>.
</Accordion>

***

2. #### Where do I find my Client ID and Client Secret?

<Accordion title="Answer" icon="fab fa-adn">
  Your production Client ID and Client Secret are in the PayU Dashboard:

  1. Log in to <Anchor target="_blank" href="https://onboarding.payu.in/">PayU Dashboard</Anchor>
  2. Go to **Settings → API Keys** (or **Developer Settings**, depending on your dashboard version)
  3. Your **Client ID** and **Client Secret** are listed there alongside your Key and Salt.

  If you do not see them, your account may not have Payment Links API access enabled. Contact your PayU account manager or raise a request via the Dashboard **Help** section.

  **For UAT testing**, your UAT Client ID and Client Secret are provided separately by the integration team with your UAT credentials. Do not use production credentials in UAT and vice versa.

  <Callout icon="🚧" theme="warning">
    Never share your Client Secret in public code repositories, client-side JavaScript, or mobile app binaries. Store it server-side only.
  </Callout>
</Accordion>

***

3. #### What are the UAT and production API endpoints?

<Accordion title="Answer" icon="fab fa-adn">
  Payment Links APIs use different base URLs for UAT and production:

  | Environment    | Token endpoint                             | Payment Links endpoint                    |
  | -------------- | ------------------------------------------ | ----------------------------------------- |
  | **UAT**        | `https://uat-accounts.payu.in/oauth/token` | `https://uatoneapi.payu.in/payment-links` |
  | **Production** | `https://accounts.payu.in/oauth/token`     | `https://oneapi.payu.in/payment-links`    |

  Using a UAT token against the production endpoint (or vice versa) will return a `401 Unauthorized` error. Confirm you are using matching credentials and URLs for the same environment.
</Accordion>

***

4. #### What scopes does each API operation require?

<Accordion title="Answer" icon="fab fa-adn">
  | Operation              | Required scope         |
  | ---------------------- | ---------------------- |
  | Create a payment link  | `create_payment_links` |
  | Share a payment link   | `read_payment_links`   |
  | Fetch a single link    | `read_payment_links`   |
  | Fetch all links        | `read_payment_links`   |
  | Update / cancel a link | `update_payment_links` |

  Request multiple scopes in one token by separating them with spaces: `create_payment_links update_payment_links read_payment_links`.
</Accordion>

***

5. #### How long is a token valid, and can I reuse it?

<Accordion title="Answer" icon="fab fa-adn">
  Tokens expire after the number of seconds in the `expires_in` field — typically 3600 (1 hour). A token is valid for multiple API calls until it expires or is revoked — you do not need a new token per request. Generate a new token before it expires and do not hard-code tokens in your application.
</Accordion>

***

6. #### Why am I getting a 401 Unauthorized error?

<Accordion title="Answer" icon="fab fa-adn">
  A `401` error almost always means one of:

  - **Token expired** — tokens are valid for \~1 hour. Generate a new token and retry.
  - **Wrong environment** — you are using a UAT token against the production endpoint, or vice versa. See the endpoint table above.
  - **Missing or wrong scope** — the token was generated without the scope required for the operation. Check the scopes table above and regenerate the token with the correct scopes.
  - **Token revoked** — if the token was explicitly revoked, generate a new one.
</Accordion>

***

7. #### Why am I getting 'furl/surl not recognised'?

<Accordion title="Answer" icon="fab fa-adn">
  The Payment Links API does not use the shorthand `furl` and `surl` (those are used in the standard PayU Hosted Checkout integration). Use `failureUrl` and `successUrl` instead in your create-link payload.
</Accordion>

***

8. #### Why am I getting 'Invoice Number already exists'?

<Accordion title="Answer" icon="fab fa-adn">
  Each payment link must have a unique `invoiceNumber` within your merchant account. Either use a different value, or omit `invoiceNumber` entirely — PayU will auto-generate a unique one.
</Accordion>

***

9. #### The Fetch All Payment Links API requires `fromDate` and `toDate` — can I skip them to fetch a specific link? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  The `fromDate` and `toDate` parameters are mandatory for the **Fetch All Payment Links** API because the API retrieves a list of links across a date range. Without these bounds, the response could include thousands of records and become prohibitively large.

  **To fetch a specific link without date parameters**, use the <Anchor target="_blank" href="doc:api-fetch">Fetch Single Payment Link API</Anchor> instead — it takes only the `invoiceNumber` as a path parameter and returns that link's full details immediately, with no date range required.
</Accordion>

***

10. #### Are UDF fields (udf1–udf5) visible to customers on the checkout page? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  No. UDF (User Defined Fields) values passed in your create-link API request are **not displayed to customers** on the PayU-hosted checkout page. They are server-side metadata — they travel with the transaction and appear in your transaction reports, webhook payloads, and the Fetch Payment Link API response, but customers never see them.

  Use UDFs to pass your internal order IDs, customer segments, product codes, or any reference data you need for reconciliation.
</Accordion>

***

11. #### Does Payment Links support TPV (Third Party Verification)? <Badge type="success">New</Badge>

<Accordion title="Answer" icon="fab fa-adn">
  TPV is not configured during payment link creation — it is enforced at the payment page level when the customer selects a payment method.

  To restrict a payment link's checkout to TPV-verified accounts (for example, accepting Net Banking only from a customer's registered account), use the `enforcePayMethod` parameter when creating the link. TPV must be enabled on your merchant account before you can use it.

  TPV is primarily used for subscription or mandate-based flows (SI / UPI Autopay), not standard one-time payment links. Contact your PayU account manager to confirm whether TPV is active for your MID and to understand the applicable payment methods.
</Accordion>

***

12. #### Why am I getting 'Transaction initiation not allowed on aggregator'?

<Accordion title="Answer" icon="fab fa-adn">
  This error means your merchant account is configured as an aggregator but **split settlement has not been activated** for your account.

  If you are using `aggregatorSplitInfo` or `aggregatorCharges` in your create-link payload, split settlement must be explicitly enabled by PayU. Contact your PayU account manager to activate split settlement for your MID.
</Accordion>

***

13. #### Can I use split settlement with Payment Links?

<Accordion title="Answer" icon="fab fa-adn">
  Yes, but it requires prior activation. Split settlement lets you distribute a single payment across multiple sub-merchants or accounts using `aggregatorSplitInfo` in the create-link API payload.

  **Prerequisites:**

  1. Your account must be onboarded as an aggregator with split settlement enabled — contact your PayU account manager.
  2. Child merchant accounts must be onboarded and approved before you can route payments to them.
  3. Test split settlement in UAT before going to production.

  Attempting to use `aggregatorSplitInfo` without activation will return the "Transaction initiation not allowed on aggregator" error.
</Accordion>
