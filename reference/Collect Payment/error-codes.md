---
title: Error Codes
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The following are possible errors and error codes for a transaction. You need to remember the following while error handling based on payment response:

- The **PayU Error Code** column in the following table corresponds to the value returned in the **error** parameter of the payment response
- The **error\_message / message** column in the following table corresponds to the value returned in the **error\_message / message** parameter of the payment response

> 📘 **Note:**&#x20;
>
> The reason for failure depends upon the error codes provided by different banks and hence the detailing of error reasons may differ from one transaction to another.

> ❗️ **Transaction Stages Error handling**:&#x20;
>
> For error references on during various transaction stages in Net Banking, Cards and Wallets, refer to [Transaction Stages - Error References on Field7 & Field8](#transaction-stages-error-references-field7-field8).

> 📘 **Reference:**
>
> Refer to the **[Cards](https://docs.payu.in/reference/error-codes#cards)** section for AuthN and AuthZ errors

<SearchableTableRemote
  dataUrl="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/payment-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

## Other Error Codes from PayU

<SearchableTableRemote
  dataUrl="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/other-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

## Error References on Field7 and Field8

The PayU error mappings documentation page provides a reference guide for various error codes in the PayU payment system. The page includes:

- [Field Error code structure](https://docs.payu.in/reference/error-codes#field-error-code-structure): Explains how error codes are formatted and what different components mean
- **Field7 Error Code Mapping** - Contains error codes like ALT\_ID\_PROV\_ERROR, 3DS\_METHOD\_POSITIVE, etc., with their descriptions, platform layers, and API layers for the following payment modes:
  - [Field7 for Card payments](https://docs.payu.in/reference/error-codes#field7-for-card-payments)
  - [Field 7 for Net Banking/Wallet payments](https://docs.payu.in/reference/error-codes#netbanking-and-wallets)

> :blue_book: Standard error codes vs Field 7 error codes
>
> The Field7 error codes documented in this section are part of PayU's comprehensive error handling system. These codes provide detailed transaction state information that complements the standard [Error Codes](#error-codes) used across PayU's payment platform.
>
> While standard error codes (E.g. E501, E502, etc.) indicate specific failure reasons, Field7 values track the transaction state and provide visibility into exactly where in the payment flow an error or status change occurred. For complete error handling, developers should check both:
>
> 1. **Field7 Values**: To determine the transaction state and processing stage
> 2. **Error Codes**: To identify specific failure reasons when applicable
>
> For integration purposes, always implement error handling that accounts for both these complementary systems to provide the best user experience and troubleshooting capabilities.

### Field Error code structure

To understand the error codes, you need to read the Error Code Object sent in the Response structure or stored in database.

1. **Field7 – Execution Leg**: This field is used to understand at which execution stage (or leg) the transaction got declined. It is essentially a forward leg or process leg of an API that identifies the point of transaction failure. Refer to following sub-sections for understanding this field values:
   - [Field7 for Card payments](#field7-for-card-payments)
   - [Field 7 for Net Banking/Wallet payments](#field-7-for-net-bankingwallet-payments)
2. **Field8 – Bank or Wallet's Reason**: This field captures the actual reason for the transaction failure as provided by the bank.<br />It gives direct feedback or error information from the bank's end.
3. **Field9 – PayU's Error Translation**: This field contains the PayU-translated version of the error recorded in Field8.<br />It provides a simplified and standardized interpretation of the error for easier understanding and debugging.
4. **Error Code**: Represents PayU's error code mapped to the specific issue. It acts as a unique identifier for the error.
5. **Error Message**: This contains PayU's error interpretation, which elaborates on or describes the error in a user-friendly manner to assist in troubleshooting.

## Issuer Decline Error Codes

The following table helps you identify specific reasons for payment failures and provides standardized error codes and messages. This will facilitate troubleshooting and communicate your customers when transactions are declined.

<SearchableTableRemote
  dataUrl="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/issuer-decline-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

## Cards

The following are the errors associated with cards along with their reasons and descriptions.

### Field7 for Card payments

<SearchableTableRemote
  dataUrl="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/field7-card-payments.json"
  placeholder="Search"
  maxHeight="500px"
/>

### AuthN Errors

<SearchableTableRemote
  dataUrl="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/auth-n-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

> ⬇️ **Download Template**
>
> **[Download AuthN Errors in the CSV Template](https://github.com/palgunams21/payu-docs-assets/releases/download/AuthN-AuthZ-errors/AuthN_error_list.csv)**

### AuthZ Errors

<SearchableTableRemote
  dataUrl="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/auth-z-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

> ⬇️ **Download Template**
>
> **[Download AuthZ Errors in the CSV Template](https://github.com/palgunams21/payu-docs-assets/releases/download/AuthN-AuthZ-errors/AuthZ_error_list.csv)**

### Alt ID Errors

<SearchableTableRemote
  dataUrl="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/alt-id-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

## NetBanking and Wallets

The following are the errors associated with NetBanking and wallets along with their reasons and descriptions.

<SearchableTableRemote
  dataUrl="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/netbanking-wallets.json"
  placeholder="Search"
  maxHeight="500px"
/>

## UPI Error Codes

<SearchableTable
  headers={['Mode', 'Error Code', 'Reason']}
  rows={[
    ['UPICC','E000','Error at the Bank Server end'],
    ['UPIPPI','E000','Error at the Bank Server end'],
    ['UPI','E000','Error at the Bank Server end'],
    ['UPI','E1020','Offus Master Card Not Approved Transaction'],
    ['UPI','E1101','Cancellation not allowed for offus master card'],
    ['UPI','E1203','Empty Otp Received'],
    ['UPICC','E1203','Empty Otp Received'],
    ['UPI','E1204','Transaction failed during authentication'],
    ['UPICC','E1206','Invalid Merchant Key'],
    ['UPI','E1206','Invalid Merchant Key'],
    ['UPIPPI','E1206','Invalid Merchant Key'],
    ['UPI','E1400','Transaction could not be completed due to violation of law'],
    ['UPIPPI','E1605','Incorrect request received for one click transaction'],
    ['UPI','E1605','Incorrect request received for one click transaction'],
    ['UPICC','E1605','Incorrect request received for one click transaction'],
    ['UPI','E1610','Invalid Action'],
    ['UPI','E1611','The transaction cannot be processed as discount given exceeds the allowed limit. If money is debited from your account then it will be auto refunded. Please try again'],
    ['UPI','E1626','Invalid PG & Bank Code Combination'],
    ['UPICC','E1626','Invalid PG & Bank Code Combination'],
    ['UPI','E1629','Transaction failed as additional charges could not be calculated'],
    ['UPICC','E1629','Transaction failed as additional charges could not be calculated'],
    ['UPIPPI','E1629','Transaction failed as additional charges could not be calculated'],
    ['UPI','E202','No Bank response'],
    ['UPI','E214','Security Signature missing or mismatched'],
    ['UPI','E219','The address needs to match with the records of card issuing bank'],
    ['UPI','E220','Transaction denied due to risk'],
    ['UPIPPI','E220','Transaction denied due to risk'],
    ['UPICC','E220','Transaction denied due to risk'],
    ['UPICC','E225','Bank failed to authenticate the customer due to 3D Secure Authentication decline'],
    ['UPI','E225','Bank failed to authenticate the customer due to 3D Secure Authentication decline'],
    ['UPICC','E307','Transaction failed due to invalid OTP'],
    ['UPIPPI','E307','Transaction failed due to invalid OTP'],
    ['UPI','E307','Transaction failed due to invalid OTP'],
    ['UPI','E308','Transaction failed due to invalid merchant'],
    ['UPICC','E308','Transaction failed due to invalid merchant'],
    ['UPI','E311','Technical Failure. Kindly try alternative payment methods'],
    ['UPI','E316','The transaction has been identified as duplicate transaction.'],
    ['UPI','E317','Transaction Expired'],
    ['UPICC','E324','Card authentication failed as user exceeded maximum number of permitted retries for PIN.'],
    ['UPIPPI','E324','Card authentication failed as user exceeded maximum number of permitted retries for PIN.'],
    ['UPI','E324','Card authentication failed as user exceeded maximum number of permitted retries for PIN.'],
    ['UPI','E325','Transaction failed due to invalid credit card name'],
    ['UPI','E345','EMI is not supported on this card'],
    ['UPI','E4001','ISSUER NOT LIVE ON UPI'],
    ['UPI','E4005','Transaction failed due to MPIN not set by customer'],
    ['UPICC','E4005','Transaction failed due to MPIN not set by customer'],
    ['UPICC','E4009','Transaction failed due to mobile number linked to account is changed'],
    ['UPI','E4009','Transaction failed due to mobile number linked to account is changed'],
    ['UPICC','E4010','Transaction not allowed on/from the account'],
    ['UPI','E4010','Transaction not allowed on/from the account'],
    ['UPIPPI','E4010','Transaction not allowed on/from the account'],
    ['UPI','E4012','MOBILE NUMBER REGISTERED WITH MULTIPLE CUSTOMER IDS'],
    ['UPICC','E4013','Transaction failed due to beneficiary timeout'],
    ['UPIPPI','E4013','Transaction failed due to beneficiary timeout'],
    ['UPI','E4013','Transaction failed due to beneficiary timeout'],
    ['UPI','E4019','DUPLICATE RRN FOUND IN THE TRANSACTION. (BENEFICIARY)'],
    ['UPI','E4020','DUPLICATE RRN FOUND IN THE TRANSACTION. (REMITTER)'],
    ['UPI','E4021','Transaction failed due to first transaction limit exceeded by the customer'],
    ['UPICC','E4021','Transaction failed due to first transaction limit exceeded by the customer'],
    ['UPI','E4022','Transaction failed due to freeze period for the first time customer'],
    ['UPICC','E4022','Transaction failed due to freeze period for the first time customer'],
    ['UPI','E4027','BANKS HSM IS DOWN(REMITTER)'],
    ['UPICC','E4027','BANKS HSM IS DOWN(REMITTER)'],
    ['UPI','E4031','PAYER/PAYEE .INFO.IDENTITY VERIFIEDNAME MUST BE PRESENT ALPHANUMERIC MINLENGTH 1 MAXLENGTH 99'],
    ['UPI','E4037','Transaction failed due to funds blocked for mandate in customer\'s account'],
    ['UPI','E4041','Transaction failed due to internal exception at server/cbs end at customer\'s bank'],
    ['UPICC','E4041','Transaction failed due to internal exception at server/cbs end at customer\'s bank'],
    ['UPI','E4045','Transaction failed due to debit processing issue in pool account of the customer bank'],
    ['UPI','E408','Transaction ID you have generated is not valid'],
    ['UPICC','E4101','Transaction failed due to technical issue at Issuer/Acquirer end'],
    ['UPI','E4101','Transaction failed due to technical issue at Issuer/Acquirer end'],
    ['UPI','E4102','Transaction failed due to customer not notified of the transaction'],
    ['UPI','E4106','Transaction failed due to recurrence pattern, value and amount rule mismatch'],
    ['UPI','E4108','Transaction failed as mandate is paused by the user'],
    ['UPI','E4109','Transaction failed as mandate is already honoured'],
    ['UPI','E4110','Transaction failed as mandate is revoked by the user'],
    ['UPI','E4111','Transaction failed as mandate is expired'],
    ['UPI','E4114','Transaction failed as umn details does not exist at customer\'s end'],
    ['UPI','E4115','Transaction failed as mandate request limit is breached'],
    ['UPI','E4116','Transaction failed as mandate amount is higher than allowed by customer\'s application'],
    ['UPI','E4118','Transaction failed due to duplicate mandate request'],
    ['UPI','E4121','Transaction failed as mandate is not allowed to be created on this merchant'],
    ['UPI','E4122','Transaction failed as execution day and execution rule mismatch'],
    ['UPI','E4125','Transaction declined as customer account has changed'],
    ['UPI','E4138','Transaction failed as payer and payee account cannot be same'],
    ['UPI','E4142','Debit failed due to timeout at customer\'s bank'],
    ['UPICC','E4142','Debit failed due to timeout at customer\'s bank'],
    ['UPI','E4143','Transaction failed as merchant is reported SPAM by the customer'],
    ['UPICC','E4146','Transaction not allowed from overdraft account'],
    ['UPIPPI','E4146','Transaction not allowed from overdraft account'],
    ['UPI','E4146','Transaction not allowed from overdraft account'],
    ['UPICC','E4147','Transaction failed as customer is not active on UPI'],
    ['UPI','E4147','Transaction failed as customer is not active on UPI'],
    ['UPI','E4149','Transaction request declined as merchant is blocked by the customer'],
    ['UPI','E4150','Transaction declined due to duplicate request'],
    ['UPI','E4151','Transaction failed due to amount limit on merchant exceeded'],
    ['UPICC','E4152','Transaction failed due to debit limit on customer exceeded'],
    ['UPI','E4152','Transaction failed due to debit limit on customer exceeded'],
    ['UPIPPI','E4152','Transaction failed due to debit limit on customer exceeded'],
    ['UPICC','E4158','Transaction failed due to timeout at acquirer\'s end'],
    ['UPIPPI','E4158','Transaction failed due to timeout at acquirer\'s end'],
    ['UPI','E4158','Transaction failed due to timeout at acquirer\'s end'],
    ['UPI','E4166','Transaction failed as handle used is not registered'],
    ['UPI','E4167','Transaction failed as authorisation acknowledgement not received'],
    ['UPI','E4168','Transaction declined by the customer'],
    ['UPIPPI','E4168','Transaction declined by the customer'],
    ['UPICC','E4168','Transaction declined by the customer'],
    ['UPI','E4177','Debit failed due to technical issue at customer\'s bank'],
    ['UPICC','E4177','Debit failed due to technical issue at customer\'s bank'],
    ['UPICC','E4178','Transaction failed due to technical error at customer\'s application'],
    ['UPIPPI','E4178','Transaction failed due to technical error at customer\'s application'],
    ['UPI','E4178','Transaction failed due to technical error at customer\'s application'],
    ['UPICC','E4179','Transaction failed as debit failed from the customer\'s account'],
    ['UPI','E4179','Transaction failed as debit failed from the customer\'s account'],
    ['UPI','E4180','Credit failed due to technical issue at acquirer\'s bank'],
    ['UPICC','E4180','Credit failed due to technical issue at acquirer\'s bank'],
    ['UPIPPI','E4180','Credit failed due to technical issue at acquirer\'s bank'],
    ['UPI','E4197','Transaction failed as original transaction details not found during status check'],
    ['UPI','E4218','Transaction failed due to collect request expired'],
    ['UPICC','E4220','MERCHANT CREDIT NOT SUPPORTED IN IMPS'],
    ['UPI','E4242','PAYEE VPA AADHAAR OR IIN VPA IS DISABLED'],
    ['UPICC','E4259','Transaction failed due to internal exception at server/cbs end at acquirer\'s bank'],
    ['UPI','E4259','Transaction failed due to internal exception at server/cbs end at acquirer\'s bank'],
    ['UPI','E4263','OTHER BANK/PSP IS NOT SUPPORTED IN 2 VERSION'],
    ['UPI','E4271','Mandate request declined by the customer'],
    ['UPI','E4272','Transaction declined due to timeout at Issuer/Acquirer end'],
    ['UPI','E4273','Transaction failed due to mandate request expired'],
    ['UPI','E4278','Transaction failed as mandate setup failed from customer\'s bank'],
    ['UPI','E4279','Transaction declined due to timeout at customer\'s bank'],
    ['UPI','E4283','RESPMANDATE ACK NOT RECEIVED FROM PAYER'],
    ['UPI','E4284','REQMANDATECONFIRMATION ACK NOT RECEIVED FROM PAYER'],
    ['UPI','E4285','PAYER PSP NOT AVAILABLE'],
    ['UPI','E4286','PAYEE PSP NOT AVAILABLE'],
    ['UPI','E4288','PAYER PSP NOT REGISTERED'],
    ['UPI','E4292','Transaction declined due to timeout at Issuer\'s end'],
    ['UPI','E4293','Transaction declined as mandate amount limit exceeded'],
    ['UPI','E4294','Transaction declined due to timeout at Issuer/Customer\'s end'],
    ['UPICC','E4294','Transaction declined due to timeout at Issuer/Customer\'s end'],
    ['UPI','E4295','Transaction failed as vpa is not valid/expired'],
    ['UPI','E4299','PIN Cred Block is missing (txns < 2000 and Seq No = 1)'],
    ['UPI','E4309','Transaction failed as mandate signature is tampered'],
    ['UPI','E4312','Transaction failed as number of mandates allowed exceeded'],
    ['UPI','E4313','MANDATE REGISTRATION NOT ALLOWED FOR CC PF PPF ACT (BANK\'S POLICY)'],
    ['UPI','E4314','Transaction failed as debit not allowed'],
    ['UPI','E4315','PAYMENT STOPPED BY COURT ORDER'],
    ['UPI','E4319','DUPLICATE MANDATE REQUEST FOR SAME ITEM'],
    ['UPI','E4336','INVALID AMOUNT (REMITTER)'],
    ['UPICC','E4340','Transaction failed due to account details not found at customer\'s bank'],
    ['UPI','E4340','Transaction failed due to account details not found at customer\'s bank'],
    ['UPICC','E4341','Transaction failed due to account details not found at acquirer\'s bank'],
    ['UPI','E4341','Transaction failed due to account details not found at acquirer\'s bank'],
    ['UPI','E4342','REQUESTED FUNCTION NOT SUPPORTED (REMITTER)'],
    ['UPI','E4343','REQUESTED FUNCTION NOT SUPPORTED (BENEFICIARY)'],
    ['UPICC','E4346','Transaction failed due to no card details from customer\'s bank'],
    ['UPI','E4346','Transaction failed due to no card details from customer\'s bank'],
    ['UPI','E4352','Transaction failed due to CBS cut-off at customer\'s bank'],
    ['UPI','E4356','NO FINANCIAL ADDRESS RECORD FOUND'],
    ['UPI','E4357','Transaction failed due to customer\'s bank CBS offline'],
    ['UPICC','E4357','Transaction failed due to customer\'s bank CBS offline'],
    ['UPI','E4358','Transaction failed due to acquirers bank CBS offline'],
    ['UPICC','E4359','Transaction failed due to lost or stolen card from customer\'s bank'],
    ['UPI','E4359','Transaction failed due to lost or stolen card from customer\'s bank'],
    ['UPICC','E4363','Transaction declined due to customer\'s account blocked or frozen'],
    ['UPI','E4363','Transaction declined due to customer\'s account blocked or frozen'],
    ['UPIPPI','E4364','Transaction declined due to acquirer\'s account blocked or frozen'],
    ['UPICC','E4364','Transaction declined due to acquirer\'s account blocked or frozen'],
    ['UPI','E4364','Transaction declined due to acquirer\'s account blocked or frozen'],
    ['UPIPPI','E4365','Transaction declined due to merchant error'],
    ['UPICC','E4365','Transaction declined due to merchant error'],
    ['UPI','E4365','Transaction declined due to merchant error'],
    ['UPI','E4367','INVALID RESPONSE CODE'],
    ['UPICC','E4367','INVALID RESPONSE CODE'],
    ['UPI','E4369','Transaction declined as count of transactions increased as set by customer\'s bank'],
    ['UPICC','E4369','Transaction declined as count of transactions increased as set by customer\'s bank'],
    ['UPI','E4371','Transaction declined due to invalid merchant details'],
    ['UPICC','E4371','Transaction declined due to invalid merchant details'],
    ['UPI','E4373','VALIDATION ERROR'],
    ['UPICC','E4373','VALIDATION ERROR'],
    ['UPICC','E4374','Transaction not allowed on VPA by customer application'],
    ['UPIPPI','E4374','Transaction not allowed on VPA by customer application'],
    ['UPI','E4374','Transaction not allowed on VPA by customer application'],
    ['UPI','E4375','TRANSACTION NOT PERMITTED TO DEVICE'],
    ['UPICC','E4378','Transaction declined due to risk score by beneficiary bank'],
    ['UPICC','E4389','LIMIT EXCEEDED FOR REMITTING BANK/ISSUING BANK'],
    ['UPI','E4389','LIMIT EXCEEDED FOR REMITTING BANK/ISSUING BANK'],
    ['UPI','E4391','Transaction failed due to customer\'s account being inactive or dormant'],
    ['UPICC','E4391','Transaction failed due to customer\'s account being inactive or dormant'],
    ['UPIPPI','E4391','Transaction failed due to customer\'s account being inactive or dormant'],
    ['UPICC','E4803','Transaction failed as amount should always be positive'],
    ['UPIPPI','E4803','Transaction failed as amount should always be positive'],
    ['UPI','E4803','Transaction failed as amount should always be positive'],
    ['UPIPPI','E500','Transaction failed due to invalid params shared by the merchant'],
    ['UPI','E500','Transaction failed due to invalid params shared by the merchant'],
    ['UPICC','E500','Transaction failed due to invalid params shared by the merchant'],
    ['UPI','E501','Card authentication failure'],
    ['UPI','E502','Third Party Funds Transfer facility and Secure Access not enabled.'],
    ['UPI','E507','Credit card used in Debit Card PG.'],
    ['UPICC','E700','Bank failed to authenticate the customer due to 3D Secure Enrollment decline'],
    ['UPI','E700','Bank failed to authenticate the customer due to 3D Secure Enrollment decline'],
    ['UPIPPI','E700','Bank failed to authenticate the customer due to 3D Secure Enrollment decline'],
    ['UPI','E706','You do not have sufficient credit limit to complete this transaction.'],
    ['UPICC','E706','You do not have sufficient credit limit to complete this transaction.'],
    ['UPIPPI','E706','You do not have sufficient credit limit to complete this transaction.'],
    ['UPI','E708','Transaction failed. Page expired due to no user input.'],
    ['UPICC','E708','Transaction failed. Page expired due to no user input.'],
    ['UPI','E710','Transaction failed due to incorrect user action.'],
    ['UPICC','E710','Transaction failed due to incorrect user action.'],
    ['UPI','E803','S2S flow not enabled on selected payment gateway'],
    ['UPI','E905','Transaction declined due to either incorrect cvv/expiry or card validation failure'],
    ['UPI','E909','Transaction time out']
  ]}
  placeholder="Search"
/>

<br />
