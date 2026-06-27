---
title: '[Internal Review]Refunds Overview'
deprecated: false
hidden: true
metadata:
  robots: index
---
Order cancellations are an unfortunate reality for any business. Customers may cancel an order, return part of the order, or return the full order. Merchants may not have the resources to fulfill the order and must cancel it. Therefore, it is imperative for merchants collecting payments online to refund payments back to customers efficiently.

This guide covers everything you need to know about processing refunds through PayU.

## Refund vs Chargeback

Understanding the difference helps you choose the right approach:

| Aspect                  | Refund                | Chargeback                    |
| ----------------------- | --------------------- | ----------------------------- |
| **Initiated by**        | Merchant              | Customer (via their bank)     |
| **Process**             | Direct through PayU   | Bank-mediated dispute         |
| **Timeline**            | 5-21 days             | 30-90 days                    |
| **Cost**                | No additional fees    | Chargeback fee + ratio impact |
| **Control**             | Full merchant control | Limited merchant control      |
| **Customer Experience** | Positive              | Negative                      |

<Callout icon="💡" theme="default">
  ###

  **Best Practice:** Always process refunds proactively when customers have legitimate complaints. This prevents chargebacks and maintains good customer relationships.
</Callout>

***

## Types of Refunds

### Partial Refund

A partial refund is when the refund amount is **less than** the original payment amount. Use this when:

- Customer returns only part of an order
- Partial service was delivered
- Offering goodwill discount after complaint

**Example:**

```
Original Order: ₹7,500
- Product A: ₹500
- Product B: ₹7,000

Customer returns Product A only.
Partial Refund Amount: ₹500
```

### Full Refund

A full refund is when the refund amount **equals** the original payment amount. Use this when:

- Customer cancels the entire order
- Order cannot be fulfilled
- Product/service not delivered

**Example:**

```
Original Order: ₹7,500
- Product A: ₹500
- Product B: ₹7,000

Customer returns entire order.
Full Refund Amount: ₹7,500
```

### Multiple Partial Refunds

You can issue multiple partial refunds on a single transaction until the total refunded equals the original amount.

**Example:**

```
Original Transaction: ₹10,000

Refund 1: ₹2,000 (Product A returned)
Refund 2: ₹3,000 (Product B returned)
Refund 3: ₹5,000 (Product C returned)

Total Refunded: ₹10,000 ✓
```

<Callout icon="⚠️" theme="warn">
  ### **Note:** Total refund amount cannot exceed the original transaction amount.
</Callout>

***

## Automatic Refunds

PayU automatically initiates refunds in specific scenarios where a transaction fails but the customer's account is debited.

### How It Works


<Image src="https://files.readme.io/0076248a4b081620eeb6fda5f130165772e90b5a68c74bd17b74a9c858565af2-refunds_flow.png" align="center" width="450px" />


### Enabling Automatic Refunds

Automatic refunds are **not enabled by default**. To enable:

1. Contact your PayU Key Account Manager (KAM)

Or

Send an email to [integration@payu.in](mailto:integration@payu.in)

1. Specify the transaction types you want auto-refund enabled for

### Configuration Options

| Option                                 | Description                                  |
| -------------------------------------- | -------------------------------------------- |
| **Enable for all failed transactions** | All pending/dropped transactions auto-refund |
| **Enable for specific payment modes**  | Only certain payment methods auto-refund     |
| **Threshold amount**                   | Auto-refund only above/below certain amount  |
| **Exclude specific MIDs**              | Disable for certain merchant IDs             |

***

## Refund Eligibility

### When Customers Are Eligible

A customer is eligible for a refund when:

✅ Payment was successfully captured (status: `success`)<br />✅ Customer did not receive the expected goods/services<br />✅ Product was returned as per return policy<br />✅ Service was cancelled within cancellation window<br />✅ Duplicate payment was made<br />✅ Incorrect amount was charged

### When Refunds Cannot Be Processed

❌ Transaction is still pending (not yet captured)<br />❌ Transaction already fully refunded<br />❌ Transaction older than refund window (varies by payment method)<br />❌ Chargeback already filed for the transaction<br />❌ Transaction was voided/reversed

***

## Refund Timelines

### Timeline by Payment Method

