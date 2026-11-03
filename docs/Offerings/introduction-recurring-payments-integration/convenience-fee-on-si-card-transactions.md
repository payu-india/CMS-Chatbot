---
title: Convenience Fee on SI Card Transactions
excerpt: >-
  Apply normal or dynamic convenience fees on Standing Instruction recurring
  card transactions across Registration, Pre-Debit, and Recurring phases.
deprecated: false
hidden: false
metadata:
  robots: index
---
## What is a Convenience Fee?

A convenience fee is an additional charge collected from the customer on top of the base transaction amount to cover the cost of processing a payment through a specific payment instrument or channel. For Standing Instruction (SI) card transactions, this allows merchants to recover processing costs associated with recurring card mandates, such as credit card interchange fees or debit card surcharges, on a per-card-type basis.

The fee can be a **flat amount** (e.g., ₹10 per transaction) or a **percentage of the transaction amount** (e.g., 1.5%), and can vary by card type using ibibocodes.

***

## Who Can Use It?

Convenience fee on SI is available to merchants who:

- Have an active SI (Standing Instruction) integration with PayU for card recurring payments
- Are enabled for convenience fee collection on their MID by PayU
- Comply with applicable RBI and card network guidelines on surcharging

Contact <Anchor target="_blank" href="https://help.payu.in/raise-ticket">PayU Support</Anchor> to check eligibility and get the feature enabled on your MID.

***

## Use Cases

| Use Case                               | Description                                                                                                                      |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Recover card processing costs**      | Pass on interchange or processing fees for recurring card debits to the customer, differentiated by card type (credit vs debit). |
| **Dynamic pricing per cycle**          | Apply different fee amounts each billing cycle based on transaction value or card type using Dynamic Convenience Fee.            |
| **Platform-level surcharging**         | Aggregators and platforms can configure different rates per merchant sub-account to reflect actual processing costs.             |
| **Compliance with card network rules** | Transparently disclose and collect surcharges on card-based SI mandates in line with RBI and Visa/Mastercard guidelines.         |

***

## Convenience Fee Models

PayU supports convenience fees on Standing Instruction (SI) recurring card transactions in two models:

| Model                       | How it works                                                                                                                                                       | Who controls the value |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| **Normal Convenience Fee**  | Fee rates are pre-configured by PayU on the MID. Applied automatically. There are no additional parameters needed in the request.                                  | PayU backend           |
| **Dynamic Convenience Fee** | Merchant passes fee values in each API request using `additional_charges` and `percentage_additional_charges`. Allows different fees per transaction or card type. | Merchant               |

<Callout icon="📘" theme="info">
  ### **Tips:**

  - You can pass both `additional_charges` and `percentage_additional_charges` simultaneously in the same request. PayU will apply both, a flat fee and a percentage fee together on the transaction.
  - For general (non-SI) convenience fee on one-time payments, refer to [Collect Additional Charges](doc:collect-additional-charges).
</Callout>

***

## Parameters

The following parameters are used for Dynamic Convenience Fee. They are string and optional and applicable only when the relevant MID flags are enabled.

| Parameter                       | Description                                                                                                                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `additional_charges`            | Flat convenience fee per SI card type. Pass as a comma-separated `IBIBOCODE:value` string where value is the fee amount in INR. Example: `CCSI:10,DCSI:20,AMEXSI:30`             |
| `percentage_additional_charges` | Percentage-based convenience fee per SI card type. Pass as a comma-separated `IBIBOCODE:value` string where value is the fee percentage. Example: `CCSI:1.5,DCSI:1.0,AMEXSI:2.0` |

***

## Ibibocodes

Both models use ibibocodes to identify the SI card type:

| Ibibocode  | Card Type           | Registration | Pre-Debit | Recurring |
| ---------- | ------------------- | ------------ | --------- | --------- |
| `CCSI`     | Credit Card SI      | ✅            | ✅         | ✅         |
| `DCSI`     | Debit Card SI       | ✅            | ✅         | ✅         |
| `AMEXSI`   | American Express SI | ✅            | ✅         | ✅         |
| `VISASI`   | Visa SI             | ✅            | ✅         | ✅         |
| `HDFCDCSI` | HDFC Debit Card SI  | ❌            | ✅         | ✅         |

<Callout icon="⚠️" theme="warn">
  ### Warning

  `HDFCDCSI` is **not** supported during the Registration phase. Passing it in a registration request will result in an error.
</Callout>

***

## Enablement

<Accordion title="Normal Convenience Fee" icon="fa-gear">
  Contact <Anchor target="_blank" href="https://help.payu.in/raise-ticket">PayU Support</Anchor> to configure flat or percentage fee rates per ibibocode on your MID. Provide the ibibocode and the fee amount or percentage for each SI card type you want to enable. No API changes are required from your end once configured.
</Accordion>

