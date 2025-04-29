---
title: FAQs
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
- **What is Dynamic Currency Conversion (DCC)?**

Dynamic Currency Conversion (DCC) is a feature that allows merchants to price their goods and services in multiple currencies. This can be beneficial for merchants who want to sell to customers in other countries.

- **How does DCC work?**

DCC works by using a real-time currency converter to convert the merchant’s price into the customer’s currency. This ensures that the customer always sees the price in their own currency.

- **What are the benefits of using DCC?**

DCC offers a number of benefits for merchants, including:

- **Increased sales**: DCC can help merchants increase sales by making it easier for customers to pay in their own currency.
- **Improved customer experience**: DCC can improve the customer experience by making it easier for customers to understand the price of goods and services.
- **Reduced fraud**: DCC can help reduce fraud by making it more difficult for customers to make fraudulent payments.
- **How can I integrate DCC into my website or app?**

There are a number of ways to integrate DCC into your website or app. One way is to use a third-party payment processor, such as PayU. Another way is to integrate the PayU API directly into your website or app.

- **What are the supported payment methods for DCC?**

A: The supported payment methods for DCC vary depending on the country you are selling to. In general, the most common payment methods for DCC are credit cards, debit cards, and bank transfers.

- **What are the modes of payments PayU supports for international payment?**  
  You can accept international payment using Credit Card, Debit Card, Prepaid Cards.
- **What is Dynamic Currency Conversion?**
- Dynamic currency conversion allows merchants to price goods and services in consumer’s card issuing currency on the fly while still receiving fund settlement in chosen currency (INR).
- For consumers, it helps to better comprehend the price of goods/services in the currency they understand well.
- **How is an international transaction processed?**
- Consumer lands on the merchant’s checkout page/PayU checkout page and sees transaction amount in INR
- Consumer enters his card details and proceeds to Pay
- Merchant redirects the consumer to PayU’s payment interface
- PayU detects consumer’s card issuing currency
- PayU processes the transaction by applying exchange rate/margins on card issuing currency
- PayU settles the merchant in INR
- **How is DCC transaction processed?**
- Consumer lands on the merchant’s checkout page/PayU Checkout page and sees transaction amount INR
- Consumer enters his card details and proceeds to Pay
- Merchant redirects the consumer to PayU’s payment interface
- PayU detects consumer’s card issuing currency is different from INR
- PayU offers choice of paying in consumer’s card currency (ex. USD) or merchant currency (INR)
- Depending on the currency chosen by the consumer, PayU processes the transaction downstream via a supporting PG
- **What are the supported currencies by PayU?**

You can accept international cards in 130+ currencies. You can, however, show local prices in 27 different currencies, such as USD, CAD, EUR, GBP, CNH, SGD among others.

- **What is FIRC certificate?**

Foreign Inward Remittance Certificate (FIRC) is a document that provides proof of inward remittance to India. It is treated as documentary evidence by most of the statutory authorities for confirming the validity of the foreign money received by the beneficiary.

- **Does PayU provides FIRC certificate?**

Yes, PayU provides FIRC certificate, you can reach out to your PayU Key Account Manager (KAM) for more details.

- **What are the settlement cycles supported for international payment?**

Ideally, it takes two business days to settle international payments in your account. PayU also supports instant settlement, you can reach out to your account manager or drop a mail to [support@payu.in](mailto:support@payu.in) for more details.

- **What are the settlement currencies supported by PayU?**

PayU settles all international payments in INR. Also, the exchange rate is calculated as per the rate on the day of the transaction.

- **What are the different types of integration available with PayU for international payments?**

PayU supports both PayU hosted, and Merchant hosted checkout for International/Dynamic Currency Conversion transactions.

- **What is the list of documents required by merchant for enabling international payments?**

The following documents needs to submitted with PayU while onboarding or to enable international payments. These can vary from case to case or LOB basis. For more information, reach out to your PayU Key Account Manager.

