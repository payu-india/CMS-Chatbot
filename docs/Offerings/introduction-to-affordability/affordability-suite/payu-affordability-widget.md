---
title: PayU Affordability Widget
deprecated: false
hidden: false
metadata:
  robots: index
---
The PayU Affordability Widget is a lightweight, customizable solution that enables merchants to seamlessly integrate affordability options directly on their Product Display Pages (PDPs). The widget provides customers with transparent access to EMI plans, Buy Now Pay Later (BNPL) offers, and personalized discounts to enhance purchase decision-making and improve conversion rates.

## Key Features

### Customer-Facing Features
- **EMI Calculator**: Transparent display of interest rates, payment amounts, and eligibility
- **BNPL Integration**: Quick access to Buy Now Pay Later options for amounts under ₹5,000
- **Personalized Offers**: Customized offers based on user tokens, cookies, customer ID, or mobile number
- **Comprehensive Affordability Options**: Credit Card EMI, Debit Card EMI, and Cardless EMI plans
- **Responsive Design**: Optimized for both desktop and mobile devices

### Merchant-Facing Features
- **Zero Integration Effort**: Simple HTML embed with 4-5 lines of code
- **Fast Loading**: Lightweight widget that loads after merchant website completion
- **Customizable Design**: Widget appearance can be customized to match website themes (upcoming)
- **Custom Promotions**: Ability to send targeted messages and offers to customers
- **Performance Optimized**: Minimal impact on website loading times

## Widget Components

### 1. Main Affordability Widget
*[Figure 1: PayU Affordability Widget - Collapsed View]*  
`[PLACEHOLDER: Screenshot showing the main widget in its collapsed state on a PDP]`

The main widget displays:
- BNPL or EMI plans based on purchase amount
- Consolidated affordability options in a single interface
- PayU branding and trust indicators

### 2. Expanded Drawer View
*[Figure 2: PayU Affordability Widget - Expanded Drawer]*  
`[PLACEHOLDER: Screenshot showing the expanded drawer with detailed EMI and BNPL options]`

The expanded view includes:
- **BNPL Options**: For purchases under ₹5,000
- **Credit Card EMI**: Various tenure options with interest rates
- **Debit Card EMI**: Bank-specific EMI plans
- **Cardless EMI**: Digital loan options
- Offer descriptions, effective pricing, and discount information

### 3. Offers Widget
*[Figure 3: Offers Widget Display]*  
`[PLACEHOLDER: Screenshot showing the offers widget with active promotions and discounts]`

Displays:
- Active merchant-specific offers
- Personalized promotions
- Discount information and terms

## Technical Implementation

### Integration Steps

#### Step 1: Basic HTML Integration
Add the following HTML snippet to your Product Display Page:

```html
<!-- PayU Affordability Widget Integration -->
<div id="payu-affordability-widget"></div>
<script src="[PayU Widget JS URL]"></script>
<script>
  PayUAffordabilityWidget.init({
    amount: '[PRODUCT_AMOUNT]',
    merchantId: '[YOUR_MERCHANT_ID]',
    userIdentifier: '[CUSTOMER_MOBILE_OR_ID]'
  });
</script>
