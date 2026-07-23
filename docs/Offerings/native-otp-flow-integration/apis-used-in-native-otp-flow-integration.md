---
title: APIs used in Integration
deprecated: false
hidden: false
icon: far fa-stopwatch-20
metadata:
  title: APIs used in Native OTP Flow integration
  robots: index
---
The following APIs are used for Native OTP Flow integration:

### Collect Payment

| Use case → Reference                                                                       | `command` / primary value                     | Description                                                                                                                               |
| ------------------------------------------------------------------------------------------ | --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Initiate payment — [Collect Payment API – Server-to-Server](ref:_payment_server_to_server) | `POST _payment` with `S2S=4`                  | Initiates a payment in which the customer enters the OTP on the merchant or PayU page instead of being redirected to the bank's 3DS page. |
| Submit the OTP — [Submit OTP API](ref:submit-otp-to-payu)                                  | `POST ResponseHandler.php` with `otp`         | Submits the OTP entered by the customer to complete card authentication.                                                                  |
| Resend the OTP — [Resend OTP API](ref:resend-otp-api)                                      | `POST ResponseHandler.php` with `resendOtp=1` | Resends the OTP when the previously issued OTP is incorrect or expired.                                                                   |
| Check EMI eligibility — [Get Checkout Details API](ref:get_checkout_details)               | `get_checkout_details`                        | Checks customer eligibility before initiating Debit Card EMI or Cardless EMI Native OTP payments.                                         |
| Verify a payment — [Verify Payment API](ref:verify_payment_api)                            | `verify_payment`                              | Reconciles the transaction status with PayU after OTP submission.                                                                         |

### Submit or Resend OTP

| Use case → Reference                                      | `command` / primary value                     | Description                                                              |
| --------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------ |
| Submit the OTP — [Submit OTP API](ref:submit-otp-to-payu) | `POST ResponseHandler.php` with `otp`         | Submits the OTP entered by the customer to complete card authentication. |
| Resend the OTP — [Resend OTP API](ref:resend-otp-api)     | `POST ResponseHandler.php` with `resendOtp=1` | Resends the OTP when the previously issued OTP is incorrect or expired.  |

### Check EMI

| Use case → Reference                                                         | `command` / primary value | Description                                                                                       |
| ---------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------- |
| Check EMI eligibility — [Get Checkout Details API](ref:get_checkout_details) | `get_checkout_details`    | Checks customer eligibility before initiating Debit Card EMI or Cardless EMI Native OTP payments. |

### Verify Payment

| Use case → Reference                                            | `command` / primary value | Description                                                       |
| --------------------------------------------------------------- | ------------------------- | ----------------------------------------------------------------- |
| Verify a payment — [Verify Payment API](ref:verify_payment_api) | `verify_payment`          | Reconciles the transaction status with PayU after OTP submission. |

<br />

<br />
