---
title: Cancel the Recurring Payment for UPI
excerpt: 'API Command: **upi\_mandate\_revoke**'
deprecated: false
hidden: true
metadata:
  title: Cancel the Recurring Payment for UPI
  description: >-
    Learn how to cancel recurring payment registrations for UPI using PayU's
    API. This documentation provides detailed instructions for revoking
    mandates, ensuring compliance with RBI guidelines and enabling seamless
    management of subscription cancellations.
  keywords:
    - upi_mandate_revoke
    - ' PayU Cancel Recurring Payments API'
    - ' Revoke Recurring Payment UPI'
    - ' PayU UPI recurring billing cancellation'
    - ' PayU UPI subscription cancellation'
    - ' Cancel UPI recurring transactions'
  robots: index
next:
  description: ''
  pages:
    - type: endpoint
      slug: get-mandate-status-api-for-upi-only
      title: Get UPI Mandate Status API
    - type: endpoint
      slug: modify-the-recurring-payment-for-upi
      title: Modify Recurring Payment for UPI
---
**Cancel Recurring Registration** API allows the merchants to cancel the UPI registration from their website. It is a mandate to implement the **Cancel Recurring Registration** API so that your customers can use Recurring Payments. After the registration is canceled for a customer, the merchant cannot restore it, and the customer must register a fresh mandate with the merchant (applicable for UPI).

> 📘 Note:
>
> Your customers cannot use Recurring Payments without the **Cancel Recurring Registration** API being implemented.

HTTP Method: **POST**

**Environment**

|                        |                                                        |
| :--------------------- | :----------------------------------------------------- |
| Test Environment       | &lt;https://test.payu.in/merchant/postservice.php?form=2&gt; |
| Production Environment | &lt;https://info.payu.in/merchant/postservice.php?form=2&gt; |

## Request parameters

<HTMLBlock>{`
<p>Error parsing JSON</p>
`}</HTMLBlock>

### var1 JSON fields description

**var1** parameter (JSON format) fields description:

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>authPayuId<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must contain the mihpayid returned in the payment response of the Registration transaction when the transaction is successfully completed.<br>As explained in <a href="ref:payment-consent-transaction-merchant-hosted">Payment Consent Transaction using Merchant Hosted Checkout</a> the section, the merchant needs to map this value against the customer profile at their end so that correct authPayuid will be passed in the request.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>requestId<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>This parameter must contain the unique request value generated at merchant’s end to distinguish independent request call.</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Response Parameters

| **Parameter Name** | **Description**                                                       |
| ------------------ | --------------------------------------------------------------------- |
| status             | Status defines acknowledgment from PayU. Possible values are:         |
| action             | Always returned as “MANDATE\_REVOKE” to highlight the type of action. |
| message            | Description of the Mandate cancellation process.                      |

## Sample response

- Sample response for successful cancellation:

Cancelling Recurring Registration - Success Response

```plaintext
{
	"status": 1,
	"action": "MANDATE_REVOKE",
	"message": "Request Initiated"
}
```

- Sample Response for failed cancellation

Cancelling Recurring Registration - Failure Response

```plaintext
{
	"status": 0,
	"action": "MANDATE_REVOKE",
	"message": "Mandate is not active"
}
```