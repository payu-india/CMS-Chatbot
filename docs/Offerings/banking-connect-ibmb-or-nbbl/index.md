---
title: Banking Connect - IBMB or NBBL
deprecated: false
hidden: true
metadata:
  robots: index
---
Banking Connect is PayU's interoperable platform that modernizes net banking transactions across India. This integration allows PayU merchants to offer **Net Banking 2.0** - a next-generation payment experience that replaces traditional redirection-based flows with QR codes and mobile app intent-based payments. The platform addresses traditional net banking challenges by providing centralized integration, reducing failure points, and enabling real-time settlement capabilities.

## How It Works?

* **Certificate Exchange**: Establish public-key exchange for encrypted communication
* **Health Check**: Verify Banking Connect endpoint availability every 5 seconds before transactions
* **Merchant Onboarding**: Bulk upload or API-based merchant registration with Banking Connect

## Features

### Desktop

* **QR Code Generation**: Dynamic, secure QR codes for mobile app scanning
* **Browser Optimization**: Seamless redirect flows for desktop browsers
* **Multi-Bank Support**: Single integration for all Banking Connect participating banks
* **Visual Feedback**: Real-time transaction status updates on desktop interface

<Image align="center" border={false} src="https://files.readme.io/a7f7292beca283f7c0b234ec78fbd10e9d8c726db0ef3fb6f101f04dbab56f40-0.jpg" />

### Mobile

* **Intent Deep Linking**: Direct app-to-app payment flows
* **Mobile-Optimized QR**: Enhanced QR display and scanning experience
* **Native App Integration**: Seamless banking app interactions
* **Responsive Design**: Optimized checkout experience across mobile devices

<Image align="center" border={false} src="https://files.readme.io/7fd70ef02b0bd532680ff69b8a4870f1cd92a96d2c61c2bf8e510e185afaf476-PayU_Hosted_Mobile_QR_Step3.png" />

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

* **Intent URL Handling**: Deep linking configuration for banking apps
* **Mobile QR Optimization**: Responsive QR code display
* **App Detection**: Automatic banking app availability checking
* **Mobile Callbacks**: Handle app-to-browser return flows

## Regulatory Compliance Requirements

* **RBI Guidelines**: Full adherence to KYC Master Direction requirements
* **PCI DSS Certification**: Mandatory for handling payment data across all platforms
* **Data Protection**: PII encryption and secure data transmission protocols
* **Cross-Platform Security**: Consistent security standards for desktop and mobile
