---
title: '[Internal Review] Payment Retries'
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Subscription Retry Settings** feature on the PayU Dashboard introduces an advanced and flexible retry mechanism for Subscription (SI) transactions. It helps improve payment success rates by enabling more effective handling of failed recurring transactions.

This page covers the following sections:

- Overview
- Access Retry Settings
- Retry Options Available
- Types of Retry Systems
- Configure Custom Retry
- Post-Retry Behavior
- Additional Preferences
- Field Validations
- Save Configuration

## Overview

Subscription Retry Settings give merchants greater control over how failed SI transactions are retried. Key benefits include:

- Choose and configure retry strategies based on your business needs
- Greater control and flexibility compared to traditional retry approaches
- Improved revenue recovery through higher payment success rates
- A smoother and more reliable experience for your customers

## Access Retry Settings

To access retry settings on the PayU Dashboard:

1. Log in to the **PayU Dashboard**.
2. Navigate to the **Revenue Recovery** tab from the side panel.

## Retry Options Available

Once inside the **Revenue Recovery** tab, you can view and configure the available retry options.

### Default State

By default, **Retry is Disabled**. No retry attempts are made unless you explicitly configure a retry strategy.

## Types of Retry Systems

PayU supports two retry modes for subscription transactions.

### Smart Retry (PayU Managed)

Smart Retry is fully controlled by PayU and requires no manual configuration. PayU uses historical data and intelligence to:

- Decide **when to retry**
- Decide **how often to retry**

### Custom Retry (Merchant Configured)

Custom Retry is fully configurable by the merchant. You can define:

- Number of retries
- Retry intervals
- Applicable subscription cycles

## Configure Custom Retry

When you select **Custom Retry**, you can configure the following settings.

### Scope of Retry

You can configure retries for:

- **All subscription cycles**
- **Specific billing cycles**

### Adding Retry Attempts

Use the **Add** button to configure multiple retry attempts.

Each retry attempt can have:

- Different timing
- Different conditions

### Retry Intervals

For each retry attempt, choose from the following interval options:

- **Minute Wise**
- **Hour Wise**
- **Day Wise**

### Billing Cycle-Level Configuration

If required, you can:

- Define retry logic per billing cycle
- Customize retry behavior differently for each cycle

## Post-Retry Behavior

Once all configured retries are exhausted, you can define the outcome using **Max Retry Action**.

### Options Available

| Option               | Description                                           |
| -------------------- | ----------------------------------------------------- |
| **Unpaid (Default)** | The subscription remains active but marked as unpaid. |
| **Cancelled**        | The subscription is automatically cancelled.          |

> 📘
>
> **Note:** The **Cancelled** post-retry action is not supported for AMEX and RUPAY cards.

## Additional Preferences

### Skip Weekends Option

You can enable **Skip retry attempts on weekends** to prevent retries from being triggered on Saturdays and Sundays. This preference applies across all retry configurations.

## Field Validations

The Retry Management page validates each field before you save. Use the following reference when configuring retry settings.

| Column Name                                      | Field Type                          | Validation / Allowed Values                                                                                                              |
| ------------------------------------------------ | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Retry Preference (`retryType`)                   | Mandatory                           | Allowed values: `SMART`, `CUSTOM`, `NO_RETRY`                                                                                            |
| Max Retry Action (`retryActionOnMax`)            | Mandatory                           | Allowed values: `UNPAID`, `CANCEL`. **Note:** Not supported for AMEX and RUPAY cards.                                                    |
| Skip Weekends (`skipWeekends`)                   | Optional                            | —                                                                                                                                        |
| Custom Toggle (when Retry Preference = `CUSTOM`) | Mandatory when `CUSTOM`             | `BY_INTERVAL` or `SPECIFIC_DATES`. **Note:** Specific Dates feature coming soon.                                                         |
| Subscription Types (`selectedSubscriptionTypes`) | Mandatory when `CUSTOM`             | At least one required. Allowed values: `DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`, `ONCE`, `ADHOC`. Option to select **All Subscriptions**.  |
| Interval Value (`intervalValue`)                 | Mandatory when `CUSTOM BY_INTERVAL` | Positive integers only. Required for each retry row.                                                                                     |
| Interval Unit (`intervalUnit`)                   | Mandatory when `CUSTOM BY_INTERVAL` | Allowed values: `HOURS`, `MINUTES`, `DAYS`                                                                                               |
| Start Time (`startTime`)                         | Mandatory                           | 12-hour format with AM/PM. If Start Time is set, End Time is required.                                                                   |
| End Time (`endTime`)                             | Mandatory                           | 12-hour format with AM/PM. If End Time is set, Start Time is required. End must be **after** Start. Example: Start = 11 PM → End = 12 AM |
| Max Number of Retries                            | Mandatory                           | Maximum **7 retries** per subscription type                                                                                              |

## Save Configuration

Once all retry configurations are set as per your requirements:

1. Click **Update** to save your changes.
2. All configured retry settings are applied to your merchant account.

> 📘 **Reference**&#x20;
>
> Retry settings apply to subscription (SI) transactions on your merchant account. For mandate and transaction details, refer to Access Subscription Mandates.

<br />
