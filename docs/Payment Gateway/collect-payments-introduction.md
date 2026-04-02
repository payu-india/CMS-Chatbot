---
title: Overview
deprecated: false
hidden: false
metadata:
  title: Collect Payments Introduction
  keywords:
    - Collect Payments Introduction
  robots: index
next:
  description: Refer to the following pages for additional information.
  pages:
    - slug: payu-payment-gateway-workflow
      title: PayU Payment Gateway Workflow
      type: basic
---
A **payment gateway** enables businesses to securely accept payments from customers through their website or mobile application. The **PayU Payment Gateway** acts as a secure bridge between your customer, your application, and the banking networks to process transactions safely and reliably.

<Accordion title="Benefits" icon="fa-lightbulb">
  * **Secure and Reliable Transactions**: The PayU Payment Gateway ensures that every transaction is securely processed using encryption and industry-standard safeguards, helping protect customers from fraud and unauthorized access.
  * **Faster and Smoother Payments**: PayU provides an optimized checkout experience that reduces friction and enables quick transaction processing, ensuring a smooth payment journey for customers.
  * **Reduced Payment Failures**: With real-time transaction handling and intelligent processing, PayU helps minimize failed payments and improves overall payment success rates.
  * **Multiple Payment Options**: PayU enables businesses to accept a wide range of payment methods including cards, UPI, net banking, and wallets, offering flexibility and convenience to customers.
  * **Improved Customer Experience**: A seamless and intuitive payment flow helps customers complete transactions quickly, enhancing trust and satisfaction.
  * **Flexible Integration Options**: PayU offers multiple integration methods such as Hosted Checkout, Web Checkout, and APIs, allowing businesses to choose what best fits their needs.
  * **Better Conversion Rates**: A smoother payment experience leads to fewer drop-offs during checkout, helping businesses improve conversion rates and revenue.
  * **Scalable and Business-Friendly**: PayU is built to handle growing transaction volumes, making it suitable for businesses of all sizes across web and mobile platforms.
  * **Developer-Friendly**: With simple integration options and support for multiple tech stacks, PayU enables developers to go live quickly and efficiently.
  * **Operational Efficiency**: PayU simplifies payment management with centralized tracking and reporting, reducing manual effort and improving operational workflows.
</Accordion>

## Types of Checkout

PayU offers the following checkout types:

<Tabs>
  <Tab title="PayU Hosted">
    * Quick and easy integration
    * No PCI compliance required
    * PayU handles UI, security, and payment flow<br />

    Know more about <a href="/docs/prebuilt-checkout-payu-hosted" target="_blank">PayU Hosted Checkout</a>.
  </Tab>

  <Tab title="Merchant Hosted (Custom)">
    * Full control over UI/UX
    * Better branding and customization
    * Seamless user experience<br />

    Know more about <a href="/docs/custom-checkout-merchant-hosted" target="_blank">Merchant Hosted Checkout</a>.
  </Tab>

  <Tab title="S2S">
    * Eliminates intermediate browser hops
    * Reduces latency and failure points
    * Higher control over payment flow
    * Better success rates due to fewer redirects<br />

    Know more about <a href="/docs/server-to-server-integration" target="_blank">Server-to-Server (S2S)</a>.
  </Tab>

  <Tab title="CommercePro">
    * Faster checkout with minimal form filling
    * Higher conversions through personalization
    * Reduced drop-offs using recommendation engine
    * Lower RTO with intelligent COD controls<br />

    Know more about <a href="/docs/checkout-express" target="_blank">CommercePro (checkout Express)</a>.
  </Tab>

  <Tab title="Checkout Plus">
    * Reduced drop-offs
    * Faster checkout experience
    * Improved conversion rates<br />

    Know more about <a href="/docs/checkout-plus-integration" target="_blank">Checkout Plus</a>.
  </Tab>
</Tabs>

<Callout icon="📘" theme="info">
  **No-code Solutions**

  PayU also provides <Anchor label="No-code options" target="_blank" href="https://docs.payu.in/docs/introduction-no-code-payments-integration">No-code options</Anchor> to collect payments based on your business needs without integration.
</Callout>

## Payment Gateway Solutions by Industry

