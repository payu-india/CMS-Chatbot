---
title: Pre-Discounted Offer - Merchant Hosted Checkout
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
With the Merchant Hosted Checkout integration, the entire payment experience is controlled by PayU. This section describes how to use the PayU Hosted Integration to collect payments with a Pre-Discounted EMI Offer.

## Integration Procedure

To integrate offers using Merchant Hosted Checkout integration with Pre-Discounted EMI:

**Reference**: For the Merchant Hosted Checkout flow, refer [Merchant Hosted Checkout Integration.](https://devguide.payu.in/merchant-integration/web-checkout/merchant-hosted-checkout/)

---

## Step 1: Fetch and display offers

On the checkout page (or earlier on PDP, Cart, Offers) use the **Fetch Offers** API to get the offers and display all the offers. For more information, refer to [Fetch Offers API](https://devguide.payu.in/offers-integration/offers-api/fetch-offer-api/).

---

## Step 2: Validate the offer

Use the **Validate Offer** API to validate if the offer will be applied on this transaction or not. For more information, refer to [Validate Offer API](https://devguide.payu.in/offers-integration/offers-api/validate-offer-api/).

---

## Step 3: Make the payment request

Make the payment request using the **_payment** API using the following additional parameters for Offers. For more information on the complete list of parameters to be posted, refer to [Collect Payment with Merchant Hosted Integration](https://devguide.payu.in/merchant-integration/merchant-hosted-checkout/merchant-hosted-integration/#req_params).

<Accordion title="Additional request parameters" icon="fa-table">
  <table>
    <thead>
      <tr>
        <th><strong>Parameter</strong></th>
        <th><strong>Description</strong></th>
        <th><strong>Example</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>api_version<br /><strong>mandatory</strong></td>
        <td>The API version of the _payment API must be specified as <strong>14</strong>.</td>
        <td>14</td>
      </tr>
      <tr>
        <td>user_token<br /><strong>mandatory for UPI, NB, Wallet</strong></td>
        <td>
          The use for this param is to allow the offer engine to apply velocity rules at a user level.<br /><br />
          - <strong>Card Based Offers (CC, DC, EMI)</strong>: In case of card payment mode offers, if this parameter is passed the velocity rules would be applied on this token, if not passed the same would be applied on the card number.<br />
          - <strong>UPI, NB, Wallet</strong>: It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.
        </td>
        <td>User123456</td>
      </tr>
      <tr>
        <td>offer_key<br /><strong>mandatory</strong></td>
        <td>This parameter is to apply the specific offer to the transaction. Offer key can be accessed from the dashboard on offer creation. In case the offer is created via assisted mode, please reach out to your Key Account manager to provide the offer key</td>
        <td>newoffer1@5686</td>
      </tr>
      <tr>
        <td>hash<br /><strong>mandatory</strong></td>
        <td>
          It is used to avoid the possibility of transaction tampering.<br /><strong>Notes</strong>:<br /><br />
          - The following order must be used for hashing: <code>key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|offer_key|offer_auto_apply|SALT</code><br />
          For more information on hash generation process, refer to [Hashing Request and Response](https://devguide.payu.in/web-checkout/encryption-of-request/).<br />
          - If any of the keys is null/not configured, "|" character must be concatenated.<br />
          - The above hash logic is for _payment API version 10 or later
        </td>
        <td></td>
      </tr>
    </tbody>
  </table>
</Accordion>

---

## Step 4: Check the response from PayU

Check the following response parameters (for Offers) from PayU to handle the payment response, as the net amount debit may be different from the amount sent by you in the request.

<Accordion title="Response parameters" icon="fa-table">
  <table>
    <thead>
      <tr>
        <th><strong>Parameter</strong></th>
        <th><strong>Description</strong></th>
        <th><strong>Example</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>discount</td>
        <td>This will specify the offer value provided to the user.</td>
        <td>10.00</td>
      </tr>
      <tr>
        <td>net_amount_debit</td>
        <td>This will specify the actual amount deducted from the customer's payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request.</td>
        <td>100.00</td>
      </tr>
      <tr>
        <td>offer</td>
        <td>This parameter is used to post the offer key.</td>
        <td>newoffer1@5686</td>
      </tr>
      <tr>
        <td>offer_type</td>
        <td>This parameter is used to post any of the following offer_type:<br /><br />- instant<br />- cashback</td>
        <td>instant</td>
      </tr>
    </tbody>
  </table>
</Accordion>

For a sample response, refer to the [Sample Response](https://devguide.payu.in/merchant-integration/payu-hosted-checkout/payu-hosted-checkout-integration#Step3) section of [Merchant Hosted Checkout Integration.](https://devguide.payu.in/merchant-integration/payu-hosted-checkout/payu-hosted-checkout-integration#Step3)

---

## Step 5: Verify the payment

Similar to the payment response, the same parameters can be handled as part of the **Verify Payment** API. For more information on **Verify Payment** API, refer to [Verify Payment Status by Transaction ID](https://devguide.payu.in/api/payments/transaction-verification-apis/verify_payment-api/).

<Accordion title="Verify payment response parameters" icon="fa-table">
  <table>
    <thead>
      <tr>
        <th><strong>Parameter</strong></th>
        <th><strong>Description</strong></th>
        <th><strong>Example</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>transaction_amount</td>
        <td>This parameter contains the total transaction amount before discount.</td>
        <td>50000.00</td>
      </tr>
      <tr>
        <td>net_amount_debit</td>
        <td>This parameter contains the actual amount deducted from the customer's payment instrument. In case of Instant discount this amount would be lesser than the amount passed by you in the request.</td>
        <td>47500.00</td>
      </tr>
      <tr>
        <td>discount</td>
        <td>This parameter contains the offer value provided to the user. This value will specify the offer amount for both Instant discount and Cashback offers.</td>
        <td>2500.00</td>
      </tr>
    </tbody>
  </table>
</Accordion>

PayU would refund the exact amount passed by you in the Refund request. For more information, refer to [Refunds for Offers](https://devguide.payu.in/offers-internal/refunds-for-offers/).

<Callout icon="📘" theme="info">
  **Note**: You can enable the **Enforce Offer** flag by requesting your PayU Key Account Manager. If you enable the **Enforce Offer** flag, the best offer out of the all the offers passed will be applied for the customer.
</Callout>
