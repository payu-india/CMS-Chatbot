---
title: MCP Tools
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Available Tools
deprecated: false
hidden: false
metadata:
  title: Remote MCP for Merchants - Available Tools
  keywords:
    - MCP Tools
    - Transaction Tools
    - Payment Tools
    - Report Tools
  robots: index
---

PayU Remote MCP provides access to multiple merchant services through specialized tools. The available tools depend on your account permissions and service configuration.

## Tool Categories

The service provides tools in three main categories:

* **Transactions** - View and manage transaction data
* **Payments** - Process payment operations
* **Reports** - Generate and download reports

## Transactions

Tools for viewing and managing transaction data.

### View Transaction History

Access historical transaction data with filtering options.

| Capability           | Description                                |
| -------------------- | ------------------------------------------ |
| Date range filtering | Filter transactions by start and end dates |
| Status filtering     | Filter by success, failed, pending status  |
| Amount filtering     | Filter by transaction amount range         |
| Pagination           | Handle large result sets efficiently       |

**Example Queries:**

```
"Show me transactions for the last 7 days"
"List failed transactions from January"
"Show transactions over ₹10,000"
```

### Get Transaction Details

Retrieve comprehensive information for specific transactions.

| Capability            | Description                             |
| --------------------- | --------------------------------------- |
| Transaction ID lookup | Find transaction by PayU transaction ID |
| Order ID lookup       | Find transaction by merchant order ID   |
| Complete details      | Access all transaction metadata         |

**Example Queries:**

```
"Get details for transaction TX-98765"
"Show complete information for order ORD-2026-001"
```

### Generate Transaction Reports

Create custom reports for analysis and record-keeping.

| Capability         | Description                             |
| ------------------ | --------------------------------------- |
| Custom date ranges | Specify exact date ranges for reports   |
| Format options     | Export as CSV, PDF, or other formats    |
| Filtered reports   | Include only specific transaction types |

**Example Queries:**

```
"Generate a transaction report for January 2026"
"Download CSV of all successful transactions this week"
```

## Payments

Tools for processing payment operations.

### Process Refunds

Initiate refund requests for completed transactions.

| Capability      | Description                            |
| --------------- | -------------------------------------- |
| Full refunds    | Refund the complete transaction amount |
| Partial refunds | Refund a specific amount               |
| Refund tracking | Track refund status and completion     |

**Example Queries:**

```
"Process a refund for transaction TX-12345"
"Initiate partial refund of ₹500 for TX-98765"
```

> ⚠️ Important
>
> Refund operations are irreversible. Ensure you have selected the correct merchant account and transaction before processing refunds.

### Check Payment Status

View real-time status of payments.

| Capability       | Description                                |
| ---------------- | ------------------------------------------ |
| Real-time status | Get current payment state                  |
| Status history   | View status changes over time              |
| Failure details  | Access failure reasons for failed payments |

**Example Queries:**

```
"Check status of payment PAY-12345"
"Is the payment for order ORD-2026-001 complete?"
```

### View Settlement Information

Access settlement details and history.

| Capability          | Description                        |
| ------------------- | ---------------------------------- |
| Settlement status   | Check if settlements are processed |
| Settlement amounts  | View amounts and deductions        |
| Settlement schedule | See upcoming settlement dates      |

**Example Queries:**

```
"Check status of settlement S-567890"
"Show today's settlement details"
```

## Reports

Tools for generating and downloading reports.

### Generate Custom Reports

Create tailored reports for your business needs.

| Capability          | Description                         |
| ------------------- | ----------------------------------- |
| Transaction reports | Detailed transaction data exports   |
| Settlement reports  | Settlement summaries and breakdowns |
| Analytics reports   | Business insights and trends        |

**Example Queries:**

```
"Generate a monthly transaction summary"
"Create a report of payment methods used"
```

### Download Transaction Data

Export transaction data in various formats.

| Capability   | Description                          |
| ------------ | ------------------------------------ |
| CSV export   | Comma-separated values format        |
| PDF export   | Formatted PDF documents              |
| Excel export | Spreadsheet format (where available) |

**Example Queries:**

```
"Download transaction data for this month as CSV"
"Export settlement report as PDF"
```

### View Analytics

Access business analytics and insights.

| Capability               | Description                       |
| ------------------------ | --------------------------------- |
| Success rates            | Transaction success/failure rates |
| Payment method breakdown | Usage by payment type             |
| Volume trends            | Transaction volume over time      |

**Example Queries:**

```
"Show transaction success rate for this month"
"What payment methods are most used?"
```

## Tool Availability

<Callout icon="📘" theme="info">
  **Note**: Actual available tools depend on your account permissions and service configuration. Some tools may require additional permissions or may not be available for all merchant accounts.
</Callout>

### Checking Available Tools

To see which tools are available for your account:

```
"What tools do I have access to?"
"List available capabilities"
```

### Permission Requirements

| Tool Category           | Typical Permission         |
| ----------------------- | -------------------------- |
| View Transactions       | Basic merchant access      |
| Get Transaction Details | Basic merchant access      |
| Process Refunds         | Refund permission required |
| Generate Reports        | Reporting permission       |
| View Settlements        | Settlement access          |

<br />