| Payment Method        | Refund Initiation | Customer Credit    | Total Time |
| --------------------- | ----------------- | ------------------ | ---------- |
| **Credit Card**       | Instant           | 5-7 business days  | 5-7 days   |
| **Debit Card**        | Instant           | 5-7 business days  | 5-7 days   |
| **UPI**               | Instant           | 1-3 business days  | 1-3 days   |
| **Net Banking**       | Instant           | 5-10 business days | 5-10 days  |
| **Wallets**           | Instant           | 1-2 business days  | 1-2 days   |
| **EMI (Credit Card)** | Instant           | 7-14 business days | 7-14 days  |
| **EMI (Debit Card)**  | Instant           | 7-14 business days | 7-14 days  |
| **BNPL**              | Instant           | 7-14 business days | 7-14 days  |
| **PayPal**            | Instant           | 3-5 business days  | 3-5 days   |

<Callout icon="📘" theme="info">
  ###

  **Note:** Public sector banks may take additional 2-3 business days for Net Banking refunds.
</Callout>

### Factors Affecting Refund Speed

| Factor                         | Impact                                   |
| ------------------------------ | ---------------------------------------- |
| **Bank processing time**       | Primary factor; varies by bank           |
| **Payment method**             | UPI/Wallets fastest; Net Banking slowest |
| **Weekend/Holidays**           | Adds 1-2 days                            |
| **Bank reconciliation cycles** | Some banks process weekly                |
| **International cards**        | May take 10-14 days                      |

***

## Refund Lifecycle

### Refund States

<Table>
  <thead>
    <tr>
      <th>
        State
      </th>

      <th>
        Description
      </th>

      <th>
        Next Possible States
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        **INITIATED**
      </td>

      <td>
        Refund request submitted
      </td>

      <td>
        PROCESSING, FAILED
      </td>
    </tr>

    <tr>
      <td>
        **PROCESSING**
      </td>

      <td>
        Being processed by bank
      </td>

      <td>
        SUCCESS, FAILED
      </td>
    </tr>

    <tr>
      <td>
        **SUCCESS**
      </td>

      <td>
        Refund completed
      </td>

      <td>
        - (Final)
      </td>
    </tr>

    <tr>
      <td>
        **FAILED**
      </td>

      <td>
        Refund failed
      </td>

      <td>
        INITIATED (retry)
      </td>
    </tr>

    <tr>
      <td>
        **PENDING**
      </td>

      <td>
        Awaiting bank confirmation
      </td>

      <td>
        SUCCESS, FAILED
      </td>
    </tr>
  </tbody>
</Table>

### State Flow Diagram


<Image src="https://files.readme.io/5d52f825e2b8d4a3533c6b07a103462e311cdaa1755ebefed90b6147e2f55393-refund_states.png" align="center" width="500px" />


## Refund Methods

You can process refunds through two methods:

### 1. PayU Dashboard

Best for: Low volume, manual review needed

**Steps:**

1. Log in to PayU Dashboard
2. Navigate to **Transactions**
3. Find the transaction to refund
4. Click **Actions → Refund**
5. Enter refund amount (full or partial)
6. Add refund reason (optional)
7. Click **Submit**

For detailed instructions, refer to [Refunds Dashboard](/docs/refunds-dashboard).

### 2. Refund APIs

Best for: High volume, automated systems

