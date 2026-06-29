---
title: Third-Party Verification (TPV)
excerpt: >-
  The global financial industry is coming up with a new paradigm for risk
  management. If you are a merchant in the BFSI sector, your business is subject
  to strict guidelines, where various regulatory bodies regulate your day-to-day
  operations.
deprecated: false
hidden: false
metadata:
  title: Third-Party Verification or TPV Integration Introduction
  description: >-
    The page explains that TPV ensures credibility and reduces risk for
    customers. It compares the TPV workflow with regular net banking or UPI
    transactions, highlighting the need to pass the customer's account number in
    the payment request for TPV integration.


    The advantages of TPV integration on PayU's platform are emphasized,
    including compliance with SEBI guidelines for account authentication, the
    ability to lock transactions to specific bank account numbers or Customer
    Relationship Numbers (CRN), and the added security of having a locked
    account during fund transfers. The page further explains that brokers and
    online businesses can sign up for PayU's TPV solution to securely and
    conveniently transact with their customers in real-time while meeting
    compliance requirements.


    The page also mentions the TPV integration support for Net Banking and UPI,
    as well as Merchant Hosted Checkout (Seamless) and PayU Server-to-Server
    Integration. However, it states that TPV is currently not supported for the
    PayU Hosted Checkout integration.
  keywords:
    - TPV
    - ' TPV integration'
    - ' TPV workflow'
    - ' TPV'
    - ' Third-Party Verification integration'
  robots: index
next:
  description: ''
---
The global financial industry is coming up with a new paradigm for risk management. If you are a merchant in the BFSI sector, your business is subject to strict guidelines, where various regulatory bodies regulate your day-to-day operations.

Third-Party Verification (TPV) is a mandatory requirement as per Stock Exchange Bureau India (SEBI) mandate for merchants such as stockbrokers and mutual funds operating in the BFSI sector. TPV is a prerequisite that ensures credibility, and it reduces the risk for customers.

## TPV Workflow

![](https://files.readme.io/2bea29d-image.png)

## Comparison of TPV with regular flow

In a regular Net Banking or a UPI transaction, you don’t pass the customer account number from which you want the customer to transact, but in the case of TPV integration, you know the customer account number, and you want the customer only to transact with the same account number.<br />You also pass the customer account number in the payment request compared to regular retail banking or UPI.

## Why TPV?

In its constant endeavour to reach out to new categories of merchants, PayU, now provides TPV integration on its payment processing platform.

Third-Party Verification (TPV) procedure is a mandatory requirement for web merchants such as stock brokers and mutual funds, operating in the BFSI (Banking, Financial Services and Insurance) sector. This account authentication procedure is essential for brokerage, Demat Account transfers, investments and other payments specified by the Securities and Exchange Board of India (SEBI).

As per SEBI guidelines, transactions must be made by their customers exclusively from a specific bank account number or CRN (Customer Relationship Number).

PayU will enable these businesses to meet their compliance requirements for online payment collections by offering the TPV integrations of banks. When the customer transacts with the merchant through our payment gateway, his bank account number or CRN is mapped in such a way so as to lock the transaction to ensure that the payment is processed only from his registered bank account.

TPV integration on the payment gateway resembles a Net Banking transaction with the added advantage of having a locked account during fund transfers. The merchant (such as a broker) initially registers the bank account number or CRN of the customer to meet the SEBI guideline. These account parameters will be stored by the merchant and forwarded to PayU, which in turn submits them to the corresponding bank of the customer during the transaction process.

Brokers and other online businesses can now sign up for our services and take advantage of our TPV solution to transact online with their customers securely and conveniently in real-time.

Meet your compliance requirements and start transacting online with your customers by availing the TPV integration of leading banks on PayU’s advanced payment platform.

## TPV integration support

PayU supports the PayU Hosted Checkout (non-seamless), Merchant Hosted Checkout (Seamless) and PayU Server-to-Server Integration are supported

- [PayU Hosted or non-seamless integration](payu-hosted-checkout-tpv-workflow)
- [Seamless Integration](https://docs.payu.in/docs/collect-payments-with-tpv-merchant-hosted-checkout)
  - [Net Banking](/docs/net-banking-integration-for-tpv)
  - [UPI](/docs/upi-integration-for-tpv)
    - [UPI Intent Autopay](https://docs.payu.in/docs/upi-intent-autopay-tpv-integration)
    - [UPI Collect Autopay](https://docs.payu.in/docs/upi-collect-autopay-tpv-integration)\ <br />

## APIs used in TPV integration

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
        \### \_payment API for Collect Payment use cases
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
      </td>

      <td>
        Initiate TPV payments on PayU Hosted Checkout with `beneficiarydetail` to lock transactions to pre-registered bank accounts. **Used in:** [Net Banking TPV Integration – PayU Hosted](doc:collect-netbanking-payment-with-tpv-payu-hosted-checkout), [UPI TPV Integration – PayU Hosted](doc:collect-upi-payment-with-tpv-payu-hosted-checkout), [Subscription TPV Integration](doc:tpv-recurring-payments-integration-pay-hosted-checkout), [Integrate Payment Link TPV](doc:integrate-payment-link-tpv).
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – Merchant Hosted Checkout](ref:_payment_merchant_hosted)
      </td>

      <td>
        Submit merchant-hosted TPV payment requests with `beneficiarydetail` for NetBanking, UPI, and NEFT/RTGS. **Used in:** [Net Banking Integration for TPV](doc:net-banking-integration-for-tpv), [UPI Integration for TPV](doc:upi-integration-for-tpv), [UPI Intent and Collect Autopay – TPV Integration](doc:upi-intent-and-collect-autopay-tpv-integration), [NEFT/RTGS Integration for TPV](doc:neftrtgs-integration-for-tpv).
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
        Execute recurring debits after a successful UPI Autopay mandate registration with TPV. **Used in:** [UPI Intent and Collect Autopay – TPV Integration](doc:upi-intent-and-collect-autopay-tpv-integration).
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
        Create a payment link with beneficiary account details for TPV verification. **Used in:** [Integrate Payment Link TPV](doc:integrate-payment-link-tpv).
      </td>
    </tr>

    <tr>
      <td>
        [Get Access Token API for Payment Links](ref:get-token-api-for-payment-links)
      </td>

      <td>
        Generate an OAuth token with `create_payment_links` scope to authenticate Payment Link API requests. **Used in:** [Integrate Payment Link TPV](doc:integrate-payment-link-tpv).
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
        Validate the customer's UPI handle before initiating UPI TPV or UPI Autopay flows. **Used in:** [UPI Integration for TPV](doc:upi-integration-for-tpv), [UPI Intent and Collect Autopay – TPV Integration](doc:upi-intent-and-collect-autopay-tpv-integration).
      </td>
    </tr>

    <tr>
      <td>
        [Verify Payment API](ref:verify_payment_api)
      </td>

      <td>
        Server-side reconciliation of transaction status after payment. **Used in:** all TPV integration guides via `<Verify_Payment_Tabs />` or inline verification steps.
      </td>
    </tr>
  </tbody>
</Table>

<br />
