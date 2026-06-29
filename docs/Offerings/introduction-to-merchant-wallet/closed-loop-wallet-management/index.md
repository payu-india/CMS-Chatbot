---
title: Closed-Loop Wallets
deprecated: false
hidden: false
metadata:
  title: Closed-Loop Wallet Management
  keywords:
    - Closed-Loop Wallet Management
    - clw
    - closed loop wallet management
  robots: index
---
**Closed-Loop Wallet API suite** enables businesses to implement merchant-specific digital wallet solutions that can only be used within the issuing merchant's website or mobile application. This prepaid payment instrument provides a controlled, branded payment experience that drives customer loyalty and repeat engagement.

Unlike semi-closed-loop wallets, closed-loop wallets are **not regulated by RBI** and operate within the merchant's ecosystem, making them ideal for businesses looking to create a seamless, integrated payment experience for their customers.

## Key Highlights

- Merchant-specific wallet usage only
- No RBI regulatory requirements
- Enhanced customer retention through integrated experience
- Cashback and loyalty program integration

## Implementation Benefits

- **Easy to Integrate:** Simplified implementation process
- **Merchant Control:** Complete control over wallet features and experience
- **Customer Retention:** Enhanced loyalty through integrated payment experience
- **Flexible Features:** Support for cashback, promotions, and loyalty programs

## Key Features

### Merchant-Specific Usage

The wallet can only be used on the issuing merchant's website or mobile application, ensuring complete control over the customer payment experience.

### One-Click Payments

- Instant payment processing using stored wallet balance
- Pre-fetched wallet balance display during checkout
- Seamless transaction completion without redirections

### Load & Pay Functionality

- On-the-fly wallet loading during checkout
- Flexible payment options when wallet balance is insufficient
- Immediate transaction processing after successful loading

### No Cash Withdrawal

Cash withdrawal is not permitted, ensuring funds remain within the merchant ecosystem for future purchases.

## Advantages

- **Enhanced Customer Retention**: Closed-loop wallets keep customers within your ecosystem, encouraging repeat purchases and building long-term customer relationships through integrated loyalty programs
- **Simplified Compliance**: Since closed-loop wallets are not regulated by RBI, businesses can implement wallet solutions without complex regulatory compliance requirements.
- **Complete Control**: Merchants have full control over the wallet experience, including branding, features, and customer journey optimization.
- **Increased Transaction Success**: With funds pre-loaded in the wallet, transaction success rates improve significantly compared to traditional payment methods.
- **No Limit**: No restriction on limit of wallet balance or usage of wallet supporting high ticket size transactions

### Load & Pay Journey

For Transaction Amount > Wallet Balance:

1. **Insufficient Balance Detection**
   System identifies when wallet balance is insufficient for the transaction

2. **Add Amount Option**
   Customer can choose to add the required amount to complete the purchase

3. **Payment Instrument Selection**
   Customer selects preferred payment method for wallet loading

4. **Transaction Completion**
   Wallet is loaded and original transaction is processed immediately

This part of the document includes the various Closed-Loop integration based on use cases:

- [Seamless Debit Integration](https://docs.payu.in/docs/seamless-debit-integration-clw)
- [PayU Hosted Check-out Integration](https://docs.payu.in/docs/pay-hosted-checkout-merchant-integration-merchant-wallet)

## APIs used in Closed-Loop Wallet integration

<Table>
  <thead>
    <tr>
      <th>
        API name
      </th>

      <th>
        Purpose
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ### Customer Management
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Register Customer API](ref:register-customer-api)
      </td>

      <td>
        Onboard a customer and create a closed-loop wallet account.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Retrieve Customer Record API](ref:retrieve-customer-record-api-1)
      </td>

      <td>
        Fetch customer details and wallet balance before debit or load operations.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Update Profile API – Closed Loop](ref:update-profile-api-closed-loop)
      </td>

      <td>
        Update customer profile details for a closed-loop wallet.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        ### Load & Unload Amount
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [PG Load API](ref:pg-load-api)
      </td>

      <td>
        Initiate a wallet top-up through the payment gateway.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [PG Load Enquiry API](ref:pg-load-enquiry-api)
      </td>

      <td>
        Check the status of a PG Load transaction during the top-up journey.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Load API – Closed Loop Wallet](ref:load-api-closed-loop-wallet)
      </td>

      <td>
        Credit the wallet after a successful payment gateway transaction.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Check Status API – CLW](ref:check-status-api-clw)
      </td>

      <td>
        Check the status of a load transaction in the top-up journey.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        ### Debit using \_payment API
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Seamless Debit Transaction API](ref:collect-payment-api-card-seamless)
      </td>

      <td>
        Debit the wallet instantly via server-to-server `_payment` without user redirection.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Non-Seamless Debit Transaction API](ref:non-seamless-debit-transaction-api)
      </td>

      <td>
        Debit the wallet via PayU Hosted Checkout with user authorization on the payment page.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Seamless Debit Enquiry API](ref:seamless-debit-enquiry-api)
      </td>

      <td>
        Check the status of a seamless debit transaction.
      </td>
    </tr>

    <tr>
      <td>
        [Load and Pay Transaction API](ref:load-and-pay-transaction-api)
      </td>

      <td>
        Load funds and debit the wallet in a single unified API call when balance is insufficient.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
      </td>

      <td>
        Redirect customers to PayU Hosted Checkout for wallet debit or load-and-pay flows.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        ### &#x20;Enquiry APIs
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Statement Inquiry API – CLW](ref:statement-inquiry-api-clw)
      </td>

      <td>
        Fetch wallet transaction history for a date range.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Change Wallet Status API](ref:change-wallet-status-api)
      </td>

      <td>
        Change the wallet status for a customer account.&#x20;
      </td>
    </tr>

    <tr>
      <td>
        [Verify Payment API](ref:verify_payment_api)
      </td>

      <td>
        Server-side reconciliation after wallet load or payment gateway transactions.&#x20;
      </td>
    </tr>
  </tbody>
</Table>

<br />
