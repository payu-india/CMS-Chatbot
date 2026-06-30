---
title: POC 1
deprecated: false
hidden: true
metadata:
  robots: index
---
<HTMLBlock>{`
<!--
  PayU Integration Path Recommender — ReadMe HTML embed
  Paste the contents of integration-path-recommender-embed.html into ReadMe HTMLBlock,
  OR host this file and iframe it. All styles are scoped under #payu-ipr.
-->
<div id="payu-ipr" class="payu-ipr" role="region" aria-label="PayU Integration Path Recommender">
  <div class="payu-ipr__shell">
    <header class="payu-ipr__header">
      <div class="payu-ipr__badge">PayU DevEx</div>
      <h2 class="payu-ipr__title">Which integration is right for you?</h2>
      <p class="payu-ipr__subtitle">Answer a few questions to get a tailored PayU integration recommendation.</p>
    </header>

    <div class="payu-ipr__progress-wrap" id="payu-ipr-progress-wrap" hidden>
      <div class="payu-ipr__progress-meta">
        <span id="payu-ipr-step-label">Question 1 of 7</span>
        <span id="payu-ipr-pct-label">0%</span>
      </div>
      <div class="payu-ipr__progress-bar"><div class="payu-ipr__progress-fill" id="payu-ipr-progress-fill"></div></div>
    </div>

    <div id="payu-ipr-wizard" class="payu-ipr__panel"></div>
    <div id="payu-ipr-results" class="payu-ipr__panel" hidden></div>

    <div class="payu-ipr__nav" id="payu-ipr-nav">
      <button type="button" class="payu-ipr__btn payu-ipr__btn--ghost" id="payu-ipr-back" disabled>← Back</button>
      <button type="button" class="payu-ipr__btn payu-ipr__btn--primary" id="payu-ipr-next" disabled>Next →</button>
    </div>
  </div>
</div>

<style>
  #payu-ipr, #payu-ipr * { box-sizing: border-box; }
  #payu-ipr {
    --payu-ipr-green: #00A651;
    --payu-ipr-green-dark: #008C44;
    --payu-ipr-navy: #1e3a5f;
    --payu-ipr-border: #e5e7eb;
    --payu-ipr-muted: #6b7280;
    --payu-ipr-bg: #f9fafb;
    --payu-ipr-card: #ffffff;
    font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
    font-size: 14px;
    line-height: 1.5;
    color: #111827;
    margin: 1rem 0;
  }
  #payu-ipr .payu-ipr__shell {
    border: 1px solid var(--payu-ipr-border);
    border-radius: 12px;
    background: var(--payu-ipr-card);
    padding: 1.25rem;
    box-shadow: 0 1px 3px rgba(0,0,0,.06);
  }
  #payu-ipr .payu-ipr__header { margin-bottom: 1rem; }
  #payu-ipr .payu-ipr__badge {
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: .04em;
    color: var(--payu-ipr-green);
    margin-bottom: .35rem;
  }
  #payu-ipr .payu-ipr__title {
    margin: 0 0 .35rem;
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--payu-ipr-navy);
  }
  #payu-ipr .payu-ipr__subtitle { margin: 0; color: var(--payu-ipr-muted); font-size: 13px; }
  #payu-ipr .payu-ipr__progress-wrap { margin-bottom: 1rem; }
  #payu-ipr .payu-ipr__progress-meta {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    color: var(--payu-ipr-muted);
    margin-bottom: .35rem;
  }
  #payu-ipr .payu-ipr__progress-bar {
    height: 6px;
    background: #e5e7eb;
    border-radius: 999px;
    overflow: hidden;
  }
  #payu-ipr .payu-ipr__progress-fill {
    height: 100%;
    width: 0%;
    background: var(--payu-ipr-green);
    border-radius: 999px;
    transition: width .25s ease;
  }
  #payu-ipr .payu-ipr__q-title {
    margin: 0 0 .25rem;
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--payu-ipr-navy);
  }
  #payu-ipr .payu-ipr__q-hint { margin: 0 0 .75rem; font-size: 12px; color: var(--payu-ipr-muted); }
  #payu-ipr .payu-ipr__options { display: grid; gap: .5rem; }
  #payu-ipr .payu-ipr__option {
    width: 100%;
    text-align: left;
    padding: .75rem .9rem;
    border: 2px solid var(--payu-ipr-border);
    border-radius: 10px;
    background: var(--payu-ipr-card);
    cursor: pointer;
    font: inherit;
    color: inherit;
    transition: border-color .15s, background .15s;
  }
  #payu-ipr .payu-ipr__option:hover { border-color: rgba(0,166,81,.45); }
  #payu-ipr .payu-ipr__option--on {
    border-color: var(--payu-ipr-green);
    background: rgba(0,166,81,.06);
  }
  #payu-ipr .payu-ipr__nav {
    display: flex;
    justify-content: space-between;
    gap: .75rem;
    margin-top: 1rem;
    padding-top: .75rem;
    border-top: 1px solid var(--payu-ipr-border);
  }
  #payu-ipr .payu-ipr__btn {
    padding: .55rem 1rem;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    border: 1px solid transparent;
  }
  #payu-ipr .payu-ipr__btn:disabled { opacity: .45; cursor: not-allowed; }
  #payu-ipr .payu-ipr__btn--primary {
    background: var(--payu-ipr-green);
    color: #fff;
  }
  #payu-ipr .payu-ipr__btn--primary:hover:not(:disabled) { background: var(--payu-ipr-green-dark); }
  #payu-ipr .payu-ipr__btn--ghost {
    background: #fff;
    border-color: var(--payu-ipr-border);
    color: #374151;
  }
  #payu-ipr .payu-ipr__explain {
    margin-bottom: 1rem;
    padding: .85rem 1rem;
    border-radius: 10px;
    border: 1px solid rgba(0,166,81,.25);
    background: rgba(0,166,81,.06);
    font-size: 13px;
    color: #374151;
  }
  #payu-ipr .payu-ipr__primary {
    border: 2px solid var(--payu-ipr-green);
    border-radius: 12px;
    overflow: hidden;
    margin-bottom: 1rem;
  }
  #payu-ipr .payu-ipr__primary-hd {
    background: var(--payu-ipr-green);
    color: #fff;
    font-size: 12px;
    font-weight: 600;
    padding: .45rem .9rem;
  }
  #payu-ipr .payu-ipr__primary-bd { padding: 1rem; }
  #payu-ipr .payu-ipr__score {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--payu-ipr-green);
  }
  #payu-ipr .payu-ipr__tags { display: flex; flex-wrap: wrap; gap: .35rem; margin: .5rem 0; }
  #payu-ipr .payu-ipr__tag {
    font-size: 11px;
    font-weight: 600;
    padding: .2rem .55rem;
    border-radius: 999px;
    background: #f3f4f6;
    color: #374151;
    text-transform: capitalize;
  }
  #payu-ipr .payu-ipr__tag--low { background: #d1fae5; color: #065f46; }
  #payu-ipr .payu-ipr__tag--medium { background: #fef3c7; color: #92400e; }
  #payu-ipr .payu-ipr__tag--high { background: #fee2e2; color: #991b1b; }
  #payu-ipr .payu-ipr__cols { display: grid; gap: .75rem; }
  @media (min-width: 560px) { #payu-ipr .payu-ipr__cols { grid-template-columns: 1fr 1fr; } }
  #payu-ipr .payu-ipr__list { margin: 0; padding-left: 1.1rem; font-size: 13px; color: #4b5563; }
  #payu-ipr .payu-ipr__list li { margin: .2rem 0; }
  #payu-ipr .payu-ipr__cards { display: grid; gap: .6rem; }
  @media (min-width: 560px) { #payu-ipr .payu-ipr__cards { grid-template-columns: 1fr 1fr; } }
  #payu-ipr .payu-ipr__card {
    border: 1px solid var(--payu-ipr-border);
    border-radius: 10px;
    padding: .75rem;
    background: var(--payu-ipr-bg);
  }
  #payu-ipr .payu-ipr__card h4 { margin: 0 0 .25rem; font-size: 14px; color: var(--payu-ipr-navy); }
  #payu-ipr .payu-ipr__link {
    display: inline-block;
    margin-top: .65rem;
    font-size: 13px;
    font-weight: 600;
    color: var(--payu-ipr-green);
    text-decoration: none;
  }
  #payu-ipr .payu-ipr__link:hover { text-decoration: underline; }
</style>

<script>
(function () {
  var PRODUCTS = {
    "PayU Hosted Checkout": {
      category: "checkout",
      description: "Redirect customers to PayU-hosted payment page. Minimal PCI burden, fastest go-live.",
      pros: ["Lowest PCI scope", "Fast integration (1–3 days)", "All payment methods supported"],
      cons: ["Redirect flow", "Limited checkout customization"],
      complexity: "low", goLiveDays: 3, docsUrl: "https://docs.payu.in/docs/hosted-checkout"
    },
    "PayU Seamless Checkout": {
      category: "checkout",
      description: "Embed payment form on your website with PayU handling card data securely.",
      pros: ["Native checkout experience", "Customer stays on your site"],
      cons: ["Higher PCI requirements", "More frontend work"],
      complexity: "medium", goLiveDays: 10, docsUrl: "https://docs.payu.in/docs/seamless-checkout"
    },
    "PayU Android SDK": {
      category: "sdk",
      description: "Native Android SDK for in-app payments with UPI Intent, cards, and wallets.",
      pros: ["Native Android UX", "UPI Intent support", "In-app flow"],
      cons: ["Android-only", "Native dev skills required"],
      complexity: "medium", goLiveDays: 14, docsUrl: "https://docs.payu.in/docs/android-sdk"
    },
    "PayU iOS SDK": {
      category: "sdk",
      description: "Native iOS SDK for seamless in-app payments.",
      pros: ["Native iOS UX", "In-app payment flow"],
      cons: ["iOS-only", "Swift/Obj-C skills required"],
      complexity: "medium", goLiveDays: 14, docsUrl: "https://docs.payu.in/docs/ios-sdk"
    },
    "PayU Web SDK": {
      category: "sdk",
      description: "JavaScript SDK for embedding payments in web apps.",
      pros: ["Works in any web framework", "Embedded checkout"],
      cons: ["Web-only", "Browser testing needed"],
      complexity: "medium", goLiveDays: 7, docsUrl: "https://docs.payu.in/docs/web-sdk"
    },
    "UPI Intent": {
      category: "upi",
      description: "Deep-link to UPI apps for one-tap mobile payments.",
      pros: ["Best UPI conversion on mobile", "No VPA entry"],
      cons: ["Mobile-only", "Requires UPI app"],
      complexity: "low", goLiveDays: 5, docsUrl: "https://docs.payu.in/docs/upi-intent"
    },
    "UPI Collect": {
      category: "upi",
      description: "Collect via UPI VPA entry or QR code.",
      pros: ["Works on desktop and mobile", "QR support"],
      cons: ["Manual VPA entry", "Status polling"],
      complexity: "low", goLiveDays: 5, docsUrl: "https://docs.payu.in/docs/upi-collect"
    },
    "Token Hub / Saved Cards": {
      category: "tokenization",
      description: "Store card tokens for one-click repeat payments.",
      pros: ["Repeat purchase conversion", "PCI-compliant tokens"],
      cons: ["Extra integration step", "Customer consent"],
      complexity: "medium", goLiveDays: 10, docsUrl: "https://docs.payu.in/docs/token-hub"
    },
    "Recurring Payments / Subscription": {
      category: "subscription",
      description: "Automated recurring billing and standing instructions.",
      pros: ["Automated billing", "SI on cards and UPI"],
      cons: ["RBI compliance", "Mandate registration"],
      complexity: "high", goLiveDays: 21, docsUrl: "https://docs.payu.in/docs/recurring-payments"
    },
    "Split Settlements": {
      category: "marketplace",
      description: "Split settlements between marketplace and vendors.",
      pros: ["Multi-vendor payouts", "Configurable splits"],
      cons: ["Vendor onboarding", "Reconciliation overhead"],
      complexity: "high", goLiveDays: 21, docsUrl: "https://docs.payu.in/docs/split-settlements"
    },
    "Payment Links": {
      category: "links",
      description: "Shareable payment links — no code integration.",
      pros: ["Zero code", "Share via SMS/email/WhatsApp"],
      cons: ["Limited customization", "Manual for high volume"],
      complexity: "low", goLiveDays: 1, docsUrl: "https://docs.payu.in/docs/payment-links"
    },
    "Dynamic QR": {
      category: "qr",
      description: "Dynamic QR codes for offline UPI collection.",
      pros: ["Offline collection", "UPI QR standard"],
      cons: ["Display mechanism needed", "Status polling"],
      complexity: "low", goLiveDays: 5, docsUrl: "https://docs.payu.in/docs/dynamic-qr"
    },
    "Webhooks": {
      category: "api",
      description: "Real-time server-to-server payment notifications.",
      pros: ["Real-time status", "Reliable reconciliation"],
      cons: ["Public endpoint required", "Idempotency handling"],
      complexity: "low", goLiveDays: 2, docsUrl: "https://docs.payu.in/docs/webhooks"
    },
    "Refund API": {
      category: "api",
      description: "Programmatic refunds and status tracking.",
      pros: ["Automated refunds", "Partial refund support"],
      cons: ["Settlement timing", "Error handling"],
      complexity: "low", goLiveDays: 2, docsUrl: "https://docs.payu.in/docs/refund-api"
    },
    "Transaction Status API": {
      category: "api",
      description: "Query transaction status for reconciliation.",
      pros: ["Reconciliation", "Webhook fallback"],
      cons: ["Rate limits", "Complement webhooks"],
      complexity: "low", goLiveDays: 1, docsUrl: "https://docs.payu.in/docs/transaction-status-api"
    }
  };

  var QUESTIONS = [
    { field: "platform", text: "What are you building?", type: "single", hint: "Select one",
      options: [
        { v: "website", l: "Website" },
        { v: "mobile", l: "Mobile App" },
        { v: "both", l: "Both Website & Mobile App" }
      ]
    },
    { field: "platforms", text: "Which platforms do you need?", type: "multi", hint: "Select all that apply",
      depends: { field: "platform", values: ["mobile", "both"] },
      options: [
        { v: "android", l: "Android" }, { v: "ios", l: "iOS" }, { v: "web", l: "Web" }
      ]
    },
    { field: "checkout", text: "What is your checkout preference?", type: "single", hint: "Select one",
      options: [
        { v: "hosted", l: "Redirect / Hosted — PayU handles the payment page" },
        { v: "embedded", l: "Embedded / Seamless — payment on my site or app" },
        { v: "no_code", l: "No code — payment links or QR codes" }
      ]
    },
    { field: "paymentMethods", text: "Which payment methods do you need?", type: "multi", hint: "Select all that apply",
      options: [
        { v: "cards", l: "Cards" }, { v: "upi", l: "UPI" },
        { v: "netbanking", l: "Net Banking" }, { v: "wallets", l: "Wallets" }, { v: "emi", l: "EMI" }
      ]
    },
    { field: "savedCards", text: "Need saved cards / one-click payments?", type: "bool", hint: "Select one",
      options: [{ v: true, l: "Yes" }, { v: false, l: "No" }]
    },
    { field: "recurring", text: "Need recurring payments or subscriptions?", type: "bool", hint: "Select one",
      options: [{ v: true, l: "Yes" }, { v: false, l: "No" }]
    },
    { field: "splitSettlement", text: "Need marketplace / split settlement?", type: "bool", hint: "Select one",
      options: [{ v: true, l: "Yes" }, { v: false, l: "No" }]
    },
    { field: "pciPreference", text: "PCI compliance preference?", type: "single", hint: "Select one",
      depends: { field: "checkout", values: ["hosted", "embedded"] },
      options: [
        { v: "avoid", l: "Minimize PCI scope — redirect to PayU" },
        { v: "moderate", l: "Moderate — embedded, PayU handles card data" },
        { v: "full", l: "Full control — I can handle PCI" }
      ]
    }
  ];

  var RULES = [
    { product: "PayU Hosted Checkout", weight: 95, reason: "Best for fast integration with minimal PCI burden.",
      conditions: [
        { f: "platform", op: "in", v: ["website", "both"] },
        { f: "checkout", op: "eq", v: "hosted" },
        { f: "pciPreference", op: "eq", v: "avoid" }
      ]
    },
    { product: "PayU Hosted Checkout", weight: 85, reason: "Ideal redirect checkout for web merchants.",
      conditions: [{ f: "platform", op: "eq", v: "website" }, { f: "checkout", op: "eq", v: "hosted" }]
    },
    { product: "PayU Seamless Checkout", weight: 90, reason: "Embedded checkout keeps customers on your site.",
      conditions: [{ f: "platform", op: "in", v: ["website", "both"] }, { f: "checkout", op: "eq", v: "embedded" }]
    },
    { product: "PayU Web SDK", weight: 80, reason: "JavaScript SDK for seamless web integration.",
      conditions: [
        { f: "platform", op: "in", v: ["website", "both"] },
        { f: "checkout", op: "eq", v: "embedded" },
        { f: "platforms", op: "contains", v: "web" }
      ]
    },
    { product: "PayU Android SDK", weight: 95, reason: "Best for embedded Android payments.",
      conditions: [
        { f: "platform", op: "in", v: ["mobile", "both"] },
        { f: "checkout", op: "eq", v: "embedded" },
        { f: "platforms", op: "contains", v: "android" }
      ]
    },
    { product: "PayU iOS SDK", weight: 95, reason: "Best for embedded iOS payments.",
      conditions: [
        { f: "platform", op: "in", v: ["mobile", "both"] },
        { f: "checkout", op: "eq", v: "embedded" },
        { f: "platforms", op: "contains", v: "ios" }
      ]
    },
    { product: "UPI Intent", weight: 85, reason: "Best mobile UPI conversion via intent flow.",
      conditions: [{ f: "paymentMethods", op: "contains", v: "upi" }, { f: "platform", op: "in", v: ["mobile", "both"] }]
    },
    { product: "UPI Collect", weight: 80, reason: "UPI on desktop via VPA or QR.",
      conditions: [{ f: "paymentMethods", op: "contains", v: "upi" }, { f: "platform", op: "eq", v: "website" }]
    },
    { product: "UPI Collect", weight: 60, reason: "General UPI payment support.",
      conditions: [{ f: "paymentMethods", op: "contains", v: "upi" }]
    },
    { product: "Token Hub / Saved Cards", weight: 90, reason: "PCI-compliant saved card payments.",
      conditions: [{ f: "savedCards", op: "eq", v: true }]
    },
    { product: "Recurring Payments / Subscription", weight: 95, reason: "Automated recurring billing.",
      conditions: [{ f: "recurring", op: "eq", v: true }]
    },
    { product: "Split Settlements", weight: 95, reason: "Multi-vendor marketplace payouts.",
      conditions: [{ f: "splitSettlement", op: "eq", v: true }]
    },
    { product: "Payment Links", weight: 95, reason: "Zero-code payment collection.",
      conditions: [{ f: "checkout", op: "eq", v: "no_code" }]
    },
    { product: "Dynamic QR", weight: 75, reason: "Offline or in-store UPI QR collection.",
      conditions: [{ f: "checkout", op: "eq", v: "no_code" }, { f: "paymentMethods", op: "contains", v: "upi" }]
    },
    { product: "Webhooks", weight: 70, reason: "Essential for real-time payment notifications.",
      conditions: [{ f: "checkout", op: "neq", v: "no_code" }]
    },
    { product: "Refund API", weight: 50, reason: "Programmatic refunds for support automation.",
      conditions: [{ f: "checkout", op: "neq", v: "no_code" }]
    },
    { product: "Transaction Status API", weight: 40, reason: "Payment reconciliation and verification.",
      conditions: [{ f: "checkout", op: "neq", v: "no_code" }]
    },
    { product: "PayU Hosted Checkout", weight: 75, reason: "Minimizes PCI compliance scope.",
      conditions: [{ f: "pciPreference", op: "eq", v: "avoid" }]
    }
  ];

  var FALLBACK = ["PayU Hosted Checkout", "Webhooks", "Refund API"];

  function norm(v) {
    if (v === "true") return true;
    if (v === "false") return false;
    return v;
  }

  function getAns(answers, field) {
    var v = answers[field];
    if (v === undefined || v === null) return undefined;
    return norm(v);
  }

  function matchCond(c, answers) {
    var a = getAns(answers, c.f);
    if (a === undefined) return false;
    var e = c.v;
    switch (c.op) {
      case "eq": return a === e || String(a) === String(e);
      case "neq": return a !== e && String(a) !== String(e);
      case "in":
        var list = Array.isArray(e) ? e : [e];
        var arr = Array.isArray(a) ? a : [String(a)];
        return arr.some(function (x) { return list.indexOf(String(x)) >= 0; });
      case "contains":
        if (!Array.isArray(a)) return String(a) === String(e);
        return a.indexOf(String(e)) >= 0;
      default: return false;
    }
  }

  function matchRule(rule, answers) {
    return rule.conditions.every(function (c) { return matchCond(c, answers); });
  }

  function recommend(answers) {
    var scores = {};
    var reasons = {};
    RULES.forEach(function (r) {
      if (!matchRule(r, answers)) return;
      scores[r.product] = (scores[r.product] || 0) + r.weight;
      if (!reasons[r.product]) reasons[r.product] = r.reason;
    });
    var max = 1;
    Object.keys(scores).forEach(function (k) { if (scores[k] > max) max = scores[k]; });
    var recs = Object.keys(scores).map(function (name) {
      var p = PRODUCTS[name];
      return {
        name: name,
        score: Math.round((scores[name] / max) * 100),
        reason: reasons[name],
        product: p
      };
    }).sort(function (a, b) { return b.score - a.score; }).slice(0, 6);

    if (!recs.length) {
      recs = FALLBACK.map(function (name) {
        return { name: name, score: 50, reason: "A safe starting point for most PayU integrations.", product: PRODUCTS[name] };
      });
    }
    return { recommendations: recs, confidence: recs[0] ? recs[0].score : 0 };
  }

  function explain(answers, recs) {
    var p = recs[0];
    if (!p) return "";
    var parts = ["We recommend " + p.name + " as your primary integration path."];
    if (answers.checkout === "hosted" || answers.pciPreference === "avoid")
      parts.push("This minimizes PCI burden and speeds up go-live.");
    if (answers.recurring === true)
      parts.push("Recurring payment needs are covered by PayU subscription APIs.");
    if (answers.savedCards === true)
      parts.push("Token Hub enables one-click saved card checkout.");
    if (answers.splitSettlement === true)
      parts.push("Split Settlements handles multi-vendor payouts.");
    parts.push(p.reason);
    return parts.join(" ");
  }

  function visibleQuestions(answers) {
    return QUESTIONS.filter(function (q) {
      if (!q.depends) return true;
      var v = answers[q.depends.field];
      if (v === undefined) return false;
      if (Array.isArray(v)) return v.some(function (x) { return q.depends.values.indexOf(String(x)) >= 0; });
      return q.depends.values.indexOf(String(v)) >= 0;
    });
  }

  var answers = {};
  var step = 0;
  var wizardEl = document.getElementById("payu-ipr-wizard");
  var resultsEl = document.getElementById("payu-ipr-results");
  var navEl = document.getElementById("payu-ipr-nav");
  var backBtn = document.getElementById("payu-ipr-back");
  var nextBtn = document.getElementById("payu-ipr-next");
  var progressWrap = document.getElementById("payu-ipr-progress-wrap");
  var stepLabel = document.getElementById("payu-ipr-step-label");
  var pctLabel = document.getElementById("payu-ipr-pct-label");
  var progressFill = document.getElementById("payu-ipr-progress-fill");

  function isAnswered(q) {
    var v = answers[q.field];
    if (q.type === "multi") return Array.isArray(v) && v.length > 0;
    return v !== undefined && v !== "";
  }

  function renderQuestion() {
    var qs = visibleQuestions(answers);
    var q = qs[step];
    if (!q) return;
    var html = '<h3 class="payu-ipr__q-title">' + q.text + '</h3><p class="payu-ipr__q-hint">' + q.hint + '</p><div class="payu-ipr__options">';
    q.options.forEach(function (opt) {
      var on = false;
      if (q.type === "multi") on = (answers[q.field] || []).indexOf(opt.v) >= 0;
      else on = answers[q.field] === opt.v;
      html += '<button type="button" class="payu-ipr__option' + (on ? ' payu-ipr__option--on' : '') + '" data-field="' + q.field + '" data-type="' + q.type + '" data-value="' + String(opt.v) + '">' + opt.l + '</button>';
    });
    html += "</div>";
    wizardEl.innerHTML = html;
    wizardEl.hidden = false;
    resultsEl.hidden = true;
    navEl.hidden = false;
    progressWrap.hidden = false;

    var pct = Math.round(((step + 1) / qs.length) * 100);
    stepLabel.textContent = "Question " + (step + 1) + " of " + qs.length;
    pctLabel.textContent = pct + "%";
    progressFill.style.width = pct + "%";

    backBtn.disabled = step === 0;
    nextBtn.disabled = !isAnswered(q);
    nextBtn.textContent = step < qs.length - 1 ? "Next →" : "Get recommendations →";

    wizardEl.querySelectorAll(".payu-ipr__option").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var field = btn.getAttribute("data-field");
        var type = btn.getAttribute("data-type");
        var val = btn.getAttribute("data-value");
        if (type === "bool") val = val === "true";
        if (type === "multi") {
          var arr = answers[field] ? answers[field].slice() : [];
          var i = arr.indexOf(val);
          if (i >= 0) arr.splice(i, 1); else arr.push(val);
          answers[field] = arr;
        } else {
          answers[field] = val;
        }
        renderQuestion();
      });
    });
  }

  function renderResults() {
    var out = recommend(answers);
    var recs = out.recommendations;
    var primary = recs[0];
    var rest = recs.slice(1);
    var exp = explain(answers, recs);

    var html = '<div class="payu-ipr__explain">' + exp + '</div>';
    if (primary && primary.product) {
      var p = primary.product;
      html += '<div class="payu-ipr__primary"><div class="payu-ipr__primary-hd">Primary recommendation</div><div class="payu-ipr__primary-bd">';
      html += '<div style="display:flex;justify-content:space-between;align-items:flex-start;gap:.5rem">';
      html += '<div><h3 style="margin:0;font-size:1.1rem;color:var(--payu-ipr-navy)">' + primary.name + '</h3>';
      html += '<p style="margin:.2rem 0 0;font-size:12px;color:var(--payu-ipr-muted);text-transform:capitalize">' + p.category + '</p></div>';
      html += '<span class="payu-ipr__score">' + primary.score + '%</span></div>';
      html += '<p style="margin:.65rem 0;font-size:13px">' + p.description + '</p>';
      html += '<div class="payu-ipr__tags"><span class="payu-ipr__tag payu-ipr__tag--' + p.complexity + '">' + p.complexity + ' complexity</span>';
      html += '<span class="payu-ipr__tag">~' + p.goLiveDays + ' days to go-live</span></div>';
      html += '<div class="payu-ipr__cols"><div><strong style="font-size:12px;color:#065f46">Pros</strong><ul class="payu-ipr__list">';
      p.pros.forEach(function (x) { html += "<li>" + x + "</li>"; });
      html += '</ul></div><div><strong style="font-size:12px;color:#991b1b">Cons</strong><ul class="payu-ipr__list">';
      p.cons.forEach(function (x) { html += "<li>" + x + "</li>"; });
      html += '</ul></div></div>';
      html += '<a class="payu-ipr__link" href="' + p.docsUrl + '" target="_blank" rel="noopener noreferrer">View documentation →</a>';
      html += '</div></div>';
    }
    if (rest.length) {
      html += '<p style="font-weight:600;color:var(--payu-ipr-navy);margin:0 0 .5rem">Also recommended</p><div class="payu-ipr__cards">';
      rest.forEach(function (r) {
        if (!r.product) return;
        html += '<div class="payu-ipr__card"><h4>' + r.name + ' <span style="color:var(--payu-ipr-green);font-size:12px">' + r.score + '%</span></h4>';
        html += '<p style="margin:0 0 .35rem;font-size:12px;color:var(--payu-ipr-muted)">' + r.reason + '</p>';
        html += '<a class="payu-ipr__link" href="' + r.product.docsUrl + '" target="_blank" rel="noopener noreferrer">Docs →</a></div>';
      });
      html += '</div>';
    }
    resultsEl.innerHTML = html;
    wizardEl.hidden = true;
    resultsEl.hidden = false;
    progressWrap.hidden = true;
    backBtn.disabled = false;
    nextBtn.textContent = "Start over";
    nextBtn.disabled = false;
  }

  backBtn.addEventListener("click", function () {
    if (!resultsEl.hidden) {
      step = 0;
      answers = {};
      renderQuestion();
      return;
    }
    if (step > 0) { step--; renderQuestion(); }
  });

  nextBtn.addEventListener("click", function () {
    if (!resultsEl.hidden) {
      step = 0;
      answers = {};
      renderQuestion();
      return;
    }
    var qs = visibleQuestions(answers);
    if (step < qs.length - 1) { step++; renderQuestion(); }
    else renderResults();
  });

  renderQuestion();
})();
</script>
`}</HTMLBlock>

<br />
