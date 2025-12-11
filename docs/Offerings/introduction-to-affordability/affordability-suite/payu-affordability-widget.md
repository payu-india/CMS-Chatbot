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

* **Influence customer decisioning at the time of product selection**​
  Customers can discover offers + available affordability options at the time of purchase selection thereby nudging customers to make purchases & improve top of the funnel conversion rates​

* **Informed decision about the customized affordability rates & eligibility**​
  Customers can quickly use the EMI calculator to check rate of interests and EMI payment amounts. Customers to get customised options and offers basis They may also enter card/ mobile number to quickly check eligibility in the specific purchase context​

* **Entry Point to the NTB flow (Upcoming feature)**​
  Ineligible customers may apply for a quick digital loan to complete the purchase​

* **Improved discoverability of offers (Upcoming feature) **​
  Customers can compare and evaluate customized (basis token/cookie/mobile) offers on the PDP page itself. Additionally, customers can check eligibility of offers basis their cust id/mobile /card number​

* **Custom Promotions (Upcoming feature ) **​
  Merchants can specify custom messages/promotions which can be displayed on the widget​

* **Zero integration Effort**​
  Merchants need to embed a 4–5-line HTML code (via a JS file) to display widgets on their PDP pages​

* **Customize to merchant’s specific website theme (Upcoming feature)**​
  Merchants to choose widget orientation /color scheme etc to ensure widget fits in their website seamlessly. Additionally, merchant can control specific features to be enabled/disabled ​

## Widget Components

### Affordability Widget

The main widget displays:

* BNPL or EMI plans based on purchase amount
* Consolidated affordability options in a single interface
* PayU branding and trust indicators

<Image align="center" border={true} src="https://files.readme.io/37de7e8844ab437abd7e0fc3c5603a3f4ab5cb218bfe7b4f2f98b03300c990a2-widget_expanded_view.png" className="border" />

In the above example:

* **BNPL Options**: For purchases under ₹5,000
* **Credit Card EMI**: Various tenure options with interest rates
* **Debit Card EMI**: Bank-specific EMI plans
* **Cardless EMI**: Digital loan options
* Offer descriptions, effective pricing, and discount information

### Offers Widget

<Image align="center" border={false} src="https://files.readme.io/29f91c78fe57f01127f928c2317adc8bd253ebabe496394ccb90b7a1678a3aa9-figure_08_widget_screenshot.png" />

The above screenshot displays an example of offers integration:

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
