---
title: Refunds Online Retry and Offline Handling
deprecated: false
hidden: true
icon: fab fa-cash-app
metadata:
  robots: index
---
After you initiate a refund, PayU sends the request to the payment gateway or bank. The request can succeed, remain in progress while PayU waits for confirmation, or fail. When a temporary failure occurs, PayU determines whether the refund can be retried online or must be sent for offline processing.

This section describes what to expect after initiation. For refund initiation and tracking options, see [Refunds Dashboard](doc:refunds-dashboard), [Refund APIs](doc:refund-apis-doc), or the [Refunds](doc:refunds) overview.

The refund lifecycle can include more than one attempt or status transition:

1. PayU sends the refund request to the payment gateway or bank.
2. The request may succeed, remain in progress while awaiting confirmation, or fail.
3. For an eligible temporary failure, PayU retries the refund online automatically.
4. If online retries are exhausted or are not allowed, PayU sends the refund for offline processing.
5. The bank processes the refund and confirms the final status.

Multiple attempts or status transitions for the same refund are expected. The final status is communicated after processing is complete.

## What happens when a refund is initiated

A refund request is sent to the payment gateway or bank. The response determines the next state:

- **Success**: The refund is completed.
- **In progress**: The refund is still being processed while confirmation is pending.
- **Failure**: The request cannot be completed through the available processing paths.

If the first online attempt fails, PayU evaluates the failure and automatically chooses the next available path. You do not need to submit another refund request just because an online attempt failed.

## Online retry handling

PayU automatically retries a refund when the failure is temporary and the refund is eligible for another online attempt.

### What happens during online retry

1. PayU creates another online retry attempt.
2. The system waits a short interval, typically from a few minutes to a few hours.
3. PayU sends the refund request to the payment gateway or bank again.
4. PayU repeats this process up to **three retry attempts** within the retry limit.

No manual retry action is required from you.

- If a retry succeeds, the refund is completed and reaches **SUCCESS**.
- If all allowed retries fail, or an online retry is not allowed, the refund can move to offline processing.

## Offline refund handling

Offline processing is the manual or batch path used when online processing cannot continue. PayU sends the refund to the bank through a secure channel. The bank processes the request and confirms the final status.

Once the refund is transferred for offline processing:

- No further online attempts occur.
- The refund can take approximately **5–7 business days** to process and receive a final status.
- The final outcome is **SUCCESS** or **FAILURE**, based on the bank's confirmation.

> **Important:** `REQUESTED` means the refund has been sent for offline processing. It does **not** mean that the refund succeeded.

## When a refund moves offline

A refund can move to offline processing when any of the following applies:

- The maximum number of online retry attempts has been reached.
- The bank or payment gateway does not allow another retry.
- The error requires manual handling.
- Online retry is disabled by merchant or system settings.
- Online retries have failed and offline processing is the next available path.

After the offline transfer, PayU does not make another online attempt for that refund.

## Refund status meanings

The following meanings use the status terminology described in the refund documentation and source process flow:

| Status          | Meaning                                                                                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Pending**     | The refund is being processed. A final outcome is not available yet.                                                                                      |
| **IN PROGRESS** | The refund has been initiated and is being processed. It is not a final success or failure.                                                               |
| **Retry**       | PayU will try the refund again online, subject to the retry limit and eligibility. No merchant action is required.                                        |
| **REQUESTED**   | The refund has been sent to the bank for offline or manual processing. No further online attempts occur. This status is not confirmation of success.      |
| **SUCCESS**     | The refund has been successfully processed.                                                                                                               |
| **FAILURE**     | The refund has failed permanently after the available processing paths could not complete it, or the bank confirmed that it could not process the refund. |

A status can change as the refund moves through online attempts and, where applicable, offline processing. Wait for the final status before treating the refund as completed or failed.

## When a refund fails completely

A refund reaches final **FAILURE** when neither online retry nor offline processing is allowed, or when the bank confirms that it cannot process the refund.

A final failure is different from a temporary online failure. A temporary failure can lead to an automatic retry or offline processing. A final **FAILURE** means that no available processing path can complete the refund.

## What merchants should expect

- **Do not retry manually after the first online failure.** PayU automatically retries eligible temporary failures, up to three times.
- **Expect a short wait between online attempts.** The wait can be from a few minutes to a few hours.
- **Allow more time for offline processing.** Offline processing typically takes 5–7 business days.
- **Expect more than one attempt or status transition.** These are part of the refund process and can be visible for the same refund.
- **Do not treat&#x20;**`REQUESTED`**&#x20;as success.** It means that the refund is being handled offline and is awaiting the bank's final status.
- **Use the final status to determine the outcome.** The refund is complete only when it reaches `SUCCESS`; `FAILURE` indicates that processing could not be completed.

## Simple lifecycle summary

```text
Refund initiated
      |
      v
Request sent to the payment gateway or bank
      |
      +--> Success --------------------------> SUCCESS
      |
      +--> In progress ----------------------> Await confirmation
      |
      +--> Temporary online failure
              |
              v
       Automatic online retry
       (up to 3 attempts; wait minutes to hours)
              |
              +--> Retry succeeds -----------> SUCCESS
              |
              +--> Retry exhausted or not allowed
                      |
                      v
               Offline processing
               (secure bank channel; 5–7 business days)
                      |
                      +--> Bank confirms success -> SUCCESS
                      |
                      +--> Bank cannot process -> FAILURE

If neither retry nor offline processing is allowed -> FAILURE
```
