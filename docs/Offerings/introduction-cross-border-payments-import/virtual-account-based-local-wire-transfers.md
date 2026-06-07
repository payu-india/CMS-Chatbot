---
title: Virtual-Account Based Local Wire Transfers
deprecated: false
hidden: true
metadata:
  robots: index
---
Collect cross-border payments through Virtual Accounts (VA). Payers in India transfer INR via NEFT, RTGS, or IMPS. PayU confirms the credit, holds it until required trade data is submitted and approved, then settles to your offshore account in currency of choice.

Suited for: Global **Payment Service Providers&#x20;**(PSPs) integrating via API.

**Illustrative payment journey for PACB Virtual Account Collections.**

![](https://files.readme.io/363270ff925b38a549c84cdfddf9b4bd346b7180f3a944581c9b680b6a889635-image.png)

<br />

1. **Sub-merchant onboarding** — Create sub-merchant and retrieve API credentials.
2. **Create & manage VA&#x20;**— Provision and manage Virtual Account via API.
3. **Receive credit&#x20;**— Payer transfers to VA; PayU confirms and notifies PSP.
4. **On-hold handling** — PSP submits invoice and trade metadata; PayU runs checks.
5. **Settle&#x20;**— Approved payments settle to PSP via AD Bank with UTR.

PayU partners with an AD-1 category bank for outward settlement. Funds move to the Outward Collection Account (OCA) before settlement to the PSP, similar to the [import collections workflow.](https://docs.payu.in/docs/workflow-for-cross-border-payments-import)

## Integration Guide

<Table>
  <thead>
    <tr>
      <th>
        Section
      </th>

      <th>
        Activity
      </th>

      <th>
        API Document
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **Sub-merchant onboarding**
      </td>

      <td>
        Create sub-merchant
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Update sub-merchant profile
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        **Virtual Account (VA) Management**
      </td>

      <td>
        Create & Update VA
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Get List of VA per merchant
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        **Payments**
      </td>

      <td>
        Payment webhooks & Status Check API
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        List transactions
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Get transaction details
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        **On hold transactions**
      </td>

      <td>
        Get & Update On-Hold transactions
      </td>

      <td>
        - Get On-hold Settlement API
        - Invoice Upload API
      </td>
    </tr>

    <tr>
      <td>
        **Settlement**
      </td>

      <td>
        Get Settlement Status
      </td>

      <td>
        [https://docs.payu.in/reference/settlement-detail-range-api-for-cross-border](https://docs.payu.in/reference/settlement-detail-range-api-for-cross-border "https://docs.payu.in/reference/settlement-detail-range-api-for-cross-border")
      </td>
    </tr>

    <tr>
      <td>
        **Refunds**
      </td>

      <td>
        Initiate refund by merchant txn ID / PayU
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Get Refund Status&#x20;
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        Refund Webooks & Status API
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

## Key Behaviours

- After credit, payment is on hold until metadata is complete and checks pass
- Transaction limit at INR 25,00,000, any transaction on the virtual account higher than this amount will be **rejected**.
- Onboarding uses PSP's credentials; payments use **sub-merchant credentials**

<br />

## Getting Started

- Obtain parent PA credentials from PayU.
- Integrate Create Merchant and Get Credentials for a test sub-merchant.
- Register webhook URLs.
- Test: create sub-merchant → receive credit → submit metadata → fetch settlement details.

For issues, share merchant ID, transaction ID, and webhook eventId with your PayU integration contact or international.integration\@payu.in
