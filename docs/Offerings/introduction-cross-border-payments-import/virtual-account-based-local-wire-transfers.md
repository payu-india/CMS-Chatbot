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

<br />

Onboard sub-merchant. PSP creates a Copy MID through the Create Merchant API and retrieves sub-merchant credentials. A Virtual Account is issued for the sub-merchant.

<br />

Receive payment. Payer in India transfers funds to the Virtual Account. PayU confirms the credit and notifies the PSP via webhook. The payment is placed on hold.

<br />

Submit compliance data. PSP lists on-hold transactions and submits invoice and trade metadata. PayU runs compliance checks.

<br />

Settle or return. Approved payments are released for outward settlement to the PSP. Failed or timed-out payments are returned.

PayU partners with an AD-1 category bank for outward settlement. Funds move to the Outward Collection Account (OCA) before settlement to the PSP, similar to the import collections workflow.

<br />

Integration guide

<br />

<br />

<br />

Section

<br />

Activity

<br />

API

<br />

Dev-docs

<br />

<br />

Authentication

<br />

Authenticate with parent PA key and salt

<br />

—

<br />

\[Authentication]

<br />

<br />

Sub-merchant onboarding

<br />

Create sub-merchant (Copy MID)

<br />

Create Merchant (PACB)

<br />

\[Create Merchant — PACB]

<br />

<br />

<br />

<br />

Update sub-merchant profile

<br />

Update Merchant Details (PACB)

<br />

\[Update Merchant — PACB]

<br />

<br />

<br />

<br />

Fetch sub-merchant status and profile

<br />

Get Merchant Details (PACB)

<br />

\[Get Merchant — PACB]

<br />

<br />

<br />

<br />

Get sub-merchant key and salt

<br />

Get Sub-merchant Credentials

<br />

\[Get Credentials — PACB]

<br />

<br />

Virtual Account

<br />

Get VA number, IFSC, and status

<br />

Get Merchant Details / List VA

<br />

\[Virtual Account]

<br />

<br />

<br />

<br />

Activate or deactivate a VA

<br />

Update Virtual Account

<br />

\[Update VA]

<br />

<br />

Payments

<br />

Payment received webhook

<br />

Webhook — payment received

<br />

\[Webhooks — payment received]

<br />

<br />

<br />

<br />

Payment rejected webhook

<br />

Webhook — payment rejected

<br />

\[Webhooks — payment rejected]

<br />

<br />

<br />

<br />

List transactions

<br />

List Transactions

<br />

\[List Transactions]

<br />

<br />

<br />

<br />

Get transaction details

<br />

Get Transaction

<br />

\[Get Transaction]

<br />

<br />

On hold

<br />

List on-hold transactions

<br />

List On-Hold Transactions

<br />

\[On-Hold Transactions]

<br />

<br />

<br />

<br />

Check missing fields

<br />

Get Transaction Readiness

<br />

\[Transaction Readiness]

<br />

<br />

<br />

<br />

Submit invoice and trade data

<br />

Submit Metadata

<br />

\[Submit Metadata]

<br />

<br />

<br />

<br />

Upload invoice file

<br />

Upload Invoice

<br />

\[Upload Invoice]

<br />

<br />

Settlement

<br />

Ready for settlement webhook

<br />

Webhook — settlement eligible

<br />

\[Webhooks — settlement eligible]

<br />

<br />

<br />

<br />

Refund completed webhook

<br />

Webhook — refund

<br />

\[Webhooks — refund]

<br />

<br />

<br />

<br />

Get settlement by date or UTR

<br />

Get Settlement Details

<br />

\[Settlement Details]

<br />

<br />

<br />

<br />

Get settlement for a transaction

<br />

Get Transaction Settlement

<br />

\[Transaction Settlement]

<br />

<br />

<br />

<br />

Configure reconciliation reports

<br />

Configure Reports

<br />

\[Report Configuration]

<br />

Key behaviours

<br />

<br />

<br />

Topic

<br />

Behaviour

<br />

<br />

After credit

<br />

Payment is on hold until metadata is complete and checks pass

<br />

<br />

Settlement

<br />

Only approved payments enter settlement batches

<br />

<br />

Credit limit

<br />

Credits above INR 25,00,000 are rejected

<br />

<br />

Inactive VA

<br />

New credits are rejected

<br />

<br />

API credentials

<br />

Onboarding uses parent PA key/salt; payments use sub-merchant credentials

<br />

Getting started

<br />

<br />

Obtain parent PA credentials from PayU.

<br />

Integrate Create Merchant and Get Credentials for a test sub-merchant.

<br />

Register webhook URLs.

<br />

Test: create sub-merchant → receive credit → submit metadata → fetch settlement details.

For issues, share merchant ID, transaction ID, and webhook eventId with your PayU integration contact.
