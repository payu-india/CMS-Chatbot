---
title: '[Internal Review]PayU Credentials Security — Rotation and Compromise Response'
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section covers PayU credential types, what to do if credentials are exposed, how to rotate your salt, and best practices for preventing accidental exposure.

***

## Overview of PayU Credentials

| Credential        | Purpose                                              | Client-Safe? | Notes                                                                             |
| ----------------- | ---------------------------------------------------- | ------------ | --------------------------------------------------------------------------------- |
| **Merchant Key**  | Identifies your merchant account in payment requests | ✅ Yes        | Safe to include in client-side HTML forms and front-end code                      |
| **Salt**          | Signs payment requests via SHA-512 hash              | ❌ No         | **Must never be exposed client-side.** Used only server-side for hash computation |
| **Client ID**     | OAuth 2.0 identifier for v2 APIs                     | ❌ No         | Treat like a username for API access                                              |
| **Client Secret** | OAuth 2.0 secret for v2 APIs                         | ❌ No         | Treat like a password — keep strictly server-side                                 |

All credentials are **environment-specific**. Your test environment key, salt, Client ID, and Client Secret are completely different from your production credentials. Never mix them.

> 📘 **Note:** The Merchant Key being "client-safe" does not mean it has no value to an attacker on its own. Without the Salt, an attacker cannot forge valid payment hashes, but the Key alone can be used to probe your integration. Always keep the Salt secret.

***

## What to Do If Credentials Are Exposed

If you believe your Salt, Client Secret, or any PayU credential has been exposed (committed to a public repository, logged, sent via email, etc.), follow these steps immediately:

### Step 1 — Contact PayU immediately

Email **[integration@payu.in](mailto:integration@payu.in)** or call your KAM with the subject line:

```
URGENT: Credential Compromise — MID [your MID]
```

Include:

- Your Merchant ID (MID)
- Which credential was exposed (salt, client secret, etc.)
- Which environment (test or production)
- How it was exposed and when you discovered it

### Step 2 — Request immediate salt rotation

Ask PayU to rotate (regenerate) your Salt. Once rotated, all requests using the old Salt will immediately fail. This limits the window of exposure.

### Step 3 — Prepare your application before rotation

> ⚠️ **Note:** Salt rotation takes effect immediately. If you rotate the salt before updating your application, **all payment requests will fail** until the application is updated. Coordinate the rotation timing carefully.

Update your application's salt configuration with the new salt value **before** requesting the rotation to go live in production. Use a feature flag or configuration hot-reload if possible to minimise downtime.

### Step 4 — Handle the public repository case

If credentials were committed to a public Git repository:

1. **Assume the credentials are already compromised.** Repository clones, GitHub's cached views, and automated scrapers capture credentials within minutes of a public commit.
2. **Rotate credentials before or simultaneously with any commit history cleanup.** Removing a commit or force-pushing does not retroactively protect credentials that were already public.
3. Remove the credentials from the repository history using `git filter-repo` or BFG Repo Cleaner.
4. Rotate the salt as described above — removing from history alone is not sufficient.

### Step 5 — Audit recent transactions

After rotation, review recent transactions in your PayU Dashboard for any suspicious activity:

- Transactions you did not initiate
- Unusual amounts, product descriptions, or customer details
- Payment attempts from unexpected IP addresses

Report any suspicious transactions to PayU support immediately.

### Step 6 — Review server logs

Check your application and web server logs for:

- Unexpected API calls using your merchant key
- Hash verification failures before the exposure date (which may indicate earlier probing)
- Requests from IPs not associated with your application servers

***

## How to Rotate Your Salt

### Self-serve rotation (if available)

1. Log in to the **PayU Dashboard**.
2. Navigate to **Developer** → **API Keys**.
3. Look for a **"Regenerate Salt"** button next to your Salt value.
4. If available, click it — you will be prompted to confirm.
5. The new salt is shown once — copy it immediately and store it securely.

> 📘 **Note:** Not all merchant accounts have self-serve salt rotation. If the option is not visible, contact your KAM or raise a support ticket.

### Manual rotation (via KAM/support)

If self-serve rotation is not available:

1. Contact your KAM or email [integration@payu.in](mailto:integration@payu.in).
2. Request a Salt rotation for your MID.
3. Specify which environment (UAT / Production / both).
4. PayU will provide the new salt and coordinate the rotation timing with you.

### After rotation

- The old salt stops working immediately upon rotation.
- Update your application's environment variable or secrets manager entry.
- Test a payment request end-to-end to confirm the new salt is working.
- Test environment salt can be rotated independently of production.

***

## Preventing Credential Exposure

### Never hardcode credentials

```javascript
// ❌ WRONG — never do this
const salt = "4edc5d27f0eb4b453e530877100b2eb6";

// ✅ CORRECT — read from environment variable
const salt = process.env.PAYU_SALT;
```

### Always compute hashes server-side

The hash **must** be computed on your server, not in the browser. A client-side hash computation necessarily exposes the Salt to anyone who inspects the JavaScript.

```
Browser → (params without hash) → Your server → (compute hash with Salt) → PayU
```

Never send the Salt to the browser. Never compute the hash in front-end JavaScript.

### Use a secrets manager

For production systems, store the Salt and Client Secret in a dedicated secrets manager rather than in environment variable files:

- **AWS:** AWS Secrets Manager or AWS Parameter Store
- **GCP:** Google Secret Manager
- **Azure:** Azure Key Vault
- **Self-hosted:** HashiCorp Vault

### Add `.env` to `.gitignore` before the first commit

```bash
echo ".env" >> .gitignore
git add .gitignore
git commit -m "Add .env to gitignore"
```

Adding `.gitignore` entries after a file has already been committed does **not** remove it from history. Add it before you ever commit the `.env` file.

### Enable automated secret scanning

Use automated tooling to detect accidental credential exposure:

- **GitHub:** Enable Secret Scanning in repository Settings → Security → Code security. GitHub will alert you if recognised credential patterns are detected.
- **GitLab:** Enable Secret Detection in your CI pipeline.
- **Pre-commit hooks:** Use `detect-secrets` or `gitleaks` as a pre-commit hook to block commits containing secrets.

### Rotate credentials periodically

Even without a known compromise, rotate your Salt periodically as a security hygiene measure. Recommended rotation schedule: **every 6–12 months** for production credentials.

***

## Rate Limiting and "Too Many Requests" Error

PayU enforces rate limits on the payment endpoint to prevent abuse.

**Error message:**

> Sorry, we are unable to process your payment due to Too many Requests. Please try after 60 seconds.

### Common causes

1. **High request volume in a short window** — too many payment initiation calls from your server in rapid succession.
2. **Using production credentials against the test endpoint** (or vice versa) — this can trigger anomaly detection.
3. **Repeated failed transactions from the same IP** — multiple failures in quick succession from one source trigger temporary throttling.
4. **Duplicate&#x20;**`txnid`**&#x20;values** — reusing a transaction ID across requests.

### Resolution

- Wait **60 seconds** and retry the request.
- Ensure you are using the correct endpoint for your credentials:
  - Test credentials → `https://test.payu.in/_payment`
  - Production credentials → `https://secure.payu.in/_payment`
- Ensure each payment request uses a **unique&#x20;**`txnid`.
- If rate limiting occurs frequently in production, contact your KAM to discuss rate limit adjustments for your MID.

***

## Related Pages

- Dashboard — Developer Settings and API Keys
- Merchant Account Feature Flags — Activation Guide
- Hash Computation — Standard Payment
- SI Hash Formulas Reference

<br />