---
title: Plan Management
deprecated: false
hidden: true
metadata:
  robots: index
---
A plan defines the subscription terms that the customer accepts before a Standing Instruction (SI) mandate is registered. In API-based SI integrations, the plan is managed by your system and shared with PayU during the consent transaction through `si_details`.

PayU does not require you to create a separate plan object before registering an SI mandate. Your frontend should maintain the plan configuration, show it to the customer, pass the approved values to PayU during consent, and use the returned mandate identifiers for future pre-debit notifications, recurring debits, and mandate management.

You can create a plan:

- From PayU dashboard.
- Using APIs.

> 📘 **Handy Tips**
>
> - Creating a plan is optional. You can create a subscription without creating a plan.
> - You can create multiple subscriptions for a plan.

## Prerequisites

- Enable Subscriptions for your PayU merchant account. Contact your PayU Key Account Manager or onboarding team before integrating SI plans.

## Benefits of a Plan

Using a plan gives merchants a structured way to manage SI subscriptions.

<Accordion title="Plan Benefits" icon="fa-list-check">
<ul><li><strong>Clear customer consent:</strong> The customer sees the amount, frequency, start date, and end date before approving the mandate.</li>
<li><strong>Consistent billing schedule:</strong> Your system can calculate upcoming debit dates from the plan instead of relying on manual inputs for every cycle.</li>
<li><strong>Easier pre-debit management:</strong> The plan provides the amount and due date needed to trigger pre-debit notifications on time.</li>
<li><strong>Faster recurring payment operations:</strong> Merchants can trigger debits from a saved plan and mandate mapping instead of recreating payment details.</li>
<li><strong>Better dashboard controls:</strong> The frontend can show plan status, next debit date, last debit status, and allowed actions in one place.</li>
<li><strong>Improved reconciliation:</strong> Plan ID or merchant reference, mandate ID, invoice number, and transaction IDs can be mapped together for reports.</li>
<li><strong>Safer modifications and cancellations:</strong> Merchants can separate draft edits from active mandate changes and use the correct PayU APIs for supported updates.</li>
<li><strong>Reusable subscription setup:</strong> Common plan templates can reduce errors when merchants create similar subscriptions for multiple customers.</li>
<li><strong>Better customer support:</strong> Support teams can quickly see what the customer approved, when the next charge is due, and why a debit succeeded or failed.</li></ul>

</Accordion>

## Plan Status

Every plan goes through the following statuses:

<Cards>
  <Card title="Draft" icon="fa-file-pen" iconColor="#0c6150">
    Plans are saved in the system but not active. You cannot use draft plans for subscriptions until they are activated.
  </Card>

  <Card title="Active" icon="fa-circle-check" iconColor="#0c6150">
    A plan becomes active once it is created and immediately available for creating subscriptions.
  </Card>
</Cards>

## Access Plans

You can access **Plans** under **Subscriptions&#x20;**&#x66;rom the left navigation as shown below.


<Image src="https://files.readme.io/ceab99a98c18eb24f14d434f5159d4a6ae066d810e940e9f32828515fee74cc7-plan-management.gif" alt="Access Plans" align="center" caption="_Access Plans_" border={true} />


## Dashboard Actions

- Create a plan
- Duplicate a plan
- Edit a plan
- Deactivate a plan
- Create a Subscription

# Frequently Asked Questions (FAQs)

Find answers to frequently asked questions about SI plans.

### SI Plan Basics

1. #### What is an SI plan?
   <Accordion title="Answer" icon="fa-comment-dots">
   An SI Plan is the billing schedule and amount that your customer agrees to before a Standing Instruction mandate is registered. In this API-based flow, the plan is maintained in your system and passed to PayU as `si_details` during consent.<br/>
   <strong>Best Practice:</strong> Keep a unique merchant-side plan reference so support, reconciliation, and retries can be traced back to the exact plan shown to the customer
   </Accordion>
2. #### When should I create a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
   Create the plan before initiating consent, after the customer has selected the subscription terms but before calling the consent transaction API.<br/>
   **Best Practice:** Move a plan from Draft to activate only when the exact amount, frequency, start date, end date, and customer details are frozen for the consent attempt.
   </Accordion>
3. #### What is the difference between a plan and a mandate?
   <Accordion title="Answer" icon="fa-comment-dots">
   A plan is your business configuration for what to charge and when. A mandate is the customer's authorized payment instruction created after successful consent through PayU and the issuer/payment ecosystem.<br/>
   <blockquote class="callout callout_info" theme="📘">
     <h3>📘 Handy Tips</h3>
     <p>Your plan can exist before consent. The mandate exists only after successful registration.</p>
   </blockquote>
   </Accordion>
