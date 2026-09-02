---
title: '[Internal Review] Payment Retries'
deprecated: false
hidden: true
metadata:
  robots: index
---
## What is Payment Retry?

Payment retry is an automated mechanism that attempts to re-process failed recurring payment transactions for subscriptions (Standing Instructions). When a scheduled recurring payment fails, the retry system automatically attempts the payment again at configured intervals, improving the chances of successful collection.

***

## Why Use Payment Retries?

Failed recurring payments are a common challenge for subscription-based businesses. Payment retries help merchants:

<Tabs>
  <Tab title="Revenue Recovery" icon="fa-solid fa-money-bill-trend-up">
    - Recover revenue from failed transactions that would otherwise be lost
    - Increase successful payment collection rates by 15-30% on average
    - Reduce revenue churn from temporary payment failures
  </Tab>

  <Tab title="Common Payment Failure Scenarios" icon="fa-solid fa-triangle-exclamation">
    - Customer's card has expired

    - Insufficient balance at the time of debit

    - Temporary bank system issues or downtime

    - Card blocked by bank for security reasons

    - Network connectivity issues during transaction
  </Tab>

  <Tab title="Operational Efficiency" icon="fa-solid fa-gears">
    - Automate re-attempts instead of manual follow-up

    - Reduce support team workload handling failed payment queries

    - Minimize customer intervention for temporary issues
  </Tab>

  <Tab title="Better Customer Experience" icon="fa-solid fa-face-smile">
    - Seamless subscription continuity without manual customer action

    - Reduced service interruptions from temporary payment issues

    - Proactive resolution before customers notice the problem
  </Tab>
</Tabs>

***

## How to Configure Retries

PayU provides two approaches to configure payment retries for subscription transactions:

### Smart Retry (PayU Managed)

<Callout icon="🤖" theme="info">
  ### **Note**

  Verify with PayU Support or your Key Account Manager if Smart Retry is available for your merchant account.
</Callout>

Smart Retry is fully controlled by PayU using machine learning and historical transaction data. PayU automatically:

- Decides the optimal time to retry based on success patterns
- Determines how many attempts to make
- Adjusts retry strategy based on failure reason

**When to use:** Merchants who want a hands-off approach with PayU-optimized retry logic.

***

### Custom Retry (Merchant Configured)

Custom Retry gives you complete control over retry configuration. You can define:

- **Number of retries:** Up to 7 retry attempts per subscription cycle
- **Retry intervals:** Minutes, hours, or days between attempts
- **Applicable subscription cycles:** Daily, Weekly, Monthly, Yearly, Once, or Adhoc
- **Post-retry action:** What happens after all retries fail (Unpaid or Cancelled)
- **Weekend exclusion:** Skip retry attempts on Saturdays and Sundays

**When to use:** Merchants who need specific retry timing aligned with their business logic or customer payment patterns.

***

## Common Payment Failure Reasons

Understanding why payments fail helps you configure appropriate retry strategies:

| Failure Reason           | Description                                                         | Retry Recommended?                                      |
| ------------------------ | ------------------------------------------------------------------- | ------------------------------------------------------- |
| **Card Expired**         | Customer's payment card has crossed expiry date                     | ❌ No - Customer needs to update payment method          |
| **Insufficient Balance** | Customer's account doesn't have enough funds                        | ✅ Yes - Balance may be available later                  |
| **Card Blocked by Bank** | Issuing bank has blocked the card for security or other reasons     | ⚠️ Conditional - May resolve if temporary security hold |
| **Mandate Cancelled**    | Customer has cancelled the mandate from their bank/app              | ❌ No - Customer action required to reinstate            |
| **Technical Failure**    | Network issues, gateway timeout, or temporary system unavailability | ✅ Yes - Usually resolves automatically                  |

<Callout icon="👍" theme="success">
  ### **Best Practice**

  Configure 2-3 retry attempts with 24-48 hour intervals for temporary failures like insufficient balance or technical issues.
</Callout>

***

## Navigate to Retry Settings

To access the retry configuration page:

