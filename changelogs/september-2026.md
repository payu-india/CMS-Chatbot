---
title: September 2026
author: Raghuram Pandurangan
hidden: true
published_at: '2026-11-05T05:39:54.874Z'
---
Discover PayU payment capabilities, API enhancements, and integration changes for September 2026. This changelog is for merchants and developers integrating PayU APIs. Availability can depend on merchant activation, payment-method support, or eligibility described in the relevant entry.

## Banking Connect

<Accordion title="Banking Connect (IBMB / NBBL) for Net Banking" icon="fa-sparkles">
  <Columns layout="auto">
    <Column>
      <div style={{ borderLeft: '3px solid #208B75', paddingLeft: '16px' }}>

        **Date:** September 28, 2026  
        **Product:** Net Banking  
        **Feature/API:** Banking Connect (IBMB / NBBL)  
        **Impact:** Medium  
        **Breaking Change:** No  
        **Action Required:** Optional, subject to enablement
      </div>
    </Column>
  </Columns>

  **Summary**

  PayU has introduced **Banking Connect**, an implementation of NPCI Bharat BillPay Limited’s (NBBL) standardized NetBanking framework (Internet Banking for Merchants and Businesses — IBMB). Banking Connect modernizes Net Banking checkout into a mobile-first, password-free payment experience without requiring changes to existing merchant Net Banking integrations. Customers authenticate securely inside their own bank's mobile application using biometrics or an MPIN, or scan a Net Banking QR code on desktop.<br />

  **Why this matters**<br />

  Traditional Net Banking requires customers to remember and enter User IDs and passwords during browser redirects, contributing to checkout drop-offs. Banking Connect enables app-first, password-free authentication directly inside bank applications while retaining Net Banking's core benefits: high-value transaction support with no ticket-size caps, existing settlement schedules, and unchanged reconciliation workflows.<br />

  **Who is affected**<br />

  - Merchants offering Net Banking on their checkout pages.
  - Developers managing web checkout or mobile app integrations.
  - Operations and finance teams handling Net Banking settlements and reconciliation.<br />

  **What's new**<br />

  - **Mobile App-Intent Flow:** When paying on mobile browsers or apps, customers select a supported bank to open their installed bank app directly via a deep link, authenticating seamlessly via biometrics or MPIN.
  - **Desktop Dynamic QR Flow:** On desktop browsers, PayU presents a dynamic Net Banking QR code that customers scan with their mobile banking app to authenticate and complete payment.
  - **Automatic Bank Website Fallback:** If the customer's bank app is not installed or the app-first flow is unavailable, the transaction automatically falls back to the familiar bank website Net Banking login flow.
  - **Zero Integration Changes:** Existing merchant Net Banking integrations (`pg=NB` and bank codes) remain completely unchanged.
  - **Uncapped High-Value Payments:** Full Net Banking limits are preserved for large ticket-size transactions.
  - **Phased Rollout:** PayU can enable banks individually or configure traffic splits to evaluate conversion metrics before a full rollout.
  - **Currently Live Banks:** HDFC Bank, ICICI Bank, Axis Bank, and YES Bank.
  - **Upcoming Banks:** SBI, IDBI Bank, Bank of Baroda, IDFC FIRST Bank, Canara Bank, Kotak Mahindra Bank, CSB Bank, Federal Bank, and AU Small Finance Bank.<br />

  **Action required**<br />

  Contact your PayU Key Account Manager (KAM) or PayU Support to enable Banking Connect on your Merchant ID (MID). No code changes are required for existing web integrations.<br />

  **Need to migrate**<br />

  No. Existing Net Banking payment requests remain fully backward-compatible. Banking Connect routing is applied seamlessly at the PayU gateway layer once activated.

  **Related documentation**<br />

  - [Banking Connect - IBMB or NBBL](https://docs.payu.in/docs/banking-connect-ibmb-or-nbbl)
</Accordion>