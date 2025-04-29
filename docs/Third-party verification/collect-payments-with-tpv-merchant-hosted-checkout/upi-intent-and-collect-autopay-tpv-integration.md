---
title: UPI Intent and Collect Autopay TPV Integration
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
For recurring payment use-case, you can use UPI as a payment instrument. It requires, registration of the mandate and then doing the debit in the customer’s account. During registration, customer validates the billing details of the mandate on the respective application, enters their MPIN (Mobile PIN) and authorizes the mandate. After the registration transaction is successful, you can then use the **Recurring Payment Transaction** API to charge the customer without requiring further intervention. For more information on Recurring Payment API, refer to  [Recurring Payment Transaction API](ref:recurring_payment_api)

The Third-Party Verification (TPV) functionality is now being added to the UPI Autopay too. 

> 📘 Notes:
> 
> - Currently, PayU supports UPI Autopay only with Seamless integration.
> - Contact your PayU Key Account Manager (KAM) or [PayU Support ](https://help.payu.in)to activate this feature.

### Use Cases

Merchants have use cases, which requires the transactions to be allowed only for selected accounts only. These accounts are provided by the customer before hand (during customer registration on merchant platform). Few merchant use cases are:

- Mutual Funds (SEBI guideines)
- Loan Repayment

However, as part of UPI, customer has the flexibility to link multiple accounts under the same VPA and on run-time, change the account for authorisation. So using TPV services, merchant makes sure that customer authorises the transaction using pre-registered accounts only.

### Collect Autopay TPV Flow

The merchant initiates the call to PayU with SI details, **bankcode** as **UPITPV**, and account number + IFSC details. PayU then initiates a mandate call with all the SI and account-related parameters to the bank. After the customer authorizes the mandate, the bank will validate the account. If the account details match, only then will the success notification be sent to PayU. However, if the account details do not match, Bank will pass validation error to PayU. Internally, Bank will cancel the mandate that has been setup on customer’s account. 

To integrate the UPI Collect Autopay TPV Flow, refer to [UPI Collect Autopay TPV Integration](doc:upi-collect-autopay-tpv-integration).

### Intent Autopay TPV Flow

The merchant initiates the call to PayU with SI details, **bankcode** as **INTTPV**, and account number + IFSC details. PayU then initiates a mandate call to the bank, including all the SI and account-related parameters. The bank responds to PayU with a reference-Id, which PayU passes to the merchant in an Intent URL. When the customer authorizes the transaction, the bank will validate the account. If the account details match, a success message will be sent to PayU. However, if the account details do not match, Bank will pass validation error to PayU. Internally, Bank will cancel the mandate that has been setup on customer’s account.

To integrate the UPI Collect Intent TPV Flow, refer to [UPI Intent Autopay TPV Integration](doc:upi-intent-autopay-tpv-integration).

> 📘 Note:
> 
> Validation is done only in the registration step of the mandate. If the account matches, rest of the journey for UPI Autopay will remain as-is.