---
title: APIs used in Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Closed-Loop Wallet integration
  robots: index
---
<br />

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

<Callout icon="📘" theme="info">
  **Note**: To unload your wallet, refer to [Seamless Debit Integration - CLW](https://docs.payu.in/docs/seamless-debit-integration-clw) or [PayU Hosted Check-out Integration - CLW](https://docs.payu.in/docs/pay-hosted-checkout-merchant-integration-merchant-wallet) based on the integration.
</Callout>

<br />