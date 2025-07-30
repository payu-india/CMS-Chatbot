---
title: Introduction
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - checkout integration
    - ' API reference'
    - ' payment gateway API integration'
    - ' payment aggregator API integration'
    - ' payment gateway integration'
    - ' UPI payment integration'
    - ' card payment integration'
    - ' NetBanking integration'
  robots: index
next:
  description: ''
---
PayU offers multiple payment workflows suitable for your online payment collection and disbursement strategy with diverse requirements and operational realities. Your website’s payment workflow is an integral part of your customer’s shopping experience. After the customer adds the products to the shopping cart on your website and checkout, you need to offer various payment modes to make the shopping experience complete.

# What is a payment gateway?

A payment gateway is a technology used by merchants to accept debit or credit card, UPI, wallets, EMI, etc. for purchases made by customers.

# Benefits

* Safer, faster, smoother transactions that give customers peace of mind.
* Secure and protect customers from frauds.
* Improves user experience, saves time, and empowers your customers.
* Enables you to accept multiple payment types and cards securely
* Reduces declined payments with real time transactions.

## Why v2 PayU APIs?

PayU v2 APIs represent a significant evolution in payment integration, offering improved developer experience, enhanced security, and better organization. This guide outlines the key advantages of migrating to v2 APIs.

### Key advantages of v2 APIs

<Accordion title="Simplified Authentication" icon="fa-shield-alt">
  **v2 APIs vs v1 APIs Authentication:**

  | Feature              | v1 APIs                   | v2 APIs                     |
  | -------------------- | ------------------------- | --------------------------- |
  | **Method**           | Complex hashing mechanism | Header-based authentication |
  | **Response Parsing** | Requires reverse hashing  | Direct JSON parsing         |
  | **Implementation**   | Complex hash generation   | Simple header configuration |
  | **Debugging**        | Difficult due to hashing  | Easy with standard headers  |

  **Benefits of v2 Authentication:**

  * ✅ Easier implementation and debugging
  * ✅ Reduced complexity in handling authentication
  * ✅ No need for reverse hashing to parse responses
  * ✅ More secure and standard authentication approach
</Accordion>

<Accordion title="Better Parameter Organization" icon="fa-layer-group">
  **v2 APIs vs v1 APIs Parameter Structure:**

  | Aspect              | v1 APIs                               | v2 APIs                          |
  | ------------------- | ------------------------------------- | -------------------------------- |
  | **Structure**       | Large, flat list of parameters        | Grouped JSON objects             |
  | **Maintainability** | Complex parameter management          | Clean, organized structure       |
  | **Readability**     | Difficult to understand relationships | Logical grouping of related data |
  | **Error Handling**  | Higher chances of mapping errors      | Reduced parameter mapping errors |

  **v2 API Structured Objects:**

  * `paymentMethod` - Payment method details
  * `paymentCard` - Card-specific information
  * `order` - Order and product details
  * `paymentChargeSpecification` - Pricing information
  * `additionalInfo` - Additional configuration
  * `callBackActions` - Success/failure URLs
  * `billingDetails` - Customer billing information
  * `authorization` - 3DS authorization data
</Accordion>

<Accordion title="Enhanced Developer Experience" icon="fa-code">
  **Developer Experience Improvements:**

  <HTMLBlock>{`
                        <table>
                          <thead>
                            <tr>
                              <th>Feature</th>
                              <th>v1 APIs</th>
                              <th>v2 APIs</th>
                              <th>Impact</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td><strong>Learning Curve</strong></td>
                              <td>Steeper due to hashing complexity</td>
                              <td>Gentler with standard practices</td>
                              <td>🟢 Faster onboarding</td>
                            </tr>
                            <tr>
                              <td><strong>Code Readability</strong></td>
                              <td>Complex parameter lists</td>
                              <td>Structured JSON objects</td>
                              <td>🟢 Better maintainability</td>
                            </tr>
                            <tr>
                              <td><strong>Error Debugging</strong></td>
                              <td>Hash validation issues</td>
                              <td>Clear parameter validation</td>
                              <td>🟢 Easier troubleshooting</td>
                            </tr>
                            <tr>
                              <td><strong>Integration Time</strong></td>
                              <td>Longer due to complexity</td>
                              <td>Faster with modern patterns</td>
                              <td>🟢 Reduced development time</td>
                            </tr>
                          </tbody>
                        </table>
  `}</HTMLBlock>
