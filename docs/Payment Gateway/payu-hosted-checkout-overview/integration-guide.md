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

    <HoverCardGrid
      columns={2}
      items={[
        {
          title: "1. Build Integration",
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

<br />
