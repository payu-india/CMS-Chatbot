---
title: APIs used in Offers Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Offers Integration
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
        ### \_payment API to Collect Payment
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
      </td>

      <td>
        Initiate a PayU-hosted checkout payment with offer parameters for instant discount, cashback, or SKU-based offers.
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – Merchant Hosted Checkout](ref:_payment_merchant_hosted)
      </td>

      <td>
        Submit the payment request with offer parameters (`offer_key`, `api_version`, `user_token`, and related fields) for merchant-hosted checkout.
      </td>
    </tr>

    <tr>
      <td>
        ### Eligibility and Offer APIs
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Fetch Offers API](ref:fetch-offers-api)
      </td>

      <td>
        Retrieve applicable offers for a transaction context to display on checkout, cart, product detail, or offers pages.
      </td>
    </tr>

    <tr>
      <td>
        [EMI Calculator API](ref:emi-calculator-api)
      </td>

      <td>
        Return EMI tenure plans with monthly instalments, interest rates, and applicable EMI offers when the customer selects EMI.
      </td>
    </tr>

    <tr>
      <td>
        [Validate Offer API](ref:validate-offer-api)
      </td>

      <td>
        Confirm that the selected offer applies to the transaction before initiating payment.
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