1. Log in to the <Anchor target="_blank" href="https://onboarding.payu.in/app/account/signin">PayU Dashboard.</Anchor>
2. Navigate to **Subscriptions** from the left sidebar.
3. Click **Revenue Recovery.**


<Image src="https://files.readme.io/e0c4066c46015cd568fcf6dea4131e54aa506aac522d9efc5cbda72f1fc655b1-revenue-recovery-retry-settings.gif" align="center" caption="_Navigate to Revenue Recovery_" border={true} />


<Callout icon="⚠️" theme="warning">
  ### **Default State: Retry Disabled**

  By default, payment retry is **disabled** on your merchant account. Failed subscription transactions will not be automatically retried until you configure and enable a retry strategy below.
</Callout>

***

## Configure Retry Strategy

Follow these steps to configure your retry strategy:

### Step 1: Choose Retry Type

Select one of the following retry types:

<Accordion title="Smart Retry (Recommended for most merchants)" icon="fa-magic">
  Select this option to let PayU automatically manage retry timing and frequency based on machine learning models trained on historical payment data.

  **Configuration:** None required - PayU handles everything automatically.
</Accordion>

<Accordion title="Custom Retry (Advanced)" icon="fa-sliders">
  Configure your own retry logic with complete control over timing, frequency, and post-failure actions.

  **Configuration Steps:**

  1. **Select Subscription Cycles:** Choose which subscription types this retry configuration applies to:
     - All Subscriptions (applies to Daily, Weekly, Monthly, Yearly, Once, Adhoc)
     - Specific cycles only (e.g., Monthly and Yearly only)

  2. **Define Retry Attempts:** Configure up to 7 retry attempts:
     - **Retry Interval:** Time between attempts (in Minutes, Hours, or Days)
     - **Time Window:** Start time and end time for retry attempts (12-hour format with AM/PM)
     - **Example:** First retry after 24 hours, second after 48 hours, third after 72 hours

  3. **Configure Post-Retry Action:** Define what happens when all retry attempts fail:

     | Action               | Impact on Subscription                         | Impact on Mandate      | When to Use                                          |
     | -------------------- | ---------------------------------------------- | ---------------------- | ---------------------------------------------------- |
     | **Unpaid** (Default) | Subscription stays active but marked as unpaid | Mandate remains active | Temporary failures - give customer time to resolve   |
     | **Cancelled**        | Subscription automatically cancelled           | **Mandate is revoked** | Permanent failures - clean up inactive subscriptions |

     <Callout icon="⚠️" theme="warning">
       ### **Important**

       The **Cancelled** action is **not supported** for AMEX and RUPAY cards. Use **Unpaid** for these card types.
     </Callout>

  4. **Weekend Handling:** Enable **Skip weekends** to prevent retry attempts on Saturdays and Sundays.

  5. **Save Configuration:** Click **Update** to apply retry settings to your merchant account.


     <Image src="https://files.readme.io/d2ed1e95a18d547a3a650e08a38b7fc524b9aa0a0a38452666aeedc7ccf374d7-payment-retry.gif" align="center" caption="Configure Custom Retry Settings" border={true} />

</Accordion>

### Step 2: Verify Configuration

After saving, your retry settings are applied immediately to all future failed subscription transactions. Existing failed transactions are not retroactively retried.

***

## Field Validations

The **Retry Configuration** page validates each field before saving. Use the following reference when configuring Custom Retry settings:

<Callout icon="📘" theme="info">
  ### **Technical Validation**

  Field specifications have been verified against PayU's retry management system. For the latest validation rules, contact PayU Support or refer to internal documentation.
</Callout>

