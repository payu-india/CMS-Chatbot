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

MCC helps businesses expand internationally while providing customers with the clarity and convenience of seeing prices in their familiar currency throughout their shopping journey. The following workflow provides steps involved in DCC with sample checkout page:

<Image align="center" className="border" border={true} src="https://files.readme.io/c48884f6a01962d61d33c46466cb387103a3e08b78a45b385a529f62991d81e5-dcc_demo_page.png" />

1. Customer browses products on merchant’s website and sees prices on website in their local currency.
2. Merchant initiates payment with PayU for products selected by the customer
3. Customer enters their international card details on checkout
4. Payment gets captured successfully in merchant initiated currency 
5. Customer is redirected back to merchant’s website and order is confirmed