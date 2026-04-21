---
title: UPI Collect Disablement Information
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: UPI Collect Disablement Information
excerpt: 'Important information regarding the discontinuation of UPI Collect flow as per NPCI guidelines effective 28 February 2026.'
deprecated: false
hidden: false
metadata:
  title: UPI Collect Disablement Information
  description: >-
    NPCI has announced the sunset of UPI Collect flow effective 28 February
    2026. Learn about the key changes, exemptions, and required actions for
    PayU merchants to migrate to UPI Intent or UPI QR flows.
  keywords:
    - UPI Collect
    - UPI Collect Disablement
    - NPCI Mandate
    - UPI Intent
    - UPI QR
    - UPI Migration
    - VPA discontinuation
  robots: index
next:
  description: ''
---

NPCI has announced that the UPI Collect flow will be sunset effective **28 February 2026**. After this date, customers will no longer be able to initiate payments or register UPI mandates by manually entering a Virtual Payment Address (VPA), UPI ID, or mobile number.

## Key Changes

* Manual entry of VPA/UPI ID or mobile number for payments and mandate registration will be discontinued.
* All payment and mandate initiation must transition to alternative UPI flows, such as **UPI Intent** or **UPI QR**.

## Exemptions

UPI Collect will remain available only for the following specific use cases:

| Use Case                          | Description                                                                  |
| --------------------------------- | ---------------------------------------------------------------------------- |
| **MCC 6012 & 6211**               | IPO and secondary market transactions.                                       |
| **iOS Mobile App and Mobile Web** | Transactions initiated via iOS mobile applications and mobile web platforms. |
| **UPI Mandates**                  | Only for executing, modifying, or revoking existing mandates.                |
| **PACB Businesses**               | Cross-border and international payments.                                     |

## Action Required

### For New PayU Merchants

Integrate UPI payments using the **UPI Intent flow** and **UPI QR flow**. For more information, refer to the [UPI Intent Server-to-Server Integration](doc:upi-intent-server-to-server)

### For Existing PayU Users

Merchants not covered by the above exemptions must migrate their integration to **UPI Intent** or **UPI QR code** to ensure continued acceptance of UPI payments. For more information, refer to the [UPI Intent Server-to-Server Integration](doc:upi-intent-server-to-server)
