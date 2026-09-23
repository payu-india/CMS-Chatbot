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
  A <Anchor target="_blank" href="doc:payment-links-overview">payment link</Anchor> is a secure, shareable URL that lets your customer pay you without visiting your website or app. You <Anchor target="_blank" href="doc:send-a-payment-link">create the link</Anchor> in the PayU Dashboard or via <Anchor target="_blank" href="doc:api-create-share">API</Anchor>, share it over any channel such as email, SMS, or WhatsApp. Your customer clicks it to pay on a PayU-hosted checkout page. Once paid, you receive a notification and the transaction appears in your Dashboard.

  See <Anchor target="_blank" href="doc:how-payment-links-works">How Payment Links Works</Anchor> for the end-to-end flow.
</Accordion>

***

2. #### Do I need a developer or any code to create a Payment Link?

<Accordion title="Answer" icon="fab fa-adn">
  No. Payment Links is a no-code product. You can <Anchor target="_blank" href="doc:send-a-payment-link">create</Anchor>, <Anchor target="_blank" href="doc:manage-payment-links">share</Anchor>, and manage links entirely from the PayU Dashboard. The <Anchor target="_blank" href="doc:api-create-share">Payment Links API</Anchor> is available for merchants who want to automate link creation inside their own systems, but it is optional.
</Accordion>

***

3. #### Which payment methods can customers use?

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

4. #### UPI is not showing on the customer's payment page — why?

<Accordion title="Answer" icon="fab fa-adn">
  UPI should be enabled on your merchant account. If you can see UPI when you test the link but not your customer, ask them to try a different browser or device.

  If UPI is missing for all customers, contact <Anchor target="_blank" href="https://help.payu.in/query">PayU support</Anchor> to confirm that UPI is active on your merchant account.

  **UPI Intent (direct app redirect):** if you want to direct your customers straight into a UPI app without entering their VPA, you should enable UPI Intent separately. Contact your PayU KAM to enable it.
</Accordion>

***

5. #### Can I restrict payments to a specific bank or card type?

<Accordion title="Answer" icon="fab fa-adn">
  No. PayU Payment Links do not support bank-level or card-issuer-level restrictions (for example, Union Bank credit cards only). The checkout page shows all payment methods active on your account.

  If your use case requires restricting the checkout to a specific payment method or issuer, consider a Server-to-Server (S2S) integration, which gives you more control over the checkout experience. Contact your PayU KAM for guidance.
</Accordion>

***

6. #### Are Payment Links secure?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. PayU Payment Links are PCI DSS compliant. PayU uses advanced encryption and tokenisation to protect customer payment data. No card or bank details pass through your systems. The customer pays directly on PayU's hosted checkout page.
</Accordion>

***

## Creating and Configuring Links

1. #### Can I set a custom amount for each link?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Each link has its own amount field. You can also leave the amount flexible so the customer fills it in at checkout. This use case is useful for donations or open-ended collections.
</Accordion>

***

2. #### Can I collect customer information with the payment?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. You can add standard fields (name, email, phone, address) and fully custom fields (any label, any type) to the checkout page. See <Anchor target="_blank" href="https://docs.payu.in/docs/create-a-payment-link#how-do-i-create-a-payment-link">Payment Link Options</Anchor> for details.
</Accordion>

***

3. #### My custom fields are not visible on the customer's checkout page. Why?

<Accordion title="Answer" icon="fab fa-adn">
  Custom fields are visible on the checkout page only when the link is opened in a browser. To confirm they are configured correctly:

  1. Open the link in a **browser** (not the Dashboard preview).
  2. Check that the fields were added under **Additional Customer Details → Add New Fields+** during creation.
  3. Confirm the field type is set correctly (Alphanumeric, Calendar, or Dropdown).

  If the fields are still missing, the most common cause is that they were added after the link was already created. Payment Links cannot be edited after creation. <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links#what-can-i-do-with-a-payment-link-after-it-is-created">Duplicate</Anchor> the link, add the custom fields before clicking **Create and Send Payment Link**, then deactivate the original.
</Accordion>

***

4. #### Can I set an expiry date on a payment link?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. The default expiry is 1 year. You can set any future date during creation. Once expired, the link cannot accept payments.

  To extend expiry after creation: via API, use the <Anchor target="_blank" href="doc:api-cancel-status">Cancel / Change Status API</Anchor> with an updated `expiryDate`. From the Dashboard, you cannot extend expiry directly — duplicate the link with a new expiry date and deactivate the original.
</Accordion>

***

5. #### Can I limit how many times a link can be used?