</Accordion>

### v2 API request structure

<Accordion title="Sample Request Structure" icon="fa-code">
  ```json
  {
      "accountId": "smsplus",
      "txnId": "b5f2d8785768087678fm9",
      "amount": "1000",
      "paymentMethod": {
          "name": "CreditCard",
          "bankCode": "CC",
          "paymentCard": {
              "cardNumber": "5497774415170603",
              "validThrough": "05/2025",
              "cvv": "123",
              "ownerName": "Ashish"
          }
      },
      "order": {
          "productInfo": "Product details",
          "orderedItem": [
              {
                  "itemId": "1",
                  "description": "Product A",
                  "quantity": 1,
                  "amount": 1000
              }
          ],
          "userDefinedFields": {
              "udf1": "test1",
              "udf2": "test2",
              "udf3": "test3",
              "udf4": "test4",
              "udf5": "test5"
          },
          "paymentChargeSpecification": {
              "price": "1000"
          }
      },
      "additionalInfo": {
          "enforcePaymethod": "CC",
          "createOrder": true,
          "authOnly": false
      },
      "callBackActions": {
          "successAction": "https://checkout.payu.in/testCB/success",
          "failureAction": "https://checkout.payu.in/testCB/failure",
          "cancelAction": "https://checkout.payu.in/testCB/cancel"
      },
      "billingDetails": {
          "firstName": "Ashish",
          "lastName": "Kumar",
          "address1": "123 Main Street",
          "phone": "9123456789",
          "email": "testv2@example.in",
          "city": "Bharatpur",
          "state": "Rajasthan",
          "country": "India",
          "zipCode": "321028"
      },
      "authorization": {
          "eci": "05",
          "cavv": "AAABAWFlmQAAAABjRWWZEEFgFz",
          "flowType": "Frictionless",
          "threeDSTransID": "67b4c71f-19bf-4d97-bd09-4e3687dc9e42",
          "threeDSServerTransID": "eea30d14-71cf-41af-b961-f95b7d67dc93",
          "threeDSTransStatus": "Y",
          "threeDSTransStatusReason": "01",
          "aquirer_bin": "401200",
          "additionalInfo": {
              "authUdf1": "string",
              "authUdf2": "string"
          }
      },
      "threeDS2RequestData": {
          "threeDSVersion": "2.2.0",
          "deviceChannel": "APP"
      }
  }
  ```
</Accordion>

<Accordion title="JSON Object Breakdown" icon="fa-list">
  **Key JSON Objects in v2 APIs:**

  <HTMLBlock>{`
                        <table>
                          <thead>
                            <tr>
                              <th>JSON Object</th>
                              <th>Purpose</th>
                              <th>Key Benefits</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td><code>paymentMethod</code></td>
                              <td>Payment method configuration</td>
                              <td>Centralized payment type management</td>
                            </tr>
                            <tr>
                              <td><code>paymentCard</code></td>
                              <td>Card-specific details</td>
                              <td>Secure card data handling</td>
                            </tr>
                            <tr>
                              <td><code>order</code></td>
                              <td>Order and product information</td>
                              <td>Complete transaction context</td>
                            </tr>
                            <tr>
                              <td><code>billingDetails</code></td>
                              <td>Customer billing information</td>
                              <td>Organized customer data</td>
                            </tr>
                            <tr>
                              <td><code>callBackActions</code></td>
                              <td>Success/failure URLs</td>
                              <td>Clear flow management</td>
                            </tr>
                            <tr>
                              <td><code>authorization</code></td>
                              <td>3DS authentication data</td>
                              <td>Enhanced security handling</td>
                            </tr>
                          </tbody>
                        </table>
  `}</HTMLBlock>
</Accordion>

