---
title: How Server-to-Server Integration Works
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
PayU Server-to-Server architectures communicate through direct backend REST API calls, returning cryptographic tokens, ACS challenge payloads, or deep-link URIs depending on the selected payment method.

***

## 1. Cards S2S Flow (Classic & Decoupled)

```mermaid
sequenceDiagram
    autonumber
    actor Customer
    participant MerchantApp as Merchant App / Frontend
    participant MerchantServer as Merchant Backend
    participant PayU as PayU Payment Gateway
    participant BankACS as Bank ACS / 3DS Server

    Customer->>MerchantApp: Enter Card Details (PAN, Expiry, CVV)
    MerchantApp->>MerchantServer: Submit Order Details
    MerchantServer->>MerchantServer: Compute SHA-512 Hash
    MerchantServer->>PayU: POST /_payment (S2S Payload)
    
    alt 3DS Challenge Flow
        PayU-->>MerchantServer: JSON Response with base64 acsTemplate
        MerchantServer-->>MerchantApp: Return Decoded ACS HTML Form
        MerchantApp->>BankACS: Auto-submit ACS Form / Render OTP Screen
        Customer->>BankACS: Enter OTP & Authorize
        BankACS->>PayU: 3DS Authentication Callback
    else 3DS Frictionless Flow
        PayU->>BankACS: Direct Frictionless Authorization
    end
    
    PayU->>MerchantServer: S2S Webhook / Notification Callback
    PayU-->>MerchantApp: Redirect to surl / furl
    MerchantServer->>PayU: POST verify_payment (Double Verification)
    MerchantServer-->>Customer: Display Payment Success / Failure
```

***

## 2. UPI Intent S2S Flow

```mermaid
sequenceDiagram
    autonumber
    actor Customer
    participant MerchantApp as Merchant Mobile App
    participant MerchantServer as Merchant Backend
    participant PayU as PayU Gateway
    participant UPIApp as UPI App (GPay/PhonePe/Paytm)

    Customer->>MerchantApp: Selects UPI Payment Method
    MerchantApp->>MerchantServer: Request Intent Creation
    MerchantServer->>PayU: POST /_payment (pg=UPI, bankcode=INTENT, txn_s2s_flow=4)
    PayU-->>MerchantServer: Return JSON containing intent_uri, deep_links, qr_data
    MerchantServer-->>MerchantApp: Pass Intent URI
    MerchantApp->>UPIApp: Invoke UPI Deep Link via Intent
    Customer->>UPIApp: Authorize with UPI MPIN
    UPIApp->>PayU: Transaction Settled via NPCI
    PayU->>MerchantServer: Webhook / S2S Notification Callback
    MerchantServer-->>Customer: Display Order Confirmation
```
