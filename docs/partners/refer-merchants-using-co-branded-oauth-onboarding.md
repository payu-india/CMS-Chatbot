---
title: Refer Merchants using Co-Branded (OAuth) Onboarding
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Refer Merchants using Co-Branded or OAuth Onboarding
  description: >-
    Streamline your referral process with PayU's Co-Branded OAuth Onboarding.
    Our detailed guide helps you integrate and manage referral merchants
    efficiently, enhancing your partnership benefits. Learn how to use OAuth for
    secure and seamless referral onboarding with PayU.
  keywords:
    - PayU co-branded onboarding
    - OAuth referral onboarding PayU
    - Co-branded referral onboarding
    - PayU merchant referral OAuth
    - PayU co-branded OAuth integration
    - >-
      Referral onboarding PayU partner.PayU OAuth referral process.Partner
      portal co-branded onboarding
    - PayU referral merchant onboarding.Co-branded OAuth PayU referral
    - How to onboard referrals PayU
    - PayU partner OAuth integration
    - Seamless referral onboarding PayU
  robots: index
next:
  description: ''
---
When partners develop the GUIs for the onboarding of their merchants (while using PayU APIs for merchant onboarding), it consumes a few minutes to create a co-branded experience. The merchants have to share the key & Salt explicitly with partners. Co-Branded Onboarding (OAuth) allows the partners to provide a seamless co-branded onboarding journey for merchants powered by PayU, where the partners can customize the Look & Feel of the onboarding GUI without building the GUI from scratch. At its core, it is a simple but seamless onboarding product for partners who will redirect their users to PayU only to complete onboarding. 

## How OAuth helps partners?

OAuth allows the partners to provide a seamless co-branded onboarding journey for merchants powered by PayU, where the partners can customize the Look & Feel of the onboarding GUI without building the GUI from scratch. It is a simple but seamless onboarding product for a partner who will redirect their users to PayU only to complete onboarding.

## OAuth user journey

OAuth user journey is a PayU co-branded onboarding journey. The partner provides a sign-up or login link on their platform.

1. The user is directed to the PayU co-branded onboarding form using the sign-up or login link provided by the partner.
2. The partner can choose to send information related to the merchant and the capabilities in the URL.
3. Based on the configuration (default/custom) saved in the backend, the journey of the merchants will be customized. Merchants can either sign up or log in through this page.
   - If the merchant is signing up, thy will be taken to the onboarding journey only if it is pending. On submitting the information, the user will be taken to a _Consent_ page, where the user will be asked to allow access to the partner.
4. The Consent page will have the list of permission enabled. Upon acceptance, the merchant will be redirected back to the platform.
5. In the redirection URL, there will be an access code using which the partner can generate a token to use the APIs.

This solution is the fastest way to complete the onboarding of merchants. This will also save substantial engineering or operations efforts for the partner.

## Co-Branded onboarding flow

For example, Soylent Corp. has partnered with PayU and wants to onboard ABC LLP. merchants through the co-branded onboarding method.

[block:parameters]
{
  "data": {
    "h-0": "XYZ Partner",
    "h-1": "PayU",
    "h-2": "ABC Merchant",
    "0-0": "- Connects with PayU  \n- Selects co-branded onboarding  \n- Receives the web link of the PayU hosted onboarding webpage  \n- Shares the link with Merchant to start onboarding",
    "0-1": "- Creates Partner Profile and builds Onboarding Platform on behalf of Partner  \n- Shares the Webpage link with XYZ along with the Create Merchant API V3 capabilities  \n- Provides service to the merchant on behalf of partner",
    "0-2": "- Initiates onboarding process"
  },
  "cols": 3,
  "rows": 1,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## APIs used in Co-Branded onboarding

The following APIs used in Co-branded onboarding:

- [Validate Auth Code and Client](ref:validate_authcode_and_client_api)
- [Get Merchant Credentials API](ref:get_merchant_credentials_api)