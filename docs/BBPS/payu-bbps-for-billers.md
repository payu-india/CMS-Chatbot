---
title: PayU BBPS for Billers
excerpt: >-
  Accept recurring bill payments across every consumer platform in India — with
  one integration
deprecated: false
hidden: true
metadata:
  robots: index
---

## 1. What is PayU BBPS for Billers?

Bharat Bill Payment System (BBPS) — also known as Bharat Connect — is an RBI-mandated, NPCI-operated national infrastructure for recurring bill payments. As a biller (merchant), joining BBPS means your customers can pay your bills from any app, any bank, and any channel in India — without you having to build separate integrations with each of them.

PayU holds a dual BBPS licence — both a **Biller Operating Unit (BOU)** and a **Consumer Operating Unit (COU)**. As your BOU, PayU registers your business on the BBPS network and instantly connects you to **120M+ monthly digital users** and **200M+ monthly physical-channel users** across India — all through a single API integration.

> 💡 **Why BBPS?**
> Before BBPS, every biller had to integrate individually with each consumer app and payment outlet. BBPS eliminates that entirely — one integration with PayU as your BOU opens your billing system to the entire BBPS consumer ecosystem simultaneously.

---

## 2. Is This Right for You?

PayU BBPS is the right fit for your business if:

- You collect **recurring payments** — electricity, gas, water, internet/broadband, insurance premiums, school or college fees, loan EMIs, government taxes, or subscriptions.
- You want customers to pay from **any app** — PhonePe, Paytm, bank apps, BHIM, WhatsApp — without you building separate integrations with each.
- You want **NPCI-guaranteed settlement** and a standardised dispute resolution mechanism, removing your dependence on individual payment gateway SLAs.
- You want to **cut engineering effort** — one API instead of dozens of integrations.
- You want **automated MIS reports**, a real-time transaction dashboard, and single-point reconciliation.
- You **do not have a live biller API** and prefer an offline bill data-upload model.

> ⚠️ **Consider alternatives if:**
> - You only need to accept one-time or ad-hoc payments with no recurring billing cycle.
> - Your category is **Hospitals** or **Donations** — new biller onboarding has been discontinued by NPCI (Aug 2025).
> - You are a **non-regulated entity** seeking Loan Repayment category onboarding — a Certificate of Registration from RBI/SEBI/IRDAI is mandatory for this category.

---

## 3. What You Get

When you onboard as a biller via PayU BBPS, you unlock:

- **Access to 22,000+ Live Billers' Ecosystem:** Your billing system becomes reachable and payable across the entire BBPS ecosystem — every consumer app, bank portal, and physical agent outlet in India.
- **Omni-Channel Payment Acceptance:** Customers pay your bills digitally (mobile apps, internet banking, UPI, cards) or physically through 200M+ monthly users at cash-based agent outlets — no extra integration needed.
- **Single API Integration — No Multiple Deals:** One integration with PayU (BOU) gives you access to all consumer platforms, eliminating individual negotiations and separate engineering efforts.
- **Guaranteed T+1 Settlement:** NPCI clears funds between all parties. PayU settles the collected amount directly to your bank account on T+1 — predictable, guaranteed, zero delays.
- **Automated Reconciliation & MIS Reports:** Receive automated TXT files and MIS reports on T+1. Track every transaction in real time from your PayU dashboard, including refunds, chargebacks, and complaints.
- **NPCI-Managed Dispute Resolution:** Customer complaints and refund requests are routed through NPCI's standardised grievance mechanism — significantly reducing your customer support burden.
- **Offline Biller Support — No Real-Time API Required:** Upload bill data via a secure web portal at each billing cycle. PayU handles all fetch and payment calls from an offline repository on your behalf. Bills are marked 'Paid' automatically on successful payment, preventing duplicate payments.
- **BBPS Click Pay — Push Payments to Customers:** Send pre-filled, single-click payment links to your customers via WhatsApp, SMS, or email. Customers are taken directly to a pre-populated payment screen — no searching for your biller.
- **UPMS — Autopay Mandates for Recurring Bills:** Let customers register their recurring bills once and set up autopay. Bills are fetched automatically when due and paid without manual action each cycle.
- **Business Bill Pay Platform:** For corporate billers — register and pay thousands of bills in bulk, set maker-checker approval workflows, and generate region-wise and usage reports.
- **WhatsApp as a Bill Payment Channel:** Reach 400M+ WhatsApp users via a chatbot-guided bill payment flow — customers receive a BBPS payment link in the chat with bill details pre-filled.
- **Trusted Brand Credibility:** The BBPS / Bharat Connect brand — created by RBI, driven by NPCI — signals security and reliability to your customers at every payment touchpoint.

---

## 4. How It Works

