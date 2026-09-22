---
title: How Payment Links Works
excerpt: >-
  Understand the complete end-to-end lifecycle of a PayU Payment Link — from
  creating an account to receiving funds in your bank account.
deprecated: false
hidden: true
metadata:
  title: How Payment Links Works | PayU Developer Docs
  description: >-
    End-to-end lifecycle of a PayU Payment Link — account setup, link creation,
    sending to customers, payment, status tracking, and fund settlement.
  keywords:
    - how payu payment links works
    - payu payment link lifecycle
    - payment link flow payu
    - payu payment link workflow
    - payment link end to end payu
    - how does payment link work india
    - payu payment link steps
    - payment link process payu
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-links
      title: Payment Links
      type: basic
    - slug: create-a-payment-link
      title: Create a Payment Link
      type: basic
    - slug: manage-payment-links
      title: Manage Payment Links
      type: basic
    - slug: payment-links-errors-and-troubleshooting
      title: Errors and Troubleshooting
      type: basic
    - slug: payment-links-faqs
      title: FAQs (Frequently Asked Questions)
      type: basic
---
Understand the complete end-to-end flow of how PayU Payment Links works. Starting from creating your account to receiving funds in your bank account.

<HTMLBlock>{`
<style>
# pf-diagram * { box-sizing: border-box; margin: 0; padding: 0; }
# pf-diagram {
  font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
  background: linear-gradient(135deg, #E8F5EE 0%, #F5FAF7 60%, #EAF6F0 100%);
  border-radius: 14px;
  padding: 44px 24px 32px;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-x: auto;
}
# pf-diagram .payu-badge {
  background: #00A550; color: white; font-size: 13px; font-weight: 700;
  letter-spacing: 0.5px; padding: 4px 14px; border-radius: 20px;
  margin-bottom: 20px; display: inline-block;
}
# pf-diagram .flow {
  display: flex; align-items: center; gap: 0; position: relative;
}
# pf-diagram .step {
  display: flex; flex-direction: column; align-items: center;
  position: relative; opacity: 0; transform: translateY(16px);
  animation: pfSlideIn 0.5s ease forwards;
}
# pf-diagram .step:nth-child(1)  { animation-delay: 0.1s; }
# pf-diagram .step:nth-child(3)  { animation-delay: 0.3s; }
# pf-diagram .step:nth-child(5)  { animation-delay: 0.5s; }
# pf-diagram .step:nth-child(7)  { animation-delay: 0.7s; }
# pf-diagram .step:nth-child(9)  { animation-delay: 0.9s; }
# pf-diagram .step:nth-child(11) { animation-delay: 1.1s; }
@keyframes pfSlideIn { to { opacity: 1; transform: translateY(0); } }
# pf-diagram .card {
  width: 148px; padding: 34px 14px 18px;
  background: white; border-radius: 18px;
  box-shadow: 0 4px 20px rgba(0,68,32,0.09), 0 1px 4px rgba(0,68,32,0.05);
  display: flex; flex-direction: column; align-items: center;
  text-align: center; position: relative; border-top: 4px solid #00A550;
}
# pf-diagram .badge {
  position: absolute; top: -20px; left: 50%; transform: translateX(-50%);
  width: 40px; height: 40px; background: #00A550; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 15px; font-weight: 700; color: white;
  box-shadow: 0 4px 12px rgba(0,165,80,0.35);
  animation: pfPulse 2.5s ease-in-out infinite;
}
# pf-diagram .step:nth-child(1)  .badge { animation-delay: 0s; }
# pf-diagram .step:nth-child(3)  .badge { animation-delay: 0.4s; }
# pf-diagram .step:nth-child(5)  .badge { animation-delay: 0.8s; }
# pf-diagram .step:nth-child(7)  .badge { animation-delay: 1.2s; }
# pf-diagram .step:nth-child(9)  .badge { animation-delay: 1.6s; }
# pf-diagram .step:nth-child(11) .badge { animation-delay: 2.0s; }
@keyframes pfPulse {
  0%,100% { box-shadow: 0 4px 12px rgba(0,165,80,0.35); }
  50%      { box-shadow: 0 4px 20px rgba(0,165,80,0.7), 0 0 0 8px rgba(0,165,80,0.1); }
}
# pf-diagram .icon-wrap {
  width: 52px; height: 52px; background: #E8F5EE; border-radius: 14px;
  display: flex; align-items: center; justify-content: center; margin-bottom: 12px;
}
# pf-diagram .icon-wrap svg { width: 26px; height: 26px; }
# pf-diagram .card-title { font-size: 12.5px; font-weight: 700; color: #1B2D3E; margin-bottom: 4px; line-height: 1.3; }
# pf-diagram .card-desc  { font-size: 11px; color: #6B7A8D; line-height: 1.5; }
# pf-diagram .arrow-wrap {
  position: relative; width: 68px; height: 2px;
  flex-shrink: 0; margin: 0 2px; align-self: center;
}
# pf-diagram .arrow-line {
  position: absolute; top: 0; left: 0; right: 12px; height: 2px;
  background: repeating-linear-gradient(to right,#00A550 0,#00A550 6px,transparent 6px,transparent 10px);
  opacity: 0.4;
}
# pf-diagram .arrow-head {
  position: absolute; right: 0; top: -5px;
  width: 0; height: 0;
  border-left: 10px solid #00A550;
  border-top: 6px solid transparent;
  border-bottom: 6px solid transparent;
  opacity: 0.8;
}
# pf-diagram .dot {
  position: absolute; top: -5px; width: 12px; height: 12px;
  background: #00A550; border-radius: 50%;
  box-shadow: 0 0 8px rgba(0,165,80,0.6);
  animation: pfMoveDot 1.8s ease-in-out infinite;
}
# pf-diagram .dot2 { animation-delay: 0.9s; opacity: 0.6; width: 8px; height: 8px; top: -3px; }
# pf-diagram .arrow-wrap:nth-of-type(2)  .dot  { animation-delay: 0.2s; }
# pf-diagram .arrow-wrap:nth-of-type(2)  .dot2 { animation-delay: 1.1s; }
# pf-diagram .arrow-wrap:nth-of-type(4)  .dot  { animation-delay: 0.4s; }
# pf-diagram .arrow-wrap:nth-of-type(4)  .dot2 { animation-delay: 1.3s; }
# pf-diagram .arrow-wrap:nth-of-type(6)  .dot  { animation-delay: 0.6s; }
# pf-diagram .arrow-wrap:nth-of-type(6)  .dot2 { animation-delay: 1.5s; }
# pf-diagram .arrow-wrap:nth-of-type(8)  .dot  { animation-delay: 0.8s; }
# pf-diagram .arrow-wrap:nth-of-type(8)  .dot2 { animation-delay: 1.7s; }
# pf-diagram .arrow-wrap:nth-of-type(10) .dot  { animation-delay: 1.0s; }
# pf-diagram .arrow-wrap:nth-of-type(10) .dot2 { animation-delay: 1.9s; }
@keyframes pfMoveDot {
  0%   { left: 0%;              opacity: 0; }
  8%   { opacity: 1; }
  88%  { opacity: 1; }
  100% { left: calc(100% - 12px); opacity: 0; }
}
# pf-diagram .refund-note {
  margin-top: 28px; font-size: 11.5px; color: #00A550; font-weight: 600;
  text-align: center; background: #E8F5EE; border: 1.5px dashed #00A550;
  border-radius: 8px; padding: 8px 20px; display: inline-block;
}
# pf-diagram .refund-note span { font-weight: 400; color: #6B7A8D; margin-left: 6px; }
</style>

<div id="pf-diagram">
  <span class="payu-badge">PayU</span>
  <div class="flow">
    <div class="step">
      <div class="card">
        <div class="badge">1</div>
        <div class="icon-wrap"><svg viewBox="0 0 26 26" fill="none"><circle cx="13" cy="9" r="5" stroke="#00A550" stroke-width="2.2"></circle><path d="M4 22c0-4.418 4.03-8 9-8s9 3.582 9 8" stroke="#00A550" stroke-width="2.2" stroke-linecap="round"></path></svg></div>
        <div class="card-title">Create Account</div>
        <div class="card-desc">Sign up and complete KYC</div>
      </div>
    </div>
    <div class="arrow-wrap"><div class="arrow-line"></div><div class="arrow-head"></div><div class="dot"></div><div class="dot dot2"></div></div>
    <div class="step">
      <div class="card">
        <div class="badge">2</div>
        <div class="icon-wrap"><svg viewBox="0 0 26 26" fill="none"><rect x="5" y="3" width="16" height="20" rx="2.5" stroke="#00A550" stroke-width="2.2"></rect><line x1="9" y1="9" x2="17" y2="9" stroke="#00A550" stroke-width="1.8"></line><line x1="9" y1="13" x2="17" y2="13" stroke="#00A550" stroke-width="1.8"></line><line x1="9" y1="17" x2="13" y2="17" stroke="#00A550" stroke-width="1.8"></line></svg></div>
        <div class="card-title">Create Link</div>
        <div class="card-desc">Set amount, expiry, and options</div>
      </div>
    </div>
    <div class="arrow-wrap"><div class="arrow-line"></div><div class="arrow-head"></div><div class="dot"></div><div class="dot dot2"></div></div>
    <div class="step">
      <div class="card">
        <div class="badge">3</div>
        <div class="icon-wrap"><svg viewBox="0 0 26 26" fill="none"><rect x="3" y="15" width="20" height="9" rx="3" stroke="#00A550" stroke-width="2.2"></rect><line x1="13" y1="15" x2="13" y2="4" stroke="#00A550" stroke-width="2.2" stroke-linecap="round"></line><path d="M8 8l5-5 5 5" stroke="#00A550" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg></div>
        <div class="card-title">Send the Link</div>
        <div class="card-desc">Via SMS, Email, or WhatsApp</div>
      </div>
    </div>
    <div class="arrow-wrap"><div class="arrow-line"></div><div class="arrow-head"></div><div class="dot"></div><div class="dot dot2"></div></div>
    <div class="step">
      <div class="card">
        <div class="badge">4</div>
        <div class="icon-wrap"><svg viewBox="0 0 26 26" fill="none"><rect x="3" y="7" width="20" height="14" rx="3" stroke="#00A550" stroke-width="2.2"></rect><line x1="3" y1="11" x2="23" y2="11" stroke="#00A550" stroke-width="3"></line><rect x="6" y="14" width="7" height="4" rx="1.5" fill="#00A550"></rect></svg></div>
        <div class="card-title">Customer Pays</div>
        <div class="card-desc">Secure PayU checkout page</div>
      </div>
    </div>
    <div class="arrow-wrap"><div class="arrow-line"></div><div class="arrow-head"></div><div class="dot"></div><div class="dot dot2"></div></div>
    <div class="step">
      <div class="card">
        <div class="badge">5</div>
        <div class="icon-wrap"><svg viewBox="0 0 26 26" fill="none"><circle cx="11" cy="11" r="7" stroke="#00A550" stroke-width="2.2"></circle><line x1="16" y1="16" x2="23" y2="23" stroke="#00A550" stroke-width="2.8" stroke-linecap="round"></line></svg></div>
        <div class="card-title">Check Status</div>
        <div class="card-desc">Dashboard or webhook</div>
      </div>
    </div>
    <div class="arrow-wrap"><div class="arrow-line"></div><div class="arrow-head"></div><div class="dot"></div><div class="dot dot2"></div></div>
    <div class="step">
      <div class="card">
        <div class="badge">6</div>
        <div class="icon-wrap"><svg viewBox="0 0 26 26" fill="none"><rect x="2" y="8" width="22" height="14" rx="3.5" stroke="#00A550" stroke-width="2.2"></rect><rect x="14" y="12" width="9" height="9" rx="2.5" stroke="#00A550" stroke-width="2"></rect><circle cx="18.5" cy="16.5" r="2" fill="#00A550"></circle><line x1="2" y1="13" x2="14" y2="13" stroke="#00A550" stroke-width="1.5" stroke-dasharray="2,2" opacity="0.45"></line></svg></div>
        <div class="card-title">Funds Settled</div>
        <div class="card-desc">To your bank, minus fees</div>
      </div>
    </div>
  </div>
  <div class="refund-note">↩ Optional: Initiate a Refund <span>— partial or full, from Dashboard or via API</span></div>
</div>
`}</HTMLBlock>

