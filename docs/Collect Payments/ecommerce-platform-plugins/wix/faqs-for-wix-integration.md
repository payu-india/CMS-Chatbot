---
title: FAQs for Wix Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
---
title: FAQs for Wix
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - Wix FAQs
    - PayU Wix FAQs
    - Wix integration FAQs
  robots: index
next:
  description: ''
---
This page answers frequently asked questions about integrating PayU with Wix, including supported payment methods, setup, testing, and troubleshooting.

<Callout icon="📘" theme="info">
  **Reference**: For integration steps, refer to [Wix](doc:wix) and [Integrate with Wix](doc:integrate-with-wix).
</Callout>

## General

<Accordion title="1. What does the PayU India plugin do on Wix?" icon="fa-info-circle">
  The PayU India plugin lets merchants accept payments on their Wix store. At checkout, customers are redirected to PayU to complete payment securely, then returned to the Wix store after the order is confirmed. For an overview, refer to [Wix](doc:wix).
</Accordion>

<Accordion title="2. Which payment methods does PayU support on Wix?" icon="fa-info-circle">
  PayU on Wix supports cards (VISA, MasterCard, Diners, American Express), Net Banking, UPI, EMI, and wallets. Availability may depend on your merchant account configuration. Contact your PayU Key Account Manager (KAM) if a required mode is not enabled.
</Accordion>

<Accordion title="3. Do I need a PayU merchant account before integrating with Wix?" icon="fa-info-circle">
  Yes. Register for a merchant account on PayU before starting integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Accordion>

<Accordion title="4. How does the payment flow work on Wix with PayU?" icon="fa-info-circle">
  When a customer checks out on your Wix store, they are redirected to PayU to complete payment. After a successful payment, the order is confirmed and the customer is redirected back to your Wix store.
</Accordion>

<Accordion title="5. Who do I contact for Wix integration enablement or support?" icon="fa-info-circle">
  Contact your PayU Key Account Manager (KAM) for account enablement and payment-mode configuration. For technical issues during integration, use [PayU Support](https://help.payu.in) or refer to [Troubleshooting Wix Integration](doc:troubleshooting-wix-integration).
</Accordion>

## Integrate with Wix

<Accordion title="1. What are the prerequisites to integrate PayU on Wix?" icon="fa-info-circle">
  You need Wix account credentials, a store or site set up on Wix where PayU will be configured, and removal of any previously installed PayU India plugin. Refer to [Integrate with Wix](doc:integrate-with-wix).
</Accordion>

<Accordion title="2. How do I connect PayU India on my Wix store?" icon="fa-info-circle">
  In Wix admin, go to **Settings > Accept Payments**, click **See More Payment Options**, select **Connect** on the **PayU India** tile, enter your merchant key and salt, and click **Connect**. Refer to [Integrate with Wix](doc:integrate-with-wix).
</Accordion>

<Accordion title="3. What credentials do I need to connect PayU to Wix?" icon="fa-info-circle">
  You need your PayU merchant key and salt. For production, refer to [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard). For test or sandbox, refer to [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
</Accordion>

<Accordion title="4. Should I remove an existing PayU plugin before reconnecting?" icon="fa-info-circle">
  Yes. If a PayU India plugin is already installed, remove it before connecting again to avoid configuration conflicts. Refer to the prerequisites in [Integrate with Wix](doc:integrate-with-wix).
</Accordion>

<Accordion title="5. How do I verify transactions after integrating PayU on Wix?" icon="fa-info-circle">
  PayU recommends verifying transaction details using the [Verify Payment API](ref:verify_payment_api) after you receive the payment response to reconcile with PayU's database.
</Accordion>

<Accordion title="6. Where do I get test credentials for Wix integration?" icon="fa-info-circle">
  Use test merchant key and salt from PayU Dashboard. For more information, refer to [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
</Accordion>

## Troubleshooting

<Accordion title="1. PayU is not appearing or not working on my Wix store" icon="fa-info-circle">
  Check that your merchant API key and salt are configured correctly. Log in to [Merchant Dashboard](http://onboarding.payu.in/) and verify the values match what you entered in Wix. For more information, refer to [Troubleshooting Wix Integration](doc:troubleshooting-wix-integration) and [Integrate with Wix](doc:integrate-with-wix).
</Accordion>

<Accordion title="2. What should I do if I see a connection error after entering key and salt?" icon="fa-info-circle">
  Confirm you are using key and salt from the same environment (test or production). Copy the salt directly from PayU Dashboard because it is case-sensitive. Remove any previously installed PayU plugin and reconnect. If the issue persists, contact [PayU Support](https://help.payu.in).
</Accordion>

<Accordion title="3. PayU Plugin is not working" icon="fa-info-circle">
Check whether the merchant API key and Salt are configured accurately and navigate to <Anchor label="Merchant Dashboard" target="_blank" href="http://onboarding.payu.in/">Merchant Dashboard</Anchor> and verify these values. For more information, refer to [Integrate with Wix](doc:integrate-with-wix). For more information on generating API key and salt, refer to [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt).
</Accordion>