Once you are onboarded as a biller via PayU BOU, here is how a typical bill payment works for your customer — regardless of which app or channel they use.

### Standard Fetch-and-Pay Flow (e.g., Electricity, Loan EMI, School Fees)

1. **Step 1: Customer Opens Any Supported App** — Your customer opens any BBPS-enabled app (PhonePe, their bank's app, BHIM, or any Agent Institution), selects your biller category, and finds your biller name.
2. **Step 2: Customer Enters Unique Identifier** — The customer enters their unique identifier — e.g., consumer number, loan account number, student ID, or policy number — depending on your category.
3. **Step 3: Bill is Fetched from Your System** — The consumer app sends a fetch request → COU → NPCI (BBPCU) → PayU BOU → Your biller system. Your system returns bill details: amount due, due date, and any other relevant fields.
4. **Step 4: Bill Details Displayed to the Customer** — The fetched bill details travel back through the chain and are displayed on the consumer app. The customer reviews and confirms the amount.
5. **Step 5: Customer Pays** — The customer selects a payment mode (UPI, card, netbanking, wallet, or cash at an agent outlet) and completes the payment.
6. **Step 6: Payment Confirmation Sent to Your System** — The payment confirmation is posted back: COU → NPCI → PayU BOU → Your biller system. A receipt is generated and shown to the customer.
7. **Step 7: Settlement to Your Account on T+1** — NPCI clears the funds. PayU settles the net amount to your registered bank account on T+1. MIS reports and TXT files are delivered for reconciliation.

### Other Supported Transaction Flows

- **Validation & Pay:** Customer validates their identifier (e.g., broadband account) — no bill is pre-fetched. Amount may be entered manually. Common for broadband and postpaid categories.
- **Plan-Based Validation & Pay:** Customer validates identifier and selects a plan — applies to mobile prepaid and DTH recharges.
- **Offline Fetch & Pay:** For data-upload billers: PayU fetches bill details from its internal offline repository (populated by your uploaded bill data) instead of calling your live API.

---

## 5. What You Will Need (Prerequisites)

Before going live on BBPS as a biller via PayU, ensure the following are in place:

- **A PayU Merchant Account:** New to PayU? Complete PG onboarding first. Existing PayU PG merchants skip this step and proceed directly to BBPS onboarding — saving significant time.
- **Business & KYC Documents:** Standard KYC and business registration documents are required for NPCI biller registration. Exact documents vary by biller category.
- **Certificate of Registration — Loan Repayment Category Only:** A valid Certificate of Registration from the relevant regulator (RBI for NBFCs, SEBI for investment firms, IRDAI for insurers) is mandatory to onboard under the Loan Repayment category.
- **A Live Biller API — OR — Bill Data for Offline Upload:** Online billers need a REST API responding to fetch and payment posting requests. Offline billers need bill data in the agreed CSV/Excel format, ready for portal upload at each billing cycle.
- **UAT Environment Testing:** End-to-end testing — fetch, payment posting, status check, complaint registration — must be completed and verified in the UAT environment before production go-live.
- **NPCI Sign-Off:** After development and UAT, NPCI review and approval is required before your biller goes live on the BBPS network. PayU coordinates this process on your behalf.

> 💡 **Tip:** If you are already a PayU PG merchant, BBPS onboarding is significantly faster — PayU handles the NPCI biller registration as your authorised BOU, so you focus on testing and go-live, not paperwork.

---

## 6. Supported Payment Methods

Your customers can pay your bills using any of the following modes through any BBPS-enabled consumer app or physical agent outlet:

| Payment Method | Details | Status |
|---|---|---|
| 💳 Credit Cards | All major networks — Visa, Mastercard, RuPay, Amex | ✅ Active |
| 💳 Debit Cards | All major networks — Visa, Mastercard, RuPay | ✅ Active |
| 📱 UPI | Any UPI-enabled app — BHIM, PhonePe, GPay, Paytm, etc. | ✅ Active |
| 🌐 Internet Banking | All major banks' netbanking portals | ✅ Active |
| 👛 Prepaid Wallets / PPI | Supported prepaid payment instruments | ✅ Active |
| 💵 Cash (Agent Outlets) | Physical BBPS agent outlets — cash & AEPS | ✅ Active |
| ⚡ NEFT / IMPS | Disabled w.e.f. June 5, 2025 (NPCI Circular) | ❌ Disabled |

> ⚠️ **Regulatory Update — Action Required**
> NEFT and IMPS are disabled as eligible BBPS payment modes effective **June 5, 2025**, per NPCI Circular NPCI/2025-26/BBPS/003. If your existing integration routes payments via these modes, update it immediately.

---

## 7. Supported Biller Categories

BBPS supports 20+ biller categories. Active categories for onboarding as of 2025:

| Category | Includes | Status |
|---|---|---|
| Utility | Electricity, Water, Gas (Piped & LPG), Landline | ✅ Open |
| Telecom & Broadband | Mobile Postpaid, Broadband / Internet, DTH, Cable TV | ✅ Open |
| Credit Card Payments | Credit card bill payments (~2/3 of BBPS volume by value) | ✅ Open |
| Loan Repayment | EMIs — regulated entities only (Certificate of Registration mandatory) | ⚠️ Restricted |
| Insurance Premiums | Renewal premiums for all major insurers | ✅ Open |
| Education | School, college, and coaching institute fees | ✅ Open |
| Government & Municipal | Municipal tax, property tax, water tax, traffic challans | ✅ Open |
| Subscriptions | OTT / streaming services, club memberships | ✅ Open |
| Housing Societies | Maintenance charges (P2P payments restricted) | ⚠️ Restricted |
| Hospitals | New biller onboarding discontinued — NPCI Aug 2025 circular | ❌ Closed |
| Donations | New biller onboarding discontinued — NPCI Aug 2025 circular | ❌ Closed |
| Recurring Deposits | New onboarding discontinued, incl. Digital Gold | ❌ Closed |

---

## 8. What Happens After a Payment

Once a customer completes a bill payment on any BBPS channel, here is exactly what happens on your end:

1. **Instant Confirmation Sent to Your System:** A real-time payment confirmation is posted to your biller API (or your offline repository is updated automatically). The customer receives a receipt on their app immediately.
2. **Bill Status Updated:** For offline billers — the bill record in PayU's offline repository is automatically updated from 'Due' to 'Paid', preventing any duplicate payment for the same bill.
3. **NPCI Clears Funds on T+1:** NPCI debits the consumer-side and credits the biller-side sponsor bank accounts on T+1. PayU's Axis Bank sponsor account is credited for all BOU-side transactions processed on T Day.
4. **PayU Settles to Your Bank Account on T+1:** PayU transfers the net collected amount to your registered bank account on T+1, net of applicable transaction charges.
5. **MIS Reports & TXT Files Delivered on T+1:** Automated reconciliation files (TXT) and detailed MIS reports are delivered on T+1, covering all transactions from the previous day, broken down by category, biller, and payment mode.
6. **Complaints & Refunds Handled by NPCI:** Customer disputes and refund requests are routed through NPCI's standardised grievance mechanism. Track all complaint statuses in real time from your PayU merchant dashboard.
7. **Live Dashboard Visibility:** Your PayU dashboard gives you real-time visibility into transaction statuses, settlement timelines, chargeback management, and complaint resolution — all in one place.

> ⚠️ **Important — Server-Side Verification**
> Always verify payment status using PayU's **Status Check API** on your server side. Do not rely solely on the customer-facing confirmation screen or webhook for bill status updates or order fulfilment.

---

## 9. Ready to Integrate?

Choose the onboarding path that best fits your setup:

### Path A — Online Biller (Live Biller API)

1. Contact your PayU account manager to initiate BBPS biller onboarding.
2. Submit KYC and business documents. PayU registers you with NPCI as your authorised BOU.
3. Expose your Fetch API and Payment Posting API endpoints to PayU for integration.
4. Complete end-to-end UAT — fetch, payment posting, status check, and complaints.
5. Receive NPCI sign-off. PayU takes your biller live on the BBPS network.
6. You are live — customers can pay your bills from any BBPS-enabled app in India.

### Path B — Offline Biller (Data Upload via Web Portal)

1. PayU configures your biller profile and data-upload structure on the web portal.
2. At each billing cycle, upload your bill data (CSV/Excel) to the PayU web portal. Mark bills as 'Paid' if collected elsewhere to prevent duplicates.
3. PayU handles all fetch and payment calls from the offline repository automatically.
4. Complete UAT and receive NPCI sign-off. Go live — same experience as an online biller for your customers.

### Path C — Click Pay (Push Payment Links to Customers)

1. Onboard as a biller via Path A or B above.
2. Use PayU's Click Pay API to generate pre-filled BBPS payment links.
3. Push links to customers via WhatsApp, SMS, or email — one tap to pay, all bill details pre-populated, no biller search needed.

---

> 🚀 **Get Your Billing System Live on BBPS**
> Talk to your PayU Account Manager | Explore the API Reference | Test with the Postman Collection | Begin NPCI Biller Registration via PayU

---

*This document is based on PayU BBPS product materials and NPCI/RBI regulatory guidelines current as of 2025. Biller category availability is subject to NPCI review and regulatory compliance. PayU — Authorised BOU & COU under Bharat Bill Payment System (Bharat Connect).*
