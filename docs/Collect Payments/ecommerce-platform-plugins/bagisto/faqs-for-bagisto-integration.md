---
title: FAQs for Bagisto Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: FAQs for Bagisto
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - Bagisto FAQs
    - PayU Bagisto FAQs
    - Bagisto integration FAQs
  robots: index
next:
  description: ''
---
This section includes answers for frequently asked questions about configuring PayU with Bagisto, including credentials, setup, and testing.

<Callout icon="📘" theme="info">
  **Reference**: For configuration steps, refer to [Bagisto](doc:bagisto).
</Callout>


<Accordion title="1. Which payment methods does PayU support on Bagisto?" icon="fa-info-circle">
  PayU on Bagisto supports credit cards, debit cards, net banking, UPI, and wallets.
</Accordion>

<Accordion title="2. How does PayU authentication work with Bagisto?" icon="fa-info-circle">
  The PayU integration for Bagisto uses key-based authentication. Merchants need a **Merchant Key** to identify their PayU account and a **Merchant Salt** to generate the secure hash for transaction verification. All sensitive payment data is processed on PayU's servers, which helps maintain PCI-DSS compliance.
</Accordion>

<Accordion title="3. What are the prerequisites to configure PayU on Bagisto?" icon="fa-info-circle">
  Before you begin, ensure you have an active PayU merchant account, your PayU Merchant Key, and your PayU Merchant Salt.
</Accordion>

<Accordion title="4. How do I get my Merchant Key and Salt for Bagisto?" icon="fa-info-circle">
  Log in to [PayU Merchant Dashboard](https://onboarding.payu.in/app/account), select **Developer** from the left menu, and view your credentials under the API Keys tab. For more information, refer to [Bagisto](doc:bagisto).
</Accordion>

<Accordion title="6. How do I configure PayU in Bagisto?" icon="fa-info-circle">
  PayU comes built in with Bagisto core. In the Bagisto Admin panel, go to **Configuration > Payment Methods**, expand **PayU payment**, enter your Merchant Key and Salt, select the environment (Test/Production), set the payment title, enable the method, and save. For more information, refer to [Bagisto](doc:bagisto).
</Accordion>

<Accordion title="7. How do I test the PayU integration on Bagisto?" icon="fa-info-circle">
  Use Test Mode with PayU test credentials, complete test transactions using test card details, and verify transaction status in both Bagisto order management and the PayU Dashboard. For more information, refer to [Bagisto](doc:bagisto).
</Accordion>
