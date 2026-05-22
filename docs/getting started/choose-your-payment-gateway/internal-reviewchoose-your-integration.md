---
title: '[Internal Review]Choose Your Integration'
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Choose your Integration
excerpt: >-
  Interactive walkthrough and comparison of PayU no-code, hosted checkout,
  merchant hosted, mobile SDK, and plugin integration options.
deprecated: false
hidden: false
metadata:
  title: Choose your Integration
  description: >-
    Compare PayU integration options with an interactive finder—no-code, hosted
    checkout, merchant hosted, mobile SDKs, and ecommerce plugins.
  robots: index
next:
  description: ''
---
Selecting the appropriate payment solution depends on your specific business needs and technical capabilities.

> 📘 For documentation links by topic (Payment APIs, webhooks, SDKs, plugins), see [Merchant First Integration Guide](doc:merchant-first-integration-guide). For Payment API paths and mandatory hash/webhook steps, see [Payment APIs Getting Started](doc:payment-apis-getting-started).

## Interactive integration finder

Use the walkthrough below to branch to a recommended PayU integration path. You can restart anytime or read the detailed sections further down this page.

<HTMLBlock>{`
<div id="payu-integration-wizard" class="piw-root" role="region" aria-label="PayU integration walkthrough">
  <style>
    #payu-integration-wizard { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; color: #0f172a; max-width: 720px; margin: 1.5rem 0 2rem; border: 1px solid #e2e8f0; border-radius: 12px; background: linear-gradient(180deg, #f8fafc 0%, #fff 120px); box-shadow: 0 4px 24px rgba(15,23,42,.06); overflow: hidden; }
    #payu-integration-wizard * { box-sizing: border-box; }
    #payu-integration-wizard .piw-header { display: flex; gap: 14px; align-items: flex-start; padding: 20px 22px 12px; border-bottom: 1px solid #e2e8f0; background: #fff; }
    #payu-integration-wizard .piw-header-icon { width: 44px; height: 44px; border-radius: 10px; background: linear-gradient(135deg, #0ea5e9, #6366f1); flex-shrink: 0; display: flex; align-items: center; justify-content: center; }
    #payu-integration-wizard .piw-header-icon svg { width: 24px; height: 24px; fill: #fff; }
    #payu-integration-wizard .piw-title { margin: 0; font-size: 1.15rem; font-weight: 700; line-height: 1.3; }
    #payu-integration-wizard .piw-subtitle { margin: 4px 0 0; font-size: 0.875rem; color: #64748b; line-height: 1.45; }
    #payu-integration-wizard .piw-progress { height: 4px; background: #e2e8f0; }
    #payu-integration-wizard .piw-progress-fill { height: 100%; width: 0%; background: linear-gradient(90deg, #0ea5e9, #6366f1); transition: width .35s ease; }
    #payu-integration-wizard .piw-body { padding: 18px 22px 22px; }
    #payu-integration-wizard .piw-step-label { margin: 0 0 14px; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: .06em; color: #6366f1; }
    #payu-integration-wizard .piw-q { margin: 0 0 14px; font-size: 1.05rem; font-weight: 600; line-height: 1.4; }
    #payu-integration-wizard .piw-hint { margin: -8px 0 14px; font-size: 0.8125rem; color: #64748b; }
    #payu-integration-wizard .piw-options { display: grid; gap: 10px; }
    @media (min-width: 520px) { #payu-integration-wizard .piw-options.piw-grid-2 { grid-template-columns: 1fr 1fr; } }
    #payu-integration-wizard .piw-opt { display: flex; gap: 12px; align-items: flex-start; text-align: left; width: 100%; padding: 14px 14px; border: 2px solid #e2e8f0; border-radius: 10px; background: #fff; cursor: pointer; transition: border-color .2s, background .2s, box-shadow .2s; font: inherit; color: inherit; }
    #payu-integration-wizard .piw-opt:hover { border-color: #93c5fd; background: #f0f9ff; }
    #payu-integration-wizard .piw-opt:focus-visible { outline: 2px solid #2563eb; outline-offset: 2px; }
    #payu-integration-wizard .piw-opt.piw-selected { border-color: #2563eb; background: #eff6ff; box-shadow: 0 0 0 1px #2563eb; }
    #payu-integration-wizard .piw-opt-icon { width: 40px; height: 40px; border-radius: 8px; background: #f1f5f9; display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: #0369a1; }
    #payu-integration-wizard .piw-opt-icon svg { width: 22px; height: 22px; }
    #payu-integration-wizard .piw-opt-title { font-weight: 600; font-size: 0.9375rem; display: block; margin-bottom: 2px; }
    #payu-integration-wizard .piw-opt-desc { font-size: 0.8125rem; color: #64748b; line-height: 1.4; display: block; }
    #payu-integration-wizard .piw-actions { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 18px; align-items: center; }
    #payu-integration-wizard .piw-btn { padding: 10px 18px; border-radius: 8px; font-size: 0.875rem; font-weight: 600; cursor: pointer; border: none; font-family: inherit; }
    #payu-integration-wizard .piw-btn-primary { background: #2563eb; color: #fff; }
    #payu-integration-wizard .piw-btn-primary:hover { background: #1d4ed8; }
    #payu-integration-wizard .piw-btn-primary:disabled { background: #94a3b8; cursor: not-allowed; }
    #payu-integration-wizard .piw-btn-secondary { background: #fff; color: #334155; border: 1px solid #cbd5e1; }
    #payu-integration-wizard .piw-btn-secondary:hover { background: #f8fafc; }
    #payu-integration-wizard .piw-result { border: 2px solid #86efac; border-radius: 10px; background: #f0fdf4; padding: 16px 18px; }
    #payu-integration-wizard .piw-result-badge { display: inline-flex; align-items: center; gap: 6px; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: .05em; color: #15803d; margin-bottom: 8px; }
    #payu-integration-wizard .piw-result h4 { margin: 0 0 8px; font-size: 1.125rem; color: #14532d; }
    #payu-integration-wizard .piw-result p { margin: 0 0 12px; font-size: 0.875rem; color: #166534; line-height: 1.5; }
    #payu-integration-wizard .piw-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 14px; }
    #payu-integration-wizard .piw-tag { font-size: 0.7rem; font-weight: 600; padding: 4px 8px; border-radius: 6px; background: #dcfce7; color: #166534; }
    #payu-integration-wizard .piw-links { display: flex; flex-direction: column; gap: 8px; }
    #payu-integration-wizard .piw-link { display: inline-flex; align-items: center; gap: 8px; font-size: 0.875rem; font-weight: 600; color: #1d4ed8; text-decoration: none; }
    #payu-integration-wizard .piw-link:hover { text-decoration: underline; }
    #payu-integration-wizard .piw-link svg { width: 16px; height: 16px; flex-shrink: 0; }
    #payu-integration-wizard .piw-alsos { margin-top: 14px; padding-top: 14px; border-top: 1px solid #bbf7d0; }
    #payu-integration-wizard .piw-alsos-title { font-size: 0.75rem; font-weight: 600; color: #15803d; margin: 0 0 8px; }
    #payu-integration-wizard .piw-intro-text { font-size: 0.9rem; color: #475569; line-height: 1.55; margin: 0 0 16px; }
  </style>
  <div class="piw-header">
    <div class="piw-header-icon" aria-hidden="true"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L4 6v6c0 5 3.4 9.4 8 10 4.6-.6 8-5 8-10V6l-8-4zm0 2.2l6 3v5.8c0 4.1-2.7 7.8-6 8.3-3.3-.5-6-4.2-6-8.3V7.2l6-3zM11 11h2v5h-2v-5zm0-3h2v2h-2V8z"/></svg></div>
    <div>
      <p class="piw-title">Integration path finder</p>
      <p class="piw-subtitle">Branch by channel, team skills, and checkout goals.</p>
    </div>
  </div>
  <div class="piw-progress" aria-hidden="true"><div class="piw-progress-fill" id="piw-progress-fill"></div></div>
  <div class="piw-body" id="piw-body"></div>
</div>
<script>
(function () {
  var ROOT = document.getElementById('payu-integration-wizard');
  if (!ROOT) return;
  var BODY = document.getElementById('piw-body');
  var FILL = document.getElementById('piw-progress-fill');
  var DOC = 'https://docs.payu.in/docs/';
  var state = { step: 0, channel: '', tech: '', goal: '', mobilePlatform: '' };
  var ICONS = {
    compass: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm.31-8.86c-1.77-.45-2.34-.94-2.34-1.67 0-.84.79-1.43 2.1-1.43 1.38 0 2.06.63 2.06 1.64h-1.9c0-.32-.25-.56-.73-.56-.47 0-.72.2-.72.5 0 .39.35.54 1.48.86 1.77.46 2.33.95 2.33 1.67 0 .91-.84 1.5-2.2 1.5-1.44 0-2.2-.66-2.26-1.64h1.9c.05.41.36.6.86.6.52 0 .79-.23.79-.55z"/></svg>',
    web: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>',
    mobile: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17 1H7c-1.1 0-2 .9-2 2v18c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2V3c0-1.1-.9-2-2-2zm0 18H7V5h10v14z"/></svg>',
    shop: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2-.9-2-2-2zM1 2v2h2l3.6 7.59-1.35 2.45c-.16.28-.25.61-.25.96 0 1.1.9 2 2 2h12v-2H7.42c-.14 0-.25-.11-.25-.25l.03-.12.9-1.63h7.45c.75 0 1.41-.41 1.75-1.03l3.58-6.49c.08-.14.12-.31.12-.48 0-.55-.45-1-1-1H5.21l-.94-2H1zm16 16c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2 2-.9 2-2-.9-2-2-2z"/></svg>',
    layers: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l-5.5 9h11L12 2zm0 3.84L13.93 9h-3.87L12 5.84zM17.5 13c-2.49 0-4.5 2.01-4.5 4.5s2.01 4.5 4.5 4.5 4.5-2.01 4.5-4.5-2.01-4.5-4.5-4.5zm-11 0C4.01 13 2 15.01 2 17.5S4.01 22 6.5 22 11 19.99 11 17.5 8.99 13 6.5 13zm11 7c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5zm-11 0c-1.38 0-2.5-1.12-2.5-2.5S4.12 15 5.5 15 8 16.12 8 17.5 6.88 20 5.5 20z"/></svg>',
    spark: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 14l-5-5 1.41-1.41L12 14.17l7.59-7.59L21 8l-9 9z"/></svg>',
    wrench: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22.7 19l-9.1-9.1c.9-2.3.4-5-1.5-6.9-2-2-5-2.4-7.4-1.3L9 6 6 9 1.6 4.7C.4 7.1.9 10.1 2.9 12.1c1.9 1.9 4.6 2.4 6.9 1.5l9.1 9.1c.4.4 1 .4 1.4 0l2.3-2.3c.5-.4.5-1.1.1-1.4z"/></svg>',
    code: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/></svg>',
    rocket: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.5c0 0-4.5 5.5-4.5 10.5 0 1.93 1.57 3.5 3.5 3.5.55 0 1-.45 1-1v-1.5c0-.83.67-1.5 1.5-1.5H12c.83 0 1.5.67 1.5 1.5V15c0 .55.45 1 1 1 1.93 0 3.5-1.57 3.5-3.5C17.5 8 12 2.5 12 2.5zM10 20.5c0 .83.67 1.5 1.5 1.5h1c.83 0 1.5-.67 1.5-1.5v-.5h-4v.5z"/></svg>',
    palette: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3c-4.97 0-9 4.03-9 9 0 4.17 2.84 7.67 6.69 8.69V21h4.62v-.31c3.85-1.02 6.69-4.52 6.69-8.69 0-4.97-4.03-9-9-9zm0 2c3.86 0 7 3.14 7 7 0 3.25-2.22 5.98-5.22 6.74L13 20h-2l-.78-1.26C7.22 17.98 5 15.25 5 12c0-3.86 3.14-7 7-7z"/></svg>',
    api: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 6h16v2H4V6zm0 5h10v2H4v-2zm0 5h16v2H4v-2z"/></svg>',
    android: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6 18c0 .55.45 1 1 1h1v3c0 .55.45 1 1 1s1-.45 1-1v-3h4v3c0 .55.45 1 1 1s1-.45 1-1v-3h1c.55 0 1-.45 1-1v-5H6v5zM16 7V4h-1V2h-2v2H9V4H8v3H5v12h14V7h-3z"/></svg>',
    apple: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.71 19.5c-.83 1.24-1.71 2.45-3.05 2.47-1.34.03-1.77-.79-3.29-.79-1.53 0-2 .77-3.27.82-1.31.05-2.3-1.32-3.14-2.53C4.25 17 2.94 12.45 4.7 9.39c.87-1.52 2.43-2.48 4.12-2.51 1.28-.02 2.5.87 3.29.87.78 0 2.26-1.07 3.81-.91.65.03 2.47.26 3.64 1.98-.09.06-2.17 1.28-2.15 3.81.03 3.02 2.65 4.03 2.68 4.04-.03.07-.42 1.44-1.38 2.83M13 3.5c.73-.83 1.94-1.46 2.94-1.5.13 1.17-.34 2.35-1.04 3.19-.69.85-1.83 1.51-2.95 1.42-.15-1.15.41-2.35 1.05-3.11z"/></svg>',
    cross: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M4 6h18V4H4c-1.1 0-2 .9-2 2v11h2V6zm6 7H8v5h2v-5zm7-1h-2v6h2v-6zm3-3H2v11c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V9c0-1.1-.9-2-2-2zm0 13H4V9h16v11z"/></svg>',
    link: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"/></svg>',
    check: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>'
  };
  function progress() {
    var total = state.channel === 'mobile' ? 4 : (state.channel === 'ecommerce' ? 2 : 4);
    var cur = state.step;
    if (state.step >= 4) cur = total;
    FILL.style.width = Math.min(100, Math.round((cur / total) * 100)) + '%';
  }
  function link(href, label) {
    return '<a class="piw-link" href="' + href + '" target="_blank" rel="noopener noreferrer">' + ICONS.link + '<span>' + label + '</span></a>';
  }
  function option(id, icon, title, desc) {
    return '<button type="button" class="piw-opt" data-value="' + id + '" aria-pressed="false">' +
      '<span class="piw-opt-icon" aria-hidden="true">' + icon + '</span>' +
      '<span><span class="piw-opt-title">' + title + '</span><span class="piw-opt-desc">' + desc + '</span></span></button>';
  }
  function bindOptions(selectFn) {
    var opts = BODY.querySelectorAll('.piw-opt');
    for (var i = 0; i < opts.length; i++) {
      opts[i].addEventListener('click', function () {
        for (var j = 0; j < opts.length; j++) { opts[j].classList.remove('piw-selected'); opts[j].setAttribute('aria-pressed', 'false'); }
        this.classList.add('piw-selected');
        this.setAttribute('aria-pressed', 'true');
        selectFn(this.getAttribute('data-value'));
        var next = BODY.querySelector('.piw-btn-primary');
        if (next) next.disabled = false;
      });
    }
  }
  function recommend() {
    var c = state.channel, t = state.tech, g = state.goal, m = state.mobilePlatform;
    if (c === 'multi') {
      return {
        title: 'Multiple integration paths',
        desc: 'You likely need more than one PayU surface—for example Hosted Checkout or APIs on the web plus mobile SDKs in your app. Use the Merchant First guide to map each channel, then follow the checklist per product before go-live.',
        tags: ['Web + mobile', 'Use routing guide', 'Separate credentials per env'],
        primary: { href: DOC + 'merchant-first-integration-guide', label: 'Merchant First Integration Guide' },
        also: [
          { href: DOC + 'payment-apis-getting-started', label: 'Payment APIs getting started' },
          { href: DOC + 'prebuilt-checkout-payu-hosted', label: 'PayU Hosted Checkout' },
          { href: DOC + 'explore-android-sdks', label: 'Explore Android SDKs' },
          { href: DOC + 'go-live-checklist-all-integrations', label: 'Go-live checklist' }
        ]
      };
    }
    if (c === 'ecommerce') {
      return {
        title: 'Ecommerce plugin integration',
        desc: 'Use a ready-made PayU plugin for Shopify, WooCommerce, Magento, or similar platforms. Integration effort is very low and PayU hosts sensitive card data.',
        tags: ['Very easy', 'No PCI burden', 'Platform-native'],
        primary: { href: DOC + 'ecommerce-platform-plugins', label: 'Plugins — Introduction' },
        also: [
          { href: DOC + 'prebuilt-checkout-payu-hosted', label: 'PayU Hosted Checkout (reference)' },
          { href: DOC + 'integration-checklist-plugins', label: 'Production checklist — Plugins' },
          { href: DOC + 'troubleshooting-shopify-integration', label: 'Troubleshooting — Shopify' }
        ]
      };
    }
    if (c === 'mobile') {
      var sdkLabel = 'Explore mobile SDKs';
      var sdkHref = DOC + 'explore-android-sdks';
      if (m === 'ios') sdkHref = DOC + 'explore-ios-sdks';
      if (m === 'cross') sdkHref = DOC + 'explore-reactnative-sdks';
      if (m === 'flutter') sdkHref = DOC + 'flutter-sdk-introduction';
      return {
        title: 'Mobile SDK (CheckoutPro / Core)',
        desc: 'Integrate PayU into your native or cross-platform app. Generate payment hashes on your server, configure webhooks, and follow the SDK go-live checklist before production.',
        tags: ['Mobile-native', 'Moderate effort', 'Server-side hash'],
        primary: { href: sdkHref, label: sdkLabel },
        also: [
          { href: DOC + 'integration-steps-android-checkout-pro', label: 'CheckoutPro — Android integration' },
          { href: DOC + 'ios-checkout-pro-sdk-integration-steps', label: 'CheckoutPro — iOS integration' },
          { href: DOC + 'go-live-checklist-all-integrations', label: 'Go-live checklist — All integrations' },
          { href: DOC + 'faqs-android-sdk', label: 'FAQs — Android SDK' }
        ]
      };
    }
    if (t === 'none' || g === 'speed') {
      return {
        title: 'No-code or PayU Hosted Checkout',
        desc: 'Collect payments quickly without building a custom checkout. Payment Links, invoices, and buttons need minimal development; Hosted Checkout redirects customers to a secure PayU page.',
        tags: ['Very easy', 'Fast go-live', 'PayU-managed PCI'],
        primary: { href: DOC + 'introduction-no-code-payments-integration', label: 'No-code payments' },
        also: [
          { href: DOC + 'prebuilt-checkout-payu-hosted', label: 'PayU Hosted Checkout' },
          { href: DOC + 'faqs-payment-links', label: 'FAQs — Payment Links' },
          { href: DOC + 'payment-apis-getting-started', label: 'Payment APIs getting started' }
        ]
      };
    }
    if (g === 'branded' && t === 'some') {
      return {
        title: 'Checkout Plus or Hosted Checkout',
        desc: 'Low-code options let you customize branding with less engineering than full merchant-hosted checkout. Hosted Checkout keeps PCI scope lighter.',
        tags: ['Low–medium effort', 'Customizable UI', 'Optimized conversion'],
        primary: { href: DOC + 'checkout-plus-integration', label: 'Checkout Plus' },
        also: [
          { href: DOC + 'prebuilt-checkout-payu-hosted', label: 'PayU Hosted Checkout' },
          { href: DOC + 'checkout-express', label: 'CommercePro Checkout' },
          { href: DOC + 'payment-apis-getting-started', label: 'Payment APIs getting started' }
        ]
      };
    }
    if (g === 'control' || (t === 'full' && g !== 'speed')) {
      return {
        title: 'Merchant Hosted or Server-to-Server',
        desc: 'You control the checkout UI and payment orchestration on your servers. Requires hash generation, reverse hash validation, webhooks, and PCI planning for card data on your site.',
        tags: ['High control', 'Developer APIs', 'PCI consideration'],
        primary: { href: DOC + 'custom-checkout-merchant-hosted', label: 'Merchant Hosted Checkout' },
        also: [
          { href: DOC + 'server-to-server-integration', label: 'Server-to-Server integration' },
          { href: DOC + 'generate-hash-merchant-hosted', label: 'Generate hash' },
          { href: DOC + 'integration-checklist-merchant-hosted-checkout', label: 'Checklist — Merchant Hosted' },
          { href: DOC + 'integration-checklist-s2s', label: 'Checklist — S2S' }
        ]
      };
    }
    return {
      title: 'PayU Hosted Checkout',
      desc: 'A secure redirect-based checkout with minimal development—ideal when you want PayU to manage the payment page and PCI scope.',
      tags: ['Easy', 'Secure', 'Multiple payment modes'],
      primary: { href: DOC + 'prebuilt-checkout-payu-hosted', label: 'PayU Hosted Checkout' },
      also: [
        { href: DOC + 'merchant-first-integration-guide', label: 'Merchant First Integration Guide' },
        { href: DOC + 'go-live-checklist-all-integrations', label: 'Go-live checklist' }
      ]
    };
  }
  function renderResult() {
    var r = recommend();
    var html = '<p class="piw-step-label">Your recommendation</p>';
    html += '<div class="piw-result" role="status">';
    html += '<div class="piw-result-badge">' + ICONS.check + ' Best match</div>';
    html += '<h4>' + r.title + '</h4><p>' + r.desc + '</p><div class="piw-tags">';
    for (var i = 0; i < r.tags.length; i++) html += '<span class="piw-tag">' + r.tags[i] + '</span>';
    html += '</div><div class="piw-links">' + link(r.primary.href, r.primary.label) + '</div>';
    if (r.also && r.also.length) {
      html += '<div class="piw-alsos"><p class="piw-alsos-title">Also review</p><div class="piw-links">';
      for (var j = 0; j < r.also.length; j++) html += link(r.also[j].href, r.also[j].label);
      html += '</div></div>';
    }
    html += '</div><div class="piw-actions"><button type="button" class="piw-btn piw-btn-secondary" id="piw-back">Back</button>';
    html += '<button type="button" class="piw-btn piw-btn-primary" id="piw-restart">Start over</button></div>';
    BODY.innerHTML = html;
    document.getElementById('piw-restart').onclick = function () { state = { step: 0, channel: '', tech: '', goal: '', mobilePlatform: '' }; render(); };
    var back = document.getElementById('piw-back');
    if (back) back.onclick = function () {
      if (state.channel === 'ecommerce') state.step = 1;
      else if (state.channel === 'mobile') state.step = 3;
      else state.step = 3;
      render();
    };
    progress();
  }
  function render() {
    progress();
    if (state.step === 0) {
      BODY.innerHTML = '<p class="piw-step-label">Step 1 of 4</p><p class="piw-intro-text">This walkthrough mirrors the options on this page—channel, team capability, and checkout goals—and points you to the right PayU documentation.</p>' +
        '<div class="piw-actions"><button type="button" class="piw-btn piw-btn-primary" id="piw-start">Start walkthrough</button></div>';
      document.getElementById('piw-start').onclick = function () { state.step = 1; render(); };
      return;
    }
    if (state.step === 1) {
      BODY.innerHTML = '<p class="piw-step-label">Step 1 of 4 — Channel</p><p class="piw-q">Where do you primarily collect payments?</p><p class="piw-hint">Choose the closest match.</p>' +
        '<div class="piw-options piw-grid-2">' +
        option('website', ICONS.web, 'Website', 'Browser checkout on your site') +
        option('mobile', ICONS.mobile, 'Mobile app', 'Android, iOS, Flutter, or React Native') +
        option('ecommerce', ICONS.shop, 'Ecommerce platform', 'Shopify, WooCommerce, Magento, etc.') +
        option('multi', ICONS.layers, 'Multiple channels', 'Web plus app or several surfaces') +
        '</div><div class="piw-actions"><button type="button" class="piw-btn piw-btn-secondary" id="piw-back">Back</button>' +
        '<button type="button" class="piw-btn piw-btn-primary" id="piw-next" disabled>Continue</button></div>';
      bindOptions(function (v) { state.channel = v; });
      document.getElementById('piw-back').onclick = function () { state.step = 0; render(); };
      document.getElementById('piw-next').onclick = function () {
        if (!state.channel) return;
        if (state.channel === 'ecommerce') { state.step = 4; renderResult(); return; }
        if (state.channel === 'multi') { state.step = 2; render(); return; }
        state.step = 2; render();
      };
      return;
    }
    if (state.step === 2) {
      BODY.innerHTML = '<p class="piw-step-label">Step 2 of 4 — Team</p><p class="piw-q">What developer resources do you have?</p>' +
        '<div class="piw-options">' +
        option('none', ICONS.spark, 'No dedicated developers', 'Prefer no-code or hosted solutions') +
        option('some', ICONS.wrench, 'Some technical support', 'Can use low-code or light integration') +
        option('full', ICONS.code, 'Full development team', 'Custom checkout or APIs') +
        '</div><div class="piw-actions"><button type="button" class="piw-btn piw-btn-secondary" id="piw-back">Back</button>' +
        '<button type="button" class="piw-btn piw-btn-primary" id="piw-next" disabled>Continue</button></div>';
      bindOptions(function (v) { state.tech = v; });
      document.getElementById('piw-back').onclick = function () { state.step = 1; render(); };
      document.getElementById('piw-next').onclick = function () {
        if (!state.tech) return;
        if (state.channel === 'mobile') { state.step = 3; render(); return; }
        state.step = 3; render();
      };
      return;
    }
    if (state.step === 3 && state.channel === 'mobile') {
      BODY.innerHTML = '<p class="piw-step-label">Step 3 of 4 — Mobile stack</p><p class="piw-q">Which mobile stack are you using?</p>' +
        '<div class="piw-options piw-grid-2">' +
        option('android', ICONS.android, 'Android', 'Native Kotlin/Java') +
        option('ios', ICONS.apple, 'iOS', 'Native Swift/Objective-C') +
        option('cross', ICONS.cross, 'React Native', 'Cross-platform RN') +
        option('flutter', ICONS.mobile, 'Flutter', 'Cross-platform Flutter') +
        '</div><div class="piw-actions"><button type="button" class="piw-btn piw-btn-secondary" id="piw-back">Back</button>' +
        '<button type="button" class="piw-btn piw-btn-primary" id="piw-next" disabled>See recommendation</button></div>';
      bindOptions(function (v) { state.mobilePlatform = v; });
      document.getElementById('piw-back').onclick = function () { state.step = 2; render(); };
      document.getElementById('piw-next').onclick = function () { if (!state.mobilePlatform) return; state.step = 4; renderResult(); };
      return;
    }
    if (state.step === 3) {
      BODY.innerHTML = '<p class="piw-step-label">Step 3 of 4 — Priority</p><p class="piw-q">What matters most for your checkout?</p>' +
        '<div class="piw-options">' +
        option('speed', ICONS.rocket, 'Speed to go-live', 'Minimal coding and fastest setup') +
        option('branded', ICONS.palette, 'Branded experience', 'Match your site look and feel') +
        option('control', ICONS.api, 'Maximum control', 'Own UI and server-side payment flows') +
        '</div><div class="piw-actions"><button type="button" class="piw-btn piw-btn-secondary" id="piw-back">Back</button>' +
        '<button type="button" class="piw-btn piw-btn-primary" id="piw-next" disabled>See recommendation</button></div>';
      bindOptions(function (v) { state.goal = v; });
      document.getElementById('piw-back').onclick = function () { state.step = 2; render(); };
      document.getElementById('piw-next').onclick = function () { if (!state.goal) return; state.step = 4; renderResult(); };
      return;
    }
    renderResult();
  }
  render();
})();
</script>
`}</HTMLBlock>

