---
title: Integrate WhatsApp Payments
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integrate PayU for WhatsApp Payments
  description: >-
    Learn how to integrate WhatsApp Payments with PayU to enhance your business
    transactions. This guide provides detailed steps for setting up and managing
    payments via WhatsApp, ensuring a seamless and efficient payment process for
    your customers. Ideal for businesses seeking to leverage WhatsApp for
    payment solutions.
  keywords:
    - Integrate PayU for WhatsApp Payments
    - Steps to Integrate PayU for WhatsApp Payments
    - PayU for WhatsApp Payments Integration
    - PayU for WhatsApp Payments Set up
  robots: index
next:
  description: ''
---
To enable payments for partners powered by PayU, following steps need to be completed:

<Cards>
  <Card title="Step 1: Integrate with WhatsApp Business APIs" href="#step-1-integrate-with-whatsapp-business-apis" icon="fa-globe">
    New to our platform? Follow this guide to get started.
  </Card>

  <Card title="Step 2: Link PayU Account with WhatsApp" href="#step-2-link-account-with-whatsapp" icon="fa-tools">
    Explore our interactive API reference.
  </Card>
</Cards>

## Step 1: Integrate with WhatsApp Business APIs

PayU has partnered with the top BSPs in India for seamless integration & enablement with a few clicks. Please reach out to your BSP to enable WhatsApp payments. In case your BSP currently does not offer native payments, please reach out to Meta directly.

<Callout icon="👍">
  **Reference**: For more details around the WhatsApp Business APIs for native payments, refer to [Meta Native Payments Documentation ](https://developers.facebook.com/docs/whatsapp/on-premises/payments-api/payments-in/pg).
</Callout>

## Step 2: Link PayU Account with WhatsApp

Once the BSP has integrated with WhatsApp Business APIs and integrated payments, you need to link your PayU account with WhatsApp. Depending on how your WhatsApp Business account is managed, following approaches are applicable:

* **Self-owned WhatsApp Business Account**: Directly link your WhatsApp Business Account with PayU using the Meta Business Manager. This is applicable if your have direct access to your Meta Business Manager.
* **BSP-owned WhatsApp Business Account**: Link your WhatsApp Business Account with the help of the BSP provider. This is applicable if you do not have direct access to your Meta Business Manager - and the BSP runs it end-to-end.

### Self-owned WhatsApp Business Account

To integrate PayU with your WhatsApp Business Account:

1. Log in to Meta Business Manager
2. Create a Direct Pay Method.
3. Select PayU as the payment gateway.
4. Shares the link generated with the merchant that will redirect to PayU payment page.
5. Configure PayU Key and Salt. For more information on checking your Key and Salt, refer to [Check your API Key and Salt](doc:check-api-key-and-salt).

> 📘 Reference:
>
> For detailed instructions on self-owned WhatsApp business account linking, refer to [Link PayU with WhatsApp Business Account​](doc:link-payu-with-whatsapp-business-account).

### BSP-owned WhatsApp Business Account

If you use a BSP-owned WABA, below is the workflow to link your PayU account with WhatsApp.

1. The BSP logs in to WhatsApp Manager
2. BSP creates a Direct Pay Method and selects PayU as the payment gateway.
3. Shares the link generated with the merchants that will redirect them to PayU
4. The merchant logs in and allows Meta to request payments on their behalf

## Next Steps

After linking your PayU account with WhatsApp, you will be ready to incorporate seamless payments within your existing flows or create new ones with the help of your BSP.