| Column Name                                      | Field Type                          | Validation / Allowed Values                                                                                                          |
| ------------------------------------------------ | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Retry Preference (`retryType`)                   | Mandatory                           | Allowed values: `SMART`, `CUSTOM`, `NO_RETRY`                                                                                        |
| Max Retry Action (`retryActionOnMax`)            | Mandatory                           | Allowed values: `UNPAID`, `CANCEL`. <br /><br />**Note:** Not supported for AMEX and RUPAY cards.                                    |
| Skip Weekends (`skipWeekends`)                   | Optional                            | —                                                                                                                                    |
| Custom Toggle (when Retry Preference = `CUSTOM`) | Mandatory when `CUSTOM`             | `BY_INTERVAL` or `SPECIFIC_DATES`. <br /><br />**Note:** Specific Dates feature coming soon.                                         |
| Subscription Types (`selectedSubscriptionTypes`) | Mandatory when `CUSTOM`             | At least one required. Allowed values: `DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`, `ONCE`, `ADHOC`. Option to select All Subscriptions.  |
| Interval Value (`intervalValue`)                 | Mandatory when `CUSTOM BY_INTERVAL` | Positive integers only. Required for each retry row.                                                                                 |
| Interval Unit (`intervalUnit`)                   | Mandatory when `CUSTOM BY_INTERVAL` | Allowed values: `HOURS`, `MINUTES`, `DAYS`                                                                                           |
| Start Time (`startTime`)                         | Mandatory                           | 12-hour format with AM/PM. If Start Time is set, End Time is required.                                                               |
| End Time (`endTime`)                             | Mandatory                           | 12-hour format with AM/PM. If End Time is set, Start Time is required. End must be after Start. Example: Start = 11 PM → End = 12 AM |
| Max Number of Retries                            | Mandatory                           | Maximum **7 retries** per subscription type                                                                                          |

***

## Frequently Asked Questions

1. #### What is the difference between Smart Retry and Custom Retry?
   <Accordion title="Answer" icon="fa-comment-dots">
     **Smart Retry:** PayU-managed approach using machine learning to automatically determine optimal retry timing and frequency based on historical transaction data. No configuration required.

     **Custom Retry:** Merchant-configured approach where you define the exact number of retries, intervals between attempts, applicable subscription cycles, and post-failure actions.

     **Recommendation:** Use Smart Retry for hands-off optimization, or Custom Retry if you need specific retry timing for business reasons (e.g., align with customer salary dates).
   </Accordion>

2. #### How many retry attempts can I configure?
   <Accordion title="Answer" icon="fa-comment-dots">
     With Custom Retry, you can configure up to **7 retry attempts** per subscription cycle. Each retry can have different intervals (minutes, hours, or days) and time windows.
   </Accordion>

3. #### What happens when all retry attempts fail?
   <Accordion title="Answer" icon="fa-comment-dots">
     You choose the post-retry action when configuring Custom Retry:

     - **Unpaid (Default):** Subscription remains active but marked as unpaid. Mandate stays active. Customer can still manually pay or resolve the issue.
     - **Cancelled:** Subscription is automatically cancelled and **mandate is revoked**. Customer must re-register to resume subscription.

     **Note:** Cancelled action is not available for AMEX and RUPAY cards.
   </Accordion>

4. #### Can I skip retry attempts on weekends?
   <Accordion title="Answer" icon="fa-comment-dots">
     Yes. When configuring Custom Retry, enable the **Skip weekends** option to prevent retry attempts on Saturdays and Sundays. This setting applies to all retry attempts in your configuration.
   </Accordion>

5. #### When do retry settings take effect?
   <Accordion title="Answer" icon="fa-comment-dots">
     Retry settings are applied **immediately** after you click Update. The settings apply to all future failed subscription transactions. Existing failed transactions are not retroactively retried.
   </Accordion>

6. #### Does cancelling a subscription after retry failure revoke the mandate?
   <Accordion title="Answer" icon="fa-comment-dots">
     Yes. When you select **Cancelled** as the post-retry action, both the subscription is cancelled AND the customer's mandate is revoked with the bank/payment provider. The customer will need to create a new mandate if they want to re-subscribe.
   </Accordion>

7. #### Can I configure different retry strategies for different subscription cycles?
   <Accordion title="Answer" icon="fa-comment-dots">
     Yes. When configuring Custom Retry, you can select specific subscription cycles (Daily, Weekly, Monthly, Yearly, Once, Adhoc) and define different retry configurations for each. For example, you might retry Monthly subscriptions 3 times but Daily subscriptions only once.
   </Accordion>
