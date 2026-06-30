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
  4 click-only questions · auto-advances · scoped under #payu-ipr
-->
<div id="payu-ipr" class="payu-ipr" role="region" aria-label="PayU Integration Path Recommender">
  <div class="payu-ipr__shell">
    <header class="payu-ipr__header">
      <div class="payu-ipr__badge">PayU DevEx</div>
      <h2 class="payu-ipr__title">Which integration is right for you?</h2>
      <p class="payu-ipr__subtitle">Tap an option below — no typing required. Four quick questions.</p>
    </header>

    <div class="payu-ipr__progress-wrap" id="payu-ipr-progress-wrap">
      <div class="payu-ipr__progress-meta">
        <span id="payu-ipr-step-label">Question 1 of 4</span>
        <span id="payu-ipr-pct-label">25%</span>
      </div>
      <div class="payu-ipr__progress-bar"><div class="payu-ipr__progress-fill" id="payu-ipr-progress-fill" style="width:25%"></div></div>
    </div>

    <div id="payu-ipr-wizard" class="payu-ipr__panel"></div>
    <div id="payu-ipr-results" class="payu-ipr__panel" hidden></div>

    <div class="payu-ipr__nav" id="payu-ipr-nav">
      <button type="button" class="payu-ipr__btn payu-ipr__btn--ghost" id="payu-ipr-back" hidden>← Back</button>
      <button type="button" class="payu-ipr__btn payu-ipr__btn--primary" id="payu-ipr-restart" hidden>Start over</button>
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
  #payu-ipr .payu-ipr__title { margin: 0 0 .35rem; font-size: 1.25rem; font-weight: 700; color: var(--payu-ipr-navy); }
  #payu-ipr .payu-ipr__subtitle { margin: 0; color: var(--payu-ipr-muted); font-size: 13px; }
  #payu-ipr .payu-ipr__progress-wrap { margin-bottom: 1rem; }
  #payu-ipr .payu-ipr__progress-meta { display: flex; justify-content: space-between; font-size: 12px; color: var(--payu-ipr-muted); margin-bottom: .35rem; }
  #payu-ipr .payu-ipr__progress-bar { height: 6px; background: #e5e7eb; border-radius: 999px; overflow: hidden; }
  #payu-ipr .payu-ipr__progress-fill { height: 100%; background: var(--payu-ipr-green); border-radius: 999px; transition: width .25s ease; }
  #payu-ipr .payu-ipr__q-title { margin: 0 0 .25rem; font-size: 1.05rem; font-weight: 600; color: var(--payu-ipr-navy); }
  #payu-ipr .payu-ipr__q-hint { margin: 0 0 .75rem; font-size: 12px; color: var(--payu-ipr-muted); }
  #payu-ipr .payu-ipr__options { display: grid; gap: .5rem; }
  #payu-ipr .payu-ipr__option {
    width: 100%; text-align: left; padding: .8rem .95rem;
    border: 2px solid var(--payu-ipr-border); border-radius: 10px;
    background: var(--payu-ipr-card); cursor: pointer; font: inherit; color: inherit;
    transition: border-color .15s, background .15s, transform .1s;
  }
  #payu-ipr .payu-ipr__option:hover { border-color: rgba(0,166,81,.5); transform: translateY(-1px); }
  #payu-ipr .payu-ipr__option:active { transform: translateY(0); }
  #payu-ipr .payu-ipr__option-desc { display: block; margin-top: .2rem; font-size: 12px; color: var(--payu-ipr-muted); font-weight: 400; }
  #payu-ipr .payu-ipr__nav { display: flex; justify-content: space-between; gap: .75rem; margin-top: 1rem; padding-top: .75rem; border-top: 1px solid var(--payu-ipr-border); }
  #payu-ipr .payu-ipr__btn { padding: .55rem 1rem; border-radius: 8px; font-size: 13px; font-weight: 600; cursor: pointer; border: 1px solid transparent; }
  #payu-ipr .payu-ipr__btn--primary { background: var(--payu-ipr-green); color: #fff; }
  #payu-ipr .payu-ipr__btn--primary:hover { background: var(--payu-ipr-green-dark); }
  #payu-ipr .payu-ipr__btn--ghost { background: #fff; border-color: var(--payu-ipr-border); color: #374151; }
  #payu-ipr .payu-ipr__explain { margin-bottom: 1rem; padding: .85rem 1rem; border-radius: 10px; border: 1px solid rgba(0,166,81,.25); background: rgba(0,166,81,.06); font-size: 13px; color: #374151; }
  #payu-ipr .payu-ipr__primary { border: 2px solid var(--payu-ipr-green); border-radius: 12px; overflow: hidden; margin-bottom: 1rem; }
  #payu-ipr .payu-ipr__primary-hd { background: var(--payu-ipr-green); color: #fff; font-size: 12px; font-weight: 600; padding: .45rem .9rem; }
  #payu-ipr .payu-ipr__primary-bd { padding: 1rem; }
  #payu-ipr .payu-ipr__score { font-size: 1.5rem; font-weight: 700; color: var(--payu-ipr-green); }
  #payu-ipr .payu-ipr__tags { display: flex; flex-wrap: wrap; gap: .35rem; margin: .5rem 0; }
  #payu-ipr .payu-ipr__tag { font-size: 11px; font-weight: 600; padding: .2rem .55rem; border-radius: 999px; background: #f3f4f6; color: #374151; text-transform: capitalize; }
  #payu-ipr .payu-ipr__tag--low { background: #d1fae5; color: #065f46; }
  #payu-ipr .payu-ipr__tag--medium { background: #fef3c7; color: #92400e; }
  #payu-ipr .payu-ipr__tag--high { background: #fee2e2; color: #991b1b; }
  #payu-ipr .payu-ipr__cols { display: grid; gap: .75rem; }
  @media (min-width: 560px) { #payu-ipr .payu-ipr__cols { grid-template-columns: 1fr 1fr; } }
  #payu-ipr .payu-ipr__list { margin: 0; padding-left: 1.1rem; font-size: 13px; color: #4b5563; }
  #payu-ipr .payu-ipr__list li { margin: .2rem 0; }
  #payu-ipr .payu-ipr__cards { display: grid; gap: .6rem; }
  @media (min-width: 560px) { #payu-ipr .payu-ipr__cards { grid-template-columns: 1fr 1fr; } }
  #payu-ipr .payu-ipr__card { border: 1px solid var(--payu-ipr-border); border-radius: 10px; padding: .75rem; background: var(--payu-ipr-bg); }
  #payu-ipr .payu-ipr__card h4 { margin: 0 0 .25rem; font-size: 14px; color: var(--payu-ipr-navy); }
  #payu-ipr .payu-ipr__link { display: inline-block; margin-top: .65rem; font-size: 13px; font-weight: 600; color: var(--payu-ipr-green); text-decoration: none; }
  #payu-ipr .payu-ipr__link:hover { text-decoration: underline; }
  #payu-ipr [hidden] { display: none !important; }
</style>

<script>
(function () {
  function boot() {
    var root = document.getElementById("payu-ipr");
    if (!root || root.getAttribute("data-ipr-ready") === "1") return;
    root.setAttribute("data-ipr-ready", "1");

    var PRODUCTS = {
      "PayU Hosted Checkout": { category: "checkout", description: "Redirect to PayU-hosted payment page. Minimal PCI burden, fastest go-live.", pros: ["Lowest PCI scope", "Fast integration (1–3 days)", "All payment methods"], cons: ["Redirect flow", "Limited UI customization"], complexity: "low", goLiveDays: 3, docsUrl: "https://docs.payu.in/docs/hosted-checkout" },
      "PayU Seamless Checkout": { category: "checkout", description: "Embed payment on your website; PayU secures card data.", pros: ["Native checkout UX", "Customer stays on site"], cons: ["More frontend work", "Higher PCI scope than hosted"], complexity: "medium", goLiveDays: 10, docsUrl: "https://docs.payu.in/docs/seamless-checkout" },
      "PayU Android SDK": { category: "sdk", description: "Native Android in-app payments with UPI Intent and cards.", pros: ["Native Android UX", "UPI Intent support"], cons: ["Android only", "Native dev skills"], complexity: "medium", goLiveDays: 14, docsUrl: "https://docs.payu.in/docs/android-sdk" },
      "PayU iOS SDK": { category: "sdk", description: "Native iOS in-app payments.", pros: ["Native iOS UX", "In-app flow"], cons: ["iOS only", "Swift/Obj-C skills"], complexity: "medium", goLiveDays: 14, docsUrl: "https://docs.payu.in/docs/ios-sdk" },
      "PayU Web SDK": { category: "sdk", description: "JavaScript SDK for web embedded checkout.", pros: ["Any web framework", "Embedded checkout"], cons: ["Web only", "Browser testing"], complexity: "medium", goLiveDays: 7, docsUrl: "https://docs.payu.in/docs/web-sdk" },
      "UPI Intent": { category: "upi", description: "Deep-link to UPI apps for one-tap mobile payments.", pros: ["Best UPI conversion on mobile"], cons: ["Mobile only"], complexity: "low", goLiveDays: 5, docsUrl: "https://docs.payu.in/docs/upi-intent" },
      "UPI Collect": { category: "upi", description: "UPI via VPA entry or QR — works on web and mobile.", pros: ["Desktop + mobile", "QR support"], cons: ["Manual VPA entry"], complexity: "low", goLiveDays: 5, docsUrl: "https://docs.payu.in/docs/upi-collect" },
      "Token Hub / Saved Cards": { category: "tokenization", description: "One-click repeat payments with tokenized cards.", pros: ["Higher repeat conversion", "PCI-compliant tokens"], cons: ["Extra integration step"], complexity: "medium", goLiveDays: 10, docsUrl: "https://docs.payu.in/docs/token-hub" },
      "Recurring Payments / Subscription": { category: "subscription", description: "Automated recurring billing and standing instructions.", pros: ["Subscription billing", "SI on cards & UPI"], cons: ["Mandate flows", "RBI compliance"], complexity: "high", goLiveDays: 21, docsUrl: "https://docs.payu.in/docs/recurring-payments" },
      "Split Settlements": { category: "marketplace", description: "Split payouts between marketplace and vendors.", pros: ["Multi-vendor payouts"], cons: ["Vendor onboarding"], complexity: "high", goLiveDays: 21, docsUrl: "https://docs.payu.in/docs/split-settlements" },
      "Payment Links": { category: "links", description: "Shareable payment links — zero code.", pros: ["No integration code", "Share via SMS/email"], cons: ["Not for high-volume checkout"], complexity: "low", goLiveDays: 1, docsUrl: "https://docs.payu.in/docs/payment-links" },
      "Dynamic QR": { category: "qr", description: "Dynamic UPI QR for offline or in-store collection.", pros: ["Offline UPI collection"], cons: ["Needs display + polling"], complexity: "low", goLiveDays: 5, docsUrl: "https://docs.payu.in/docs/dynamic-qr" },
      "Webhooks": { category: "api", description: "Real-time payment status notifications.", pros: ["Reliable reconciliation"], cons: ["Public endpoint needed"], complexity: "low", goLiveDays: 2, docsUrl: "https://docs.payu.in/docs/webhooks" },
      "Refund API": { category: "api", description: "Programmatic refunds.", pros: ["Automated refunds"], cons: ["Settlement timing"], complexity: "low", goLiveDays: 2, docsUrl: "https://docs.payu.in/docs/refund-api" },
      "Transaction Status API": { category: "api", description: "Query payment status for reconciliation.", pros: ["Webhook fallback"], cons: ["Use with webhooks"], complexity: "low", goLiveDays: 1, docsUrl: "https://docs.payu.in/docs/transaction-status-api" }
    };

    /* 4 questions — each answer is one tap; last question shows results immediately */
    var QUESTIONS = [
      {
        id: "build",
        text: "What are you building?",
        hint: "Tap one option",
        options: [
          { id: "website", label: "Website", desc: "Web checkout in browser" },
          { id: "android", label: "Android app", desc: "Native or hybrid mobile app" },
          { id: "ios", label: "iOS app", desc: "Native or hybrid mobile app" },
          { id: "both", label: "Website + mobile apps", desc: "Omnichannel presence" }
        ]
      },
      {
        id: "checkout",
        text: "How should customers complete payment?",
        hint: "Tap one option",
        options: [
          { id: "hosted", label: "Redirect / Hosted checkout", desc: "Fastest setup — PayU hosts the payment page" },
          { id: "embedded", label: "Embedded on my site or app", desc: "Seamless UX — payment stays in your UI" },
          { id: "no_code", label: "Payment links or QR", desc: "No code — share a link or display a QR" }
        ]
      },
      {
        id: "payments",
        text: "Which payment methods do you need?",
        hint: "Tap one option",
        options: [
          { id: "cards", label: "Cards only", desc: "Credit & debit cards" },
          { id: "upi", label: "UPI only", desc: "Intent, collect, or QR" },
          { id: "cards_upi", label: "Cards + UPI", desc: "Most common for India checkout" },
          { id: "all", label: "All methods", desc: "Cards, UPI, net banking, wallets, EMI" }
        ]
      },
      {
        id: "extra",
        text: "Do you need any of these?",
        hint: "Tap one option — we'll show your recommendation next",
        options: [
          { id: "none", label: "Standard checkout only", desc: "No subscriptions, saved cards, or marketplace splits" },
          { id: "recurring", label: "Recurring / subscriptions", desc: "Standing instructions, SI, auto-debit" },
          { id: "saved", label: "Saved cards / one-click", desc: "Token Hub for returning customers" },
          { id: "marketplace", label: "Marketplace split settlement", desc: "Pay vendors from one transaction" }
        ]
      }
    ];

    var RULES = [
      { product: "PayU Hosted Checkout", weight: 95, reason: "Best for fast go-live with minimal PCI burden.", when: function (a) { return a.checkout === "hosted" && a.build !== "android" && a.build !== "ios"; } },
      { product: "PayU Hosted Checkout", weight: 85, reason: "Ideal redirect checkout for web merchants.", when: function (a) { return a.build === "website" && a.checkout === "hosted"; } },
      { product: "PayU Seamless Checkout", weight: 90, reason: "Keeps customers on your website during payment.", when: function (a) { return (a.build === "website" || a.build === "both") && a.checkout === "embedded"; } },
      { product: "PayU Web SDK", weight: 82, reason: "JavaScript SDK for embedded web payments.", when: function (a) { return (a.build === "website" || a.build === "both") && a.checkout === "embedded"; } },
      { product: "PayU Android SDK", weight: 96, reason: "Best fit for embedded payments in Android apps.", when: function (a) { return (a.build === "android" || a.build === "both") && a.checkout === "embedded"; } },
      { product: "PayU iOS SDK", weight: 96, reason: "Best fit for embedded payments in iOS apps.", when: function (a) { return (a.build === "ios" || a.build === "both") && a.checkout === "embedded"; } },
      { product: "UPI Intent", weight: 88, reason: "Highest UPI conversion on mobile via app intent.", when: function (a) { return a.payments !== "cards" && (a.build === "android" || a.build === "ios" || a.build === "both"); } },
      { product: "UPI Collect", weight: 80, reason: "UPI on web via VPA or QR code.", when: function (a) { return a.payments !== "cards" && a.build === "website"; } },
      { product: "UPI Collect", weight: 65, reason: "Supports UPI across channels.", when: function (a) { return a.payments === "upi" || a.payments === "cards_upi" || a.payments === "all"; } },
      { product: "Payment Links", weight: 95, reason: "Zero-code collection via shareable links.", when: function (a) { return a.checkout === "no_code"; } },
      { product: "Dynamic QR", weight: 78, reason: "In-store or offline UPI via dynamic QR.", when: function (a) { return a.checkout === "no_code" && a.payments !== "cards"; } },
      { product: "Recurring Payments / Subscription", weight: 95, reason: "Required for subscriptions and standing instructions.", when: function (a) { return a.extra === "recurring"; } },
      { product: "Token Hub / Saved Cards", weight: 92, reason: "Enables PCI-compliant saved card checkout.", when: function (a) { return a.extra === "saved"; } },
      { product: "Split Settlements", weight: 95, reason: "Splits one payment across marketplace vendors.", when: function (a) { return a.extra === "marketplace"; } },
      { product: "Webhooks", weight: 70, reason: "Essential for production payment notifications.", when: function (a) { return a.checkout !== "no_code"; } },
      { product: "Refund API", weight: 50, reason: "Automate refunds from your backend.", when: function (a) { return a.checkout !== "no_code"; } },
      { product: "Transaction Status API", weight: 40, reason: "Reconcile payments and verify status.", when: function (a) { return a.checkout !== "no_code"; } }
    ];

    var FALLBACK = ["PayU Hosted Checkout", "Webhooks", "Refund API"];
    var TOTAL = QUESTIONS.length;
    var step = 0;
    var picks = {};

    var wizardEl = root.querySelector("#payu-ipr-wizard");
    var resultsEl = root.querySelector("#payu-ipr-results");
    var progressWrap = root.querySelector("#payu-ipr-progress-wrap");
    var stepLabel = root.querySelector("#payu-ipr-step-label");
    var pctLabel = root.querySelector("#payu-ipr-pct-label");
    var progressFill = root.querySelector("#payu-ipr-progress-fill");
    var backBtn = root.querySelector("#payu-ipr-back");
    var restartBtn = root.querySelector("#payu-ipr-restart");

    function recommend() {
      var scores = {};
      var reasons = {};
      RULES.forEach(function (r) {
        if (!r.when(picks)) return;
        scores[r.product] = (scores[r.product] || 0) + r.weight;
        if (!reasons[r.product]) reasons[r.product] = r.reason;
      });
      var max = 1;
      Object.keys(scores).forEach(function (k) { if (scores[k] > max) max = scores[k]; });
      var recs = Object.keys(scores).map(function (name) {
        return { name: name, score: Math.round((scores[name] / max) * 100), reason: reasons[name], product: PRODUCTS[name] };
      }).filter(function (r) { return r.product; }).sort(function (a, b) { return b.score - a.score; }).slice(0, 5);

      if (!recs.length) {
        recs = FALLBACK.map(function (name) {
          return { name: name, score: 50, reason: "A reliable starting point for most PayU integrations.", product: PRODUCTS[name] };
        });
      }
      return recs;
    }

    function explain(recs) {
      var p = recs[0];
      if (!p) return "";
      var parts = ["We recommend " + p.name + " as your primary integration."];
      if (picks.checkout === "hosted") parts.push("Hosted checkout keeps PCI scope low and speeds up go-live.");
      if (picks.checkout === "embedded") parts.push("Embedded checkout gives a seamless experience on your site or app.");
      if (picks.extra === "recurring") parts.push("Add Recurring Payments APIs for subscriptions.");
      if (picks.extra === "saved") parts.push("Pair with Token Hub for one-click saved cards.");
      if (picks.extra === "marketplace") parts.push("Split Settlements handles vendor payouts.");
      parts.push(p.reason);
      return parts.join(" ");
    }

    function setProgress(n) {
      var pct = Math.round((n / TOTAL) * 100);
      stepLabel.textContent = "Question " + n + " of " + TOTAL;
      pctLabel.textContent = pct + "%";
      progressFill.style.width = pct + "%";
    }

    function renderQuestion() {
      var q = QUESTIONS[step];
      if (!q) return;

      var html = '<h3 class="payu-ipr__q-title">' + q.text + '</h3>';
      html += '<p class="payu-ipr__q-hint">' + q.hint + '</p><div class="payu-ipr__options">';
      q.options.forEach(function (opt) {
        html += '<button type="button" class="payu-ipr__option" data-qid="' + q.id + '" data-oid="' + opt.id + '">';
        html += opt.label + '<span class="payu-ipr__option-desc">' + opt.desc + '</span></button>';
      });
      html += "</div>";

      wizardEl.innerHTML = html;
      wizardEl.hidden = false;
      resultsEl.hidden = true;
      progressWrap.hidden = false;
      backBtn.hidden = step === 0;
      restartBtn.hidden = true;
      setProgress(step + 1);
    }

    function renderResults() {
      var recs = recommend();
      var primary = recs[0];
      var rest = recs.slice(1);
      var html = '<div class="payu-ipr__explain">' + explain(recs) + '</div>';

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
      backBtn.hidden = true;
      restartBtn.hidden = false;
    }

    function onOptionClick(qid, oid) {
      picks[qid] = oid;
      if (step < TOTAL - 1) {
        step += 1;
        renderQuestion();
      } else {
        renderResults();
      }
    }

    function reset() {
      step = 0;
      picks = {};
      renderQuestion();
    }

    /* Event delegation — survives re-renders and ReadMe re-injection */
    root.addEventListener("click", function (e) {
      var opt = e.target.closest(".payu-ipr__option");
      if (opt && root.contains(opt)) {
        e.preventDefault();
        onOptionClick(opt.getAttribute("data-qid"), opt.getAttribute("data-oid"));
        return;
      }
      if (e.target === backBtn || (e.target.closest && e.target.closest("#payu-ipr-back"))) {
        e.preventDefault();
        if (step > 0) { step -= 1; renderQuestion(); }
        return;
      }
      if (e.target === restartBtn || (e.target.closest && e.target.closest("#payu-ipr-restart"))) {
        e.preventDefault();
        reset();
      }
    });

    renderQuestion();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
</script>
`}</HTMLBlock>

<br />
