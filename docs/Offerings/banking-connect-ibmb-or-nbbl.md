---
title: Banking Connect - IBMB or NBBL
deprecated: false
hidden: false
metadata:
  robots: index
---
Banking Connect is PayU's interoperable platform that modernizes net banking transactions across India. This integration allows PayU merchants to offer **Net Banking 2.0** - a next-generation payment experience that replaces traditional redirection-based flows with QR codes and mobile app intent-based payments. The platform addresses traditional net banking challenges by providing centralized integration, reducing failure points, and enabling real-time settlement capabilities.

## How It Works?

* **Certificate Exchange**: Establish public-key exchange for encrypted communication
* **Health Check**: Verify Banking Connect endpoint availability every 5 seconds before transactions
* **Merchant Onboarding**: Bulk upload or API-based merchant registration with Banking Connect

## Customer Journey by Platform

### &#x20;Desktop 

#### QR Flow

1. Customer selects net banking on PayU Hosted Checkout (desktop)
2. PayU generates dynamic QR code via Banking Connect
3. Customer scans QR with their mobile banking app
4. Banking app decodes transaction details and initiates authentication
5. Payment completion with OTP/biometric verification on mobile
6. Real-time status update displayed on desktop merchant page

#### Redirect Flow

1. Customer chooses net banking payment option on desktop
2. PayU redirects to Banking Connect-managed bank pages
3. Customer login with banking credentials on desktop browser
4. Transaction completion on bank website interface
5. Automatic redirect back to merchant confirmation page
6. Transaction status displayed on desktop

### Mobile

#### QR Flow

1. Customer accesses PayU Hosted Checkout on mobile browser
2. Banking Connect generates QR code optimized for mobile display
3. Customer switches to banking app to scan QR
4. In-app transaction processing and authentication
5. Return to mobile browser with completion status
6. Mobile-optimized confirmation page display

##### App Intent Flow

1. Customer selects net banking on mobile browser/app
2. PayU creates intent URL for selected bank via Banking Connect
3. Automatic deep linking to banking app (Android/iOS)
4. Native in-app authentication and payment authorization
5. Instant callback to PayU mobile interface
6. Seamless transaction confirmation

#### Mobile Desktop Compatibility

* Cross-platform session management between mobile and desktop
* QR codes generated on desktop can be scanned by mobile app
* Transaction status synchronization across device  
* Unified merchant dashboard for multi-device transactions

## Features

### Desktop

* **QR Code Generation**: Dynamic, secure QR codes for mobile app scanning
* **Browser Optimization**: Seamless redirect flows for desktop browsers
* **Multi-Bank Support**: Single integration for all Banking Connect participating banks
* **Visual Feedback**: Real-time transaction status updates on desktop interface

### Mobile

* **Intent Deep Linking**: Direct app-to-app payment flows
* **Mobile-Optimized QR**: Enhanced QR display and scanning experience
* **Native App Integration**: Seamless banking app interactions
* **Responsive Design**: Optimized checkout experience across mobile devices

### Cross-Platform Features

* **Device Synchronization**: Transaction continuity across desktop and mobile
* **Universal Compatibility**: Works with existing PayU integrations
* **Fallback Mechanisms**: Automatic switching between QR, intent, and redirect flows
* **Real-time Processing**: Instant status updates regardless of device platform

## Benefits by Use Case

### Desktop Users

* **Enhanced Security**: Mobile app-based authentication for desktop transactions
* **Convenience**: No need to remember banking credentials on shared computers
* **Speed**: QR scanning faster than traditional login processes
* **Familiarity**: Maintain desktop browsing with mobile authentication

### Mobile Users

* **Native Experience**: Direct banking app integration without browser switching
* **One-Touch Payments**: Intent flows reduce friction and completion time
* **Biometric Authentication**: Leverage mobile security features
* **Optimized Interface**: Mobile-first design for better user experience

### Merchants

* **Higher Success Rates**: Multi-flow support increases payment completion
* **Unified Integration**: Single API covers all device types and flow options
* **Reduced Development**: Minimal changes to existing PayU implementations
* **Better Analytics**: Device-specific transaction tracking and optimization

### Cross-Platform Benefits

* **Flexibility**: Customers can start on one device and complete on another
* **Broader Reach**: Support for all device types and user preference
* **Consistent Branding**: Unified PayU experience across platforms
* **Future-Ready**: Scalable architecture for emerging payment methods

## Implementation by Platform

### Desktop Integration

* **QR Display**: Implement QR code rendering in checkout interface
* **Redirect Handling**: Configure Banking Connect redirect URLs
* **Status Polling**: Real-time transaction status checking
* **Error Handling**: Fallback options for QR timeout or scan failures

### Mobile Integration

*  **Intent URL Handling**: Deep linking configuration for banking apps
* **Mobile QR Optimization**: Responsive QR code display
* **App Detection**: Automatic banking app availability checking
* **Mobile Callbacks**: Handle app-to-browser return flows

## Regulatory Compliance Requirements 

* **RBI Guidelines**: Full adherence to KYC Master Direction requirements
* **PCI DSS Certification**: Mandatory for handling payment data across all platforms
* **Data Protection**: PII encryption and secure data transmission protocols
* **Cross-Platform Security**: Consistent security standards for desktop and mobile
