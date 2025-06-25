---
title: Workflow
deprecated: false
hidden: false
metadata:
  title: PayU International Payments Workflow
  description: >-
    Discover how to integrate international payments with PayU, a leading online
    payment service provider in India. Learn how to enable dynamic currency
    conversion for your customers using PayU’s hosted checkout and APIs.
  keywords:
    - Dynamic Currency Conversion Workflow
    - DCC Integration Steps
    - PayU Currency Conversion Workflow
    - Currency Conversion Process
    - DCC Implementation Workflow
    - Multi-Currency Payment Flow.International Payments Workflow
    - Foreign Currency Payment Setup
  robots: index
next:
  description: ''
---
## Currency Conversion Solutions for Global Business

PayU offers flexible currency conversion options, enabling merchants to choose between Dynamic Currency Conversion (DCC) and Multi-Currency Conversion (MCC) based on their specific business requirements. These solutions allow businesses to optimize international payment experiences while maintaining operational efficiency, supporting various customer preferences across global markets.

## Multi-Currency Conversion (MCC)

Multi-Currency Conversion (MCC) is a payment solution that enables merchants to display prices and process transactions in multiple currencies. MCC allows merchants to display prices in the customer's local currency, creating a seamless international shopping experience. With PayU's MCC solution, businesses can offer localized pricing across 27+ currencies while managing operations in their base currency.

**Key Benefits:**

* **Enhanced Customer Experience**: Customers can understand and transact in their local currency, making international purchases transparent and convenient
* **Flexible Currency Support**: Access to 27+ currency options to serve diverse global markets
* **FX Rates on the fly**: Use PayU's FX rate APIs which source rates directly from card networks or any third-party APIs while initiating payments with PayU
* **Risk-free Refunds**: Initiate refunds in the customer's original currency, reducing forex risks and losses
* **Simplified Global Expansion**: Display prices and accept payments in multiple currencies without complex operational changes
* **Convenient Settlements:** Get settlements in INR or non-INR currencies as per your business needs. 

MCC helps businesses expand internationally while providing customers with the clarity and convenience of seeing prices in their familiar currency throughout their shopping journey. The following steps describes the workflow involved in DCC with sample checkout page screenshots.

1. Customer browses products on merchant’s website and sees prices on website in their local currency.

<Image align="center" className="border" border={true} src="https://files.readme.io/c48884f6a01962d61d33c46466cb387103a3e08b78a45b385a529f62991d81e5-dcc_demo_page.png" />

2. Merchant initiates payment with PayU for products selected by the customer.

<Image align="center" className="border" border={true} src="https://files.readme.io/7ab35f606b877e9d46d1faace2845b4c464aeb01a240576e790ba5ecfc04c2c7-dcc_local_currency.png" />

3. Customer enters their international card details on checkout.

<Image align="center" className="border" border={true} src="https://files.readme.io/6690d72af4a2537cfeffdfa30d71b966b83e65e058592c71c1d6262f3f0ba6a1-dcc-enter-card-details.png" />

4. Payment gets captured successfully in merchant initiated currency.

<Image align="center" className="border" border={true} src="https://files.readme.io/8846f3766b3bb77655a8cf850aae5ef54eaedafc7e2cc05b8abb7a8f30749118-dcc-payment-successful.png" />

5. Customer is redirected back to merchant’s website and order is confirmed.

<Image align="center" className="border" border={true} src="https://files.readme.io/3f40f34f39a7916e4f37abb8877655ad84e1a2bb9a47d3d2e37b861306774652-dcc-order-confirmation.png" />