Here are some considerations to help you make an informed decision:

- **Technical Expertise**: Evaluate your team's technical knowledge and resources. No-code solutions require minimal technical expertise, while custom checkouts may require development skills.
- **User Experience**: Consider the desired user experience for your customers. If a seamless, branded experience is crucial, custom checkout or iframe-based checkout may be the best choice.
- **Security**: Assess the level of security required for your transactions. Hosted checkout solutions offer robust security and PCI compliance, reducing your compliance burden.
- **Mobility**: If your customers predominantly use mobile devices for transactions, prioritize mobile checkouts or responsive design.
- **Integration**: Determine how you want to integrate payments into your platform. Payment buttons, payment links, and payment invoices offer simple integration, while custom checkout and iframe-based checkout provide more control.

By carefully assessing your needs and preferences in these areas, you can select the payment solution that aligns with your business goals and customer expectations.

## No-Code Payment Solutions

### Payment Links

**Use Case**: Payment links are ideal for businesses or individuals who want a simple and efficient way to collect payments without the need for technical expertise. Payment links can be shared via email, SMS, or social media platforms, allowing customers to make payments with ease.

**Key Features**:

- **Quick Setup**: Generate payment links instantly without any coding or integration.
- **Customizable**: Add product details, descriptions, and amounts to personalize payment requests.
- **Real-Time Notifications**: Receive instant payment notifications when customers complete transactions.
  Tracking: Monitor payment status and history for easy reconciliation.

