---
title: Banking Connect - IBMB or NBBL
deprecated: false
hidden: true
metadata:
  robots: index
---
**NBBL (NPCI Bharat Bill Pay)** has developed the **Net Banking Interoperable Platform (IBMB/Banking Connect)** to modernize and revitalize net banking in India. This platform addresses the long-standing challenges of traditional net banking by providing interoperability, standardized settlements, and enhanced user experience.

PayU has been selected as a key partner to pilot this new net banking platform, enabling merchants to offer a modern, seamless net banking payment experience to their customers.

### What is NBBL?

NBBL's Interoperable Platform is a centralized payment system that enables:

* **Single Integration** – Merchants integrate once with NBBL to accept payments from multiple banks
* **Mobile-First Experience** – Authentication and authorization handled within the issuer's mobile app
* **Near-Real-Time Settlement** – Faster fund transfers between banks
* **No Amount Limits** – Process transactions of any size
* **Standardized Operations** – Unified dispute management and settlement processes

<Accordion title="Challenges with Traditional Net Banking" icon="fa-info-circle">
  Despite significant advancements in India's payments landscape, net banking has remained largely unchanged for over a decade. While UPI and cards have revolutionized transactions, net banking continues to struggle with:

  ### Key Challenges

  | Challenge                   | Impact                                                                              |
  | :-------------------------- | :---------------------------------------------------------------------------------- |
  | **Multiple Integrations**   | Payment Aggregators need to integrate with 40-50 individual banks separately        |
  | **Varying Commercials**     | Pricing varies widely by industry sector (flat rates, percentage, revenue-sharing)  |
  | **Unpredictable Refunds**   | No defined TAT; process varies by bank (2-10 days)                                  |
  | **Inconsistent Settlement** | Settlement times vary significantly between banks                                   |
  | **Low Success Rates**       | Frequently below 50%, with significant variations between banks                     |
  | **Poor User Experience**    | Mandatory Customer ID & Password, step-up authentication (OTP & Security Questions) |
  | **Lack of Risk Checks**     | No defined risk checklist; up to bank discretion                                    |
  | **Dispute Management**      | Difficult to resolve disputes without centralized authority                         |

  ### Why Net Banking Still Matters

  Despite challenges, net banking offers unique advantages:

  * **High Ticket Size** – Often used for large transactions
  * **Flat Rate Commercials** – Attractive pricing model for businesses
  * **TPV Features** – Supports various transaction processing functionalities
  * **Bank Security** – Strong authentication credentials and risk mitigation

  NBBL's platform addresses these challenges through a centralized, interoperable system that standardizes net banking transactions across all participating banks and payment aggregators.
</Accordion>

## Key Features

* **Interoperability** - Single integration with NBBL enables access to all participating banks
* **Mobile-First Approach** - Authentication and authorization within bank's mobile app
* **Near-Real-Time Settlement** - Faster fund transfers between banks
* **No Amount Limit** - Process transactions of any size
* **Configurability** - Platform can be customized to meet specific business needs
* **Standardized Disputes** - Unified dispute management system
* **Settlement Framework** - Standardized settlement process similar to IMPS, BBPS, UPI

<Callout icon="📘" theme="info">
  **Only non-seamless integration supported**: PayU currently **supports PayU Hosted integration** or non-seamless integration. Support for **Merchant Hosted** integration or seamless integration is in progress and will be available shortly.
</Callout>

## Desktop Features

* **QR Code Generation**: Dynamic, secure QR codes for mobile app scanning
* **Browser Optimization**: Seamless redirect flows for desktop browsers
* **Multi-Bank Support**: Single integration for all Banking Connect participating banks
* **Visual Feedback**: Real-time transaction status updates on desktop interface

<Image align="center" border={false} src="https://files.readme.io/a7f7292beca283f7c0b234ec78fbd10e9d8c726db0ef3fb6f101f04dbab56f40-0.jpg" />

## Mobile Features

* **Intent Deep Linking**: Direct app-to-app payment flows
* **Native App Integration**: Seamless banking app interactions
* **Responsive Design**: Optimized checkout experience across mobile devices

<Image align="center" border={true} src="https://files.readme.io/9ca652247279c924a3dcd8b3784c02a7cb53e57afd8e5386b804d4e25cad2cfe-nbbl_mobile_intent_consolidate.png" className="border" />

## Cross-Platform Features

* **Device Synchronization**: Transaction continuity across desktop and mobile
* **Universal Compatibility**: Works with existing PayU integrations
* **Fallback Mechanisms**: Automatic switching between QR, intent, and redirect flows
* **Real-time Processing**: Instant status updates regardless of device platform

## Banks Supported

Currently, PayU supports the following banks for Banking Connect:

* HDFC Bank
* ICICI Bank
* Axis Bank

## Regulatory Compliance Requirements

* **RBI Guidelines**: Full adherence to KYC Master Direction requirements
* **PCI DSS Certification**: Mandatory for handling payment data across all platforms
* **Data Protection**: PII encryption and secure data transmission protocols
* **Cross-Platform Security**: Consistent security standards for desktop and mobile
