---
title: FAQs for Odoo Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: FAQs for Odoo Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - Odoo FAQs
    - PayU Odoo FAQs
    - Odoo integration FAQs
  robots: index
next:
  description: ''
---
This section includes answers for the frequently asked questions about integrating PayU with Odoo, including supported payment methods, setup, and configuration.

<Callout icon="📘" theme="info">
  **Reference**: For integration steps, refer to [Odoo](doc:odoo) and [Install and Configure Odoo Plugin](doc:install-and-configure-odoo-plugin).
</Callout>

<Accordion title="1. What does the PayU India plugin do on Odoo?" icon="fa-info-circle">
  The PayU India plugin for Odoo allows store owners to accept online payments securely through their Odoo-powered site. When a customer reaches checkout, Odoo redirects them to PayU's secure payment page. Once payment is complete, the order is confirmed and the customer is brought back to your Odoo store.
</Accordion>

<Accordion title="2. Which payment features does PayU support on Odoo?" icon="fa-info-circle">
  PayU on Odoo supports 150+ payment modes, international cards, BIN-based offers and cashback, and EMI and BNPL. Only offers that do not modify the final invoice amount (such as cashback) are supported.
</Accordion>

<Accordion title="3. What are the prerequisites to integrate PayU on Odoo?" icon="fa-info-circle">
  You need Odoo installed and running, administrative access to the server, access to Odoo configuration files, and a PayU merchant account. Developer mode must be enabled in Odoo. This plugin has been developed and tested on Odoo 18; version 18 or above is recommended. For more information, refer to [Install and Configure Odoo Plugin](doc:install-and-configure-odoo-plugin).
</Accordion>

<Accordion title="4. Do I need a PayU merchant account before integrating with Odoo?" icon="fa-info-circle">
  Yes. Register for a PayU merchant account before starting the integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Accordion>