***

## Workflow

The steps below give a detailed view of the lifecycle of a PayU Payment Link.

<Accordion title="Step 1: Create a PayU Merchant Account" icon="far fa-user">
  <Anchor target="_blank" href="https://docs.payu.in/docs/set-up-your-account">Sign up</Anchor> for a PayU merchant account and complete KYC verification. Once your account is approved, you can start creating payment links immediately from the Dashboard.

  <Callout icon="💡" theme="info">
    ### **Already Have an Account?**

    &#x20;You can skip to the Step 2
  </Callout>
</Accordion>

<Accordion title="Step 2: Create a Payment Link" icon="far fa-link">
  <Anchor target="_blank" href="https://docs.payu.in/docs/create-a-payment-link">Create a payment</Anchor> link by entering the amount, purpose of the payment and other details. You can optionally set an expiry date, enable partial payments, collect customer details at checkout, and add custom fields for your records.

  <Callout icon="💡" theme="info">
    ### **Automate:**

    You can automate creation from your own system using <Anchor target="_blank" href="https://docs.payu.in/reference/create-payment-links">Payment Links APIs</Anchor>.
  </Callout>
</Accordion>

<Accordion title="Step 3: Send the Link to Your Customer" icon="far fa-paper-plane">
  Share the payment link with your customer over SMS, Email, or WhatsApp. If you enter the customer's phone number or email when creating the link and toggle notifications on, PayU sends the link automatically the moment you click **Create Payment Link**.

  <Callout icon="💡" theme="info">
    ### **Note:**

    You can <Anchor target="_blank" href="https://docs.payu.in/docs/manage-payment-links#what-can-i-do-with-a-payment-link-after-it-is-created">resend or share</Anchor> the link again at any time from the Dashboard as long as the link is Active.
  </Callout>
