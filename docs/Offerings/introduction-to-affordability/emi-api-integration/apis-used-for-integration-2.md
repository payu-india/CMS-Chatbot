---
title: APIs used for Integration
deprecated: false
hidden: false
metadata:
  title: APIs used for EMI Integration
  robots: index
---
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
        ### \_payment API for Collect Payment
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
      </td>

      <td>
        Initiate an EMI transaction on the PayU-hosted payment page (non-seamless checkout). Customer selects EMI, enters card details, and completes OTP on PayU’s page.
      </td>
    </tr>

    <tr>
      <td>
        ### Eligibility Check APIs
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Get Checkout Details API](ref:get_checkout_details)
      </td>

      <td>
        Check customer eligibility before payment — by mobile number for debit-card pre-EMI and cardless EMI.
      </td>
    </tr>

    <tr>
      <td>
        [Get EMI According to Interest API](ref:get_emi_according_to_interest_api)
      </td>

      <td>
        Calculate EMI details — interest rate, monthly instalment, processing fee, No-Cost EMI, tenure, and the corresponding `bankcode` for the chosen plan.
      </td>
    </tr>

    <tr>
      <td>
        [Eligible BINs for EMI API v1.0](ref:eligiblebinsforemi)
      </td>

      <td>
        Check credit-card EMI eligibility from the card BIN; returns issuing bank and minimum eligible amount.
      </td>
    </tr>

    <tr>
      <td>
        [Eligible BINs for EMI API v2.0](ref:eligible-bins-for-emi-v20)
      </td>

      <td>
        Check cardless EMI eligibility from card or customer information in the S2S flow.
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