4. #### Can a customer have multiple plans?
   <Accordion title="Answer" icon="fa-comment-dots">
   Yes, your system can maintain multiple plans for a customer. Each plan should have its own merchant reference and should be mapped to the correct mandate and debit schedule.<br/>
   <blockquote class="callout callout_info" theme="📘">
     <h3>📘 Handy Tips</h3>
     <p>Avoid reusing the same merchant transaction ID or invoice number across plans.</p>
   </blockquote>
   </Accordion>
5. #### Is plan status the same as mandate status?
   <Accordion title="Answer" icon="fa-comment-dots">
   No. Plan status is usually merchant-managed, such as **Draft** or **Active**. Mandate status is returned by PayU or the payment ecosystem and indicates whether debits are allowed.
   </Accordion>
6. #### How does billing cycle behavior work?
   <Accordion title="Answer" icon="fa-comment-dots">
   `billingCycle` defines the unit, such as DAILY, WEEKLY, MONTHLY, or YEARLY. `billingInterval` defines how many units must pass between debits.<br/>
   <blockquote class="callout callout_info" theme="📘">
     <h3>📘 Example</h3>
     <p><code>billingCycle=MONTHLY</code> and <code>billingInterval=1</code> means once every month. <code>billingCycle=DAILY</code> and <code>billingInterval=3</code> means once every 3 days.</p>
   </blockquote>
   </Accordion>

### Plan Management

1. #### How should I set start date and end date?
   <Accordion title="Answer" icon="fa-comment-dots">
   Use the start date as the first date from which recurring debits may begin and the end date as the last date through which the mandate can be used.<br/>
   **Best Practice:** Do not schedule pre-debit or recurring debit attempts outside the approved start and end date range.
   </Accordion>
2. #### Can the start date be the current date?
   <Accordion title="Answer" icon="fa-comment-dots">
   It depends on payment mode and issuer rules. Even if consent completes today, subsequent recurring debits may require a pre-debit notification window before the actual charge.<br/>
   **Best Practice:** Build date validation that accounts for pre-debit lead time, especially for Cards and UPI.
   </Accordion>
3. #### Can I create duplicate plans?
   <Accordion title="Answer" icon="fa-comment-dots">
   You can duplicate a draft plan as a convenience feature, but every consent attempt should use unique transaction and invoice identifiers.
   </Accordion>

### Plan Lifecycle and Statuses

1. #### What is the difference between Draft and Active plans?
   <Accordion title="Answer" icon="fa-comment-dots">
   Draft means the plan exists only in your system and has not activated. Active means the plan is activated and ready to use.
   </Accordion>
2. #### Can I edit a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
   Yes, you can edit a plan.
   </Accordion>
3. Can i delete a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
   No, you cannot delete a plan. However, you can deactivate a plan. Once deactivated, a plan moves to the **Archived** state. You can dupliacte it to create a new plan.
   </Accordion>
4. Can I pause and resume a plan?
   <Accordion title="Answer" icon="fa-comment-dots">
     Lorem ipsum dolor sit amet, **consectetur adipiscing elit.** Ut enim
     ad minim veniam, quis nostrud exercitation ullamco. Excepteur sint
     occaecat cupidatat non proident!
   </Accordion>

#### Can I pause and resume a plan?

**Short answer:** Pause and resume are merchant-side controls unless you also modify or cancel the mandate. Pausing should stop your scheduler from sending pre-debit and recurring debit requests.

**Best Practice:** On resume, re-check mandate status before scheduling the next debit.

#### Can a Failed plan be retried?

**Short answer:** Yes, if consent failed before mandate creation, you can retry with a new transaction ID. If recurring debit failed after mandate creation, first verify mandate status and failure reason.

**Note:** Do not retry blindly. Repeated retries without checking status can create duplicate attempts or poor customer experience.

### Integration and APIs

#### What is the recommended API flow sequence?

**Short answer:** Create the plan in your system, initiate consent with `si=1` and `si_details`, store PayU identifiers after success, send pre-debit notification when due, then call the recurring payment API.

**References:** [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted), [Pre-Debit Notification API](ref:pre_debit_notification_api), and [Recurring Payment Transaction API](ref:recurring_payment_api).

#### Do I need to call PayU when creating a Draft plan?

**Short answer:** No. Draft plan creation is a merchant-side action. PayU is called when you initiate consent, check mandate status, send pre-debit, debit the customer, or manage the mandate.