### Payment Invoices

**Use Case**: Payment invoices are perfect for businesses that need to bill clients for goods or services. Create professional invoices that include payment links and details for easy payment processing.

**Key Features**:

- **Invoice Generation**: Easily create and send invoices to clients.
- **Payment Tracking**: Monitor invoice status and payment history.
- **Payment Reminders**: Send automated payment reminders to clients.
- **Invoice Customization**: Customize invoices with your brand logo and colors.

### Payment Buttons

**Use Case**: Payment buttons are suitable for businesses with an online presence. Integrate payment buttons seamlessly into your website or e-commerce platform to provide a convenient checkout experience for customers.

**Key Features**:

- **Easy Integration**: Add payment buttons to your website with minimal technical knowledge.
- **Customizable**: Customize button appearance and text to match your brand.
- **Multiple Payment Methods**: Accept payments through various methods, including credit cards and digital wallets.
- **Security**: Ensure secure and PCI-compliant transactions for your customers.

***

## Web Integration

### Prebuilt Checkout

**Use Case**: Hosted checkout is designed for businesses that require a secure and hassle-free online payment experience. Redirect customers to our secure payment page for transaction processing.

**Key Features**:

- **Security**: Benefit from our robust security infrastructure, reducing the risk of fraud.
- **PCI Compliance**: Eliminate the burden of PCI DSS compliance as we handle payment data securely.
- **Customization**: Customize the hosted page to match your brand's look and feel.
- **Multiple Payment Options**: Offer customers a range of payment methods.

