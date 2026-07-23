---
title: APIs used in BNPL Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in BNPL Integration
  robots: index
---
<br />

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
        ### Eligibility Check
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Get EMI Checkout Details API](ref:get-emi-checkout-details-api)
      </td>

      <td>
        Check BNPL Link & Pay eligibility and retrieve checkout details for supported lenders.
      </td>
    </tr>

    <tr>
      <td>
        [Get Checkout Details API](ref:get_checkout_details)
      </td>

      <td>
        Check customer BNPL eligibility before initiating payment on merchant-hosted checkout.
      </td>
    </tr>

    <tr>
      <td>
        ### \_payment API to Collect Payment
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – BNPL (Merchant Hosted Checkout)](ref:_payment_merchant_hosted_bnpl)
      </td>

      <td>
        Submit a BNPL payment request with `pg=BNPL` and the provider `bankcode` on merchant-hosted checkout.
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – BNPL Link & Pay](ref:collect-payment-api-bnpl-link-pay)
      </td>

      <td>
        Initiate BNPL Link & Pay transactions, including one-click repeat-user flows after wallet linking.
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – S2S Link and Pay](ref:_payment_s2s_link_pay)
      </td>

      <td>
        Server-to-server payment initiation for BNPL Link & Pay with OTP-based authentication.
      </td>
    </tr>

    <tr>
      <td>
        ### Submit OTP for Link & Pay
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Submit OTP API](ref:submit-otp-to-payu)
      </td>

      <td>
        Submit the customer OTP along with the reference ID from the `_payment` response to complete BNPL Link & Pay authentication.
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