<Accordion title="Answer" icon="fab fa-adn">
  Yes. Use the **Max Transactions** field when <Anchor target="_blank" href="https://docs.payu.in/docs/create-a-payment-link">[creating the link](https://docs.payu.in/docs/create-a-payment-link)</Anchor>. Leave it blank for unlimited. Once the limit is reached, the link automatically deactivates.
</Accordion>

***

6. #### Can I edit a payment link after creating it?

<Accordion title="Answer" icon="fab fa-adn">
  You cannot edit a link's amount, description, or configuration from the Dashboard after creation. To correct a mistake, <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links#what-can-i-do-with-a-payment-link-after-it-is-created">duplicate</Anchor> the link with the right details, then deactivate the original.

  Via API, you can update `active` status, `expiryDate`, `subAmount`, `tax`, `shippingCharge`, and `isPartialPaymentAllowed` using the <Anchor target="_blank" href="doc:api-cancel-status">Cancel / Change Status API</Anchor>.
</Accordion>

***

7. #### Can a customer pay in instalments?

<Accordion title="Answer" icon="fab fa-adn">
  Yes, if you enable **Partial Payment** on the link. The customer can pay any amount less than the total — you cannot specify a minimum partial amount. For structured auto-debiting, use <Anchor target="_blank" href="doc:recurring-payments">Recurring Payments</Anchor>.
</Accordion>

***

8. #### How many payment links can I create?

<Accordion title="Answer" icon="fab fa-adn">
  There is no hard limit on the number of payment links. For creating hundreds at once, use the <Anchor target="_blank" href="https://docs.payu.in/docs/create-a-payment-link#how-do-i-create-many-links-at-once">Bulk Upload</Anchor> feature or the <Anchor target="_blank" href="doc:api-create-share">Create Payment Link API</Anchor>.
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

3. #### My customer didn't receive the SMS. Why?

<Accordion title="Answer" icon="fab fa-adn">
  The three most common causes:

  **1. Mobile number was not included.**<br /><br />**For Dashboard links:** Confirm you entered the customer's mobile number in the Customer Details section and toggled **Send via SMS** on before creating the link.<br /><br />**For API links:** Confirm your request payload includes the `mobileNumber` field. PayU triggers SMS only when the mobile number is present in the create-link request — it is not optional if you want SMS delivery.

  **2. DND (Do Not Disturb) is active on the customer's number.**<br /><br />DND blocks all promotional and transactional SMS from every sender. Ask the customer to check their DND status with their mobile operator, or share the link via WhatsApp or email instead.

  **3. Notifications fire once at creation only.**<br /><br />SMS cannot be re-triggered for an existing link. To resend, go to **Actions → Share** in the Dashboard and send the link again manually, or share the URL directly.
</Accordion>

***

4. #### My customer didn't receive the payment link email. Why?

<Accordion title="Answer" icon="fab fa-adn">
  Check the following:

  1. Confirm the customer's email address was entered correctly. To verify, open the link **Details** view in the Dashboard.
  2. Confirm **Send Email** was toggled on at the time of creation. Notifications sent once at creation only. You cannot re-trigger them.
  3. Ask the customer to check their spam or junk folder.

  To resend, go to **Actions → Share** in the Dashboard and re-send via email, or copy the URL and share manually.
</Accordion>

***

## Payments and Reconciliation

1. #### How will I know when a customer has paid?

<Accordion title="Answer" icon="fab fa-adn">
  The link status in the Dashboard changes to **Paid** (or remains **Active** with a non-zero `totalRevenue` for partial-payment links). The transaction appears in the **Transactions** tab in the Dashboard.

  If you have webhooks configured, you receive a real-time `payment.success` event. See <Anchor target="_blank" href="doc:receive-and-verify-a-webhook">Webhooks: Receive & Verify</Anchor>.
</Accordion>

***

2. #### What happens if a customer's payment fails?

<Accordion title="Answer" icon="fab fa-adn">
  The link remains **Active** and the customer can try again — either immediately or later. A failed attempt does not count against the Max Transactions limit.
</Accordion>

***

3. #### The payment page shows a blank screen or a timeout — what do I do?

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

4. #### I'm getting a hash mismatch on the payment response — how do I fix it?

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

5. #### Why isn't my webhook receiving payment notifications?

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

6. #### Can I issue a refund for a payment made via a payment link?

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

9. #### Why am I getting 'Transaction initiation not allowed on aggregator'?

<Accordion title="Answer" icon="fab fa-adn">
  This error means your merchant account is configured as an aggregator but **split settlement has not been activated** for your account.

  If you are using `aggregatorSplitInfo` or `aggregatorCharges` in your create-link payload, split settlement must be explicitly enabled by PayU before you can use these fields. Contact your PayU account manager to activate split settlement for your MID.
</Accordion>

***

10. #### Can I use split settlement with Payment Links?

<Accordion title="Answer" icon="fab fa-adn">
  Yes, but it requires prior activation. Split settlement lets you distribute a single payment across multiple sub-merchants or accounts using `aggregatorSplitInfo` in the create-link API payload.

  **Prerequisites:**

  1. Your account must be onboarded as an aggregator with split settlement enabled — contact your PayU account manager.
  2. Child merchant accounts must be onboarded and approved before you can route payments to them.
  3. Test split settlement in UAT before going to production.

  Attempting to use `aggregatorSplitInfo` without activation will return the "Transaction initiation not allowed on aggregator" error.
</Accordion>
