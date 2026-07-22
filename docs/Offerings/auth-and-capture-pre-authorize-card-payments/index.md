---
title: Pre-Authorize Payments
excerpt: ''
deprecated: false
hidden: false
icon: far fa-shop-lock
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## What is Auth & Capture

Auth and Capture is a two-step payment processing method that provides greater control and flexibility over transactions:

1. **Authorization** (Auth): Verifies the payment method is valid and reserves funds on the customer's account without immediately charging them
2. **Capture**: Later transfers the reserved funds from the customer's account to the merchant's account, completing the transaction

PayU supports Auth and Capture on Credit Card and Debit Card payments.

## PayU's offering

In a basic payment flow, the payable amount from your payment request is authorized and captured immediately during the transaction flow, but sometimes you may want to charge the customer a different amount or extend the period of authorization to capture the payment at later point in time.<br />PayU’s pre-authorization (also card authorization, authorization hold or Auth and Capture) product allows merchants two-step card payments so you can temporarily block some amount of funds when a customer places an order (authorization) and then capture the amount later. If the order canceled by the customer within a specific time frame (typically 5-7 days), then you can mark the transaction cancelled and the amount goes back to the consumer’s original payment source instantly.

<Callout icon="🚧" theme="warn">
  ###

  **Remember**: PayU currently supports Pre-authorization (Auth and Capture) for Visa, Mastercard and Amex Credit Cards.
</Callout>

<Callout icon="👍" theme="okay">
  ### Before you begin:

  Register for a account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

## Integration guides

The following sections describe how to integrate pre-authorization (Auth and Capture) with PayU:

- [Pre-Authorize Card Transactions](doc:pre-authorize-card-transactions)
  - [PayU Hosted Integration](doc:payu-hosted-integration-pre-authorize-payments)
  - [Credit Card – Merchant Hosted Integration](doc:credit-card-merchant-hosted-integration-pre-authorize-payment)
  - [Debit Card – Merchant Hosted Integration](doc:debit-card-merchant-hosted-integration-preauthorize-payments)
- [UPI One-Time Mandate Integration](doc:upi-one-time-mandate-integration)
  - [UPI Intent – PayU Hosted](doc:upi-intent-one-time-mandate-integration-payu-hosted)
  - [UPI Intent – Merchant Hosted](doc:upi-intent-one-time-mandate-integration)
  - [UPI Collect – PayU Hosted](doc:upi-collect-one-time-mandate-integration-payu-hosted)
  - [UPI Collect – Merchant Hosted](doc:upi-collect-one-time-mandate-integration)
  - [UPI Reserve Pay](doc:upi-reserve-pay)
- [S2S Pre-Authorize Payment](doc:s2s-pre-authorize-payment)
- [Cancel a Pre-Authorized Payment](doc:cancel-a-pre-authorized-payment)

## Features

- Assurance that held funds are maintained by the payer up to 7 days.
- No transaction cost (TDR) levied on the cancelled ordered.
- Improved Customer experience as cancelled amount is instantly credited to the payer’s source account.
- No chargeback liability until a capture of funds is made on the authorization request.

## Workflow

The following flow diagrams illustrates the difference between collecting payment without and with Auth and Capture:


<Image src="https://files.readme.io/2af883b-preauth_workflow.png" align="center" />


- **Pre-authorization** transaction checks the fund availability and holds the required funds on the payer’s card for up to 7 days.
- A capture request is used to debit the funds from the payer’s card.
- After an authorization has been made, you can capture either a partial amount (partial capture) or the full amount of the authorization.
- PayU provides **Auto Capture** feature by default on 7th day of authorization initiation If there is no request of capture/cancel from merchant. Merchant can opt in for Auto Cancel or set a different Auto capture time for their authorization requests. 
- Cancel is only applicable to the Authorization requests and any Authorization which is captured can only be refunded.
- After the partial amount has been captured, the balance amount is cancelled immediately.

<Callout icon="📘" theme="info">
  ### Note:

  PayU does not support multiple partial captures on a single authorization request.
</Callout>

## Use cases

There are several use cases for adjusting an authorisation. A few scenarios are:

<Accordion title="Hospitality" icon="fa-hotel">
  * At the checkout page of the hotel’s website, the hotel pre-authorises payment of the rooms that the guest pre-booked.
  * Before the arrival, the guests decides to cancel one of the pre-booked rooms. The hotel adjusts these expenses of their pre-authorized amount.
  * When the guest checks out, the hotel captures the final adjusted amount using partial capture.
</Accordion>

<Accordion title="Prepaid Services" icon="fa-car">
  For example, a self drive car renting platform, the merchants often collect security deposits along side the variable expenses. In this case merchant does a pre-authorize of the payment with some extra margins. At the end of the trip, the merchant adjusts the authorised amount and does a partial capture or full capture based on the expenses incurred.
</Accordion>

<Accordion title="E-Commerce merchants" icon="fa-shopping-cart">
  For example, a seller is running a promotional event, where a shopper pre-books a phone that will be released few days later. The phone seller pre-authorises the payment, but as they can only ship the product later, they need to extend the authorisation validity. This allows both merchants to capture the payment over an extended duration.
</Accordion>

## APIs used in Integration

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