---
title: How Payment Button Works
excerpt: >-
  Understand the complete end-to-end lifecycle of a PayU Payment Button — from  
  creating your account to receiving funds in your bank account.
deprecated: false
hidden: true
metadata:
  title: How Payment Buttons Works | PayU Developer Docs
  description: >-
    End-to-end lifecycle of a PayU Payment Button 

    account setup, button creation, adding to your website, customer payment,
    status tracking, and fund settlement.
  keywords:
    - how payu payment buttons works
    - payu payment button lifecycle
    - payment button flow payu
    - payu payment button workflow
    - payment button end to end payu
    - how does payment button work india
    - payu payment button steps
    - payment button process payu
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payment-button
      title: Payment Button
      type: basic
    - slug: add-payment-button
      title: Add a Payment Button
      type: basic
    - slug: manage-payment-buttons
      title: Manage Payment Buttons
      type: basic
    - slug: payment-button-errors-troubleshooting
      title: Errors and Troubleshooting
      type: basic
    - slug: payment-button-faqs
      title: FAQs (Frequently Asked Questions)
      type: basic
---
Understand the complete end-to-end flow of how PayU Payment Buttons works — from creating your account to receiving funds in your bank account.

<HTMLBlock>{`
<style>
# pb-diagram * { box-sizing: border-box; margin: 0; padding: 0; }
# pb-diagram {
  font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
  background: linear-gradient(135deg, #E8F5EE 0%, #F5FAF7 60%, #EAF6F0 100%);
  border-radius: 14px;
  padding: 44px 24px 32px;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow-x: auto;
}
# pb-diagram .payu-badge {
  background: #00A550; color: white; font-size: 13px; font-weight: 700;
  letter-spacing: 0.5px; padding: 4px 14px; border-radius: 20px;
  margin-bottom: 20px; display: inline-block;
}
# pb-diagram .flow {
  display: flex; align-items: center; gap: 0; position: relative;
}
# pb-diagram .step {
  display: flex; flex-direction: column; align-items: center;
  position: relative; opacity: 0; transform: translateY(16px);
  animation: pbSlideIn 0.5s ease forwards;
}
# pb-diagram .step:nth-child(1)  { animation-delay: 0.1s; }
# pb-diagram .step:nth-child(3)  { animation-delay: 0.3s; }
# pb-diagram .step:nth-child(5)  { animation-delay: 0.5s; }
# pb-diagram .step:nth-child(7)  { animation-delay: 0.7s; }
# pb-diagram .step:nth-child(9)  { animation-delay: 0.9s; }
# pb-diagram .step:nth-child(11) { animation-delay: 1.1s; }
@keyframes pbSlideIn { to { opacity: 1; transform: translateY(0); } }
# pb-diagram .card {
  width: 148px; padding: 34px 14px 18px;
  background: white; border-radius: 18px;
  box-shadow: 0 4px 20px rgba(0,68,32,0.09), 0 1px 4px rgba(0,68,32,0.05);
  display: flex; flex-direction: column; align-items: center;
  text-align: center; position: relative; border-top: 4px solid #00A550;
}
# pb-diagram .badge {
  position: absolute; top: -20px; left: 50%; transform: translateX(-50%);
  width: 40px; height: 40px; background: #00A550; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-size: 15px; font-weight: 700; color: white;
  box-shadow: 0 4px 12px rgba(0,165,80,0.35);
  animation: pbPulse 2.5s ease-in-out infinite;
}
# pb-diagram .step:nth-child(1)  .badge { animation-delay: 0s; }
# pb-diagram .step:nth-child(3)  .badge { animation-delay: 0.4s; }
# pb-diagram .step:nth-child(5)  .badge { animation-delay: 0.8s; }
# pb-diagram .step:nth-child(7)  .badge { animation-delay: 1.2s; }
# pb-diagram .step:nth-child(9)  .badge { animation-delay: 1.6s; }
# pb-diagram .step:nth-child(11) .badge { animation-delay: 2.0s; }
@keyframes pbPulse {
  0%,100% { box-shadow: 0 4px 12px rgba(0,165,80,0.35); }
  50%      { box-shadow: 0 4px 20px rgba(0,165,80,0.7), 0 0 0 8px rgba(0,165,80,0.1); }
}
# pb-diagram .icon-wrap {
  width: 52px; height: 52px; background: #E8F5EE; border-radius: 14px;
  display: flex; align-items: center; justify-content: center; margin-bottom: 12px;
}
# pb-diagram .icon-wrap svg { width: 26px; height: 26px; }
# pb-diagram .card-title { font-size: 12.5px; font-weight: 700; color: #1B2D3E; margin-bottom: 4px; line-height: 1.3; }
# pb-diagram .card-desc  { font-size: 11px; color: #6B7A8D; line-height: 1.5; }
# pb-diagram .arrow-wrap {
  position: relative; width: 68px; height: 2px;
  flex-shrink: 0; margin: 0 2px; align-self: center;
}
# pb-diagram .arrow-line {
  position: absolute; top: 0; left: 0; right: 12px; height: 2px;
  background: repeating-linear-gradient(to right,#00A550 0,#00A550 6px,transparent 6px,transparent 10px);
  opacity: 0.4;
}
# pb-diagram .arrow-head {
  position: absolute; right: 0; top: -5px;
  width: 0; height: 0;
  border-left: 10px solid #00A550;
  border-top: 6px solid transparent;
  border-bottom: 6px solid transparent;
  opacity: 0.8;
}
# pb-diagram .dot {
  position: absolute; top: -5px; width: 12px; height: 12px;
  background: #00A550; border-radius: 50%;
  box-shadow: 0 0 8px rgba(0,165,80,0.6);
  animation: pbMoveDot 1.8s ease-in-out infinite;
}
# pb-diagram .dot2 { animation-delay: 0.9s; opacity: 0.6; width: 8px; height: 8px; top: -3px; }
# pb-diagram .arrow-wrap:nth-of-type(2)  .dot  { animation-delay: 0.2s; }
# pb-diagram .arrow-wrap:nth-of-type(2)  .dot2 { animation-delay: 1.1s; }
# pb-diagram .arrow-wrap:nth-of-type(4)  .dot  { animation-delay: 0.4s; }
# pb-diagram .arrow-wrap:nth-of-type(4)  .dot2 { animation-delay: 1.3s; }
# pb-diagram .arrow-wrap:nth-of-type(6)  .dot  { animation-delay: 0.6s; }
# pb-diagram .arrow-wrap:nth-of-type(6)  .dot2 { animation-delay: 1.5s; }
# pb-diagram .arrow-wrap:nth-of-type(8)  .dot  { animation-delay: 0.8s; }
# pb-diagram .arrow-wrap:nth-of-type(8)  .dot2 { animation-delay: 1.7s; }
# pb-diagram .arrow-wrap:nth-of-type(10) .dot  { animation-delay: 1.0s; }
# pb-diagram .arrow-wrap:nth-of-type(10) .dot2 { animation-delay: 1.9s; }
@keyframes pbMoveDot {
  0%   { left: 0%;              opacity: 0; }
  8%   { opacity: 1; }
  88%  { opacity: 1; }
  100% { left: calc(100% - 12px); opacity: 0; }
}
# pb-diagram .refund-note {
  margin-top: 28px; font-size: 11.5px; color: #00A550; font-weight: 600;
  text-align: center; background: #E8F5EE; border: 1.5px dashed #00A550;
  border-radius: 8px; padding: 8px 20px; display: inline-block;
}
# pb-diagram .refund-note span { font-weight: 400; color: #6B7A8D; margin-left: 6px; }
</style>

<div id="pb-diagram">
  <span class="payu-badge">PayU</span>
  <div class="flow">

    <!-- Step 1: Create Account -->
    <div class="step">
      <div class="card">
        <div class="badge">1</div>
        <div class="icon-wrap"><svg viewBox="0 0 26 26" fill="none"><circle cx="13" cy="9" r="5" stroke="#00A550" stroke-width="2.2"></circle><path d="M4 22c0-4.418 4.03-8 9-8s9 3.582 9 8" stroke="#00A550" stroke-width="2.2" stroke-linecap="round"></path></svg></div>
        <div class="card-title">Create Account</div>
        <div class="card-desc">Sign up and complete KYC</div>
      </div>
    </div>
    <div class="arrow-wrap"><div class="arrow-line"></div><div class="arrow-head"></div><div class="dot"></div><div class="dot dot2"></div></div>

    <!-- Step 2: Create Button -->
    <div class="step">
      <div class="card">
        <div class="badge">2</div>
        <div class="icon-wrap"><svg viewBox="0 0 26 26" fill="none"><rect x="4" y="9" width="18" height="10" rx="3" stroke="#00A550" stroke-width="2.2"></rect><line x1="8" y1="14" x2="18" y2="14" stroke="#00A550" stroke-width="1.8" stroke-linecap="round"></line><line x1="13" y1="4" x2="13" y2="9" stroke="#00A550" stroke-width="1.8" stroke-linecap="round" stroke-dasharray="2,2"></line></svg></div>
        <div class="card-title">Create Button</div>
        <div class="card-desc">Set label, amount, colour</div>
      </div>
    </div>
    <div class="arrow-wrap"><div class="arrow-line"></div><div class="arrow-head"></div><div class="dot"></div><div class="dot dot2"></div></div>

    <!-- Step 3: Add to Website -->
    <div class="step">
      <div class="card">
        <div class="badge">3</div>
        <div class="icon-wrap"><svg viewBox="0 0 26 26" fill="none"><polyline points="9,8 3,14 9,20" stroke="#00A550" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"></polyline><polyline points="17,8 23,14 17,20" stroke="#00A550" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" fill="none"></polyline></svg></div>
        <div class="card-title">Add to Website</div>
        <div class="card-desc">Paste code on your page</div>
      </div>
    </div>
    <div class="arrow-wrap"><div class="arrow-line"></div><div class="arrow-head"></div><div class="dot"></div><div class="dot dot2"></div></div>

    <!-- Step 4: Customer Clicks and Pays -->
    <div class="step">
      <div class="card">
        <div class="badge">4</div>
        <div class="icon-wrap"><svg viewBox="0 0 26 26" fill="none"><rect x="3" y="7" width="20" height="14" rx="3" stroke="#00A550" stroke-width="2.2"></rect><line x1="3" y1="11" x2="23" y2="11" stroke="#00A550" stroke-width="3"></line><rect x="6" y="14" width="7" height="4" rx="1.5" fill="#00A550"></rect></svg></div>
        <div class="card-title">Customer Pays</div>
        <div class="card-desc">Secure PayU payment page</div>
      </div>
    </div>
    <div class="arrow-wrap"><div class="arrow-line"></div><div class="arrow-head"></div><div class="dot"></div><div class="dot dot2"></div></div>

    <!-- Step 5: Track Payments -->
    <div class="step">
      <div class="card">
        <div class="badge">5</div>
        <div class="icon-wrap"><svg viewBox="0 0 26 26" fill="none"><circle cx="11" cy="11" r="7" stroke="#00A550" stroke-width="2.2"></circle><line x1="16" y1="16" x2="23" y2="23" stroke="#00A550" stroke-width="2.8" stroke-linecap="round"></line></svg></div>
        <div class="card-title">Track Payments</div>
        <div class="card-desc">Dashboard or webhook</div>
      </div>
    </div>
    <div class="arrow-wrap"><div class="arrow-line"></div><div class="arrow-head"></div><div class="dot"></div><div class="dot dot2"></div></div>

    <!-- Step 6: Funds Settled -->
    <div class="step">
      <div class="card">
        <div class="badge">6</div>
        <div class="icon-wrap"><svg viewBox="0 0 26 26" fill="none"><rect x="2" y="8" width="22" height="14" rx="3.5" stroke="#00A550" stroke-width="2.2"></rect><rect x="14" y="12" width="9" height="9" rx="2.5" stroke="#00A550" stroke-width="2"></rect><circle cx="18.5" cy="16.5" r="2" fill="#00A550"></circle><line x1="2" y1="13" x2="14" y2="13" stroke="#00A550" stroke-width="1.5" stroke-dasharray="2,2" opacity="0.45"></line></svg></div>
        <div class="card-title">Funds Settled</div>
        <div class="card-desc">To your bank, minus fees</div>
      </div>
    </div>

  </div>
  <div class="refund-note">↩ Optional: Initiate a Refund <span>— partial or full, from the Dashboard</span></div>
</div>
`}</HTMLBlock>

