---
title: What is Tokenization?
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: What is Tokenization?
  description: >-
    Learn about tokenization, a secure method for protecting payment data by
    replacing sensitive card information with unique tokens. Discover how
    tokenization enhances payment security, complies with PCI DSS standards, and
    prevents fraud. Explore the benefits and implementation of tokenization in
    online payments with PayU.
  keywords:
    - Tokenization
    - Payment tokenization
    - Tokenization in payments
    - Card tokenization
    - Tokenization process
    - Secure payment methods
    - Tokenization technology
    - Payment security
    - Data protection in payments
    - PCI DSS compliance
  robots: index
next:
  description: ''
---
Tokenization protects sensitive data by creating an identifier that maps back to the sensitive data but does not have any intrinsic value. 

## RBI Guidelines

According to the RBI circular, you must be using tokenization to save card details on your website starting 1st January 2022. For more information, refer to the [Tokenisation – Card Transactions: Permitting Card-on-File Tokenisation (CoFT) Services](https://rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=12159) circular.

In a card context, it replaces the actual card number with a dummy reference ID.

## PayU’s interpretation of RBI guidelines

- Only Issuers & Payment Networks are allowed to store customer card data. ​
- Limited data can be stored by non-payment entities (Bank Name,  Last 4 digits of card)​
- Every token to be stored with customer consent (AFA)​
- Customers should be able to manage their details on business and Issuing bank platforms​
- Every token is unique to a user, card, and the merchant
- Existing data migration is not possible

## Who can Tokenize Cards?

As per the current RBI guidelines, tokens can be created with either the networks or the issuing bank. 

For example, Mr. John Doe has an HDFC VISA Signature credit card. This card can be tokenized by VISA (VTS or Visa Token Service) or by HDFC through its proprietary token service.  

PayU is working with both the networks and issuers to be able to provide tokenization to its merchants. 

## PayU Solution

PayU will provide both network tokens and issuer tokens for its merchants along with other suites of products to maintain and manage the vault services:

- **Network Tokens**: Network tokens are virtual payment cards created by the payment schemes (VISA, Mastercard), and they replace the original card in the digital space. This allows for several network tokens to be created per card, and they function in the same way as the original card when storing and transacting with them. 
- **Issuer Tokens**: Issuer tokens are virtual payment cards created by the card-issuing bank, and they replace the original card in the digital space. However, **these tokens are not understood by the network schemes**