---
title: '[Internal Review] Payment Retries'
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Subscription Retry Settings** feature on the PayU Dashboard introduces an advanced and flexible retry mechanism for Subscription (SI) transactions. It helps improve payment success rates by enabling more effective handling of failed recurring transactions. The following are the available retry types:

**Smart Retry (PayU Managed)**

Smart Retry is fully controlled by PayU and requires no manual configuration. PayU uses historical data and intelligence to:

- Decide when to retry
- Decide how often to retry

**Custom Retry (Merchant Configured)**

Custom Retry is fully configurable by the merchant. You can define:

- Number of retries
- Retry intervals
- Applicable subscription cycles
- Action to be taken after retries are exhausted
- To skip weekends

<Accordion title="Benefits" icon="fa-gift">
* Enables merchants to configure payment retry strategies that align with their business requirements and customer journeys.
* Provides greater flexibility and control over retry logic compared to conventional retry mechanisms.
* Improves revenue recovery by increasing the likelihood of successful payment collection on subsequent attempts.
* Delivers a seamless and reliable payment experience, reducing customer friction caused by failed transactions.
</Accordion>

## Payment Failure Reasons

Below are the reasons for payment failures:

<Accordion title="Reasons" icon="fa-list">
* Customer card has expired.
* The bank has blocked the customer card.
* The customer's account has insufficient balance.
* The customer has cancelled the mandate from their end.
</Accordion>

## Access Retry Settings

You can access retry settings under **Subscriptions&#x20;**&#x66;rom the left navigation as shown below.


<Image src="https://files.readme.io/e0c4066c46015cd568fcf6dea4131e54aa506aac522d9efc5cbda72f1fc655b1-revenue-recovery-retry-settings.gif" align="center" caption="_Access Retry Settings_" border={true} framed={true} />


<br />

> ⚠️ Watch out!
>
> By default, payment retry is disabled in the dashboard. No retry attempts are made unless you define a retry strategy.

## Configure Payment Retries

To configure payment retries:

<Accordion title="Step 1: Log in to the PayU Dashboard" icon="fa-right-to-bracket">
Log in to the <Anchor target="_blank" href="https://payu.in/">dashboard,</Anchor> expand **Subscriptions** and click **Revenue Recovery** from the left menu.

<Image src="https://files.readme.io/d80f28822870a7b6d160553f447a4f06b421a2f4acd175cad872fb060457be1d-image.png" align="center" caption="_Access Revenue Recovery_" border={true} framed={true} />
</Accordion>

<Accordion title="Step 2: Define Payment Retry" icon="fa-sliders">
1. Select either of the retry type. The following are the available options:
* **Smart Retry:** Select this option if you want PayU to control the payment retry with no manual configuration. PayU uses historical data and intelligence to decide when and how often to retry.
* **Custom:** Perform the following steps to define the payment retry:
  1. 
</Accordion>

### Options Available

| Option               | Description                                           |
| -------------------- | ----------------------------------------------------- |
| **Unpaid (Default)** | The subscription remains active but marked as unpaid. |
| **Cancelled**        | The subscription is automatically cancelled.          |

> 📘 **Note:**&#x20;
>
> The **Cancelled** post-retry action is not supported for AMEX and RUPAY cards.

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

## FAQs

### Where do I configure subscription retry settings?

Log in to the PayU Dashboard and open the **Revenue Recovery** tab from the side panel.

### Is retry enabled by default?

No. By default, **Retry is Disabled**. Failed subscription transactions are not retried until you enable Smart Retry or Custom Retry and click **Update**.

### What is the difference between Smart Retry and Custom Retry?

**Smart Retry** is managed by PayU. PayU decides when and how often to retry based on historical data—no manual setup required.

**Custom Retry** lets you configure the number of retries, intervals (minutes, hours, or days), and which subscription cycles the settings apply to.

### How many retry attempts can I configure?

You can configure a maximum of **7 retries** per subscription type when using Custom Retry.

### What happens after all retry attempts fail?

You choose the outcome using **Max Retry Action**:

- **Unpaid (default):** The subscription stays active but is marked unpaid.
- **Cancelled:** The subscription is automatically cancelled.

### Can I skip retries on weekends?

Yes. Enable **Skip retry attempts on weekends** to avoid retries on Saturdays and Sundays. This applies to all retry configurations.

### Is the Cancelled option available for all payment methods?

No. The **Cancelled** post-retry action is not supported for **AMEX** and **RUPAY** cards.

### When do my retry settings take effect?

After you configure your preferences, click **Update**. The settings are applied to your merchant account immediately.
