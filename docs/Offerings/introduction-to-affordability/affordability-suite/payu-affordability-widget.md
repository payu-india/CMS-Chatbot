---
title: PayU Affordability Widget
deprecated: false
hidden: true
metadata:
  robots: index
---
# PayU Affordability Widget - Developer Guide Overview

## Overview

The PayU Affordability Widget is a lightweight, customizable solution that enables merchants to seamlessly integrate affordability options directly on their Product Display Pages (PDPs). The widget provides customers with transparent access to EMI plans, Buy Now Pay Later (BNPL) offers, and personalized discounts to enhance purchase decision-making and improve conversion rates.

## Key Features

### Customer-Facing Features

* **EMI Calculator**: Transparent display of interest rates, payment amounts, and eligibility
* **BNPL Integration**: Quick access to Buy Now Pay Later options for amounts under ₹5,000
* **Personalized Offers**: Customized offers based on user tokens, cookies, customer ID, or mobile number
* **Comprehensive Affordability Options**: Credit Card EMI, Debit Card EMI, and Cardless EMI plans
* **Responsive Design**: Optimized for both desktop and mobile devices

### Merchant-Facing Features

* **Zero Integration Effort**: Simple HTML embed with 4-5 lines of code
* **Fast Loading**: Lightweight widget that loads after merchant website completion
* **Customizable Design**: Widget appearance can be customized to match website themes (upcoming)
* **Custom Promotions**: Ability to send targeted messages and offers to customers
* **Performance Optimized**: Minimal impact on website loading times

## Widget Components

### 1. Main Affordability Widget

<Image border={false} />

The main widget displays:

* BNPL or EMI plans based on purchase amount
* Consolidated affordability options in a single interface
* PayU branding and trust indicators

### 2. Expanded Drawer View

_[Figure 2: PayU Affordability Widget - Expanded Drawer]_  
`[PLACEHOLDER: Screenshot showing the expanded drawer with detailed EMI and BNPL options]`

The expanded view includes:

* **BNPL Options**: For purchases under ₹5,000
* **Credit Card EMI**: Various tenure options with interest rates
* **Debit Card EMI**: Bank-specific EMI plans
* **Cardless EMI**: Digital loan options
* Offer descriptions, effective pricing, and discount information

### 3. Offers Widget

_[Figure 3: Offers Widget Display]_  
`[PLACEHOLDER: Screenshot showing the offers widget with active promotions and discounts]`

Displays:

* Active merchant-specific offers
* Personalized promotions
* Discount information and terms

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
```

_[Figure 4: Code Implementation Example]_  
`[PLACEHOLDER: Screenshot showing the HTML code implementation in a developer IDE or text editor]`

#### Step 2: Configuration Parameters

| Parameter        | Type   | Required | Description                                              |
| ---------------- | ------ | -------- | -------------------------------------------------------- |
| `amount`         | Number | Yes      | Product purchase amount                                  |
| `merchantId`     | String | Yes      | Your PayU merchant identifier                            |
| `userIdentifier` | String | Optional | Customer mobile number, email, or ID for personalization |
| `customization`  | Object | Optional | Widget appearance settings (upcoming)                    |

#### Step 3: Advanced Configuration (Upcoming)

```javascript
PayUAffordabilityWidget.init({
  amount: 15000,
  merchantId: 'MERCHANT123',
  userIdentifier: 'customer@email.com',
  customization: {
    orientation: 'horizontal', // 'vertical' or 'horizontal'
    colorScheme: 'light', // 'dark' or 'light'
    theme: 'custom' // Use merchant's brand colors
  }
});
```

### Mobile Responsiveness

_[Figure 5: Mobile Widget Display]_  
`[PLACEHOLDER: Screenshot showing the widget displayed on mobile devices in both collapsed and expanded states]`

The widget automatically adapts to different screen sizes:

* Responsive layout for mobile devices
* Touch-optimized interactions
* Maintains functionality across all device types

## Widget Anatomy

### Desktop Layout

_[Figure 6: Desktop Widget Anatomy]_  
`[PLACEHOLDER: Annotated screenshot showing different parts of the widget on desktop - EMI section, BNPL section, offers area, etc.]`

### Mobile Layout

_[Figure 7: Mobile Widget Anatomy]_  
`[PLACEHOLDER: Annotated screenshot showing the mobile layout with collapsed/expanded states and touch interaction areas]`

## Use Cases and Benefits

### For Customers

* **Informed Decision Making**: Clear visibility of financing options before purchase
* **Transparency**: Upfront display of EMI rates, tenures, and eligibility
* **Convenience**: Quick access to BNPL and digital loan applications
* **Personalization**: Tailored offers based on customer profile

### For Merchants

* **Increased Conversions**: Higher purchase completion rates through affordability options
* **Enhanced User Experience**: Seamless integration without redirecting customers
* **Improved Offer Visibility**: Better discoverability of promotions and discounts
* **Minimal Development Effort**: Quick integration with simple HTML embed

## Entry Points and User Flows

### New-to-Bank (NTB) Flow (Upcoming)

_[Figure 8: NTB User Flow Diagram]_  
`[PLACEHOLDER: Flowchart showing the journey for customers not eligible for existing EMI options, leading to quick digital loan application]`

For customers not eligible for standard EMI options:

1. Widget displays alternative options
2. Customer can apply for quick digital loans
3. Seamless onboarding process within the widget

### Existing Customer Flow

_[Figure 9: Existing Customer Flow]_  
`[PLACEHOLDER: Flowchart showing the journey for eligible customers with existing cards/accounts]`

For eligible customers:

1. Personalized EMI and BNPL options displayed
2. Real-time eligibility check
3. Direct selection and checkout integration

## Performance Considerations

### Loading Strategy

* Widget loads after merchant website completion
* Asynchronous loading prevents blocking of main content
* Minimal JavaScript footprint for fast execution

### Optimization Features

_[Figure 10: Performance Metrics Dashboard]_  
`[PLACEHOLDER: Screenshot of performance monitoring dashboard showing load times, conversion rates, and user engagement metrics]`

* Lazy loading of widget content
* Cached offer information for returning customers
* Optimized API calls for real-time data

## Customization Options

### Current Customization

* Basic widget positioning
* Amount and merchant-specific configurations
* User identifier for personalization

### Upcoming Customization Features

_[Figure 11: Customization Options Panel]_  
`[PLACEHOLDER: Screenshot showing the future customization interface with color schemes, layouts, and branding options]`

* Custom color schemes to match brand identity
* Widget orientation (horizontal/vertical)
* Advanced styling options
* Custom promotional messages

## Next Steps

1. **Contact Integration Team**: Reach out to PayU integration support for merchant ID and setup
2. **Development Environment**: Test integration in staging environment
3. **Widget Customization**: Configure widget appearance and behavior
4. **Go Live**: Deploy to production after thorough testing
5. **Monitor Performance**: Track conversion metrics and customer engagement

***

_For technical support and integration assistance, contact the PayU Developer Support team._