<Accordion title="E-commerce (Retail and D2C)" icon="fa-cart-shopping">
  **Challenges**

  * High drop-offs during checkout
  * Diverse payment preferences (UPI, cards, wallets and BNPL)

  **Recommended Checkout Solutions**

  * <a href="docs/prebuilt-checkout-payu-hosted" target="_blank">PayU Hosted Checkout</a>
  * <a href="docs/custom-checkout-merchant-hosted" target="_blank">Merchant Hosted</a> or <a href="docs/server-to-server-integration" target="_blank">S2S</a> Checkout
  * <a href="docs/upi-intent-and-collect-autopay-tpv-integration" target="_blank">UPI Intent and Collect</a>
  * <a href="docs/emi-api-integration" target="_blank">EMI</a> or <a href="docs/payu-bnpl-integration-introduction" target="_blank">BNPL</a>

  **Benefits**

  * **Merchants:** Higher conversion rates, easy integration
  * **Users:** Faster, flexible, secure checkout
</Accordion>

<br />

<Accordion title="Travel and Ticketing" icon="fa-plane-departure">
  **Challenges**

  * Time-critical bookings
  * High cost of payment failures

  **Recommended Checkout Solutions**

  * <a href="docs/prebuilt-checkout-payu-hosted" target="_blank">PayU Hosted Checkout</a>
  * <a href="docs/upi-intent-and-collect-autopay-tpv-integration" target="_blank">UPI Intent</a>
  * <a href="docs/introduction-dynamic-currency-conversion" target="_blank">International Cards</a>

  **Benefits**

  * **Merchants:** Reduced booking drop-offs
  * **Users:** Faster confirmations, smoother refunds
</Accordion>

<br />

<Accordion title="Educational Technology (EdTech)" icon="fa-laptop-file">
  **Challenges**

  * High ticket-size transactions
  * Installments and recurring payments

  **Recommended Checkout Solutions**

  * <a href="docs/prebuilt-checkout-payu-hosted" target="_blank">PayU Hosted Checkout</a>
  * <a href="docs/introduction-recurring-payments-integration" target="_blank">Recurring Payments (Subscriptions)</a>
  * <a href="docs/emi-api-integration" target="_blank">EMI</a>
  * <a href="docs/payment-links-dashboard" target="_blank">Payment Links</a>

  **Benefits**

  * **Merchants:** Consistent revenue collection
  * **Users:** Flexible and manageable payments
</Accordion>

<br />

<Accordion title="Gaming and Digital Services" icon="fa-gamepad">
  **Challenges**

  * Frequent microtransactions
  * Real-time payment confirmation required

  **Recommended Checkout Solutions**

  * <a href="docs/custom-checkout-merchant-hosted" target="_blank">Merchant Hosted</a> or <a href="docs/server-to-server-integration" target="_blank">S2S</a> Checkout
  * <a href="docs/upi-intent-and-collect-autopay-tpv-integration" target="_blank">UPI Intent and Collect</a>
  * <a href="docs/emi-api-integration" target="_blank">EMI</a>
  * <a href="docs/collect-payments-using-a-saved-card" target="_blank">Tokenized Cards</a>
  * <a href="docs/explore-android-sdks" target="_blank">Mobile SDKs</a>

  **Benefits**

  * **Merchants:** Higher success rates and better engagement
  * **Users:** Fast and uninterrupted experience
</Accordion>

<br />

<Accordion title="Subscription Services (SaaS and OTT)" icon="fa-square-rss">
  **Challenges**

  * Recurring billing cycles
  * Payment failures leading to churn

  **Recommended Checkout Solutions**

  * <a href="docs/introduction-recurring-payments-integration" target="_blank">Recurring Payments (Subscriptions)</a>
  * <a href="docs/collect-payments-using-a-saved-card" target="_blank">Tokenized Cards</a>
  * <a href="docs/prebuilt-checkout-payu-hosted" target="_blank">PayU Hosted Checkout (for mandate setup)</a>

  **Benefits**

  * **Merchants:** Reduced churn and predictable revenue
  * **Users:** Hassle-free renewals and billing transparency
</Accordion>

<br />

<Accordion title="Financial Services (Lending and NBFCs)" icon="fa-money-bill">
  **Challenges**

  * EMI collections and repayments
  * Compliance and trust requirements

  **Recommended Checkout Solutions**

  * <a href="docs/payment-links-dashboard" target="_blank">Payment Links</a>
  * <a href="docs/introduction-recurring-payments-integration" target="_blank">Recurring Payments (eMandates)</a>
  * <a href="docs/upi-intent-and-collect-autopay-tpv-integration" target="_blank">UPI Collect</a>

  **Benefits**

  * **Merchants:** Improved recovery rates
  * **Users:** Convenient repayment options
