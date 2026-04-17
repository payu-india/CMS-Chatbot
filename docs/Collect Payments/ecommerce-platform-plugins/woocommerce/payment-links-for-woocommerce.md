---
title: 'Payment Links for WooCommerce '
deprecated: false
hidden: true
metadata:
  robots: index
---
## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Installation](#2-installation)
3. [Configuration](#3-configuration)
4. [Webhook Setup](#4-webhook-setup)
5. [Creating a Payment Link](#5-creating-a-payment-link)
6. [Sharing a Payment Link](#6-sharing-a-payment-link)
7. [Tracking Payment Links](#7-tracking-payment-links)
8. [Exporting Reports](#8-exporting-reports)
9. [Refunds](#9-refunds)
10. [Status Reference](#10-status-reference)
11. [Restrictions and Important Notes](#11-restrictions-and-important-notes)
12. [Go-Live Checklist](#12-go-live-checklist)

***

## 1. Prerequisites

Before installing the plugin, ensure you have:

| Requirement               | Details                                                                         |
| ------------------------- | ------------------------------------------------------------------------------- |
| **WordPress**             | Version 5.9 or higher                                                           |
| **WooCommerce**           | Version 7.0 or higher (tested up to 10.5.x)                                     |
| **PHP**                   | Version 7.4 or higher                                                           |
| **PayU Merchant Account** | Active account with Payment Links enabled                                       |
| **SSL Certificate**       | Your site must be on HTTPS (required for webhooks and secure API communication) |

### PayU Credentials You Will Need

Obtain the following from your [PayU Dashboard](https://dashboard.payu.in):

| Credential            | Where to find        | Used for                                       |
| --------------------- | -------------------- | ---------------------------------------------- |
| **Client ID**         | Dashboard → API Keys | OAuth authentication for Payment Links APIs    |
| **Client Secret**     | Dashboard → API Keys | OAuth authentication for Payment Links APIs    |
| **Merchant ID (MID)** | Dashboard → Profile  | API request headers                            |
| **Merchant Key**      | Dashboard → API Keys | Settlement API and Refund API authentication   |
| **Salt**              | Dashboard → API Keys | Hash generation for Settlement and Refund APIs |

> **Don't have a PayU account?** Click the "Create PayU Account" button in the plugin settings to sign up.

### For Multi-Currency Merchants

If you accept payments in multiple currencies (e.g., INR and USD), you need **separate credentials for each currency**. Each currency requires its own MID, Client ID, Client Secret, Merchant Key, and Salt.

***

## 2. Installation

### Step 1: Upload the Plugin

1. Log in to your WordPress admin panel
2. Navigate to **Plugins → Add New → Upload Plugin**
3. Click **Choose File** and select the `payu-payment-links-woocommerce.zip` file
4. Click **Install Now**
5. Click **Activate Plugin**

### Step 2: Verify Activation

After activation, confirm:

* No error messages appear
* Two new items appear under **WooCommerce** in the sidebar:
  * **PayU Create Link** — for creating manual/standalone payment links
  * **Payment Links** — for viewing and managing all payment links
* The database tables `wp_payu_payment_links` and `wp_payu_payment_link_events` are available (created on first install and reused on reinstall)

### Troubleshooting Activation Issues

| Issue                           | Solution                                                        |
| ------------------------------- | --------------------------------------------------------------- |
| "WooCommerce is required" error | Install and activate WooCommerce first                          |
| White screen after activation   | Enable WP_DEBUG in wp-config.php and check wp-content/debug.log |
| Menu items missing              | Deactivate and reactivate the plugin                            |

***

## 3. Configuration

Navigate to **WooCommerce → Settings → PayU Payment Links** tab.

### 3.1 Basic Settings

| Setting           | Description                                                | Recommended Value                                                 |
| ----------------- | ---------------------------------------------------------- | ----------------------------------------------------------------- |
| **Environment**   | Test (UAT) for testing, Production for live                | Start with Test (UAT), switch to Production after go-live testing |
| **Client ID**     | OAuth Client ID from PayU Dashboard                        | —                                                                 |
| **Client Secret** | OAuth Client Secret from PayU Dashboard                    | —                                                                 |
| **Merchant ID**   | Your PayU MID (used in API headers)                        | —                                                                 |
| **Merchant Key**  | Required for Settlement API (UTR retrieval) and Refund API | —                                                                 |
| **Salt**          | Required for hash generation in Settlement and Refund APIs | —                                                                 |

### 3.2 Payment Link Defaults

| Setting                        | Description                                                                                 | Default   |
| ------------------------------ | ------------------------------------------------------------------------------------------- | --------- |
| **Allow partial payment**      | Lets customers pay less than the full amount                                                | Unchecked |
| **Order status after payment** | WooCommerce order status when payment succeeds                                              | Completed |
| **Default link expiry (days)** | How many days until a link expires (1–365). Can be overridden per link.                     | 7         |
| **Description prefix**         | Text prepended to the auto-generated link description. E.g., "Order" produces "Order #1234" | Order     |

> **Per-link override:** The global **Allow partial payment** setting is only the default.  
> While creating a link (from the order panel or manual link page), you can explicitly check/uncheck **Allow partial payment** for that specific link.

### 3.3 Multi-Currency Configuration

If you accept payments in multiple currencies, scroll to the **Multi-currency credentials** section.

In the **Currency credentials** textarea, add one line per currency in this exact format:

```
CURRENCY,MERCHANT_ID,CLIENT_ID,CLIENT_SECRET,MERCHANT_KEY,SALT
```

**Example:**

```
INR,8406928,abc123client,xyz789secret,k0g8PG,LTVYALHKekKs
USD,9501234,def456client,uvw012secret,m2h9QR,NMWZBOILflLt
```

> **Important:** When multi-currency credentials are configured, they override the single credential fields above for the matching currency.

### 3.4 Save Changes

Click **Save changes** at the bottom of the page. The plugin will validate and store your credentials.

***

## 4. Webhook Setup

Webhooks allow PayU to notify your WooCommerce store when a payment is completed or fails. Without webhooks, payment status and order status will not update automatically.

### 4.1 Your Webhook URL

Your webhook URL is:

```
https://your-site.com/?payu_payment_link_webhook=1
```

Replace `your-site.com` with your actual domain. For example:

```
https://store.example.com/?payu_payment_link_webhook=1
```

### 4.2 Register in PayU Dashboard

1. Log in to your [PayU Dashboard](https://dashboard.payu.in)
2. Navigate to **Settings → Webhooks** (or contact PayU support for webhook configuration)
3. Add your webhook URL
4. Select the relevant payment events (payment success, payment failure)
5. Save the configuration

### 4.3 Webhook Signature Verification

Webhook signatures are verified using your configured **Merchant Key** and **Salt**.

1. Ensure Merchant Key and Salt are correctly configured in **WooCommerce → Settings → PayU Payment Links**
2. The plugin verifies SHA-512 signature on each incoming webhook

> If Merchant Key/Salt are unavailable and "I don't have Merchant Key & Salt" mode is enabled, webhook verification is skipped and status updates rely on polling.

### 4.4 What the Webhook Does

When PayU sends a webhook to your URL:

| PayU Status             | Plugin Action                                                                                                                                                  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `success` or `credited` | Compares collected amount vs order amount; marks payment as **paid** (full) or **partially_paid** (partial), then updates WooCommerce order status accordingly |
| Any other status        | Marks payment link as **failed**, updates WooCommerce order to **Failed**                                                                                      |

***

## 5. Creating a Payment Link

### 5.1 From an Order (Recommended)

This is the standard flow for B2B invoicing.

#### Step 1: Create a WooCommerce Order

1. Go to **WooCommerce → Orders → Add order**
2. Add a customer (optional)
3. Click **Add item(s)** and add products
4. Click **Recalculate** to update the total
5. Click **Create** to save the order

#### Step 2: Generate the Payment Link

**Option A: Using Order Actions (quickest)**

1. In the order edit screen, find the **Order actions** dropdown (top-right)
2. Select **"Generate PayU payment link"**
3. Click the blue arrow button (▶) or **Update**
4. The link is created using the default currency and expiry

**Option B: Using the PayU Payment Link Panel (more control)**

1. In the sidebar, find the **PayU Payment Link** panel
2. Select your desired **Currency** from the dropdown
3. Set an **Expiry date** (defaults to today + configured days)
4. Set **Allow partial payment** for this link (pre-filled from global default, but can be changed)
5. Click **Generate new link**

#### Step 3: Verify

After generation, the PayU Payment Link panel shows:

* Payment link URL (with a Copy button)
* Invoice number (PayU's reference)
* Amount and currency
* Link status: **active**
* Payment status: **pending**

### 5.2 Manual / Standalone Link

For creating a payment link without an existing order (or attaching to an existing order later):

1. Go to **WooCommerce → PayU Create Link**
2. Fill in:
   * **Amount** (required)
   * **Currency** (select from configured currencies)
   * **Description** (e.g., "Invoice #ABC-123")
   * **Expiry date**
   * **Allow partial payment for this link** (pre-filled from global default, but can be changed)
   * **Customer email** (optional)
   * **Customer phone** (optional)
   * **Attach to order** (optional — select an existing order or leave as "None")
3. Click **Create payment link**
4. Copy the generated link

### 5.3 Rules and Restrictions for Link Creation

| Rule                          | Details                                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **One active link per order** | You cannot create a new link while an active link exists for the same order. Expire the active link first. |
| **Completed orders**          | Link creation is disabled for orders with status "Completed"                                               |
| **Refunded orders**           | Link creation is disabled for orders with status "Refunded"                                                |
| **Zero-total orders**         | The order must have a positive total. Add items and recalculate before generating.                         |
| **Credentials required**      | At least one currency must be configured with valid credentials                                            |

***

## 6. Sharing a Payment Link

### 6.1 Copy and Share Manually

1. Click the **Copy** button next to any payment link
2. Paste the URL into your preferred channel:
   * Email (Gmail, Outlook, etc.)
   * WhatsApp
   * SMS
   * Any messaging platform

### 6.2 Share via the Plugin (Email)

1. In the order's **PayU Payment Link** panel, click **Share** on the active link
2. Enter one or more **email addresses** (comma-separated)
3. Click **Send**
4. A success or failure message appears immediately
5. The "Shared to" information is recorded and displayed on the link card

> **Note on PayU Share API:** The plugin attempts to use PayU's native Share API first. If unavailable (currently the case on UAT), it falls back to sending email via WordPress. The sharing works reliably for email recipients.

### 6.3 Resending from the Payment Links List

1. Go to **WooCommerce → Payment Links**
2. Find the link row and click **Resend**
3. Enter recipient email(s) in the prompt
4. Click OK

***

## 7. Tracking Payment Links

### 7.1 Payment Links List

Navigate to **WooCommerce → Payment Links**

1. Set the **From** and **To** date range
2. Click **Filter**

The table displays all payment links created in that date range:

| Column          | Description                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------- |
| **Invoice**     | PayU's invoice number (e.g., WC161L4081). Contains the WooCommerce order ID.                        |
| **Order**       | Linked WooCommerce order number. Click to open the order. Shows "—" for standalone links.           |
| **Amount**      | Payment amount in major currency units (e.g., 6,000.00)                                             |
| **Currency**    | Currency code (e.g., INR, USD)                                                                      |
| **Link Status** | Status of the payment link itself: `active` (usable), `expired` (no longer usable)                  |
| **Payment**     | Payment status: `pending`, `partially_paid`, `paid`, `failed`, `refunded`, `partially_refunded`     |
| **Refund**      | Refund amount if a refund was initiated. Shows "NA" when no refund exists.                          |
| **Created**     | Date and time the link was created                                                                  |
| **Expiry**      | Date and time the link expires                                                                      |
| **UTR**         | Unique Transaction Reference number for bank settlement reconciliation. Populated after settlement. |
| **Actions**     | View (detail page), Copy, Resend (share), Refresh (fetch latest status from PayU)                   |

### 7.2 Detail View

Click **View** on any link to see the full snapshot:

* All fields from the list view
* PayU Transaction ID
* UDF1 (WooCommerce Order ID — for audit)
* UDF5 (Source identifier — always "WooCommerce_paymentlink")
* Refund amount, Refund request ID, Refund status
* Customer email, phone, name
* Last shared to and when

### 7.3 Syncing Statuses from PayU

Click **Sync statuses from PayU** on the list page to bulk-refresh all link statuses for the displayed date range. This calls PayU's Get All Payment Links API and updates any links whose status has changed.

### 7.4 Refreshing a Single Link

Click **Refresh** on any row to fetch the latest status from PayU for that specific link. This updates both the link status and payment status.

> **Important:** PayU expires payment links after a successful payment. So a "paid" link will typically show Link Status: **expired** + Payment: **paid**. This is normal — the link served its purpose.

***

## 8. Exporting Reports

### 8.1 CSV Export

1. Go to **WooCommerce → Payment Links**
2. Set the desired date range and click **Filter**
3. Click **Export CSV**

The CSV file contains the following columns:

| Column         | Description                                                              |
| -------------- | ------------------------------------------------------------------------ |
| Invoice        | PayU invoice number                                                      |
| Order ID       | WooCommerce order ID (empty for standalone links)                        |
| Amount         | Payment amount in major currency units                                   |
| Currency       | Currency code                                                            |
| Link Status    | active / expired                                                         |
| Payment Status | pending / partially_paid / paid / failed / refunded / partially_refunded |
| Refund Amount  | Amount refunded (0.00 if none)                                           |
| Created        | Creation timestamp                                                       |
| Expiry         | Expiry timestamp                                                         |
| UTR Number     | Bank settlement UTR (empty until settled)                                |
| Shared To      | Last shared recipients                                                   |
| Shared At      | Last share timestamp                                                     |
| Customer Email | Customer email address                                                   |
| Payment Link   | Full payment link URL                                                    |

### 8.2 Use Cases for Export

* **Reconciliation:** Match UTR numbers against bank statements
* **Accounting:** Import into accounting software
* **Audit:** Track all payment links with UDF fields and timestamps
* **Customer support:** Look up payment link status for a specific order

***

## 9. Refunds

### 9.1 Initiating a Refund

The plugin supports both full and partial refunds through PayU's Refund Transaction API.

#### Step 1: Open the Order

1. Go to **WooCommerce → Orders**
2. Open the order that has a paid payment link

#### Step 2: Click Refund

1. In the **PayU Payment Link** panel, find the paid link
2. Click the **Refund** button (appears only when payment status is "paid")

#### Step 3: Enter the Amount

1. A refund form appears with the amount pre-filled to the maximum refundable amount
2. For a **full refund:** leave the amount as-is
3. For a **partial refund:** enter a smaller amount (e.g., 3000.00 out of 6000.00)
4. Click **Confirm refund**

#### Step 4: Confirmation

A confirmation dialog asks: "Initiate refund of [amount]? This will process through PayU and cannot be undone."

Click OK to proceed.

### 9.2 Refund Status Lifecycle

After initiating a refund, it goes through these states:

```
Refund initiated
  ↓
QUEUED (accepted by PayU, not yet sent to bank)
  ↓
IN PROGRESS (sent to bank for processing)
  ↓
SUCCESS → Order & link marked as Refunded
   or
FAILURE → Refund failed, order remains unchanged (note added)
```

| Refund Status   | Description                                                  | What Happens                                                                                                 |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| **queued**      | PayU accepted the request but hasn't sent it to the bank yet | Order: On Hold. Link: shows yellow "queued" badge                                                            |
| **in_progress** | Refund raised to bank for processing                         | Order: On Hold. Link: shows yellow badge                                                                     |
| **requested**   | Sent to bank for offline processing (5–7 business days)      | Order: On Hold                                                                                               |
| **pending**     | Overdraft occurred / insufficient funds (5–7 business days)  | Order: On Hold                                                                                               |
| **success**     | Refund processed successfully                                | Full refund → Order: Refunded, Link: refunded. Partial → Order: Partially Refunded, Link: partially_refunded |
| **failure**     | Refund processing failed. No funds deducted.                 | Order status remains unchanged (typically On Hold until reviewed), note added                                |

### 9.3 Checking Refund Status

Refund statuses are updated automatically via:

* **Hourly cron job:** The plugin polls PayU every hour for all pending refunds
* **Manual check:** Click the **Check refund** button on the link card (appears when a refund is in progress)

### 9.4 Multiple Partial Refunds

You can initiate multiple partial refunds on the same link until the full amount is refunded. Each refund is tracked cumulatively.

**Example:**

* Original amount: INR 6,000.00
* First partial refund: INR 2,000.00 → Payment status: **partially_refunded**
* Second partial refund: INR 4,000.00 → Payment status: **refunded** (total equals original)

### 9.5 Refund Restrictions

| Restriction                        | Details                                                                                            |
| ---------------------------------- | -------------------------------------------------------------------------------------------------- |
| **PayU Transaction ID required**   | Refund can only be initiated if the link has a PayU Transaction ID (set by the webhook on payment) |
| **Cannot exceed original amount**  | Total refunds cannot exceed the original payment amount                                            |
| **Merchant Key and Salt required** | The Refund API uses the same authentication as the Settlement API                                  |
| **Cannot undo a refund**           | Once initiated, a refund cannot be reversed                                                        |

***

## 10. Status Reference

### 10.1 Link Status (PayU Payment Link)

| Status      | Meaning                                                  | Can customer pay? |
| ----------- | -------------------------------------------------------- | ----------------- |
| **active**  | Link is live and usable                                  | Yes               |
| **expired** | Link has passed its expiry date or payment was completed | No                |

### 10.2 Payment Status (Payment Outcome)

| Status                 | Meaning                                    |
| ---------------------- | ------------------------------------------ |
| **pending**            | Link created, awaiting customer payment    |
| **partially_paid**     | Customer has paid part of the order amount |
| **paid**               | Customer completed the payment             |
| **failed**             | Payment attempt failed                     |
| **partially_refunded** | Part of the payment has been refunded      |
| **refunded**           | Full payment amount has been refunded      |

### 10.3 WooCommerce Order Status

| Order Status           | When it's set                                                              |
| ---------------------- | -------------------------------------------------------------------------- |
| **Pending payment**    | Order created, no payment link or payment pending                          |
| **Partially Paid**     | Partial payment received for a payment link; full amount not yet collected |
| **On hold**            | Refund has been initiated and is being processed                           |
| **Completed**          | Payment confirmed via webhook (default setting)                            |
| **Processing**         | Payment confirmed via webhook (if configured)                              |
| **Refunded**           | Full refund confirmed by PayU                                              |
| **Partially Refunded** | Partial refund confirmed by PayU (custom status added by this plugin)      |
| **Failed**             | Payment failed                                                             |

### 10.4 Refund Status (PayU)

| Status          | Meaning                                            |
| --------------- | -------------------------------------------------- |
| **queued**      | Accepted by PayU, not yet sent to bank             |
| **in_progress** | Sent to bank for processing                        |
| **requested**   | Sent for offline processing (5–7 business days)    |
| **pending**     | Overdraft / insufficient funds (5–7 business days) |
| **success**     | Refund completed successfully                      |
| **failure**     | Refund failed — no funds deducted                  |

***

## 11. Restrictions and Important Notes

### General

* **One active payment link per order.** You must expire an existing active link before creating a new one for the same order.
* **Payment links expire after payment.** This is normal PayU behavior. A paid link will show Link Status: expired + Payment: paid.
* **All plugin-created links are tagged** with `udf5 = WooCommerce_paymentlink` for identification in PayU's dashboard.
* **WooCommerce order ID is stored** in `udf1` on every link for audit and reconciliation.
* **Collected paid amount is persisted** per link and synced to WooCommerce order metadata (`_payu_paid_amount`) for partial/full payment reconciliation.
* **Plugin data persists across deactivate/delete/reinstall.** Existing PayU link/payment/refund mappings are retained and reused on reinstall.

### Multi-Currency

* One MID supports only one currency.
* To accept multiple currencies, configure separate credentials per currency.
* The currency is selected at the time of link creation and cannot be changed afterward.

### Webhook

* **Webhooks are required** for automatic payment status updates. Without webhooks, you must manually refresh link statuses.
* Your site must be **publicly accessible** from PayU's servers (not behind a VPN or firewall that blocks external traffic).
* If using a staging/local environment, use a tool like [ngrok](https://ngrok.com) to expose your site.

### Settlement and UTR

* UTR numbers are fetched via a **daily automated job** (WP-Cron). They are not available immediately after payment — they depend on PayU's settlement cycle.
* The Merchant Key and Salt must be configured for UTR retrieval and refunds.
* The Settlement API has a maximum date range of 3 days. The plugin handles this automatically.

### Refunds

* Refunds require a **PayU Transaction ID**, which is set when the payment webhook is received. If no webhook was received, you cannot refund through the plugin.
* Refund processing time depends on the bank (immediate to 5–7 business days).
* The **hourly cron job** checks refund statuses automatically. Ensure WP-Cron is running reliably (consider setting up a real cron job if you have high volume).

### Share API

* The PayU Share Payment Link API may not be available on UAT environments. The plugin falls back to sending email via WordPress when the API is unavailable.
* Phone/SMS sharing via PayU requires the Share API to be functional. Use copy + paste for SMS/WhatsApp in the meantime.

***

## 12. Go-Live Checklist

Complete this checklist before switching from UAT to Production.

### 12.1 Pre-Go-Live Testing (on UAT)

* [ ] **Settings saved without errors.** All credential fields filled. "Create PayU Account" button visible.
* [ ] **Create a test order** with at least one product (positive total).
* [ ] **Generate a payment link** from the order's PayU Payment Link panel.
* [ ] **Copy the link** and open it in a browser — confirm the PayU hosted payment page loads with the correct amount and currency.
* [ ] **Complete a test payment** using PayU test cards/credentials.
* [ ] **Verify the webhook fires:**
  * Order status changes to Completed (or your configured status)
  * Payment link shows Payment: **paid** in the order panel
  * Payment Links list shows the updated status
* [ ] **Test sharing:** Click Share, enter an email, click Send. Confirm the email is received.
* [ ] **Test CSV export:** Click Export CSV. Open the file and verify all columns are present and data is correct.
* [ ] **Test manual/standalone link creation** via WooCommerce → PayU Create Link.
* [ ] **Test expiry:** Click Expire on an active link. Confirm the link is marked expired and the Generate button becomes available again.
* [ ] **Test refund (if applicable):**
  * Initiate a partial refund on a paid link
  * Click "Check refund" to poll status
  * Confirm payment status updates to "partially_refunded"
  * Initiate a second refund for the remaining amount
  * Confirm payment status updates to "refunded" and order status changes to "Refunded"

### 12.2 Switch to Production

1. Go to **WooCommerce → Settings → PayU Payment Links**
2. Change **Environment** to **Production**
3. Update all credentials with your **production** Client ID, Client Secret, Merchant ID, Merchant Key, and Salt
4. If using multi-currency, update the Currency credentials textarea with production values
5. Click **Save changes**

### 12.3 Post-Go-Live Verification

* [ ] **Webhook URL updated** in PayU Production Dashboard to point to your live site
* [ ] **Create a real order** and generate a payment link
* [ ] **Complete a real payment** (small amount recommended for initial test)
* [ ] **Verify order status updates** automatically via webhook
* [ ] **Verify the link appears** in WooCommerce → Payment Links
* [ ] **Test Copy** and manually share the link via email or WhatsApp
* [ ] **Test CSV export** with the real data
* [ ] **Monitor for 24 hours** — check that the daily UTR cron runs and populates UTR numbers for settled transactions

### 12.4 Ongoing Monitoring

* Check **WooCommerce → Payment Links** regularly to ensure statuses are up to date
* Use **Sync statuses from PayU** if you suspect statuses are stale
* Monitor the **Order notes** on individual orders for webhook activity
* If WP-Cron is unreliable (low-traffic sites), set up a system cron:

```bash
# Add to your server's crontab (runs every 15 minutes):
*/15 * * * * wget -q -O - https://your-site.com/wp-cron.php?doing_wp_cron > /dev/null 2>&1
```

***

## Support

* **PayU API Documentation:** [https://docs.payu.in](https://docs.payu.in)
* **Plugin Issues:** Contact your development team or refer to the TESTING.md file included with the plugin
* **PayU Support:** For API errors, credential issues, or webhook configuration, contact PayU merchant support through your dashboard