#### How should I generate the hash for consent?

**Short answer:** Generate the hash exactly as required by the consent API and include `si_details` in the hash sequence where applicable.

**Best Practice:** Use the exact string sent in the request for hash generation. Changes in JSON formatting, field order, escaping, or values after hash generation can cause hash mismatch.

#### What should I expect from callbacks or webhooks?

**Short answer:** The consent response or redirect tells you the result of the registration attempt. Webhooks or status APIs should be used to update asynchronous payment and recurring debit outcomes.

**Best Practice:** Treat callbacks and webhooks as status signals, but always make status updates idempotent because notifications can be delayed or repeated.

#### Should I use Verify Payment API after consent?

**Short answer:** Yes, especially when the customer journey is interrupted, the browser closes, or your success/failure URL is not reached.

**Reference:** Use [Verify Payment API](ref:verify_payment_api) to confirm final payment status.

#### How should I test in sandbox?

**Short answer:** Test successful consent, failed consent, invalid hash, duplicate transaction ID, pre-debit success, recurring debit success, recurring debit failure, mandate cancellation, and status verification.

**Best Practice:** Maintain test cases for every payment mode you plan to support in production.

#### How should I handle idempotency and retries?

**Short answer:** Use unique merchant transaction IDs for new attempts and store request/response state. If a network timeout occurs, verify status before creating a new attempt.

**Best Practice:** Do not retry consent, pre-debit, or recurring debit with a new ID until you know whether the previous request succeeded, failed, or timed out with no record.

#### What should I do when PayU returns an error?

**Short answer:** Log the request ID or transaction ID, error code, error message, payment mode, plan reference, and timestamp. Fix validation or configuration errors before retrying.

**Note:** Errors such as invalid hash, missing parameters, unsupported card, inactive mandate, or duplicate transaction ID require different actions. Do not handle all failures as generic retries.

### Merchant Troubleshooting

#### Why does plan creation fail in my dashboard?

**Short answer:** Since plan creation is merchant-side, failures usually come from your own validation rules, such as missing amount, invalid dates, unsupported frequency, duplicate plan reference, or missing customer details.

**Best Practice:** Show field-level errors before the merchant starts consent.

#### Why does mandate registration fail after I create the plan?

**Short answer:** Common reasons include unsupported card or payment mode, invalid `si_details`, amount above limits, hash mismatch, customer authentication failure, duplicate transaction ID, or issuer decline.

**Reference:** For card support issues, check BIN/payment-mode support before checkout where applicable.

#### Why does the subscription fail even though the mandate was successful?

**Short answer:** The plan may be Active in your system, but recurring payment can still fail because pre-debit was not sent, the mandate became inactive, the amount exceeded the approved limit, the card expired, or the customer had insufficient funds.

#### Why does pre-debit fail?

**Short answer:** Pre-debit can fail if the mandate identifier is wrong, the debit date is outside allowed windows, the amount exceeds the approved mandate, mandatory fields are missing, or the mandate is inactive/cancelled.

**Best Practice:** Validate mandate status and amount before sending pre-debit.

#### Why does recurring debit fail after pre-debit succeeded?

**Short answer:** A successful pre-debit notification does not guarantee debit success. Debit can still fail due to insufficient funds, issuer decline, inactive mandate, expired mandate, expired card, or incorrect recurring transaction parameters.

#### What should I check first when debugging a failed plan?

**Short answer:** Check plan status, mandate status, consent transaction status, pre-debit response, recurring debit response, amount, dates, transaction ID uniqueness, and hash logs.

**Best Practice:** Build an internal debug view that shows these values on one screen.

#### What are the most common integration mistakes?

**Short answer:** Common mistakes include changing plan values after consent, not storing `mihpayid` or `authpayuid`, skipping pre-debit, using duplicate transaction IDs, passing malformed `si_details`, treating pending as success, and not verifying final status.

#### How do I reduce support tickets from operations teams?

**Short answer:** Show clear plan status, mandate status, next action, last error reason, next debit date, and whether pre-debit is required before debit.

**Best Practice:** Add tooltips for statuses such as Consent pending, Active, Debit scheduled, Paused, Failed, and Cancelled.

### Edge Cases

#### Can I update a plan mid-cycle?

**Short answer:** You can update merchant-side display fields anytime, but changing approved terms such as amount, frequency, or date range may require mandate modification or fresh consent.

**Best Practice:** Apply changes from the next billing cycle unless the payment mode and mandate rules explicitly support immediate changes.

