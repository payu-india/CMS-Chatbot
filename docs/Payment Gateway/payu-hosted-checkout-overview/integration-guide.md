---
title: Integration Guide
deprecated: false
hidden: false
metadata:
  robots: index
---
Follow these steps to integrate the PayU Hosted Checkout on your website.

<Callout icon="👍" theme="okay">
  **Payment Flow**

  Before you start integrating, it’s important to understand how PayU Hosted Checkout payment flow and customer journey works.
</Callout>

<Tabs>
  <Tab title="Web">
    <HoverCardGrid
      columns={2}
      items={[
        {
          title: "Checkout Integrations",
          text: (
            <ul style={{ paddingLeft: "16px", margin: 0 }}>
              {[
                { name: "PayU Hosted", link: "/docs/prebuilt-checkout-payu-hosted" },
                { name: "Merchant Hosted", link: "/docs/custom-checkout-merchant-hosted" },
                { name: "CommercePro", link: "/docs/checkout-express" },
                { name: "Checkout Plus", link: "/docs/checkout-plus-integration" },
              ].map((item) => (
                <li key={item.name}>
                  <a href={item.link} target="_blank" rel="noopener noreferrer">
                    <strong>{item.name}</strong>
                  </a>
                </li>
              ))}
            </ul>
          ),
        },
        {
          title: "Server-side Integrations",
          text: (
            <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
              {[
                { name: "GO SDK", link: "/docs/go-sdk", icon: "fa-brands fa-golang" },
                { name: "JAVA SDK", link: "/docs/java-sdk", icon: "fa-brands fa-java" },
                { name: "PHP SDK", link: "/docs/php-sdk", icon: "fa-brands fa-php" },
                { name: "NodeJS SDK", link: "/docs/node-js-sdk", icon: "fa-brands fa-node-js" },
              ].map((item) => (
                <li
                  key={item.name}
                  style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "6px" }}
                >
                  <span style={{ width: "20px", display: "inline-flex", justifyContent: "center" }}>
                    <i className={`${item.icon} fa-lg`} />
                  </span>
                  <a
                    href={item.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{ whiteSpace: "nowrap" }}
                  >
                    <strong>{item.name}</strong>
                  </a>
                </li>
              ))}
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
              {[
                { name: "Shopify", link: "/docs/shopify", icon: "fa-brands fa-shopify" },
                { name: "Wix", link: "/docs/wix", icon: "fa-brands fa-wix" },
                { name: "Odoo", link: "/docs/odoo", icon: "fa-solid fa-o" },
                { name: "WooCommerce", link: "/docs/woocommerce", icon: "fa-brands fa-wordpress" },
                { name: "Interakt", link: "/docs/interakt-for-whatsapp-business", icon: "fa-brands fa-whatsapp" },
                { name: "Magento", link: "/docs/magento", icon: "fa-brands fa-magento" },
                { name: "OpenCart", link: "/docs/opencart", icon: "fa-brands fa-opencart" },
                { name: "Shopmatic", link: "/docs/shopmatic", icon: "fa fa-shopping-cart" },
                { name: "PrestaShop", link: "/docs/prestashop", icon: "fa fa-shopping-cart" },
                { name: "BigCommerce", link: "/docs/bigcommerce", icon: "fa fa-store" },
                { name: "Zoho", link: "/docs/zoho-integration", icon: "fa fa-briefcase" },
                { name: "Fynd Store", link: "/docs/fynd-integration", icon: "fa fa-store" },
              ].map((item) => (
                <li
                  key={item.name}
                  style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "6px" }}
                >
                  <span style={{ width: "20px", display: "inline-flex", justifyContent: "center" }}>
                    <i className={`${item.icon} fa-lg`} />
                  </span>
                  <a
                    href={item.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{ whiteSpace: "nowrap" }}
                  >
                    <strong>{item.name}</strong>
                  </a>
                </li>
              ))}
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
              {[
                { name: "Android SDK", link: "/docs/explore-android-sdks", icon: "fa-brands fa-android" },
                { name: "iOS Mobile SDK", link: "/docs/explore-ios-sdks", icon: "fa fa-tablet" },
                { name: "React Native Mobile SDK", link: "/docs/explore-reactnative-sdks", icon: "fa-brands fa-react" },
                { name: "Flutter Mobile SDK", link: "/docs/flutter-sdk-introduction", icon: "fa fa-mobile" },
                { name: "Cordova CheckoutPro SDK", link: "/docs/cordova-sdk-introduction", icon: "fa fa-plug" },
                { name: "Capacitor UPI Bolt Mobile SDK", link: "/docs/upi-bolt-sdk-ionic", icon: "fa fa-bolt" },
              ].map((item) => (
                <li
                  key={item.name}
                  style={{ display: "flex", alignItems: "center", gap: "8px", marginBottom: "6px" }}
                >
                  <span style={{ width: "20px", display: "inline-flex", justifyContent: "center" }}>
                    <i className={`${item.icon} fa-lg`} />
                  </span>
                  <a
                    href={item.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    style={{ whiteSpace: "nowrap" }}
                  >
                    <strong>{item.name}</strong>
                  </a>
                </li>
              ))}
            </ul>
          ),
        },
      ]}
    />
  </Tab>
</Tabs>

<br />