- Bank statement (Last 1 year) / ITR (Last 2 years). \*(Only for startups)
- Audited balance sheet for last 2 years. (If Company is more than 2 Years Old)
- Profit and loss statement (If Company is more than 2 years old)
- Import/Export certificate in case of tangible products.
- FSSAI license in case of bakeries and food items.
- IATA certificate in case of travel business or any other authorized certificate for travel LOB.
- **What are the integration changes to enable International?**

There are no integration changes to enable international payments with your existing integration in place.

- **What are the integration changes to enable DCC?**

There is no technical change to process DCC with existing payment integrations. There will just be an intermediary page for users to select currency and confirm margins which merchants need to embed in their website/app.

- **What are the fees associated with DCC?**

A: The fees associated with DCC vary depending on the payment method, the country you are selling to, and the amount of money you are selling. In general, DCC can be expensive, due to the following factors:

- Currency conversion fees
- International transaction fees
- Merchant fees
- **How can I reduce the fees associated with DCC?**

There are a number of ways to reduce the fees associated with DCC, including:

- Using a third-party payment processor that offers competitive fees
- Selling in bulk
- Negotiating a fee discount with your bank
- **What are the benefits of using PayU Hosted Checkout for international payments?**

PayU Hosted Checkout for international payments offers a number of benefits for merchants, including:

- A secure and convenient checkout experience for customers
- A variety of payment options, including credit cards, debit cards, and net banking
- A simple and easy integration process
- Competitive pricing
- **How do I enable international payments with my PayU Hosted Checkout integration?**

To enable international payments with your PayU Hosted Checkout integration, contact your PayU Key Account Manager.

- **What are the supported payment methods for PayU Hosted Checkout for international payments?**

The supported payment methods for PayU Hosted Checkout for international payments vary depending on your location. In India, the supported payment methods include credit cards, debit cards, and net banking.

- **How can I get started with PayU Hosted Checkout for international payments?**

A: To get started with PayU Hosted Checkout for international payments, you will need to create a PayU account and obtain your PayU credentials. You can then integrate the PayU Hosted Checkout SDK into your website or app. After you have integrated the SDK, you will need to configure your PayU settings and test your integration. For more information, refer to [PayU Hosted Checkout Integration for DCC](doc:payu-hosted-checkout-integration-dynamic-currency-conversion)

- **What are the benefits of using PayU Merchant Hosted Checkout for international payments?**

PayU Merchant Hosted Checkout for international payments offers a number of benefits for merchants, including:

- A secure and convenient checkout experience for customers
- A variety of payment options, including credit cards and debit cards
- A simple and easy integration process
- Competitive pricing
- **What are the supported payment methods for PayU Merchant Hosted Checkout for international payments?**

The supported payment methods for PayU Merchant Hosted Checkout for international payments vary depending on your location. In India, the supported payment methods include credit cards, debit cards, and net banking.

- **How can I get started with PayU Merchant Hosted Checkout for international payments?**

To get started with PayU Merchant Hosted Checkout for international payments, you will need to create a PayU account and obtain your PayU credentials. You can then integrate the PayU Merchant Hosted Checkout into your website or Checkout Pro SDK for mobile app. Once you have integrated the SDK, you will need to configure your PayU settings and test your integration. For more information, refer to following sections: 

- Web Checkout: [PayU Hosted Checkout Integration for DCC](doc:payu-hosted-checkout-integration-dynamic-currency-conversion) or [Merchant Hosted Checkout Integration for DCC](doc:merchant-hosted-checkout-dynamic-currency-conversion)
- Mobile SDK:
- **What are the different types of international payments that can be made using Merchant Hosted Checkout?**

There are two main types of international payments that can be made using PayU Merchant Hosted Checkout:

- **Domestic payments:** These are payments made in the currency of the merchant’s website or app. For example, a merchant in India could accept payments in Indian rupees (INR) from customers in India.
- **Cross-border payments:** These are payments made in a currency that is different from the merchant’s website or app. For example, a merchant in India could accept payments in US dollars (USD) from customers in the United States.