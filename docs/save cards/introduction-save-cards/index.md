---
title: Introduction
excerpt: >-
  PayU Vault APIs allow users to store multiple credit card or debit card
  details on PayU Vault (Cloud) easily and safely. PayU Vault stores the card
  details and provides access to you (merchant) when your customer provides
  his/her user credentials accompanied with or without a card token.
deprecated: false
hidden: true
metadata:
  title: Save Cards Introduction
  description: >-
    Learn how to use PayU’s Save Cards feature to enable your customers to
    securely store their card details and make faster payments on your website.
    Find out how to integrate the Save Cards API, manage tokens, and customize
    the user experience.
  keywords:
    - Tokenizing Card with PayU India Introduction
    - Save Cards Integration with PayU Introduction
    - PayU India card saving Introduction
    - Saving card with PayU Introduction
    - Save card details PayU integration Introduction
    - Tokenization of cards Introduction
    - PayU India save card functionality Introduction
    - Save cards PayU integration Introduction
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: what-is-tokenization
      title: What is Tokenization?
    - type: basic
      slug: which-model-you-should-choose
      title: Which Model you Should Choose for Tokenization?
---
Your users save invaluable time when they use their cards that are stored on PayU Vault instead of entering the card details when they make payments safely on your website. Customers can use saved cards on all the merchant websites where they support PayU Vault.

Users can update or delete their card details on the PayU vault when required. You may need to enable this on their website.

The workflow for users with PayU Vault are:

1. Customer visit the merchant’s website, adds items to the cart, or utilize the merchant’s services, and then enter the card details.
2. Customer provides consent to the merchant and the merchant [saves the card details](doc:zero-code-change-for-vault-integration-model-2#first-time-payment-workflow) on PayU Vault
3. Customer visits the same merchant and uses the saved card details to proceed with the transaction.
4. Customer provides his/her user credentials, the merchant [retrieves the card details](ref:get_user_cards_api) and the user enters the CVV or 3DBC number to complete payment.

> **Note**: While CVV is not mandatory from the network perspective, some banks may impose the necessity of the same for doing transactions with a saved card. Also, if the bank does not mandate the CVV but the merchant captures the same, CVV will be verified. It is recommended that for the banks where CVV is not required, merchants should not ask for the same

5. User can update or  delete the card details when required.

> 📘 Note:
>
> You need to ensure that you have filled the “[Self-Assessment Questionnaire A-EP and Attestation of Compliance](https://www.pcisecuritystandards.org/documents/PCI-DSS-v3_2-SAQ-A_EP-rev1_1.pdf)” form from PCI, which is mandatory for all entities seeking to store, process, and transmit cardholder data.
