---
title: APIs used for Integration
excerpt: ''
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used for Cross-Border Import Integration
  description: ''
  robots: index
next:
  description: ''
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
        ### \_payment to Collect Payment
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [PayU Hosted Checkout – CB](ref:_payment_cross-border_payu_hosted_checkout)
      </td>

      <td>
        Initiate cross-border payments on PayU Hosted Checkout with `buyer_type_business` and mandatory UDF fields.
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – Cards (Cross-Border)](ref:_payment_cross-border_merchant_hosted_cards)
      </td>

      <td>
        Submit merchant-hosted card payment requests for cross-border one-time transactions.
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – NetBanking (Cross-Border)](ref:_payment_cross-border_merchant_hosted_netbanking)
      </td>

      <td>
        Initiate NetBanking payments for cross-border transactions. **Used in:** [NetBanking Integration](doc:netbanking-integration-merchant-hosted-integration-cb).
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – UPI (Cross-Border)](ref:_payment_cross-border_merchant_hosted_upi)
      </td>

      <td>
        Initiate UPI Intent payments for cross-border transactions.
      </td>
    </tr>

    <tr>
      <td>
        ### UDF Update & Invoice Upload
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [UDF Update API](ref:udf_update_api)
      </td>

      <td>
        Update UDF1–UDF5 values (including invoice ID) on a completed transaction. **Used in:** [Integrate Cross-Border Payments with PayU](doc:integrate-cross-border-payments-for-payubiz), [Import Plugin Integration](doc:cross-border-payments-import-plugin-integration-1).
      </td>
    </tr>

    <tr>
      <td>
        [Invoice Upload API](ref:invoice_upload_api)
      </td>

      <td>
        Upload invoice documents and AWB files required for bank processing and settlement.
      </td>
    </tr>

    <tr>
      <td>
        ### Subscriptions with PACB
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Payment Consent Transaction – PayU Hosted](ref:payment-consent-transaction-payu-hosted)
      </td>

      <td>
        Register a subscription mandate on PayU Hosted Checkout for cross-border recurring payments.
      </td>
    </tr>

    <tr>
      <td>
        [Registration Mandate for Cards ](ref:registration-mandate-for-cards-pacb)
      </td>

      <td>
        Register a card mandate for cross-border subscription consent transactions.
      </td>
    </tr>

    <tr>
      <td>
        [UPI Consent Transaction ](ref:upi-consent-transaction-cross-border)
      </td>

      <td>
        Register a UPI mandate for cross-border subscription consent transactions.
      </td>
    </tr>

    <tr>
      <td>
        [Pre-Debit Notification API](ref:pre_debit_notification_api)
      </td>

      <td>
        Notify the customer before executing a recurring debit (required at least 48 hours in advance).
      </td>
    </tr>

    <tr>
      <td>
        [Recurring Payment Transaction API ](ref:recurring-payment-transaction-api-pacb)
      </td>

      <td>
        Execute recurring debits against a registered cross-border mandate.
      </td>
    </tr>

    <tr>
      <td>
        ### PACB Settlements
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Get On-Hold Transactions API ](ref:get-on-hold-transactions-api)
      </td>

      <td>
        Retrieve transactions held pending additional invoice or trade metadata. .
      </td>
    </tr>

    <tr>
      <td>
        [Update On-Hold Transactions API](ref:update-on-hold-transactions-api)
      </td>

      <td>
        Submit additional customer or trade information to release on-hold settlements.
      </td>
    </tr>

    <tr>
      <td>
        [Settlement Detail Range API](ref:settlement-detail-range-api-for-cross-border)
      </td>

      <td>
        Retrieve paginated transaction-level settlement data for a date range or UTR.
      </td>
    </tr>

    <tr>
      <td>
        [Get Settlement Detail API ](ref:get-settlement-detail-api-cross-border-payments)
      </td>

      <td>
        Retrieve settlement details for cross-border transactions.
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

<Accordion title="LRS-specific APIs" icon="fa-globe">
  Cross-border transactions under the Liberalised Remittance Scheme (LRS) use additional `_payment` parameters for PAN validation, TCS declarations, and `lrs_service_type`. For the full LRS API list and integration guides, refer to [Liberalised Remittance Scheme (LRS) for Travel & Education](doc:cb-lrs-integration).
</Accordion>

<br />