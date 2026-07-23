---
title: APIs used in International Payments Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in International Payments Integration
  robots: index
---
<Table>
  <thead>
    <tr>
      <th>
        API
      </th>

      <th>
        Purpose
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ### Card Check
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Check is Domestic API](ref:check_is_domestic_api)
      </td>

      <td>
        Validate whether the customer's card BIN is domestic or international before initiating payment, to avoid failures on international-only flows.
      </td>
    </tr>

    <tr>
      <td>
        ### \_payment to Collect Payment
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
      </td>

      <td>
        Initiate an international card payment on the PayU-hosted page; PayU displays DCC conversion when the customer enters an international card.
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – Merchant Hosted Checkout](ref:_payment_merchant_hosted)
      </td>

      <td>
        Submit the card payment request with international payment parameters (including optional `transactionCurrency` for MCC merchants).
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