***

## Workflow

The steps below give a detailed view of the lifecycle of a PayU Payment Button.

<Accordion title="Step 1: Create a PayU Merchant Account" icon="far fa-user">
  Sign up for a PayU merchant account and complete KYC verification. Once your account is approved, you can start creating payment buttons immediately from the Dashboard — no technical setup needed.

  <Callout icon="💡" theme="info">
    **Handy Tip**

    Already have an account? Skip to Step 2.

    - [Set Up Your Account](doc:set-up-your-account)
  </Callout>
</Accordion>

<Accordion title="Step 2: Create a Payment Button" icon="far fa-rectangle-terminal">
  In the PayU Dashboard, go to **Payment Tools → Payment Buttons** and click **Create New Button**. Set the button text (Buy Now, Pay Now, Book Now, or Donate Now), item name, amount, colour, and size. Optionally add checkout fields to collect customer details — name, email, phone — or any custom fields specific to your business.

  <Callout icon="💡" theme="info">
    **Handy Tip**

    Payment Buttons cannot be edited after creation — double-check all settings before clicking **Generate Button**.

    - [Add a Payment Button — Dashboard walkthrough](doc:add-a-payment-button)
    - [Payment Button Options](doc:customize-payment-button)
  </Callout>
</Accordion>

<Accordion title="Step 3: Add the Button to Your Website" icon="far fa-code">
  Click **Generate Button**. PayU creates your button and gives you a short piece of code. Copy the code and paste it into an HTML or Code block on your website — WordPress, Wix, Squarespace, and most website builders support this. The button appears on your page right away. No developer needed.

  <Callout icon="💡" theme="info">
    **Handy Tip**

    Paste the code in an HTML or Code block — not a text or rich-text editor. Using a text editor will show the raw code as plain text instead of a button.

    - [Add a Payment Button — Embed Steps](doc:add-a-payment-button)
  </Callout>
