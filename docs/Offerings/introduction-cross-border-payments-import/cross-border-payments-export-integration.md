---
title: Cross Border Payments - Export Integration
deprecated: false
hidden: true
icon: far fa-arrow-down-up-across-line
metadata:
  robots: index
---
<HTMLBlock>{`
<div style="background-color:#FFC107;padding:10px 16px;border-radius:8px;font-weight:600;font-family:sans-serif;">

  ⚙️ Minimal technical setup required — uses PayU Hosted Checkout
</div>
`}</HTMLBlock>

## What you're building

A PayU Hosted Checkout integration that lets overseas buyers pay your Indian business in their own currency. Your buyer pays with a local wallet (such as GrabPay or Touch 'n Go) or an international card. PayU settles the proceeds to your Indian bank account in INR and issues an electronic Foreign Inward Remittance Advice (eFIRA) for every settled transaction, which you can use as proof of export receipt.

<Callout icon="📘" theme="info">
  ### **Key Capabilities**

  - **Local wallets for overseas buyers**: Buyers pay with the wallet they already use in their home market, alongside international cards.
  - **No new payment UI**: PayU Hosted Checkout shows the wallets and handles wallet authentication (app deeplink, QR, or OTP).
  - **One integration**: You integrate with PayU only. PayU manages every wallet connection behind the scenes.
  - **INR settlement with eFIRA**: Proceeds are settled in INR to your Indian bank account, with an eFIRA for RBI and GST compliance.
</Callout>

***

## How it works

1. Your website collects the buyer's details and the amount in the buyer's currency (foreign currency, or FCY).
2. Your server posts the payment request to PayU using the merchant key and salt of the MID for that currency.
3. PayU Hosted Checkout shows the wallets enabled for that currency, alongside international cards.
4. The buyer selects a wallet and is redirected to the wallet provider's page to authenticate (deeplink, QR, or OTP, depending on the wallet and device).
5. After authorization, the buyer returns to PayU, and PayU confirms the final payment result.
6. PayU redirects the buyer to your `surl` (success) or `furl` (failure) and sends a webhook to your notification URL.
7. PayU settles the INR amount to your bank account and shares the eFIRA.

### Supported currencies and wallets

PayU assigns **one MID per currency**. The wallets shown on the checkout depend on the MID currency and on what PayU has activated on that MID during onboarding. You can't configure wallet visibility yourself.

| MID currency | Wallet            | Buyer market | Buyer authentication (mobile)                          | Buyer authentication (desktop)                       |
| :----------- | :---------------- | :----------- | :----------------------------------------------------- | :--------------------------------------------------- |
| `SGD`        | GrabPay Singapore | Singapore    | Deeplink to the Grab app, then PIN or biometric        | Mobile number + SMS OTP                              |
| `MYR`        | Touch 'n Go       | Malaysia     | Deeplink to the TnG eWallet app, then PIN or biometric | QR (interoperates with DuitNow QR)                   |
| `MYR`        | GrabPay Malaysia  | Malaysia     | Deeplink to the Grab app, then PIN or biometric        | Mobile number + SMS OTP; DuitNow QR interoperability |

For example, a merchant using the SGD MID shows GrabPay and international cards. A merchant using the MYR MID shows Touch 'n Go, GrabPay Malaysia and international cards.

**The PayU Cross-Border Exports integration involves the following steps:**

<Cards columns="3">
  <Card title="1. Start Integration" href="#step-1-start-integration">
    Build the payment request, hash and response handling
  </Card>

  <Card title="2. Test Integration" href="#step-2-test-integration">
    Run success, failure and validation scenarios
  </Card>

  <Card title="3. Go-Live Checklist" href="#step-3-go-live-checklist">
    Switch to production and verify settlement
  </Card>
</Cards>

<Callout icon="📘" theme="info">
  ### **Prerequisites**

  - An active PayU merchant account onboarded for **Cross-Border Exports**. Onboarding is assisted by your PayU Key Account Manager (KAM).
  - **One MID per currency** you want to accept, each with its own merchant **key** and **salt**, for both test and production.
  - Your **RBI purpose code** and **service utilization country** agreed with the PayU onboarding team.
  - An HTTPS `surl` and `furl` on your website, and an HTTPS **webhook URL** registered with PayU.
  - A way to convert your INR prices to the buyer's currency before calling PayU. PayU doesn't convert currency at checkout.
</Callout>

***

## Step 1: Start Integration

| Environment    | Payment URL                       |
| :------------- | :-------------------------------- |
| **Test**       | `https://test.payu.in/_payment`   |
| **Production** | `https://secure.payu.in/_payment` |

<Accordion title="Step 1.1: Select the MID for the transaction currency" icon="fa-coins">
  Your server decides which currency applies to each transaction and must use the **key and salt of the MID for that currency**.

  - One MID supports one currency only.
  - If the MID key and `transactionCurrency` don't match (for example, the SGD key with `transactionCurrency=MYR`), the payment fails.
  - Store each MID's key and salt securely on your server, mapped by currency.

  **Expected Output:** For each order, your server has the correct `key` and `salt` for the buyer's currency.
</Accordion>

<Accordion title="Step 1.2: Calculate the amount in the buyer's currency" icon="fa-calculator">
  Pass the amount **in the foreign currency (FCY)**. PayU doesn't convert INR to FCY.

  If you price in INR, convert to FCY on your server using a rate of your choice before you call PayU.

  For example, if a course costs INR 10,000 and your SGD/INR rate is 62, pass `amount=161.29` with `transactionCurrency=SGD`.

  **Expected Output:** A decimal amount in FCY, with no currency symbol.
</Accordion>

<Accordion title="Step 1.3: Collect the buyer's remitter details" icon="fa-user-check">
  The buyer's `firstname`, `address1`, `zipcode` and `country` are **mandatory for export settlement**. Every export transaction must carry the remitter's name, address and country. If any of these is missing, **settlement is rejected even if the payment succeeded at checkout**.

  You can collect these details in one of two ways:

  1. **Pass them in the payment request (recommended).** Use this if you already collect the buyer's billing details at registration or checkout.
  2. **Let PayU Hosted Checkout collect them.** Use this only if you don't hold the details at payment time. Confirm this option with the PayU integration team during onboarding.

  {/* REVIEW: Confirm that PayU Hosted Checkout can collect remitter details for exports, and how it is enabled. */}

  <Callout icon="🚧" theme="warn">
    ### **Watch Out!**

    - `country` must **not** be `IN`. Export transactions must come from foreign residents, so a buyer country of India fails the settlement check. Block Indian-resident buyers from this payment option on your website.
    - Collect the buyer's name in English.
  </Callout>

  {/* REVIEW: Source doc mentions a custom note "Please enter your name in English". Confirm whether this is shown on the PayU checkout or is a merchant requirement. */}
</Accordion>

<Accordion title="Step 1.4: Prepare the request parameters" icon="fa-list-check">
  These are the parameters for a Cross-Border Exports payment. Fields marked **Exports** differ from the standard domestic integration.

  <Tabs>
    <Tab title="Mandatory">
      | Parameter             | Description                                                                                                                                                                                              |
      | :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `key`                 | `string` Merchant key of the MID for the transaction currency. Each currency has a separate key. For example, `YOUR_SGD_MID_KEY`                                                                         |
      | `txnid`               | `string` Unique transaction ID you generate. Alphanumeric, maximum 25 characters. Must be unique across all your transactions; a reused `txnid` is treated as a duplicate. For example, `EXP20261022001` |
      | `amount`              | `string` Amount in the foreign currency, with no currency symbol. For example, `161.29`                                                                                                                  |
      | `transactionCurrency` | `string` **Exports.** ISO 4217 code of the amount. Must match the currency of the MID key. Optional in domestic integrations, mandatory here. For example, `SGD`                                         |
      | `productinfo`         | `string` Short description of the actual product or service. Avoid generic labels. For example, `Online Course`                                                                                          |
      | `firstname`           | `string` **Exports.** Buyer's first name, used as the remitter name for settlement. For example, `Wei Ling`                                                                                              |
      | `email`               | `string` Buyer's email address. For example, `weiling@example.com`                                                                                                                                       |
      | `phone`               | `string` Buyer's phone number with country code. For example, `+6591234567`                                                                                                                              |
      | `address1`            | `string` **Exports.** Buyer's billing address line 1, used as the remitter address for settlement. Optional in domestic integrations, mandatory here. For example, `10 Anson Road`                       |
      | `city`                | `string` Buyer's city. For example, `Singapore`                                                                                                                                                          |
      | `zipcode`             | `string` Buyer's postal or ZIP code. For example, `079903`                                                                                                                                               |
      | `country`             | `string` **Exports.** Buyer's country as an ISO alpha-2 code. Must not be `IN`. For example, `SG`                                                                                                        |
      | `surl`                | `string` HTTPS URL PayU redirects the buyer to on success. For example, `<redacted URL>`                                                                                                                 |
      | `furl`                | `string` HTTPS URL PayU redirects the buyer to on failure or cancellation. For example, `<redacted URL>`                                                                                                 |
      | `hash`                | `string` SHA-512 hash of the request, generated on your server. For for more information, refer to Step 1.5                                                                                              |
    </Tab>

    <Tab title="Conditional">
      | Parameter     | Description                                                                                                                                                                                                            |
      | :------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `udf1`        | `string` **Exports.** RBI purpose code. Required for service exports. Confirm the code for your service category with the PayU onboarding team. For example, `P1007` (online education) or `P1004` (software services) |
      | `udf2`        | `string` **Exports.** Service utilization country, that is, the country where the buyer uses the service (usually the same as `country`). Required when `udf1` is a service-export purpose code. For example, `SG`     |
      | `udf5`        | `string` **Exports.** Invoice ID. Required when your purpose code needs an invoice reference. For example, `INV-2026-0001`                                                                                             |
      | `api_version` | `string` API version that allows `transactionCurrency`. For example, `22`                                                                                                                                              |
    </Tab>

    <Tab title="New Tab">

    </Tab>
  </Tabs>
</Accordion>

<Accordion title="Step 1.5: Generate the hash" icon="fa-lock">
  Generate the SHA-512 hash **on your server only**, using the salt of the same MID as the `key`.

  <Callout icon="❗️" theme="error">
    ### **Important**

    The exact hash formula for Cross-Border Exports is confirmed by the PayU integration team at onboarding. Don't assume the domestic formula applies.
  </Callout>

  The samples below use the formula for `api_version=22`, which adds `transactionCurrency` after the ten UDF slots:

  ```text
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|transactionCurrency|SALT)
  ```

  Empty UDFs are kept as empty slots. With `udf6`–`udf10` empty, the string looks like this:

  ```text
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||transactionCurrency|SALT
  ```



  <Tabs>
    <Tab title="PHP">
      ```php
      <?php
      function generateHash(array $p, string $salt): string {
          $seq = [
              $p['key'], $p['txnid'], $p['amount'], $p['productinfo'],
              $p['firstname'], $p['email'],
              $p['udf1'] ?? '', $p['udf2'] ?? '', $p['udf3'] ?? '',
              $p['udf4'] ?? '', $p['udf5'] ?? '',
              '', '', '', '', '',               // udf6 to udf10
              $p['transactionCurrency'],
              $salt
          ];
          return strtolower(hash('sha512', implode('|', $seq)));
      }
      ```
    </Tab>

    <Tab title="Java">
      ```java
      import java.nio.charset.StandardCharsets;
      import java.security.MessageDigest;
      import java.util.Map;

      public class ExportsHash {
          public static String generateHash(Map<String, String> p, String salt) throws Exception {
              String[] seq = {
                  p.get("key"), p.get("txnid"), p.get("amount"), p.get("productinfo"),
                  p.get("firstname"), p.get("email"),
                  p.getOrDefault("udf1", ""), p.getOrDefault("udf2", ""), p.getOrDefault("udf3", ""),
                  p.getOrDefault("udf4", ""), p.getOrDefault("udf5", ""),
                  "", "", "", "", "",               // udf6 to udf10
                  p.get("transactionCurrency"),
                  salt
              };
              MessageDigest md = MessageDigest.getInstance("SHA-512");
              byte[] digest = md.digest(String.join("|", seq).getBytes(StandardCharsets.UTF_8));
              StringBuilder sb = new StringBuilder();
              for (byte b : digest) sb.append(String.format("%02x", b));
              return sb.toString();
          }
      }
      ```
    </Tab>

    <Tab title="C#">
      ```csharp
      using System.Collections.Generic;
      using System.Security.Cryptography;
      using System.Text;

      public static class ExportsHash
      {
          public static string GenerateHash(Dictionary<string, string> p, string salt)
          {
              string Get(string k) => p.TryGetValue(k, out var v) ? v : "";
              var seq = new[] {
                  Get("key"), Get("txnid"), Get("amount"), Get("productinfo"),
                  Get("firstname"), Get("email"),
                  Get("udf1"), Get("udf2"), Get("udf3"), Get("udf4"), Get("udf5"),
                  "", "", "", "", "",               // udf6 to udf10
                  Get("transactionCurrency"),
                  salt
              };
              using var sha = SHA512.Create();
              var bytes = sha.ComputeHash(Encoding.UTF8.GetBytes(string.Join("|", seq)));
              var sb = new StringBuilder();
              foreach (var b in bytes) sb.Append(b.ToString("x2"));
              return sb.ToString();
          }
      }
      ```
    </Tab>

    <Tab title="Python">
      ```python
      import hashlib

      def generate_hash(p: dict, salt: str) -> str:
          seq = [
              p["key"], p["txnid"], p["amount"], p["productinfo"],
              p["firstname"], p["email"],
              p.get("udf1", ""), p.get("udf2", ""), p.get("udf3", ""),
              p.get("udf4", ""), p.get("udf5", ""),
              "", "", "", "", "",               # udf6 to udf10
              p["transactionCurrency"],
              salt,
          ]
          return hashlib.sha512("|".join(seq).encode("utf-8")).hexdigest()
      ```
    </Tab>

    <Tab title="Node.js">
      ```javascript
      const crypto = require("crypto");

      function generateHash(p, salt) {
        const seq = [
          p.key, p.txnid, p.amount, p.productinfo,
          p.firstname, p.email,
          p.udf1 || "", p.udf2 || "", p.udf3 || "", p.udf4 || "", p.udf5 || "",
          "", "", "", "", "",                // udf6 to udf10
          p.transactionCurrency,
          salt,
        ];
        return crypto.createHash("sha512").update(seq.join("|"), "utf8").digest("hex");
      }
      ```
    </Tab>
  </Tabs>

  **Expected Output:** A 128-character lowercase hexadecimal string.
</Accordion>

<Accordion title="Step 1.6: Post the payment request" icon="fa-paper-plane">
  Post the parameters to the payment URL as an HTML form from the buyer's browser. PayU then shows the hosted checkout.

  <Tabs>
    <Tab title="HTML">
      ```html
      <form action="https://test.payu.in/_payment" method="post">
        <input type="hidden" name="key" value="YOUR_SGD_MID_KEY" />
        <input type="hidden" name="txnid" value="EXP20261022001" />
        <input type="hidden" name="amount" value="161.29" />
        <input type="hidden" name="transactionCurrency" value="SGD" />
        <input type="hidden" name="api_version" value="22" />
        <input type="hidden" name="productinfo" value="Online Course" />
        <input type="hidden" name="firstname" value="Wei Ling" />
        <input type="hidden" name="email" value="weiling@example.com" />
        <input type="hidden" name="phone" value="+6591234567" />
        <input type="hidden" name="address1" value="10 Anson Road" />
        <input type="hidden" name="city" value="Singapore" />
        <input type="hidden" name="zipcode" value="079903" />
        <input type="hidden" name="country" value="SG" />
        <input type="hidden" name="udf1" value="P1007" />
        <input type="hidden" name="udf2" value="SG" />
        <input type="hidden" name="udf5" value="INV-2026-0001" />
        <input type="hidden" name="surl" value="<redacted URL>" />
        <input type="hidden" name="furl" value="<redacted URL>" />
        <input type="hidden" name="hash" value="YOUR_GENERATED_HASH" />
        <input type="submit" value="Pay now" />
      </form>
      ```
    </Tab>

    <Tab title="cURL">
      ```bash
      curl -X POST "https://test.payu.in/_payment" \
        -H "Content-Type: application/x-www-form-urlencoded" \
        --data-urlencode "key=YOUR_SGD_MID_KEY" \
        --data-urlencode "txnid=EXP20261022001" \
        --data-urlencode "amount=161.29" \
        --data-urlencode "transactionCurrency=SGD" \
        --data-urlencode "api_version=22" \
        --data-urlencode "productinfo=Online Course" \
        --data-urlencode "firstname=Wei Ling" \
        --data-urlencode "email=weiling@example.com" \
        --data-urlencode "phone=+6591234567" \
        --data-urlencode "address1=10 Anson Road" \
        --data-urlencode "city=Singapore" \
        --data-urlencode "zipcode=079903" \
        --data-urlencode "country=SG" \
        --data-urlencode "udf1=P1007" \
        --data-urlencode "udf2=SG" \
        --data-urlencode "udf5=INV-2026-0001" \
        --data-urlencode "surl=<redacted URL>" \
        --data-urlencode "furl=<redacted URL>" \
        --data-urlencode "hash=YOUR_GENERATED_HASH"
      ```
    </Tab>
  </Tabs>

  **Expected Output:** The buyer sees PayU Hosted Checkout with the wallets for the MID currency and international cards.
</Accordion>

<Accordion title="Step 1.7: Handle the redirect response (surl / furl)" icon="fa-reply">
  After the buyer completes or abandons the wallet authorization, PayU redirects the buyer to your `surl` (success) or `furl` (failure) with the standard PayU response parameters, including `txnid`, `status`, `mihpayid`, `amount` and error details on failure.

  Before you update the order, **verify the response hash** on your server using the same MID's salt. Browser redirects can be tampered with, so never trust the `status` value alone.

  ```text
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  {/* REVIEW: Confirm the reverse hash formula for api_version 22 (whether transactionCurrency is included). */}

  **Expected Output:** The order is marked paid only when the reverse hash matches and `status=success`.
</Accordion>

<Accordion title="Step 1.8: Handle the webhook" icon="fa-bell">
  PayU sends an HTTP POST to your registered webhook URL when the final payment result is available. The notification includes:

  - `txnid`: your transaction ID from the request.
  - `status`: `success` or `failure`.
  - `mihpayid`: PayU's transaction reference.
  - `amount`, `net_amount_debit`, `transactionCurrency`.
  - `error_code` and `error_message` (on failure).

  <Callout icon="❗️" theme="error">
    ### **Critical Rules**

    - Return HTTP `200` quickly. PayU retries the notification on a non-200 response or a timeout.
    - Process notifications idempotently, using `txnid` as the deduplication key.
    - Treat the webhook (or a successful Verify Payment call) as the source of truth for the final status.
  </Callout>
</Accordion>

<Accordion title="Step 1.9: Verify the payment if the webhook doesn't arrive" icon="fa-magnifying-glass">
  <Verify_Payment_Tabs />


</Accordion>

### Common failure scenarios

| Scenario                                               | What happens                                                          | What you should do                                                     |
| :----------------------------------------------------- | :-------------------------------------------------------------------- | :--------------------------------------------------------------------- |
| Wallet provider is unavailable or declines the payment | The payment fails; no funds are captured                              | Show the failure page and let the buyer retry or choose another method |
| Buyer abandons the wallet page or fails authentication | The payment fails; buyer returns to `furl`; a failure webhook is sent | Offer a retry with a **new** `txnid`                                   |
| MID key and `transactionCurrency` don't match          | The payment fails                                                     | Map each currency to the correct MID key and salt                      |
| `country` is `IN`, or remitter details are missing     | Settlement is rejected or held, even if checkout succeeded            | Validate buyer details before posting the request                      |
| Wallet not shown on checkout                           | The wallet isn't supported or activated on that MID currency          | Contact PayU Support to review the MID wallet configuration            |

***

## Step 2: Test Integration

<Accordion title="Step 2.1: Test a successful wallet payment" icon="fa-thumbs-up">
  1. Post a request to `https://test.payu.in/_payment` with your test MID key for SGD and `transactionCurrency=SGD`.
  2. Confirm the checkout shows GrabPay and international cards.
  3. Complete the wallet authorization.
  4. Confirm you land on `surl`, the reverse hash matches, and your webhook receives `status=success`.

{/* REVIEW: Confirm test wallet credentials or a simulator for GrabPay and Touch 'n Go in the test environment. */}

</Accordion>

<Accordion title="Step 2.2: Test failure and cancellation" icon="fa-triangle-exclamation">
  1. Abandon the wallet page and confirm you land on `furl` and receive a failure webhook.
  2. Retry with a new `txnid` and confirm the first `txnid` isn't reused.
  3. Send the SGD key with `transactionCurrency=MYR` and confirm the payment fails.
</Accordion>

<Accordion title="Step 2.3: Test your validation and fallbacks" icon="fa-circle-check">
  1. Confirm your website blocks buyers with `country=IN` from this payment option.
  2. Confirm every request carries `firstname`, `address1`, `zipcode` and `country`.
  3. Send the same webhook twice and confirm your order is updated only once.
  4. Disable your webhook endpoint and confirm your Verify Payment polling marks the order correctly.
</Accordion>

***

## Step 3: Go-Live Checklist

<Accordion title="Step 3.1: Switch to production" icon="fa-key">
  - Replace test keys and salts with the **production key and salt for each currency MID**.
  - Change the payment URL to `https://secure.payu.in/_payment`.
  - Register your production webhook URL with PayU.
</Accordion>

<Accordion title="Step 3.2: Final verification" icon="fa-clipboard-check">
  - ✅ Each currency maps to its own MID key and salt.
  - ✅ INR prices are converted to FCY before the request.
  - ✅ `transactionCurrency`, `firstname`, `address1`, `zipcode` and `country` are sent on every request; `country` is never `IN`.
  - ✅ Purpose code (`udf1`) and service utilization country (`udf2`) are set as agreed at onboarding.
  - ✅ Hash is generated on the server; salt is never exposed in the browser.
  - ✅ Reverse hash is verified on `surl` and `furl`.
  - ✅ Webhooks are idempotent on `txnid`, with Verify Payment as a fallback.
  - ✅ One low-value live transaction completes end to end, and you receive the settlement and eFIRA.
</Accordion>

***

## Settlement and eFIRA

PayU settles the proceeds to your Indian bank account in INR. The foreign currency is converted to INR at the prevailing daily rate, which includes the bank's margin.

| Stage                                                             | Typical duration                                      |
| :---------------------------------------------------------------- | :---------------------------------------------------- |
| Wallet collections remitted to PayU's AD bank in foreign currency | Up to T+6 business days                               |
| Conversion to INR                                                 | T+1 after the foreign currency is received            |
| PayU settlement to you                                            | As per your settlement cycle, confirmed at onboarding |

{/* REVIEW: Source doc says "up to T+6" in the table but "T+5 collection period" in the FAQ. Confluence (PACB Exports Go-Live) says T+5. Confirm one value. */}

From buyer payment to INR in your account typically takes **7 to 10 business days**. You can see exact settlement dates on the PayU Dashboard.

An **eFIRA** (electronic Foreign Inward Remittance Advice) is issued for each settled transaction. It's your documentary proof that export proceeds were received, required for RBI compliance and for claiming GST zero-rating on export of services. Keep it with your export records for the statutory period.

{/* REVIEW: Source doc says PayU generates and shares the eFIRA; Confluence (PACB Exports Go-Live) says for P0 it is generated by HDFC and emailed to the merchant. Confirm who sends it and how. */}

***

## Refunds and disputes

\- **Refunds** are made in the original currency, in full or in part. {/* REVIEW: Refunds aren't covered in the source doc. Confluence says full and partial refunds in the buyer's currency can be triggered from the dashboard. Confirm whether the standard refund API also supports exports. */}
\- **Disputes:** The wallets in scope don't have a card-style chargeback process. Disputes are resolved through refunds. If a buyer's dispute is upheld by their wallet provider, the refund amount is recovered from your future settlements, and PayU notifies you of the deduction.
\- Keep records of service delivery as evidence in case of a dispute.

***

## FAQs

<Accordion title="Do I need to integrate with each wallet provider?" icon="fa-circle-question">
  No. You integrate with PayU only. PayU manages the wallet connections, and you don't call any wallet API directly.
</Accordion>

<Accordion title="How many MIDs do I need?" icon="fa-circle-question">
  One MID per currency you want to accept. Each MID has its own key and salt, and your server must pick the right one for each transaction.
</Accordion>

<Accordion title="Can I use one MID for several currencies?" icon="fa-circle-question">
  No. Each MID supports one currency. Sending a different currency from the one the MID is configured for makes the payment fail.
</Accordion>

<Accordion title="Who converts the amount from INR?" icon="fa-circle-question">
  You do. Send the amount in the buyer's currency. PayU doesn't convert INR to foreign currency at checkout.
</Accordion>

<Accordion title="Can a buyer from India use this product?" icon="fa-circle-question">
  No. Export payments must come from foreign residents. A buyer country of India is rejected at settlement, so block Indian-resident buyers from this option.
</Accordion>

<Accordion title="Does this replace international cards?" icon="fa-circle-question">
  No. The wallets are additive. They appear alongside international cards on PayU Hosted Checkout.
</Accordion>

<Accordion title="What if a wallet isn't showing on the checkout?" icon="fa-circle-question">
  The wallets shown depend on the MID currency and what PayU has activated on that MID. Contact PayU Support to review the MID's wallet configuration.
</Accordion>

***

## Next Steps

<Cards columns="3">
  <Card title="Payment API Reference" href="/reference/cross-border-exports-payment-api">
    All request and response parameters
  </Card>

  <Card title="Verify Payment API" href="/reference/verify-payment-api">
    Confirm the transaction status from your server
  </Card>

  <Card title="Webhooks" href="/docs/webhooks">
    Set up and secure payment notifications
  </Card>
</Cards>