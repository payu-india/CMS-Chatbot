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

  No. Existing Net Banking payment requests remain fully backward-compatible. Banking Connect routing is applied seamlessly at the PayU gateway layer once activated.<br />

  **Related documentation**<br />

  - [Banking Connect - IBMB or NBBL](https://docs.payu.in/docs/banking-connect-ibmb-or-nbbl)
</Accordion>

## Partner Integration Enhancements

<Accordion title="Offline Merchant Onboarding API" icon="fa-code">
  <Columns layout="auto">
    <Column>
      <div style={{ borderLeft: '3px solid #208B75', paddingLeft: '16px' }}>

        **Date:** September 18, 2026  
        **Product:** Partner Platform / Onboarding  
        **Feature/API:** Offline Merchant Onboarding API  
        **Impact:** Medium  
        **Breaking Change:** No  
        **Action Required:** Optional, for partners onboarding offline merchants
      </div>
    </Column>
  </Columns>

  **Summary**

  PayU has extended its Partner Onboarding APIs to support physical, brick-and-mortar merchants without an active website or mobile app. Partners can now programmatically register offline merchants, specify whether a POS terminal is needed, and submit physical verification data—including store photos and geolocation coordinates—directly via API wrappers.

  **Why this matters**

  Previously, the Partner Onboarding flow was optimized primarily for online merchants (`PayuBiz`), requiring website and app URLs for compliance checks. Partners serving offline retail networks, ERP ecosystems, and field sales channels can now onboard physical merchants end-to-end without redirection to web dashboards or manual operational workarounds.

  **Who is affected**

  - Platform partners, aggregators, and ERPs referring offline retail merchants.
  - Developers integrating PayU Partner Onboarding APIs (`POST /api/v3/merchants` or `POST /api/v1/merchants`).
  - Operations and risk teams handling physical store onboarding and verification.

  **What's new**

  - **Onboarding Mode Parameter:** Include `onboarding_type: "offline"` in the Create Merchant request payload. If omitted, the request defaults to standard `online` onboarding.
  - **POS Indicator Parameter:** When `onboarding_type` is set to `offline`, the `pos_merchant` boolean parameter is required (`true` if a POS terminal is needed, `false` otherwise). Omitting this parameter for offline merchants returns an HTTP 422 error.
  - **Shop Photo Upload API:** Submit physical store imagery using `POST /api/v3/merchants/{mid}/shop_photos` to capture storefront and interior evidence.
  - **Geolocation Capture API:** Record the establishment's physical coordinates using `POST /api/v3/merchants/{mid}/geo_location`.
  - **Bank Statement Upload API:** Upload bank statements for POS offline merchants via `POST /api/v3/merchants/{mid}/bank_statements` (applicable when `pos_merchant: true`).
  - **Partner Classification Verification:** The onboarding pipeline automatically respects partner classification: Registered Entity (RE) partners can leverage Customer Point of Visit (CPV) verification as an alternative to VKYC, whereas Non-RE partners follow standard mandatory VKYC requirements.
  - **Full Backward Compatibility:** Existing partner integrations creating online merchants without `onboarding_type` or `pos_merchant` continue operating without any changes.

  **Action required**

  Partners integrating offline merchant onboarding should update their Create Merchant payload to supply `onboarding_type: "offline"` and `pos_merchant: true | false`, and integrate the shop photo, geolocation, and bank statement endpoints into their submission sequence as applicable.

  **Need to migrate**

  No. This is a backward-compatible enhancement. Existing partner onboarding integrations for online merchants do not require modification.

  **Related documentation**

  - [Partner Offline Merchant Onboarding API](https://docs.payu.in/update/reference/partner-offline-merchant-onboarding-api)
</Accordion>