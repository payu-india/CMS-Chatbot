---
title: APIs used in TPV integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in TPV integration
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
        ### \_payment API for Collect Payment use cases
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
      </td>

      <td>
        Initiate TPV payments on PayU Hosted Checkout with `beneficiarydetail` to lock transactions to pre-registered bank accounts.
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – Merchant Hosted Checkout](ref:_payment_merchant_hosted)
      </td>

      <td>
        Submit merchant-hosted TPV payment requests with `beneficiarydetail` for NetBanking, UPI, and NEFT/RTGS.
      </td>
    </tr>

    <tr>
      <td>
        ### Recurring Payment with TPV
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Recurring Payment Transaction API](ref:recurring_payment_api)
      </td>

      <td>
        Execute recurring debits after a successful UPI Autopay mandate registration with TPV.
      </td>
    </tr>

    <tr>
      <td>
        ### Payment Links
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Create Payment Link API](ref:create-payment-links)
      </td>

      <td>
        Create a payment link with beneficiary account details for TPV verification.
      </td>
    </tr>

    <tr>
      <td>
        [Get Access Token API for Payment Links](ref:get-token-api-for-payment-links)
      </td>

      <td>
        Generate an OAuth token with `create_payment_links` scope to authenticate Payment Link API requests.
      </td>
    </tr>

    <tr>
      <td>
        ### General
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Validate VPA API](ref:validate_vpa_api)
      </td>

      <td>
        Validate the customer's UPI handle before initiating UPI TPV or UPI Autopay flows.
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