## Recommended migration strategy

<Accordion title="For Existing Merchants" icon="fa-building">
  **Continued Support & Flexibility:**

  * ✅ **v1 APIs remain fully supported** - No disruption to existing integrations
  * ✅ **No immediate migration required** - Continue operations without interruption
  * ✅ **Seamless coexistence** - v1 and v2 APIs can work together during transition
  * ✅ **Optional migration** - Upgrade to v2 for enhanced features when ready

  **Migration Benefits:**

  * Enhanced security with header-based authentication
  * Better code maintainability with structured parameters
  * Access to new features and improvements
  * Future-proof integration approach
</Accordion>

<Accordion title="For New Merchants" icon="fa-rocket">
  **v2-First Approach:**

  * ✅ **Encouraged to use v2 APIs only** - Start with the latest technology
  * ✅ **Access to latest features** - All new capabilities available immediately
  * ✅ **Better long-term support** - Priority support for v2 implementations
  * ✅ **Integration team guidance** - Dedicated support for v2 implementation

  **Advantages for New Merchants:**

  * Modern API design patterns from day one
  * Reduced complexity in initial setup
  * Better developer experience
  * Future-ready integration
</Accordion>

<Accordion title="🔗 API Availability & Compatibility" icon="fa-link">
  **Current API Landscape:**

  <HTMLBlock>{`
                        <table>
                          <thead>
                            <tr>
                              <th>Aspect</th>
                              <th>Status</th>
                              <th>Details</th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td><strong>v2 API Coverage</strong></td>
                              <td>🟢 Comprehensive</td>
                              <td>Covers most common payment use cases</td>
                            </tr>
                            <tr>
                              <td><strong>Duplicate API Elimination</strong></td>
                              <td>🟡 In Progress</td>
                              <td>v1 APIs with duplicate functionality being phased out</td>
                            </tr>
                            <tr>
                              <td><strong>v1 Documentation</strong></td>
                              <td>🔄 Being Updated</td>
                              <td>Adding disclaimers and v2 alternative links</td>
                            </tr>
                            <tr>
                              <td><strong>Compatibility</strong></td>
                              <td>✅ Full Support</td>
                              <td>Both versions work together seamlessly</td>
                            </tr>
                          </tbody>
                        </table>
  `}</HTMLBlock>
</Accordion>

<Accordion title="🏗️ Modern Architecture" icon="fa-building">
  **Built for Today's Standards:**

  1. **Modern API Design**: Following current REST API best practices
  2. **JSON-First Approach**: Native JSON structure for better integration
  3. **Stateless Design**: Improved scalability and reliability
  4. **Standard HTTP Methods**: Conventional HTTP verb usage
</Accordion>

<Accordion title="🔒 Enhanced Security" icon="fa-shield-alt">
  **Security Improvements:**

  1. **Header-Based Authentication**: Eliminates complex hashing requirements
  2. **Standard Security Practices**: Industry-standard authentication methods
  3. **Reduced Attack Surface**: Simplified authentication reduces vulnerabilities
  4. **Better Debugging**: Easier to troubleshoot security issues
</Accordion>

<Accordion title="🛠️ Developer Experience" icon="fa-tools">
  **Development Advantages:**

  1. **Clear Structure**: Logical parameter grouping for better understanding
  2. **Reduced Complexity**: No need for reverse hashing or complex calculations
  3. **Better Documentation**: Structured approach enables clearer documentation
  4. **Faster Integration**: Modern patterns reduce development time
</Accordion>

<Accordion title="🔮 Future-Proof Design" icon="fa-rocket">
  **Long-Term Benefits:**

  1. **New Feature Priority**: All new features developed for v2 first
  2. **Enhanced Support**: Priority support and maintenance for v2 APIs
  3. **Technology Evolution**: Aligned with modern payment industry standards
  4. **Scalability**: Better prepared for future growth and requirements
</Accordion>

# Get support

Our dedicated support team is here to assist you if you encounter any issues or have questions during your integration process. Visit [https://help.payu.in](https://help.payu.in) and raise a ticket.