<Accordion title="Dynamic Convenience Fee" icon="fa-gear">
  The following MID flags must be enabled before using dynamic convenience fee on SI:

  | Flag                       | Description                                             |
  | -------------------------- | ------------------------------------------------------- |
  | `enableCardsSiDynamicConv` | Enables dynamic convenience fee on SI card transactions |
  | `enableSIPredebitConvFee`  | Enables dynamic convenience fee at the pre-debit stage  |
  | `DynamicConvFeeMerchant`   | Marks the MID as a dynamic convenience fee merchant     |

  Contact <Anchor target="_blank" href="https://help.payu.in/raise-ticket">PayU Support</Anchor> to get these flags enabled on your MID.
</Accordion>

***

## Applying Convenience Fee Across SI Phases

An SI card transaction goes through three distinct phases. Convenience fees can be applied at each phase — the same fee parameters are used throughout, but the API and applicable ibibocodes differ per phase.

| Phase            | When it happens                                                                                                 | API command      |
| ---------------- | --------------------------------------------------------------------------------------------------------------- | ---------------- |
| **Registration** | Customer gives consent for the SI mandate                                                                       | `_payment` API   |
| **Pre-Debit**    | Merchant notifies the customer before each recurring charge (mandatory, at least 48 hrs before debit for cards) | `pre_debit_SI`   |
| **Recurring**    | Actual debit is triggered against the mandate                                                                   | `si_transaction` |

***

