---
title: Introduction
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: PayU Partner Integration Introduction
  description: >-
    This page provides overview of various types of partners can join the
    program, including platform partners that provide ready-to-use eCommerce
    websites and software solutions, as well as resellers who aim to accelerate
    their businesses by earning incentives through their clients. The page also
    provides information on the methods of onboarding merchants, including
    referral through PayU APIs, co-branded onboarding, referral links, and
    custom onboarding journeys.


    Overall, the PayU Partner Program Overview page serves as a comprehensive
    guide for potential partners, outlining the benefits, types of partners, and
    methods of onboarding merchants, empowering them to become successful
    partners with PayU.
  keywords:
    - PayU Partner Integration
    - PayU India Partner Program
    - Payment Gateway Partner Integration
    - Partner Program Overview
    - PayU Partner Onboarding
    - PayU Partnership Benefits
    - PayU Partner Integration
    - PayU India Partner Program
    - Payment Gateway Partner Integration
    - Partner Program Overview
    - PayU Partner Onboarding
    - PayU Partner Prerequisites
    - Who Can Become Partner
    - PayU Reseller Introduction
    - PayU Partner Platform Integration
    - Partnering with PayU
    - PayU referral program
  robots: index
next:
  description: ''
---
A partner is a person you refer to PayU and earn incentives. The partner can be resellers or franchisees who can earn incentives for being associated with your business by referral or being part of your platform by offering PayU Payment Platform to the referrals.

PayU Partner Program is a way to grow your business exponentially, raising your profits. PayU’s reliable and secure payment solutions help you with the best customer service efforts. Connect your merchants with PayU with our easy and simple integration methods. By joining this program, you can focus more on business goals to enrich the product experiences and less on maintaining payment systems. To get started, you need to register as a merchant with PayU. For more information, refer to [Register a Partner Account on PayU website](doc:onboard-merchants-manually#step-1-register-a-partner-account).

Onboard merchants, collect payments, and manage refunds — all from your own platform.

## Advantages

- Quick and easy integration
- Refer merchants and get rewarded
- Easy Account reconciliation
- Real-time merchant onboarding status updates
- Onboard merchants quickly using Partner Partner Integration APIs
- Onboard merchants and validate KYC automatically on the Partner Portal
- Customize Partner Portal with OAuth and onboard merchants with a branded portal.

## Who can become a partner?

PayU welcomes any small- or large-scale enterprise into their partner program. The following list demonstrates LOBs that have partnered with PayU:

- Web Designers and Developers
- Digital Service Providers
- Web Hosting Services
- Freelancers & Small-scale Businesses
- Accelerator Firms
- E-commerce Businesses

## Types of partner

- **Platform Partner**: Companies who are providing ready-to-use eCommerce websites, software solutions for retailers, and accountants, or restaurants, partnering with PayU helps you create new revenue streams and scale internationally. For example, Shopify, Zoho, ClearTax, etc.
- **Resellers:** Resellers are freelancers/entrepreneurs looking to accelerate their business by earning incentives through their clients.

After you onboard the merchants, they can start collecting payments from their customers. For more information, refer to [API Reference > Partner Payments Integration.](doc:partner-payments-integration)

## How it works

You integrate with PayU as a partner to bring merchants onto our payment platform. Depending on your needs, you can share a simple referral link or run the entire onboarding journey through APIs.

PayU handles verification (KYC, CKYC, VKYC), compliance, and activation. You collect merchant details, call our APIs, and receive status updates via webhooks.

```mermaid
flowchart LR
    A[Your Platform] -->|API| B[PayU]
    B --> C[KYC Registries]
    B --> D[E-Sign]
    B --> E[Banking Partners]
    B -.->|Webhook| A
    
    style B fill:#e1f5ff
    style A fill:#fff4e1

```

## Choose your integration

The following table helps you how to choose the method for onboarding partners. For detailed information, refer to [Which Partner Integration Method to Choose?.](doc:which-partner-integration-to-choose)

|                                     | [API](doc:apis-used-in-partner-integration) | [Partner Portal](docs:onboard-merchants-manually) | [Co-Branded OAuth](doc:refer-merchants-using-co-branded-oauth-onboarding) | [Referral Link](docs:refer-merchants-using-referral-links) |
| ----------------------------------- | ------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------- |
| **You build UI**                    | Yes                                         | No                                                | No                                                                        | No                                                         |
| **Brand control**                   | Full                                        | None                                              | Your logo + colors                                                        | None                                                       |
| **Technical effort**                | High                                        | None                                              | Low                                                                       | None                                                       |
| **Merchant stays on your platform** | Yes                                         | No                                                | No                                                                        | No                                                         |
| **Best for**                        | Large platforms                             | Manual onboarding                                 | Mid-size platforms                                                        | Individual resellers                                       |

If you need merchants to stay in your platform with an end-to-end controlled experience, use **API integration**. For a quick start with your branding, use **Co-Branded OAuth**.

## Next Steps

In this part of the document, the following sections provide the steps to integrate using various integration methods:

- [Quick start — five API calls](doc:quick-start-partner-integration)
- [API reference](doc:partner-api-authentication) (auth, onboarding, KYC, payments, webhooks)
- [Errors and troubleshooting](doc:errors-partner-integration)
