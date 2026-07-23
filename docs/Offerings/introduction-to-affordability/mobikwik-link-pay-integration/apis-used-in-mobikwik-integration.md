---
title: APIs used Integration
deprecated: false
hidden: false
metadata:
  title: APIs used in Mobikwik Integration
  robots: index
---
<Table>
  <thead>
    <tr>
      <th>
        API&#x20;
      </th>

      <th>
        Purpose
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ### Check Balance and Pay
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Check User Balance and Link Status API](doc:steps-to-integrate-mobikwik-link-pay#step-1-check-user-balance-and-link-status) (`/userbalance`)
      </td>

      <td>
        Check whether the customer's Mobikwik wallet is linked and retrieve the available balance before initiating payment.
      </td>
    </tr>

    <tr>
      <td>
        [Payment Initiation API](doc:steps-to-integrate-mobikwik-link-pay#step-2-payment-initiation-api) (`/v2/payments`)
      </td>

      <td>
        Initiate a Mobikwik Link & Pay transaction on PayU; automatically routes linked users to auto-debit and unlinked users to the wallet-linking flow.
      </td>
    </tr>

    <tr>
      <td>
        [Token Generate API – Mobikwik](ref:token-generate-api-mobikwik) (`/tokengenerate`)
      </td>

      <td>
        Submit the OTP and generate a wallet token for linked repeat transactions.
      </td>
    </tr>

    <tr>
      <td>
        ### Manage Wallet
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Add Money to Wallet And Debit API – Mobikwik](ref:add-money-to-wallet-and-debit-api-mobikwik)
      </td>

      <td>
        Load money into the wallet and debit in a single flow when the wallet balance is insufficient.
      </td>
    </tr>

    <tr>
      <td>
        [Check Status API – Mobikwik](ref:check-status-api-mobikwik)
      </td>

      <td>
        Verify whether the payment is complete
      </td>
    </tr>

    <tr>
      <td>
        ### Verify the Payment
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Verify Payment API](ref:verify_payment_api)
      </td>

      <td>
        Server-side reconciliation of transaction status after payment.
      </td>
    </tr>
  </tbody>
</Table>

<br />