<Accordion title="Phase 1: Registration" icon="fa-pen-to-square">
  The registration phase captures the customer's consent and sets up the SI mandate. For the complete registration flow including `si_details` structure, refer to [Cards SI Integration — Merchant Hosted Checkout](doc:cards-subscription-integration-merchant-hosted-checkout).

  **Applicable ibibocodes:** `CCSI`, `DCSI`, `AMEXSI`, `VISASI` — `HDFCDCSI` is not supported at registration.

  ***

  ### Normal Convenience Fee

  No changes are needed in the registration request. PayU applies the configured fee automatically. The fee details are returned in the payment response.

  **Response parameters:**

  | Parameter                       | Description                                                              |
  | ------------------------------- | ------------------------------------------------------------------------ |
  | `additional_charges`            | Flat fee charged, as a `IBIBOCODE:value` string (e.g., `CCSI:10`)        |
  | `percentage_additional_charges` | Percentage fee charged, as a `IBIBOCODE:value` string (e.g., `CCSI:1.5`) |

  **Reverse hash formula (when&#x20;**`additional_charges`**&#x20;is present in response):**

  ```plaintext
  sha512(additional_charges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  ***

  ### Dynamic Convenience Fee

  Pass `additional_charges` and/or `percentage_additional_charges` in the `_payment` API request.

  <Accordion title="Sample request" icon="fa-upload">
    ```curl
    curl -X POST "https://secure.payu.in/_payment" \
      -d "key=YOUR_KEY" \
      -d "txnid=TXN001" \
      -d "amount=500.00" \
      -d "productinfo=Subscription" \
      -d "firstname=Aarav" \
      -d "email=aarav@example.com" \
      -d "phone=9999999999" \
      -d "surl=https://yoursite.com/success" \
      -d "furl=https://yoursite.com/failure" \
      -d "si=1" \
      -d "si_details=YOUR_SI_DETAILS_JSON" \
      -d "additional_charges=CCSI:10,DCSI:20,AMEXSI:30,VISASI:50" \
      -d "percentage_additional_charges=CCSI:1.5,DCSI:1.0,AMEXSI:2.0,VISASI:1.2" \
      -d "hash=YOUR_HASH"
    ```

    > For the full `si_details` JSON structure, refer to [Cards SI Integration — Merchant Hosted Checkout](doc:cards-subscription-integration-merchant-hosted-checkout).
  </Accordion>

  **Hash formula:**

  ```plaintext
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|additional_charges|SALT)
  ```

  **Response parameters:**

  | Parameter                       | Description                                                       |
  | ------------------------------- | ----------------------------------------------------------------- |
  | `additional_charges`            | Flat fee applied, echoed back as a `IBIBOCODE:value` string       |
  | `percentage_additional_charges` | Percentage fee applied, echoed back as a `IBIBOCODE:value` string |

  **Reverse hash formula (when&#x20;**`additional_charges`**&#x20;is present in response):**

  ```plaintext
  sha512(additional_charges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```
</Accordion>

<Accordion title="Phase 2: Pre-Debit" icon="fa-bell">
  A pre-debit notification must be sent at least 48 hours before the recurring debit for Cards. This is mandatory — the recurring debit will fail without it. For full API reference, refer to [Pre-Debit Notification API](ref:predebit).

  **Applicable ibibocodes:** `CCSI`, `DCSI`, `AMEXSI`, `HDFCDCSI`, `VISASI`

  | Environment | URL                                                    |
  | ----------- | ------------------------------------------------------ |
  | Production  | `https://info.payu.in/merchant/postservice.php?form=2` |
  | Test        | `https://test.payu.in/merchant/postservice.php?form=2` |

  ***

  ### Normal Convenience Fee

  No changes are needed in the `pre_debit_SI` request. PayU applies the configured fee automatically. The invoice will reflect the total amount including the fee.

  ***

  ### Dynamic Convenience Fee

  Pass `additional_charges` and/or `percentage_additional_charges` inside the `var1` JSON.

  <Accordion title="Sample request" icon="fa-upload">
    ```curl
    curl -X POST "https://info.payu.in/merchant/postservice.php?form=2" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      -d "form=2" \
      -d "key=YOUR_KEY" \
      -d "command=pre_debit_SI" \
      -d "hash=YOUR_HASH" \
      -d 'var1={
        "authpayuid": "403993715524262603",
        "requestId": "REQ-2024-001",
        "amount": "500.00",
        "debitDate": "2024-05-10",
        "invoiceDisplayNumber": "INV-12345",
        "additional_charges": "CCSI:10,DCSI:20,AMEXSI:30,HDFCDCSI:40,VISASI:50",
        "percentage_additional_charges": "CCSI:1.5,DCSI:1.0,AMEXSI:2.0,HDFCDCSI:1.8,VISASI:1.2"
      }'
    ```
  </Accordion>

  **Hash formula:**

  ```plaintext
  sha512(key|command|var1|salt)
  ```

  <Accordion title="Sample response" icon="fa-download">
    ```json Success
    {
      "invoiceid": "76323425",
      "approvedStatus": "na",
      "invoiceStatus": "unpaid",
      "amount": "500.00",
      "status": 1,
      "message": "Invoice Created Successfully",
      "action": "MANDATE_PRE_DEBIT"
    }
    ```

    ```json Failure
    {
      "status": 0,
      "action": "MANDATE_PRE_DEBIT",
      "message": "Mandate is not active"
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="Phase 3: Recurring" icon="fa-rotate">
  The recurring debit charges the customer's card against the existing mandate. For full API reference, refer to [Pre-debit and Recurring Payments Transaction API](ref:predebitRecurringPaymentTransaction).

  **Applicable ibibocodes:** `CCSI`, `DCSI`, `AMEXSI`, `HDFCDCSI`, `VISASI`

  | Environment | URL                                                    |
  | ----------- | ------------------------------------------------------ |
  | Production  | `https://info.payu.in/merchant/postservice.php?form=2` |
  | Test        | `https://test.payu.in/merchant/postservice.php?form=2` |

  ***

  ### Normal Convenience Fee

  No changes are needed in the `si_transaction` request. PayU applies the configured fee automatically.

  ***

  ### Dynamic Convenience Fee

  Pass `additional_charges` and/or `percentage_additional_charges` inside the `var1` JSON.

  <Accordion title="Sample request" icon="fa-upload">
    ```curl
    curl -X POST "https://info.payu.in/merchant/postservice.php?form=2" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      -d "form=2" \
      -d "key=YOUR_KEY" \
      -d "command=si_transaction" \
      -d "hash=YOUR_HASH" \
      -d 'var1={
        "authPayuId": "403993715529787",
        "txnId": "TXN_20240510_001",
        "amount": "500.00",
        "debitDate": "2024-05-10",
        "debitType": "PREDEBIT_AND_RECURRING",
        "additional_charges": "CCSI:10,DCSI:20,AMEXSI:30,HDFCDCSI:40,VISASI:50",
        "percentage_additional_charges": "CCSI:1.5,DCSI:1.0,AMEXSI:2.0,HDFCDCSI:1.8,VISASI:1.2"
      }'
    ```
  </Accordion>

  **Hash formula:**

  ```plaintext
  sha512(key|command|var1|salt)
  ```

  <Accordion title="Sample response" icon="fa-download">
    ```json Success
    {
      "status": 1,
      "message": "Debit Scheduled successfully",
      "details": [],
      "predebitDetails": []
    }
    ```

    ```json Failure
    {
      "status": 0,
      "message": "debitDate is mandatory",
      "errorCode": "SIR004",
      "action": "SI_RECURRING"
    }
    ```
  </Accordion>
</Accordion>

***

## Related Pages

<Cards>
  <Card title="Cards SI Integration — Merchant Hosted Checkout" href="doc:cards-subscription-integration-merchant-hosted-checkout">
    Full registration and SI consent flow for card mandates including si_details structure
  </Card>

  <Card title="Pre-Debit Notification API" href="ref:predebit">
    API reference for the pre_debit_SI command with all var1 parameters
  </Card>

  <Card title="Pre-debit and Recurring Payments Transaction API" href="ref:predebitRecurringPaymentTransaction">
    API reference for the si_transaction command
  </Card>

  <Card title="Collect Additional Charges" href="doc:collect-additional-charges">
    Convenience fee for one-time (non-SI) payments
  </Card>
</Cards>