</Accordion>

<br />

<Accordion title="Marketplaces and Aggregators" icon="fa-shop">
  **Challenges**

  * Multiple sellers in one transaction
  * Complex settlement flows

  **Recommended Checkout Solutions**

  * <a href="docs/prebuilt-checkout-payu-hosted" target="_blank">PayU Hosted Checkout</a> or <a href="docs/custom-checkout-merchant-hosted" target="_blank">Merchant Hosted</a> Checkout
  * <a href="docs/split-settlments" target="_blank">Split Payments</a>

  **Benefits**

  * **Merchants:** Operational efficiency and scalability
  * **Users:** Unified checkout experience
</Accordion>

<Callout icon="📘" theme="info">
  **Implementation Tips**

  Combine Hosted or Seamless Checkout + UPI + Cards + Recurring Payments based on your business model to optimize success rates and user experience.
</Callout>

## Payment Gateway for Web, Mobile and E-commerce

PayU offers the following various integrations:

<Tabs>
  <Tab title="Web">
    <HoverCardGrid
      columns={2}
      items={[
      {
        title: "Checkout Integrations",
        text: (
          <ul style={{ paddingLeft: "16px", margin: 0 }}>
            <li>
              <a
                href="/docs/prebuilt-checkout-payu-hosted"
                target="_blank"
                rel="noopener noreferrer"
              >
                <strong>PayU Hosted</strong>
              </a>
            </li>
            <li>
              <a
                href="/docs/custom-checkout-merchant-hosted"
                target="_blank"
                rel="noopener noreferrer"
              >
                <strong>Merchant Hosted</strong>
              </a>
            </li>
            <li>
              <a
                href="/docs/checkout-express"
                target="_blank"
                rel="noopener noreferrer"
              >
                <strong>CommercePro</strong>
              </a>
            </li>
            <li>
              <a
                href="/docs/checkout-plus-integration"
                target="_blank"
                rel="noopener noreferrer"
              >
                <strong>Checkout Plus</strong>
              </a>
            </li>
          </ul>
        ),
      },
      {
        title: "Server-side Integrations",
        text: (
          <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
                marginBottom: "6px",
              }}
            >
              <i className="fa-brands fa-golang fa-2x" />
              <a href="/docs/go-sdk" target="_blank" rel="noopener noreferrer">
                <strong>GO SDK</strong>
              </a>
            </li>

            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
                marginBottom: "6px",
              }}
            >
              <i className="fa-brands fa-java fa-2x" />
              <a href="/docs/java-sdk" target="_blank" rel="noopener noreferrer">
                <strong>JAVA SDK</strong>
              </a>
            </li>

            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
                marginBottom: "6px",
              }}
            >
              <i className="fa-brands fa-php fa-2x" />
              <a href="/docs/php-sdk" target="_blank" rel="noopener noreferrer">
                <strong>PHP SDK</strong>
              </a>
            </li>

            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa-brands fa-node-js fa-2x" />
              <a href="/docs/node-js-sdk" target="_blank" rel="noopener noreferrer">
                <strong>NodeJS SDK</strong>
              </a>
            </li>
          </ul>
        ),
      },
    ]}
    />
  </Tab>

  <Tab title="Plugins">
    <HoverCardGrid
      columns={2}
      items={[
      {
        title: "PayU Payment Gateway Ecommerce Plugins",
        text: (
          <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
                marginBottom: "6px",
              }}
            >
              <i className="fa-brands fa-shopify fa-2x" />
              <a href="/docs/shopify" target="_blank" rel="noopener noreferrer">
                <strong>Shopify</strong>
              </a>
            </li>

            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
                marginBottom: "6px",
              }}
            >
              <i className="fa-brands fa-wix fa-2x" />
              <a href="/docs/wix" target="_blank" rel="noopener noreferrer">
                <strong>Wix</strong>
              </a>
            </li>

            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
                marginBottom: "6px",
              }}
            >
              <i className="fa-solid fa-o fa-2x" />
              <a href="/docs/odoo" target="_blank" rel="noopener noreferrer">
                <strong>Odoo</strong>
              </a>
            </li>

            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa-brands fa-wordpress fa-2x" />
              <a href="/docs/woocommerce" target="_blank" rel="noopener noreferrer">
                <strong>WooCommerce</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa-brands fa-whatsapp fa-2x" />
              <a href="/docs/interakt-for-whatsapp-business" target="_blank" rel="noopener noreferrer">
                <strong>Interakt</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa-brands fa-magento fa-2x" />
              <a href="/docs/magento" target="_blank" rel="noopener noreferrer">
                <strong>Magento</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa-brands fa-opencart fa-2x" />
              <a href="/docs/opencart" target="_blank" rel="noopener noreferrer">
                <strong>OpenCart</strong>
              </a>
            </li>
	          <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa fa-shopping-cart fa-2x" />
              <a href="/docs/shopmatic" target="_blank" rel="noopener noreferrer">
                <strong>Shopmatic</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa fa-shopping-cart fa-lg fa-2x" />
              <a href="/docs/prestashop" target="_blank" rel="noopener noreferrer">
                <strong>PrestaShop</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa fa-store fa-lg fa-2x" />
              <a href="/docs/bigcommerce" target="_blank" rel="noopener noreferrer">
                <strong>BigCommerce</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa fa-briefcase fa-lg fa-2x" />
              <a href="/docs/zoho-integration" target="_blank" rel="noopener noreferrer">
                <strong>Zoho</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa fa-store fa-2x" />
              <a href="/docs/fynd-integration" target="_blank" rel="noopener noreferrer">
                <strong>Fynd Store</strong>
              </a>
            </li>
          </ul>
        ),
      },
    ]}
    />
  </Tab>

  <Tab title="Mobile SDKs">
    <HoverCardGrid
      columns={2}
      items={[
      {
        title: "Mobile SDK Integrations",
        text: (
          <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
                marginBottom: "6px",
              }}
            >
              <i className="fa-brands fa-android fa-2x" />
              <a href="/docs/explore-android-sdks" target="_blank" rel="noopener noreferrer">
                <strong>Android SDK</strong>
              </a>
            </li>

            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
                marginBottom: "6px",
              }}
            >
              <i className="fa-apple fa-2x" />
              <a href="/docs/explore-ios-sdks" target="_blank" rel="noopener noreferrer">
                <strong>iOS Mobile SDK</strong>
              </a>
            </li>

            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
                marginBottom: "6px",
              }}
            >
              <i className="fa-brands fa-react fa-2x" />
              <a href="/docs/explore-reactnative-sdks" target="_blank" rel="noopener noreferrer">
                <strong>React Native Mobile SDK</strong>
              </a>
            </li>

            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa fa-mobile fa-2x" />
              <a href="/docs/flutter-sdk-introduction" target="_blank" rel="noopener noreferrer">
                <strong>Flutter Mobile SDK</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa-brands fa-whatsapp fa-2x" />
              <a href="/docs/interakt-for-whatsapp-business" target="_blank" rel="noopener noreferrer">
                <strong>Interakt</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa-brands fa-magento fa-2x" />
              <a href="/docs/magento" target="_blank" rel="noopener noreferrer">
                <strong>Magento</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa-brands fa-opencart fa-2x" />
              <a href="/docs/opencart" target="_blank" rel="noopener noreferrer">
                <strong>OpenCart</strong>
              </a>
            </li>
	          <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa fa-shopping-cart fa-2x" />
              <a href="/docs/shopmatic" target="_blank" rel="noopener noreferrer">
                <strong>Shopmatic</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa fa-shopping-cart fa-lg fa-2x" />
              <a href="/docs/prestashop" target="_blank" rel="noopener noreferrer">
                <strong>PrestaShop</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa fa-store fa-lg fa-2x" />
              <a href="/docs/bigcommerce" target="_blank" rel="noopener noreferrer">
                <strong>BigCommerce</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa fa-briefcase fa-lg fa-2x" />
              <a href="/docs/zoho-integration" target="_blank" rel="noopener noreferrer">
                <strong>Zoho</strong>
              </a>
            </li>
            <li
              style={{
                display: "flex",
                alignItems: "center",
                gap: "8px",
              }}
            >
              <i className="fa fa-store fa-2x" />
              <a href="/docs/fynd-integration" target="_blank" rel="noopener noreferrer">
                <strong>Fynd Store</strong>
              </a>
            </li>
          </ul>
        ),
      },
    ]}
    />
  </Tab>
</Tabs>

<br />
