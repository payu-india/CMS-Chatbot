---
title: EMI
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: EMI Integration with PayU APIs
  description: >-
    Explore the process of collecting payments through EMI options using PayU's
    Merchant Hosted Checkout integration. Discover how to determine customer
    eligibility, calculate EMI details, and initiate transactions with EMI
    conversion using EMI APIs. This guide covers various EMI integration flows,
    including debit cards, credit cards, cardless EMI, and native OTP flow.
  keywords:
    - PayU EMI API Integration
    - PayU EMI Conversion Process
  robots: index
next:
  description: ''
---
Equated Monthly Instalment (EMI) refers to the fixed amount of money you pay to a bank or a lender every month as part of the repayment of an outstanding loan. EMI as a payment option gives your customers the freedom and affordability to purchase expensive items without having to deal with banks or NBFCs as intermediaries.

<Callout icon="👍" theme="okay">
  ### Before you begin:

  Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

The following sections describe the procedure to integrate cards with EMI:

- [PayU Hosted Checkout Integration](doc:collect-payments-using-payu-hosted-checkout-integration-emi)
- Merchant Hosted Checkout Integration
  - [Debit Card](doc:collect-payments-with-emi-using-debit-card)
  - [Credit Card](doc:collect-payments-with-emi-using-credit-card)
  - [Cardless EMI](doc:collect-payments-with-cardless-emi-using-merchant-hosted-checkout)
  - [Native OTP Flow Integration](doc:native-otp-flow-integration)
    - [Debit Card](/docs/native-otp-flow-integration#collect-payments-with-debit-card)
    - [Cardless EMI](/docs/native-otp-flow-integration#collect-payments-with-cardless-emi)

<Accordion title="APIs mentioned without a linked reference page" icon="fa-info-circle">
  | Mention | Context | Purpose |
  | --- | --- | --- |
  | **BIN API** | Parameter tables in Debit Card, Credit Card, and Cardless EMI integration guides | Validate CVV length and rules for the card type (for example, 3-digit vs 4-digit for AMEX). No `ref:` link is provided on those pages. |
</Accordion>

<Accordion title="Verification methods (not standalone payment APIs)" icon="fa-check-circle">
  | Name | Purpose |
  | --- | --- |
  | [Webhooks](doc:webhooks) | Alternative server-to-server verification of payment status. **Used in:** [Production Checklist](doc:integration-checklist-emi) and the shared `<Verify_Payment_Tabs />` component on integration pages. |
</Accordion>

## Supported Banks or Institutions

PayU supports EMI for the following banks or institutions with debit cards, credit cards, cardless EMI, and No-Cost EMI:

<Accordion title="Credit Cards" icon="fa-credit-card">
  * American Express
  * HDFC Bank
  * ICICI Bank
  * Axis Bank
  * Citibank
  * State Bank of India
  * Kotak
  * RBL Bank
  * IndusInd Bank
  * Standard Chartered Bank
  * YES Bank
  * HSBC Bank
  * One Card
  * AU Small Finance Bank
  * Bank of Baroda
  * IDBI Bank
  * IDFC First Bank
</Accordion>

<Accordion title="Debit Cards" icon="fa-credit-card">
  * State Bank of India
  * HDFC Bank
  * ICICI Bank
  * Axis Bank
  * Kotak Mahindra Bank
  * Federal Bank
  * Bank of Baroda
</Accordion>

<Accordion title="Cardless" icon="fa-mobile">
  * Bajaj Finserve
  * Liquiloan
  * Zest Money
  * KreditBee
</Accordion>

<br />

## APIs used for Integration

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
