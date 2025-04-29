---
title: Test Credentials
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
For test credentials for Payouts, you need to sign up for a test merchant in the following URL:

&lt;https://uat-onepayuonboarding.payu.in/app/account/signup&gt;

After your test merchant account is created, share your email ID, merchant ID (under the Profile section), and phone number used while registering for test credentials with your PayU Key Account Manager (KAM) in order to activate Payouts.

You may also use the following credentials too.

|           |                                                                  |
| :-------- | :--------------------------------------------------------------- |
| Client ID | ccbb70745faad9c06092bb5c79bfd919b6f45fd454f34619d83920893e90ae6b |

## Testing Various Responses

The following testing credentials can be used to get particular responses from transfer APIs:

- Use beneficiaryAccountNumber as “**51234567890**” to get the success response
- Use beneficiaryAccountNumber as “**41234567890**” to get the Failure response
- Use beneficiaryAccountNumber as “**61234567890**” to get the Pending response

> 📘 Note:
>
> You can use any valid VPA in the test environment.

## Testing VPA

Use only "kk@okaxis" in the Test Environment for the **Validate VPA** API for Payouts. For more information on the **Validate VPA** API, refer to [Validate VPA - Payouts](ref:validatevpa).