### Custom Checkout

- **Use Case**: Custom checkout is suitable for businesses seeking complete control over the payment process. Integrate our payment gateway directly into your website or app for a seamless, branded experience.

**Key Features**:

- **Full Control**: Design and control the entire payment flow within your website or app.
- **User Experience**: Create a tailored, user-friendly checkout experience.
- **API Access**: Access our developer-friendly APIs for deep integration and customization.
- **Data Analytics**: Analyze transaction data and customer behavior for optimization.

### Iframe-Based Checkout

**Use Case**: Iframe-based checkout is ideal for businesses looking to embed the payment process seamlessly within their website, maintaining a consistent user experience.

**Key Features**:

- **Seamless Integration**: Embed our payment gateway within your website using iframes.
- **Security**: Maintain the highest level of security while keeping customers on your site.
- **Responsive Design**: Ensure compatibility with various screen sizes and devices.
- **Easy Implementation**: Simplify integration with our provided code snippets.

***

## Mobile Checkouts

**Use Case**: Mobile checkouts cater to businesses that want to provide a convenient payment experience on mobile devices, including mobile apps and responsive websites.

**Key Features**:

- **Responsive Design**: Ensure your checkout process is mobile-friendly for a smooth user experience.
- **Mobile Wallet Integration**: Allow customers to pay using popular mobile wallets.
- **One-Click Payments**: Enable one-click or fingerprint authentication for speedy checkouts.
- **Push Notifications**: Send order updates and payment confirmations via mobile notifications.

