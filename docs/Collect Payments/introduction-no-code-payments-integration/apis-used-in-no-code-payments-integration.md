---
title: APIs used for Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used for No Code Payments Integration
  robots: index
---
PayU offers following APIs for Payment Link Integration. Also, you can use create them using Dashboard   as described in the [Payment Links](doc:payment-links-dashboard) section.

<Callout icon="📘" theme="warn">
  ### Use PayU Dashboard for creating buttons or invoices.

  You must use PayU Dashboard for creating buttons or invoices. For more information, refer to [Payment Buttons](doc:payment-buttons-dashboard) or [Payment Invoices.](doc:invoices-dashboard)&#x20;
</Callout>

| API                                                                    | Purpose                                                                                                                                 |
| ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| [Get Token API – Payment Links](ref:get-token-api-for-payment-links)   | Obtain an OAuth bearer token (`create_payment_links`, `read_payment_links`, `update_payment_links` scopes) for Payment Links API calls. |
| [Revoke Token API – Payment Links](ref:revoke-token-api-payment-links) | Invalidate an access token when no longer needed.                                                                                       |
| [Create Payment Link API](ref:create-payment-links)                    | Create a payment link with amount, description, customer details, and callback URL.                                                     |
| [Share Payment Link API](ref:share_payment_link_api)                   | Share a created payment link with customers via configured channels.                                                                    |
| [Get Single Payment Link API](ref:get-single-payment-link)             | Retrieve details for one payment link.]\(doc:integration-api-for-payment-links).                                                        |
| [Get All Payment Links API](ref:get-all-payment-links-api)             | List payment links with filters and pagination.                                                                                         |

<br />