#### What happens if a recurring payment fails?

**Short answer:** Mark that debit attempt as failed or pending based on PayU response, verify final status, notify the customer if needed, and decide whether a retry is allowed under your business policy.

**Note:** Do not mark the full plan as Failed for a single failed debit unless your business rules require it.

#### Can I retry a failed recurring payment?

**Short answer:** Yes, but first check the final transaction status and mandate status. Use a new unique transaction ID for a new debit attempt.

#### Can I change the payment mode for an active plan?

**Short answer:** Usually, changing payment mode requires a new consent flow because the mandate is tied to the customer's approved payment instrument.

#### What is the maximum amount I can configure?

**Short answer:** Maximum amount depends on payment mode, issuer/network rules, regulatory limits, and merchant configuration. Validate limits before showing the plan to the customer.

**Best Practice:** Store both the displayed amount and the approved mandate limit for variable plans.

#### Can I use currencies other than INR?

**Short answer:** For India SI flows, use INR unless your PayU setup and the specific product documentation confirm support for another currency.

#### What happens if the customer's card expires before plan end date?

**Short answer:** Recurring debits can fail after card expiry. Ask the customer to register a new mandate or update payment details through the supported flow.

#### Can I use the same mandate for multiple plans?

**Short answer:** This depends on how your business maps plans and mandates. If you reuse a mandate, every debit must remain within the consented terms and limits.

**Best Practice:** Keep mapping explicit: plan reference, mandate identifier, debit amount, and schedule should be traceable for each debit.

#### How should I handle duplicate plans created by mistake?

**Short answer:** If they are Draft, delete or archive duplicates. If consent has started or succeeded, do not delete history; cancel the duplicate flow or mandate if needed.

### Production Readiness

#### What should be on my go-live checklist?

**Short answer:** Confirm merchant enablement, validate all mandatory fields, test consent and failure paths, implement pre-debit, store PayU identifiers, configure webhooks, verify final status handling, and prepare reconciliation reports.

#### What validations should I run before consent?

**Short answer:** Validate amount, currency, billing cycle, interval, start date, end date, customer email/phone, payment mode availability, unique transaction ID, and hash generation.

#### What should I monitor in production?

**Short answer:** Monitor consent success rate, mandate activation rate, pre-debit success rate, recurring debit success rate, pending transactions, webhook failures, duplicate transaction errors, and top issuer decline reasons.

#### How should I handle webhook retries?

**Short answer:** Make webhook processing idempotent. If the same event is received again, update the same record instead of creating duplicates.

**Best Practice:** Store event ID or a derived idempotency key using transaction ID, event type, and status timestamp.

#### What logs should I keep?

**Short answer:** Log plan reference, transaction ID, PayU ID, mandate identifier, request payload summary, response code, error message, hash source string reference, webhook payload, and status transitions.

**Note:** Do not log sensitive card data, CVV, OTP, full tokens, or secrets.

#### How long should I keep plan and mandate records?

**Short answer:** Keep records long enough for refunds, disputes, reconciliation, audit, and customer support based on your compliance policy.

### Developer Experience

#### What implementation flow should developers follow?

**Short answer:** Build plan draft first, validate fields, initiate consent, store identifiers, verify final consent status, schedule pre-debit, trigger recurring debit, then update status through response, webhook, or Verify Payment API.

#### What should be included in a Postman collection?

**Short answer:** Include consent request samples, hash generation examples, pre-debit request, recurring debit request, verify payment request, mandate status check, modify mandate, and cancel mandate.

**Best Practice:** Add both success and failure examples so developers know what to expect during integration testing.

#### What is the recommended testing strategy?

**Short answer:** Test unit validation for plan fields, integration tests for PayU APIs, end-to-end consent tests, scheduler tests for pre-debit timing, webhook retry tests, and reconciliation tests for recurring debit outcomes.

#### Which confusion points should I document in my internal runbook?

**Short answer:** Document that plan status is not mandate status, Draft plan creation does not call PayU, Active requires successful consent, pre-debit is required before many recurring debits, pending is not final success, and cancelled mandates cannot be reused.

#### What should frontend developers be careful about?

**Short answer:** Do not allow unsupported actions for the current status, do not mutate active plan terms silently, do not hide mandate failures, and do not let users trigger duplicate debits without status verification.

#### What should backend developers be careful about?

**Short answer:** Use stable identifiers, protect hash generation, make retries idempotent, store full status history, validate dates and limits, and separate merchant plan state from PayU transaction and mandate state.

<br />

<br />