| API                                                                          | Purpose                  |
| ---------------------------------------------------------------------------- | ------------------------ |
| [Cancel Refund Transaction API](/docs/refund-apis#cancel-refund-transaction) | Initiate a refund        |
| [Check Refund Status API](/docs/refund-apis#check-refund-status)             | Check refund status      |
| [Get Refund Details API](/docs/refund-apis#get-refund-details)               | Get detailed refund info |

For API integration, refer to [Refund APIs](/docs/refund-apis).

***

## Settlement Impact

When you process a refund, it affects your settlements:

### How Refund Deduction Works


<Image src="https://files.readme.io/118bbf9276ddd7924ba02d33e661b2ac10a72ea9861243d3caf71adf5a25bc8e-how_settlement_works_with_example.png" align="center" width="550px" />


### Insufficient Settlement Balance

If your settlement balance is insufficient to cover refunds:

| Scenario                | What Happens                                         |
| ----------------------- | ---------------------------------------------------- |
| **Partial coverage**    | Available amount deducted; remainder carried forward |
| **No balance**          | Refund queued; deducted from next settlement         |
| **Persistent negative** | PayU may request bank transfer to cover refunds      |

### Viewing Refunds in Settlement Reports

Refunds appear in your settlement reports with:

- Original transaction ID
- Refund request ID
- Refund amount
- Deduction date

## Refund Constraints

### Amount Limits

| Constraint           | Rule                                 |
| -------------------- | ------------------------------------ |
| **Minimum refund**   | ₹1.00                                |
| **Maximum refund**   | Original transaction amount          |
| **Cumulative limit** | Sum of all refunds ≤ Original amount |

### Time Limits

| Payment Method  | Refund Window                          |
| --------------- | -------------------------------------- |
| **Credit Card** | Up to 180 days                         |
| **Debit Card**  | Up to 180 days                         |
| **UPI**         | Up to 90 days                          |
| **Net Banking** | Up to 180 days                         |
| **Wallets**     | Up to 90 days                          |
| **EMI**         | Up to 180 days                         |
| **BNPL**        | Varies by provider (typically 90 days) |

<Callout icon="⚠️" theme="warn">
  ### **Note:** Refunds requested after the window may require manual intervention. Contact PayU support.
</Callout>

### Transaction Status Requirements

| Transaction Status | Refund Allowed               |
| ------------------ | ---------------------------- |
| `success`          | ✅ Yes                        |
| `captured`         | ✅ Yes                        |
| `pending`          | ❌ No (wait for final status) |
| `failed`           | ❌ No (no amount captured)    |
| `dropped`          | ❌ No (auto-refund may apply) |
| `bounced`          | ❌ No                         |

***

## Refund Notifications

### Customer Notifications

When a refund is processed, customers receive:

1. **Email notification** from PayU
   - Refund amount
   - Original transaction details
   - Expected credit timeline
   - Reference number

2. **SMS notification** (if enabled)
   - Short confirmation message
   - Refund amount

### Merchant Notifications

You can receive refund status updates via:

1. **Webhooks** (recommended)
2. **Email notifications**
3. **Dashboard alerts**

For webhook setup, refer to [Webhooks for Refunds](/docs/webhooks-for-refunds).

***

## Best Practices

### Do's ✅

- Process refunds promptly (within 24-48 hours of request)
- Communicate expected timeline to customers
- Keep records of refund reasons
- Use webhooks for real-time status updates
- Publish clear refund policy on your website

### Don'ts ❌

- Don't delay refunds hoping customer will forget
- Don't process refund for pending transactions
- Don't refund more than original amount
- Don't ignore failed refund notifications
- Don't promise instant refunds (timelines vary)

***

## Publish Your Refund Policy

PayU recommends publishing a clear refund policy on your website. Include:

```
RECOMMENDED REFUND POLICY ELEMENTS
──────────────────────────────────

✓ Refund eligibility criteria
✓ Refund request process (how to request)
✓ Required information (order ID, reason)
✓ Refund timeline by payment method
✓ Partial refund conditions
✓ Non-refundable items/services (if any)
✓ Contact information for refund queries
✓ Policy for failed transaction refunds
```

***

## Next Steps

| Topic                                              | Description                   |
| -------------------------------------------------- | ----------------------------- |
| [Refunds Dashboard](/docs/refunds-dashboard)       | Process refunds via Dashboard |
| [Refund APIs](/docs/refund-apis)                   | API integration guide         |
| [Webhooks for Refunds](/docs/webhooks-for-refunds) | Real-time notifications       |
| [Refunds for EMI](/docs/refunds-for-emi)           | EMI-specific refund handling  |
| [Refunds for BNPL](/docs/refunds-for-bnpl)         | BNPL-specific refund handling |

***

## FAQs

### How long does a refund take?

Refund timelines vary by payment method:

- **UPI/Wallets:** 1-3 business days
- **Cards:** 5-7 business days
- **Net Banking:** 5-10 business days
- **EMI/BNPL:** 7-14 business days

### Can I cancel a refund after initiating?

No, once a refund is initiated, it cannot be cancelled. Ensure you verify details before processing.

### Why did my refund fail?

Common reasons:

- Customer's account is closed
- Bank rejected the refund
- Invalid account details
- Timeout during processing

Contact PayU support with the refund ID for specific failure reasons.

### Can I refund to a different account?

No, refunds are always processed to the original payment source. This is a regulatory requirement.

### What happens to TDR/MDR on refunded transactions?

Transaction fees (TDR/MDR) on refunded transactions may or may not be reversed depending on your agreement. Contact your KAM for details.

### How do I handle refunds for split settlement transactions?

For split settlements, refunds follow specific rules. Refer to [Refund APIs for Split Settlements](/docs/refund-apis-for-split-settlements).

***

_Last updated: December 2024_