| Payment Solution              | Ease of Integration | Use Case                                     | Key Features                                                                   |
| :---------------------------- | :------------------ | :------------------------------------------- | :----------------------------------------------------------------------------- |
| **No-Code Payment Solutions** |                     |                                              |                                                                                |
| Payment Links                 | Very Easy           | Simple, efficient payment collection         | Quick setup **|** Customizable **|** Real-time notifications **|** Tracking       |
| Payment Invoices              | Very Easy           | Professional client billing with invoices    | Invoice generation **|** Payment tracking **|** Payment reminders Customization |
| Payment Buttons               | Easy                | Seamless integration into websites/platforms | Easy integration **|** Customizable **|** Multiple payment methods **|** Security |
| **Web Integration**           |                     |                                              |                                                                                |
| Hosted Checkout               | Easy                | Secure, hassle-free online payments          | Robust security **|** PCI compliance **|** Multiple payment options              |
| Custom Checkout               | Moderate            | Total control over the payment process       | Full customization **|** Optimal user experience **|** Developer-friendly APIs   |
| Checkout Express              | Easy                | Seamless payment integration within websites | Seamless integration **|** Enhanced security **|** Easy implementation                   |
| **Mobile Checkouts**          |                     |                                              |                                                                                |
| Mobile SDKs                   | Moderate            | Convenient mobile payment experience         | Responsive design **|** Mobile wallet integration **|** One-click payments               |