</Accordion>

<Accordion title="Step 4: Customer Opens the Link and Pays" icon="far fa-credit-card">
  Your customer clicks the link and is taken to a PayU-hosted checkout page. They choose their preferred payment method such as cards, UPI, net banking, wallets, and more to complete the payment. If partial payment is enabled, they can choose how much to pay.

  The payment link is marked as **Expired** once the payment is fully made. If you have webhooks configured, PayU sends a `payment.success` event to your server.

  <Callout icon="💡" theme="info">
    ### **Webhooks:**

    Webhooks are optional — your Dashboard always reflects the current payment status without any webhook setup.
  </Callout>
</Accordion>

<Accordion title="Step 5: Track and Manage Your Links" icon="far fa-chart-line">
  Track all payment links and their statuses from the Payment Links Dashboard. You can filter by status or date, view transaction history per link, download reports in CSV or Excel format, and duplicate or deactivate links as needed.

  <Callout icon="💡" theme="info">
    ### **Note:**

    To retrieve link data programmatically — for reconciliation or reporting — use the Fetch API.

    - [Manage Payment Links — Dashboard](doc:manage-payment-links)
    - [Fetch Payment Links API](doc:api-fetch)
  </Callout>
</Accordion>

<Accordion title="Step 6: Funds Are Settled to Your Account" icon="far fa-building-columns">
  After a successful payment, PayU settles the funds to your registered bank account as per the settlement schedule — minus applicable fees and taxes. You can track settlement reports from the PayU Dashboard.

  <Callout icon="💡" theme="info">
    ### **Note:**

    If a customer requests a refund or raises a dispute with their bank, PayU has a process for each.

    - [Refunds](doc:introduction-refunds)
    - [Settlements](doc:split-settlments)
    - [Disputes and Chargebacks](doc:chargeback)
  </Callout>
</Accordion>
