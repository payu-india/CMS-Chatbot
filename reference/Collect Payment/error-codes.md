---
title: Error Codes
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
The following are possible errors and error codes for a transaction. You need to remember the following while error handling based on payment response:

* The **PayU Error Code** column in the following table corresponds to the value returned in the **error** parameter of the payment response
* The **error_message / message** column in the following table corresponds to the value returned in the **error_message / message** parameter of the payment response

<Callout icon="📘" theme="info">
  **Note**: The reason for failure depends upon the error codes provided by different banks and hence the detailing of error reasons may differ from one transaction to another.
</Callout>

<Callout icon="❗️" theme="error">
  **Transaction Stages Error handling**: For error references on during various transaction stages in Net Banking, Cards and Wallets, refer to [Transaction Stages - Error References on Field7 & Field8](#transaction-stages-error-references-field7-field8).
</Callout>

| PayU Error Code | error_message / message                                                                                                                                                                                                                          | error_description                                                                    | title                                                                                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E1620           | Payment Method Enforced and wrong method selected                                                                                                                                                                                                | WRONG_PAYMENT_METHOD_SELECTED                                                        | WRONG_PAYMENT_METHOD_SELECTED                                                                                                                                    |
| E907            | Wrong payment method selected.                                                                                                                                                                                                                   | WRONG_PAYMENT_METHOD                                                                 | WRONG_PAYMENT_METHOD                                                                                                                                             |
| E4318           | WITHDRAWAL STOPPED OWING TO LUNACY OF ACCOUNT HOLD                                                                                                                                                                                               | WITHDRAWAL STOPPED OWING TO LUNACY OF ACCOUNT HOLD                                   | WITHDRAWAL_STOPPED_OWING_TO_LUNACY_OF_ACCOUNT_HOLD                                                                                                               |
| E4317           | WITHDRAWAL STOPPED OWING TO INSOLVENCY OF ACCOUNT                                                                                                                                                                                                | WITHDRAWAL STOPPED OWING TO INSOLVENCY OF ACCOUNT                                    | WITHDRAWAL_STOPPED_OWING_TO_INSOLVENCY_OF_ACCOUNT                                                                                                                |
| E4316           | WITHDRAWAL STOPPED OWING TO DEATH OF ACCOUNT HOLDER                                                                                                                                                                                              | WITHDRAWAL STOPPED OWING TO DEATH OF ACCOUNT HOLDER                                  | WITHDRAWAL_STOPPED_OWING_TO_DEATH_OF_ACCOUNT_HOLDER                                                                                                              |
| E4684           | VPA is not available for transaction                                                                                                                                                                                                             | VPA is not available for transaction                                                 | VPA_Is_Not_Available_For_Transaction                                                                                                                             |
| E4685           | VPA is available for transaction                                                                                                                                                                                                                 | VPA is available for transaction                                                     | VPA_Is_Available_For_Transaction                                                                                                                                 |
| E224            | Virtual Account Number Mismatch                                                                                                                                                                                                                  | VIRTUAL_ACCOUNT_NUMBER_MISMATCH                                                      | VIRTUAL_ACCOUNT_NUMBER_MISMATCH                                                                                                                                  |
| E1649           | VIP Approval                                                                                                                                                                                                                                     | VIP_APPROVAL                                                                         | VIP_APPROVAL                                                                                                                                                     |
| E4251           | VERSION/TAGS SENT NOT SUPPORTED BY PSP/BANK                                                                                                                                                                                                      | VERSION/TAGS SENT NOT SUPPORTED BY PSP/BANK                                          | VERSION_TAGS_SENT_NOT_SUPPORTED_BY_PSP_BANK                                                                                                                      |
| E4530           | Mandate request failed as start date is less than current date                                                                                                                                                                                   | Validity start date should not be less than current date                             | Validity_Start_Date_Should_Not_Be_Less_Than_Current_Date                                                                                                         |
| E4531           | Mandate request failed as end date is less than start date                                                                                                                                                                                       | Validity end date should not be less than validity start date                        | Validity_End_Date_Should_Not_Be_Less_Than_Validity_Start_Date                                                                                                    |
| E4156           | VALIDATION ERROR                                                                                                                                                                                                                                 | VALIDATION ERROR                                                                     | VALIDATION_ERROR                                                                                                                                                 |
| E4373           | VALIDATION ERROR                                                                                                                                                                                                                                 | VALIDATION ERROR                                                                     | VALIDATION_ERROR_1                                                                                                                                               |
| E4221           | VAE FAILED                                                                                                                                                                                                                                       | VAE FAILED                                                                           | VAE_FAILED                                                                                                                                                       |
| E705            | Bank declined to process the transaction due to user permissions set for the card.                                                                                                                                                               | USER_PROFILE_SETTINGS_ERROR                                                          | USER_PROFILE_SETTINGS_ERROR                                                                                                                                      |
| E4255           | URL VERSION MISMATCHED (NEG ACK FOR RESPAUTH. ERROR CODE U18 IN FINAL RESPPAY.)                                                                                                                                                                  | URL VERSION MISMATCHED (NEG ACK FOR RESPAUTH. ERROR CODE U18 IN                      | URL_VERSION_MISMATCHED_NEG_ACK_FOR_RESPAUTH__ERROR_CODE_U18_IN_FINAL_RESPPAY                                                                                     |
| E500            | Bank failed to authenticate the customer                                                                                                                                                                                                         | UNKNOWN_ERROR_PG                                                                     | UNKNOWN_ERROR_PG                                                                                                                                                 |
| E908            | International cards not allowed                                                                                                                                                                                                                  | UNKNOWN_BINS_NO_ACTIVE_PG_ASSIGNED                                                   | UNKNOWN_BINS_NO_ACTIVE_PG_ASSIGNED                                                                                                                               |
| E1634           | Unique Constraint failure from the bank                                                                                                                                                                                                          | UNIQUE_CONSTRAINT_FAILURE                                                            | UNIQUE_CONSTRAINT_FAILURE                                                                                                                                        |
| E9209           | Unacceptable Transaction Fee                                                                                                                                                                                                                     | Unacceptable Transaction Fee                                                         | UNACCEPTABLE_TRANSACTION_FEE                                                                                                                                     |
| E1608           | Unable to process the request.                                                                                                                                                                                                                   | UNABLE_TO_PROCESS                                                                    | UNABLE_TO_PROCESS                                                                                                                                                |
| E4385           | UNABLE TO PROCESS REVERSAL                                                                                                                                                                                                                       | UNABLE TO PROCESS REVERSAL                                                           | UNABLE_TO_PROCESS_REVERSAL                                                                                                                                       |
| E4041           | Transaction failed due to internal exception at server/cbs end at customer's bank                                                                                                                                                                | UNABLE TO PROCESS DUE TO INTERNAL EXCEPTION AT SERVER/CBS/ETC ON                     | UNABLE_TO_PROCESS_DUE_TO_INTERNAL_EXCEPTION_AT_SERVER_CBS_ETC_ON_REMITTER_SIDE                                                                                   |
| E4259           | Transaction failed due to internal exception at server/cbs end at acquirer's bank                                                                                                                                                                | UNABLE TO PROCESS DUE TO INTERNAL EXCEPTION AT SERVER/CBS/ETC ON                     | UNABLE_TO_PROCESS_DUE_TO_INTERNAL_EXCEPTION_AT_SERVER_CBS_ETC_ON_BENEFICIARY_TD_SIDE                                                                             |
| E4044           | Transaction failed due to credit processing issue in pool account of the acquriing bank                                                                                                                                                          | UNABLE TO PROCESS CREDIT FROM BANK'S POOL/BGL ACCOUNT                                | UNABLE_TO_PROCESS_CREDIT_FROM_BANK_S_POOL_BGL_ACCOUNT                                                                                                            |
| E4045           | Transaction failed due to debit processing issue in pool account of the customer bank                                                                                                                                                            | UNABLE TO PROCESS CREDIT FROM BANK'S POOL/BGL ACCOUNT                                | UNABLE_TO_PROCESS_DEBIT_IN_BANK_S_POOL_BGL_ACCOUNT                                                                                                               |
| E4102           | Transaction failed due to customer not notified of the transaction                                                                                                                                                                               | Unable to Notify the Customer                                                        | Unable_To_Notify_The_Customer                                                                                                                                    |
| E9211           | Unable to Locate Record on File                                                                                                                                                                                                                  | Unable to Locate Record on File                                                      | UNABLE_TO_LOCATE_RECORD_ON_FILE                                                                                                                                  |
| E9225           | Unable to Dispense                                                                                                                                                                                                                               | Unable to Dispense                                                                   | UNABLE_TO_DISPENSE                                                                                                                                               |
| E9240           | Unable to Authorise                                                                                                                                                                                                                              | Unable to Authorise                                                                  | UNABLE_TO_AUTHORISE                                                                                                                                              |
| E4114           | Transaction failed as umn details doesn't exist at customer's end                                                                                                                                                                                | UMN DOES NOT EXIST (PAYER)                                                           | UMN_DOES_NOT_EXIST_PAYER                                                                                                                                         |
| E4128           | Transaction failed as umn details doesn't exist at acquiring bank's end                                                                                                                                                                          | UMN DOES NOT EXIST (PAYEE)                                                           | UMN_DOES_NOT_EXIST_PAYEE                                                                                                                                         |
| E4227           | UIDAI FAILURE                                                                                                                                                                                                                                    | UIDAI FAILURE                                                                        | UIDAI_FAILURE                                                                                                                                                    |
| E2101           | Transaction could not be processed because offer is not applicable.                                                                                                                                                                              | TXN_FAILURE_FOR * INVALID_OFFER                                                      | TXN_FAILURE_FOR_INVALID_OFFER                                                                                                                                    |
| E2201           | splitRequest param sent for non-aggregator merchant                                                                                                                                                                                              | TXN_FAILED_AGGREGATOR * TXN_NOT_ALLOWED                                              | TXN_FAILED_AGGREGATOR_TXN_NOT_ALLOWED                                                                                                                            |
| E2202           | Invalid split provided in transaction request.                                                                                                                                                                                                   | TXN_FAILED_AGGREGATOR * INVALID_SPLIT_PROVIDED                                       | TXN_FAILED_AGGREGATOR_INVALID_SPLIT_PROVIDED                                                                                                                     |
| E1101           | Transaction failed due to invalid params shared by the merchant                                                                                                                                                                                  | TXN_DETAIL_INVALID * REDIRECTING_TO_MERCHANT                                         | TXN_DETAIL_INVALID_REDIRECTING_TO_MERCHANT                                                                                                                       |
| E4112           | Transaction failed as mandate and transaction amount is different                                                                                                                                                                                | TXN AMOUNT DIFFERS FROM MANDATE AMOUNT                                               | TXN_AMOUNT_DIFFERS_FROM_MANDATE_AMOUNT                                                                                                                           |
| E9234           | TVR validation failed by Issuer                                                                                                                                                                                                                  | TVR validation failed by Issuer                                                      | TVR_VALIDATION_FAILED_BY_ISSUER                                                                                                                                  |
| E227            | Transaction is Pending                                                                                                                                                                                                                           | TRANSACTION_PENDING                                                                  | TRANSACTION_PENDING                                                                                                                                              |
| E306            | Card authentication failure                                                                                                                                                                                                                      | TRANSACTION_INVALID_PG                                                               | TRANSACTION_INVALID_PG                                                                                                                                           |
| E229            | Transaction declined as no prior EMI transaction exists here                                                                                                                                                                                     | TRANSACTION_INVALID * EMI_BASE_ID                                                    | TRANSACTION_INVALID_EMI_BASE_ID                                                                                                                                  |
| E308            | Transaction Failed at bank end.                                                                                                                                                                                                                  | TRANSACTION_FAILED                                                                   | TRANSACTION_FAILED                                                                                                                                               |
| E507            | Transaction Expired                                                                                                                                                                                                                              | TRANSACTION_EXPIRED                                                                  | TRANSACTION_EXPIRED                                                                                                                                              |
| E231            | Transaction was marked as dropped                                                                                                                                                                                                                | TRANSACTION_DROPPED                                                                  | TRANSACTION_DROPPED                                                                                                                                              |
| E408            | Transaction failed. Page expired due to no user input.                                                                                                                                                                                           | TRANSACTION_BOUNCED                                                                  | TRANSACTION_BOUNCED                                                                                                                                              |
| E345            | Transaction declined due to technical failure                                                                                                                                                                                                    | Transaction rejected                                                                 | TECHNICAL_FAILURE                                                                                                                                                |
| E4374           | Transaction not allowed on VPA by customer application                                                                                                                                                                                           | TRANSACTION NOT PERMITTED TO VPA by the PSP                                          | TRANSACTION_NOT_PERMITTED_TO_VPA_By_The_PSP                                                                                                                      |
| E4010           | Transaction not allowed on/from the account                                                                                                                                                                                                      | TRANSACTION NOT PERMITTED TO THE ACCOUNT                                             | TRANSACTION_NOT_PERMITTED_TO_THE_ACCOUNT                                                                                                                         |
| E1642           | Transaction not permitted to cardholder                                                                                                                                                                                                          | Transaction not permitted to issuer/cardholder                                       | CARD_NOT_PERMITTED                                                                                                                                               |
| E4375           | TRANSACTION NOT PERMITTED TO DEVICE                                                                                                                                                                                                              | TRANSACTION NOT PERMITTED TO DEVICE                                                  | TRANSACTION_NOT_PERMITTED_TO_DEVICE                                                                                                                              |
| E4348           | TRANSACTION NOT PERMITTED TO CARDHOLDER (REMITTER)                                                                                                                                                                                               | Transaction not permitted to cardholder                                              | TRANSACTION_NOT_PERMITTED_TO_CARDHOLDER_REMITTER                                                                                                                 |
| E4146           | Transaction not allowed from overdraft account                                                                                                                                                                                                   | TRANSACTION NOT PERMITTED FOR THIS A/C TYPE (OD)                                     | TRANSACTION_NOT_PERMITTED_FOR_THIS_A_C_TYPE_OD                                                                                                                   |
| E4931           | Transaction is in `value` state                                                                                                                                                                                                                  | Transaction is in `value` state                                                      | Transaction_Is_In_Value_State                                                                                                                                    |
| E4188           | TRANSACTION IS ALREADY BEEN FAILED                                                                                                                                                                                                               | TRANSACTION IS ALREADY BEEN FAILED                                                   | TRANSACTION_IS_ALREADY_BEEN_FAILED                                                                                                                               |
| E4197           | Transaction failed as original transaction details not found during status check                                                                                                                                                                 | TRANSACTION ID IS NOT PRESENT                                                        | TRANSACTION_ID_IS_NOT_PRESENT                                                                                                                                    |
| E4155           | TRANSACTION ID IS MISMATCHED VALIDATION ERROR                                                                                                                                                                                                    | TRANSACTION ID IS MISMATCHED VALIDATION ERROR                                        | TRANSACTION_ID_IS_MISMATCHED_VALIDATION_ERROR                                                                                                                    |
| E4369           | Transaction declined as count of transactions increased as set by customer's bank                                                                                                                                                                | TRANSACTION FREQUENCY LIMIT EXCEEDED AS SET BY REMITTING MEMBER                      | TRANSACTION_FREQUENCY_LIMIT_EXCEEDED_AS_SET_BY_REMITTING_MEMBER_BD                                                                                               |
| E1655           | Transaction could not be completed due to violation of law                                                                                                                                                                                       | TRANSACTION CANNOT BE COMPLETED. COMPLIANCE VIOLATION (REMITTER)                     | DECLINING_DUE_TO_VOILATION_OF_LAW                                                                                                                                |
| E217            | This error comes when Bank does some changes in the terminal/plug-in profile of the merchant. If merchant receives this error Bank should generate new resource file and forward the same to the merchant.                                       | TRANPORTAL_ID_ERROR                                                                  | TRANPORTAL_ID_ERROR                                                                                                                                              |
| E1911           | User entered wrong VPA too many times                                                                                                                                                                                                            | TOO_MANY_WRONG_VPA                                                                   | TOO_MANY_WRONG_VPA                                                                                                                                               |
| E9226           | TID not present on host                                                                                                                                                                                                                          | TID not present on host                                                              | TID_NOT_PRESENT_ON_HOST                                                                                                                                          |
| E4516           | Refund failed as original transaction details not valid                                                                                                                                                                                          | This transaction is already processed ("ICICI", Online duplicate                     | This_Transaction_Is_Already_Processed_ICICI_Online_Duplicate_Transaction                                                                                         |
| E4119           | Revoke is not allowed for this mandate                                                                                                                                                                                                           | THIS MANDATE IS NON REVOKEABLE BD                                                    | THIS_MANDATE_IS_NON_REVOKEABLE_BD                                                                                                                                |
| E4150           | Transaction declined due to duplicate request                                                                                                                                                                                                    | THE REQUEST IS DUPLICATE                                                             | THE_REQUEST_IS_DUPLICATE                                                                                                                                         |
| E223            | Transaction not approved                                                                                                                                                                                                                         | The order has been rejected by Decision Manager                                      | TRANSACTION_REJECTED_BY_CHECKER                                                                                                                                  |
| E338            | Transaction denied because one or more risk rules failed                                                                                                                                                                                         | The customer matched the Denied Parties List                                         | RISK_RULE_FAILED                                                                                                                                                 |
| E335            | Transaction failed due to incomplete authentication process                                                                                                                                                                                      | The cardholder is enrolled in Payer Authentication. Please authe                     | AUTHENTICATION_INCOMPLETE                                                                                                                                        |
| E2405           | Sorry, you are not eligible for the selected tenure. Please select another tenure                                                                                                                                                                | TENURE_NOT_FOUND                                                                     | TENURE_NOT_FOUND                                                                                                                                                 |
| E4157           | SYSTEM EXCEPTION                                                                                                                                                                                                                                 | SYSTEM EXCEPTION                                                                     | SYSTEM_EXCEPTION                                                                                                                                                 |
| E4004           | SUSPECTED FRAUD, DECLINE/TRANSACTIONS DECLINED BASED ON RISKSCORE BY REMITTER                                                                                                                                                                    | SUSPECTED_FRAUD_DECLINE_TRANSACTIONS_DECLINED_BASED_ON_RISKSCORE_BY_REMITTER         | SUSPECTED_FRAUD_DECLINE_TRANSACTIONS_DECLINED_BASED_ON_RISKSCORE_BY_REMITTER                                                                                     |
| E9208           | Suspected Malfunction                                                                                                                                                                                                                            | Suspected Malfunction                                                                | SUSPECTED_MALFUNCTION                                                                                                                                            |
| E4378           | Transaction declined due to risk score by beneficiary bank                                                                                                                                                                                       | SUSPECTED FRAUD, DECLINE / TRANSACTIONS DECLINED BASED ON RISK S                     | SUSPECTED_FRAUD_DECLINE_TRANSACTIONS_DECLINED_BASED_ON_RISK_SCORE_BY_BD_BENEFICIARY                                                                              |
| E1611           | UserCancelled as the Transaction was left orphan during sure_pay                                                                                                                                                                                 | SURE_PAY_USER_CANCELLED                                                              | SURE_PAY_USER_CANCELLED                                                                                                                                          |
| E1613           | SurePay usercancelled                                                                                                                                                                                                                            | SURE_PAY_PROCESSED                                                                   | SURE_PAY_PROCESSED                                                                                                                                               |
| E1657           | Surcharge amount not permitted                                                                                                                                                                                                                   | SURCHARGE_AMOUNT_NOT_PERMITTED                                                       | SURCHARGE_AMOUNT_NOT_PERMITTED                                                                                                                                   |
| E000            | No Error                                                                                                                                                                                                                                         | Successful transaction                                                               | NO_ERROR                                                                                                                                                         |
| E1631           | Merchant Validation Failed                                                                                                                                                                                                                       | Sorry! Transaction could not be processed as the limit of your m                     | MERCHANT_VALIDATION_FAILED                                                                                                                                       |
| E1630           | Invalid Bank ME Code                                                                                                                                                                                                                             | Sorry! Transaction could not be processed as limit is exhausted                      | INVALID_BANK_ME_CODE                                                                                                                                             |
| E4520           | Refund failed as online refund not enabled on merchant                                                                                                                                                                                           | Sorry you canNULLt initiate refund request                                           | Sorry_You_Cant_Initiate_Refund_Request                                                                                                                           |
| E337            | Transaction declined by the issuer                                                                                                                                                                                                               | Soft Decline - The authorization request was approved by the iss                     | NOT_CAPTURED                                                                                                                                                     |
| E4025           | SIGNATURE MISMATCH                                                                                                                                                                                                                               | SIGNATURE MISMATCH                                                                   | SIGNATURE_MISMATCH                                                                                                                                               |
| E4024           | SIGNATURE ERROR                                                                                                                                                                                                                                  | SIGNATURE ERROR                                                                      | SIGNATURE_ERROR                                                                                                                                                  |
| E4093           | SHARETOPAYEE=Y FOR PAYER INITIATED IF PURPOSE=01                                                                                                                                                                                                 | SHARETOPAYEE=Y FOR PAYER INITIATED IF PURPOSE=01                                     | SHARETOPAYEE_Y_FOR_PAYER_INITIATED_IF_PURPOSE_01                                                                                                                 |
| E1658           | Service not available                                                                                                                                                                                                                            | SERVICE_NOT_AVAILABLE                                                                | SERVICE_NOT_AVAILABLE                                                                                                                                            |
| E1201           | You are not authorized to do this transaction.                                                                                                                                                                                                   | SERVICE_AUTHORIZATION_ERROR                                                          | SERVICE_AUTHORIZATION_ERROR                                                                                                                                      |
| E4147           | Transaction failed as customer is not active on UPI                                                                                                                                                                                              | Service disable on UPI/ Customer is not active                                       | Service_Disable_On_UPI__Customer_is_Not_Active                                                                                                                   |
| E4105           | Transaction failed due to recurring sequence mismatch                                                                                                                                                                                            | SEQNUM MISMATCH (PAYER PSP)                                                          | SEQNUM_MISMATCH_PAYER_PSP                                                                                                                                        |
| E1633           | Separate Authentication Failed                                                                                                                                                                                                                   | SEPARATE_AUTHENTICATION_FAILED                                                       | SEPARATE_AUTHENTICATION_FAILED                                                                                                                                   |
| E1663           | Failure received in send OTP API call                                                                                                                                                                                                            | SEND_OTP_API_FAILURE                                                                 | SEND_OTP_API_FAILURE                                                                                                                                             |
| E1670           | Card authentication failed at the bank due to invalid CVV (or CVC or Card Security Code)                                                                                                                                                         | Security violation                                                                   | ISSUER_RISK_RULE_FAILED                                                                                                                                          |
| E700            | Validation of secure hash failed                                                                                                                                                                                                                 | SECURE_HASH_FAILURE                                                                  | SECURE_HASH_FAILURE                                                                                                                                              |
| E300            | Card failed 3D authentication as 3 D Secure signatures did not match                                                                                                                                                                             | SECURE_3D_PASSWORD_ERROR                                                             | SECURE_3D_PASSWORD_ERROR                                                                                                                                         |
| E1000           | 3-D secure authentication failed.                                                                                                                                                                                                                | SECURE_3D_AUTHENTICATION_ERROR_S3A                                                   | SECURE_3D_AUTHENTICATION_ERROR_S3A                                                                                                                               |
| E317            | Payer could not be authenticated                                                                                                                                                                                                                 | SECURE_3D_AUTHENTICATION_ERROR                                                       | SECURE_3D_AUTHENTICATION_ERROR                                                                                                                                   |
| E1662           | ATM PIN monthly limit exceeded for this card. Please retry using OTP or any other payment option.                                                                                                                                                | SBI_DI_MONTHLY_CARD_LIMIT_EXCEEDED                                                   | SBI_DI_MONTHLY_CARD_LIMIT_EXCEEDED                                                                                                                               |
| E1661           | ATM PIN daily limit exceeded for this card. Please retry using OTP or any other payment option.                                                                                                                                                  | SBI_DI_DAILY_CARD_LIMIT_EXCEEDED                                                     | SBI_DI_DAILY_CARD_LIMIT_EXCEEDED                                                                                                                                 |
| E1664           | Card blocked by the issuer. Please contact the bank to get it enabled for online transactions.                                                                                                                                                   | SBI_DI_BLOCKED_CARD                                                                  | SBI_DI_BLOCKED_CARD                                                                                                                                              |
| E1615           | txn_s2s_flow missing parameter                                                                                                                                                                                                                   | S2S_PARAMETER_MISSING                                                                | S2S_PARAMETER_MISSING                                                                                                                                            |
| E1622           | S2S flow not enabled on selected payment gateway                                                                                                                                                                                                 | S2S_NOT_ENABLED_PAYMENTGATEWAY                                                       | S2S_NOT_ENABLED_PAYMENTGATEWAY                                                                                                                                   |
| E1621           | Merchant does not have access to S2S flow                                                                                                                                                                                                        | S2S_NOT_ENABLED_MERCHANT                                                             | S2S_NOT_ENABLED_MERCHANT                                                                                                                                         |
| E199            | Rreq not received from the Network Scheme                                                                                                                                                                                                        | RREQ_NOT_RECEIVED                                                                    | RREQ_NOT_RECEIVED                                                                                                                                                |
| E1654           | Route to merchant unavailable                                                                                                                                                                                                                    | ROUTE_UNAVAILABLE                                                                    | ROUTE_UNAVAILABLE                                                                                                                                                |
| E4034           | REVOKE MANDATE AFTER THE REMITTER UNBLOCKED THE AMOUNT                                                                                                                                                                                           | REVOKE MANDATE AFTER THE REMITTER UNBLOCKED THE AMOUNT                               | REVOKE_MANDATE_AFTER_THE_REMITTER_UNBLOCKED_THE_AMOUNT                                                                                                           |
| E4183           | REVERTED                                                                                                                                                                                                                                         | REVERTED                                                                             | REVERTED                                                                                                                                                         |
| E4186           | REVERSAL HAS BEEN SENT                                                                                                                                                                                                                           | REVERSAL HAS BEEN SENT                                                               | REVERSAL_HAS_BEEN_SENT                                                                                                                                           |
| E1500           | Retry not allowed                                                                                                                                                                                                                                | RETRY_NOT_ALLOWED                                                                    | RETRY_NOT_ALLOWED                                                                                                                                                |
| E1626           | Restricted card                                                                                                                                                                                                                                  | RESTRICTED CARD, DECLINE (REMITTER)                                                  | RESTRICTED_CARD_TYPE                                                                                                                                             |
| E4268           | Response ValQR TimeOut                                                                                                                                                                                                                           | Response ValQR TimeOut                                                               | Response_ValQR_TimeOut                                                                                                                                           |
| E9220           | Response Received Too Late                                                                                                                                                                                                                       | Response Received Too Late                                                           | RESPONSE_RECEIVED_TOO_LATE                                                                                                                                       |
| E4187           | RESPONSE IS ALREADY BEEN SENT                                                                                                                                                                                                                    | RESPONSE IS ALREADY BEEN SENT                                                        | RESPONSE_IS_ALREADY_BEEN_SENT                                                                                                                                    |
| E4184           | RESPONSE IS ALREADY BEEN RECEIVED                                                                                                                                                                                                                | RESPONSE IS ALREADY BEEN RECEIVED                                                    | RESPONSE_IS_ALREADY_BEEN_RECEIVED                                                                                                                                |
| E4267           | Response Activation TimeOut                                                                                                                                                                                                                      | Response Activation TimeOut                                                          | Response_Activation_TimeOut                                                                                                                                      |
| E4279           | Transaction declined due to timeout at customer's bank                                                                                                                                                                                           | RESPMANDATE TIMEOUT AT REMITTER END                                                  | RESPMANDATE_TIMEOUT_AT_REMITTER_END                                                                                                                              |
| E4278           | Transaction failed as mandate setup failed from customer's bank                                                                                                                                                                                  | RESPMANDATE DECLINED BY REMITTER BANK                                                | RESPMANDATE_DECLINED_BY_REMITTER_BANK                                                                                                                            |
| E4283           | RESPMANDATE ACK NOT RECEIVED FROM PAYER                                                                                                                                                                                                          | RESPMANDATE ACK NOT RECEIVED FROM PAYER                                              | RESPMANDATE_ACK_NOT_RECEIVED_FROM_PAYER                                                                                                                          |
| E4272           | Transaction declined due to timeout at Issuer/Acquirer end                                                                                                                                                                                       | RESPAUTHMANDATE TIMEOUT                                                              | RESPAUTHMANDATE_TIMEOUT                                                                                                                                          |
| E4275           | RESPAUTHMANDATE NEGATIVE ACK SENT FROM UPI TO PSP                                                                                                                                                                                                | RESPAUTHMANDATE NEGATIVE ACK SENT FROM UPI TO PSP                                    | RESPAUTHMANDATE_NEGATIVE_ACK_SENT_FROM_UPI_TO_PSP                                                                                                                |
| E4273           | Transaction failed due to mandate request expired                                                                                                                                                                                                | RESPAUTHMANDATE EXPIRED                                                              | RESPAUTHMANDATE_EXPIRED                                                                                                                                          |
| E4271           | Mandate request declined by the customer                                                                                                                                                                                                         | RESPAUTHMANDATE DECLINED BY PSP                                                      | RESPAUTHMANDATE_DECLINED_BY_PSP                                                                                                                                  |
| E215            | Unknown Error                                                                                                                                                                                                                                    | RESERVED_USAGE_ERROR                                                                 | RESERVED_USAGE_ERROR                                                                                                                                             |
| E9231           | Reserved for National Use                                                                                                                                                                                                                        | Reserved for National Use                                                            | RESERVED_FOR_NATIONAL_USE                                                                                                                                        |
| E4342           | REQUESTED FUNCTION NOT SUPPORTED (REMITTER)                                                                                                                                                                                                      | REQUESTED FUNCTION NOT SUPPORTED (REMITTER)                                          | REQUESTED_FUNCTION_NOT_SUPPORTED_REMITTER                                                                                                                        |
| E4343           | REQUESTED FUNCTION NOT SUPPORTED (BENEFICIARY)                                                                                                                                                                                                   | REQUESTED FUNCTION NOT SUPPORTED (BENEFICIARY)                                       | REQUESTED_FUNCTION_NOT_SUPPORTED_BENEFICIARY                                                                                                                     |
| E9218           | Requested Function not Supported                                                                                                                                                                                                                 | Requested Function not Supported                                                     | REQUESTED_FUNCTION_NOT_SUPPORTED                                                                                                                                 |
| E4200           | REQUEST REFUND IS NOT FOUND                                                                                                                                                                                                                      | REQUEST REFUND IS NOT FOUND                                                          | REQUEST_REFUND_IS_NOT_FOUND                                                                                                                                      |
| E4605           | Request Processed Successfully                                                                                                                                                                                                                   | Request Processed Successfully                                                       | Request_Processed_Successfully                                                                                                                                   |
| E4198           | REQUEST MESSAGE ID IS NOT PRESENT                                                                                                                                                                                                                | REQUEST MESSAGE ID IS NOT PRESENT                                                    | REQUEST_MESSAGE_ID_IS_NOT_PRESENT                                                                                                                                |
| E4153           | REQUEST IS NOT FOUND                                                                                                                                                                                                                             | REQUEST IS NOT FOUND                                                                 | REQUEST_IS_NOT_FOUND                                                                                                                                             |
| E4185           | REQUEST IS ALREADY BEEN SENT                                                                                                                                                                                                                     | REQUEST IS ALREADY BEEN SENT                                                         | REQUEST_IS_ALREADY_BEEN_SENT                                                                                                                                     |
| E4608           | Request has been timed out                                                                                                                                                                                                                       | Request has been timed out                                                           | Request_Has_Been_Timed_Out                                                                                                                                       |
| E4517           | Offline Refund request already raised                                                                                                                                                                                                            | Request has already been initiated for this transaction ("ICICI"                     | Request_Has_Already_Been_Initiated_For_This_Transaction_ICICI_Offline_Duplicate_Transaction                                                                      |
| E4140           | Transaction declined by the bank                                                                                                                                                                                                                 | Request Decline by the bank                                                          | Request_Decline_By_The_Bank                                                                                                                                      |
| E4196           | REQUEST DEBIT IS NOT FOUND                                                                                                                                                                                                                       | REQUEST DEBIT IS NOT FOUND                                                           | REQUEST_DEBIT_IS_NOT_FOUND                                                                                                                                       |
| E4195           | REQUEST CREDIT IS NOT FOUND                                                                                                                                                                                                                      | REQUEST CREDIT IS NOT FOUND                                                          | REQUEST_CREDIT_IS_NOT_FOUND                                                                                                                                      |
| E4170           | REQUEST AUTHORISATION IS NOT FOUND                                                                                                                                                                                                               | REQUEST AUTHORISATION IS NOT FOUND                                                   | REQUEST_AUTHORISATION_IS_NOT_FOUND                                                                                                                               |
| E4167           | Transaction failed as authorisation acknowledgement not received                                                                                                                                                                                 | REQUEST AUTHORISATION ACKNOWLEDGEMENT IS NOT                                         | REQUEST_AUTHORISATION_ACKNOWLEDGEMENT_IS_NOT                                                                                                                     |
| E4284           | REQMANDATECONFIRMATION ACK NOT RECEIVED FROM PAYER                                                                                                                                                                                               | REQMANDATECONFIRMATION ACK NOT RECEIVED FROM PAYER                                   | REQMANDATECONFIRMATION_ACK_NOT_RECEIVED_FROM_PAYER                                                                                                               |
| E4280           | REQMANDATE NEGATIVE ACK RECEIVED FROM REMITTER                                                                                                                                                                                                   | REQMANDATE NEGATIVE ACK RECEIVED FROM REMITTER                                       | REQMANDATE_NEGATIVE_ACK_RECEIVED_FROM_REMITTER                                                                                                                   |
| E4277           | REQMANDATE ACK NOT RECEIVED FROM REMITTER BANK                                                                                                                                                                                                   | REQMANDATE ACK NOT RECEIVED FROM REMITTER BANK                                       | REQMANDATE_ACK_NOT_RECEIVED_FROM_REMITTER_BANK                                                                                                                   |
| E4274           | REQAUTHMANDATE NEGATIVE ACK RECEIVED FROM PSP                                                                                                                                                                                                    | REQAUTHMANDATE NEGATIVE ACK RECEIVED FROM PSP                                        | REQAUTHMANDATE_NEGATIVE_ACK_RECEIVED_FROM_PSP                                                                                                                    |
| E4363           | Transaction declined due to customer's account blocked or frozen                                                                                                                                                                                 | REMITTING ACCOUNT BLOCKED/FROZEN                                                     | REMITTING_ACCOUNT_BLOCKED_FROZEN                                                                                                                                 |
| E4294           | Transaction declined due to timeout at Issuer/Customer's end                                                                                                                                                                                     | REMITTER/ISSUER UNAVAILABLE (TIMEOUT)                                                | REMITTER_ISSUER_UNAVAILABLE_TIMEOUT                                                                                                                              |
| E4357           | Transaction failed due to customer's bank CBS offline                                                                                                                                                                                            | REMITTER CBS OFFLINE                                                                 | REMITTER_CBS_OFFLINE                                                                                                                                             |
| E4258           | REMITTER BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK                                                                                                                                                                                            | REMITTER BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK                                | REMITTER_BANK_VERSION_TAGS_SENT_NOT_SUPPORTED_BY_BANK                                                                                                            |
| E4256           | REMITTER BANK,REQUEST & RESPONSE HEADER VERSION MISMATCH                                                                                                                                                                                         | REMITTER BANK,REQUEST & RESPONSE HEADER VERSION MISMATCH                             | REMITTER_BANK_REQUEST_RESPONSE_HEADER_VERSION_MISMATCH                                                                                                           |
| E4257           | REMITTER BANK,HEADER OR URL VERSION MISMATCHED                                                                                                                                                                                                   | REMITTER BANK,HEADER OR URL VERSION MISMATCHED                                       | REMITTER_BANK_HEADER_OR_URL_VERSION_MISMATCHED                                                                                                                   |
| E4290           | Mandate not supported by customer's bank                                                                                                                                                                                                         | REMITTER BANK NOT REGISTERED (MANDATE)                                               | REMITTER_BANK_NOT_REGISTERED_MANDATE                                                                                                                             |
| E4177           | Debit failed due to technical issue at customer's bank                                                                                                                                                                                           | REMITTER BANK NOT AVAILABLE                                                          | REMITTER_BANK_NOT_AVAILABLE                                                                                                                                      |
| E4096           | REMITTER BANK DOES NOT SUPPORT VERSION MANDATE 2.1                                                                                                                                                                                               | REMITTER BANK DOES NOT SUPPORT VERSION MANDATE 2.1                                   | REMITTER_BANK_DOES_NOT_SUPPORT_VERSION_MANDATE_2_1                                                                                                               |
| E4265           | REMITTER BANK DOES NOT SUPPORT VERSION                                                                                                                                                                                                           | REMITTER BANK DOES NOT SUPPORT VERSION                                               | REMITTER_BANK_DOES_NOT_SUPPORT_VERSION                                                                                                                           |
| E4009           | Transaction failed due to mobile number linked to account is changed                                                                                                                                                                             | REGISTERED MOBILE NUMBER LINKED TO THE ACCOUNT HAS BEEN CHANGED/                     | REGISTERED_MOBILE_NUMBER_LINKED_TO_THE_ACCOUNT_HAS_BEEN_CHANGED_REMOVED                                                                                          |
| E348            | Transaction declined by the issuer                                                                                                                                                                                                               | Refer to card issuer                                                                 | ISSUER_DECLINED                                                                                                                                                  |
| E4649           | Ref Url is not valid or proper format. e.g. [http://www.yyy.zzz](http://www.yyy.zzz)                                                                                                                                                             | Ref Url is not valid or proper format. e.g. [http://www.yyy.zzz](http://www.yyy.zzz) | Ref_Url_Is_Not_Valid_Or_Proper_Format                                                                                                                            |
| E1206           | Transaction interrupted by pressing back button                                                                                                                                                                                                  | REDIRECTED_BY_BACK_BUTTON                                                            | REDIRECTED_BY_BACK_BUTTON                                                                                                                                        |
| E4682           | Recurrence Payment is in progress                                                                                                                                                                                                                | Recurrence Payment is in progress                                                    | Recurrence_Payment_Is_In_Progress                                                                                                                                |
| E4683           | Recurrence Payment is already completed                                                                                                                                                                                                          | Recurrence Payment is already completed                                              | Recurrence_Payment_Is_Already_Completed                                                                                                                          |
| E4091           | RECURRENCE PATTERN IS ALWAYS ONETIME IF PURPOSE=01                                                                                                                                                                                               | RECURRENCE PATTERN IS ALWAYS ONETIME IF PURPOSE=01                                   | RECURRENCE_PATTERN_IS_ALWAYS_ONETIME_IF_PURPOSE_01                                                                                                               |
| E4063           | RECURRENCE PATTERN AS WELL AS FOR PAYER INITIATED                                                                                                                                                                                                | RECURRENCE PATTERN AS WELL AS FOR PAYER INITIATED                                    | RECURRENCE_PATTERN_AS_WELL_AS_FOR_PAYER_INITIATED                                                                                                                |
| E4106           | Transaction failed due to recurrence pattern, value and amount rule mismatch                                                                                                                                                                     | RECURRENCE PATTERN AND VALUE MISMATCH (PAYER)                                        | RECURRENCE_PATTERN_AND_VALUE_MISMATCH_PAYER                                                                                                                      |
| E4526           | Transaction not found in status check                                                                                                                                                                                                            | Record not found against given parameters                                            | Record_Not_Found_Against_Given_Parameters                                                                                                                        |
| E9229           | Reconciliation Totals Reset                                                                                                                                                                                                                      | Reconciliation Totals Reset                                                          | RECONCILIATION_TOTALS_RESET                                                                                                                                      |
| E1656           | Reconcile Error                                                                                                                                                                                                                                  | RECONCILE_ERROR                                                                      | RECONCILE_ERROR                                                                                                                                                  |
| E4168           | Transaction declined by the customer                                                                                                                                                                                                             | RECEIVED REQUEST AUTHORISATION IS DECLINED                                           | RECEIVED_REQUEST_AUTHORISATION_IS_DECLINED                                                                                                                       |
| E4219           | RECEIVED LATE RESPONSE                                                                                                                                                                                                                           | RECEIVED LATE RESPONSE                                                               | RECEIVED_LATE_RESPONSE                                                                                                                                           |
| E4381           | RECEIVED LATE RESPONSE                                                                                                                                                                                                                           | RECEIVED LATE RESPONSE                                                               | RECEIVED_LATE_RESPONSE_1                                                                                                                                         |
| E704            | Authorization request declined by the bank due to an internal error                                                                                                                                                                              | RECEIPT_NUMBER_ERROR                                                                 | RECEIPT_NUMBER_ERROR                                                                                                                                             |
| E4301           | Transaction failed as revoke should be allowed for recurring mandate                                                                                                                                                                             | Purpose Code=14, Revocable= N ( Revokable tag must always be Y f                     | Purpose_Code_14_Revocable_N_Revokable_Tag_Must_Always_Be_Y_For_For_SI__Recurring_Mandate_REMITTER                                                                |
| E4107           | Transaction failed as blocking of funds not allowed for recurring mandate                                                                                                                                                                        | Purpose code=14, Block fund = Y ( Block Fund must be N always fo                     | Purpose_Code_14_Block_Fund_Y_Block_Fund_Must_Be_N_Always_For_SI_Recurring_Mandate_PAYER                                                                          |
| E4292           | Transaction declined due to timeout at Issuer's end                                                                                                                                                                                              | PSP TIME-OUT                                                                         | PSP_TIME_OUT                                                                                                                                                     |
| E4202           | PSP REQUEST PAY DEBIT ACKNOWLEDGEMENT NOT RECEIVED                                                                                                                                                                                               | PSP REQUEST PAY DEBIT ACKNOWLEDGEMENT NOT RECEIVED                                   | PSP_REQUEST_PAY_DEBIT_ACKNOWLEDGEMENT_NOT_RECEIVED                                                                                                               |
| E4175           | PSP REQUEST CREDIT PAY ACKNOWLEDGEMENT IS NOT RECEIVED                                                                                                                                                                                           | PSP REQUEST CREDIT PAY ACKNOWLEDGEMENT IS NOT RECEIVED                               | PSP_REQUEST_CREDIT_PAY_ACKNOWLEDGEMENT_IS_NOT_RECEIVED                                                                                                           |
| E4201           | PSP ORGID NOT FOUND                                                                                                                                                                                                                              | PSP ORGID NOT FOUND                                                                  | PSP_ORGID_NOT_FOUND                                                                                                                                              |
| E4249           | PSP NOT SUPPORTED BY UPI                                                                                                                                                                                                                         | PSP NOT SUPPORTED BY UPI                                                             | PSP_NOT_SUPPORTED_BY_UPI                                                                                                                                         |
| E4658           | PSP not found or configured                                                                                                                                                                                                                      | PSP not found or configured                                                          | PSP_Not_Found_Or_Configured                                                                                                                                      |
| E4166           | Transaction failed as handle used is not registered                                                                                                                                                                                              | PSP IS NOT REGISTERED                                                                | PSP_IS_NOT_REGISTERED_NEW                                                                                                                                        |
| E800            | Transaction failed due to error at the merchant's end                                                                                                                                                                                            | PREFERED_GATEWAY_NOT_SET                                                             | PREFERED_GATEWAY_NOT_SET                                                                                                                                         |
| E4527           | Refund failed due to invalid amount                                                                                                                                                                                                              | Please enter valid refund amount                                                     | Please_Enter_Valid_Refund_Amount                                                                                                                                 |
| E9244           | PIN required                                                                                                                                                                                                                                     | PIN required                                                                         | PIN_REQUIRED                                                                                                                                                     |
| E4298           | PIN Cred Block is missing (txns > 2000)                                                                                                                                                                                                          | PIN Cred Block is missing (txns > 2000)                                              | PIN_Cred_Block_Is_Missing_txns__2000                                                                                                                             |
| E4299           | PIN Cred Block is missing (txns \< 2000 and Seq No = 1)                                                                                                                                                                                          | PIN Cred Block is missing (txns \< 2000 and Seq No = 1)                              | PIN_Cred_Block_Is_Missing_txns__2000_And_Seq_No_1                                                                                                                |
| E310            | Card has been classified as lost and has been blocked.                                                                                                                                                                                           | Pick Up Card                                                                         | LOST_CARD                                                                                                                                                        |
| E1907           | We are unable to fetch status of transaction right now. Check with merchant for order confirmation                                                                                                                                               | PHONE_PE_VERIFY_ERROR                                                                | PHONE_PE_VERIFY_ERROR                                                                                                                                            |
| E1905           | Transaction could not be processed due to some internal error                                                                                                                                                                                    | PHONE_PE_JS_EXCEPTION                                                                | PHONE_PE_JS_EXCEPTION                                                                                                                                            |
| E1906           | Error while initiating payment with PhonePe!                                                                                                                                                                                                     | PHONE_PE_INITIATE_ERROR                                                              | PHONE_PE_INITIATE_ERROR                                                                                                                                          |
| E1203           | You have exceeded your third party funds transfer limit for the day.You cannot transfer any more funds.                                                                                                                                          | PER TRANSACTION LIMIT EXCEEDED AS SET BY REMITTING MEMBER                            | LIMIT_EXCEED                                                                                                                                                     |
| E330            | Validation Failure at PG End                                                                                                                                                                                                                     | PAYMENT_GATEWAY_VALIDATION_FAILURE                                                   | PAYMENT_GATEWAY_VALIDATION_FAILURE                                                                                                                               |
| E4103           | Payment validity expired                                                                                                                                                                                                                         | Payment validity expired                                                             | Payment_Validity_Expired                                                                                                                                         |
| E4315           | PAYMENT STOPPED BY COURT ORDER                                                                                                                                                                                                                   | PAYMENT STOPPED BY COURT ORDER                                                       | PAYMENT_STOPPED_BY_COURT_ORDER                                                                                                                                   |
| E4326           | PAYMENT STOPPED BY ATTACHMENT ORDER BD                                                                                                                                                                                                           | PAYMENT STOPPED BY ATTACHMENT ORDER BD                                               | PAYMENT_STOPPED_BY_ATTACHMENT_ORDER_BD                                                                                                                           |
| E1903           | Authorization failed at Bank                                                                                                                                                                                                                     | Payment could not be authorised                                                      | AUTHORIZATION_FAILED_BY_BANK                                                                                                                                     |
| E4030           | PAYER/PAYEE.INFO.IDENTITY.TYPE MUST BE PRESENT MINLENGTH 1 MAXLENGTH 20                                                                                                                                                                          | PAYER/PAYEE.INFO.IDENTITY.TYPE MUST BE PRESENT MINLENGTH 1 MAXLE                     | PAYER_PAYEE_INFO_IDENTITY_TYPE_MUST_BE_PRESENT_MINLENGTH_1_MAXLENGTH_20                                                                                          |
| E4028           | PAYER/PAYEE.INFO MUST BE PRESENT                                                                                                                                                                                                                 | PAYER/PAYEE.INFO MUST BE PRESENT                                                     | PAYER_PAYEE_INFO_MUST_BE_PRESENT                                                                                                                                 |
| E4017           | PAYER/PAYEE.DEVICE MUST BE PRESENT                                                                                                                                                                                                               | PAYER/PAYEE.DEVICE MUST BE PRESENT                                                   | PAYER_PAYEE_DEVICE_MUST_BE_PRESENT                                                                                                                               |
| E4018           | PAYER/PAYEE. DEVICE.TAGS MUST BE PRESENT PAYER/PAYEE.TAG.DEVICE .NAME/VALUE MUST BE PRESENT                                                                                                                                                      | PAYER/PAYEE. DEVICE.TAGS MUST BE PRESENT PAYER/PAYEE.TAG.DEVICE.                     | PAYER_PAYEE__DEVICE_TAGS_MUST_BE_PRESENT_PAYER_PAYEE_TAG_DEVICE_NAME_VALUE_MUST_BE_PRESENT                                                                       |
| E4254           | PAYER/PAYEE PSP,VERSION/TAGS NOT SUPPORTED BY PSP/BANK                                                                                                                                                                                           | PAYER/PAYEE PSP,VERSION/TAGS NOT SUPPORTED BY PSP/BANK                               | PAYER_PAYEE_PSP_VERSION_TAGS_NOT_SUPPORTED_BY_PSP_BANK                                                                                                           |
| E4253           | PAYER/PAYEE PSP,REQUEST & RESPONSE HEADER VERSION MISMATCH                                                                                                                                                                                       | PAYER/PAYEE PSP,REQUEST & RESPONSE HEADER VERSION MISMATCH                           | PAYER_PAYEE_PSP_REQUEST_RESPONSE_HEADER_VERSION_MISMATCH                                                                                                         |
| E4252           | PAYER/PAYEE PSP,HEADER OR URL VERSION MISMATCHED                                                                                                                                                                                                 | PAYER/PAYEE PSP,HEADER OR URL VERSION MISMATCHED                                     | PAYER_PAYEE_PSP_HEADER_OR_URL_VERSION_MISMATCHED                                                                                                                 |
| E4032           | PAYER/PAYEE .INFO.RATING WHITELISTED MUST BE PRESENT MINLENGTH 1 MAXLENGTH 5                                                                                                                                                                     | PAYER/PAYEE .INFO.RATING WHITELISTED MUST BE PRESENT MINLENGTH 1                     | PAYER_PAYEE_INFO_RATING_WHITELISTED_MUST_BE_PRESENT_MINLENGTH_1_MAXLENGTH_5                                                                                      |
| E4031           | PAYER/PAYEE .INFO.IDENTITY VERIFIEDNAME MUST BE PRESENT ALPHANUMERIC MINLENGTH 1 MAXLENGTH 99                                                                                                                                                    | PAYER/PAYEE .INFO.IDENTITY VERIFIEDNAME MUST BE PRESENT ALPHANUM                     | PAYER_PAYEE_INFO_IDENTITY_UERIFIEDNAME_MUST_BE_PRESENT_ALPHANUMERIC_MINLENGTH_1_MAXLENGTH_99                                                                     |
| E4029           | PAYER/PAYEE .INFO.IDENTITY MUST BE PRESENT                                                                                                                                                                                                       | PAYER/PAYEE .INFO.IDENTITY MUST BE PRESENT                                           | PAYER_PAYEE_INFO_IDENTITY_MUST_BE_PRESENT                                                                                                                        |
| E4136           | PAYER.TYPE MUST BE PRESENT/VALID                                                                                                                                                                                                                 | PAYER.TYPE MUST BE PRESENT/VALID                                                     | PAYER_TYPE_MUST_BE_PRESENT_VALID                                                                                                                                 |
| E4135           | PAYER.SEQNUM NUMERIC MINLENGTH 1 MAXLENGTH 3                                                                                                                                                                                                     | PAYER.SEQNUM NUMERIC MINLENGTH 1 MAXLENGTH 3                                         | PAYER_SEQNUM_NUMERIC_MINLENGTH_1_MAXLENGTH_3                                                                                                                     |
| E4134           | PAYER.NAME ALPHANUMERIC MINLENGTH 1 MAXLENGTH 99                                                                                                                                                                                                 | PAYER.NAME ALPHANUMERIC MINLENGTH 1 MAXLENGTH 99                                     | PAYER_NAME_ALPHANUMERIC_MINLENGTH_1_MAXLENGTH_99                                                                                                                 |
| E4026           | PAYER.INFO MUST BE PRESENT                                                                                                                                                                                                                       | PAYER.INFO MUST BE PRESENT                                                           | PAYER_INFO_MUST_BE_PRESENT                                                                                                                                       |
| E4137           | PAYER.CODE NUMERIC OF LENGTH 4                                                                                                                                                                                                                   | PAYER.CODE NUMERIC OF LENGTH 4                                                       | PAYER_CODE_NUMERIC_OF_LENGTH_4                                                                                                                                   |
| E4133           | PAYER.ADDR MUST BE VALID VPA MAXLENGTH 255                                                                                                                                                                                                       | PAYER.ADDR MUST BE VALID VPA MAXLENGTH 255                                           | PAYER_ADDR_MUST_BE_VALID_VPA_MAXLENGTH_255                                                                                                                       |
| E4117           | Transaction failed as payer details are not correct in mandate                                                                                                                                                                                   | PAYER VPA IS INCORRECT (PAYER)                                                       | PAYER_VPA_IS_INCORRECT_PAYER                                                                                                                                     |
| E4288           | PAYER PSP NOT REGISTERED                                                                                                                                                                                                                         | PAYER PSP NOT REGISTERED                                                             | PAYER_PSP_NOT_REGISTERED                                                                                                                                         |
| E4285           | PAYER PSP NOT AVAILABLE                                                                                                                                                                                                                          | PAYER PSP NOT AVAILABLE                                                              | PAYER_PSP_NOT_AVAILABLE                                                                                                                                          |
| E4264           | PAYER PSP DOES NOT SUPPORTS VERSION                                                                                                                                                                                                              | PAYER PSP DOES NOT SUPPORTS VERSION                                                  | PAYER_PSP_DOES_NOT_SUPPORTS_VERSION                                                                                                                              |
| E4094           | PAYER PSP DOES NOT SUPPORT VERSION MANDATE 2.1                                                                                                                                                                                                   | PAYER PSP DOES NOT SUPPORT VERSION MANDATE 2.1                                       | PAYER_PSP_DOES_NOT_SUPPORT_VERSION_MANDATE_2_1                                                                                                                   |
| E4295           | Transaction failed as vpa is not valid/expired                                                                                                                                                                                                   | PAYER PROFILE DOES NOT EXIST (DE REGISTRATION/VPA REMOVED/UPDATE                     | EXPIRED_VIRTUAL_ADDRESS                                                                                                                                          |
| E4132           | PAYER NOT PRESENT                                                                                                                                                                                                                                | PAYER NOT PRESENT                                                                    | PAYER_NOT_PRESENT                                                                                                                                                |
| E4120           | Modification not allowed by merchant for payer initiated mandate                                                                                                                                                                                 | PAYER INITIATED MANDATE CANNOT BE MODIFIED BY PAYEE                                  | PAYER_INITIATED_MANDATE_CANNOT_BE_MODIFIED_BY_PAYEE                                                                                                              |
| E4210           | PAYER INFO DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                         | PAYER INFO DIFFERS FROM ORIGINAL REQUEST                                             | PAYER_INFO_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                                         |
| E4211           | PAYER INFO DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                         | PAYER INFO DIFFERS FROM ORIGINAL REQUEST                                             | PAYER_INFO_DIFFERS_FROM_ORIGINAL_REQUEST_1                                                                                                                       |
| E4050           | PAYER AND PAYEE TOTAL AMOUNT NOT MATCHING                                                                                                                                                                                                        | PAYER AND PAYEE TOTAL AMOUNT NOT MATCHING                                            | PAYER_AND_PAYEE_TOTAL_AMOUNT_NOT_MATCHING                                                                                                                        |
| E4138           | Transaction failed as payer and payee account cannot be same                                                                                                                                                                                     | PAYER AND PAYEE ACCOUNT SHOULD NOT BE EQUAL                                          | PAYER_AND_PAYEE_ACCOUNT_SHOULD_NOT_BE_EQUAL                                                                                                                      |
| E4052           | PAYER AMOUNT SHOULD BE GREATER THAN TOTAL PAYEE AMOUNT                                                                                                                                                                                           | PAYER AMOUNT SHOULD BE GREATER THAN TOTAL PAYEE AMOUNT                               | PAYER_AMOUNT_SHOULD_BE_GREATER_THAN_TOTAL_PAYEE_AMOUNT                                                                                                           |
| E4222           | PAYER ACCOUNT MISMATCH                                                                                                                                                                                                                           | PAYER ACCOUNT MISMATCH                                                               | PAYER_ACCOUNT_MISMATCH                                                                                                                                           |
| E4125           | Transaction declined as customer account has changed                                                                                                                                                                                             | PAYER ACCOUNT HAS CHANGED (PAYER)                                                    | PAYER_ACCOUNT_HAS_CHANGED_PAYER                                                                                                                                  |
| E4048           | PAYER & PAYEE TOTAL AMOUNT NOT MATCHING                                                                                                                                                                                                          | PAYER & PAYEE TOTAL AMOUNT NOT MATCHING                                              | PAYER_PAYEE_TOTAL_AMOUNT_NOT_MATCHING                                                                                                                            |
| E4006           | PAYEES NOT PRESENT                                                                                                                                                                                                                               | PAYEES NOT PRESENT                                                                   | PAYEES_NOT_PRESENT                                                                                                                                               |
| E4008           | PAYEE.ADDR MUST BE VALID VPA MAXLENGTH 255                                                                                                                                                                                                       | PAYEE.ADDR MUST BE VALID VPA MAXLENGTH 255                                           | PAYEE_ADDR_MUST_BE_UALID_UPA_MAXLENGTH_255                                                                                                                       |
| E4325           | Transaction declined as merchant vpa is not correct                                                                                                                                                                                              | PAYEE VPA IS INCORRECT (REMITTER)                                                    | PAYEE_VPA_IS_INCORRECT_REMITTER                                                                                                                                  |
| E4113           | Transaction failed as payee details are not correct in mandate                                                                                                                                                                                   | PAYEE VPA IS INCORRECT (PAYER)                                                       | PAYEE_VPA_IS_INCORRECT_PAYER                                                                                                                                     |
| E4242           | PAYEE VPA AADHAAR OR IIN VPA IS DISABLED                                                                                                                                                                                                         | PAYEE VPA AADHAAR OR IIN VPA IS DISABLED                                             | PAYEE_VPA_AADHAAR_OR_IIN_VPA_IS_DISABLED                                                                                                                         |
| E4244           | PAYEE VPA AADHAAR OR IIN VPA IS DISABLED                                                                                                                                                                                                         | PAYEE VPA AADHAAR OR IIN VPA IS DISABLED                                             | PAYEE_VPA_AADHAAR_OR_IIN_VPA_IS_DISABLED_1                                                                                                                       |
| E4289           | PAYEE PSP NOT REGISTERED                                                                                                                                                                                                                         | PAYEE PSP NOT REGISTERED                                                             | PAYEE_PSP_NOT_REGISTERED                                                                                                                                         |
| E4286           | PAYEE PSP NOT AVAILABLE                                                                                                                                                                                                                          | PAYEE PSP NOT AVAILABLE                                                              | PAYEE_PSP_NOT_AVAILABLE                                                                                                                                          |
| E4095           | PAYEE PSP DOES NOT SUPPORT VERSION MANDATE 2.1                                                                                                                                                                                                   | PAYEE PSP DOES NOT SUPPORT VERSION MANDATE 2.1                                       | PAYEE_PSP_DOES_NOT_SUPPORT_VERSION_MANDATE_2_1                                                                                                                   |
| E4038           | PAYEE PSP DOES NOT SUPPORT VERSION 2                                                                                                                                                                                                             | PAYEE PSP DOES NOT SUPPORT VERSION 2                                                 | PAYEE_PSP_DOES_NOT_SUPPORT_VERSION_2                                                                                                                             |
| E4007           | PAYEE NOT PRESENT                                                                                                                                                                                                                                | PAYEE NOT PRESENT                                                                    | PAYEE_NOT_PRESENT                                                                                                                                                |
| E4143           | Transaction failed as merchant is reported SPAM by the customer                                                                                                                                                                                  | PAYEE IS REPORTED AS SPAM UNDER RULE 1                                               | PAYEE_IS_REPORTED_AS_SPAM_UNDER_RULE_1                                                                                                                           |
| E4130           | Modification not allowed by payer for merchant initiated mandate                                                                                                                                                                                 | PAYEE INITIATED MANDATE CANNOT BE MODIFIED BY PAYER                                  | PAYEE_INITIATED_MANDATE_CANNOT_BE_MODIFIED_BY_PAYER                                                                                                              |
| E4047           | PAYEE AMOUNTCUR IS INVALID                                                                                                                                                                                                                       | PAYEE AMOUNTCUR IS INVALID                                                           | PAYEE_AMOUNTCUR_IS_INVALID                                                                                                                                       |
| E4206           | PAYEE AMOUNT DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                       | PAYEE AMOUNT DIFFERS FROM ORIGINAL REQUEST                                           | PAYEE_AMOUNT_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                                       |
| E4207           | PAYEE AMOUNT DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                       | PAYEE AMOUNT DIFFERS FROM ORIGINAL REQUEST                                           | PAYEE_AMOUNT_DIFFERS_FROM_ORIGINAL_REQUEST_1                                                                                                                     |
| E4046           | PAYEE AMOUNT CUR MUST BE CONSISTENT                                                                                                                                                                                                              | PAYEE AMOUNT CUR MUST BE CONSISTENT                                                  | PAYEE_AMOUNT_CUR_MUST_BE_CONSISTENT                                                                                                                              |
| E4208           | PAYEE ADDRESS DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                      | PAYEE ADDRESS DIFFERS FROM ORIGINAL REQUEST                                          | PAYEE_ADDRESS_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                                      |
| E4209           | PAYEE ADDRESS DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                      | PAYEE ADDRESS DIFFERS FROM ORIGINAL REQUEST                                          | PAYEE_ADDRESS_DIFFERS_FROM_ORIGINAL_REQUEST_1                                                                                                                    |
| E4223           | PAYEE ACCOUNT MISMATCH                                                                                                                                                                                                                           | PAYEE ACCOUNT MISMATCH                                                               | PAYEE_ACCOUNT_MISMATCH                                                                                                                                           |
| E326            | Authentication failed due to invalid password.                                                                                                                                                                                                   | PASSWORD_ERROR                                                                       | PASSWORD_ERROR                                                                                                                                                   |
| E4003           | PARTIAL REVERSAL                                                                                                                                                                                                                                 | PARTIAL REVERSAL                                                                     | PARTIAL_REVERSAL                                                                                                                                                 |
| E4141           | Transaction failed as partial debit request timeout at customer's bank                                                                                                                                                                           | PARTIAL DEBIT REVERSAL TIMEOUT                                                       | PARTIAL_DEBIT_REVERSAL_TIMEOUT                                                                                                                                   |
| E1648           | Partial Approval                                                                                                                                                                                                                                 | Partial amount was approved                                                          | PARTIAL_APPROVAL                                                                                                                                                 |
| E9202           | Partial Amount Approved                                                                                                                                                                                                                          | Partial Amount Approved                                                              | PARTIAL_AMOUNT_APPROVED                                                                                                                                          |
| E1606           | Transaction failed due to user pressing refresh button.                                                                                                                                                                                          | PAGE_REFRESHED_BY_USER                                                               | PAGE_REFRESHED_BY_USER                                                                                                                                           |
| E1610           | Transaction failed. Page expired due to no user input.                                                                                                                                                                                           | PAGE_EXPIRED                                                                         | PAGE_EXPIRED                                                                                                                                                     |
| E9246           | Over Daily Limit                                                                                                                                                                                                                                 | Over Daily Limit                                                                     | OVER_DAILY_LIMIT                                                                                                                                                 |
| E2404           | OTP Validation Failed                                                                                                                                                                                                                            | OTP_VALIDATION_FAILED                                                                | OTP_VALIDATION_FAILED                                                                                                                                            |
| E1604           | Transaction failed due to incorrect user action.                                                                                                                                                                                                 | OTP_MAX_RESEND_ATTEMPT                                                               | OTP_MAX_RESEND_ATTEMPT                                                                                                                                           |
| E1601           | Customer Authentication failed due to incorrect OTP.                                                                                                                                                                                             | OTP_MAX_LIMIT_EXCEEDED                                                               | OTP_MAX_LIMIT_EXCEEDED                                                                                                                                           |
| E4388           | OTP TRANSACTION LIMIT EXCEEDED                                                                                                                                                                                                                   | OTP TRANSACTION LIMIT EXCEEDED                                                       | OTP_TRANSACTION_LIMIT_EXCEEDED                                                                                                                                   |
| E4387           | OTP EXPIRED                                                                                                                                                                                                                                      | OTP EXPIRED                                                                          | OTP_EXPIRED                                                                                                                                                      |
| E4263           | OTHER BANK/PSP IS NOT SUPPORTED IN 2 VERSION                                                                                                                                                                                                     | OTHER BANK/PSP IS NOT SUPPORTED IN 2 VERSION                                         | OTHER_BANK_PSP_IS_NOT_SUPPORTED_IN_2_VERSION                                                                                                                     |
| E4282           | ORIGINAL REQMANDATE NOT FOUND                                                                                                                                                                                                                    | ORIGINAL REQMANDATE NOT FOUND                                                        | ORIGINAL_REQMANDATE_NOT_FOUND                                                                                                                                    |
| E4276           | ORIGINAL REQAUTHMANDATE NOT FOUND                                                                                                                                                                                                                | ORIGINAL REQAUTHMANDATE NOT FOUND                                                    | ORIGINAL_REQAUTHMANDATE_NOT_FOUND                                                                                                                                |
| E9253           | Amount Incorrect / Mismatch                                                                                                                                                                                                                      | Original Amount Incorrect                                                            | AMOUNT_INCORRECT_MISMATCH                                                                                                                                        |
| E1668           | Failing as no gateway found for One Click transaction                                                                                                                                                                                            | ONE_CLICK_PG * SELECTION_FAILED                                                      | ONE_CLICK_PG_SELECTION_FAILED                                                                                                                                    |
| E1667           | Failing as One Click only option was used and data validation checks failed                                                                                                                                                                      | ONE_CLICK_DATA * VALIDATION_FAILED                                                   | ONE_CLICK_DATA_VALIDATION_FAILED                                                                                                                                 |
| E1666           | Failing as One Click only option was used and transaction failed in authentication                                                                                                                                                               | ONE_CLICK_AUTHENTICATION * FAILED                                                    | ONE_CLICK_AUTHENTICATION_FAILED                                                                                                                                  |
| E4049           | ONE OR MORE PAYEE AMOUNT IS MISSING                                                                                                                                                                                                              | ONE OR MORE PAYEE AMOUNT IS MISSING                                                  | ONE_OR_MORE_PAYEE_AMOUNT_IS_MISSING                                                                                                                              |
| E9250           | Offline Approved                                                                                                                                                                                                                                 | Offline Approved                                                                     | OFFLINE_APPROVED                                                                                                                                                 |
| E1800           | The transaction cannot be processed as discount given exceeds the allowed limit. If money is debited from your account then it will be auto refunded. Please try again                                                                           | OFFER_AMOUNT_EXCEEDED * DURING_TRANSACTION                                           | OFFER_AMOUNT_EXCEEDED_DURING_TRANSACTION                                                                                                                         |
| E1303           | Transaction declined due to technical failure                                                                                                                                                                                                    | OBJECT_CREATION_FAILED                                                               | OBJECT_CREATION_FAILED                                                                                                                                           |
| E4205           | NUMBER OF PAYEES DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                   | NUMBER OF PAYEES DIFFERS FROM ORIGINAL REQUEST                                       | NUMBER_OF_PAYEES_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                                   |
| E4312           | Transaction failed as number of mandates allowed exceeded                                                                                                                                                                                        | NUMBER OF MANDATES ALLOWED ON THIS ACCOUNT HAS EXCEEDED ISSUER'S                     | NUMBER_OF_MANDATES_ALLOWED_ON_THIS_ACCOUNT_HAS_EXCEEDED_ISSUER_S_LIMIT_BD_OPTIONAL_AS_PER_BANKS_POLICY                                                           |
| E4247           | NULL ACK RECEIVED BY UPI FOR META TRANSACTION                                                                                                                                                                                                    | NULL ACK RECEIVED BY UPI FOR META TRANSACTION                                        | NULL_ACK_RECEIVED_BY_UPI_FOR_META_TRANSACTION                                                                                                                    |
| E1618           | No form post variables found [S2S Flow]                                                                                                                                                                                                          | NO_FORM_POST * VARS_S2SFLOW                                                          | NO_FORM_POST_VARS_S2SFLOW                                                                                                                                        |
| E803            | Payment gateway seems to be down at this moment.                                                                                                                                                                                                 | NO_ELIGIBLE_PG                                                                       | NO_ELIGIBLE_PG                                                                                                                                                   |
| E222            | Debit account number is not received in transaction response                                                                                                                                                                                     | NO_DEBIT_ACCOUNT * NUMBER                                                            | NO_DEBIT_ACCOUNT_NUMBER                                                                                                                                          |
| E221            | Bank reference number is not received in transaction response                                                                                                                                                                                    | NO_BANK_REFERENCE * NUMBER                                                           | NO_BANK_REFERENCE_NUMBER                                                                                                                                         |
| E1624           | No Active Authentication Option Eligible                                                                                                                                                                                                         | NO_ACTIVE_PAYMENT * ELIGIBLE                                                         | NO_ACTIVE_PAYMENT_ELIGIBLE                                                                                                                                       |
| E2402           | The customer does not have an active credit line to book a consumer loan                                                                                                                                                                         | NO_ACTIVE_CREDIT_LINE * WITH_THE_CUSTOMER                                            | NO_ACTIVE_CREDIT_LINE_WITH_THE_CUSTOMER                                                                                                                          |
| E1650           | No action taken                                                                                                                                                                                                                                  | NO_ACTION_TAKEN                                                                      | NO_ACTION_TAKEN                                                                                                                                                  |
| E342            | Transaction not initiated                                                                                                                                                                                                                        | NOT_INITIATED                                                                        | NOT_INITIATED                                                                                                                                                    |
| E1609           | Transaction declined due to the registered mobile number being international. It should be a domestic number to process the transaction.                                                                                                         | NOT_DOMESTIC_NUMBER                                                                  | NOT_DOMESTIC_NUMBER                                                                                                                                              |
| E343            | Transaction not approved                                                                                                                                                                                                                         | NOT_APPROVED                                                                         | NOT_APPROVED                                                                                                                                                     |
| E347            | Transaction failed because of non whitelisted domain                                                                                                                                                                                             | NON_WHITELISTED_DOMAIN                                                               | NON_WHITELISTED_DOMAIN                                                                                                                                           |
| E1616           | Non-seamless not allowed in S2S Flow                                                                                                                                                                                                             | NONSEAMLESS_NOT * ALLOWED_S2SFLOW                                                    | NONSEAMLESS_NOT_ALLOWED_S2SFLOW                                                                                                                                  |
| E9252           | The customer's card issuer has declined the transaction as the account type selected is not valid for this credit card number.                                                                                                                   | No Universal Account                                                                 | NO_UNIVERSAL_ACCOUNT                                                                                                                                             |
| E4176           | Transaction failed as no response received from merchant/customer                                                                                                                                                                                | NO RESPONSE FROM PSP                                                                 | NO_RESPONSE_FROM_PSP                                                                                                                                             |
| E4522           | Refund failed due to no response from Customer's bank                                                                                                                                                                                            | No response from Beneficiary Bank                                                    | No_Response_From_Beneficiary_Bank                                                                                                                                |
| E4101           | Transaction failed due to technical issue at Issuer/Acquirer end                                                                                                                                                                                 | NO ORIGINAL REQUEST FOUND DURING DEBIT/CREDIT BD                                     | NO_ORIGINAL_REQUEST_FOUND_DURING_DEBIT_CREDIT_BD                                                                                                                 |
| E4680           | No Mandate data found to Modify                                                                                                                                                                                                                  | No Mandate data found to Modify                                                      | No_Mandate_Data_Found_To_Modify                                                                                                                                  |
| E4356           | NO FINANCIAL ADDRESS RECORD FOUND                                                                                                                                                                                                                | NO FINANCIAL ADDRESS RECORD FOUND                                                    | NO_FINANCIAL_ADDRESS_RECORD_FOUND                                                                                                                                |
| E9224           | No Envelope Inserted                                                                                                                                                                                                                             | No Envelope Inserted                                                                 | NO_ENVELOPE_INSERTED                                                                                                                                             |
| E4346           | Transaction failed due to no card details from customer's bank                                                                                                                                                                                   | NO CARD RECORD (REMITTER)                                                            | NO_CARD_RECORD_REMITTER                                                                                                                                          |
| E4347           | Transaction failed due to no card details from acquirer's bank                                                                                                                                                                                   | NO CARD RECORD (BENEFICIARY)                                                         | NO_CARD_RECORD_BENEFICIARY                                                                                                                                       |
| E4533           | No active mandates found                                                                                                                                                                                                                         | No Approved Mandates are available                                                   | No_Approved_Mandates_Are_Available                                                                                                                               |
| E4002           | NO ACTION TAKEN (FULL REVERSAL)                                                                                                                                                                                                                  | NO ACTION TAKEN (FULL REVERSAL)                                                      | NO_ACTION_TAKEN_FULL_REVERSAL                                                                                                                                    |
| E9207           | No Action Taken                                                                                                                                                                                                                                  | No Action Taken                                                                      | NO_ACTION_TAKEN_                                                                                                                                                 |
| E211            | The Bank servers are unreachable over the network                                                                                                                                                                                                | NETWORK_ERROR                                                                        | NETWORK_ERROR                                                                                                                                                    |
| E801            | Netbanking option was temporarily not available so set as bounced.                                                                                                                                                                               | NETBANKING_GATEWAY * DOWN                                                            | NETBANKING_GATEWAY_DOWN                                                                                                                                          |
| E1204           | Transaction Failed at bank end.                                                                                                                                                                                                                  | NETBANKING_AUTHENTICATION * ERROR                                                    | NETBANKING_AUTHENTICATION_ERROR                                                                                                                                  |
| E4152           | Transaction failed due to debit limit on customer exceeded                                                                                                                                                                                       | NET DEBIT CAP IS EXCEEDED                                                            | NET_DEBIT_CAP_IS_EXCEEDED                                                                                                                                        |
| E4248           | NEGATIVE ACK RECEIVED BY UPI FOR META TRANSACTION                                                                                                                                                                                                | NEGATIVE ACK RECEIVED BY UPI FOR META TRANSACTION                                    | NEGATIVE_ACK_RECEIVED_BY_UPI_FOR_META_TRANSACTION                                                                                                                |
| E4314           | Transaction failed as debit not allowed                                                                                                                                                                                                          | NATURE OF DEBIT NOT ALLOWED IN ACCOUNT TYPE                                          | NATURE_OF_DEBIT_NOT_ALLOWED_IN_ACCOUNT_TYPE                                                                                                                      |
| E4525           | Multiple transactions found in status check                                                                                                                                                                                                      | Multiple transactions against given parameter                                        | Multiple_Transactions_Against_Given_Parameter                                                                                                                    |
| E4005           | Transaction failed due to MPIN not set by customer                                                                                                                                                                                               | MPIN NOT SET BY CUSTOMER                                                             | MPIN_NOT_SET_BY_CUSTOMER                                                                                                                                         |
| E4051           | MORE THAN ONE PAYEE AMOUNT IS MISSING                                                                                                                                                                                                            | MORE THAN ONE PAYEE AMOUNT IS MISSING                                                | MORE_THAN_ONE_PAYEE_AMOUNT_IS_MISSING                                                                                                                            |
| E4012           | MOBILE NUMBER REGISTERED WITH MULTIPLE CUSTOMER IDS                                                                                                                                                                                              | MOBILE NUMBER REGISTERED WITH MULTIPLE CUSTOMER IDS                                  | MOBILE_NUMBER_REGISTERED_WITH_MULTIPLE_CUSTOMER_IDS                                                                                                              |
| E9221           | Mobile number record not found / mis-match                                                                                                                                                                                                       | Mobile number record not found / mis-match                                           | MOBILE_NUMBER_RECORD_NOT_FOUND                                                                                                                                   |
| E4224           | MOBILE BANKING REGISTRATION FORMAT NOT SUPPORTED BY THE ISSUER BANK                                                                                                                                                                              | MOBILE BANKING REGISTRATION FORMAT NOT SUPPORTED BY THE ISSUER B                     | MOBILE_BANKING_REGISTRATION_FORMAT_NOT_SUPPORTED_BY_THE_ISSUER_BANK                                                                                              |
| E1700           | Term URL is missing in the request                                                                                                                                                                                                               | MISSING_TERM_URL                                                                     | MISSING_TERM_URL                                                                                                                                                 |
| E1644           | Empty Otp Received                                                                                                                                                                                                                               | MISSING_OTP                                                                          | MISSING_OTP                                                                                                                                                      |
| E226            | Security Signature missing or mismatched                                                                                                                                                                                                         | MISSING_MISMATCHED_SIGNATURE                                                         | MISSING_MISMATCHED_SIGNATURE                                                                                                                                     |
| E1651           | Mismatch in retrieval reference number                                                                                                                                                                                                           | MISMATCH_RETRIEVAL_REFERENCE_NUMBER                                                  | MISMATCH_RETRIEVAL_REFERENCE_NUMBER                                                                                                                              |
| E4011           | MISMATCH IN PAYMENT DETAILS                                                                                                                                                                                                                      | MISMATCH IN PAYMENT DETAILS                                                          | MISMATCH_IN_PAYMENT_DETAILS                                                                                                                                      |
| E4204           | MESSAGE INTEGRITY FAILED DUE TO ORGID MISMATCH                                                                                                                                                                                                   | MESSAGE INTEGRITY FAILED DUE TO ORGID MISMATCH                                       | MESSAGE_INTEGRITY_FAILED_DUE_TO_ORGID_MISMATCH                                                                                                                   |
| E346            | Merchant Not Eligible for this transaction                                                                                                                                                                                                       | MERCHANT_NOT_ELIGIBLE                                                                | MERCHANT_NOT_ELIGIBLE                                                                                                                                            |
| E4666           | Merchant Account details not found or configured                                                                                                                                                                                                 | Merchant_Account_Details * Not_Found_Or_Configured                                   | Merchant_Account_Details_Not_Found_Or_Configured                                                                                                                 |
| E4512           | Transaction details not present at bank's end                                                                                                                                                                                                    | Merchant TranId is not available                                                     | Merchant_TranId_Is_Not_Available                                                                                                                                 |
| E4333           | MERCHANT NOT REACHABLE (ACQURIER)                                                                                                                                                                                                                | MERCHANT NOT REACHABLE (ACQURIER)                                                    | MERCHANT_NOT_REACHABLE_ACQURIER                                                                                                                                  |
| EA09            | Alt ID Provisioning Failed                                                                                                                                                                                                                       | Merchant not onboarded, please contact PayU Support                                  | ALT_ID_PROV_MERCHANT                                                                                                                                             |
| E4365           | Transaction declined due to merchant error                                                                                                                                                                                                       | MERCHANT ERROR (PAYEE PSP)                                                           | MERCHANT_ERROR_PAYEE_PSP                                                                                                                                         |
| E9237           | Merchant Daily Limit Exceeded                                                                                                                                                                                                                    | Merchant Daily Limit Exceeded                                                        | MERCHANT_DAILY_LIMIT_EXCEEDED                                                                                                                                    |
| E4220           | MERCHANT CREDIT NOT SUPPORTED IN IMPS                                                                                                                                                                                                            | MERCHANT CREDIT NOT SUPPORTED IN IMPS                                                | MERCHANT_CREDIT_NOT_SUPPORTED_IN_IMPS                                                                                                                            |
| E4225           | Transaction failed as merchant is blocked                                                                                                                                                                                                        | MERCHANT BLOCKED                                                                     | MERCHANT_BLOCKED                                                                                                                                                 |
| E1643           | Mecode Not Permitted                                                                                                                                                                                                                             | MECODE_NOT_PERMITTED                                                                 | MECODE_NOT_PERMITTED                                                                                                                                             |
| E1669           | MCP lookup details tampered                                                                                                                                                                                                                      | MCP_LOOKUP_DETAILS_TAMPERED                                                          | MCP_LOOKUP_DETAILS_TAMPERED                                                                                                                                      |
| E2406           | You have entered incorrect otp too many times, Please try again                                                                                                                                                                                  | MAXIMUM_OTP_LIMIT_REACHED                                                            | MAXIMUM_OTP_LIMIT_REACHED                                                                                                                                        |
| E9242           | Maximum refund credit reached                                                                                                                                                                                                                    | Maximum refund credit reached                                                        | MAXIMUM_REFUND_CREDIT_REACHED                                                                                                                                    |
| E9241           | Maximum off-line refund reached                                                                                                                                                                                                                  | Maximum off-line refund reached                                                      | MAXIMUM_OFFLINE_REFUND_REACHED                                                                                                                                   |
| E9243           | Maximum number refund credits                                                                                                                                                                                                                    | Maximum number refund credits                                                        | MAXIMUM_NUMBER_REFUND_CREDITS                                                                                                                                    |
| E4104           | MAXIMUM BALANCE EXCEEDED AS SET BY BENEFICIARY BANK                                                                                                                                                                                              | MAXIMUM BALANCE EXCEEDED AS SET BY BENEFICIARY BANK                                  | MAXIMUM_BALANCE_EXCEEDED_AS_SET_BY_BENEFICIARY_BANK                                                                                                              |
| E1640           | Offus Master Card Not Approved Transaction                                                                                                                                                                                                       | MASTER_CARD_NOT_APPROVED                                                             | MASTER_CARD_NOT_APPROVED                                                                                                                                         |
| E1641           | Cancellation not allowed for offus master card                                                                                                                                                                                                   | MASTER_CARD_CANCELLATION_NOT_ALLOWED                                                 | MASTER_CARD_CANCELLATION_NOT_ALLOWED                                                                                                                             |
| E4065           | MANDATE.VALIDITY.START MUST BE PRESENT, DATE FORMAT                                                                                                                                                                                              | MANDATE.VALIDITY.START MUST BE PRESENT, DATE FORMAT                                  | MANDATE_VALIDITY_START_MUST_BE_PRESENT_DATE_FORMAT                                                                                                               |
| E4099           | MANDATE.VALIDITY.START DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                             | MANDATE.VALIDITY.START DIFFERS FROM ORIGINAL REQUEST                                 | MANDATE_VALIDITY_START_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                             |
| E4066           | MANDATE.VALIDITY.END MUST BE PRESENT, DATE FORMAT DDMMYYYY, END DATE MUST BE GREATER THAN TODAY'S DATE                                                                                                                                           | MANDATE.VALIDITY.END MUST BE PRESENT, DATE FORMAT DDMMYYYY, END                      | MANDATE_VALIDITY_END_MUST_BE_PRESENT_DATE_FORMAT_DDMMYYYY_END_DATE_MUST_BE_GREATER_THAN_TODAYS_DATE                                                              |
| E4100           | MANDATE.VALIDITY.END DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                               | MANDATE.VALIDITY.END DIFFERS FROM ORIGINAL REQUEST                                   | MANDATE_VALIDITY_END_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                               |
| E4064           | MANDATE.VALIDITY MUST BE PRESENT                                                                                                                                                                                                                 | MANDATE.VALIDITY MUST BE PRESENT                                                     | MANDATE_VALIDITY_MUST_BE_PRESENT                                                                                                                                 |
| E4098           | MANDATE.VALIDITY DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                   | MANDATE.VALIDITY DIFFERS FROM ORIGINAL REQUEST                                       | MANDATE_VALIDITY_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                                   |
| E4056           | MANDATE.UMN SHOULD NOT BE PRESENT FOR PAYEE INITIATED                                                                                                                                                                                            | MANDATE.UMN SHOULD NOT BE PRESENT FOR PAYEE INITIATED                                | MANDATE_UMN_SHOULD_NOT_BE_PRESENT_FOR_PAYEE_INITIATED                                                                                                            |
| E4060           | MANDATE.UMN MUST BE PRESENT, LENGTH 32                                                                                                                                                                                                           | MANDATE.UMN MUST BE PRESENT, LENGTH 32                                               | MANDATE_UMN_MUST_BE_PRESENT_Length_32                                                                                                                            |
| E4059           | MANDATE.UMN MUST BE PRESENT                                                                                                                                                                                                                      | MANDATE.UMN MUST BE PRESENT                                                          | MANDATE_UMN_MUST_BE_PRESENT_1                                                                                                                                    |
| E4081           | MANDATE.UMN DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                        | MANDATE.UMN DIFFERS FROM ORIGINAL REQUEST                                            | MANDATE_UMN_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                                        |
| E4075           | MANDATE.UMN CANNOT BE GENERATED BY PAYEE                                                                                                                                                                                                         | MANDATE.UMN CANNOT BE GENERATED BY PAYEE                                             | MANDATE_UMN_CANNOT_BE_GENERATED_BY_PAYEE                                                                                                                         |
| E4086           | MANDATE.TYPE DIFFERS FROM ORIGINAL REQUEST,MANDATE.AMOUNT DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                          | MANDATE.TYPE DIFFERS FROM ORIGINAL REQUEST,MANDATE.AMOUNT DIFFER                     | MANDATE_TYPE_DIFFERS_FROM_ORIGINAL_REQUEST_MANDATE_AMOUNT_DIFFERS_FROM_ORIGINAL_REQUEST                                                                          |
| E4057           | MANDATE.TXNID MUST BE PRESENT, MUST BE 35 CHARACTERS OF ALPHANUMERIC                                                                                                                                                                             | MANDATE.TXNID MUST BE PRESENT, MUST BE 35 CHARACTERS OF ALPHANUM                     | MANDATE_TXNID_MUST_BE_PRESENT_MUST_BE_35_CHARACTERS_OF_ALPHANUMERIC                                                                                              |
| E4080           | MANDATE.TXNID DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                      | MANDATE.TXNID DIFFERS FROM ORIGINAL REQUEST                                          | MANDATE_TXNID_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                                      |
| E4058           | MANDATE.TXNID AND TXN.ID MUST BE SAME                                                                                                                                                                                                            | MANDATE.TXNID AND TXN.ID MUST BE SAME                                                | MANDATE_TXNID_AND_TXN_ID_MUST_BE_SAME                                                                                                                            |
| E4061           | MANDATE.TS MUST BE PRESENT AND SHOULD BE IN ISO_ZONE                                                                                                                                                                                             | MANDATE.TS MUST BE PRESENT AND SHOULD BE IN ISO_ZONE                                 | MANDATE_TS_MUST_BE_PRESENT_AND_SHOULD_BE_IN_ISO_ZONE                                                                                                             |
| E4084           | MANDATE.SHARETOPAYEE DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                               | MANDATE.SHARETOPAYEE DIFFERS FROM ORIGINAL REQUEST                                   | MANDATE_SHARETOPAYEE_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                               |
| E4062           | MANDATE.REVOKEABLE MUST BE PRESENT                                                                                                                                                                                                               | MANDATE.REVOKEABLE MUST BE PRESENT                                                   | MANDATE_REVOKEABLE_MUST_BE_PRESENT                                                                                                                               |
| E4072           | MANDATE.RECURRENCE.RULE NOT APPLICABLE FOR MANDATE.RECURRENCE.PATTERN ONETIME/DAILY/WEEKLY/FORTNIGHTLY/MONTHLY /BIMONTHLY/QUARTERLY/HALFYEARLY /YEARLY/ASPRESENTED                                                                               | MANDATE.RECURRENCE.RULE NOT APPLICABLE FOR MANDATE.RECURRENCE.PA                     | MANDATE_RECURRENCE_RULE_NOT_APPLICABLE_FOR_MANDATE_RECURRENCE_PATTERN_ONETIME_DAILY_WEEKLY_FORTNIGHTLY_MONTHLY_BIMONTHLY_QUARTERLY_HALFYEARLY_YEARLY_ASPRESENTED |
| E4070           | MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.TYPE MUST BE AFTER OR ON OR BEFORE                                                                                                                                               | MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.                     | MANDATE_RECURRENCE_RULE_MUST_BE_PRESENT_MANDATE_RECURRENCE_RULE_TYPE_MUST_BE_AFTER_OR_ON_OR_BEFORE                                                               |
| E4071           | MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.VALUE IN BETWEEN 1 TO 7 ONLY WHEN MANDATE.RECURRENCE.PATTERN IS WEEKLY                                                                                                           | MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.                     | MANDATE_RECURRENCE_RULE_MUST_BE_PRESENT_MANDATE_RECURRENCE_RULE_VALUE_IN_BETWEEN_1_TO_7_ONLY_WHEN_MANDATE_RECURRENCE_PATTERN_IS_WEEKLY                           |
| E4087           | MANDATE.RECURRENCE.PATTERN DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                         | MANDATE.RECURRENCE.PATTERN DIFFERS FROM ORIGINAL REQUEST                             | MANDATE_RECURRENCE_PATTERN_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                         |
| E4327           | MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTREMITTER BANK NOT CERTIFIED FOR 2.7                                                                                                                                                             | MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTREMITTER BANK N                     | MANDATE_RECURRENCE_RULE_TAG_SHOULD_NOT_BE_PRESENTREMITTER_BANK_NOT_CERTIFIED_FOR_2_7                                                                             |
| E4328           | MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTBENEFICIARY BANK NOT CERTIFIED FOR 2.7                                                                                                                                                          | MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTBENEFICIARY BAN                     | MANDATE_RECURRENCE_RULE_TAG_SHOULD_NOT_BE_PRESENTBENEFICIARY_BANK_NOT_CERTIFIED_FOR_2_7                                                                          |
| E4069           | MANDATE.RECURRENCE MUST BE PRESENT,MANDATE.RECURRENCE.PATTERN MUST BE ONETIME OR DAILYOR WEEKLY                                                                                                                                                  | MANDATE.RECURRENCE MUST BE PRESENT,MANDATE.RECURRENCE.PATTERN MU                     | MANDATE_RECURRENCE_MUST_BE_PRESENT_MANDATE_RECURRENCE_PATTERN_MUST_BE_ONETIME_OR_DAILYOR_WEEKLY                                                                  |
| E4079           | MANDATE.NAME DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                       | MANDATE.NAME DIFFERS FROM ORIGINAL REQUEST                                           | MANDATE_NAME_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                                       |
| E4054           | MANDATE.NAME ALPHANUMERIC; MINLENGTH 1 , MAXLENGTH 99                                                                                                                                                                                            | MANDATE.NAME ALPHANUMERIC; MINLENGTH 1 , MAXLENGTH 99                                | MANDATE_NAME_ALPHANUMERIC_MINLENGTH_1_MAXLENGTH_99                                                                                                               |
| E4085           | MANDATE.BLOCKFUND DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                  | MANDATE.BLOCKFUND DIFFERS FROM ORIGINAL REQUEST                                      | MANDATE_BLOCKFUND_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                                  |
| E4068           | MANDATE.AMOUNT.RULE MUST BE PRESENT, RULE MUST BE EXACT/MAX                                                                                                                                                                                      | MANDATE.AMOUNT.RULE MUST BE PRESENT, RULE MUST BE EXACT/MAX                          | MANDATE_AMOUNT_RULE_MUST_BE_PRESENT_RULE_MUST_BE_EXACT_MAX                                                                                                       |
| E4067           | MANDATE.AMOUNT MUST BE PRESENT, VALUE AND RULE SHOULD NOT BE EMPTY                                                                                                                                                                               | MANDATE.AMOUNT MUST BE PRESENT, VALUE AND RULE SHOULD NOT BE EMP                     | MANDATE_AMOUNT_MUST_BE_PRESENT_VALUE_AND_RULE_SHOULD_NOT_BE_EMPTY                                                                                                |
| E4090           | MANDATE.AMOUNT CAN ONLY BE UPDATED IF PURPOSE=01                                                                                                                                                                                                 | MANDATE.AMOUNT CAN ONLY BE UPDATED IF PURPOSE=01                                     | MANDATE_AMOUNT_CAN_ONLY_BE_UPDATED_IF_PURPOSE_01                                                                                                                 |
| E4679           | Modification request already initiated                                                                                                                                                                                                           | Mandate Update Request already initiated for Same UMN                                | Mandate_Update_Request_Already_Initiated_For_Same_UMN                                                                                                            |
| E4055           | MANDATE UMN MUST BE PRESENT                                                                                                                                                                                                                      | MANDATE UMN MUST BE PRESENT                                                          | MANDATE_UMN_MUST_BE_PRESENT                                                                                                                                      |
| E4082           | MANDATE TS DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                         | MANDATE TS DIFFERS FROM ORIGINAL REQUEST                                             | MANDATE_TS_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                                         |
| E4078           | MANDATE TAG DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                        | MANDATE TAG DIFFERS FROM ORIGINAL REQUEST                                            | MANDATE_TAG_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                                        |
| E4309           | Transaction failed as mandate signature is tampered                                                                                                                                                                                              | MANDATE SIGNATURE IS TAMPERED OR CORRUPT (REMITTER)                                  | MANDATE_SIGNATURE_IS_TAMPERED_OR_CORRUPT_REMITTER                                                                                                                |
| E4083           | MANDATE REVOKEABLE DIFFERS FROM ORIGINAL REQUEST                                                                                                                                                                                                 | MANDATE REVOKEABLE DIFFERS FROM ORIGINAL REQUEST                                     | MANDATE_REVOKEABLE_DIFFERS_FROM_ORIGINAL_REQUEST                                                                                                                 |
| E4532           | Mandate request not created                                                                                                                                                                                                                      | Mandate request not created                                                          | Mandate_Request_Not_Created                                                                                                                                      |
| E4115           | Transaction failed as mandate request limit is breached                                                                                                                                                                                          | MANDATE REQUEST LIMIT HAS BREACHED                                                   | MANDATE_REQUEST_LIMIT_HAS_BREACHED                                                                                                                               |
| E4077           | MANDATE REQUEST IS DECLINED BY MERCHANT (PAYEE)                                                                                                                                                                                                  | MANDATE REQUEST IS DECLINED BY MERCHANT (PAYEE)                                      | MANDATE_REQUEST_IS_DECLINED_BY_MERCHANT_PAYEE                                                                                                                    |
| E4607           | Mandate Request Approved                                                                                                                                                                                                                         | Mandate Request Approved                                                             | Mandate_Request_Approved                                                                                                                                         |
| E4313           | MANDATE REGISTRATION NOT ALLOWED FOR CC PF PPF ACT (BANK'S POLICY)                                                                                                                                                                               | MANDATE REGISTRATION NOT ALLOWED FOR CC PF PPF ACT (BANKNULLS PO                     | MANDATE_REGISTRATION_NOT_ALLOWED_FOR_CC_PF_PPF_ACT_BANKS_POLICY                                                                                                  |
| E4329           | MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENTPAYER PSP NOT CERTIFIED FOR 2.7                                                                                                                                                                 | MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENTPAYER PSP NOT C                     | MANDATE_RECURRENCE_RULE_TAG_SHOULD_NOT_BE_PRESENTPAYER_PSP_NOT_CERTIFIED_FOR_2_7                                                                                 |
| E4330           | MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENT PAYEE PSP NOT CERTIFIED FOR 2.7                                                                                                                                                                | MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENT PAYEE PSP NOT                      | MANDATE_RECURRENCE_RULE_TAG_SHOULD_NOT_BE_PRESENT_PAYEE_PSP_NOT_CERTIFIED_FOR_2_7                                                                                |
| E4073           | MANDATE RECURRENCE PATTERN.BLOCK=N IS ALLOWED ONLY IF THE PURPOSE CODE=14                                                                                                                                                                        | MANDATE RECURRENCE PATTERN.BLOCK=N IS ALLOWED ONLY IF THE PURPOS                     | MANDATE_RECURRENCE_PATTERN_BLOCK_N_IS_ALLOWED_ONLY_IF_THE_PURPOSE_CODE_14                                                                                        |
| E4074           | MANDATE RECURRENCE PATTERN. REVOKABLE=Y, ONLY Y IS ALLOWED IF THE PURPOSE CODE=14                                                                                                                                                                | MANDATE RECURRENCE PATTERN. REVOKABLE=Y, ONLY Y IS ALLOWED IF TH                     | MANDATE_RECURRENCE_PATTERN__REVOKABLE_Y_ONLY_Y_IS_ALLOWED_IF_THE_PURPOSE_CODE_14                                                                                 |
| E4053           | Transaction failed due to mandate not present                                                                                                                                                                                                    | MANDATE NOT PRESENT                                                                  | MANDATE_NOT_PRESENT                                                                                                                                              |
| E4124           | Modification request declined by the customer                                                                                                                                                                                                    | MANDATE MODIFY REQUEST IS DECLINED (PAYER)                                           | MANDATE_MODIFY_REQUEST_IS_DECLINED_PAYER                                                                                                                         |
| E4131           | Modification request declined by merchant                                                                                                                                                                                                        | MANDATE MODIFICATION DECLINED BY MERCHANT                                            | MANDATE_MODIFICATION_DECLINED_BY_MERCHANT                                                                                                                        |
| E4108           | Transaction failed as mandate is paused by the user                                                                                                                                                                                              | MANDATE IS PAUSED BY USER                                                            | MANDATE_IS_PAUSED_BY_USER                                                                                                                                        |
| E4109           | Transaction failed as mandate is already honoured                                                                                                                                                                                                | MANDATE IS ALREADY HONOURED                                                          | MANDATE_IS_ALREADY_HONOURED_1                                                                                                                                    |
| E4111           | Transaction failed as mandate is expired                                                                                                                                                                                                         | MANDATE HAS EXPIRED                                                                  | MANDATE_HAS_EXPIRED                                                                                                                                              |
| E4110           | Transaction failed as mandate is revoked by the user                                                                                                                                                                                             | MANDATE HAS BEEN REVOKED                                                             | MANDATE_HAS_BEEN_REVOKED                                                                                                                                         |
| E4127           | Transaction declined as payee is a non-merchant                                                                                                                                                                                                  | MANDATE DECLINED AS PAYEE IS NON-MERCHANT (PAYER)                                    | MANDATE_DECLINED_AS_PAYEE_IS_NON_MERCHANT_PAYER                                                                                                                  |
| E4116           | Transaction failed as mandate amount is higher than allowed by customer's application                                                                                                                                                            | MANDATE DEBIT IS BEYOND PSP SPECIFIED AMOUNT CAP                                     | MANDATE_DEBIT_IS_BEYOND_PSP_SPECIFIED_AMOUNT_CAP                                                                                                                 |
| E4121           | Transaction failed as mandate is not allowed to be created on this merchant                                                                                                                                                                      | MANDATE CANNOT BE CREATED ON THIS VPA (PAYER)                                        | MANDATE_CANNOT_BE_CREATED_ON_THIS_VPA_PAYER                                                                                                                      |
| E4535           | Transaction failed due to amount mismatch error                                                                                                                                                                                                  | Mandate amounts mis-matched                                                          | Mandate_Amounts_Mis_matched                                                                                                                                      |
| E4293           | Transaction declined as mandate amount limit exceeded                                                                                                                                                                                            | MANDATE AMOUNT CAP IS EXCEEDED                                                       | MANDATE_AMOUNT_CAP_IS_EXCEEDED                                                                                                                                   |
| E806            | You have opted out of Lazypay service                                                                                                                                                                                                            | LP_USER_OPTED_OUT                                                                    | LP_USER_OPTED_OUT                                                                                                                                                |
| E807            | Sorry! You are currently not registered for LazyPay                                                                                                                                                                                              | LP_USER_INELIGIBLE                                                                   | LP_USER_INELIGIBLE                                                                                                                                               |
| E805            | Your Lazypay account is blocked                                                                                                                                                                                                                  | LP_USER_BLOCKED                                                                      | LP_USER_BLOCKED                                                                                                                                                  |
| E4001           | ISSUER NOT LIVE ON UPI                                                                                                                                                                                                                           | Low confidence                                                                       | ISSUER_NOT_LIVE_ON_UPI                                                                                                                                           |
| E4359           | Transaction failed due to lost or stolen card from customer's bank                                                                                                                                                                               | LOST OR STOLEN CARD (REMITTER)                                                       | LOST_OR_STOLEN_CARD_REMITTER                                                                                                                                     |
| E4360           | Transaction failed due to lost or stolen card from acquirer's bank                                                                                                                                                                               | LOST OR STOLEN CARD (BENEFICIARY)                                                    | LOST_OR_STOLEN_CARD_BENEFICIARY                                                                                                                                  |
| E1505           | You don't have sufficient credit limit to complete this transaction.                                                                                                                                                                             | LOAN_AMOUNT_GREATER * THAN_ELIGIBLITY                                                | LOAN_AMOUNT_GREATER_THAN_ELIGIBLITY                                                                                                                              |
| E2408           | Link and Pay not Eligible                                                                                                                                                                                                                        | LINK_AND_PAY_NOT_ELIGIBLE                                                            | LINK_AND_PAY_NOT_ELIGIBLE                                                                                                                                        |
| E4389           | LIMIT EXCEEDED FOR REMITTING BANK/ISSUING BANK                                                                                                                                                                                                   | LIMIT EXCEEDED FOR REMITTING BANK/ISSUING BANK                                       | LIMIT_EXCEEDED_FOR_REMITTING_BANK_ISSUING_BANK                                                                                                                   |
| E2503           | Late otp submission on Headless                                                                                                                                                                                                                  | LATE_OTP_SUBMISSSION * ON_HEADLESS                                                   | LATE_OTP_SUBMISSSION_ON_HEADLESS                                                                                                                                 |
| E4158           | Transaction failed due to timeout at acquirer's end                                                                                                                                                                                              | Issuer unavailable or switch inoperative                                             | REQAUTH_TIME_OUT_FOR_PAY                                                                                                                                         |
| E9254           | Authorization Platform or Switch / Issuer system inoperative or Not Supported                                                                                                                                                                    | Issuer or Switch is Inoperative                                                      | BANK_NOT_SUPPORTED_BY_SWITCH                                                                                                                                     |
| E9254           | ACQUIRER/BENEFICIARY UNAVAILABLE(TIMEOUT)                                                                                                                                                                                                        | ACQUIRER_BENEFICIARY_UNAVAILABLE_TIMEOUT                                             |                                                                                                                                                                  |
| E714            | Card authentication failed due to invalid ZIP code                                                                                                                                                                                               | INVALID_ZIP                                                                          | INVALID_ZIP                                                                                                                                                      |
| E1020           | Transaction ID you've generated isn't valid                                                                                                                                                                                                      | INVALID_TRANSACTION_ID                                                               | INVALID_TRANSACTION_ID                                                                                                                                           |
| E1603           | Transaction failed. Mobile number not registered for the given card.                                                                                                                                                                             | INVALID_PHONE_NO                                                                     | INVALID_PHONE_NO                                                                                                                                                 |
| E1646           | Invalid PayU ID                                                                                                                                                                                                                                  | INVALID_PAYU_ID                                                                      | INVALID_PAYU_ID                                                                                                                                                  |
| E707            | Transaction failed due to invalid Primary Account Number. (Primary Account Number or PAN is the number that is embossed and/or encoded on a plastic card that identifies the issuer and the particular cardholder account.)                      | INVALID_PAN                                                                          | INVALID_PAN                                                                                                                                                      |
| E340            | Transaction failed due to invalid OTP                                                                                                                                                                                                            | INVALID_OTP                                                                          | INVALID_OTP                                                                                                                                                      |
| E1665           | Incorrect request received for one click transaction                                                                                                                                                                                             | INVALID_ONE_CLICK * REQUEST_RECEIVED                                                 | INVALID_ONE_CLICK_REQUEST_RECEIVED                                                                                                                               |
| E339            | Transaction failed due to invalid mobile number                                                                                                                                                                                                  | INVALID_MOBILE_NUMBER                                                                | INVALID_MOBILE_NUMBER                                                                                                                                            |
| E1501           | Transaction amount is less than the minimum amount accepted by issuing bank for processing EMI.                                                                                                                                                  | INVALID_MIN_AMOUNT_EMI                                                               | INVALID_MIN_AMOUNT_EMI                                                                                                                                           |
| E1637           | Merchant Type Not Supported                                                                                                                                                                                                                      | INVALID_MERCHANT_TYPE                                                                | INVALID_MERCHANT_TYPE                                                                                                                                            |
| E1647           | Invalid Merchant Key                                                                                                                                                                                                                             | INVALID_MERCHANT_KEY                                                                 | INVALID_MERCHANT_KEY                                                                                                                                             |
| E2409           | Transaction amount is more than the maximum amount accepted by issuing bank for processing EMI.                                                                                                                                                  | INVALID_MAX_AMOUNT_EMI                                                               | INVALID_MAX_AMOUNT_EMI                                                                                                                                           |
| E327            | Authentication failed to due invalid login                                                                                                                                                                                                       | INVALID_LOGIN                                                                        | INVALID_LOGIN                                                                                                                                                    |
| E2407           | Missing User details                                                                                                                                                                                                                             | INVALID_LINK_AND_PAY * REQUEST_RECEIVED                                              | INVALID_LINK_AND_PAY_REQUEST_RECEIVED                                                                                                                            |
| E332            | Card authentication failed due to invalid FAX number                                                                                                                                                                                             | INVALID_FAX                                                                          | INVALID_FAX                                                                                                                                                      |
| E323            | Card authentication failed due to invalid card expiry date.                                                                                                                                                                                      | INVALID_EXPIRY_DATE                                                                  | INVALID_EXPIRY_DATE                                                                                                                                              |
| E910            | EMI is not supported on this card                                                                                                                                                                                                                | INVALID_EMI_CARD_BIN                                                                 | INVALID_EMI_CARD_BIN                                                                                                                                             |
| E331            | Card authentication failed due to invalid email id                                                                                                                                                                                               | INVALID_EMAIL_ID                                                                     | INVALID_EMAIL_ID                                                                                                                                                 |
| E2081           | Invalid Device Id                                                                                                                                                                                                                                | INVALID_DEVICE_ID                                                                    | INVALID_DEVICE_ID                                                                                                                                                |
| E333            | Card authentication failed due to invalid contact/phone details                                                                                                                                                                                  | INVALID_CONTACT                                                                      | INVALID_CONTACT                                                                                                                                                  |
| E709            | Transaction failed due to invalid credit card name                                                                                                                                                                                               | INVALID_CARD_NAME                                                                    | INVALID_CARD_NAME                                                                                                                                                |
| E1702           | Invalid Action                                                                                                                                                                                                                                   | INVALID_ACTION                                                                       | INVALID_ACTION                                                                                                                                                   |
| E1625           | Card not enabled for Ecomm transactions, either the card is newly issued or has not been used for any online transaction during last 12 months                                                                                                   | Invalid/nonexistent account specified (general)                                      | CARD_NOT_ENABLED_FOR_ECOMM_TXN                                                                                                                                   |
| E4148           | INVALID/INCORRECT ATM PIN                                                                                                                                                                                                                        | INVALID/INCORRECT ATM PIN                                                            | INVALID_INCORRECT_ATM_PIN                                                                                                                                        |
| E4042           | Invalid verification token                                                                                                                                                                                                                       | Invalid verification token                                                           | Invalid_Verification_Token                                                                                                                                       |
| E207            | Bank denied transaction on the card.                                                                                                                                                                                                             | Invalid transaction                                                                  | INVALID_TRANSACTION                                                                                                                                              |
| E4521           | Transaction failed due to invalid MCC details                                                                                                                                                                                                    | Invalid Terminal Id                                                                  | Invalid_Terminal_Id                                                                                                                                              |
| E2110           | Unable to process the request.                                                                                                                                                                                                                   | Invalid Response From Up Streaming Server                                            | INVALID_REQUEST_FROM_PG_TO_DOWNSTREAM                                                                                                                            |
| E4367           | INVALID RESPONSE CODE                                                                                                                                                                                                                            | INVALID RESPONSE CODE                                                                | INVALID_RESPONSE_CODE                                                                                                                                            |
| E710            | Transaction failed due to invalid PIN                                                                                                                                                                                                            | Invalid PIN                                                                          | INVALID_PIN                                                                                                                                                      |
| E4386           | INVALID OTP                                                                                                                                                                                                                                      | INVALID OTP                                                                          | INVALID_OTP_1                                                                                                                                                    |
| E4371           | Transaction declined due to invalid merchant details                                                                                                                                                                                             | INVALID MERCHANT (PAYEE PSP)                                                         | INVALID_MERCHANT_PAYEE_PSP                                                                                                                                       |
| E4332           | INVALID MERCHANT (ACQURIER)                                                                                                                                                                                                                      | INVALID MERCHANT (ACQURIER)                                                          | INVALID_MERCHANT_ACQURIER                                                                                                                                        |
| E341            | Transaction failed due to invalid merchant                                                                                                                                                                                                       | Invalid Merchant                                                                     | INVALID_MERCHANT                                                                                                                                                 |
| E305            | The transaction failed due to invalid or absent card number.                                                                                                                                                                                     | Invalid issuer                                                                       | CARD_NUMBER_INVALID                                                                                                                                              |
| E1632           | Transaction declined due to either incorrect cvv/expiry or card validation failure                                                                                                                                                               | Invalid card number                                                                  | CARD_VALIDATION_FAILED                                                                                                                                           |
| E4368           | INVALID BENEFICIARY CREDENTIALS                                                                                                                                                                                                                  | INVALID BENEFICIARY CREDENTIALS                                                      | INVALID_BENEFICIARY_CREDENTIALS                                                                                                                                  |
| E4336           | INVALID AMOUNT (REMITTER)                                                                                                                                                                                                                        | INVALID AMOUNT (REMITTER)                                                            | INVALID_AMOUNT_REMITTER                                                                                                                                          |
| E4337           | INVALID AMOUNT (BENEFICIARY)                                                                                                                                                                                                                     | INVALID AMOUNT (BENEFICIARY)                                                         | INVALID_AMOUNT_BENEFICIARY                                                                                                                                       |
| E715            | Invalid amount sent to the bank                                                                                                                                                                                                                  | Invalid amount                                                                       | INVALID_AMOUNT                                                                                                                                                   |
| E903            | International cards are not accepted                                                                                                                                                                                                             | INTERNATIONAL_CARD * NOT_ALLOWED                                                     | INTERNATIONAL_CARD_NOT_ALLOWED                                                                                                                                   |
| E4040           | International Service not activated/disabled                                                                                                                                                                                                     | International Service not activated/disabled                                         | International_Service_Not_Activated_disabled                                                                                                                     |
| E9239           | International Acceptance not enabled                                                                                                                                                                                                             | International Acceptance not enabled                                                 | INTERNATIONAL_ACCEPTANCE_NOT_ENABLED                                                                                                                             |
| E1617           | Internal server Error [S2S FLow]                                                                                                                                                                                                                 | INTERNAL_SERVER * ERROR_S2SFLOW                                                      | INTERNAL_SERVER_ERROR_S2SFLOW                                                                                                                                    |
| E1901           | Customer chose Collect over Intent                                                                                                                                                                                                               | INTENT_SDK_FALLBACK                                                                  | INTENT_SDK_FALLBACK                                                                                                                                              |
| E1900           | Unable to open intent, switched to collect                                                                                                                                                                                                       | INTENT_OPENING_FAILED                                                                | INTENT_OPENING_FAILED                                                                                                                                            |
| E1208           | Transaction failed because the customer does not have the necessary funds or he has given a wrong expiry date.                                                                                                                                   | INSUFFICIENT_FUNDS * INCORRECT_EXPIRY                                                | INSUFFICIENT_FUNDS_INCORRECT_EXPIRY                                                                                                                              |
| E713            | The account against which the payment was made has insufficient funds,or, card authentication failed due to invalid card expiry date                                                                                                             | INSUFFICIENT_FUNDS * EXPIRY_INVALID                                                  | INSUFFICIENT_FUNDS_EXPIRY_INVALID                                                                                                                                |
| E719            | Transaction failed due to card authentication failure and/or insufficient funds                                                                                                                                                                  | INSUFFICIENT_FUNDS * AUTHENTICATION_FAILURE                                          | INSUFFICIENT_FUNDS_AUTHENTICATION_FAILURE                                                                                                                        |
| E706            | The account against which the payment was made has insufficient funds.                                                                                                                                                                           | Insufficient funds/over credit limit / Not sufficient funds                          | INSUFFICIENT_FUNDS                                                                                                                                               |
| E4390           | INCORRECT OTP                                                                                                                                                                                                                                    | INCORRECT OTP                                                                        | INCORRECT_OTP                                                                                                                                                    |
| E1502           | Incorrect request for SI, CC received in drop_category.                                                                                                                                                                                          | INCOMPLETE_SI_REQUEST                                                                | INCOMPLETE_SI_REQUEST                                                                                                                                            |
| E219            | Error at the Bank Server end                                                                                                                                                                                                                     | INCOMPLETE_BANK_RESPONSE                                                             | INCOMPLETE_BANK_RESPONSE                                                                                                                                         |
| E4391           | Transaction failed due to customer's account being inactive or dormant                                                                                                                                                                           | INACTIVE OR DORMANT ACCOUNT (REMITTER)                                               | INACTIVE_OR_DORMANT_ACCOUNT_REMITTER                                                                                                                             |
| E4392           | Transaction failed due to acquirer' account being inactive or dormant                                                                                                                                                                            | INACTIVE OR DORMANT ACCOUNT (BENEFICIARY)                                            | INACTIVE_OR_DORMANT_ACCOUNT_BENEFICIARY                                                                                                                          |
| E4191           | IMPS TRANSACTION IS ALREADY BEEN PROCESSED                                                                                                                                                                                                       | IMPS TRANSACTION IS ALREADY BEEN PROCESSED                                           | IMPS_TRANSACTION_IS_ALREADY_BEEN_PROCESSED                                                                                                                       |
| E4189           | IMPS PROCESSING FAILED IN UPI                                                                                                                                                                                                                    | IMPS PROCESSING FAILED IN UPI                                                        | IMPS_PROCESSING_FAILED_IN_UPI                                                                                                                                    |
| E4190           | IMPS IS SIGNED OFF                                                                                                                                                                                                                               | IMPS IS SIGNED OFF                                                                   | IMPS_IS_SIGNED_OFF                                                                                                                                               |
| E4192           | IMPS IS DECLINED                                                                                                                                                                                                                                 | IMPS IS DECLINED                                                                     | IMPS_IS_DECLINED                                                                                                                                                 |
| E4159           | ILLEGAL OPERATION                                                                                                                                                                                                                                | ILLEGAL OPERATION                                                                    | ILLEGAL_OPERATION                                                                                                                                                |
| E4199           | IFSC IS NOT PRESENT                                                                                                                                                                                                                              | IFSC IS NOT PRESENT                                                                  | IFSC_IS_NOT_PRESENT                                                                                                                                              |
| E1639           | Host down                                                                                                                                                                                                                                        | HOST_DOWN                                                                            | HOST_DOWN                                                                                                                                                        |
| E2502           | Payu unable to parse ACS page for native                                                                                                                                                                                                         | HEADLESS_ELEMENT_MISSING                                                             | HEADLESS_ELEMENT_MISSING                                                                                                                                         |
| E4250           | HEADER & URL VERSION IS MISMATCHED                                                                                                                                                                                                               | HEADER & URL VERSION IS MISMATCHED                                                   | HEADER_URL_VERSION_IS_MISMATCHED                                                                                                                                 |
| E4076           | GLOBAL ADDRESS NOT SUPPORTED IN MANDATE                                                                                                                                                                                                          | GLOBAL ADDRESS NOT SUPPORTED IN MANDATE                                              | GLOBAL_ADDRESS_NOT_SUPPORTED_IN_MANDATE                                                                                                                          |
| E4933           | NPCI General error                                                                                                                                                                                                                               | GENERAL ERROR                                                                        | NPCI_ERROR                                                                                                                                                       |
| E4382           | FUNCTIONALITY NOT YET AVAILABLE FOR MERCHANT THROUGH THE ACQUIRING BANK                                                                                                                                                                          | FUNCTIONALITY NOT YET AVAILABLE FOR MERCHANT THROUGH THE ACQUIRI                     | FUNCTIONALITY_NOT_YET_AVAILABLE_FOR_MERCHANT_THROUGH_THE_ACQUIRING_BANK                                                                                          |
| E4383           | FUNCTIONALITY NOT YET AVAILABLE FOR CUSTOMER THROUGH THE PAYEE PSP                                                                                                                                                                               | FUNCTIONALITY NOT YET AVAILABLE FOR CUSTOMER THROUGH THE PAYEE P                     | FUNCTIONALITY_NOT_YET_AVAILABLE_FOR_CUSTOMER_THROUGH_THE_PAYEE_PSP                                                                                               |
| E4022           | Transaction failed due to freeze period for the first time customer                                                                                                                                                                              | FREEZE PERIOD FOR FIRST TIME USER                                                    | FREEZE_PERIOD_FOR_FIRST_TIME_USER                                                                                                                                |
| E4154           | FORMATION IS NOT PROPER                                                                                                                                                                                                                          | FORMATION IS NOT PROPER                                                              | FORMATION_IS_NOT_PROPER                                                                                                                                          |
| E4338           | FORMAT ERROR (INVALID FORMAT) (REMITTER)                                                                                                                                                                                                         | FORMAT ERROR (INVALID FORMAT) (REMITTER)                                             | FORMAT_ERROR_INVALID_FORMAT_REMITTER                                                                                                                             |
| E4339           | FORMAT ERROR (INVALID FORMAT) (BENEFICIARY)                                                                                                                                                                                                      | FORMAT ERROR (INVALID FORMAT) (BENEFICIARY)                                          | FORMAT_ERROR_INVALID_FORMAT_BENEFICIARY                                                                                                                          |
| E2102           | Transaction not approved                                                                                                                                                                                                                         | Format error                                                                         | TXN_FAILURE                                                                                                                                                      |
| E4194           | FORM PROCESSING HAS BEEN FAILED IN UPI                                                                                                                                                                                                           | FORM PROCESSING HAS BEEN FAILED IN UPI                                               | FORM_PROCESSING_HAS_BEEN_FAILED_IN_UPI                                                                                                                           |
| E4193           | FORM HAS BEEN SIGNED OFF                                                                                                                                                                                                                         | FORM HAS BEEN SIGNED OFF                                                             | FORM_HAS_BEEN_SIGNED_OFF                                                                                                                                         |
| E4269           | FOREX Error in ValQR                                                                                                                                                                                                                             | FOREX Error in ValQR                                                                 | FOREX_Error_In_ValQR                                                                                                                                             |
| E9245           | Force Post                                                                                                                                                                                                                                       | Force Post                                                                           | FORCE_POST                                                                                                                                                       |
| E4021           | Transaction failed due to first transaction limit exceeded by the customer                                                                                                                                                                       | FIRST TRANSACTION LIMIT EXCEEDED                                                     | FIRST_TRANSACTION_LIMIT_EXCEEDED                                                                                                                                 |
| E9210           | File Update not Supported by receiver                                                                                                                                                                                                            | File Update not Supported by receiver                                                | FILE_UPDATE_NOT_SUPPORTED_BY_RECEIVER                                                                                                                            |
| E9215           | File Update not Successful                                                                                                                                                                                                                       | File Update not Successful                                                           | FILE_UPDATE_NOT_SUCCESSFUL                                                                                                                                       |
| E9214           | File Update File Locked Out                                                                                                                                                                                                                      | File Update File Locked Out                                                          | FILE_UPDATE_FILE_LOCKED_OUT                                                                                                                                      |
| E9213           | File Update Field Edit Error                                                                                                                                                                                                                     | File Update Field Edit Error                                                         | FILE_UPDATE_FIELD_EDIT_ERROR                                                                                                                                     |
| E4888           | FAILURE                                                                                                                                                                                                                                          | FAILURE                                                                              | FAILURE_3                                                                                                                                                        |
| E4890           | FAILURE                                                                                                                                                                                                                                          | FAILURE                                                                              | FAILURE_5                                                                                                                                                        |
| E4891           | FAILURE                                                                                                                                                                                                                                          | FAILURE                                                                              | FAILURE_6                                                                                                                                                        |
| E4892           | FAILURE                                                                                                                                                                                                                                          | FAILURE                                                                              | FAILURE_7                                                                                                                                                        |
| E4897           | FAILURE                                                                                                                                                                                                                                          | FAILURE                                                                              | FAILURE_11                                                                                                                                                       |
| E4900           | FAILURE                                                                                                                                                                                                                                          | FAILURE                                                                              | FAILURE_13                                                                                                                                                       |
| E4903           | FAILURE                                                                                                                                                                                                                                          | FAILURE                                                                              | FAILURE_16                                                                                                                                                       |
| E4904           | FAILURE                                                                                                                                                                                                                                          | FAILURE                                                                              | FAILURE_17                                                                                                                                                       |
| E4907           | FAILURE                                                                                                                                                                                                                                          | FAILURE                                                                              | FAILURE_19                                                                                                                                                       |
| E4909           | FAILURE                                                                                                                                                                                                                                          | FAILURE                                                                              | FAILURE_21                                                                                                                                                       |
| E4910           | FAILURE                                                                                                                                                                                                                                          | FAILURE                                                                              | FAILURE_22                                                                                                                                                       |
| E4803           | Transaction failed at bank end                                                                                                                                                                                                                   | Failed                                                                               | Failed                                                                                                                                                           |
| E1202           | Third Party Funds Transfer facility and Secure Access not enabled.                                                                                                                                                                               | FACILITY_UNAVAILABLE                                                                 | FACILITY_UNAVAILABLE                                                                                                                                             |
| E336            | Transaction failed due to incorrect card expiry date and/or insufficient funds                                                                                                                                                                   | EXPIRY_DATE_LOW_FUNDS                                                                | EXPIRY_DATE_LOW_FUNDS                                                                                                                                            |
| E311            | Transaction declined due to invalid expiry details or the card is expired                                                                                                                                                                        | Expired card                                                                         | EXPIRED_CARD                                                                                                                                                     |
| E4122           | Transaction failed as execution day and execution rule mismatch                                                                                                                                                                                  | EXECUTION DAY AND EXECUTION RULE MISMATCH (PAYER)                                    | EXECUTION_DAY_AND_EXECUTION_RULE_MISMATCH_PAYER                                                                                                                  |
| E4536           | Transaction failed as execution amount is higher than mandate created amount                                                                                                                                                                     | Execution amount exceeded to Mandate approved amount                                 | Execution_Amount_Exceeded_To_Mandate_Approved_Amount                                                                                                             |
| E909            | Transaction amount exceeds the withdrawal limit of the user account                                                                                                                                                                              | Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc                     | TRANSACTION_MAX_LIMIT_EXCEEDED                                                                                                                                   |
| E9230           | Exceeds Cash Limit                                                                                                                                                                                                                               | Exceeds Cash Limit                                                                   | EXCEEDS_CASH_LIMIT                                                                                                                                               |
| E1645           | Transaction failed during authentication                                                                                                                                                                                                         | ERROR_OCCURRED_IN * ENROLLMENT_VALIDATION                                            | ERROR_OCCURRED_IN_ENROLLMENT_VALIDATION                                                                                                                          |
| E209            | No Bank response                                                                                                                                                                                                                                 | Error: The request was received, but a service did not finish ru                     | NO_BANK_RESPONSE                                                                                                                                                 |
| E210            | Authentication failure or there is a delay in processing the transaction.                                                                                                                                                                        | Error - The request was received, but there was a timeout at the                     | COMMUNICATION_ERROR                                                                                                                                              |
| E208            | Error at the Bank Server end                                                                                                                                                                                                                     | Error - The request was received but there was a server timeout.                     | BANK_SERVER_ERROR                                                                                                                                                |
| E309            | Bank denied transaction on the card.                                                                                                                                                                                                             | Error - General system failure                                                       | GENERAL_SYSTEM_ERROR_PG                                                                                                                                          |
| E1909           | Error while processing enstage request                                                                                                                                                                                                           | ENSTAGE_PROCESSING_ERROR                                                             | ENSTAGE_PROCESSING_ERROR                                                                                                                                         |
| E1908           | BIN not supported for pureS2S                                                                                                                                                                                                                    | ENSTAGE_BIN_NOT * ELIGIBLE_PURES2S                                                   | ENSTAGE_BIN_NOT_ELIGIBLE_PURES2S                                                                                                                                 |
| E4178           | Transaction failed due to technical error at customer's application                                                                                                                                                                              | ENCRYPTION ERROR                                                                     | ADDRESS_RESOLUTION_IS_FAILED                                                                                                                                     |
| E303            | Payer could not be authenticated                                                                                                                                                                                                                 | Encountered a Payer Authentication problem. Payer could not be a                     | AUTHENTICATION_ERROR                                                                                                                                             |
| E1301           | EMI not applicable for this transactions.                                                                                                                                                                                                        | EMI_NOT_APPLICABLE                                                                   | EMI_NOT_APPLICABLE                                                                                                                                               |
| E9236           | E-commerce Decline                                                                                                                                                                                                                               | E-commerce Decline                                                                   | ECOMMERCE_DECLINE                                                                                                                                                |
| E1300           | Customer has pressed the refresh key during the payment process.                                                                                                                                                                                 | DUPLICATE_SESSION_ID                                                                 | DUPLICATE_SESSION_ID                                                                                                                                             |
| E344            | Transaction Failed                                                                                                                                                                                                                               | DUPLICATE_CONTACT                                                                    | DUPLICATE_CONTACT                                                                                                                                                |
| E504            | The transaction has been identified as duplicate transaction.                                                                                                                                                                                    | Duplicate Transaction                                                                | DUPLICATE_TRANSACTION                                                                                                                                            |
| E4020           | DUPLICATE RRN FOUND IN THE TRANSACTION. (REMITTER)                                                                                                                                                                                               | DUPLICATE RRN FOUND IN THE TRANSACTION. (REMITTER)                                   | DUPLICATE_RRN_FOUND_IN_THE_TRANSACTION__REMITTER                                                                                                                 |
| E4019           | DUPLICATE RRN FOUND IN THE TRANSACTION. (BENEFICIARY)                                                                                                                                                                                            | DUPLICATE RRN FOUND IN THE TRANSACTION. (BENEFICIARY)                                | DUPLICATE_RRN_FOUND_IN_THE_TRANSACTION__BENEFICIARY                                                                                                              |
| E4319           | DUPLICATE MANDATE REQUEST FOR SAME ITEM                                                                                                                                                                                                          | DUPLICATE MANDATE REQUEST FOR SAME ITEM                                              | DUPLICATE_MANDATE_REQUEST_FOR_SAME_ITEM                                                                                                                          |
| E4118           | Transaction failed due to duplicate mandate request                                                                                                                                                                                              | DUPLICATE MANDATE REQUEST BD                                                         | DUPLICATE_MANDATE_REQUEST_BD                                                                                                                                     |
| E9212           | Duplicate File Update Record                                                                                                                                                                                                                     | Duplicate File Update Record                                                         | DUPLICATE_FILE_UPDATE_RECORD                                                                                                                                     |
| E4033           | DUPLICATE BLOCKFUND FOR MANDATE REQUEST                                                                                                                                                                                                          | DUPLICATE BLOCKFUND FOR MANDATE REQUEST                                              | DUPLICATE_BLOCKFUND_FOR_MANDATE_REQUEST                                                                                                                          |
| E307            | Transaction declined with do not honor                                                                                                                                                                                                           | Do not honor                                                                         | DO_NOT_HONOUR                                                                                                                                                    |
| E307            | Risk Service denied transaction                                                                                                                                                                                                                  | Risk Service denied transaction - DO_NOT_HONOUR                                      |                                                                                                                                                                  |
| E804            | Payment gateway seems to be down at this moment.                                                                                                                                                                                                 | DISABLE_PG_NOT_AVAILABLE_HANDLING                                                    | DISABLE_PG_NOT_AVAILABLE_HANDLING                                                                                                                                |
| E4212           | DEVICE REGISTRATION FAILED IN UPI                                                                                                                                                                                                                | DEVICE REGISTRATION FAILED IN UPI                                                    | DEVICE_REGISTRATION_FAILED_IN_UPI                                                                                                                                |
| E225            | Transaction in Progress                                                                                                                                                                                                                          | Destination cannot be found for routing / Unable to route transa                     | TRANSACTION_IN_PROGRESS                                                                                                                                          |
| DEFAULT         | Bank was unable to authenticate.                                                                                                                                                                                                                 | DEFAULT_VALUE                                                                        | DEFAULT_VALUE                                                                                                                                                    |
| E712            | The transaction could not be processed due to incomplete data provided at the users end.                                                                                                                                                         | Declined - The request is missing one or more fields                                 | INCOMPLETE_DATA                                                                                                                                                  |
| E2100           | Invalid Request received for processing.                                                                                                                                                                                                         | Declined - One or more fields in the request contains invalid da                     | INVALID_DATA_RECEIVED_IN_REQUEST                                                                                                                                 |
| E1638           | Transaction Already Reversed                                                                                                                                                                                                                     | Decline - The transaction has already been settled or reversed.                      | TRANSACTION_REVERSED                                                                                                                                             |
| E1701           | Invalid Payment ID                                                                                                                                                                                                                               | Decline - The request ID is invalid.                                                 | INVALID_PAYMENT_ID                                                                                                                                               |
| E1623           | Customer Authentication failed due to incorrect ATM PIN.                                                                                                                                                                                         | Decline - The Pinless Debit card's use frequency or maximum amou                     | ATM_MAX_LIMIT_EXCEEDED                                                                                                                                           |
| E329            | Transaction declined by the issuer                                                                                                                                                                                                               | Decline - The issuing bank has questions about the request. You                      | ISSUER_DECLINED_LOW_FUNDS                                                                                                                                        |
| E902            | Invalid Card Number                                                                                                                                                                                                                              | Decline - The card type is not accepted by the payment processor                     | INVALID_CARD_TYPE                                                                                                                                                |
| E1628           | Daily limit exceeded                                                                                                                                                                                                                             | Decline - The card has reached the credit limit                                      | LIMIT_EXCEEDED                                                                                                                                                   |
| E1653           | Card Issuer Unavailable                                                                                                                                                                                                                          | Decline - Issuing bank unavailable                                                   | ISSUER_UNAVAILABLE                                                                                                                                               |
| E312            | Bank denied transaction on the card.                                                                                                                                                                                                             | Decline - General decline of the card. No other information prov                     | BANK_DENIED                                                                                                                                                      |
| E2111           | Transaction failed due to technical issue at Issuer/Acquirer end                                                                                                                                                                                 | Decline - General decline by the processor.                                          | GENERAL_DECLINE_BY_PROCESSOR                                                                                                                                     |
| E1400           | Invalid data received from bank.                                                                                                                                                                                                                 | Decline - card verification number (CVN) did not match                               | INVALID_DATA_NEW                                                                                                                                                 |
| E4182           | Transaction failed as debit reversal failed in the customer's account                                                                                                                                                                            | DEBIT REVERT HAS BEEN FAILED                                                         | DEBIT_REVERT_HAS_BEEN_FAILED                                                                                                                                     |
| E4142           | Debit failed due to timeout at customer's bank                                                                                                                                                                                                   | DEBIT REVERSAL TIMEOUT(REVERSAL)                                                     | DEBIT_REVERSAL_TIMEOUT_REVERSAL                                                                                                                                  |
| E4179           | Transaction failed as debit failed from the customer's account                                                                                                                                                                                   | DEBIT HAS BEEN FAILED                                                                | DEBIT_HAS_BEEN_FAILED                                                                                                                                            |
| E4035           | DEBIT AMOUNT IS NOT BLOCKED FOR THE CUSTOMER                                                                                                                                                                                                     | DEBIT AMOUNT IS NOT BLOCKED FOR THE CUSTOMER                                         | DEBIT_AMOUNT_IS_NOT_BLOCKED_FOR_THE_CUSTOMER                                                                                                                     |
| E4036           | DEBIT AMOUNT GREATER THAN BLOCKED AMOUNT                                                                                                                                                                                                         | DEBIT AMOUNT GREATER THAN BLOCKED AMOUNT                                             | DEBIT_AMOUNT_GREATER_THAN_BLOCKED_AMOUNT                                                                                                                         |
| E4213           | DATA TAG SHOULD CONTAIN 4 PARTS DURING DEVICE REGISTRATION                                                                                                                                                                                       | DATA TAG SHOULD CONTAIN 4 PARTS DURING DEVICE REGISTRATION                           | DATA_TAG_SHOULD_CONTAIN_4_PARTS_DURING_DEVICE_REGISTRATION                                                                                                       |
| E1627           | Daily limit for wrong ATM PIN attempts reached                                                                                                                                                                                                   | DAILY_ATM_MAX_LIMIT_EXCEEDED                                                         | DAILY_ATM_MAX_LIMIT_EXCEEDED                                                                                                                                     |
| E9235           | CVR validation failed by Issuer                                                                                                                                                                                                                  | CVR validation failed by Issuer                                                      | CVR_VALIDATION_FAILED_BY_ISSUER                                                                                                                                  |
| E206            | Transaction failed as the bank servers are blocked for end of the day processing. Consequently, its servers are temporarily closed to any authentication requests.                                                                               | CUTOFF_ERROR                                                                         | CUTOFF_ERROR                                                                                                                                                     |
| E4352           | Transaction failed due to CBS cut-off at customer's bank                                                                                                                                                                                         | CUT-OFF IS IN PROCESS (REMITTER)                                                     | CUT_OFF_IS_IN_PROCESS_REMITTER                                                                                                                                   |
| E4353           | Transaction failed due to CBS cut-off at acquirer's end                                                                                                                                                                                          | CUT-OFF IS IN PROCESS (BENEFICIARY)                                                  | CUT_OFF_IS_IN_PROCESS_BENEFICIARY                                                                                                                                |
| E9227           | Cut-off in Progress                                                                                                                                                                                                                              | Cut-off in Progress                                                                  | CUTOFF_IN_PROGRESS                                                                                                                                               |
| E2401           | The customer is not eligible for this transaction                                                                                                                                                                                                | CUSTOMER_NOT_ELIGIBLE * FOR_THIS_TRANSACTION                                         | CUSTOMER_NOT_ELIGIBLE_FOR_THIS_TRANSACTION                                                                                                                       |
| E2403           | Customer KYC is pending at Issuer's end                                                                                                                                                                                                          | CUSTOMER_KYC_PENDING                                                                 | CUSTOMER_KYC_PENDING                                                                                                                                             |
| E9206           | Customer Dispute                                                                                                                                                                                                                                 | Customer Dispute                                                                     | CUSTOMER_DISPUTE                                                                                                                                                 |
| E9205           | Customer Cancellation                                                                                                                                                                                                                            | Customer Cancellation                                                                | CUSTOMER_CANCELLATION                                                                                                                                            |
| E205            | Error at the Bank Server end                                                                                                                                                                                                                     | CURL_ERROR_ENROLLED                                                                  | CURL_ERROR_ENROLLED                                                                                                                                              |
| E214            | The Bank servers are unreachable over the network                                                                                                                                                                                                | CURL_CALL_FAILURE                                                                    | CURL_CALL_FAILURE                                                                                                                                                |
| E9223           | Cryptographic Error                                                                                                                                                                                                                              | Cryptographic Error                                                                  | CRYPTOGRAPHIC_ERROR                                                                                                                                              |
| EX311           | Transaction Failed                                                                                                                                                                                                                               | CROSS_BORDER * IMPORT_ERROR                                                          | CROSS_BORDER_IMPORT_ERROR                                                                                                                                        |
| E4214           | CREDS BLOCK SHOULD CONTAIN CORRECT ELEMENTS DURING DEVICE REGISTRATION                                                                                                                                                                           | CREDS BLOCK SHOULD CONTAIN CORRECT ELEMENTS DURING DEVICE REGIST                     | CREDS_BLOCK_SHOULD_CONTAIN_CORRECT_ELEMENTS_DURING_DEVICE_REGISTRATION                                                                                           |
| E4181           | Transaction failed as credit reversal failed from the acquirer's account                                                                                                                                                                         | CREDIT REVERT HAS BEEN FAILED                                                        | CREDIT_REVERT_HAS_BEEN_FAILED                                                                                                                                    |
| E4180           | Credit failed due to technical issue at acquirer's bank                                                                                                                                                                                          | CREDIT HAS BEEN FAILED                                                               | CREDIT_HAS_BEEN_FAILED                                                                                                                                           |
| E4160           | CREDENTIALS IS NOT PRESENT                                                                                                                                                                                                                       | CREDENTIALS IS NOT PRESENT                                                           | CREDENTIALS_IS_NOT_PRESENT                                                                                                                                       |
| E4016           | Transaction failed due to currency not supported                                                                                                                                                                                                 | Country/ Currency not supported                                                      | Country__Currency_Not_Supported                                                                                                                                  |
| E1629           | Transaction declined due to technical failure at bank end                                                                                                                                                                                        | Contact Card Issuer                                                                  | BANK_TECHNICAL_FAILURE                                                                                                                                           |
| E4015           | COMPLIANCE ERROR CODE FOR ISSUER BD                                                                                                                                                                                                              | COMPLIANCE ERROR CODE FOR ISSUER BD                                                  | COMPLIANCE_ERROR_CODE_FOR_ISSUER_BD                                                                                                                              |
| E9232           | Compliance error code for issuer                                                                                                                                                                                                                 | Compliance error code for issuer                                                     | COMPLIANCE_ERROR_CODE_FOR_ISSUER                                                                                                                                 |
| E4014           | COMPLIANCE ERROR CODE FOR ACQUIRER                                                                                                                                                                                                               | COMPLIANCE ERROR CODE FOR ACQUIRER                                                   | COMPLIANCE_ERROR_CODE_FOR_ACQUIRER                                                                                                                               |
| E9216           | Completed Partially                                                                                                                                                                                                                              | Completed Partially                                                                  | COMPLETED_PARTIALLY                                                                                                                                              |
| E1902           | VPA is blank.Either validations have failed or merchant has not passed VPA                                                                                                                                                                       | COLLECT_EMPTY_VPA                                                                    | COLLECT_EMPTY_VPA                                                                                                                                                |
| E4149           | Transaction request declined as merchant is blocked by the customer                                                                                                                                                                              | COLLECT REQUEST IS DECLINED AS REQUESTOR IS BLOCKED BY CUSTOMER                      | COLLECT_REQUEST_IS_DECLINED_AS_REQUESTOR_IS_BLOCKED_BY_CUSTOMER                                                                                                  |
| E4218           | Transaction failed due to collect request expired                                                                                                                                                                                                | COLLECT EXPIRED                                                                      | COLLECT_EXPIRED                                                                                                                                                  |
| E4511           | Transaction declined due to collect by date less that current date                                                                                                                                                                               | Collect By date should be greater than or equal to Current date                      | Collect_By_Date_Should_Be_Greater_Than_Or_Equal_To_Current_Date                                                                                                  |
| E4174           | CM URL IS NOT FOUND                                                                                                                                                                                                                              | CM URL IS NOT FOUND                                                                  | CM_URL_IS_NOT_FOUND                                                                                                                                              |
| E4172           | CM REQUEST TIMEOUT                                                                                                                                                                                                                               | CM REQUEST TIMEOUT                                                                   | CM_REQUEST_TIMEOUT                                                                                                                                               |
| E4171           | CM REQUEST IS DECLINED                                                                                                                                                                                                                           | CM REQUEST IS DECLINED                                                               | CM_REQUEST_IS_DECLINED                                                                                                                                           |
| E4173           | CM REQUEST ACKNOWLEDGEMENT IS NOT RECEIVED                                                                                                                                                                                                       | CM REQUEST ACKNOWLEDGEMENT IS NOT RECEIVED                                           | CM_REQUEST_ACKNOWLEDGEMENT_IS_NOT_RECEIVED                                                                                                                       |
| E717            | Transaction declined as bank reported account to be closed                                                                                                                                                                                       | Closed account                                                                       | INVALID_ACCOUNT_NUMBER                                                                                                                                           |
| E213            | Card authentication failure                                                                                                                                                                                                                      | CHECKSUM_FAILURE                                                                     | CHECKSUM_FAILURE                                                                                                                                                 |
| E4164           | CHECKSUM FAILED                                                                                                                                                                                                                                  | CHECKSUM FAILED                                                                      | CHECKSUM_FAILED                                                                                                                                                  |
| E601            | Challan Generation Failed                                                                                                                                                                                                                        | CHALLAN_PAYMENT * TRANSACTION_FAILED                                                 | CHALLAN_PAYMENT_TRANSACTION_FAILED                                                                                                                               |
| E4023           | CERTIFICATE NOT FOUND                                                                                                                                                                                                                            | CERTIFICATE NOT FOUND                                                                | CERTIFICATE_NOT_FOUND                                                                                                                                            |
| E802            | Issuing Bank was temporarily not available so set as bounced.                                                                                                                                                                                    | CC_DC_ISSUING_BANK_DOWN                                                              | CC_DC_ISSUING_BANK_DOWN                                                                                                                                          |
| E1619           | Category or ibibo code not recieved                                                                                                                                                                                                              | CATEGORY_IBIBO_NOT_RCVD_S2SFLOW                                                      | CATEGORY_IBIBO_NOT_RCVD_S2SFLOW                                                                                                                                  |
| E9249           | Cash back exceeds daily limit                                                                                                                                                                                                                    | Cash back exceeds daily limit                                                        | CASH_BACK_EXCEEDS_DAILY_LIMIT                                                                                                                                    |
| E9238           | Card Re-use Limit Exceeded                                                                                                                                                                                                                       | Card Re-use Limit Exceeded                                                           | CARD_REUSE_LIMIT_EXCEEDED                                                                                                                                        |
| E9247           | Card Not Supported                                                                                                                                                                                                                               | Card Not Supported                                                                   | CARD_NOT_SUPPORTED                                                                                                                                               |
| E9219           | Card Acceptor Call Acquirer Security                                                                                                                                                                                                             | Card Acceptor Call Acquirer Security                                                 | CARD_ACCEPTOR_CALL_ACQUIRER_SECURITY                                                                                                                             |
| E4519           | Refund failed due to insufficient amount                                                                                                                                                                                                         | Cannot verify PIN                                                                    | Insufficient_Amount                                                                                                                                              |
| E4930           | Refund cannot be processed                                                                                                                                                                                                                       | Cannot process Refund                                                                | Cannot_Process_Refund                                                                                                                                            |
| E1605           | Transaction failed due to customer pressing cancel button.                                                                                                                                                                                       | CANCEL_BUTTON_PRESSED_BY_USER                                                        | CANCEL_BUTTON_PRESSED_BY_USER                                                                                                                                    |
| E9248           | Transaction is decline by issuing bank                                                                                                                                                                                                           | CAF status = 0 or 9                                                                  | CAF_STATUS                                                                                                                                                       |
| E1635           | Broker failure received from bank                                                                                                                                                                                                                | BROKER_FAILURE                                                                       | BROKER_FAILURE                                                                                                                                                   |
| E201            | The transaction failed due to invalid or absent card number.                                                                                                                                                                                     | BRAND_INVALID                                                                        | BRAND_INVALID                                                                                                                                                    |
| E1210           | Credit card used in Debit Card PG.                                                                                                                                                                                                               | BLOCK_CREDIT_CARDS                                                                   | BLOCK_CREDIT_CARDS                                                                                                                                               |
| E4089           | BLOCKFUND=Y IS ALLOWED FOR CREATE/UPDATE AND BLOCKFUND=N IS ALLOWED FOR REVOKE                                                                                                                                                                   | BLOCKFUND=Y IS ALLOWED FOR CREATE/UPDATE AND BLOCKFUND=N IS ALLO                     | BLOCKFUND_Y_IS_ALLOWED_FOR_CREATE_UPDATE_AND_BLOCKFUND_N_IS_ALLOWED_FOR_REVOKE                                                                                   |
| E4088           | BLOCKFUND IS ALLOWED ONLY IF THE PURPOSE=01                                                                                                                                                                                                      | BLOCKFUND IS ALLOWED ONLY IF THE PURPOSE=01                                          | BLOCKFUND_IS_ALLOWED_ONLY_IF_THE_PURPOSE_01                                                                                                                      |
| E1660           | MCP Lookup api failed after sending S2S response                                                                                                                                                                                                 | BLAZE_MCP_LOOKUP_ERROR                                                               | BLAZE_MCP_LOOKUP_ERROR                                                                                                                                           |
| E1659           | Error while connecting with blaze net encryption utility                                                                                                                                                                                         | BLAZE_ENCRYPTION_ERROR                                                               | BLAZE_ENCRYPTION_ERROR                                                                                                                                           |
| E4935           | Cryptogram missing                                                                                                                                                                                                                               | Blank or null card token crypto                                                      | CRYPTOGRAM_MISSING                                                                                                                                               |
| E4934           | Invalid BIN                                                                                                                                                                                                                                      | Bin Not Found                                                                        | INVALID_BIN                                                                                                                                                      |
| E4262           | BENIFICIARY BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK                                                                                                                                                                                         | BENIFICIARY BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK                             | BENIFICIARY_BANK_VERSION_TAGS_SENT_NOT_SUPPORTED_BY_BANK                                                                                                         |
| E4260           | BENIFICIARY BANK,REQUEST & RESPONSE HEADER VERSION MISMATCH                                                                                                                                                                                      | BENIFICIARY BANK,REQUEST & RESPONSE HEADER VERSION MISMATCH                          | BENIFICIARY_BANK_REQUEST_RESPONSE_HEADER_VERSION_MISMATCH                                                                                                        |
| E4261           | BENIFICIARY BANK,HEADER OR URL VERSION MISMATCHED                                                                                                                                                                                                | BENIFICIARY BANK,HEADER OR URL VERSION MISMATCHED                                    | BENIFICIARY_BANK_HEADER_OR_URL_VERSION_MISMATCHED                                                                                                                |
| E4097           | BENIFICIARY BANK DOES NOT SUPPORTS VERSION MANDATE 2.1                                                                                                                                                                                           | BENIFICIARY BANK DOES NOT SUPPORTS VERSION MANDATE 2.1                               | BENIFICIARY_BANK_DOES_NOT_SUPPORTS_VERSION_MANDATE_2_1                                                                                                           |
| E4358           | Transaction failed due to acquirers bank CBS offline                                                                                                                                                                                             | BENEFICIARY CBS OFFLINE                                                              | BENEFICIARY_CBS_OFFLINE                                                                                                                                          |
| E4291           | Mandate not supported by acquirer's bank                                                                                                                                                                                                         | BENEFICIARY BANK NOT REGISTERED (MANDATE)                                            | BENEFICIARY_BANK_NOT_REGISTERED_MANDATE                                                                                                                          |
| E4364           | Transaction declined due to acquirer's account blocked or frozen                                                                                                                                                                                 | BENEFICIARY ACCOUNT BLOCKED/FROZEN                                                   | BENEFICIARY_ACCOUNT_BLOCKED_FROZEN                                                                                                                               |
| E4027           | BANKS HSM IS DOWN(REMITTER)                                                                                                                                                                                                                      | BANKS HSM IS DOWN(REMITTER)                                                          | BANKS_HSM_IS_DOWN_REMITTER                                                                                                                                       |
| E4384           | BANKS AS BENEFICIARY NOT LIVE ON PARTICULAR TXN TYPE                                                                                                                                                                                             | BANKS AS BENEFICIARY NOT LIVE ON PARTICULAR TXN TYPE                                 | BANKS_AS_BENEFICIARY_NOT_LIVE_ON_PARTICULAR_TXN_TYPE                                                                                                             |
| E4039           | BANK/PSP IS NOT SUPPORTING VERSION 2                                                                                                                                                                                                             | BANK/PSP IS NOT SUPPORTING VERSION 2                                                 | BANK_PSP_IS_NOT_SUPPORTING_VERSION_2                                                                                                                             |
| E4281           | BANK TD RESPMANDATE NEGATIVE ACK SENT FROM UPI TO REMITTER BANK                                                                                                                                                                                  | BANK TD RESPMANDATE NEGATIVE ACK SENT FROM UPI TO REMITTER BANK                      | BANK_TD_RESPMANDATE_NEGATIVE_ACK_SENT_FROM_UPI_TO_REMITTER_BANK                                                                                                  |
| E9251           | Bank Settlement Limit Exceeded                                                                                                                                                                                                                   | Bank Settlement Limit Exceeded                                                       | BANK_SETTLEMENT_LIMIT_EXCEEDED                                                                                                                                   |
| E9251           | PAYER PSP THROTTLE DECLINE                                                                                                                                                                                                                       | ADDRESS_RESOLUTION_IS_FAILED                                                         |                                                                                                                                                                  |
| E9252           | PSP REQUEST META ACKNOWLEDGEMENT NOT RECEIVED                                                                                                                                                                                                    | ADDRESS_RESOLUTION_IS_FAILED                                                         |                                                                                                                                                                  |
| E1607           | Transaction failed due to user pressing back button.                                                                                                                                                                                             | BACK_BUTTON_PRESSED                                                                  | BACK_BUTTON_PRESSED                                                                                                                                              |
| E1703           | Auth Data mismatch                                                                                                                                                                                                                               | AUTH_DATA_MISMATCH                                                                   | AUTH_DATA_MISMATCH                                                                                                                                               |
| E1001           | Bank network is unavailable at the moment.                                                                                                                                                                                                       | AUTHENTICATION_SERVICE_UNAVAILABLE_ASU                                               | AUTHENTICATION_SERVICE_UNAVAILABLE_ASU                                                                                                                           |
| E334            | Authentication service not available                                                                                                                                                                                                             | AUTHENTICATION_SERVICE_UNAVAILABLE                                                   | AUTHENTICATION_SERVICE_UNAVAILABLE                                                                                                                               |
| E1003           | Card not enabled for Ecomm transactions, either the card is newly issued or has not been used for any online transaction during last 12 months                                                                                                   | AUTHENTICATION_NOT_ATTEMPTED                                                         | AUTHENTICATION_NOT_ATTEMPTED                                                                                                                                     |
| E914            | Transaction failed by Acquirer due to invalid request                                                                                                                                                                                            | AUTHENTICATION_INVALID_REQUEST_ERROR                                                 | AUTHENTICATION_INVALID_REQUEST_ERROR                                                                                                                             |
| E1910           | Authentication failed or invalid PaRes received                                                                                                                                                                                                  | AUTHENTICATION_INVALID_PARES                                                         | AUTHENTICATION_INVALID_PARES                                                                                                                                     |
| E916            | Transaction failed due to invalid merchant config at Acquirer                                                                                                                                                                                    | AUTHENTICATION_INVALID_MERCHANT_CONFIG                                               | AUTHENTICATION_INVALID_MERCHANT_CONFIG                                                                                                                           |
| E915            | Transaction failed by Acquirer due to invalid request data                                                                                                                                                                                       | AUTHENTICATION_INVALID_DATA_ERROR                                                    | AUTHENTICATION_INVALID_DATA_ERROR                                                                                                                                |
| E917            | Transaction failed due to card authentication failure                                                                                                                                                                                            | AUTHENTICATION_FAILURE                                                               | AUTHENTICATION_FAILURE                                                                                                                                           |
| E232            | Payer could not be authenticated                                                                                                                                                                                                                 | AUTHENTICATION_ATTEMPTS                                                              | AUTHENTICATION_ATTEMPTS                                                                                                                                          |
| E1002           | Authentication was attempted but was not available at banks end                                                                                                                                                                                  | AUTHENTICATION_ATTEMPTED                                                             | AUTHENTICATION_ATTEMPTED                                                                                                                                         |
| E600            | Bank denied transaction on the card.                                                                                                                                                                                                             | Authentication declined by issuer                                                    | PAYU_API_ERROR                                                                                                                                                   |
| E1602           | Transaction failed. Page expired due to no user input.                                                                                                                                                                                           | ATM_PIN_PAGE_EXPIRED                                                                 | OTP_PAGE_EXPIRED                                                                                                                                                 |
| E9233           | ARQC validation failed by Issuer                                                                                                                                                                                                                 | ARQC validation failed by Issuer                                                     | ARQC_VALIDATION_FAILED_BY_ISSUER                                                                                                                                 |
| E9203           | Approved VIP (not used)                                                                                                                                                                                                                          | Approved VIP (not used)                                                              | APPROVED_VIP                                                                                                                                                     |
| E9204           | Approved Update Track 3 (not used)                                                                                                                                                                                                               | Approved Update Track 3 (not used)                                                   | APPROVED_TRACK                                                                                                                                                   |
| E9222           | Approved (ANZ only)                                                                                                                                                                                                                              | Approved (ANZ only)                                                                  | APPROVED_ANZ_ONLY                                                                                                                                                |
| E220            | Amount or transaction doesnt match                                                                                                                                                                                                               | AMOUNT_TRANSACTION_MISMATCH                                                          | AMOUNT_TRANSACTION_MISMATCH                                                                                                                                      |
| E4092           | AMOUNT RULE SHOULD BE ALWAYS MAX IF PURPOSE=01                                                                                                                                                                                                   | AMOUNT RULE SHOULD BE ALWAYS MAX IF PURPOSE=01                                       | AMOUNT_RULE_SHOULD_BE_ALWAYS_MAX_IF_PURPOSE_01                                                                                                                   |
| E4161           | AMOUNT OR CURRENCY MISMATCH                                                                                                                                                                                                                      | AMOUNT OR CURRENCY MISMATCH                                                          | AMOUNT_OR_CURRENCY_MISMATCH                                                                                                                                      |
| E4151           | Transaction failed due to amount limit on merchant exceeded                                                                                                                                                                                      | AMOUNT CAP IS EXCEEDED                                                               | AMOUNT_CAP_IS_EXCEEDED                                                                                                                                           |
| EA08            | Alt ID Provisioning Failed                                                                                                                                                                                                                       | Alt ID Provisioning Failed due to incorrect Card Details                             | ALT_ID_PROV                                                                                                                                                      |
| E9217           | Allowable PIN Tries Exceeded                                                                                                                                                                                                                     | Allowable PIN Tries Exceeded                                                         | ALLOWABLE_PIN_TRIES_EXCEEDED                                                                                                                                     |
| E708            | Card authentication failed as user exceeded maximum number of permitted retries for PIN.                                                                                                                                                         | Allowable number of PIN tries exceeded                                               | PIN_RETRIES_EXCEEDED                                                                                                                                             |
| E4037           | Transaction failed due to funds blocked for mandate in customer's account                                                                                                                                                                        | ADEQUATE FUNDS NOT AVAILABLE IN THE ACCOUNT BECAUSE FUNDS HAVE B                     | ADEQUATE_FUNDS_NOT_AVAILABLE_IN_THE_ACCOUNT_BECAUSE_FUNDS_HAVE_BEEN_BD_BLOCKED_FOR_MANDATE                                                                       |
| E304            | The address needs to match with the records of card issuing bank                                                                                                                                                                                 | ADDRESS_INVALID                                                                      | ADDRESS_INVALID                                                                                                                                                  |
| E4013           | Transaction failed due to beneficiary timeout                                                                                                                                                                                                    | ACQUIRER/BENEFICIARY UNAVAILABLE(TIMEOUT)                                            | ACQUIRER_BENEFICIARY_UNAVAILABLE_TIMEOUT                                                                                                                         |
| E4232           | ACCTYPE IS NOT SUPPORTED (OD)                                                                                                                                                                                                                    | ACCTYPE IS NOT SUPPORTED (OD)                                                        | ACCTYPE_IS_NOT_SUPPORTED_OD                                                                                                                                      |
| E4340           | Transaction failed due to account details not found at customer's bank                                                                                                                                                                           | ACCOUNT DOES NOT EXIST (REMITTER)                                                    | ACCOUNT_DOES_NOT_EXIST_REMITTER                                                                                                                                  |
| E4341           | Transaction failed due to account details not found at acquirer's bank                                                                                                                                                                           | ACCOUNT DOES NOT EXIST (BENEFICIARY)                                                 | ACCOUNT_DOES_NOT_EXIST_BENEFICIARY                                                                                                                               |
| E324            | Transaction was declined by the issuing bank due to suspected fraudulent activities                                                                                                                                                              | Suspected Fraud, Retain Card                                                         | CARD_FRAUD_SUSPECTED                                                                                                                                             |
| E325            | Transaction declined due to card not enabled for online transactions or user / Bank Defined Restrictions                                                                                                                                         | Restricted Card, Retain Card                                                         | RESTRICTED_CARD                                                                                                                                                  |
| E313            | Card authentication failed at the bank due to invalid CVV (or CVC or Card Security Code)                                                                                                                                                         | Negative online CAM, dCVV, iCVV, CVV, or CAVV results or Offlin                      | CVC_FAILURE                                                                                                                                                      |
| E1652           | Card blocked                                                                                                                                                                                                                                     | nan                                                                                  | CARD_BLOCKED                                                                                                                                                     |
| E502            | Transaction cancelled by customer                                                                                                                                                                                                                | nan                                                                                  | TRANSACTION_ABORTED                                                                                                                                              |
| E228            | Transaction is Deferred                                                                                                                                                                                                                          | nan                                                                                  | TRANSACTION_DEFERRED                                                                                                                                             |
| E501            | Bank was unable to authenticate.                                                                                                                                                                                                                 | nan                                                                                  | DEFAULT_ERROR                                                                                                                                                    |
| E905            | Transaction declined                                                                                                                                                                                                                             | nan                                                                                  | USER_DECLINED                                                                                                                                                    |
| E314            | The address needs to match with the records of card issuing bank                                                                                                                                                                                 | nan                                                                                  | ADDRESS_FAILURE                                                                                                                                                  |
| E216            | Submitting multiple transactions in a single file is an efficient way to upload credit card and electronic check transaction data from enterprise applications or other file-based systems. Error occurred during batch processing of the cards. | nan                                                                                  | BATCH_ERROR                                                                                                                                                      |
| E316            | Bank failed to authenticate the customer due to 3D Secure Authentication decline                                                                                                                                                                 | nan                                                                                  | SECURE_3D_NOT_ENROLLED                                                                                                                                           |
| E1636           | Transaction time out                                                                                                                                                                                                                             | nan                                                                                  | TRANSACTION_TIMEOUT                                                                                                                                              |
| E1302           | Bank failed to authenticate the customer due to 3D Secure Enrollment decline                                                                                                                                                                     | nan                                                                                  | NOT_ENROLLED_FAILURE                                                                                                                                             |
| E202            | Card authentication failure                                                                                                                                                                                                                      | nan                                                                                  | TRANSACTION_INVALID                                                                                                                                              |

## Other Error Codes from PayU

| PayU Error Code | error_message / message                                                                                                                     | error_description                           |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| EX000           |  nan                                                                                                                                        | GRAND_TOTAL                                 |
| EX001           | No MySQL DSN Supplied                                                                                                                       | MYSQL_DSN_ERROR                             |
| EX002           | Default db not mentioned                                                                                                                    | MYSQL_DEFAULT_DB_UKNOWN                     |
| EX003           | MySQL DSN not configured for ?                                                                                                              | MYSQL_DSN_NOT_CONFIGURED                    |
| EX004           | MySQL DSN not configured for ?                                                                                                              | MYSQL_DSNKEY_NOT_CONFIGURED                 |
| EX005           | Data is empty                                                                                                                               | MYSQL_DATA_EMPTY                            |
| EX006           | where clause is empty                                                                                                                       | MYSQL_WHERE_CLAUSE_EMPTY                    |
| EX007           | Table name is empty                                                                                                                         | MYSQL_TABLENAME_EMPTY                       |
| EX008           | Insufficient dataTypes given.                                                                                                               | MYSQL_DATATYPE_INSUFFICIENT                 |
| EX009           | DataTypes provided but whereParamTypes not provided                                                                                         | MYSQL_WHEREPARAMTYPE_EMPTY                  |
| EX010           | Insufficent whereParamTypes provided                                                                                                        | MYSQL_WHEREPARAMTYPE_INSUFFICIENT           |
| EX011           | CSRF happened                                                                                                                               | CSRF_OCCURRED                               |
| EX012           | Key is Null                                                                                                                                 | NULL_KEY                                    |
| EX013           | Insufficient Input                                                                                                                          | INSUFFICIENT_INPUT                          |
| EX014           | Merchant Param: Key not supplied                                                                                                            | MERCHANT_PARAM_KEY_EMPTY                    |
| EX015           | Merchant payment type insufficient parameters                                                                                               | MERCHANT_PAYMENT_TYPE_INSUFFICIENT          |
| EX016           | Merchant gateway insufficient parameters                                                                                                    | MERCHANT_GATEWAY_INSUFFICIENT_PARAMS        |
| EX017           | Payment gateway id not assigned to merchant payment type                                                                                    | PG_UNASSIGNED_TO_MERCHANT_PAYMENT_TYPE      |
| EX018           | Invalid Payment Gateway Identifier                                                                                                          | INVALID_PAYMENTGATEWAY_INDENTIFIER          |
| EX019           | Unable to obtain lock for transaction                                                                                                       | UNABLE_TO_LOCK                              |
| EX020           | Inconsistent Transaction Status in database                                                                                                 | INCONSISTENCY_IN_TRANSACTION_STATUS         |
| EX021           | The risk_category for this merchant hasn                                                                                                    | RISK_CATEGORY_MISSING                       |
| EX022           | PayuId not attached to Transaction Class ?                                                                                                  | PAYUID_MISSING                              |
| EX023           | Verifier hash mismatch                                                                                                                      | VERIFIER_MISMATCH                           |
| EX024           | Empty lockid in transaction::unlock                                                                                                         | LOCKID_EMPTY                                |
| EX025           | Merchant not found                                                                                                                          | MERCHANT_NOT_FOUND                          |
| EX026           | Transaction could not be reinitiated due to empty base transaction or invalid status                                                        | TRANSACTION_REINITIATION_PROBLEM            |
| EX027           | Empty previous transaction id                                                                                                               | TRANSACTIONID_EMPTY                         |
| EX028           | Invalid Attempt                                                                                                                             | INVALID_ATTEMPT                             |
| EX029           | Invalid User Identifier                                                                                                                     | INVALID_USER_IDENTIFIER                     |
| EX030           | Invalid Vendor Identifier                                                                                                                   | INVALID_VENDOR_IDENTIFIER                   |
| EX031           | Cancel Error: Invalid File or no data                                                                                                       | CANCEL_ERROR_INVALID_FILE                   |
| EX032           | Cancel Error: Mandatory column missing. Mandatory columns are: \<b> ? \</b>                                                                 | CANCEL_ERROR_MANDATORY_COLUMN               |
| EX033           | Refund Error: Invalid File or no data ?                                                                                                     | REFUND_ERROR_INVALID_FILE                   |
| EX034           | Refund Error: Mandatory column missing. Mandatory columns are: \<b> ? \</b>                                                                 | REFUND_ERROR_MANDATORY_COLUMN               |
| EX035           | Capture Error: Invalid File or no data                                                                                                      | CAPTURE_ERROR_INVALID_FILE                  |
| EX036           | Captured Error: Mandatory column missing. Mandatory columns are: \<b> ? \</b>                                                               | CAPTURE_ERROR_MANDATORY_COLUMN              |
| EX037           | Reconciliation Error: Invalid File or no data                                                                                               | RECONCILIATION_ERROR_INVALID_FILE           |
| EX038           | Reconciliation Error: Mandatory column missing. Mandatory columns are: \<b> ? \</b>                                                         | RECONCILIATION_ERROR_MANDATORY_COLUMN       |
| EX039           | Recon: Transaction not set                                                                                                                  | RECON_TRANSACTION_UNSET                     |
| EX040           | ?                                                                                                                                           | NO_PRIVILEGE                                |
| EX041           | The requested file does not exist or you do not have priviledge to access it                                                                | FILE_DO_NOT_EXIST_OR_NO_PRIVILEGE           |
| EX042           | Invalid Invoice ID                                                                                                                          | INVOICE_INVALID                             |
| EX043           | Problem reading data from ? : ?                                                                                                             | PROBLEM_READING_DATA_SENTROPI_URL           |
| EX044           | pExcelReader: Invalid type ?                                                                                                                | PEXCELREADER_INVALID_TYPE                   |
| EX045           | pExcelReader: File ? not readable                                                                                                           | PEXCELREADER_FILE_NOT_READABLE              |
| EX046           | XLSXReader : File not readable Filepath : ( ? ) Error : ( ? )                                                                               | XLSXREADER_FILE_NOT_READABLE                |
| EX047           | ODSReader :  File not readable Filepath : ( ? ) Error : ( ? )                                                                               | ODSREADER_FILE_NOT_READABLE                 |
| EX048           | CSVReader :  File not readable Filepath : ( ? ) Error : ( ? )                                                                               | CSVREADER_FILE_NOT_READABLE                 |
| EX049           | All edit keys must have an associated value                                                                                                 | EDIT_KEY_UNASSOCIATED_VALUE                 |
| EX050           | No data found for this form. Edit form is unavailable                                                                                       | EDIT_FORM_UNAVAILABLE                       |
| EX051           | All edit keys must be part of edit fields                                                                                                   | EDIT_KEY_PART_OF_EDIT_FIELDS                |
| EX052           | TransactionID not found in Pg Response                                                                                                      | TRANSACTIONID_NOT_FOUND_PG_RESPONSE         |
| EX053           | Invalid Transaction ID in gateway response                                                                                                  | TRANSACTIONID_INVALID_GATEWAY_RESPONSE      |
| EX054           | Base merchant id not posted from the paisa request for payuId ?                                                                             | BASE_MERCHANT_ID_MISSING                    |
| EX055           | Base payu id not posted from the paisa request for payuId ?                                                                                 | BASE_PAYU_ID_MISSING                        |
| EX056           | Invalid Paisa Merchant Id                                                                                                                   | INVALID_PAISA_MERCHANT                      |
| EX057           | Not Implemented                                                                                                                             | NOT_IMPLEMENTED                             |
| EX058           | Object can not be saved to database. Identifiers not set                                                                                    | OBJECT_UNSAVED_IDENTIFIER_UNSET             |
| EX059           | Object can not be saved to database. Table name not mentioned                                                                               | OBJECT_UNSAVED_TABLENAME_MISSING            |
| EX060           | Object can not be saved to database. Identifier value missing                                                                               | OBJECT_UNSAVED_IDENTIFIER_MISSING           |
| EX061           | Protocol Mismatch                                                                                                                           | PROTOCOL_MISSMATCH                          |
| EX062           | Add Payment Call to payu_paisa_addpayment_url failed                                                                                        | PAYU_PAISA_ADDPAYMENT_URL_FAILED            |
| EX063           | Invalid Transaction State: Transaction in IN PROGRESS state in cancel.php                                                                   | INVALID_TRANSACTION_STATE                   |
| EX064           | Missing forward action                                                                                                                      | MISSING_FORWARD_ACTION                      |
| EX065           | Invalid forward - App ? not available                                                                                                       | APPS_APPNAME_UNAVAILABLE                    |
| EX066           | Action must extend PayuAction                                                                                                               | ACTION_MUST_EXTEND_PAYUACTION               |
| EX067           | Unable to reload action: ?                                                                                                                  | UNABLE_TO_RELOAD_ACTION                     |
| EX068           | No fields specified in adminViewer                                                                                                          | MISSING_ADMINVIEWER_FIELDS                  |
| EX069           | The request parameter must be set                                                                                                           | REQUEST_PARAM_UNSET                         |
| EX070           | The ? request parameter must be set                                                                                                         | HTTPREQUEST_PARAM_UNSET                     |
| EX071           | Problem Building WURFL Repository: ?                                                                                                        | WURFL_REPOSITORY_PROBLEM                    |
| EX072           | There is no device with ID [?] in the loaded WURFL Data                                                                                     | DEVICE_MISSING_IN_WURFL_DATA                |
| EX073           | WriteRow failed: Unknown Result                                                                                                             | WRITE_ROW_FAILED                            |
| EX074           | WriteFormattedRow failed: unknown result                                                                                                    | WRITE_FORMATTED_ROW_FAILED                  |
| EX075           | OpenExcel failed: unknown result                                                                                                            | OPENEXCEL_FAILED                            |
| EX076           | SaveFile failed: unknown result                                                                                                             | SAVEFILE_FAILED                             |
| EX077           | Write N Rows failed: unknown result                                                                                                         | WRITE_N_ROW_FAILED                          |
| EX078           | WriteFormattedNRows failed: unknown result                                                                                                  | WRITE_N_FORMATTED_ROW_FAILED                |
| EX079           | Message : ?. Error Code : ?                                                                                                                 | DB_EXCEPTION_ERROR_OTHERS                   |
| EX080           | Could not open remote file: ?                                                                                                               | REMOTE_FILE_OPEN_FAILED                     |
| EX081           | Could not open local file: ?                                                                                                                | LOCAL_FILE_OPEN_FAILED                      |
| EX082           | Could not send data from file: ?                                                                                                            | DATA_SENDIG_FAILED                          |
| EX083           | Parameter Passed : ?                                                                                                                        | BLANK                                       |
| EX084           | Return URI not received                                                                                                                     | URI_NOT_RECEIVED                            |
| EX085           | Verifier payu Id not received                                                                                                               | VERIFIER_PAYUID_NOT_RECEIVED                |
| EX086           | Card bin is not present                                                                                                                     | CARD_BIN_NOT_PRESENT                        |
| EX087           | Transaction failed due to incorrectly calculated \<b>hash\</b> parameter. ?                                                                 | CHECKSUM_FAILED                             |
| EX088           | Merchant registration limit exceeded in 1 hour                                                                                              | MERCHANT_REGISTRATION_LIMIT_EXCEEDED        |
| EX089           | Token mismatch                                                                                                                              | TOKEN_MISMATCH                              |
| EX090           | Payu id or token missing                                                                                                                    | PAYUID_MISSING_TOKEN_MISS                   |
| EX091           | Invalid Request ?                                                                                                                           | INVALID_PAGE_REQUESTED                      |
| EX092           | Upload Error: Invalid File or no data                                                                                                       | UPLOAD_ERROR                                |
| EX093           | Reporting Error: Invalid File or no data                                                                                                    | REPORTING_ERROR_INVALID_FILE                |
| EX094           | Vendor details not saved                                                                                                                    | VENDOR_DETAILS_NOT_SAVED                    |
| EX095           | The value must be an integer (not 0) signifying the number of days ? ?                                                                      | NON_INTEGER_ERROR                           |
| EX096           | Reconciliation Error: Undefined actions requested. Defined actions are : \<b> ? \</b> Change \<b> ? \</b> action(s) to appropriate actions. | RECONCILIATION_ERROR_UNDEFINED_ACTION       |
| EX097           | Invalid Merchant Identifier                                                                                                                 | INVALID_MERCHANT_IDENTIFIER                 |
| EX098           | Insufficient parameters for pt key addition                                                                                                 | INSUFFICIENT_PARAM_PT_KEY_ADDITION          |
| EX099           | Insufficient parameters for pt key deletion                                                                                                 | INSUFFICIENT_PARAM_PT_KEY_DELETION          |
| EX100           | Insufficient parameters for pt key update                                                                                                   | INSUFFICIENT_PARAM_PT_KEY_UPDATE            |
| EX101           | Remove pg key - Invalid merchant id                                                                                                         | INVALID_MERCHANT_ID                         |
| EX102           | Insufficient Input for pg keys                                                                                                              | INSUFFICIENT_INPUT_FOR_PG_KEYS              |
| EX103           | Mapped status and unmapped status of payu id ? didnt match                                                                                  | MAPPED_UNMAPPED_STATUS                      |
| EX104           | Reporting Error: Mandatory column missing. Mandatory columns are: \<b> ? \</b>                                                              | REPORTING_ERROR_MANDATORY_COL_MISSING       |
| EX105           | Upload Error: Mandatory column missing. Mandatory columns are: \<b> ? \</b>                                                                 | UPLOAD_ERROR_MANDATORY_COL_MISSING          |
| EX106           | Refund Reference Number Upload Error: Invalid File or no data                                                                               | REFUND_UPLOAD_ERROR_INVLALID_FILE           |
| EX107           | Refund Reference Number Upload Error: Mandatory column missing. Mandatory columns are: \<b> ? \</b>                                         | REFUND_UPLOAD_ERROR_MANDATORY_COL_MISS      |
| EX108           | This \<b>txnid\</b> has been used previously or was successfully captured. ?                                                                | DUPLICATE_ORDER_ID                          |
| EX109           | Wallet Mode Override for ?                                                                                                                  | WALLET_MODE_OVERRIDE                        |
| EX110           | Error! File upload for ? ? failed                                                                                                           | FILE_UPLOAD_FAILURE                         |
| EX111           | Incorrect additional charge posted in paisa response for p1 ?                                                                               | INCORRECT_ADDITIONAL_CHARGE                 |
| EX112           | Invalid request for payuid: ? : addedon: ? : updatedon: ? ?                                                                                 | INVALID_REQUEST_FOR_PAYUID                  |
| EX113           | Invalid Transaction                                                                                                                         | ACCESS_TOKEN_MISMATCH                       |
| EX114           | Merchant key missing in Request                                                                                                             | MERCHANT_KEY_MISSING                        |
| EX115           | The \<b>key\</b> ? value which you are using in the transaction request - is currently inactive. ?                                          | PAYMENTFLOW_INACTIVE_MERCHANT               |
| EX116           | Expired transaction.                                                                                                                        | PAYMENTFLOW_EXPIRED_TRANSACTION             |
| EX117           | Invalid amount                                                                                                                              | INVALID_AMOUNT                              |
| EX118           | Invalid Transaction.                                                                                                                        | PAYMENTFLOW_INVALID_TRANSACTION             |
| EX119           | Card details invalid.                                                                                                                       | CARD_DETAILS_INVALID                        |
| EX120           | Invalid additional amount                                                                                                                   | INVALID_ADDITIONAL_AMOUNT                   |
| EX121           | No edit keys specified. Edit form is unavailable.                                                                                           | NO_EDIT_KEY_EDIT_FORM_UNAVAILABLE           |
| EX122           | Error: Invalid File or no data                                                                                                              | ERROR_INVALID_FILE                          |
| EX123           | Mandatory parameter payuId missing.                                                                                                         | MANDATORY_PARAMETER_PAYUID_MISSING          |
| EX124           | One or more mandatory parameters are missing in the transaction request. ?                                                                  | MANDATORY_PARAMETER_TXNID_MISSING           |
| EX125           | Transaction Expired, payuid: ?  base txn Id: ? uniqueness: ? , ?                                                                            | PAYMENT_FLOW_EXCEP_TRANSACTION_EXPIRED      |
| EX126           | Invalid Data                                                                                                                                | PAYMENTFLOW_INVALID_DATA                    |
| EX127           | Invalid check card is credit                                                                                                                | INVALID_CHECK_CARD_IS_CREDIT                |
| EX128           | This Invoice has expired                                                                                                                    | INVOICE_EXPIRED                             |
| EX129           | Invalid set user request                                                                                                                    | INVALID_SET_USER_REQUEST                    |
| EX130           | Error: Mandatory column missing. Mandatory columns are: \<b> ? \</b>                                                                        | ERROR_MANDATORY_FILE_MISSING                |
| EX131           | Switcher Failure - No active gateway set for merchant transaction id: ?.                                                                    | NO_ACTIVE_PG_FOUND                          |
| EX132           | SS-ratio based Switcher failure - No eligible gateway returned for transaction id: ?.                                                       | SS_RATIO_BASED_SWITCHER_FAILURE             |
| EX133           | Invalid discount amount                                                                                                                     | INVALID_DISCOUNT                            |
| EX134           | Recon: All Ibibo Code not set                                                                                                               | RECON_ALL_IBIBO_CODE_UNSET                  |
| EX135           | Number of elements in a row should be equal to column count                                                                                 | MYSQL_ROW_COLUMN_COUNT_MISMATCH             |
| EX136           | Message sending failed. Message Content : ?; Mobile Number : ?; App : ? .  \n Response received : ?                                         | MESSAGE_SENDING_FAILED                      |
| EX137           | Recon: Card bin map not set                                                                                                                 | RECON_CARDBIN_PGS_UNSET                     |
| EX138           | Fatal Error Handler Counter                                                                                                                 | FATAL_ERROR_HANDLER                         |
| EX139           | Recon: Email Template not set                                                                                                               | RECON_EMAIL_TEMPLATE_UNSET                  |
| EX140           | Profiling error. ProfilerName: ?, AppName: ?, Event: ?, Message: ?                                                                          | PROFILING_ERROR                             |
| EX141           | Mandrill ERROR : ?                                                                                                                          | MANDRILL_ERROR                              |
| EX142           | Message : ?. Error Code : ?                                                                                                                 | DB_EXCEPTION_ERROR_MASTER                   |
| EX143           | Message : ?. Error Code : ?                                                                                                                 | DB_EXCEPTION_ERROR_SLAVE                    |
| EX144           | Message : ?. Error Code : ?                                                                                                                 | DB_EXCEPTION_ERROR_CONCURRENCY              |
| EX145           | Redirection loop for key : ?                                                                                                                | EXCEPTION_REDIRECTION                       |
| EX146           | ? table details are missing in lib/utility/RiskConstants.php                                                                                | INVALID_TABLENAME                           |
| EX147           | You seem to be using an incorrect \<b>key\</b> or \<b>salt\</b> value. ?                                                                    | INCORRECT_MERCHANT_KEY                      |
| EX148           | Invalid Request: ? Unable to parse URL.                                                                                                     | INVALID_URL                                 |
| EX149           | Maximum retry attempts for this \<b>txnid\</b> has been exceeded.                                                                           | RETRY_EXHAUSTED                             |
| EX150           | Invalid subvention amount                                                                                                                   | INVALID_SUBVENTION_AMOUNT                   |
| EX151           |                                                                                                                                             | SFTP_CONNECTION_FAILED                      |
| EX151           | Invalid subvention                                                                                                                          | INVALID_SUBVENTION                          |
| EX152           | No form post variables found [S2S Flow]                                                                                                     | NO_FORM_POST_VARS_S2SFLOW                   |
| EX153           | Category or ibibo code not recieved                                                                                                         | CATEGORY_IBIBO_NOT_RCVD_S2SFLOW             |
| EX154           | Payment Method Enforced and wrong method selected                                                                                           | WRONG_PAYMENT_METHOD_SELECTED               |
| EX155           | NB option is down                                                                                                                           | NB_OPTIION_DOWN                             |
| EX156           | Issuing Bank is down                                                                                                                        | ISSUING_BANK_DOWN                           |
| EX157           |  nan                                                                                                                                        | INVALID_CHECK_ALLOWED_BANKS_DC_IN_SI        |
| EX158           | Merchant Integration Exception occurred                                                                                                     | MERCHANT_INTEGRATION_EXCEPTION_CODE         |
| EX159           |  nan                                                                                                                                        | UNABLE_TO_DECRYPT_TRANSACTION               |
| EX160           | Zipped file generation exception occurred                                                                                                   | PASSWORD_PROTECT_FILE_GENERATION_FAILED     |
| EX200           | Something went wrong                                                                                                                        | V2_API_CURL_EXCEPTION                       |
| EX201           | Merchant key used for HMAC auth is different from merchant key in data                                                                      | V2_API_MERCHANT_KEY_MISMATCH                |
| EX210           | This link has expired                                                                                                                       | INTENT_LINK_EXPIRED                         |
| EX211           | Link already used                                                                                                                           | INTENT_LINK_USED                            |
| EX212           |  nan                                                                                                                                        | INVOICE_GMV_LIMIT_REACHED                   |
| EX213           | Duplicate Callback. Please try after sometime                                                                                               | DUPLICATE_CALLBACK                          |
| EX214           | Retry limit exhausted. Please ask your merchant to send you a new link.                                                                     | INTENT_LINK_USE_EXHAUSTED                   |
| EX215           | Invalid response from curl                                                                                                                  | INVALID_CURL_RESPONSE                       |
| EX216           |  nan                                                                                                                                        | REQUEST_LIMIT_REACHED                       |
| EX217           | Invalid First Name                                                                                                                          | INVALID_FIRST_NAME_EXCEPTION                |
| EX218           | Invalid Last Name                                                                                                                           | INVALID_LAST_NAME_EXCEPTION                 |
| EX219           | Invalid Email                                                                                                                               | INVALID_EMAIL_EXCEPTION                     |
| EX220           | Invalid phone number                                                                                                                        | INVALID_PHONE_EXCEPTION                     |
| EX221           | Invalid ZipCode                                                                                                                             | INVALID_ZIPCODE_EXCEPTION                   |
| EX222           | Invalid Product Info                                                                                                                        | INVALID_PRODUCT_INFO_EXCEPTION              |
| EX223           | Incomplete Onboarding                                                                                                                       | INCOMPLETE_ONBOARDING                       |
| EX224           | Transactions initiation not allowed on aggregator-child merchant.                                                                           | AGGREGATOR_CHILD_MERCHANT_KEY               |
| EX225           |  nan                                                                                                                                        | INVALID_EXPIRY_TIME                         |
| EX226           |                                                                                                                                             | PIH_ERROR                                   |
| EX227           | This currency is not supported on your account. Please reach out to your KAM for activation                                                 | INACTIVE_CURRENCY_FOR_SINGLE_MID            |
| EX300           |  nan                                                                                                                                        | MISMATCH_CART_AMOUNT_AND_TRANSACTION_AMOUNT |
| EX301           |  nan                                                                                                                                        | INCOMPLETE_SKU_DETAILS                      |
| EX302           |  nan                                                                                                                                        | MISMATCH_CART_ITEMS_AND_SKU_QUANTITY_SUM    |
| EX303           |  nan                                                                                                                                        | MISMATCH_CART_AMOUNT_AND_PER_SKU_SUM        |
| EX304           |  nan                                                                                                                                        | MULTIPLE_SAME_SKU_ID_IN_SINGLE_CART         |
| EX305           | Invalid additional percentage                                                                                                               | INVALID_ADDITIONAL_PERCENTAGE               |
| EX306           | Transaction amount convenience fee GST is incorrect, Please try again.                                                                      | INVALID_ADDITIONAL_GST                      |
| EX306           | Invalid Webhook Url                                                                                                                         | INVALID_WEBHOOK_URL                         |
| EX306           | Wrong Api version selected for split txn                                                                                                    | API_VERSION_INCORRECT_SPLIT_TXN             |
| EX307           | Sent convenience fee over transaction amount is high. Please check & try again                                                              | HIGH_CONV_FEE                               |
| EX307           | One or more mandatory parameters are missing in the transaction request for split txn                                                       | MANDATORY_PARAMS_MISSING_SPLIT_TXN          |
| EX401           |  nan                                                                                                                                        | REDIS_DSN_ERROR                             |
| EX401           |  nan                                                                                                                                        | REDIS_DSNKEY_NOT_CONFIGURED                 |
| EX402           | Invalid Partner Param                                                                                                                       | INVALID_PARTNER_PARAM                       |
| EX403           | Invalid UDF Param                                                                                                                           | INVALID_UDF_PARAM                           |
| EX404           | Invalid Buyer Type Business                                                                                                                 | INVALID_BUYER_TYPE_BUSINESS                 |
| EX405           | Invalid More Info Param                                                                                                                     | INVALID_MORE_INFO_PARAM                     |
| EX406           | Invalid PAN or DOB Details                                                                                                                  | INVALID_PAN_DOB_DETAILS                     |
| EX407           | Invalid TCS Amount                                                                                                                          | INVALID_TCS_AMOUNT                          |
| EX408           | Insufficient TCS amount passed based on lrs service type                                                                                    | INSUFFICIENT_TCS_AMOUNT                     |
| EX409           | Invalid value for pacb_lrs_declaration_individual                                                                                           | INVALID_PACB_LRS_DECLARATION_INDIVIDUAL     |
| EX410           | Invalid Lrs Service Type                                                                                                                    | INVALID_LRS_SERVICE_TYPE                    |
| EX411           |  nan                                                                                                                                        | INVALID_PRICING_RESPONSE                    |
| EX412           | The IBIBO codes sent in request are wrong or not active for your merchant account.                                                          | INVALID_ENFORCE_PAYMETHOD                   |

## Cards

The following are the errors associated with cards AuthN and AuthZ, along with their reasons and descriptions.

### AuthN Errors

<SearchableTable
  headers={['Errors', 'Error_message/Message', 'Error Description', 'Title' ]}
  rows={[
    ["REDIRECT", '', '', "E231"],
  ["AUCNEGATIVE", "E-Commerce is not enabled for this card", '', "E1625"],
  ["AUCNEGATIVE", "01 | Card authentication failed", '', "E317"],
  ["ACS_REDIRECT", '', '', "E1602"],
  ["AUCNEGATIVE", "22 | UNKNOWN", '', "E500"],
  ["EVPOSITIVE", '', '', "E231"],
  ["EVNEGATIVE", "ERROR | Error - General system failure", '', "E309"],
  ["ACS_REDIRECT", '', '', "E501"],
  ["3DS_VERIFICATION_NEGATIVE", "Exceeds ACS maximum challenges", '', "E708"],
  ["AUCNEGATIVE", "87 | UNKNOWN", '', "E500"],
  ["AUCNEGATIVE", "901 | Card authentication failed", '', "E335"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Transaction timed out at ACS—other timeouts", '', "E1633"],
  ["AUCNEGATIVE", "INVALID_REQUEST|", '', "E2100"],
  ["REDIRECT", "Invalid card number (no such number)", '', "E1703"],
  ["3DS_METHOD_NEGATIVE", "INVALID_REQUEST | Invalid credentials.", '', "E501"],
  ["REDIRECT", "?:waiting authentication", '', "E231"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E1602"],
  ["AUCNEGATIVE", '', '', "E231"],
  ["AUCNEGATIVE", "11 | Suspected fraud", '', "E324"],
  ["ALT_ID_PROV_ERROR", "EA09|Invalid merchant ID configuration. Please reachout to PayU support team", '', "EA09"],
  ["3DS_CHALLENGE_NEGATIVE", "914 | Transaction timed out at the ACS", '', "E202"],
  ["REDIRECT", "51 | Insufficient funds/over credit limit / Not sufficient funds", '', "E231"],
  ["EVPOSITIVE", '', '', "E503"],
  ["EVNEGATIVE", '', '', "E214"],
  ["REDIRECT", "UNKNOWN_ERROR", '', "E501"],
  ["AUCINVALID", '', '', "E1601"],
  ["ACS_REDIRECT", "GW00201 | Transaction not found", '', "E1206"],
  ["AUCERROR", "00 | Authentication Request Successful", '', "E214"],
  ["3DS_METHOD_NEGATIVE", "3DS212 |", '', "E1642"],
  ["REDIRECT", "UNKNOWN_ERROR", '', "E502"],
  ["AUCNEGATIVE", "N0 | Unable to authorize", '', "E9240"],
  ["AUCNEGATIVE", "0 | OTP Generated Successfully", '', "451"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Transaction timed out at ACS—other timeouts", '', "E202"],
  ["EVNEGATIVE", "INVALID_REQUEST | Invalid credentials.", '', "E202"],
  ["AUCNEGATIVE", "909 | Security failure", '', "E335"],
  ["3DS_CHALLENGE_POSITIVE", '', '', "E000"],
  ["AUCNEGATIVE", "ACS Technical failure", '', "E500"],
  ["EVERROR", "10024 | Bad Expiry year passed!", '', "E1101"],
  ['', '', '', "E1615"],
  ["Get_cryptogram_failure", "Ibibo Code DC is not currently active on merchant", '', "E4932"],
  ['', '', '', "E308"],
  ["EVERROR", "15001 | Some parameters are missing. Please contact merchant", '', "E330"],
  ["REDIRECT", "Issuer not available", '', "E1703"],
  ["AUCNEGATIVE", "Blc|202 | Blc|FAILURE::AUTHENTICATION_FAILED", '', "E335"],
  ["3DS_CHALLENGE_POSITIVE", "Marking transaction as dropped - CSW", '', "E501"],
  ["3DS_METHOD_POSITIVE", '', '', "E308"],
  ["ACS_REDIRECT", "0 | OTP Generated Successfully", '', "E231"],
  ["ACS_REDIRECT", "K | UNKNOWN", '', "E231"],
  ["AUCNEGATIVE", "901 | INVALID_TRANSACTION_TYPE", '', "E207"],
  ["ACS_REDIRECT", "Validation problem", '', "E1703"],
  ["REDIRECT", "SYSTEM ERROR", '', "E1703"],
  ["AUCNEGATIVE", "{\"status\":401,\"message\":\"Authentication failed\",\"error_type\":\"authentication_error\",\"error_code\":\"GNAUE0003\"}", '', "E500"],
  ["ACS_REDIRECT", "N:-5014:Validation problem", '', "E231"],
  ['', "FILTERED_FOR_MCP", '', "E803"],
  ["3DS_VERIFICATION_ERROR", "CURL_CALL_FAILURE", '', "E214"],
  ["REDIRECT", "ECI 1 and ECI6", '', "E1703"],
  ["REDIRECT", "62 | Restricted card", '', "E231"],
  ["3DS_METHOD_POSITIVE", "Disable pg down time handling on UI so marked as bounced.", '', "E804"],
  ["EVERROR", "50021 | GENERAL ERROR", '', "E205"],
  ['', "N:93:Transaction cannot be completed", '', "E231"],
  ["AUCNEGATIVE", "0 |", '', "E335"],
  ["3DS_METHOD_POSITIVE", "UNKNOWN_ERROR", '', "E503"],
  ["3DS_CHALLENGE_NEGATIVE", "402 | CReq message with this ACS Transaction ID has already been received and processed.", '', "E202"],
  ["3DS_VERIFICATION_NEGATIVE", "Security failure", '', "E324"],
  ["3DS_VERIFICATION_NEGATIVE", "System Error response from ACS", '', "E208"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | CONSUMER_AUTHENTICATION_FAILED", '', "E202"],
  ["AUCNEGATIVE", "5003 | The order already exists in the database.", '', "E207"],
  ["AUCNEGATIVE", "0 |", '', "E1601"],
  ["REDIRECT", "57 | Transaction not permitted to issuer/cardholder", '', "E1206"],
  ["AUCNEGATIVE", "0 | OTP Generated Successfully", '', "07"],
  ["AUCNEGATIVE", "51 | Insufficient funds/over credit limit / Not sufficient funds", '', "E231"],
  ['', "Invalid CardNumber/Token/AltId or ibibo_code", '', "E4510"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E1608"],
  ["ACS_REDIRECT", "DECLINED (Exceeds withdrawal amount limit)", '', "E1703"],
  ["3DS_VERIFICATION_NEGATIVE", "Transaction timed out at the ACS", '', "E231"],
  ['', "PG filtering based on KTB Bin Routing", '', "E803"],
  ["REDIRECT", "Marking transaction as dropped - CS", '', "E231"],
  ["ALT_ID_PROV_ERROR", "EA081|The network token provision request contained data that could not be verified", '', "EA081"],
  ["ACS_REDIRECT", '', '', "E502"],
  ['', "SUCCESS", '', "E000"],
  ["REDIRECT", '', '', "E502"],
  ["AUCNEGATIVE", '', '', "E1601"],
  ['', "Ibibo Code RUPAYCC is not currently active on merchant", '', "E6010"],
  ["REDIRECT", "0 |", '', "E231"],
  ["AUCNEGATIVE", "Message Received Invalid", '', "E500"],
  ['', '', '', "E346"],
  ["AUCNEGATIVE", '', '', "E502"],
  ["AUCNEGATIVE", "Marking transaction as dropped - CS", '', "E231"],
  ["AUCNEGATIVE", "AUTHENTICATION_FAILED|Encountered a Payer Authentication problem. Payer could not be authenticated. | CONSUMER_AUTHENTICATION_FAILED", '', "E1003"],
  ["REDIRECT", "00 | Approved or completed successfully", '', "E000"],
  ["AUCERROR", "12002 | Rupay Redirect Response Timeout", '', "E303"],
  ["ACS_REDIRECT", "Marking transaction as dropped - CSW", '', "E202"],
  ["EVNEGATIVE", "56 | DECLINED (no card)", '', "E205"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication", '', "E1633"],
  ["AUCNEGATIVE", "SECURE_3D_AUTHENTICATION_ERROR", '', "E317"],
  ["3DS_CHALLENGE_NEGATIVE", "PG_FAILED | Authentication Failed", '', "E316"],
  ['', "Ibibo Code DINR is not currently active on merchant", '', "E6010"],
  ["ACS_REDIRECT", '', '', "E308"],
  ["3DS_CHALLENGE_NEGATIVE", "TRANSACTION_INVALID", '', "E231"],
  ["ALT_ID_PROV_ERROR", "EA080|cardType is not supported :: cardType", '', "EA080"],
  ['', "FILTERED_INTERNATIONAL_PGS", '', "E803"],
  ["REDIRECT", "Retry the transaction later", '', "E1703"],
  ["REDIRECT", "User Pressed cancel button", '', "E1703"],
  ["REDIRECT", "61 | Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc", '', "E909"],
  ["EVPOSITIVE", '', '', "E1611"],
  ["AUCNEGATIVE", "0 |", '', "E231"],
  ["EVPOSITIVE", "0 |", '', "E231"],
  ["AUCNEGATIVE", "912 | Transaction not permitted to cardholder", '', "E335"],
  ["3DS_CHALLENGE_NEGATIVE", "TRANSACTION_INVALID", '', "E1206"],
  ["AUCNEGATIVE", "0 | OTP Generated Successfully", '', "E502"],
  ["AUCNEGATIVE", "transactionid", '', "E1302"],
  ["3DS_CHALLENGE_NEGATIVE", "919 | Exceeds ACS maximum challenges", '', "E202"],
  ["EVNEGATIVE", "10024 | MRN passed in request is duplicate", '', "E1101"],
  ["3DS_CHALLENGE_POSITIVE", '', '', "E231"],
  ['', "Check for New information before retry", '', "E1703"],
  ["REDIRECT", '', '', "E501"],
  ["AUCNEGATIVE", "0 | OTP Generated Successfully", '', "96"],
  ["ACS_REDIRECT", "Element missing", '', "E2502"],
  ["REDIRECT", "Unable to authorize", '', "E1703"],
  ['', "NON SUFFICIENT FUNDS", '', "E1703"],
  ["AUCNEGATIVE", "Blc|202 | Blc|Transaction processed for 3D Secure/Bank's Page. Waiting for Verification OTP/Password verification.", '', "E335"],
  ["EVNEGATIVE", "400 | General Error", '', "E500"],
  ['', '', '', "E6008"],
  ["AUCERROR", "AUTHENTICATION_FAILED|UNKNOWN_ERROR", '', "E501"],
  ['', '', '', "E1611"],
  ["EVPOSITIVE", '', '', "E000"],
  ['', "N:ACCU400:User was Inactive", '', "E231"],
  ["3DS_METHOD_ERROR", "Blc| | Blc|", '', "E1645"],
  ["3DS_CHALLENGE_POSITIVE", "UNKNOWN_ERROR", '', "E501"],
  ["ALT_ID_PROV_ERROR", "EA080|400", '', "EA080"],
  ["AUCNEGATIVE", "Transaction timed-out.", '', "E500"],
  ["AUCNEGATIVE", "AUTHENTICATION_FAILED | 150", '', "E309"],
  ["REDIRECT", "N:51:NON SUFFICIENT FUNDS", '', "E231"],
  ['', "Invalid transaction", '', "E1703"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E308"],
  ["3DS_METHOD_POSITIVE", "Marking transaction as dropped - CSW", '', "E501"],
  ["3DS_METHOD_ERROR", '', '', "E1302"],
  ["3DS_CHALLENGE_NEGATIVE", "E317 | Failed Eci Txn Allowed for Authorize", '', "E202"],
  ["ACS_REDIRECT", "GW00462 | Invalid Tranportal Password.", '', "E231"],
  ["3DS_CHALLENGE_NEGATIVE", "914 | Transaction timed out at the ACS", '', "E231"],
  ["ACS_REDIRECT", "TRANSACTION_INVALID", '', "E202"],
  ['', "ECI 7", '', "E1703"],
  ["ALT_ID_PROV_ERROR", "|DpaId on-boarding in progress", '', ''],
  ["REDIRECT", "FRAUD - Card's country blocked", '', "E1703"],
  ["ACS_REDIRECT", "Marking transaction as dropped - CS", '', "E501"],
  ["3DS_VERIFICATION_NEGATIVE", "Card authentication failed", '', "E317"],
  ["REDIRECT", "SUCCESS", '', "E000"],
  ["AUCPOSITIVE", '', '', ''],
  ["REDIRECT", "Invalid transaction", '', "E1703"],
  ["EVPOSITIVE", "Marking transaction as dropped - CS", '', "E231"],
  ["3DS_VERIFICATION_NEGATIVE", "RREQ_NOT_RECEIVED", '', "E199"],
  ["3DS_VERIFICATION_NEGATIVE", "102", '', "E231"],
  ['', '', '', "E1101"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Issuer unable to perform authentication", '', "E202"],
  ['', "There is no eligible pg and retry are not allowed or is disabled.", '', "E803"],
  ["3DS_METHOD_NEGATIVE", '', '', "E316"],
  ["ALT_ID_PROV_ERROR", "EA081|One or more fields in the request are either missing or does not have correct value.", '', "EA081"],
  ["AUCNEGATIVE", "403", '', "E335"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E1601"],
  ['', '', '', "E312"],
  ["REDIRECT", "Transaction not permitted to cardholder", '', "E1703"],
  ["EVPOSITIVE", '', '', "E502"],
  ["REDIRECT", "N0 | Unable to Authorise", '', "E231"],
  ['', "Ibibo Code MAST is not currently active on merchant", '', "E6010"],
  ["AUCNEGATIVE", "GW00201 | Transaction not found", '', "E231"],
  ['', "Transaction not permitted to cardholder", '', "E1703"],
  ["AUCNEGATIVE", "09 | Security failure", '', "E324"],
  ["AUCNEGATIVE", '', '', "E1633"],
  ["3DS_VERIFICATION_NEGATIVE", "UNKNOWN", '', "E500"],
  ["3DS_METHOD_POSITIVE", "Marking transaction as dropped - CSW", '', "E231"],
  ["AUCNEGATIVE", "DO_NOT_PROCEED", '', "E1302"],
  ["AUCNEGATIVE", "912 | INVALID_TRANSACTION_TYPE", '', "E207"],
  ["EVERROR", "50021 | Signature Verification Failed at PG end.", '', "E205"],
  ["EVNEGATIVE", "400 | GENERAL ERROR", '', "E500"],
  ["3DS_METHOD_POSITIVE", "Marking transaction as dropped - CSW", '', "E1206"],
  ['', '', '', "E214"],
  ["REDIRECT", "Issuer authentication failure", '', "E1703"],
  ["REDIRECT", "NON SUFFICIENT FUNDS", '', "E1703"],
  ["EVNEGATIVE", "|", '', "E308"],
  ["3DS_CHALLENGE_NEGATIVE", "101 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|FAILURE::AUTHENTICATION_NOT_SUPPORTED", '', "E204"],
  ["REDIRECT", '', '', "E1602"],
  ["ALT_ID_PROV_ERROR", "EA088|Card can currently not be used with card association for tokenization", '', "EA088"],
  ["EVERROR", '', '', "E214"],
  ["REDIRECT", "51 | Insufficient funds/over credit limit / Not sufficient funds", '', "E706"],
  ["ACS_REDIRECT", '', '', "E000"],
  ["AUCNEGATIVE", "987 | Declined by DS - Transaction is excluded from Attempts Processing", '', "E335"],
  ["3DS_METHOD_NEGATIVE", "CURL_CALL_FAILURE", '', "E501"],
  ["AUCNEGATIVE", "INVALID_TRANSACTION_TYPE", '', "E207"],
  ["ALT_ID_PROV_ERROR", "EA080|Tokenization failed", '', "EA080"],
  ["AUCNEGATIVE", "08 | No Card Record", '', "E4346"],
  ["REDIRECT", "?:waiting authentication", '', "E1206"],
  ["AUCNEGATIVE", "Cardholder Account Number is not in a range belonging to Issuer.", '', "E500"],
  ['', "Retry the transaction later", '', "E1703"],
  ["AUCNEGATIVE", '', '', "E1602"],
  ["REDIRECT", "Application error", '', "E1206"],
  ["AUCNEGATIVE", "0 | OTP Generated Successfully", '', "E1601"],
  ["3DS_METHOD_ERROR", "NOT_ENROLLED_FAILURE", '', "E1302"],
  ['', "Authentication Failed", '', "E1703"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E317"],
  ["EVPOSITIVE", "GW00201 | Transaction not found", '', "E1206"],
  ["AUCNEGATIVE", "SUCCESS", '', "E000"],
  ['', "Mandatory Param Missing for Token txn store_card_token", '', "E4510"],
  ["EVERROR", "15096 | SYSTEM ERROR or PREVIOUSLY AUTHORIZED or PREVIOUSLY DECLINED", '', "E335"],
  ["EVERROR", "410 | Invalid BIN", '', "E337"],
  ["EVPOSITIVE", '', '', "E501"],
  ["ACS_REDIRECT", "0 |", '', "E1206"],
  ["AUCNEGATIVE", "906 | Invalid card number", '', "E335"],
  ['', "Mandatory Param Missing for Token txn ccexpmon", '', "E1101"],
  ['', "PG filtering based on Network Token supported PGs", '', "E803"],
  ["ACS_REDIRECT", "Marking transaction as dropped - CSW", '', "E000"],
  ["AUCNEGATIVE", "5005 | The country of the credit card has been blocked.", '', "E207"],
  ["AUCNEGATIVE", "50716 | Transaction declined. 3D Secure authentication failed.", '', "E207"],
  ['', "ECI 1 and ECI6", '', "E1703"],
  ["AUCNEGATIVE", "402 | DS Response is blank", '', "E207"],
  ["AUCNEGATIVE", "202 | SERVER_FAILED::Please contact customer support quoting the support code.", '', "E1633"],
  ["AUCNEGATIVE", "904 | Exceeds authentication frequency limit", '', "E335"],
  ["AUCNEGATIVE", '', '', "E1608"],
  ["ALT_ID_PROV_ERROR", "EA084|Card can currently not be used with issuer for tokenization", '', "EA084"],
  ["REDIRECT", "3D Secure authentication failed", '', "E1703"],
  ["REDIRECT", "0 | OTP Generated Successfully", '', "E502"],
  ['', '', '', "E1605"],
  ["REDIRECT", '', '', "E000"],
  ["AUCNEGATIVE", "10 | Stolen card", '', "E310"],
  ["AUCNEGATIVE", "AUTHENTICATION_FAILED | 476 | Issuer unable to perform authentication", '', "E303"],
  ['', '', '', "E6009"],
  ["3DS_CHALLENGE_NEGATIVE", "Blc|203 | Blc|response.gatewayRecommendation=DO_NOT_PROCEED", '', "E317"],
  ["ALT_ID_PROV_ERROR", "EA11 | Timeout reached from StoreCard", '', "EA11"],
  ["EVPOSITIVE", '', '', "E802"],
  ['', "Issuer authentication failure", '', "E1703"],
  ["EVNEGATIVE", "REJECT | Declined - One or more fields in the request contains invalid da", '', "E1400"],
  ["3DS_CHALLENGE_NEGATIVE", "908 | No Card record", '', "E202"],
  ['', '', '', "E231"],
  ["3DS_METHOD_ERROR", '', '', "E500"],
  ["ALT_ID_PROV_ERROR", "EA087|Invalid body values", '', "EA087"],
  ["REDIRECT", "Rupay check bin error", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication", '', "E202"],
  ["REDIRECT", "Restricted card", '', "E1703"],
  ["AUCNEGATIVE", "905 | INVALID_TRANSACTION_TYPE", '', "E207"],
  ["REDIRECT", "00 | Authentication Request Successful", '', "E502"],
  ["EVNEGATIVE", "ERROR | UNKNOWN", '', "E500"],
  ["ALT_ID_PROV_ERROR", "EA089|Request not permitted", '', "EA089"],
  ["REDIRECT", "UNKNOWN_ERROR", '', "E231"],
  ["3DS_VERIFICATION_NEGATIVE", "0", '', "E231"],
  ['', "FILTERED_INTERNATIONAL_PGS", '', "E804"],
  ['', "REMOVED_HEADLESS_PGS", '', "E803"],
  ["PG_NOT_ACTIVATED", "No Active PG found for Prepaid Card", '', "E803"],
  ['', '', '', "E6004"],
  ["AUCERROR", "Pg authentication not supported on Only 3DSS Supported PGs", '', "E308"],
  ['', "PG filtering based on Pre Auth Allowed PGs for merchant", '', "E803"],
  ['', "User Pressed cancel button", '', "E1703"],
  ["REDIRECT", "Lost card", '', "E1703"],
  ["AUCNEGATIVE", "00 | Approved or completed successfully", '', "E000"],
  ["REDIRECT", '', '', ''],
  ["ACS_REDIRECT", "0 | OTP Generated Successfully", '', "E1205"],
  ["ALT_ID_PROV_ERROR", "EA080|Technical error. Please try again", '', "EA080"],
  ["3DS_CHALLENGE_ERROR", "UNKNOWN_ERROR", '', "E501"],
  ["EVNEGATIVE", "96 | Issuer System Failure", '', "E500"],
  ["REDIRECT", "ECI 7", '', "E1703"],
  ["AUCNEGATIVE", "905 | INVALID_TRANSACTION_TYPE", '', "E231"],
  ["REDIRECT", "Invalid data was posted to Issuer", '', "E1703"],
  ["REDIRECT", "Do not retry", '', "E1703"],
  ["AUCNEGATIVE", "01 | Card authentication failed", '', "E1633"],
  ["3DS_METHOD_POSITIVE", '', '', "E1602"],
  ["REDIRECT", "User was Inactive", '', "E1703"],
  ["ACS_REDIRECT", "000 | Blc|SUCCESS", '', "E502"],
  ["3DS_VERIFICATION_NEGATIVE", "Exceeds ACS maximum challenges", '', "E1633"],
  ["EVNEGATIVE", "10004 | Unable to reach card information service", '', "E1617"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Transaction Error", '', "E207"],
  ["AUCNEGATIVE", "13 | Cardholder not enrolled in service", '', "E1302"],
  ["3DS_METHOD_POSITIVE", "CURL_CALL_FAILURE", '', "E214"],
  ["EVNEGATIVE", "REJECT | Declined - One or more fields in the request contains invalid da", '', "E2100"],
  ["EVNEGATIVE", "UNKNOWN_ERROR", '', "E1206"],
  ["EVNEGATIVE", "UNKNOWN_ERROR", '', "E231"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|SERVER_FAILED::Please contact customer support quoting the support code.", '', "E204"],
  ["AUCNEGATIVE", "202 | FAILURE::AUTHENTICATION_FAILED", '', "E1633"],
  ["3DS_CHALLENGE_POSITIVE", "Marking transaction as dropped - CSW", '', "E231"],
  ["3DS_VERIFICATION_NEGATIVE", "Invalid transaction", '', "E1633"],
  ["AUCNEGATIVE", "15 | Low confidence", '', "E4001"],
  ["AUCNEGATIVE", "Transaction data not valid", '', "E500"],
  ["AUCNEGATIVE", "00 | Authentication Request Successful", '', "E502"],
  ["AUCNEGATIVE", "5003 | The order already exists in the database.", '', "E231"],
  ["3DS_CHALLENGE_NEGATIVE", "PG_FAILED |", '', "E500"],
  ["AUCNEGATIVE", "305 | Invalid Account Number received in the Message.", '', "E207"],
  ["EVERROR", "50021 | XML Data Error - Invalid Parameter Value - card_exp_date", '', "E205"],
  ["REDIRECT", "0 |", '', "E1206"],
  ["AUCPOSITIVE", "Invalid Otp", '', "E231"],
  ["AUCNEGATIVE", '', '', ''],
  ['', "Ibibo Code BAJAJ is not currently active on merchant", '', "E6010"],
  ["3DS_CHALLENGE_NEGATIVE", '', '', "E317"],
  ["ACS_REDIRECT", "EXPIRED CARD", '', "E1703"],
  ["EVNEGATIVE", "REJECT | UNKNOWN", '', "E500"],
  ["ACS_REDIRECT", '', '', "E231"],
  ["EVNEGATIVE", "412 | Issuer Authentication Server failure", '', "E337"],
  ["ACS_REDIRECT", "Marking transaction as dropped - CS", '', "E231"],
  ["AUCNEGATIVE", "Session timed out", '', "E2503"],
  ["ACS_REDIRECT", "Marking transaction as dropped - CSW", '', "E231"],
  ["3DS_VERIFICATION_NEGATIVE", "102", '', "E1206"],
  ['', "FILTERED_DOMESTIC_PGS", '', "E804"],
  ["3DS_VERIFICATION_NEGATIVE", "No Card Record", '', "E4346"],
  ["EVNEGATIVE", "56 |", '', "E500"],
  ["EVPOSITIVE", "GW00201 | Transaction not found", '', "E231"],
  ['', "Restricted card", '', "E1703"],
  ["EVPOSITIVE", '', '', "E1206"],
  ['', "SUCCESS", '', "E231"],
  ["3DS_METHOD_NEGATIVE", "NOT_ENROLLED_FAILURE", '', "E1302"],
  ['', "PG filtering based on Optional TRID", '', "E803"],
  ["ALT_ID_PROV_ERROR", "EA081|card_not_eligible", '', "EA081"],
  ["ACS_REDIRECT", '', '', "E503"],
  ['', "Ibibo Code AMEX is not currently active on merchant", '', "E6010"],
  ["3DS_VERIFICATION_NEGATIVE", "Transaction not permitted to cardholder", '', "E1642"],
  ["Get_cryptogram_failure", '', '', "E4932"],
  ["EVERROR", "|", '', "E214"],
  ["3DS_CHALLENGE_NEGATIVE", "901 | Card authentication failed", '', "E202"],
  ["AUCNEGATIVE", "5111 | Transaction failed. ECI1 and ECI6 transactions are not supported by merchant.", '', "E207"],
  ["REDIRECT", '', '', "E1206"],
  ["AUCNEGATIVE", "00 | Authentication Request Successful", '', "E500"],
  ["REDIRECT", "N:ACCU400:User was Inactive", '', "E1206"],
  ["AUCNEGATIVE", "UNKNOWN_ERROR", '', "E1608"],
  ['', "PG filtering based on Fixed TID Routing", '', "E803"],
  ["AUCNEGATIVE", "0 | OTP Generated Successfully", '', "E231"],
  ['', '', '', "E4510"],
  ["REDIRECT", "62 | Restricted card", '', "E1626"],
  ["REDIRECT", "05 | Do not honor", '', "E307"],
  ["EVNEGATIVE", "400 |", '', "E4933"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E502"],
  ['', "Invalid card number (no such number)", '', "E1703"],
  ["REDIRECT", "Authentication Failed", '', "E1703"],
  ["AUCERROR", '', '', "E1302"],
  ["AUCNEGATIVE", "202 | Unknown Error. Transaction Failed. Please try again later.", '', "E1633"],
  ["REDIRECT", "INVALID_REQUEST | Invalid credentials.", '', "E202"],
  ["ALT_ID_PROV_ERROR", "EA087|INVALID_VALUE", '', "EA087"],
  ["EVNEGATIVE", "413 |", '', "E500"],
  ["3DS_CHALLENGE_NEGATIVE", "926 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["AUCINVALID", "0 |", '', "E1601"],
  ["REDIRECT", "N:-BEPG-0000017:Issuer authentication failure", '', "E231"],
  ["ACS_REDIRECT", "SUCCESS", '', "E000"],
  ["ALT_ID_PROV_ERROR", "EA085|Issuer did not respond in time. Retry the request.", '', "EA085"],
  ["AUCPOSITIVE", '', '', "E501"],
  ['', "PG filtering based on Direct Auth 3DS2 txn", '', "E803"],
  ["3DS_CHALLENGE_NEGATIVE", "101 | RReq is not available", '', "E202"],
  ["REDIRECT", "87 | No Envelope Inserted", '', "E231"],
  ["EVPOSITIVE", '', '', "E1202"],
  ["REDIRECT", "N:ACCU600:Invalid data was posted to Issuer", '', "E231"],
  ["AUCNEGATIVE", "303 | Access denied, invalid endpoint.", '', "E335"],
  ["ACS_REDIRECT", "0 |", '', "E1205"],
  ["REDIRECT", "N:05:Do not honour", '', "E231"],
  ["AUCNEGATIVE", "Blc|202 | Blc|FAILURE::AUTHENTICATION_REJECTED", '', "E335"],
  ["3DS_METHOD_ERROR", "CURL_CALL_FAILURE", '', "E214"],
  ['', "UNKNOWN_ERROR", '', "E231"],
  ["ACS_REDIRECT", "62 | Restricted card", '', "E1206"],
  ["AUCERROR", "Cannot invoke \"com.payu.cardsservice.cards.dto.response.common.FormPost.getPostUri()\" because the return value of \"com.payu.cardsservice.cards.dto.response.common.Data.getFormPost()\" is null", '', "E207"],
  ["EVNEGATIVE", "GW00201 | Transaction not found", '', "E231"],
  ['', "Validation problem", '', "E1703"],
  ["REDIRECT", "Secure Hash Mismatch", '', "E1703"],
  ['', "PG filtering based on AltId supported PGs", '', "E804"],
  ["AUCNEGATIVE", "5102 | Transaction failed. ECI-7 transactions are not supported by merchant.", '', "E207"],
  ["MER_025|No Transaction exists with given merchant id : MER0000005118097", '', '', "E346"],
  ["AUCNEGATIVE", '', '', "E1206"],
  ["ALT_ID_PROV_ERROR", "EA080|card_market_not_supported", '', "EA080"],
  ["AUCNEGATIVE", "BIN Range inactive", '', "E500"],
  ["AUCINVALID", "00 | Authentication Request Successful", '', "E1601"],
  ['', '', '', "E908"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E501"],
  ["3DS_METHOD_NEGATIVE", "56 |", '', "E500"],
  ["EVNEGATIVE", "ERROR | Error - The request was received but there was a server timeout.", '', "E208"],
  ["ACS_REDIRECT", '', '', "E1611"],
  ["AUCNEGATIVE", "303 | Access denied, invalid endpoint", '', "E335"],
  ["AUCNEGATIVE", "05 | Expired card", '', "E1633"],
  ['', "The order already exists in the database.", '', "E1703"],
  ['', "Secure Hash Mismatch", '', "E1703"],
  ["EVNEGATIVE", "410 |", '', "E500"],
  ["3DS_CHALLENGE_NEGATIVE", "912 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["ACS_REDIRECT", '', '', "E1903"],
  ["AUCNEGATIVE", "06 | Invalid card number", '', "E1633"],
  ["ACS_REDIRECT", "Invalid Otp", '', "E502"],
  ["EVNEGATIVE", "|", '', ''],
  ['', "REMOVED_HEADLESS_3DSS_ELIGIBLE_PGS", '', "E804"],
  ["REDIRECT", "GW00201 | Transaction not found", '', "E231"],
  ["PG_NOT_ACTIVATED", "No Active PG found for Corporate Card", '', "E803"],
  ["AUCNEGATIVE", "05 | Expired card", '', "E311"],
  ["ACS_REDIRECT", "0 |", '', "E231"],
  ['', '', '', "E408"],
  ["AUCNEGATIVE", "AUTHENTICATION_ATTEMPTS", '', "E232"],
  ["ACS_REDIRECT", "Marking transaction as dropped - CS", '', "E1206"],
  ["EVERROR", "15056 | No card so declined", '', "E205"],
  ["EVNEGATIVE", "412 | Transaction got declined at issuer.", '', "E207"],
  ["REDIRECT", "0 | OTP Generated Successfully", '', "E231"],
  ["AUCERROR", "10024 | Unable the process the transaction, Authentication Failed", '', "E303"],
  ["REDIRECT", "Application error", '', "E231"],
  ["EVPOSITIVE", '', '', "E1602"],
  ["3DS_METHOD_ERROR", '', '', "E4506"],
  ["REDIRECT", "Check for New information before retry", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "DO_NOT_PROCEED", '', "E317"],
  ["3DS_METHOD_POSITIVE", "UNKNOWN_ERROR", '', "E501"],
  ['', '', '', "E2101"],
  ['', '', '', "E6006"],
  ["AUCNEGATIVE", "0 | OTP Generated Successfully", '', "452"],
  ["AUCNEGATIVE", "|Decline - Invalid account number", '', "E501"],
  ['', "Mandatory Param Missing for Token txn user_credentials", '', "E4510"],
  ["EVERROR", "50021 | Invalid cvd2 passed!", '', "E205"],
  ["ACS_REDIRECT", "Marking transaction as dropped - CSW", '', "E1206"],
  ["REDIRECT", "GW00201 | Transaction not found", '', "E1206"],
  ["EVPOSITIVE", "0 | OTP Generated Successfully", '', "E231"],
  ["3DS_METHOD_POSITIVE", '', '', "E231"],
  ["3DS_CHALLENGE_NEGATIVE", "901 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["3DS_METHOD_NEGATIVE", "BNF | Bin Not Found", '', "E4934"],
  ["REDIRECT", "General exception", '', "E1703"],
  ["ALT_ID_PROV_ERROR", "EA04|Invalid merchant ID configuration. Please reachout to PayU support team", '', "EA04"],
  ["AUCNEGATIVE", "Transaction ID has already been received and processed.", '', "E500"],
  ["ACS_REDIRECT", "00 | Approved or completed successfully", '', "E000"],
  ['', "?:waiting authentication", '', "E231"],
  ['', "PG filtering based on Card SI PGs", '', "E804"],
  ["3DS_CHALLENGE_NEGATIVE", "914 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["3DS_VERIFICATION_NEGATIVE", "Card authentication failed", '', "E1633"],
  ["ALT_ID_PROV_ERROR", "EA11|Service unavailable. Typically the server not able to serve the request temporarily. Retry after sometime.", '', "EA11"],
  ["REDIRECT", "Unable to verify card enrollment", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_INVALID_REQUEST_ERROR", '', "E914"],
  ["AUCNEGATIVE", "901 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E000"],
  ['', '', '', "E2100"],
  ['', '', '', "E7001"],
  ["REDIRECT", "Suspected Fraud. Do not retry", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "SERVER_ERROR", '', "E208"],
  ["ACS_REDIRECT", '', '', "E1608"],
  ["ACS_REDIRECT", "K | UNKNOWN", '', "E1206"],
  ['', "Unable to get payer authentication", '', "E1703"],
  ["ACS_REDIRECT", "00 | Authentication Request Successful", '', "E502"],
  ["3DS_VERIFICATION_NEGATIVE", "Invalid transaction", '', "E207"],
  ['', '', '', "E6007"],
  ["3DS_METHOD_NEGATIVE", "400 |", '', "E4933"],
  ['', "Ibibo Code BAJAJF is not currently active on merchant", '', "E6010"],
  ["3DS_VERIFICATION_NEGATIVE", "Transaction not permitted to cardholder", '', "E1633"],
  ['', "UNKNOWN_ERROR", '', "E501"],
  ["REDIRECT", "Communication Error", '', "E1703"],
  ["AUCNEGATIVE", "BEPG-0000017 | Issuer authentication failure", '', "E207"],
  ["3DS_METHOD_ERROR", "CURL_CALL_FAILURE", '', "E501"],
  ["3DS_VERIFICATION_NEGATIVE", "E303 | SUCCESS", '', "E303"],
  ["AUCNEGATIVE", "906 | INVALID_TRANSACTION_TYPE", '', "E207"],
  ["ACS_REDIRECT", "000 | Blc|SUCCESS", '', "E1602"],
  ['', "?:waiting authentication", '', "E1206"],
  ["AUCNEGATIVE", "305 | Transaction data not valid", '', "E335"],
  ["3DS_CHALLENGE_NEGATIVE", "901 | Blc|Authentication/ Account Verification Rejected; Issuer is rejecting", '', "E317"],
  ['', "N:05:Do not honour", '', "E231"],
  ['', "PG filtering based on KTB Bin Routing", '', "E804"],
  ["EVPOSITIVE", "Marking transaction as dropped - CS", '', "E1206"],
  ["AUCNEGATIVE", "919 | Exceeds ACS maximum challenges", '', "E335"],
  ["REDIRECT", "0 |", '', "E1205"],
  ["3DS_CHALLENGE_NEGATIVE", "984 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["ACS_REDIRECT", "QR", '', "E507"],
  ["REDIRECT", "N:-BEPG-0000017:Issuer authentication failure", '', "E1206"],
  ["EVPOSITIVE", '', '', "E1205"],
  ["AUCNEGATIVE", "305 | Transaction ID has already been received and processed.", '', "E207"],
  ["REDIRECT", "CA | Acquirer compliance", '', "E1206"],
  ["REDIRECT", "N:ACCU400:User was Inactive", '', "E231"],
  ["AUCNEGATIVE", "Page parsing Failure", '', "E1608"],
  ['', "Rupay transaction error", '', "E1703"],
  ["REDIRECT", "Expired card", '', "E1703"],
  ["AUCNEGATIVE", "BEPG-0000013 | Failure during checkbin process", '', "E207"],
  ["REDIRECT", "Marking transaction as dropped - CS", '', "E1206"],
  ["3DS_METHOD_POSITIVE", "UNKNOWN_ERROR", '', "E1602"],
  ["EVNEGATIVE", "CTO | Network Connect Time Out", '', "E1639"],
  ["AUCNEGATIVE", "905 | Expired card", '', "E335"],
  ["AUCNEGATIVE", "Transaction ID is recognised as a duplicate.", '', "E500"],
  ["ALT_ID_PROV_ERROR", "MOF001|City name is invalid", '', "MOF001"],
  ["ALT_ID_PROV_ERROR", "EA11|internal_api_error", '', "EA11"],
  ["AUCNEGATIVE", "203 | mcc", '', "E207"],
  ['', "Ibibo Code CITD is not currently active on merchant", '', "E6010"],
  ['', "N:-50822:Processing error while provisioning Guest Checkout Token", '', "E231"],
  ["3DS_METHOD_POSITIVE", "Invalid Otp", '', "E231"],
  ['', "SUCCESS", '', "E1206"],
  ["REDIRECT", "N:-50822:Processing error while provisioning Guest Checkout Token", '', "E1206"],
  ["3DS_METHOD_NEGATIVE", "|", '', ''],
  ["3DS_METHOD_NEGATIVE", "Blc|102 | Blc|currency parameter is missing or invalid", '', "E204"],
  ["REDIRECT", '', '', "SSER001"],
  ["AUCNEGATIVE", "914 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["ACS_REDIRECT", "Invalid Otp", '', "E000"],
  ['', "ERROR", '', "E1703"],
  ["AUCNEGATIVE", "Transaction Data Not Valid", '', "E500"],
  ['', '', '', "E1205"],
  ["AUCNEGATIVE", "10024 | This Card type is not allowed !!", '', "E1101"],
  ["AUCNEGATIVE", "54 | Expired card", '', "E311"],
  ['', "N:-BEPG-0000017:Issuer authentication failure", '', "E1206"],
  ["AUCNEGATIVE", '', '', "E503"],
  ["3DS_CHALLENGE_POSITIVE", '', '', ''],
  ["AUCNEGATIVE", "926 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ['', "N:-5014:Validation problem", '', "E231"],
  ["3DS_CHALLENGE_ERROR", "INVALID_REQUEST | Unable to find order null and transaction null for merchant CPM00006", '', "E231"],
  ["EVNEGATIVE", "Invalid association id passed in request", '', "E303"],
  ["ACS_REDIRECT", "62 | Restricted card", '', "E231"],
  ["EVNEGATIVE", "integer overflow", '', "E303"],
  ["AUCNEGATIVE", "Retrieved transaction already used", '', "E500"],
  ["3DS_METHOD_POSITIVE", '', '', "E1205"],
  ["3DS_METHOD_POSITIVE", "UNKNOWN_ERROR", '', "E1601"],
  ["AUCNEGATIVE", "Marking transaction as dropped - CS", '', "E1206"],
  ["3DS_METHOD_NEGATIVE", "CURL_CALL_FAILURE", '', "E231"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E1611"],
  ["AUCNEGATIVE", "5212 | DCC is not configured for store.", '', "E207"],
  ["ACS_REDIRECT", "genericintent", '', "E507"],
  ["AUCNEGATIVE", "408 | pArq Request timed out", '', "E712"],
  ["AUCNEGATIVE", "googlepay", '', "E501"],
  ["AUCNEGATIVE", "87 | Bad Track Data", '', "E303"],
  ["EVERROR", "50021 | Bad AcquiringBank configured for merchant_id(58853232) in pg_instance_id(37887779)!", '', "E205"],
  ['', "PG filtering based on MOTO Txn Enabled Check", '', "E803"],
  ["5006", '', '', "E307"],
  ["AUCNEGATIVE", "201 | A message element required as defined in Table A.1 is missing from the message.", '', "E335"],
  ['', "Mandatory Param Missing for Token txn ccexpyr", '', "E4510"],
  ["EVPOSITIVE", "Marking transaction as dropped - CSW", '', "E1206"],
  ["REDIRECT", "INVALID_REQUEST | Value '401602xxxxxx0643' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E202"],
  ["AUCNEGATIVE", "901 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E1633"],
  ["AUCNEGATIVE", '', '', "E501"],
  ["3DS_METHOD_POSITIVE", "Blc|0 | Blc|SUCCESS", '', "E1206"],
  ['', "FILTERED_FOR_AXIS_WIBMO_ONUS", '', "E803"],
  ["REDIRECT", "DECLINED (exceeds frequency)", '', "E1703"],
  ["ACS_REDIRECT", "CURL_CALL_FAILURE", '', "E214"],
  ["ACS_REDIRECT", '', '', "E4165"],
  ["AUCNEGATIVE", "Transaction ID received is not valid for the receiving component.", '', "E500"],
  ["REDIRECT", "Transactions declined by Issuer based on Risk Score", '', "E1703"],
  ["REDIRECT", "62 | Restricted card", '', "E1206"],
  ['', "Ibibo Code ICICI is not currently active on merchant", '', "E6010"],
  ['', "Mandatory Param Missing trmerchantid", '', "E4510"],
  ["AUCNEGATIVE", "No Error", '', "E1608"],
  ["ACS_REDIRECT", "Invalid Otp", '', "E340"],
  ['', "Lost card", '', "E1703"],
  ["AUCNEGATIVE", "05 | Do not honor", '', "E307"],
  ["REDIRECT", "bhim", '', "E501"],
  ["3DS_CHALLENGE_NEGATIVE", "914 | Blc|Authentication/Account Verification Could Not Be Performed; Technical or other problem, as indicated in ARes or RReq.", '', "E317"],
  ["REDIRECT", "DECLINED (Exceeds withdrawal amount limit)", '', "E1703"],
  ["AUCNEGATIVE", "|", '', "E501"],
  ["AUCNEGATIVE", "62 | Restricted card", '', "E1626"],
  ["REDIRECT", "DECLINED (stolen)", '', "E1703"],
  ["AUCNEGATIVE", "201", '', "E335"],
  ["AUCNEGATIVE", "0 |", '', "E330"],
  ["AUCNEGATIVE", "909 | INVALID_TRANSACTION_TYPE", '', "E207"],
  ["EVNEGATIVE", "918 | Very High confidence", '', "E335"],
  ["AUCPOSITIVE", '', '', "failed"],
  ["AUCNEGATIVE", "Account number not validated", '', "E500"],
  ['', "Invalid CardNumber/Token/AltId or ibibo_code", '', "E1101"],
  ["ACS_REDIRECT", '', '', "E1601"],
  ['', "Rupay communication error", '', "E1703"],
  ["REDIRECT", "phonepe", '', "E501"],
  ["AUCNEGATIVE", "404 | Permanent System Failure", '', "E335"],
  ["EVNEGATIVE", "93 |", '', "E500"],
  ['', "FILTERED_DOMESTIC_PGS FILTERED_DOMESTIC_PGS", '', "E804"],
  ["EVNEGATIVE", "10024 | Bad cvd2 passed!", '', "E1101"],
  ["EVPOSITIVE", '', '', "E2101"],
  ["REDIRECT", "N:05:Do not honour", '', "E1206"],
  ["REDIRECT", "Issuer Compliance", '', "E1703"],
  ["ACS_REDIRECT", "NON SUFFICIENT FUNDS", '', "E1703"],
  ["ACS_REDIRECT", "phonepe", '', "E501"],
  ["3DS_METHOD_POSITIVE", "No Error", '', "E000"],
  ["EVNEGATIVE", "IER | Unknown Host", '', "E1905"],
  ["REDIRECT", "P9 | Enter lesser amount", '', "E1206"],
  ["3DS_METHOD_POSITIVE", "UNKNOWN_ERROR", '', "E502"],
  ["EVPOSITIVE", '', '', "SSER001"],
  ['', "Ibibo Code MAES is not currently active on merchant", '', "E6010"],
  ["3DS_CHALLENGE_NEGATIVE", "922 | ACS technical issue", '', "E202"],
  ["AUCNEGATIVE", "Blc|0 | Blc|SUCCESS", '', "E317"],
  ["AUCPOSITIVE", "Marking transaction as dropped - CS", '', "E231"],
  ["EVPOSITIVE", "05 | Do not honor", '', "E307"],
  ["REDIRECT", "P9 | Enter lesser amount", '', "E231"],
  ["AUCNEGATIVE", "57 | Transaction not permitted to cardholder", '', "E1642"],
  ["REDIRECT", "65 | Exceeds withdrawal count limit / Withdrawal count limit exceeded", '', "E231"],
  ["REDIRECT", "14 | Invalid card number", '', "E231"],
  ['', "Bad Track Data", '', "E1703"],
  ["3DS_CHALLENGE_POSITIVE", "UNKNOWN_ERROR", '', "E231"],
  ["REDIRECT", "googlepay", '', "E501"],
  ["AUCNEGATIVE", "306 | MCC", '', "E207"],
  ["ACS_REDIRECT", "GW00201 | Transaction not found", '', "E1903"],
  ["AUCNEGATIVE", "405 | System Connection Failure", '', "E231"],
  ["AUCNEGATIVE", "30054 | Transaction timed out", '', "E207"],
  ["REDIRECT", "91 | Issuer unavailable or switch inoperative", '', "E231"],
  ["3DS_METHOD_POSITIVE", "000 | Blc|SUCCESS", '', "E502"],
  ["ACS_REDIRECT", "paytm", '', "E501"],
  ["ACS_REDIRECT", "AUTHENTICATION_FAILED | Cardholder did not complete authentication", '', "E207"],
  ['', '', '', "E1202"],
  ["REDIRECT", "BIN is blocked", '', "E1703"],
  ["AUCNEGATIVE", "AUTHENTICATION_MODE_MISSING | AuthenticationMode not received, please reachout to PayU Support.", '', "E207"],
  ["REDIRECT", "Application error", '', "EX149"],
  ["VERERROR", "Verification | failed | Transaction failed at bank end", '', "E1903"],
  ["AUCNEGATIVE", "?:waiting authentication", '', "E1206"],
  ['', "PG filtering based on Issuer Token supported PGs", '', "E803"],
  ['', "Invalid amount", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "902 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["RNF", "PG filtering based on KTB Bin Routing", '', "E804"],
  ["REDIRECT", "93 | Transaction cannot be completed; violation of law", '', "E231"],
  ["REDIRECT", "Invalid BIN", '', "E1703"],
  ["REDIRECT", "N:ACCU600:Invalid data was posted to Issuer", '', "E1206"],
  ["AUCINVALID", '', '', "E000"],
  ["AUCNEGATIVE", "BEPG-0000017 | Issuer authentication failure", '', "E231"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|REQUEST_REJECTED::null", '', "E204"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E340"],
  ["AUCNEGATIVE", "AUTHENTICATION_FAILED|UNKNOWN_ERROR", '', "E501"],
  ["AUCNEGATIVE", "101 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["AUCNEGATIVE", "0 |", '', "E308"],
  ["REDIRECT", "N:52:No checking account", '', "E231"],
  ["REDIRECT", "N:59:DECLINED (fraud)", '', "E231"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '358759xxxxxx5940' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E204"],
  ["AUCNEGATIVE", "405 | For example, the sending component is unable to  establish connection to the receiving component.", '', "E207"],
  ["REDIRECT", '', '', "EA081"],
  ["ACS_REDIRECT", "NOT_ENROLLED_FAILURE", '', "E1302"],
  ["REDIRECT", "ERROR", '', "E1703"],
  ["AUCNEGATIVE", "14 | Invalid card number", '', "E231"],
  ["3DS_METHOD_POSITIVE", "AUTHENTICATION_FAILED|UNKNOWN_ERROR", '', "E501"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Unknown", '', "E202"],
  ["REDIRECT", "Rupay communication error", '', "E1703"],
  ["ACS_REDIRECT", "56 | No Card Record", '', "E231"],
  ["3DS_CHALLENGE_NEGATIVE", "87 | Bad Track Data", '', "E335"],
  ['', "Pick-up", '', "E1703"],
  ["REDIRECT", "61 | Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc", '', "E231"],
  ["REDIRECT", '', '', "E501"],
  ["MER_025|No Transaction exists with given merchant id : MER0000005118097", "FILTERED_DOMESTIC_PGS", '', "E804"],
  ["404", '', '', "E346"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '354047xxxxxx1040' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E204"],
  ["ACS_REDIRECT", "0 | OTP Generated Successfully", '', "E501"],
  ["AUCNEGATIVE", "5111 | Transaction failed. ECI1 and ECI6 transactions are not supported by merchant.", '', "E231"],
  ["AUCNEGATIVE", "Authentication Failed", '', "E1703"],
  ["3DS_METHOD_NEGATIVE", "CTO | Network Connect Time Out", '', "E1639"],
  ["ACS_REDIRECT", "AUTHENTICATION_ATTEMPTS", '', "E232"],
  ["REDIRECT", "0 |", '', "E706"],
  ["3DS_METHOD_POSITIVE", "googlepay", '', "E501"],
  ["3DS_METHOD_POSITIVE", "05 | Do not honor | Decline - General decline of the card. No other information provided by the issuing bank.", '', "E000"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '354350xxxxxx8301' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E204"],
  ["AUCINVALID", "Blc|399 | Blc|APPLICATION_ERROR", '', "E204"],
  ["AUCNEGATIVE", "57 | Transaction not permitted to cardholder", '', "E303"],
  ["AUCNEGATIVE", "Message Received Invalid.", '', "E500"],
  ['', "N:51:NON SUFFICIENT FUNDS", '', "E1206"],
  ["ACS_REDIRECT", "User Pressed cancel button", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "909 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["EVPOSITIVE", "GW00555 | UNKNOWN", '', "E231"],
  ["REDIRECT", "INVALID_REQUEST | Value '439486xxxxxx8650' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E202"],
  ["ACS_REDIRECT", "AUTHENTICATION_FAILED | Cardholder did not complete authentication", '', "E202"],
  ["ACS_REDIRECT", "|", '', "E502"],
  ["AUCNEGATIVE", "408 | Data element not in the required format or value is invalid as defined in Table A.1", '', "E335"],
  ['', "N:ACCU700:Session validation failed", '', "E231"],
  ["REDIRECT", "59 | Suspected fraud", '', "E231"],
  ["REDIRECT", "51 | Insufficient funds/over credit limit / Not sufficient funds", '', "E1206"],
  ["ACS_REDIRECT", "H | UNKNOWN", '', "E1206"],
  ["REDIRECT", "54 | Expired card", '', "E311"],
  ["ACS_REDIRECT", "Blc|0 | Blc|SUCCESS", '', "E501"],
  ['', "Mandatory Param Missing for Token txn ccexpmon", '', "E4510"],
  ["REDIRECT", '', '', "E000"],
  ["EVNEGATIVE", "NOT_ENROLLED_FAILURE", '', "E1302"],
  ["404", "FILTERED_DOMESTIC_PGS", '', "E803"],
  ["MER_025|No Transaction exists with given merchant id : MER0000005118097", "FILTERED_DOMESTIC_PGS", '', "E803"],
  ["REDIRECT", "H | UNKNOWN", '', "E231"],
  ["AUCNEGATIVE", "O8 | Do not retry", '', "E303"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '538952xxxxxx9037' is invalid. Invalid card number", '', "E204"],
  ["EVERROR", "50021 | Bad AcquiringBank configured for merchant_id(36413568) in pg_instance_id(37887779)!", '', "E205"],
  ["ACS_REDIRECT", '', '', "EX149"],
  ["3DS_METHOD_POSITIVE", '', '', "E502"],
  ["REDIRECT", "N:91:ERROR", '', "E231"],
  ["ACS_REDIRECT", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Transaction Error", '', "E202"],
  ["AUCNEGATIVE", "DECLINED (Exceeds withdrawal amount limit)", '', "E1703"],
  ["EVPOSITIVE", "UNKNOWN_ERROR", '', "E502"],
  ["REDIRECT", "phonepe", '', "E231"],
  ["AUCNEGATIVE", "5102 | Transaction failed. ECI-7 transactions are not supported by merchant.", '', "E303"],
  ["AUCNEGATIVE", "201 | Required element missing", '', "E335"],
  ["3DS_METHOD_NEGATIVE", "IER | Unknown Host", '', "E1905"],
  ["AUCNEGATIVE", "Blc|202 | Blc|SERVER_FAILED::Please contact customer support quoting the support code.", '', "E335"],
  ["ACS_REDIRECT", "Allowable number of PIN tries exceeded", '', "E1703"],
  ["3DS_METHOD_NEGATIVE", "INVALID_REQUEST | Value '559530xxxxxx6925' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E501"],
  ["EVPOSITIVE", "0 | OTP Generated Successfully", '', "E1206"],
  ["ACS_REDIRECT", "12 | Invalid transaction", '', "E1206"],
  ["ACS_REDIRECT", "65 | Exceeds withdrawal count limit / Withdrawal count limit exceeded", '', "E1206"],
  ["ACS_REDIRECT", '', '', "E1610"],
  ["REDIRECT", "N:-30052:Communication Error", '', "E231"],
  ["3DS_CHALLENGE_NEGATIVE", "912 | Transaction not permitted to cardholder", '', "E231"],
  ["AUCNEGATIVE", "N0 | Unable to authorize", '', "E303"],
  ["AUCNEGATIVE", "10004 | Invalid response from npci", '', "E1617"],
  ["REDIRECT", "N:ACCU700:Session validation failed", '', "E231"],
  ["3DS_METHOD_POSITIVE", "51 | Insufficient funds/over credit limit / Not sufficient funds", '', "E706"],
  ["REDIRECT", "N:-BEPG-0000006:Rupay check bin error", '', "E1206"],
  ["AUCNEGATIVE", "403 | Transient System Failure", '', "E335"],
  ["ACS_REDIRECT", '', '', "E340"],
  ['', "SYSTEM ERROR", '', "E1703"],
  ["REDIRECT", "UNKNOWN_ERROR", '', "E1601"],
  ['', "N:ACCU400:User was Inactive", '', "E1206"],
  ["ACS_REDIRECT", "Session expired for this transaction", '', "E1703"],
  ["EVERROR", "10004 | Internal server error in card info service", '', "E1617"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '547189xxxxxx4914' is invalid. Invalid card number", '', "E204"],
  ["3DS_CHALLENGE_NEGATIVE", "908 | No Card record", '', "E231"],
  ["3DS_METHOD_NEGATIVE", "Invalid Otp", '', "E316"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|Retrying due to IO Error at server", '', "E204"],
  ["AUCNEGATIVE", "405 | System connection failure.", '', "E335"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '567890xxxxxx8901' is invalid. Invalid card number", '', "E204"],
  ["REDIRECT", "55 | Invalid PIN", '', "E710"],
  ["ACS_REDIRECT", "Message Received Invalid", '', "E500"],
  ['', '', '', "E000"],
  ['', '', '', "E307"],
  ["AUCERROR", "|", '', "E501"],
  ["3DS_CHALLENGE_NEGATIVE", "PG_FAILED | Unable to parse authentication response", '', "E219"],
  ['', "Ibibo Code CC is not currently active on merchant", '', "E6010"],
  ["ACS_REDIRECT", "0 |", '', "E502"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Cardholder selected Cancel", '', "E202"],
  ["AUCNEGATIVE", "Element missing", '', "E2502"],
  ["ACS_REDIRECT", "GW00201 | Transaction not found", '', "E231"],
  ["AUCNEGATIVE", "908 | INVALID_TRANSACTION_TYPE", '', "E207"],
  ['', '', '', "E903"],
  ["REDIRECT", "0 |", '', "E502"],
  ['', "Transaction cannot be completed", '', "E1703"],
  ['', "3D Secure authentication failed", '', "E1703"],
  ["REDIRECT", "Transaction cannot be completed", '', "E1703"],
  ["AUCNEGATIVE", "AUTHENTICATION_SUCCESSFUL|Transaction failed in Authorization", '', "E308"],
  ["AUCNEGATIVE", "908 | No Card record", '', "E335"],
  ['', "PG filtering based on Card SI PGs", '', "E803"],
  ["AUCNEGATIVE", "12 | Transaction not permitted to cardholder", '', "E1633"],
  ["EVERROR", "50021 | XML Data Error - Invalid Parameter Value - ipaddress", '', "E205"],
  ["ACS_REDIRECT", '', '', "E1206"],
  ['', "Ibibo Code RUPAY is not currently active on merchant", '', "E6010"],
  ['', "Ibibo Code VISA is not currently active on merchant", '', "E6010"],
  ["AUCNEGATIVE", "19 | Exceeds ACS maximum challenges", '', "E708"],
  ['', "Disable pg down time handling on UI so marked as bounced.", '', "E804"],
  ["EVNEGATIVE", "96 | SYSTEM ERROR", '', "E205"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Cardholder selected Cancel", '', "E1633"],
  ["ALT_ID_PROV_ERROR", "EA082|DPA entity data not found for the given clientId or dpaId in getDpaEntityData request.", '', "EA082"],
  ['', "REMOVED_HEADLESS_PGS", '', "E804"],
  ["3DS_VERIFICATION_NEGATIVE", "Suspected fraud", '', "E324"],
  ['', "Bin used is blocked on platform", '', "E6016"],
  ["AUCNEGATIVE", "50822 | Processing error while provisioning Guest Checkout Token", '', "E207"],
  ["AUCNEGATIVE", "04 | Exceeds authentication frequency limit", '', "E909"],
  ["REDIRECT", "CA | Acquirer compliance", '', "E231"],
  ["3DS_CHALLENGE_NEGATIVE", "908 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["REDIRECT", "Validation problem", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "911 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E1206"],
  ["REDIRECT", "Unable to get payer authentication", '', "E1703"],
  ["REDIRECT", "Exceeds withdrawal frequency limit", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "TRANSACTION_INVALID", '', "E202"],
  ["ALT_ID_PROV_ERROR", "EA086|Not a mastercard or maestro", '', "EA086"],
  ["AUCNEGATIVE", "0 |", '', "E502"],
  ["AUCINVALID", "0 | OTP Generated Successfully", '', "E1601"],
  ['', "DECLINED (cardholder not allowed)", '', "E1703"],
  ["AUCNEGATIVE", "000 | Blc|SUCCESS", '', "E317"],
  ["3DS_CHALLENGE_NEGATIVE", "TRANSACTION_INVALID", '', "E502"],
  ["ACS_REDIRECT", "?:waiting authentication", '', "E231"],
  ["EVERROR", "10024 | Purpose of Authentication should not be Alt Id for International transactions!", '', "E1101"],
  ["EVERROR", "50021 | Bad Expiry year passed!", '', "E205"],
  ['', "DECLINED (lost card)", '', "E1703"],
  ["ACS_REDIRECT", "Invalid Otp", '', "E1602"],
  ["AUCNEGATIVE", "Required element missing", '', "E500"],
  ["REDIRECT", "DECLINED (fraud)", '', "E1703"],
  ["3DS_METHOD_ERROR", '', '', "E214"],
  ["REDIRECT", "UNKNOWN_ERROR", '', "E1602"],
  ['', "Mandatory Param Missing tavv", '', "E1101"],
  ["AUCNEGATIVE", "Blc|203 | Blc|result=FAILURE", '', "E1633"],
  ["REDIRECT", "SUCCESS", '', "E1206"],
  ["3DS_METHOD_NEGATIVE", "DAUTH | Transaction Declined By Payment Gateway.", '', "E500"],
  ["AUCNEGATIVE", '', '', "E1302"],
  ["3DS_METHOD_POSITIVE", "UNKNOWN_ERROR", '', "E231"],
  ["3DS_CHALLENGE_NEGATIVE", "919 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["AUCNEGATIVE", "Unkonwn Error.", '', "E500"],
  ["REDIRECT", "Invalid account", '', "E1703"],
  ["3DS_METHOD_NEGATIVE", "INVALID_REQUEST | Invalid credentials.", '', "E202"],
  ["AUCNEGATIVE", "BEPG-0000006 | Check BIN call failed", '', "E207"],
  ["AUCNEGATIVE", "07 | Invalid transaction", '', "E207"],
  ['', "Exceeds withdrawal frequency limit", '', "E1703"],
  ["AUCNEGATIVE", "202 | FAILURE::AUTHENTICATION_REJECTED", '', "E1633"],
  ["REDIRECT", '', '', "E1205"],
  ["ACS_REDIRECT", "GW00555 | UNKNOWN", '', "E1206"],
  ["3DS_VERIFICATION_NEGATIVE", "Exceeds authentication frequency limit", '', "E909"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Transaction Timed out at ACS - First CReq not received by ACS", '', "E202"],
  ["EVNEGATIVE", "VERMCC04 | Validation Error-MCC MisMatched", '', "E226"],
  ["Get_cryptogram_failure", "Ibibo Code CC is not currently active on merchant", '', "E4932"],
  ["REDIRECT", "57 | Transaction not permitted to issuer/cardholder", '', "E231"],
  ["3DS_CHALLENGE_ERROR", '', '', "E214"],
  ["AUCERROR", "0 |", '', "E214"],
  ["ALT_ID_PROV_ERROR", "EA03|Technical error. Please try again", '', "EA03"],
  ['', "Unable to authorize", '', "E1703"],
  ['', "Processing error while provisioning Guest Checkout Token", '', "E1703"],
  ["ALT_ID_PROV_ERROR", "EA080|GENERIC_ERROR", '', "EA080"],
  ['', "DECLINED (fraud)", '', "E1703"],
  ['', "DECLINED (restricted card)", '', "E1703"],
  ["AUCNEGATIVE", "82 | UNKNOWN", '', "E500"],
  ['', "Mandatory Param Missing last4digits", '', "E4510"],
  ["ACS_REDIRECT", "N:-BEPG-0000017:Issuer authentication failure", '', "E1206"],
  ["ACS_REDIRECT", '', '', "E1205"],
  ["EVNEGATIVE", "BNF | Bin Not Found", '', "E4934"],
  ["3DS_METHOD_NEGATIVE", '', '', "E316"],
  ["3DS_METHOD_POSITIVE", "UNKNOWN_ERROR", '', "E1206"],
  ["REDIRECT", "EXPIRED CARD", '', "E1703"],
  ["AUCNEGATIVE", "12 | Invalid transaction", '', "E207"],
  ["REDIRECT", "N:-5014:Validation problem", '', "E231"],
  ["AUCERROR", "E101", '', "E335"],
  ["3DS_CHALLENGE_NEGATIVE", "Blc|203 | Blc|result=FAILURE", '', "E317"],
  ["AUCNEGATIVE", "Transaction cannot be completed", '', "E1703"],
  ["AUCNEGATIVE", "305 | Transaction ID has already been received and processed.", '', "E335"],
  ["ACS_REDIRECT", "91 | Issuer unavailable or switch inoperative", '', "E231"],
  ["REDIRECT", "N:93:Transaction cannot be completed", '', "E231"],
  ['', "No checking account", '', "E1703"],
  ["ACS_REDIRECT", "H | UNKNOWN", '', "E231"],
  ["ACS_REDIRECT", "14 | Invalid card number", '', "E231"],
  ["EVNEGATIVE", '', '', "E231"],
  ["AUCNEGATIVE", "305 | If in response to an AReq message: Cardholder Account Number is not in a range belonging to Issuer.", '', "E335"],
  ["AUCNEGATIVE", "Transient system failure", '', "E500"],
  ["3DS_CHALLENGE_NEGATIVE", "907 | Invalid transaction", '', "E202"],
  ["AUCPOSITIVE", '', '', "E1205"],
  ["ACS_REDIRECT", "The order already exists in the database.", '', "E1703"],
  ['', "PG filtering for AMEX", '', "E803"],
  ["AUCNEGATIVE", "14 | Invalid card number (no such number)", '', "E1632"],
  ["REDIRECT", "0 | OTP Generated Successfully", '', "E1205"],
  ['', "FILTERED_FOR_MERCHANT_CURRENCY", '', "E804"],
  ["AUCNEGATIVE", "Merchant Category Code (MCC) not valid for Payment System", '', "E500"],
  ['', "N:-30051:Communication Error", '', "E231"],
  ["REDIRECT", "N:-BEPG-0000013:Rupay transaction error", '', "E231"],
  ["AUCNEGATIVE", "903 | Unsupported Device", '', "E335"],
  ["REDIRECT", "Rupay transaction error", '', "E1703"],
  ['', "N:ACCU800:General exception", '', "E231"],
  ["REDIRECT", "SERVER_FAILED | Please contact customer support quoting the support code.", '', "E214"],
  ["3DS_METHOD_NEGATIVE", "SERVER_FAILED | Please contact customer support quoting the support code.", '', "E501"],
  ["AUCPOSITIVE", '', '', "E1206"],
  ["ACS_REDIRECT", "Processing error while provisioning Guest Checkout Token", '', "E1703"],
  ["AUCNEGATIVE", "0 |", '', "E501"],
  ["ACS_REDIRECT", '', '', "SSER001"],
  ["AUCNEGATIVE", "50822 | Processing error while provisioning Guest Checkout Token", '', "E231"],
  ["AUCNEGATIVE", "acctNumber", '', "E500"],
  ["3DS_METHOD_NEGATIVE", "INVALID_REQUEST | Value '535398xxxxxx1066' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E501"],
  ["EVPOSITIVE", "65 | Exceeds withdrawal count limit / Withdrawal count limit exceeded", '', "E909"],
  ["3DS_METHOD_NEGATIVE", "SERVER_FAILED | Please contact customer support quoting the support code.", '', "E214"],
  ["AUCNEGATIVE", "50822 | Processing error while provisioning Guest Checkout Token", '', "E303"],
  ["3DS_CHALLENGE_NEGATIVE", "101 | RReq is not available", '', "E231"],
  ["EVNEGATIVE", "Marking transaction as dropped - CS", '', "E231"],
  ['', "Ibibo Code NOT_AVAILABLE is not currently active on merchant", '', "E6010"],
  ["AUCNEGATIVE", "The order already exists in the database.", '', "E1703"],
  ["AUCNEGATIVE", '', '', "E1601"],
  ["ALT_ID_PROV_ERROR", "EA085|issuer_not_supported", '', "EA085"],
  ["ACS_REDIRECT", "Blc|0 | Blc|SUCCESS", '', "E1206"],
  ["AUCNEGATIVE", "Session timed out", '', "E231"],
  ["ACS_REDIRECT", "Invalid Input Parameter For Guest Checkout Transaction | UNKNOWN", '', "E500"],
  ["AUCNEGATIVE", "5003 | The order already exists in the database.", '', "E1206"],
  ["REDIRECT", "65 | Exceeds withdrawal count limit / Withdrawal count limit exceeded", '', "E909"],
  ["AUCNEGATIVE", "Message Version Number received is not valid for the receiving component.", '', "E500"],
  ["ACS_REDIRECT", "DECLINED (stolen)", '', "E1703"],
  ["3DS_METHOD_POSITIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Transaction Error", '', "E202"],
  ["AUCNEGATIVE", "Invalid Otp", '', "SSER001"],
  ["3DS_CHALLENGE_NEGATIVE", "408 | PrqFrq request timedout!", '', "E712"],
  ["3DS_METHOD_POSITIVE", "61 | Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc | Decline - The card has reached the credit limit.", '', "E000"],
  ["AUCNEGATIVE", "101 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E1633"],
  ["3DS_CHALLENGE_NEGATIVE", "TRANSACTION_INVALID", '', "E501"],
  ["EVERROR", "50021 | Bad AcquiringBank configured for merchant_id(50756239) in pg_instance_id(37887779)!", '', "E205"],
  ["REDIRECT", "0 | OTP Generated Successfully", '', ''],
  ["3DS_METHOD_POSITIVE", '', '', ''],
  ["AUCNEGATIVE", "DECLINED (cardholder not allowed)", '', "E1703"],
  ["MER_025|No Transaction exists with given merchant id : MER0000005118097", "PG filtering based on KTB Bin Routing", '', "E803"],
  ["AUCNEGATIVE", '', '', "E1608"],
  ["AUCNEGATIVE", "QR", '', "E501"],
  ["AUCNEGATIVE", "203 | Data element not in the required format.", '', "E335"],
  ["EVERROR", "10024 | Card Information not found", '', "E1101"],
  ["3DS_CHALLENGE_NEGATIVE", "PG_FAILED | Attempts Processing Performed. Authentication could not be completed, but a proof of authentication attempt (CAVV) was generated.", '', "E316"],
  ['', "Transaction timed out", '', "E1703"],
  ["EVNEGATIVE", "101 | Message not recognised", '', "E335"],
  ["AUCPOSITIVE", "Marking transaction as dropped - CSW", '', "E1206"],
  ["AUCNEGATIVE", "N:93:Transaction cannot be completed", '', "E231"],
  ["AUCNEGATIVE", '', '', "E2100"],
  ['', "N:-5110:Cardholder did not return from Rupay", '', "E231"],
  ['', "PG filtering based on Card SI PGs", '', "E501"],
  ["3DS_METHOD_NEGATIVE", "3DS206 |", '', "E500"],
  ["AUCNEGATIVE", "T8 | Invalid account", '', "E303"],
  ["EVNEGATIVE", "922 | ACS technical issue", '', "E335"],
  ["3DS_CHALLENGE_NEGATIVE", "983 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["AUCNEGATIVE", "Message not recognised", '', "E500"],
  ["ACS_REDIRECT", '', '', "E000"],
  ["3DS_CHALLENGE_NEGATIVE", "901 | Card authentication failed", '', "E1206"],
  ["AUCNEGATIVE", "57 | Transaction not permitted to issuer/cardholder", '', "E231"],
  ["ACS_REDIRECT", "Json processing", '', "E000"],
  ["ALT_ID_PROV_ERROR", "EA080|Exceeded configured rate limit for the API, please try again later", '', "EA080"],
  ["AUCERROR", "10024 | Unable to process the transaction, Invalid Response from NPCI", '', "E303"],
  ["ACS_REDIRECT", "14 | Invalid card number", '', "E1206"],
  ["3DS_METHOD_POSITIVE", '', '', "E1611"],
  ["3DS_METHOD_NEGATIVE", "INVALID_REQUEST | Value '478896xxxxxx8844' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E501"],
  ["AUCNEGATIVE", "82 | No security module", '', "E313"],
  ["AUCNEGATIVE", "INVALID_REQUEST | Value '2741401246...1815942193' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, the transaction.id must be unique for the", '', "E202"],
  ["3DS_METHOD_POSITIVE", "000 | Blc|SUCCESS", '', "E1602"],
  ["AUCNEGATIVE", "N:51:NON SUFFICIENT FUNDS", '', "E231"],
  ["ACS_REDIRECT", "P9 | Enter lesser amount", '', "E231"],
  ["AUCNEGATIVE", "87 | UNKNOWN", '', "E1633"],
  ["EVERROR", "15093 | violation", '', "E205"],
  ["3DS_METHOD_POSITIVE", "Message Received Invalid", '', "E500"],
  ["VERERROR", "Verification | failed | Key encData not present", '', "E202"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|Services are unavailable. Please try again later.", '', "E204"],
  ["3DS_VERIFICATION_NEGATIVE", '', '', "E231"],
  ["3DS_METHOD_NEGATIVE", "INVALID_REQUEST | Value '433187xxxxxx9523' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E501"],
  ["AUCNEGATIVE", "55 | Incorrect personal identification number", '', "E710"],
  ["ACS_REDIRECT", "INVALID_REQUEST | Invalid credentials.", '', "E202"],
  ["AUCNEGATIVE", "305 | Transaction Data Not Valid", '', "E335"],
  ["REDIRECT", "N:-50822:Processing error while provisioning Guest Checkout Token", '', "E231"],
  ["3DS_METHOD_NEGATIVE", '', '', "E219"],
  ["3DS_VERIFICATION_NEGATIVE", "E303 | SUCCESS", '', "E000"],
  ["3DS_CHALLENGE_NEGATIVE", "402 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["REDIRECT", "Invalid amount", '', "E1703"],
  ["REDIRECT", "GW00555 | UNKNOWN", '', "E231"],
  ["REDIRECT", "Compliance error code for LMM", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "PROCEED", '', "E317"],
  ['', "Ibibo Code NULL is not currently active on merchant", '', "E6010"],
  ["REDIRECT", "Rupay authentication error", '', "E1703"],
  ['', "UNKNOWN", '', "E500"],
  ["ALT_ID_PROV_ERROR", "EA03 | Technical error. Please try again", '', "EA03"],
  ["AUCNEGATIVE", "?:waiting authentication", '', "E231"],
  ['', "EXPIRED CARD", '', "E1703"],
  ["REDIRECT", "000 | Blc|SUCCESS", '', "E502"],
  ["REDIRECT", "N:93:Transaction cannot be completed", '', "E1206"],
  ["AUCNEGATIVE", "Blc|202 | Blc|Invalid threeDSServerTransID, not found in transaction", '', "E335"],
  ['', "Issuer not available", '', "E1703"],
  ["EVNEGATIVE", "|", '', "E500"],
  ["ACS_REDIRECT", "?:waiting authentication", '', "E1206"],
  ["REDIRECT", "N:-5110:Cardholder did not return from Rupay", '', "E231"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '529153xxxxxx2028' is invalid. Invalid card number", '', "E204"],
  ["ACS_REDIRECT", "Invalid transaction", '', "E1703"],
  ["REDIRECT", '', '', "E502"],
  ["AUCNEGATIVE", "404 | Unkonwn Error.", '', "E207"],
  ['', "N:-BEPG-0000017:Issuer authentication failure", '', "E231"],
  ["3DS_CHALLENGE_POSITIVE", "Marking transaction as dropped - CSW", '', "E000"],
  ["REDIRECT", '', '', "E503"],
  ["AUCNEGATIVE", "INVALID_REQUEST|AUTHENTICATION_INVALID_DATA_ERROR", '', "E915"],
  ["3DS_CHALLENGE_NEGATIVE", "51 | Retry the transaction later", '', "E335"],
  ["EVPOSITIVE", "Marking transaction as dropped - CSW", '', "E231"],
  ["AUCNEGATIVE", "UNKNOWN_ERROR", '', "E1101"],
  ["3DS_METHOD_POSITIVE", "AUTHORIZED", '', "E000"],
  ["AUCNEGATIVE", "Wrong transaction state", '', "E000"],
  ["3DS_METHOD_NEGATIVE", "INVALID_REQUEST | Value '220432xxxxxx6229' is invalid. value: 220432xxxxxx6229 - reason: Invalid card number", '', "E501"],
  ["AUCNEGATIVE", "901 | INVALID_TRANSACTION_TYPE", '', "E231"],
  ["AUCNEGATIVE", "System Connection Failure", '', "E500"],
  ["AUCNEGATIVE", "101 | Message not recognised", '', "E335"],
  ["3DS_VERIFICATION_NEGATIVE", "CURL_CALL_FAILURE", '', "E231"],
  ['', "Compliance error code for LMM", '', "E1703"],
  ["AUCNEGATIVE", "0 | OTP Generated Successfully", '', "10004"],
  ["EVNEGATIVE", "10004 | Invalid response from npci", '', "E1617"],
  ["EVNEGATIVE", "10004 | Something went wrong in generate otp request", '', "E1617"],
  ["REDIRECT", "Pick-up", '', "E1703"],
  ["AUCNEGATIVE", "SERVER_FAILED | Please contact customer support quoting the support code.", '', "E207"],
  ["AUCNEGATIVE", "56 | No card record", '', "E4346"],
  ["3DS_VERIFICATION_NEGATIVE", "Suspected fraud", '', "E1633"],
  ["REDIRECT", "70 | PIN data required", '', "E1629"],
  ["3DS_CHALLENGE_NEGATIVE", "408 | Blc|Unknown Error. Transaction Failed. Please try again later.", '', "E317"],
  ["REDIRECT", "phonepe", '', "E507"],
  ["AUCNEGATIVE", "Permanent system failure.", '', "E500"],
  ['', "N:51:NON SUFFICIENT FUNDS", '', "E231"],
  ['', "Ibibo Code UNKN is not currently active on merchant", '', "E6010"],
  ["REDIRECT", "04 | Pick Up Card", '', "E310"],
  ["ACS_REDIRECT", "googlepay", '', "E501"],
  ["3DS_CHALLENGE_NEGATIVE", "000 | Success", '', "E231"],
  ["ACS_REDIRECT", "No Error", '', "E000"],
  ["AUCNEGATIVE", "N:-BEPG-0000017:Issuer authentication failure", '', "E231"],
  ['', '', '', "E6005"],
  ["REDIRECT", "N:-BEPG-0000006:Rupay check bin error", '', "E231"],
  ["AUCNEGATIVE", "404 | Unkonwn Error.", '', "E231"],
  ["AUCNEGATIVE", "983 | INVALID_TRANSACTION_TYPE", '', "E207"],
  ["3DS_CHALLENGE_NEGATIVE", "983 | Declined by DS - DS dropped reason code received from ACS", '', "E202"],
  ["REDIRECT", "DECLINED (lost card)", '', "E1703"],
  ['', "Expired card", '', "E1703"],
  ["ALT_ID_PROV_ERROR", "EA081|The network token provision request contained data that could not be verified", '', "E000"],
  ["AUCNEGATIVE", "50716 | Transaction declined. 3D Secure authentication failed.", '', "E1206"],
  ["AUCNEGATIVE", '', '', "SSER001"],
  ["AUCNEGATIVE", "96 | SYSTEM ERROR", '', "E231"],
  ["REDIRECT", "0 |", '', ''],
  ['', "N:91:Issuer not available", '', "E231"],
  ["AUCNEGATIVE", '', '', "E502"],
  ["AUCNEGATIVE", "402 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["AUCNEGATIVE", "Cardholder Account Number is not in a range belonging to Issuer", '', "E500"],
  ["3DS_CHALLENGE_NEGATIVE", "T5 | Check for New information before retry", '', "E335"],
  ["AUCNEGATIVE", "5003 | The order already exists in the database.", '', "E303"],
  ["EVPOSITIVE", "62 | Restricted card", '', "E1206"],
  ["AUCNEGATIVE", "INVALID_REQUEST | Value '2763526091...3072537053' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, the transaction.id must be unique for the", '', "E202"],
  ["REDIRECT", "Blc|0 | Blc|SUCCESS", '', "E501"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '356867xxxxxx2419' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E204"],
  ["ACS_REDIRECT", "N:-BEPG-0000013:Rupay transaction error", '', "E231"],
  ["3DS_METHOD_NEGATIVE", "AUTHENTICATION_INVALID_REQUEST_ERROR", '', "E914"],
  ["ACS_REDIRECT", "phonepe", '', "E507"],
  ["3DS_CHALLENGE_NEGATIVE", "PG_FAILED | Authentication Failed", '', "E6009"],
  ["3DS_METHOD_POSITIVE", "Value '2735162399...1410627098' is invalid. Only authentication.3ds2.transactionStatus values of \"Y\", \"N\", \"U\", \"I\" or \"A\" may be provided on a financial transaction", '', "E1602"],
  ["EVPOSITIVE", "UNKNOWN_ERROR", '', "E1602"],
  ["AUCNEGATIVE", "0 |", '', "E340"],
  ["REDIRECT", "36 | Restricted Card, Retain Card", '', "E231"],
  ["AUCNEGATIVE", "82 | Policy (Mastercard use only)", '', "E1633"],
  ["3DS_METHOD_ERROR", '', '', "E4506"],
  ["ACS_REDIRECT", "P9 | Enter lesser amount", '', "E1206"],
  ["3DS_CHALLENGE_NEGATIVE", "984 | Declined by DS - Challenge Cancelation Indicator populated, therefore did not route to Smart Authentication Stand-In", '', "E202"],
  ["REDIRECT", "N:-5014:Validation problem", '', "E1206"],
  ["ACS_REDIRECT", "91 | Issuer unavailable or switch inoperative", '', "E1206"],
  ["AUCNEGATIVE", "203 | Format of one or more elements is invalid according to the specification", '', "E335"],
  ['', "N:93:Transaction cannot be completed", '', "E1206"],
  ["3DS_CHALLENGE_NEGATIVE", "984 | Blc|Authentication/Account Verification Could Not Be Performed; Technical or other problem, as indicated in ARes or RReq.", '', "E317"],
  ["EVPOSITIVE", "72 | UNKNOWN_ERROR", '', "E501"],
  ["AUCNEGATIVE", "ACS temporary unavailable", '', "E500"],
  ["AUCNEGATIVE", "|", '', "E1633"],
  ["ACS_REDIRECT", "N:-5014:Validation problem", '', "E1206"],
  ["ALT_ID_PROV_ERROR", "EA022|Expiry year is Invalid. Please check and initiate again", '', "EA022"],
  ["REDIRECT", "D1 | UNKNOWN", '', "E231"],
  ["EVPOSITIVE", "000 | Blc|SUCCESS", '', "E502"],
  ["REDIRECT", "30 | Format error", '', "E231"],
  ["3DS_METHOD_POSITIVE", "62 | Restricted card | Decline - General decline of the card. No other information provided by the issuing bank.", '', "E1626"],
  ["3DS_VERIFICATION_NEGATIVE", "System Error response from ACS", '', "E1633"],
  ["3DS_METHOD_POSITIVE", '', '', "E1302"],
  ["ACS_REDIRECT", "T5 | CAF status = 0 or 9", '', "E231"],
  ["AUCNEGATIVE", "BEPG-0000006 | Check BIN call failed", '', "E231"],
  ["AUCNEGATIVE", "UNKNOWN", '', "E500"],
  ["3DS_METHOD_NEGATIVE", "INVALID_REQUEST | Value '519537xxxxxx6381' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E501"],
  ["AUCNEGATIVE", "EXPIRED CARD", '', "E1703"],
  ["EVERROR", "50021 | kindly provide token authentication value if your passing Y in ext10.", '', "E205"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '354059xxxxxx1195' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E204"],
  ["AUCNEGATIVE", "SERVER_ERROR|", '', "E208"],
  ["AUCNEGATIVE", "12 | Transaction not permitted to cardholder", '', "E1642"],
  ["EVERROR", "15400 | general", '', "E308"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E231"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication", '', "E207"],
  ["AUCNEGATIVE", "06 | Invalid card number", '', "E305"],
  ["ALT_ID_PROV_ERROR", "EA084|PAN Ineligible", '', "EA084"],
  ['', "FILTERED_DOMESTIC_PGS", '', "E803"],
  ["ALT_ID_PROV_ERROR", "EA06|AUTHREFNO_INVALID", '', "EA06"],
  ['', '', '', "E802"],
  ['', "Do not honour", '', "E1703"],
  ["REDIRECT", "SUCCESS", '', "E231"],
  ['', '', '', "E6005"],
  ["ALT_ID_PROV_ERROR", "EA081|Invalid / Missing Field :: card expiry", '', "EA081"],
  ["AUCNEGATIVE", "911 | Suspected fraud", '', "E335"],
  ["3DS_METHOD_POSITIVE", '', '', "E502"],
  ["REDIRECT", "Do not honour", '', "E1703"],
  ["EVERROR", "50021 | Issuer Authentication Server failure", '', "E205"],
  ["AUCNEGATIVE", '', '', "E000"],
  ["AUCNEGATIVE", "101", '', "E335"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Transaction Error", '', "E202"],
  ["ALT_ID_PROV_ERROR", "EA086|Action cannot be performed as the payment-credential request for the token was declined", '', "EA086"],
  ["AUCNEGATIVE", "918 | Very High confidence", '', "E335"],
  ["REDIRECT", "Processing error while provisioning Guest Checkout Token", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "901 | Card authentication failed", '', "E231"],
  ["AUCPOSITIVE", '', '', "E231"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Invalid credentials.", '', "E204"],
  ["ALT_ID_PROV_ERROR", "UNKNOWN_ERROR", '', "E501"],
  ["EVPOSITIVE", '', '', "E308"],
  ["AUCNEGATIVE", "0 |", '', "E1650"],
  ["AUCNEGATIVE", "51 | Retry the transaction later", '', "E706"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Transaction Error", '', "E1633"],
  ["AUCNEGATIVE", "Invalid Otp", '', "E503"],
  ["ACS_REDIRECT", "Transaction cannot be completed", '', "E1703"],
  ["REDIRECT", "Bad Track Data", '', "E1703"],
  ["ACS_REDIRECT", '', '', "E1602"],
  ["3DS_VERIFICATION_NEGATIVE", "0", '', "E1206"],
  ["REDIRECT", "FRAUD - card function blocked", '', "E1703"],
  ["3DS_VERIFICATION_NEGATIVE", "Transaction timed out at the ACS", '', "E1633"],
  ["3DS_METHOD_NEGATIVE", "EMV3DSNS |", '', "E500"],
  ['', '', '', "E501"],
  ["ACS_REDIRECT", "N:-BEPG-0000017:Issuer authentication failure", '', "E231"],
  ["EVNEGATIVE", "10024 | Merchant is not active", '', "E1101"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Transaction Timed out at ACS - First CReq not received by ACS", '', "E1633"],
  ["REDIRECT", "N:ACCU800:General exception", '', "E231"],
  ["ACS_REDIRECT", "GW00555 | UNKNOWN", '', "E231"],
  ["REDIRECT", "DECLINED (cardholder not allowed)", '', "E1703"],
  ['', "Rupay check bin error", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "912 | Transaction not permitted to cardholder", '', "E202"],
  ['', '', '', "EX312"],
  ["AUCNEGATIVE", "922 | INVALID_TRANSACTION_TYPE", '', "E207"],
  ["AUCNEGATIVE", "14 | Transaction timed out at the ACS", '', "E231"],
  ["AUCERROR", "CURL_CALL_FAILURE", '', "E214"],
  ["AUCERROR", "Cannot invoke \"com.payu.cardsservice.cards.dto.response.common.FormPost.getPostUri()\" because the return value of \"com.payu.cardsservice.cards.dto.response.common.Data.getFormPost()\" is null", '', "E231"],
  ["EVERROR", "10004 | Unable to reach card information service", '', "E1617"],
  ["REDIRECT", '', '', "E308"],
  ["3DS_METHOD_NEGATIVE", "AUTHENTICATION_INVALID_DATA_ERROR", '', "E915"],
  ["AUCNEGATIVE", "00 | Authentication Request Successful", '', "E1601"],
  ["ACS_REDIRECT", '', '', ''],
  ["REDIRECT", "Format error", '', "E1703"],
  ["REDIRECT", "The order already exists in the database.", '', "E1703"],
  ["AUCNEGATIVE", "915 | Low confidence", '', "E335"],
  ["3DS_CHALLENGE_NEGATIVE", "922 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["3DS_METHOD_POSITIVE", '', '', "E501"],
  ["ACS_REDIRECT", "000 | Blc|SUCCESS", '', "E308"],
  ["AUCNEGATIVE", "Session timed out", '', "E000"],
  ["REDIRECT", "0 | OTP Generated Successfully", '', "E1206"],
  ["EVNEGATIVE", "912 | Transaction not permitted to cardholder", '', "E335"],
  ["EVNEGATIVE", "10004 | INTERNAL_SERVER_ERROR", '', "E1617"],
  ['', "Session validation failed", '', "E1703"],
  ["REDIRECT", "05 | Do not honor", '', "E231"],
  ['', "Application error", '', "E231"],
  ["ACS_REDIRECT", "Invalid Otp", '', "E308"],
  ["ACS_REDIRECT", "Invalid Otp", '', "E503"],
  ["AUCNEGATIVE", "83 | System Error response from ACS", '', "E208"],
  ["3DS_METHOD_POSITIVE", "Invalid Otp", '', "E1602"],
  ['', "DECLINED (Exceeds withdrawal amount limit)", '', "E1703"],
  ["EVNEGATIVE", "93 | Ecommerce Not Enabled", '', "E205"],
  ["AUCINVALID", "Invalid Otp", '', "E1601"],
  ['', "Ibibo Code SODEXO is not currently active on merchant", '', "E6010"],
  ["3DS_CHALLENGE_NEGATIVE", "000 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["AUCNEGATIVE", "101 | Invalid Message Type", '', "E207"],
  ["ACS_REDIRECT", "AUTHORIZED", '', "E000"],
  ["EVNEGATIVE", "413 | INVALID CVD2", '', "E205"],
  ["3DS_CHALLENGE_NEGATIVE", "926 | Authentication attempted but not performed by the cardholder", '', "E202"],
  ["3DS_METHOD_POSITIVE", "Marking transaction as dropped - CS", '', "E231"],
  ["REDIRECT", "N:ACCU800:General exception", '', "E1206"],
  ["EVPOSITIVE", '', '', "E1303"],
  ["3DS_VERIFICATION_NEGATIVE", "Invalid card number", '', "E305"],
  ["AUCNEGATIVE", "03 | Invalid merchant", '', "E341"],
  ["3DS_VERIFICATION_NEGATIVE", "Low confidence", '', "E4001"],
  ["REDIRECT", "Cancelled by user", '', "E1703"],
  ["AUCNEGATIVE", "87 | Bad Track Data", '', "E9224"],
  ["Get_cryptogram_failure", "Mandatory Param Missing for Token txn store_card_token", '', "E4932"],
  ['', "Rupay authentication error", '', "E1703"],
  ["AUCNEGATIVE", "Not a MasterCard supported card range.", '', "E500"],
  ["3DS_METHOD_POSITIVE", '', '', "E1206"],
  ['', "Ibibo Code DC is not currently active on merchant", '', "E6010"],
  ["3DS_VERIFICATION_NEGATIVE", "RREQ_NOT_RECEIVED", '', "E1633"],
  ["3DS_VERIFICATION_NEGATIVE", "UNKNOWN", '', "E1633"],
  ["ACS_REDIRECT", '', '', "E231"],
  ["AUCNEGATIVE", "910 | Stolen card", '', "E335"],
  ["AUCNEGATIVE", "UNKNOWN_ERROR", '', "E000"],
  ["REDIRECT", "3DSecure authentication failed", '', "E1703"],
  ["ACS_REDIRECT", "Do not honour", '', "E1703"],
  ["ACS_REDIRECT", "J | UNKNOWN", '', "E231"],
  ["ACS_REDIRECT", "TRANSACTION_INVALID", '', "E1206"],
  ["AUCNEGATIVE", "922 | ACS technical issue", '', "E335"],
  ["ACS_REDIRECT", "Issuer authentication failure", '', "E1703"],
  ["AUCNEGATIVE", "GW00201 | Transaction not found", '', "E1206"],
  ["REDIRECT", '', '', "E1903"],
  ["AUCNEGATIVE", "device.browserDetails.language", '', "E1302"],
  ["3DS_METHOD_NEGATIVE", "412 | Transaction got declined at issuer.", '', "E207"],
  ["3DS_VERIFICATION_NEGATIVE", "Cardholder not enrolled in service", '', "E1302"],
  ["3DS_VERIFICATION_NEGATIVE", "RREQ_NOT_RECEIVED", '', "E000"],
  ["AUCNEGATIVE", "O8 | Do not retry", '', "E207"],
  ["EVNEGATIVE", "408 |", '', "E712"],
  ['', "DECLINED (stolen)", '', "E1703"],
  ["3DS_VERIFICATION_NEGATIVE", '', '', "E308"],
  ["AUCINVALID", "Invalid Otp", '', "E000"],
  ["AUCNEGATIVE", "93 | Transaction cannot be completed; violation of law", '', "E231"],
  ["AUCNEGATIVE", "912 | INVALID_TRANSACTION_TYPE", '', "E231"],
  ["AUCNEGATIVE", "51 | Retry the transaction later", '', "E303"],
  ["REDIRECT", "N:61:DECLINED (Exceeds withdrawal amount limit)", '', "E231"],
  ['', "FILTERED_FOR_MCP", '', "E804"],
  ["ACS_REDIRECT", "00 | Authentication Request Successful", '', "E501"],
  ["REDIRECT", '', '', "E202"],
  ["AUCNEGATIVE", "5002 | The merchant is not setup to support the requested service.", '', "E207"],
  ["EVERROR", "14004 | Failed to process the transaction.", '', "E205"],
  ['', "N:61:DECLINED (Exceeds withdrawal amount limit)", '', "E231"],
  ["AUCNEGATIVE", "96 | SYSTEM ERROR", '', "E4158"],
  ["AUCNEGATIVE", "Transaction data not valid.", '', "E500"],
  ["ALT_ID_PROV_ERROR", "EA080|I9001", '', "EA080"],
  ["AUCNEGATIVE", "Data element not in the required format", '', "E500"],
  ['', '', '', "EX149"],
  ["AUCNEGATIVE", "05 | Do not honor", '', "E231"],
  ["EVNEGATIVE", "Blc|202 | Blc|Transaction processed for 3D Secure/Bank's Page. Waiting for Verification OTP/Password verification.", '', "E335"],
  ["AUCNEGATIVE", "62 | Restricted card", '', "E1206"],
  ["EVPOSITIVE", "K | UNKNOWN", '', "E231"],
  ["AUCPOSITIVE", "AUTHENTICATION_SUCCESSFUL | 100", '', "E1303"],
  ["AUCNEGATIVE", "404 | Unkonwn Error.", '', "E335"],
  ["REDIRECT", "No security module", '', "E1703"],
  ["REDIRECT", '', '', "E1303"],
  ["ALT_ID_PROV_ERROR", "|DpaId on-boarding in progress", '', ''],
  ["ACS_REDIRECT", "genericintent", '', "E501"],
  ["AUCNEGATIVE", "Permanent System Failure", '', "E500"],
  ["REDIRECT", "Session expired for this transaction", '', "E1703"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '354047xxxxxx1097' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E204"],
  ["AUCNEGATIVE", "203 | Some fields are not valid", '', "E335"],
  ["AUCNEGATIVE", "10 | Stolen card", '', "E1633"],
  ["REDIRECT", "UNKNOWN_ERROR", '', "E000"],
  ["3DS_METHOD_POSITIVE", "UNKNOWN_ERROR", '', "E000"],
  ['', "Application error", '', "E000"],
  ['', "PG filtering based on FILTERED_FOR_SDK_3DSS_DECOUPLED_AUTH", '', "E803"],
  ["REDIRECT", "N:-BEPG-0000015:Rupay authentication error", '', "E231"],
  ["REDIRECT", "No checking account", '', "E1703"],
  ["REDIRECT", "000 | Blc|SUCCESS", '', "E1602"],
  ['', "Ibibo Code UNIONPAY is not currently active on merchant", '', "E6010"],
  ["REDIRECT", "Invalid card number (no such Number)", '', "E1703"],
  ["REDIRECT", '', '', "E231"],
  ["REDIRECT", "N:ACCU200:User Pressed cancel button", '', "E231"],
  ["3DS_VERIFICATION_NEGATIVE", "Invalid card number", '', "E1633"],
  ['', "FILTERED_FOR_MERCHANT_CURRENCY", '', "E803"],
  ["ACS_REDIRECT", "GW00462 | Invalid Tranportal Password.", '', "E1206"],
  ["ACS_REDIRECT", "51 | Insufficient funds/over credit limit / Not sufficient funds", '', "E1206"],
  ["AUCNEGATIVE", "GW00201 | Transaction not found", '', "E000"],
  ["AUCNEGATIVE", "O6 | Suspected Fraud. Do not retry", '', "E207"],
  ["3DS_METHOD_POSITIVE", "Cancel api failed with response decision as  and reason code", '', "E1206"],
  ["REDIRECT", "QR", '', "E501"],
  ["AUCNEGATIVE", "201 | acsReferenceNumber", '', "E207"],
  ["3DS_CHALLENGE_ERROR", "UNKNOWN_ERROR", '', "E1633"],
  ["AUCNEGATIVE", "T5 | Check for New information before retry", '', "E9248"],
  ["REDIRECT", "N:ACCU200:User Pressed cancel button", '', "E1206"],
  ["AUCNEGATIVE", "913 | Cardholder not enrolled in service", '', "E335"],
  ["REDIRECT", "No card record", '', "E1703"],
  ["REDIRECT", "DECLINED (terminal not allowed)", '', "E1703"],
  ['', "Mandatory Param Missing for Token txn store_card_token", '', "E1101"],
  ['', "N:ACCU200:User Pressed cancel button", '', "E231"],
  ["REDIRECT", "Transaction Completed", '', "E000"],
  ["AUCNEGATIVE", "914 | INVALID_TRANSACTION_TYPE", '', "E207"],
  ["REDIRECT", "57 | Transaction not permitted to issuer/cardholder", '', "E1642"],
  ["AUCNEGATIVE", "87 | No Envelope Inserted", '', "E231"],
  ["ACS_REDIRECT", "Blc|0 | Blc|SUCCESS", '', "E231"],
  ["AUCNEGATIVE", "412 | Issuer Authentication Server failure", '', "E4934"],
  ["AUCNEGATIVE", "403 | BANK API error occurred", '', "E207"],
  ["AUCNEGATIVE", "56 | DECLINED (no card)", '', "E4346"],
  ["3DS_VERIFICATION_NEGATIVE", "No Card Record", '', "E1633"],
  ["3DS_CHALLENGE_NEGATIVE", "05 | Do not honour", '', "E335"],
  ["AUCNEGATIVE", "05 | Do not honour", '', "E307"],
  ["AUCNEGATIVE", '', '', "E317"],
  ['', "Invalid card number (no such Number)", '', "E1703"],
  ["AUCNEGATIVE", "305 | Cardholder Account Number is not in a range belonging to Issuer", '', "E335"],
  ["AUCNEGATIVE", "301 | Transaction ID is recognised as a duplicate.", '', "E335"],
  ['', "DECLINED (terminal not allowed)", '', "E1703"],
  ["REDIRECT", "N:-5014:Validation problem", '', "E308"],
  ["AUCNEGATIVE", "Duplicate transaction", '', "E500"],
  ['', "PG filtering based on AltId supported PGs", '', "E803"],
  ["AUCNEGATIVE", "405 | System Connection Failure", '', "E207"],
  ["AUCNEGATIVE", "405", '', "E335"],
  ["AUCNEGATIVE", "402 | DS Response is blank", '', "E335"],
  ["VERERROR", "Verification | failed | Key encData not present", '', "E231"],
  ["ACS_REDIRECT", "AUTHENTICATION_SUCCESSFUL|Transaction failed in Authorization", '', "E308"],
  ["REDIRECT", "paytm", '', "E501"],
  ["EVERROR", "10004 | Could not get the proper response from NPCI", '', "E1617"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '355193xxxxxx4792' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E204"],
  ["ACS_REDIRECT", '', '', "E1206"],
  ["AUCNEGATIVE", "Format of one or more elements is invalid according to the specification.", '', "E500"],
  ["REDIRECT", "Mobile number record not found/ mis-match", '', "E1703"],
  ["AUCNEGATIVE", "65 | Exceeds withdrawal frequency limit", '', "E909"],
  ["ACS_REDIRECT", "57 | Transaction not permitted to issuer/cardholder", '', "E231"],
  ["REDIRECT", "Application error", '', "E000"],
  ["ACS_REDIRECT", "QR", '', "E308"],
  ["AUCNEGATIVE", "101 | Invalid Message Type", '', "E231"],
  ["EVPOSITIVE", '', '', ''],
  ["3DS_METHOD_POSITIVE", '', '', "E1608"],
  ["ACS_REDIRECT", "Issuer not available", '', "E1703"],
  ["ACS_REDIRECT", "QR", '', "E501"],
  ["EVPOSITIVE", "0 | OTP Generated Successfully", '', "E502"],
  ["3DS_METHOD_NEGATIVE", "INVALID_REQUEST | Value '492125xxxxxx2047' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E501"],
  ["ACS_REDIRECT", "51 | Insufficient funds/over credit limit / Not sufficient funds", '', "E231"],
  ["ACS_REDIRECT", "CA | Acquirer compliance", '', "E1206"],
  ["AUCNEGATIVE", "200 | Blc|Unknown Error. Transaction Failed. Please try again later.", '', "E335"],
  ["REDIRECT", "0 | OTP Generated Successfully", '', "E501"],
  ["REDIRECT", "?:waiting authentication", '', "E308"],
  ["ALT_ID_PROV_ERROR", "EA080|I0001", '', "EA080"],
  ['', "Transaction Completed", '', "E000"],
  ["REDIRECT", "T8 | UNKNOWN", '', "E231"],
  ["ACS_REDIRECT", "UNKNOWN_ERROR", '', "E231"],
  ["REDIRECT", "DECLINED (restricted card)", '', "E1703"],
  ['', "Invalid data was posted to Issuer", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "SECURE_3D_AUTHENTICATION_ERROR", '', "E317"],
  ["3DS_CHALLENGE_NEGATIVE", "907 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["AUCNEGATIVE", "910 | INVALID_TRANSACTION_TYPE", '', "E207"],
  ["ACS_REDIRECT", "Invalid Otp", '', "E231"],
  ["REDIRECT", "GW00201 | Transaction not found", '', "E000"],
  ["REDIRECT", "GW00201 | Transaction not found", '', "E1903"],
  ["REDIRECT", "Invalid merchant", '', "E1703"],
  ["REDIRECT", "Session validation failed", '', "E1703"],
  ["3DS_METHOD_POSITIVE", '', '', "E000"],
  ["EVPOSITIVE", "GW00462 | Invalid Tranportal Password.", '', "E231"],
  ["ACS_REDIRECT", '', '', "E502"],
  ["EVERROR", "50021 | Bad AcquiringBank configured for merchant_id(83992952) in pg_instance_id(37887779)!", '', "E205"],
  ["AUCERROR", '', '', "E214"],
  ['', '', '', "E502"],
  ["REDIRECT", "UNKNOWN", '', "E500"],
  ["REDIRECT", "UNKNOWN_ERROR", '', "E1206"],
  ['', '', '', ''],
  ['', "Invalid merchant", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Cardholder selected Cancel", '', "E207"],
  ["AUCNEGATIVE", "Blc|202 | Blc|FAILURE::DO_NOT_PROCEED", '', "E335"],
  ["AUCPOSITIVE", '', '', "E503"],
  ["3DS_CHALLENGE_NEGATIVE", "50716 | Transaction declined. 3D Secure authentication failed.", '', "E335"],
  ['', "General exception", '', "E1703"],
  ["EVERROR", "10004 | Something went wrong in checkbin request", '', "E1617"],
  ["AUCNEGATIVE", "Message received invalid", '', "E500"],
  ['', "Ibibo Code UNKNOWN is not currently active on merchant", '', "E6010"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '222841xxxxxx8081' is invalid. Invalid card number", '', "E204"],
  ["AUCNEGATIVE", "T8 | Invalid account", '', "E207"],
  ["AUCNEGATIVE", '', '', "E308"],
  ["AUCNEGATIVE", "Blc|202 | Blc|Transaction Failed  Please contact with admin.", '', "E335"],
  ["EVNEGATIVE", "DOI | Validation Error-Duplicate Order Id Received", '', "E500"],
  ["3DS_METHOD_NEGATIVE", "96 | Issuer System Failure", '', "E500"],
  ["AUCNEGATIVE", "Transient System Failure", '', "E500"],
  ["AUCNEGATIVE", "983 | Declined by DS - DS dropped reason code received from ACS", '', "E335"],
  ['', '', '', "E1660"],
  ["ACS_REDIRECT", "19 | Re-enter Transaction | Decline - General decline of the card. No other information provided by the issuing bank.", '', "E345"],
  ["AUCNEGATIVE", "T5 | Check for New information before retry", '', "E303"],
  ["AUCNEGATIVE", "305 | Transaction ID has already been received and processed.", '', "E231"],
  ["3DS_METHOD_NEGATIVE", "3DS201 |", '', "E213"],
  ['', "Invalid account", '', "E1703"],
  ['', "N:57:DECLINED (cardholder not allowed)", '', "E231"],
  ["REDIRECT", "Validation problem", '', "E000"],
  ['', "Format error", '', "E1703"],
  ["EVNEGATIVE", "RTO | Network Read Time Out", '', "E1001"],
  ['', "Ibibo Code BAJA is not currently active on merchant", '', "E6010"],
  ["3DS_VERIFICATION_NEGATIVE", "0", '', "E328"],
  ["3DS_METHOD_NEGATIVE", "3DS222 |", '', "E500"],
  ["AUCNEGATIVE", "Access denied, invalid endpoint", '', "E500"],
  ["3DS_CHALLENGE_NEGATIVE", "TRANSACTION_INVALID", '', "E1602"],
  ["EVPOSITIVE", "57 | Transaction not permitted to issuer/cardholder", '', "E1642"],
  ["AUCNEGATIVE", "910 | INVALID_TRANSACTION_TYPE", '', "E231"],
  ["ALT_ID_PROV_ERROR", "EA087|invalid_crypto_response", '', "EA087"],
  ["AUCNEGATIVE", "02 | UNKNOWN", '', "E500"],
  ["REDIRECT", "Application error", '', "E308"],
  ["ACS_REDIRECT", "Disable pg down time handling on UI so marked as bounced.", '', "E804"],
  ["EVNEGATIVE", "SERVER_FAILED | Please contact customer support quoting the support code.", '', "E214"],
  ["3DS_CHALLENGE_POSITIVE", "Marking transaction as dropped - CSW", '', "E1206"],
  ["AUCNEGATIVE", "15 | HISO_INDIA", '', "E305"],
  ["EVPOSITIVE", "00 | Approved or completed successfully", '', "E000"],
  ["AUCNEGATIVE", "00 | Authentication Request Successful", '', "E905"],
  ["AUCNEGATIVE", "922 | INVALID_TRANSACTION_TYPE", '', "E231"],
  ["AUCNEGATIVE", "47 | BIN is blocked", '', "E207"],
  ["AUCNEGATIVE", "08 | No Card Record", '', "E1633"],
  ["3DS_METHOD_POSITIVE", "INVALID_REQUEST | Value '2741821019...1837112895' is invalid. Only authentication.3ds2.transactionStatus values of \"Y\", \"N\", \"U\", \"I\" or \"A\" may be provided on a financial transaction", '', "E202"],
  ["EVNEGATIVE", "901 | Card authentication failed", '', "E335"],
  ["AUCNEGATIVE", "305 | Cardholder Account Number is not in a range belonging to Issuer.", '', "E335"],
  ["REDIRECT", "N:-30051:Communication Error", '', "E231"],
  ["EVERROR", "15417 | Duplicate requestID", '', "E504"],
  ["EVNEGATIVE", "10004 | Could not get the proper response from NPCI", '', "E1617"],
  ["AUCNEGATIVE", "302", '', "E335"],
  ['', "3DSecure authentication failed", '', "E1703"],
  ['', '', '', "E1602"],
  ["ACS_REDIRECT", "00 | Authentication Request Successful", '', "E1611"],
  ["ACS_REDIRECT", "GW00201 | Transaction not found", '', "E000"],
  ["AUCNEGATIVE", "Transaction ID received is not valid for the receiving component", '', "E500"],
  ["3DS_VERIFICATION_NEGATIVE", "Expired card", '', "E311"],
  ['', "Issuer Compliance", '', "E1703"],
  ["AUCNEGATIVE", "Blc|203 | Blc|response.gatewayRecommendation=DO_NOT_PROCEED", '', "E1633"],
  ["ACS_REDIRECT", "SECURE_3D_AUTHENTICATION_ERROR", '', "E317"],
  ["AUCNEGATIVE", "50716 | Transaction declined. 3D Secure authentication failed.", '', "E303"],
  ["REDIRECT", "GENERAL ERROR", '', "E1703"],
  ["EVPOSITIVE", "51 | Insufficient funds/over credit limit / Not sufficient funds", '', "E706"],
  ["EVNEGATIVE", "410 | Invalid BIN", '', "E337"],
  ["AUCNEGATIVE", "Invalid transaction", '', "E1703"],
  ['', "N:05:Do not honour", '', "E1206"],
  ["3DS_VERIFICATION_NEGATIVE", "Stolen card", '', "E310"],
  ["EVPOSITIVE", "62 | Restricted card", '', "E231"],
  ["REDIRECT", "0 | OTP Generated Successfully", '', "E1601"],
  ["AUCERROR", "|", '', "E303"],
  ["REDIRECT", "0 |", '', "E308"],
  ["ACS_REDIRECT", "User was Inactive", '', "E1703"],
  ['', '', '', "E507"],
  ["ACS_REDIRECT", "0 |", '', "E501"],
  ["ACS_REDIRECT", "Rupay check bin error", '', "E1703"],
  ["AUCNEGATIVE", "50655 | Unable to verify card enrollment", '', "E207"],
  ["3DS_METHOD_POSITIVE", "Session timed out", '', "E2503"],
  ["3DS_METHOD_POSITIVE", "FILTERED_FOR_MCP", '', "E804"],
  ['', '', '', "EX311"],
  ["VERERROR", "Verification | failed | Key encData not present", '', "E308"],
  ["EVPOSITIVE", "GW00201 | Transaction not found", '', "E1611"],
  ["AUCNEGATIVE", "System connection failure.", '', "E500"],
  ["AUCNEGATIVE", "202 | Transaction processed for 3D Secure/Bank's Page. Waiting for Verification OTP/Password verification.", '', "E1633"],
  ["ACS_REDIRECT", '', '', "EA082"],
  ["AUCNEGATIVE", "10004 | Could not get the proper response from NPCI", '', "E231"],
  ["5006", "PG filtering based on AltId supported PGs", '', "E803"],
  ["REDIRECT", "93 | Transaction cannot be completed; violation of law", '', "E1206"],
  ['', "Invalid BIN", '', "E1703"],
  ["REDIRECT", "N:400:GENERAL ERROR", '', "E231"],
  ["3DS_METHOD_POSITIVE", "UNKNOWN_ERROR", '', "E1611"],
  ["AUCNEGATIVE", "Issuer authentication failure", '', "E1703"],
  ["AUCNEGATIVE", "Blc|204 | Blc|No Response from PG. Please Contact support", '', "E317"],
  ["ALT_ID_PROV_ERROR", "MOF001|", '', "MOF001"],
  ["3DS_VERIFICATION_ERROR", '', '', "E1633"],
  ["3DS_CHALLENGE_ERROR", "INVALID_REQUEST | Unable to find order null and transaction null for merchant CPM03773", '', "E231"],
  ["AUCNEGATIVE", "Card range not found", '', "E500"],
  ["AUCNEGATIVE", "54 | Expired card", '', "E231"],
  ['', "N:-30052:Communication Error", '', "E231"],
  ["AUCNEGATIVE", "Transient System  Failure", '', "E500"],
  ["REDIRECT", "Transaction timed out", '', "E1703"],
  ["AUCNEGATIVE", '', '', "E501"],
  ["REDIRECT", "N:59:DECLINED (fraud)", '', "E1206"],
  ["REDIRECT", "T5 | CAF status = 0 or 9", '', "E231"],
  ["EVNEGATIVE", "908 | No Card record", '', "E335"],
  ["3DS_CHALLENGE_NEGATIVE", "5102 | Transaction failed. ECI-7 transactions are not supported by merchant.", '', "E335"],
  ["AUCNEGATIVE", "O6 | Suspected Fraud. Do not retry", '', "E303"],
  ["AUCNEGATIVE", "902 | Unknown Device", '', "E335"],
  ['', "Wrong transaction state", '', "E000"],
  ["AUCNEGATIVE", "51 | Retry the transaction later", '', "E231"],
  ["ACS_REDIRECT", "AUTHENTICATION_FAILED | Cardholder did not complete authentication | Cardholder selected Cancel", '', "E202"],
  ["AUCINVALID", '', '', "E1601"],
  ["AUCNEGATIVE", "408 | pArq Request timed out", '', "E231"],
  ["AUCNEGATIVE", "30054 | Transaction timed out", '', "E231"],
  ["REDIRECT", "N:54:EXPIRED CARD", '', "E231"],
  ["REDIRECT", "K | UNKNOWN", '', "E231"],
  ["3DS_CHALLENGE_NEGATIVE", "Blc|204 | Blc|Invalid PRsFr Response from PG. Contact Support Team.", '', "E317"],
  ["ALT_ID_PROV_ERROR", "EA11|The network token service was unavailable or timed out", '', "EA11"],
  ["3DS_METHOD_NEGATIVE", "|", '', "E308"],
  ["3DS_METHOD_POSITIVE", "AUTHORIZATION_FAILED_BY_BANK", '', "E1903"],
  ["3DS_METHOD_NEGATIVE", "3DS2ERR405 |", '', "E500"],
  ["EVPOSITIVE", "61 | Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc", '', "E909"],
  ["AUCNEGATIVE", "000 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["REDIRECT", "INVALID_REQUEST | Value '530842xxxxxx6267' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E202"],
  ["EVERROR", "50021 | Invalid tavv value", '', "E205"],
  ["EVNEGATIVE", "2032 | Invalid tavv value", '', "E205"],
  ["ACS_REDIRECT", "00 | Function performed error-free", '', "E000"],
  ["AUCNEGATIVE", "402", '', "E335"],
  ["AUCNEGATIVE", "202 | FAILURE::DO_NOT_PROCEED", '', "E1633"],
  ["3DS_CHALLENGE_NEGATIVE", "450 | INVALID OTP", '', "E231"],
  ["AUCNEGATIVE", '', '', "E1610"],
  ["REDIRECT", "46 | Closed account", '', "E717"],
  ["AUCNEGATIVE", "412 | Issuer Authentication Server failure", '', "E231"],
  ["AUCNEGATIVE", "203", '', "E335"],
  ['', "Marking transaction as dropped - CS", '', "E231"],
  ["AUCNEGATIVE", '', '', "E231"],
  ["3DS_METHOD_POSITIVE", '', '', ''],
  ["ACS_REDIRECT", "901 | Card authentication failed", '', "E202"],
  ['', '', '', "E1669"],
  ["3DS_CHALLENGE_NEGATIVE", "902 | Unknown Device", '', "E202"],
  ["ACS_REDIRECT", "googlepay", '', "E507"],
  ["REDIRECT", "13 | Invalid amount", '', "E715"],
  ["REDIRECT", "000 | Blc|SUCCESS", '', "E501"],
  ["REDIRECT", "Allowable number of PIN tries exceeded", '', "E1703"],
  ["REDIRECT", "N:57:DECLINED (cardholder not allowed)", '', "E1206"],
  ["REDIRECT", "N:96:SYSTEM ERROR", '', "E231"],
  ["EVPOSITIVE", "0 |", '', "E1206"],
  ["AUCNEGATIVE", "Rupay check bin error", '', "E1703"],
  ["ALT_ID_PROV_ERROR", "EA082|The given srci-dpa-id and program-id association is not found", '', "EA082"],
  ["REDIRECT", "00 | Authentication Request Successful", '', "E501"],
  ["MER_025|No Transaction exists with given merchant id : MER0000005118097", '', '', "E307"],
  ['', "Session expired for this transaction", '', "E1703"],
  ['', "N:96:Session expired for this transaction", '', "E231"],
  ["REDIRECT", '', '', "E1610"],
  ["EVNEGATIVE", "VERCARDT03 |", '', "E4935"],
  ["AUCNEGATIVE", "INVALID_REQUEST | Value '0' is invalid. Value is smaller than 1", '', "E207"],
  ["REDIRECT", "12 | Invalid transaction", '', "E1206"],
  ["AUCERROR", "INVALID_INPUT | Invalid request input. Please see details below.", '', "E207"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '354104xxxxxx1025' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E204"],
  ["EVPOSITIVE", "UNKNOWN", '', "E500"],
  ["3DS_VERIFICATION_NEGATIVE", "Transaction timed out at the ACS", '', "E1206"],
  ["AUCNEGATIVE", "|Decline - Expired card. You might also receive this if the expiration date you provided does not match the date the issuing bank has on file.", '', "E501"],
  ["REDIRECT", "INVALID_REQUEST | Value '515470xxxxxx8237' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E202"],
  ["ACS_REDIRECT", "0 |", '', "E1601"],
  ['', "Incorrect personal identification number", '', "E1703"],
  ["REDIRECT", "42 | No Universal Account", '', "E9252"],
  ["EVPOSITIVE", "UNKNOWN_ERROR", '', "E231"],
  ["REDIRECT", "01 | Refer to card issuer", '', "E231"],
  ["REDIRECT", '', '', "E307"],
  ["REDIRECT", "Wrong transaction state", '', "E1703"],
  ["AUCNEGATIVE", "E0914 | key not present,key not present", '', "E335"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '542843xxxxxx4814' is invalid. Invalid card number", '', "E204"],
  ["3DS_METHOD_POSITIVE", "AUTHENTICATION_ATTEMPTS", '', "E232"],
  ["ACS_REDIRECT", "51 | Insufficient funds/over credit limit / Not sufficient funds | Decline - Insufficient funds in the account.", '', "E706"],
  ["EVNEGATIVE", "07 | Pickup Card", '', "E500"],
  ["AUCNEGATIVE", "0 | OTP Generated Successfully", '', "01"],
  ["ACS_REDIRECT", "Invalid Otp", '', "E1206"],
  ["EVNEGATIVE", "2032 |", '', "E500"],
  ["ACS_REDIRECT", "00 | Successful approval/completion or that V.I.P. PIN verification is valid", '', "E000"],
  ["AUCNEGATIVE", "INVALID_REQUEST | Value '2760023501...2884677692' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, the transaction.id must be unique for the", '', "E202"],
  ["EVPOSITIVE", "13 | Invalid amount", '', "E715"],
  ["EVNEGATIVE", "911 | Suspected fraud", '', "E335"],
  ['', "Secure Hash Mismatch", '', "E000"],
  ["ACS_REDIRECT", '', '', "E500"],
  ['', "No card record", '', "E1703"],
  ['', "GENERAL ERROR", '', "E1703"],
  ["3DS_METHOD_POSITIVE", "Marking transaction as dropped - CSW", '', "E000"],
  ["ACS_REDIRECT", "UNKNOWN", '', "E500"],
  ["AUCNEGATIVE", '', '', "E340"],
  ["REDIRECT", "N:51:NON SUFFICIENT FUNDS", '', "E1206"],
  ["AUCNEGATIVE", "INVALID_REQUEST | Value '2745922311...2099809421' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, the transaction.id must be unique for the", '', "E202"],
  ["ACS_REDIRECT", "57 | Transaction not permitted to issuer/cardholder", '', "E1206"],
  ["REDIRECT", "N:91:Issuer not available", '', "E1206"],
  ["ACS_REDIRECT", "12 | Invalid transaction", '', "E231"],
  ["3DS_METHOD_POSITIVE", "Invalid Otp", '', "E340"],
  ["AUCNEGATIVE", "INVALID_REQUEST | Value '2741403236...1816062263' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, the transaction.id must be unique for the", '', "E202"],
  ["AUCNEGATIVE", "N:-BEPG-0000015:Rupay authentication error", '', "E231"],
  ["EVNEGATIVE", "405 | System connection failure.", '', "E335"],
  ["ACS_REDIRECT", "05 | Do not honor | Decline - General decline of the card. No other information provided by the issuing bank.", '', "E307"],
  ["REDIRECT", "Store is not open", '', "E1703"],
  ["REDIRECT", "slice", '', "E501"],
  ['', "N:ACCU200:User Pressed cancel button", '', "E1206"],
  ["AUCNEGATIVE", "Call failed", '', "E500"],
  ["REDIRECT", "N:-BEPG-0000001:Rupay communication error", '', "E231"],
  ["3DS_METHOD_POSITIVE", '', '', "E803"],
  ["ACS_REDIRECT", '', '', "E501"],
  ["AUCNEGATIVE", "Technical failure", '', "E1608"],
  ["3DS_CHALLENGE_NEGATIVE", "007 | PARS not available for the given ID", '', "E202"],
  ["ALT_ID_PROV_ERROR", "|DpaId on-boarding in progress", '', "E308"],
  ["3DS_METHOD_NEGATIVE", '', '', "E308"],
  ["AUCNEGATIVE", "Do not honour", '', "E1703"],
  ["REDIRECT", "12 | Invalid transaction", '', "E207"],
  ["AUCNEGATIVE", "908 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["AUCPOSITIVE", "UNKNOWN_ERROR", '', "E231"],
  ["3DS_CHALLENGE_NEGATIVE", "TRANSACTION_INVALID", '', "E1601"],
  ["EVERROR", "50021 | SYSTEM ERROR", '', "E205"],
  ["3DS_METHOD_NEGATIVE", "VERCNTDTRAI01 |", '', "E500"],
  ["3DS_METHOD_POSITIVE", "REMOVED_HEADLESS_PGS", '', "E804"],
  ["AUCNEGATIVE", "BEPG-0000001 | Could not establish connection with NPCI BEPG Initiate2 web service", '', "E207"],
  ['', "Allowable number of PIN tries exceeded", '', "E1703"],
  ["ACS_REDIRECT", "0 |", '', ''],
  ["REDIRECT", "13 | Invalid amount", '', "E231"],
  ["VERERROR", "Verification | failed | Key encData not present", '', "E1206"],
  ["AUCNEGATIVE", "Card number is not in configured bin range.", '', "E500"],
  ["AUCNEGATIVE", "305 | acctNumber", '', "E335"],
  ["AUCNEGATIVE", "0 | OTP Generated Successfully", '', "E340"],
  ["REDIRECT", "00 | Authentication Request Successful", '', ''],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|Invalid PvRs Response from PG. Contact Support Team.", '', "E204"],
  ['', "Suspected fraud", '', "E1703"],
  ["3DS_METHOD_POSITIVE", "Card authentication failed", '', "E317"],
  ["REDIRECT", '', '', "E1206"],
  ["REDIRECT", "0 |", '', "E501"],
  ["3DS_METHOD_POSITIVE", '', '', "failed"],
  ["3DS_CHALLENGE_NEGATIVE", "922 | Blc|Authentication/Account Verification Could Not Be Performed; Technical or other problem, as indicated in ARes or RReq.", '', "E317"],
  ['', "FILTERED_DOMESTIC_PGS FILTERED_DOMESTIC_PGS", '', "E803"],
  ["AUCNEGATIVE", "Transient system failure.", '', "E500"],
  ["AUCNEGATIVE", "919 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["3DS_CHALLENGE_NEGATIVE", "912 | Blc|Authentication/ Account Verification Rejected; Issuer is rejecting", '', "E317"],
  ["AUCNEGATIVE", "500|Request failed due to system error. | SYSTEM_ERROR", '', "E308"],
  ["REDIRECT", "01 | Refer to card issuer", '', "E348"],
  ["AUCNEGATIVE", '', '', "E500"],
  ["AUCNEGATIVE", "907 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["AUCNEGATIVE", "INVALID_REQUEST | Value '2758495232...2798545864' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, the transaction.id must be unique for the", '', "E202"],
  ["AUCNEGATIVE", "41 | Lost card", '', "E310"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '358440xxxxxx5412' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E204"],
  ['', "N:57:DECLINED (cardholder not allowed)", '', "E1206"],
  ["3DS_METHOD_POSITIVE", "93 | Transaction cannot be completed; violation of law | Transaction cannot be completed; violation of law", '', "E000"],
  ["ACS_REDIRECT", "bhim", '', "E501"],
  ["REDIRECT", '', '', "E1602"],
  ["AUCNEGATIVE", "Processing error while provisioning Guest Checkout Token", '', "E1703"],
  ['', "N:-BEPG-0000013:Rupay transaction error", '', "E000"],
  ["AUCERROR", "Cannot invoke \"com.payu.cardsservice.cards.dto.response.common.FormPost.getPostUri()\" because the return value of \"com.payu.cardsservice.cards.dto.response.common.Data.getFormPost()\" is null", '', "E1206"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value 'ANG' is invalid. Invalid Alpha Currency Code [ANG]", '', "E204"],
  ["REDIRECT", "N:12:Invalid transaction", '', "E231"],
  ['', "N:-BEPG-0000015:Rupay authentication error", '', "E231"],
  ["REDIRECT", "J | UNKNOWN", '', "E231"],
  ["3DS_METHOD_POSITIVE", "59 | Suspected fraud | Decline - General decline of the card. No other information provided by the issuing bank.", '', "E000"],
  ["REDIRECT", "Incorrect personal identification number", '', "E1703"],
  ["AUCNEGATIVE", "Bin range not configured", '', "E500"],
  ["AUCPOSITIVE", "UNKNOWN_ERROR", '', "E501"],
  ["ACS_REDIRECT", '', '', "E507"],
  ['', "N:54:EXPIRED CARD", '', "E231"],
  ["AUCNEGATIVE", "202 | Message not recognised", '', "E1633"],
  ["3DS_METHOD_POSITIVE", "61 | Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc", '', "E909"],
  ['', '', '', "E1610"],
  ["ACS_REDIRECT", "93 | Transaction cannot be completed; violation of law | Transaction cannot be completed; violation of law", '', "E325"],
  ["3DS_CHALLENGE_NEGATIVE", "914 | Transaction timed out at the ACS", '', "E1206"],
  ['', "User was Inactive", '', "E1703"],
  ["EVPOSITIVE", "CM900000 | UNKNOWN", '', "E231"],
  ["AUCNEGATIVE", "CAN is not in range", '', "E500"],
  ["REDIRECT", "12 | Invalid transaction", '', "E231"],
  ["3DS_VERIFICATION_NEGATIVE", '', '', ''],
  ["EVERROR", "10004 | Internal Server Error", '', "E1617"],
  ["AUCNEGATIVE", "0 | OTP Generated Successfully", '', "400"],
  ["AUCNEGATIVE", "Blc|202 | Blc|No Response from PG. Please Contact support", '', "E335"],
  ["3DS_METHOD_NEGATIVE", "Blc|102 | Blc|Invalid card scheme", '', "E204"],
  ["AUCNEGATIVE", "Internal error", '', "E500"],
  ["AUCINVALID", '', '', "E303"],
  ["EVNEGATIVE", "10024 | This Card type is not allowed !!", '', "E1101"],
  ["AUCNEGATIVE", "000 |", '', "E317"],
  ["ACS_REDIRECT", "AUTHENTICATION_FAILED | CONSUMER_AUTHENTICATION_FAILED", '', "E202"],
  ['', "Communication Error", '', "E1703"],
  ['', "PG filtering based on Optional TRID", '', "E804"],
  ["ACS_REDIRECT", "DECLINED (cardholder not allowed)", '', "E1703"],
  ["ACS_REDIRECT", "GW00201 | Transaction not found", '', "E1611"],
  ["ALT_ID_PROV_ERROR", "EA080|Error occurred during caas decryption.", '', "EA080"],
  ["REDIRECT", "54 | Expired card", '', "E231"],
  ["REDIRECT", "63 | Security violation", '', "E312"],
  ["3DS_CHALLENGE_NEGATIVE", "906 | Blc|Not Authenticated /Account Not Verified; Transaction denied", '', "E317"],
  ["ACS_REDIRECT", "J | UNKNOWN", '', "E1206"],
  ['', "Application error", '', "E1206"],
  ["ALT_ID_PROV_ERROR", "EA080|P9001", '', "EA080"],
  ["AUCNEGATIVE", "62 | Restricted card", '', "E303"],
  ["ACS_REDIRECT", "05 | Do not honor", '', "E231"],
  ["AUCNEGATIVE", "UNKNOWN_ERROR", '', "E502"],
  ["AUCNEGATIVE", "400 | GENERAL ERROR", '', "E4933"],
  ["AUCNEGATIVE", "NON SUFFICIENT FUNDS", '', "E1703"],
  ["3DS_CHALLENGE_NEGATIVE", "62 | Restricted card", '', "E335"],
  ["ACS_REDIRECT", "000 | Blc|SUCCESS", '', "E501"],
  ["AUCNEGATIVE", "22 | UNKNOWN", '', "E1633"],
  ['', "Unable to verify card enrollment", '', "E1703"],
  ['', "Mandatory Param Missing for Token txn user_credentials", '', "E1101"],
  ["AUCNEGATIVE", "402 | DS Response is blank", '', "E231"],
  ["AUCNEGATIVE", "Blc|202 | Blc|SERVER_FAILED::Cannot ensure consistent access to data. Please try again later.", '', "E335"],
  ["REDIRECT", "96 | System malfunction", '', "E4158"],
  ["REDIRECT", "Secure Hash Mismatch", '', "E000"],
  ["AUCNEGATIVE", "405 | System Connection Failure", '', "E335"],
  ['', '', '', "E1400"],
  ["3DS_CHALLENGE_POSITIVE", "Transaction failed due to BD response validation", '', "E308"],
  ["REDIRECT", "ACS response received", '', "E000"],
  ["EVERROR", "10004 | INTERNAL_SERVER_ERROR", '', "E1617"],
  ["ALT_ID_PROV_ERROR", "EA025|Expiry month is Invalid. Please check and initiate again", '', "EA025"],
  ["REDIRECT", "QR", '', "E507"],
  ["REDIRECT", "?:waiting authentication", '', "E000"],
  ["REDIRECT", "N:ACCU100:Authentication Failed", '', "E231"],
  ["REDIRECT", "N:91:Issuer not available", '', "E231"],
  ["AUCNEGATIVE", "BEPG-0000015 | Rupay authentication error", '', "E207"],
  ['', "N:62:DECLINED (restricted card)", '', "E231"],
  ["AUCNEGATIVE", "305", '', "E335"],
  ["REDIRECT", "Error while Processing FIRSTDATA payment", '', "E1703"],
  ["ACS_REDIRECT", "|", '', "E1206"],
  ["ACS_REDIRECT", "DECLINED (fraud)", '', "E1703"],
  ["REDIRECT", '', '', "E1611"],
  ['', "?:waiting authentication", '', "E000"],
  ["AUCNEGATIVE", "402 | For example, Read-Timeout expiry reached for the transaction as defined in Section 5.5.", '', "E207"],
  ["3DS_CHALLENGE_NEGATIVE", "41 | Lost card", '', "E335"],
  ["REDIRECT", "N:61:DECLINED (Exceeds withdrawal amount limit)", '', "E1206"],
  ["AUCNEGATIVE", "Element missing", '', "E000"],
  ["ACS_REDIRECT", "TRANSACTION_INVALID", '', "E000"],
  ["3DS_CHALLENGE_NEGATIVE", "402 | CReq message with this ACS Transaction ID has already been received and processed.", '', "E231"],
  ["3DS_METHOD_NEGATIVE", "3DS2001 |", '', "E500"],
  ["REDIRECT", "INVALID_REQUEST | Value '433279xxxxxx6066' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E202"],
  ["AUCNEGATIVE", "000 | Blc|SUCCESS", '', "E1602"],
  ["EVERROR", "15013 | amount error", '', "E220"],
  ["ACS_REDIRECT", "DECLINED (restricted card)", '', "E1703"],
  ["AUCNEGATIVE", "203 | Data element not in the required format or value is invalid as defined in Table A.1.", '', "E335"],
  ["AUCNEGATIVE", "101 | Invalid formatted message, can be caused by deserialization failures. Refer trace for more details", '', "E207"],
  ["REDIRECT", "56 | No Card Record", '', "E231"],
  ["AUCNEGATIVE", "305 | Cardholder Account Number is not in range belonging to Issuer.", '', "E335"],
  ["REDIRECT", "Marking transaction as dropped - CS", '', "E501"],
  ["REDIRECT", "0 |", '', "E1601"],
  ["404", '', '', "E307"],
  ["AUCNEGATIVE", "12 | Invalid transaction", '', "E231"],
  ["AUCNEGATIVE", "00 | Authentication Request Successful", '', "E501"],
  ["3DS_CHALLENGE_NEGATIVE", "Blc|204 | Blc|Services are unavailable. Please try again later.", '', "E317"],
  ["AUCERROR", '', '', "E209"],
  ["EVNEGATIVE", "454 | Duplicate requestID", '', "E337"],
  ["ACS_REDIRECT", "000 | Blc|SUCCESS", '', "E303"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '354044xxxxxx1010' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E204"],
  ["EVPOSITIVE", '', '', "E720"],
  ["AUCNEGATIVE", "0 |", '', "E1206"],
  ["AUCNEGATIVE", "If in response to an AReq message: Cardholder Account Number is not in a range belonging to Issuer.", '', "E500"],
  ["EVNEGATIVE", "10004 | Timed out at NPCI", '', "E1617"],
  ["MER_025|No Transaction exists with given merchant id : MER0000005118097", '', '', "E308"],
  ["ACS_REDIRECT", "00 | Authentication Request Successful", '', ''],
  ["3DS_CHALLENGE_POSITIVE", "UNKNOWN_ERROR", '', "E000"],
  ["AUCPOSITIVE", "Invalid Otp", '', "E503"],
  ["REDIRECT", "00 | Authentication Request Successful", '', "E1601"],
  ["ACS_REDIRECT", "cred", '', "E501"],
  ["AUCNEGATIVE", "Cannot invoke \"com.payu.cardsservice.cards.dto.response.common.FormPost.getPostUri()\" because the return value of \"com.payu.cardsservice.cards.dto.response.common.Data.getFormPost()\" is null", '', "E207"],
  ["AUCNEGATIVE", "101 | DataIntegrityViolationException while Database operation.", '', "E207"],
  ["AUCNEGATIVE", "AUTHENTICATION_FAILED|Decline - Invalid account number | INVALID_ACCOUNT", '', "E501"],
  ["ACS_REDIRECT", "N7 | Negative online CAM, dCVV, iCVV, CVV, or CAVV results or Offline | Decline - Invalid Card Verification Number (CVN).", '', "E1632"],
  ["AUCNEGATIVE", "10004 | INTERNAL_SERVER_ERROR", '', "E1617"],
  ['', "N:59:DECLINED (fraud)", '', "E1206"],
  ["AUCNEGATIVE", "987 | INVALID_TRANSACTION_TYPE", '', "E207"],
  ["REDIRECT", "INVALID_REQUEST | Value '478881xxxxxx9909' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E202"],
  ["3DS_METHOD_POSITIVE", "AUTHENTICATION_FAILED|Encountered a Payer Authentication problem. Payer could not be authenticated. | CONSUMER_AUTHENTICATION_FAILED", '', "E1003"],
  ["3DS_METHOD_ERROR", "No Error", '', "E214"],
  ["AUCNEGATIVE", "404 | Failed to invoke CardData API", '', "E335"],
  ['', "Mandatory Param Missing for AltId txn last4digits", '', "E4510"],
  ["ACS_REDIRECT", "Format error", '', "E1703"],
  ["AUCNEGATIVE", "INVALID_REQUEST | Value '2737545218...1569407615' is invalid. A transaction with this transaction ID has already been processed but the request parameters do not match. To process a new transaction for this order, the transaction.id must be unique for the", '', "E202"],
  ['', "Error while Processing FIRSTDATA payment", '', "E1703"],
  ["3DS_METHOD_POSITIVE", "NOT_ENROLLED_FAILURE", '', "E1302"],
  ["ACS_REDIRECT", "CA | Acquirer compliance", '', "E231"],
  ["3DS_CHALLENGE_NEGATIVE", "Blc|204 | Blc|No Response from PG. Please Contact support", '', "E317"],
  ["AUCNEGATIVE", "05 | Do not honour", '', "E303"],
  ["REDIRECT", "05 | Do not honor", '', "E1206"],
  ["REDIRECT", "cred", '', "E501"],
  ["AUCNEGATIVE", "SERVER_FAILED | Cannot ensure consistent access to data. Please try again later.", '', "E207"],
  ["REDIRECT", "INVALID_REQUEST | Value '443025xxxxxx9301' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E202"],
  ["AUCNEGATIVE", "0 | OTP Generated Successfully", '', "E1206"],
  ["EVNEGATIVE", "402 | DS Response is blank", '', "E335"],
  ['', "General Error", '', "E1703"],
  ["3DS_METHOD_ERROR", "APPROVED", '', "E4506"],
  ["REDIRECT", "N:57:DECLINED (cardholder not allowed)", '', "E231"],
  ["AUCNEGATIVE", "invalid transaction data", '', "E500"],
  ['', "NO ROUTING AVAILABLE", '', "E1703"],
  ["3DS_METHOD_POSITIVE", '', '', "E1601"],
  ["AUCPOSITIVE", '', '', "E000"],
  ["ACS_REDIRECT", "05 | Do not honor", '', "E1206"],
  ['', "N:-BEPG-0000017:Issuer authentication failure", '', "E000"],
  ["REDIRECT", "SUCCESS", '', "E308"],
  ['', "N:ACCU600:Invalid data was posted to Issuer", '', "E231"],
  ["ACS_REDIRECT", "N:-BEPG-0000001:Rupay communication error", '', "E231"],
  ['', "N:52:No checking account", '', "E231"],
  ["3DS_CHALLENGE_NEGATIVE", "82 | No security module", '', "E335"],
  ['', "DECLINED (exceeds frequency)", '', "E1703"],
  ["ACS_REDIRECT", '', '', "E4179"],
  ['', "Mandatory Param Missing tavv", '', "E4510"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '536472xxxxxx6135' is invalid. Invalid card number", '', "E204"],
  ['', "Acquirer compliance", '', "E1703"],
  ["AUCNEGATIVE", "402 | Transaction timed-out.", '', "E335"],
  ["3DS_METHOD_NEGATIVE", "Blc|204 | Blc|INVALID_REQUEST::Value '507872xxxxxx8773' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E204"],
  ["3DS_METHOD_NEGATIVE", "INVALID_REQUEST | Value '478926xxxxxx8429' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E501"],
  ["REDIRECT", "04 | Pick Up Card", '', "E231"],
  ["AUCNEGATIVE", "P9 | Enter lesser amount", '', "E231"],
  ["AUCNEGATIVE", "Missing card record.", '', "E500"],
  ["AUCNEGATIVE", "301 | threeDSServerTransID", '', "E207"],
  ["ACS_REDIRECT", "56 | No Card Record", '', "E1206"],
  ["AUCNEGATIVE", "203 | Format of one or more data elements is invalid according to the specification", '', "E335"],
  ["ACS_REDIRECT", "102", '', "E1206"],
  ["AUCNEGATIVE", "301 | Retrieved transaction already used", '', "E335"],
  ["REDIRECT", "INVALID_REQUEST | Value '416839xxxxxx1592' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E202"],
  ["ALT_ID_PROV_ERROR", "UNKNOWN", '', "E500"],
  ["REDIRECT", "000 | Blc|SUCCESS", '', "E303"],
  ["3DS_METHOD_NEGATIVE", "INVALID_REQUEST | Value '535398xxxxxx6715' is invalid. The combination of currency, card type and transaction type is not supported by a Merchant Acquirer relationship", '', "E501"],
  ["AUCNEGATIVE", "Blc|202 | Blc|Retrying due to IO Error at server", '', "E335"],
  ["3DS_CHALLENGE_NEGATIVE", "14 | Invalid card number (no such number)", '', "E335"],
  ["AUCNEGATIVE", "T5 | Check for New information before retry", '', "E1206"],
  ["AUCNEGATIVE", "301 | dsTransID", '', "E207"],
  ]}
  placeholder="Search"
/>
