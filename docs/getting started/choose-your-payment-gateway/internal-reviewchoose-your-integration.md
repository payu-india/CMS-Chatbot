---
title: '[Internal Review]Choose Your Integration'
deprecated: false
hidden: true
metadata:
  robots: index
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
    <div class="piw-header-icon" aria-hidden="true"><svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L4 6v6c0 5 3.4 9.4 8 10 4.6-.6 8-5 8-10V6l-8-4zm0 2.2l6 3v5.8c0 4.1-2.7 7.8-6 8.3-3.3-.5-6-4.2-6-8.3V7.2l6-3zM11 11h2v5h-2v-5zm0-3h2v2h-2V8z"></path></svg></div>
    <div>
      <p class="piw-title">Integration path finder</p>
      <p class="piw-subtitle">Branch by channel, team skills, and checkout goals.</p>
    </div>
  </div>
  <div class="piw-progress" aria-hidden="true"><div class="piw-progress-fill" id="piw-progress-fill"></div></div>
  <div class="piw-body" id="piw-body"></div>
</div>
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

| Payment Solution              | Ease of Integration | Use Case                                     | Key Features              |                               |                                      |               |
| :---------------------------- | :------------------ | :------------------------------------------- | :------------------------ | ----------------------------- | ------------------------------------ | ------------- |
| **No-Code Payment Solutions** |                     |                                              |                           |                               |                                      |               |
| Payment Links                 | Very Easy           | Simple, efficient payment collection         | Quick setup \*\*          | **Customizable**              | **Real-time notifications**          | \*\* Tracking |
| Payment Invoices              | Very Easy           | Professional client billing with invoices    | Invoice generation \*\*   | **Payment tracking**          | \*\* Payment reminders Customization |               |
| Payment Buttons               | Easy                | Seamless integration into websites/platforms | Easy integration \*\*     | **Customizable**              | **Multiple payment methods**         | \*\* Security |
| **Web Integration**           |                     |                                              |                           |                               |                                      |               |
| Hosted Checkout               | Easy                | Secure, hassle-free online payments          | Robust security \*\*      | **PCI compliance**            | \*\* Multiple payment options        |               |
| Custom Checkout               | Moderate            | Total control over the payment process       | Full customization \*\*   | **Optimal user experience**   | \*\* Developer-friendly APIs         |               |
| Checkout Express              | Easy                | Seamless payment integration within websites | Seamless integration \*\* | **Enhanced security**         | \*\* Easy implementation             |               |
| **Mobile Checkouts**          |                     |                                              |                           |                               |                                      |               |
| Mobile SDKs                   | Moderate            | Convenient mobile payment experience         | Responsive design \*\*    | **Mobile wallet integration** | \*\* One-click payments              |               |

<br />