</Accordion>

<Accordion title="Step 4: Customer Visits Your Page and Pays" icon="far fa-credit-card">
  When a customer visits your page and clicks the button, PayU's payment page opens automatically. They choose their preferred payment method — cards, UPI, net banking, wallets, EMI, and more — and complete the payment. Once done, they are sent to your success page, or your failure page if the payment did not go through.

  If you have webhooks configured, PayU sends a `payment.success` event to your server the moment the payment completes.

  <Callout icon="💡" theme="info">
    **Handy Tip**

    Webhooks are optional — your Dashboard always reflects the current payment status without any webhook setup.

    - [Set Redirect Pages](doc:customize-payment-button)
    - [Webhooks for Payments](doc:webhooks)
  </Callout>
</Accordion>

<Accordion title="Step 5: Track and Manage Your Payments" icon="far fa-chart-line">
  Every payment made through your button appears in the **Transactions** tab of your PayU Dashboard right away. You can filter by date, search by amount, view individual transaction details, and download payment records as CSV or Excel. All your buttons and their statuses are listed under **Payment Tools → Payment Buttons**.

  <Callout icon="💡" theme="info">
    **Handy Tip**

    Use the **Download** option on the Payment Buttons list to export all button records for reconciliation or your own reporting.

    - [Manage Payment Buttons — Dashboard](doc:manage-payment-buttons)
  </Callout>
</Accordion>

<Accordion title="Step 6: Funds Are Settled to Your Account" icon="far fa-building-columns">
  After a successful payment, PayU settles the funds to your registered bank account as per the settlement schedule — minus applicable fees and taxes. You can track settlement reports from the PayU Dashboard.

  <Callout icon="💡" theme="info">
    **Handy Tip**

    If a customer requests a refund or raises a dispute with their bank, PayU has a process for each.

    - [Refunds](doc:introduction-refunds)
    - [Settlements](doc:split-settlments)
    - [Disputes and Chargebacks](doc:chargeback)
  </Callout>
</Accordion>

***

## Related Information

- [Payment Button Overview](doc:payment-button-overview)
- [Add a Payment Button](doc:add-a-payment-button)
- [Customize Your Button](doc:customize-payment-button)
- [Manage Payment Buttons](doc:manage-payment-buttons)
- [Payment Button Troubleshooting](doc:payment-button-troubleshooting)
- [Payment Button FAQs](doc:payment-button-faqs)
