---
title: APIs used in Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: APIs used in Auth and Capture Integration
  description: ''
  robots: index
next:
  description: ''
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
        ### Capture and Collect Payment
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Pre-Authorize Payment API – PayU Hosted](ref:pre_authorize_payment)
      </td>

      <td>
        Initiate a card pre-authorization on PayU Hosted Checkout with `pre_authorize=1` to hold funds without capturing.
      </td>
    </tr>

    <tr>
      <td>
        [Pre-Authorize Payment API – Merchant Hosted](ref:pre_authorize_payment_merchant_hosted)
      </td>

      <td>
        Initiate a card pre-authorization on merchant-hosted checkout with `pre_authorize=1`.
      </td>
    </tr>

    <tr>
      <td>
        [Capture a Pre-Authorized Payment API](ref:capture_a_payment)
      </td>

      <td>
        Capture held funds (full or partial) using the `capture_transaction` command after authorization.
      </td>
    </tr>

    <tr>
      <td>
        [Cancel a Pre-Authorized Transaction API](ref:cancel-a-pre-authorized-transaction)
      </td>

      <td>
        Cancel an authorization and release held funds using the `cancel_transaction` command. **Used in:** [Cancel a Pre-Authorized Payment](doc:cancel-a-pre-authorized-payment), all card and UPI pre-auth integration guides.
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
        Check transaction status; `unmappedstatus` of `auth` indicates a successful authorization.
      </td>
    </tr>

    <tr>
      <td>
        ### Check Status
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Check Action Status API with Request ID](ref:check_action_status_api_with_request_id)
      </td>

      <td>
        Check the status of auth, capture, or refund requests queued at PayU.
      </td>
    </tr>

    <tr>
      <td>
        ### One-Time Mandate
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [UPI One-Time Mandate API – PayU Hosted](ref:upi-one-time-mandate-transaction-api-payu-hosted)
      </td>

      <td>
        Initiate a UPI one-time mandate pre-authorization on PayU Hosted Checkout.
      </td>
    </tr>

    <tr>
      <td>
        [UPI One-Time Mandate API – Merchant Hosted](ref:_payment-upi-one-time-mandate-transaction-api)
      </td>

      <td>
        Initiate a UPI one-time mandate pre-authorization on merchant-hosted checkout.
      </td>
    </tr>

    <tr>
      <td>
        [UPI OTM Status Check API](ref:upi-otm-status-check-api)
      </td>

      <td>
        Check the status of a UPI one-time mandate transaction.
      </td>
    </tr>

    <tr>
      <td>
        [Validate VPA API](ref:validate_vpa_api)
      </td>

      <td>
        Validate the customer's UPI VPA before initiating UPI Collect mandate flows.
      </td>
    </tr>

    <tr>
      <td>
        [UPI Reserve Pay One-Time Mandate – PayU Hosted](ref:upi-reserve-pay-one-time-mandate-payu-hosted)
      </td>

      <td>
        Pre-authorize UPI Reserve Pay transactions on PayU Hosted Checkout.
      </td>
    </tr>

    <tr>
      <td>
        [UPI Reserve Pay One-Time Mandate – Merchant Hosted](ref:upi-reserve-pay-one-time-mandate-merchant-hosted)
      </td>

      <td>
        Pre-authorize UPI Reserve Pay transactions on merchant-hosted checkout.
      </td>
    </tr>
  </tbody>
</Table>

<br />
