---
title: Transaction Stages - Error References on Field7 & Field8
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
The PayU error mappings documentation page provides a reference guide for various error codes in the PayU payment system. The page includes:

* [Field Error code structure](#field-error-code-structure): Explains how error codes are formatted and what different components mean
* **Field7 Error Code Mapping** - Contains error codes like ALT_ID_PROV_ERROR, 3DS_METHOD_POSITIVE, etc., with their descriptions, platform layers, and API layers for the following payment modes:
  * [Field7 for Card payments](#field7-for-card-payments)
  * [Field 7 for Net Banking/Wallet payments](#field-7-for-net-bankingwallet-payments)

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

# Field Error code structure

To understand the error codes, you need to read the Error Code Object sent in the Response structure or stored in database. 

1. **Field7 – Execution Leg**: This field is used to understand at which execution stage (or leg) the transaction got declined. It is essentially a forward leg or process leg of an API that identifies the point of transaction failure. Refer to following sub-sections for understanding this field values:
   * [Field7 for Card payments](#field7-for-card-payments)
   * [Field 7 for Net Banking/Wallet payments](#field-7-for-net-bankingwallet-payments)
2. **Field8 – Bank or Wallet's Reason**: This field captures the actual reason for the transaction failure as provided by the bank.  
   It gives direct feedback or error information from the bank's end.
3. **Field9 – PayU's Error Translation**: This field contains the PayU-translated version of the error recorded in Field8.  
   It provides a simplified and standardized interpretation of the error for easier understanding and debugging.
4. **Error Code**: Represents PayU's error code mapped to the specific issue. It acts as a unique identifier for the error.
5. **Error Message**: This contains PayU's error interpretation, which elaborates on or describes the error in a user-friendly manner to assist in troubleshooting.

## Field7 for Card payments

| Field7 | Description | Expanded Description | Platform Layer | API Layer |
| ------ | ----------- | -------------------- | -------------- | --------- |
| ALT_ID_PROV_ERROR | Alt Provisioning API Failure | Occurs when the alternative ID generation API encounters a technical failure. This typically happens due to network issues, system unavailability, or invalid request parameters. The system cannot generate token/alternate ID for the card details. | Network | Alt ID Generation |
| ALT_ID_PROV_NEGATIVE | Alt Provisioning Failure | Indicates that while the API itself worked correctly, the attempt to provision an alternative ID was unsuccessful. This may be due to invalid card details, issuer restrictions, or the card being ineligible for tokenization. | Network | Alt ID Generation |
| 3DS_METHOD_POSITIVE | When 3DS2 Method response is received at NotificationURL (RECEIVED) | Confirms successful receipt of the 3DS2 method data from the Access Control Server (ACS) at PayU's notification URL. This is a positive indicator that the 3D Secure authentication process is proceeding correctly. | Authentication | Transaction Requested |
| 3DS_METHOD_NEGATIVE | When 3DS Method is Shared but No Response on Notification | Indicates that while the 3DS method data was successfully sent to the ACS, PayU did not receive any response back at the notification URL within the expected timeframe. This could be due to network issues, ACS timeout, or browser-related problems. | Authentication | Transaction Requested |
| 3DS_METHOD_ERROR | When 3DS2 Method Failure | Signifies a technical failure during the 3DS2 method process. This could be due to incorrect 3DS configurations, communication errors with the Directory Server, or invalid 3DS parameters being passed. | Authentication | Transaction Requested |
| REDIRECT | Whenever PayU S2S interim response sent to Merchant or Customer | Occurs when a server-to-server (S2S) interim response is sent from PayU to either the merchant system or customer browser, indicating that the flow requires a redirect to complete the payment process. This is a transitional state rather than an error. | Merchant / PayU | Merchant S2S Response is Shared by PayU |
| AUCPOSITIVE | When Authentication is successful and 3DS Status=Y | Indicates that cardholder authentication was completed successfully and approved by the issuing bank with a "Y" (Yes) status. This means the customer has been verified through the 3D Secure process. | Authentication | Authentication Attempted |
| AUCNEGATIVE | When Authentication is failed and 3DS Status=N,U | Occurs when authentication fails with status "N" (No - authentication failed) or "U" (Unable to authenticate). This may happen when the cardholder enters incorrect authentication details or the issuer rejects the authentication attempt. | Authentication | Authentication Attempted |
| AUCINVALID | Authentication stage was completed but internal error caused it to fail | Indicates that while the authentication process reached completion, an internal system error prevented successful processing of the authentication result. This could be due to data parsing errors, database issues, or internal service failures. | Authentication | Authentication Attempted |
| AUCERROR | When there is an error is authentication call (ex. Submit otp) | Occurs when there's a technical error during an authentication action, such as when submitting an OTP. This could be due to invalid OTP format, transmission errors, or timeout issues in the authentication service. | Authentication | Authentication Attempted |
| ACS_REDIRECT | When ACS URL along with Creq is binded and sent to Customer or Merchant | Indicates that the customer is being redirected to the Access Control Server (ACS) URL with the Challenge Request (Creq) parameter for 3DS challenge flow. This is a normal part of the 3D Secure process for transactions requiring additional verification. | Authentication | Bank OTP Page |
| 3DS_CHALLENGE_POSITIVE | When received authentication response from ACS on our TermURL | Occurs when the Access Control Server (ACS) returns a positive authentication response to PayU's termination URL after the cardholder successfully completes the challenge (e.g., enters correct OTP or completes biometric verification). | Authentication | Authentication Success |
| 3DS_CHALLENGE_NEGATIVE | When received authentication response Negative from ACS on our TermURL | Indicates that the ACS returned a negative authentication response to PayU's termination URL. This typically happens when the cardholder fails to correctly complete the challenge (e.g., enters wrong OTP multiple times or cancels the authentication). | Authentication | Authentication Failed |
| 3DS_CHALLENGE_ERROR | When received authentication No response from ACS on our TermURL | Occurs when PayU does not receive any response from the ACS at the termination URL after the challenge was initiated. This could be due to timeout, network issues, or the customer closing the browser during authentication. | Authentication | Authentication Failed |
| AUTHPOSITIVE | Authentication with subsequent authorization call was successful. | Indicates that both the authentication (3DS) and subsequent authorization (payment approval) processes were successful. The payment has been approved by the issuing bank and funds have been reserved for the transaction. | Authorization | Authorization Success |
| AUTHNEGATIVE | Authentication was successful but subsequent authorization call failed. | Occurs when cardholder authentication succeeds, but the subsequent authorization request to the issuing bank is declined. This could be due to insufficient funds, spending limits, or other bank-side restrictions. | Authorization | Authorization Failed |
| AUTHERROR | When there is an error is authentication call (ex. Submit otp) | Indicates a technical error occurred during the authorization process. This could be due to gateway timeouts, network issues with the issuing bank, or internal processing errors in the authorization service. | Authorization | Authorization Failed |

## Field 7 for Net Banking/Wallet payments

| Field7 | Description | Expanded Description | Platform Layer | API Layer |
| ------ | ----------- | -------------------- | -------------- | --------- |
| INTERROR | When no response received from the bank | Occurs when PayU initiates a payment request to the bank or payment processor, but does not receive any response within the expected timeframe. This typically indicates network connectivity issues, bank system downtime, or a timeout in the communication channel between PayU and the bank. | PayU | _payment |
| INTNEGATIVE | When wrong IBIBO code is used | Indicates that an incorrect IBIBO code (internal payment method identifier) was used in the transaction request. This usually happens when there's a mismatch between the payment method selected and the code sent in the API, or when using obsolete or invalid payment method codes. | PayU | _payment |
| REDIRECT | For seamless link to redirect posted to merchant For non seamless users the user was redirected to the bank page | A status indicating that either: 1) In seamless integration, a redirect URL has been generated and provided to the merchant to forward to the customer, or 2) In non-seamless integration, the customer has been automatically redirected to the bank/wallet payment page. This is a transitional state showing that the payment flow has moved to the next stage. | Bank / Wallet | Connected to Bank / Wallet page |
| TXNPOSITIVE | Callback received from the bank - Positive identification | Indicates that the bank or wallet provider has sent a positive callback to PayU confirming that the payment was successful. The funds have been debited from the customer's account and the transaction has been approved by the issuing bank/wallet. | Bank / Wallet | Banking / Wallet Response |
| TXNNEGATIVE | Callback received from the bank - Negative identification | Occurs when the bank or wallet provider sends a negative callback to PayU, indicating that the payment was declined or rejected. This could be due to insufficient funds, incorrect payment details, expired cards, or the customer canceling the transaction at the bank's end. | Bank / Wallet | Banking / Wallet Response |
| TXNERROR | Callback not received or technical error \| Null Response received | Indicates either: 1) No callback was received from the bank/wallet within the expected timeframe, or 2) The callback received contained technical errors or null values in critical fields. This represents a broken payment flow where the final status could not be determined, requiring verification. | Bank / Wallet | Banking / Wallet Response |
| TXNPENDING | For corp transaction Maker has made the transaction. Checker yet to approve | Specific to corporate banking transactions with dual authorization flows. This status indicates that the transaction initiator (Maker) has created the payment, but it is awaiting approval from an authorized approver (Checker) at the corporate entity before being processed by the bank. | Bank / Wallet | Banking / Wallet Response |
| VERPOSITIVE | Positive status in the verification call | Occurs when PayU makes a verification call to the bank/wallet to confirm the status of a transaction, and receives confirmation that the transaction was successful. This is often used when the initial callback status was unclear or when reconciling transaction statuses. | Bank / Wallet | Banking / Wallet Verification |
| VERNEGATIVE | Negative status in the verification call | Indicates that a verification call to the bank/wallet confirmed that the transaction was declined or failed. This typically happens during status verification of transactions where the initial callback was missed or when confirming the final status of a TXNPENDING or TXNERROR transaction. | Bank / Wallet | Banking / Wallet Verification |
| VERERROR | Technical error with the verification call | Occurs when a technical error prevents PayU from successfully making or processing a verification call to the bank/wallet. This could be due to API errors, network issues, or invalid parameters in the verification request. The transaction status remains uncertain and may require manual reconciliation. | Bank / Wallet | Banking / Wallet Verification |
| VERPENDING | For corp transaction Maker has made the transaction. Checker yet to approve | This status appears during verification calls for corporate transactions where the initiator (Maker) has created the payment, but the transaction is still awaiting approval from the authorized approver (Checker). The verification confirms that the transaction is in a legitimate waiting state. | Bank / Wallet | Banking / Wallet Verification |
| AUTOREFUND | When transaction is auto refunded (Not applicable to corp) | Indicates that a transaction was automatically refunded by PayU due to policy-based triggers or system detection of issues. This could occur due to duplicate transactions, timeout issues where money was debited but PayU didn't receive confirmation, or other predefined scenarios requiring automatic reversal. | PayU | Banking / Wallet Verification |
| OTPSEND | OnUs OTP at PayU's end and PayU requested for an OTP Generation | Occurs when PayU's own authentication system (rather than the bank's) generates and sends a One-Time Password to the customer for transaction verification. This is used in certain payment flows where PayU manages the additional authentication layer. | PayU | PayU |
| OTPERROR | OnUs OTP at PayU's end and occurred error while completing above 2 stages | Indicates a technical failure in PayU's internal OTP generation or verification process. This could be due to SMS delivery failures, invalid phone numbers, system errors in OTP validation, or timeouts in the OTP verification process. | PayU | PayU |
