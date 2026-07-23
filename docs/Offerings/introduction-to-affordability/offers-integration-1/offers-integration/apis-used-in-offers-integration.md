---
title: APIs used in Offers Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Offers Integration
  robots: index
---
Use these APIs to check EMI eligibility, collect an EMI payment, and reconcile the resulting transaction.

### Collect payment

| Use case → Reference                                                            | `command` / primary value | Description                                                                                                                                                  |
| ------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout) | `_payment`                | Initiate an EMI transaction on the PayU-hosted payment page (non-seamless checkout), where the customer selects EMI, enters card details, and completes OTP. |

### Eligibility checks

| Use case → Reference                                                                            | `command` / primary value                  | Description                                                                                                               |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| [Get Checkout Details API](ref:get_checkout_details)                                            | `get_checkout_details`                     | Check customer eligibility before payment by mobile number for debit-card pre-EMI and cardless EMI.                       |
| [Get EMI According to Interest API](ref:get_emi_according_to_interest_api)                      | `getEmiAmountAccordingToInterest`          | Calculate interest, monthly instalment, processing fee, No-Cost EMI, tenure, and the corresponding `bankcode` for a plan. |
| [Eligible BINs for EMI API v1.0](ref:eligiblebinsforemi)                                        | `eligibleBins`                             | Check credit-card EMI eligibility from the card BIN and return the issuing bank and minimum eligible amount.              |
| [Eligible BINs for EMI API v2.0](https://docs.payu.in/v2/reference/eligible-bin-for-emi-api-v2) | `POST /issuing-bank/v1/bin/binEligibility` | Check EMI eligibility by card BIN or network token and return the issuing bank and minimum eligible amount.               |

### Verify the payment

| Use case → Reference                         | `command` / primary value | Description                                                      |
| -------------------------------------------- | ------------------------- | ---------------------------------------------------------------- |
| [Verify Payment API](ref:verify_payment_api) | `verify_payment`          | Reconcile the transaction status from your server after payment. |

<br />
