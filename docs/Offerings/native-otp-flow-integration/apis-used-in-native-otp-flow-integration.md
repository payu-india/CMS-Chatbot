---
title: APIs used in Native OTP Flow integration
deprecated: false
hidden: false
icon: far fa-stopwatch-20
metadata:
  title: APIs used in Native OTP Flow integration
  robots: index
---
| API                                                                     | Purpose                                                                                                                                          |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Collect Payment API – Server-to-Server](ref:_payment_server_to_server) | Initiate an S2S=4 payment request; the customer receives an OTP on the merchant or PayU page instead of being redirected to the bank's 3DS page. |
| [Submit OTP API](ref:submit-otp-to-payu)                                | Submit the OTP entered by the customer on the `postUrl`/`acsTemplate` page to complete card authentication.                                      |
| [Resend OTP API](ref:resend-otp-api)                                    | Resend OTP when the customer enters an incorrect or expired OTP. **Used in:** all Native OTP Flow integration guides.                            |
| [Get Checkout Details API](ref:get_checkout_details)                    | Check customer EMI eligibility before initiating Debit Card EMI or Cardless EMI native OTP payments.                                             |
| [Verify Payment API](ref:verify_payment_api)                            | Server-side reconciliation of transaction status after OTP submission.                                                                           |

<br />
