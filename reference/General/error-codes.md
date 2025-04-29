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
* The **error\_message / message** column in the following table corresponds to the value returned in the **error\_message / message** parameter of the payment response

> 📘 Note:
>
> The reason for failure depends upon the error codes provided by different banks and hence the detailing of error reasons may differ from one transaction to another.

> ❗️ Transaction Stages Error handling
>
> For error references on during various transaction stages in Net Banking, Cards and Wallets, refer to [Transaction Stages - Transaction Stages - Error References on Field7 & Field8](ref:transaction-stages-error-references-field7-field8).

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        PayU Error Code
      </th>

      <th>
        error_message / message
      </th>

      <th>
        error_description
      </th>

      <th>
        title
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        E1620
      </td>

      <td>
        Payment Method Enforced and wrong method selected
      </td>

      <td>
        WRONG\_PAYMENT\_METHOD\_SELECTED
      </td>

      <td>
        WRONG\_PAYMENT\_METHOD\_SELECTED
      </td>
    </tr>

    <tr>
      <td>
        E907
      </td>

      <td>
        Wrong payment method selected.
      </td>

      <td>
        WRONG\_PAYMENT\_METHOD
      </td>

      <td>
        WRONG\_PAYMENT\_METHOD
      </td>
    </tr>

    <tr>
      <td>
        E4318
      </td>

      <td>
        WITHDRAWAL STOPPED OWING\
         TO LUNACY OF ACCOUNT HOLD
      </td>

      <td>
        WITHDRAWAL STOPPED OWING TO LUNACY OF ACCOUNT HOLD
      </td>

      <td>
        WITHDRAWAL\_STOPPED\_OWING\_TO\_LUNACY\_OF\_ACCOUNT\_HOLD
      </td>
    </tr>

    <tr>
      <td>
        E4317
      </td>

      <td>
        WITHDRAWAL STOPPED OWING\
         TO INSOLVENCY OF ACCOUNT
      </td>

      <td>
        WITHDRAWAL STOPPED OWING TO INSOLVENCY OF ACCOUNT
      </td>

      <td>
        WITHDRAWAL\_STOPPED\_OWING\_TO\_INSOLVENCY\_OF\_ACCOUNT
      </td>
    </tr>

    <tr>
      <td>
        E4316
      </td>

      <td>
        WITHDRAWAL STOPPED OWING\
         TO DEATH OF ACCOUNT HOLDER
      </td>

      <td>
        WITHDRAWAL STOPPED OWING TO DEATH OF ACCOUNT HOLDER
      </td>

      <td>
        WITHDRAWAL\_STOPPED\_OWING\_TO\_DEATH\_OF\_ACCOUNT\_HOLDER
      </td>
    </tr>

    <tr>
      <td>
        E4684
      </td>

      <td>
        VPA is not available for transaction
      </td>

      <td>
        VPA is not available for transaction
      </td>

      <td>
        VPA\_Is\_Not\_Available\_For\_Transaction
      </td>
    </tr>

    <tr>
      <td>
        E4685
      </td>

      <td>
        VPA is available for transaction
      </td>

      <td>
        VPA is available for transaction
      </td>

      <td>
        VPA\_Is\_Available\_For\_Transaction
      </td>
    </tr>

    <tr>
      <td>
        E224
      </td>

      <td>
        Virtual Account Number Mismatch
      </td>

      <td>
        VIRTUAL\_ACCOUNT\_NUMBER\_MISMATCH
      </td>

      <td>
        VIRTUAL\_ACCOUNT\_NUMBER\_MISMATCH
      </td>
    </tr>

    <tr>
      <td>
        E1649
      </td>

      <td>
        VIP Approval
      </td>

      <td>
        VIP\_APPROVAL
      </td>

      <td>
        VIP\_APPROVAL
      </td>
    </tr>

    <tr>
      <td>
        E4251
      </td>

      <td>
        VERSION/TAGS SENT NOT SUPPORTED BY PSP/BANK
      </td>

      <td>
        VERSION/TAGS SENT NOT SUPPORTED BY PSP/BANK
      </td>

      <td>
        VERSION\_TAGS\_SENT\_NOT\_SUPPORTED\_BY\_PSP\_BANK
      </td>
    </tr>

    <tr>
      <td>
        E4530
      </td>

      <td>
        Mandate request failed as start date is less than current date
      </td>

      <td>
        Validity start date should not be less than current date
      </td>

      <td>
        Validity\_Start\_Date\_Should\_Not\_Be\_Less\_Than\_Current\_Date
      </td>
    </tr>

    <tr>
      <td>
        E4531
      </td>

      <td>
        Mandate request failed as end date is less than start date
      </td>

      <td>
        Validity end date should not be less than validity start date
      </td>

      <td>
        Validity\_End\_Date\_Should\_Not\_Be\_Less\_Than\_Validity\_Start\_Date
      </td>
    </tr>

    <tr>
      <td>
        E4156
      </td>

      <td>
        VALIDATION ERROR
      </td>

      <td>
        VALIDATION ERROR
      </td>

      <td>
        VALIDATION\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4373
      </td>

      <td>
        VALIDATION ERROR
      </td>

      <td>
        VALIDATION ERROR
      </td>

      <td>
        VALIDATION\_ERROR\_1
      </td>
    </tr>

    <tr>
      <td>
        E4221
      </td>

      <td>
        VAE FAILED
      </td>

      <td>
        VAE FAILED
      </td>

      <td>
        VAE\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E705
      </td>

      <td>
        Bank declined to process the transaction due\
         to user permissions set for the card.
      </td>

      <td>
        USER\_PROFILE\_SETTINGS\_ERROR
      </td>

      <td>
        USER\_PROFILE\_SETTINGS\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4255
      </td>

      <td>
        URL VERSION MISMATCHED (NEG ACK FOR\
         RESPAUTH. ERROR CODE U18 IN FINAL RESPPAY.)
      </td>

      <td>
        URL VERSION MISMATCHED (NEG ACK FOR RESPAUTH. ERROR CODE U18 IN
      </td>

      <td>
        URL\_VERSION\_MISMATCHED\_NEG\_ACK\_FOR\_RESPAUTH\_\_ERROR\_CODE\_U18\_IN\_FINAL\_RESPPAY
      </td>
    </tr>

    <tr>
      <td>
        E500
      </td>

      <td>
        Bank failed to authenticate the customer
      </td>

      <td>
        UNKNOWN\_ERROR\_PG
      </td>

      <td>
        UNKNOWN\_ERROR\_PG
      </td>
    </tr>

    <tr>
      <td>
        E908
      </td>

      <td>
        International cards not allowed
      </td>

      <td>
        UNKNOWN\_BINS\_NO\_ACTIVE\_PG\_ASSIGNED
      </td>

      <td>
        UNKNOWN\_BINS\_NO\_ACTIVE\_PG\_ASSIGNED
      </td>
    </tr>

    <tr>
      <td>
        E1634
      </td>

      <td>
        Unique Constraint failure from the bank
      </td>

      <td>
        UNIQUE\_CONSTRAINT\_FAILURE
      </td>

      <td>
        UNIQUE\_CONSTRAINT\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E9209
      </td>

      <td>
        Unacceptable Transaction Fee
      </td>

      <td>
        Unacceptable Transaction Fee
      </td>

      <td>
        UNACCEPTABLE\_TRANSACTION\_FEE
      </td>
    </tr>

    <tr>
      <td>
        E1608
      </td>

      <td>
        Unable to process the request.
      </td>

      <td>
        UNABLE\_TO\_PROCESS
      </td>

      <td>
        UNABLE\_TO\_PROCESS
      </td>
    </tr>

    <tr>
      <td>
        E4385
      </td>

      <td>
        UNABLE TO PROCESS REVERSAL
      </td>

      <td>
        UNABLE TO PROCESS REVERSAL
      </td>

      <td>
        UNABLE\_TO\_PROCESS\_REVERSAL
      </td>
    </tr>

    <tr>
      <td>
        E4041
      </td>

      <td>
        Transaction failed due to internal exception\
         at server/cbs end at customer's bank
      </td>

      <td>
        UNABLE TO PROCESS DUE TO INTERNAL EXCEPTION AT SERVER/CBS/ETC ON
      </td>

      <td>
        UNABLE\_TO\_PROCESS\_DUE\_TO\_INTERNAL\_EXCEPTION\_AT\_SERVER\_CBS\_ETC\_ON\_REMITTER\_SIDE
      </td>
    </tr>

    <tr>
      <td>
        E4259
      </td>

      <td>
        Transaction failed due to internal exception\
         at server/cbs end at acquirer's bank
      </td>

      <td>
        UNABLE TO PROCESS DUE TO INTERNAL EXCEPTION AT SERVER/CBS/ETC ON
      </td>

      <td>
        UNABLE\_TO\_PROCESS\_DUE\_TO\_INTERNAL\_EXCEPTION\_AT\_SERVER\_CBS\_ETC\_ON\_BENEFICIARY\_TD\_SIDE
      </td>
    </tr>

    <tr>
      <td>
        E4044
      </td>

      <td>
        Transaction failed due to credit processing\
         issue in pool account of the acquriing bank
      </td>

      <td>
        UNABLE TO PROCESS CREDIT FROM BANK'S POOL/BGL ACCOUNT
      </td>

      <td>
        UNABLE\_TO\_PROCESS\_CREDIT\_FROM\_BANK\_S\_POOL\_BGL\_ACCOUNT
      </td>
    </tr>

    <tr>
      <td>
        E4045
      </td>

      <td>
        Transaction failed due to debit processing\
         issue in pool account of the customer bank
      </td>

      <td>
        UNABLE TO PROCESS CREDIT FROM BANK'S POOL/BGL ACCOUNT
      </td>

      <td>
        UNABLE\_TO\_PROCESS\_DEBIT\_IN\_BANK\_S\_POOL\_BGL\_ACCOUNT
      </td>
    </tr>

    <tr>
      <td>
        E4102
      </td>

      <td>
        Transaction failed due to customer not\
         notified of the transaction
      </td>

      <td>
        Unable to Notify the Customer
      </td>

      <td>
        Unable\_To\_Notify\_The\_Customer
      </td>
    </tr>

    <tr>
      <td>
        E9211
      </td>

      <td>
        Unable to Locate Record on File
      </td>

      <td>
        Unable to Locate Record on File
      </td>

      <td>
        UNABLE\_TO\_LOCATE\_RECORD\_ON\_FILE
      </td>
    </tr>

    <tr>
      <td>
        E9225
      </td>

      <td>
        Unable to Dispense
      </td>

      <td>
        Unable to Dispense
      </td>

      <td>
        UNABLE\_TO\_DISPENSE
      </td>
    </tr>

    <tr>
      <td>
        E9240
      </td>

      <td>
        Unable to Authorise
      </td>

      <td>
        Unable to Authorise
      </td>

      <td>
        UNABLE\_TO\_AUTHORISE
      </td>
    </tr>

    <tr>
      <td>
        E4114
      </td>

      <td>
        Transaction failed as umn details doesn't\
         exist at customer's end
      </td>

      <td>
        UMN DOES NOT EXIST (PAYER)
      </td>

      <td>
        UMN\_DOES\_NOT\_EXIST\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4128
      </td>

      <td>
        Transaction failed as umn details doesn't\
         exist at acquiring bank's end
      </td>

      <td>
        UMN DOES NOT EXIST (PAYEE)
      </td>

      <td>
        UMN\_DOES\_NOT\_EXIST\_PAYEE
      </td>
    </tr>

    <tr>
      <td>
        E4227
      </td>

      <td>
        UIDAI FAILURE
      </td>

      <td>
        UIDAI FAILURE
      </td>

      <td>
        UIDAI\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E2101
      </td>

      <td>
        Transaction could not be processed\
         because offer is not applicable.
      </td>

      <td>
        TXN\_FAILURE\_FOR  

        * INVALID\_OFFER
      </td>

      <td>
        TXN\_FAILURE\_FOR\_INVALID\_OFFER
      </td>
    </tr>

    <tr>
      <td>
        E2201
      </td>

      <td>
        splitRequest param sent for\
         non-aggregator merchant
      </td>

      <td>
        TXN\_FAILED\_AGGREGATOR  

        * TXN\_NOT\_ALLOWED
      </td>

      <td>
        TXN\_FAILED\_AGGREGATOR\_TXN\_NOT\_ALLOWED
      </td>
    </tr>

    <tr>
      <td>
        E2202
      </td>

      <td>
        Invalid split provided in transaction request.
      </td>

      <td>
        TXN\_FAILED\_AGGREGATOR  

        * INVALID\_SPLIT\_PROVIDED
      </td>

      <td>
        TXN\_FAILED\_AGGREGATOR\_INVALID\_SPLIT\_PROVIDED
      </td>
    </tr>

    <tr>
      <td>
        E1101
      </td>

      <td>
        Transaction failed due to invalid params\
         shared by the merchant
      </td>

      <td>
        TXN\_DETAIL\_INVALID  

        * REDIRECTING\_TO\_MERCHANT
      </td>

      <td>
        TXN\_DETAIL\_INVALID\_REDIRECTING\_TO\_MERCHANT
      </td>
    </tr>

    <tr>
      <td>
        E4112
      </td>

      <td>
        Transaction failed as mandate and transaction\
         amount is different
      </td>

      <td>
        TXN AMOUNT DIFFERS FROM MANDATE AMOUNT
      </td>

      <td>
        TXN\_AMOUNT\_DIFFERS\_FROM\_MANDATE\_AMOUNT
      </td>
    </tr>

    <tr>
      <td>
        E9234
      </td>

      <td>
        TVR validation failed by Issuer
      </td>

      <td>
        TVR validation failed by Issuer
      </td>

      <td>
        TVR\_VALIDATION\_FAILED\_BY\_ISSUER
      </td>
    </tr>

    <tr>
      <td>
        E227
      </td>

      <td>
        Transaction is Pending
      </td>

      <td>
        TRANSACTION\_PENDING
      </td>

      <td>
        TRANSACTION\_PENDING
      </td>
    </tr>

    <tr>
      <td>
        E306
      </td>

      <td>
        Card authentication failure
      </td>

      <td>
        TRANSACTION\_INVALID\_PG
      </td>

      <td>
        TRANSACTION\_INVALID\_PG
      </td>
    </tr>

    <tr>
      <td>
        E229
      </td>

      <td>
        Transaction declined as no prior EMI\
         transaction exists here
      </td>

      <td>
        TRANSACTION\_INVALID  

        * EMI\_BASE\_ID
      </td>

      <td>
        TRANSACTION\_INVALID\_EMI\_BASE\_ID
      </td>
    </tr>

    <tr>
      <td>
        E308
      </td>

      <td>
        Transaction Failed at bank end.
      </td>

      <td>
        TRANSACTION\_FAILED
      </td>

      <td>
        TRANSACTION\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E507
      </td>

      <td>
        Transaction Expired
      </td>

      <td>
        TRANSACTION\_EXPIRED
      </td>

      <td>
        TRANSACTION\_EXPIRED
      </td>
    </tr>

    <tr>
      <td>
        E231
      </td>

      <td>
        Transaction was marked as dropped
      </td>

      <td>
        TRANSACTION\_DROPPED
      </td>

      <td>
        TRANSACTION\_DROPPED
      </td>
    </tr>

    <tr>
      <td>
        E408
      </td>

      <td>
        Transaction failed. Page expired due to no user input.
      </td>

      <td>
        TRANSACTION\_BOUNCED
      </td>

      <td>
        TRANSACTION\_BOUNCED
      </td>
    </tr>

    <tr>
      <td>
        E345
      </td>

      <td>
        Transaction declined due to technical failure
      </td>

      <td>
        Transaction rejected
      </td>

      <td>
        TECHNICAL\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E4374
      </td>

      <td>
        Transaction not allowed on VPA by customer application
      </td>

      <td>
        TRANSACTION NOT PERMITTED TO VPA by the PSP
      </td>

      <td>
        TRANSACTION\_NOT\_PERMITTED\_TO\_VPA\_By\_The\_PSP
      </td>
    </tr>

    <tr>
      <td>
        E4010
      </td>

      <td>
        Transaction not allowed on/from the account
      </td>

      <td>
        TRANSACTION NOT PERMITTED TO THE ACCOUNT
      </td>

      <td>
        TRANSACTION\_NOT\_PERMITTED\_TO\_THE\_ACCOUNT
      </td>
    </tr>

    <tr>
      <td>
        E1642
      </td>

      <td>
        Transaction not permitted to cardholder
      </td>

      <td>
        Transaction not permitted to issuer/cardholder
      </td>

      <td>
        CARD\_NOT\_PERMITTED
      </td>
    </tr>

    <tr>
      <td>
        E4375
      </td>

      <td>
        TRANSACTION NOT PERMITTED\
         TO DEVICE
      </td>

      <td>
        TRANSACTION NOT PERMITTED TO DEVICE
      </td>

      <td>
        TRANSACTION\_NOT\_PERMITTED\_TO\_DEVICE
      </td>
    </tr>

    <tr>
      <td>
        E4348
      </td>

      <td>
        TRANSACTION NOT PERMITTED TO\
         CARDHOLDER (REMITTER)
      </td>

      <td>
        Transaction not permitted to cardholder
      </td>

      <td>
        TRANSACTION\_NOT\_PERMITTED\_TO\_CARDHOLDER\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4146
      </td>

      <td>
        Transaction not allowed from overdraft account
      </td>

      <td>
        TRANSACTION NOT PERMITTED FOR THIS A/C TYPE (OD)
      </td>

      <td>
        TRANSACTION\_NOT\_PERMITTED\_FOR\_THIS\_A\_C\_TYPE\_OD
      </td>
    </tr>

    <tr>
      <td>
        E4931
      </td>

      <td>
        Transaction is in <value> state
      </td>

      <td>
        Transaction is in <value> state
      </td>

      <td>
        Transaction\_Is\_In\_Value\_State
      </td>
    </tr>

    <tr>
      <td>
        E4188
      </td>

      <td>
        TRANSACTION IS ALREADY BEEN FAILED
      </td>

      <td>
        TRANSACTION IS ALREADY BEEN FAILED
      </td>

      <td>
        TRANSACTION\_IS\_ALREADY\_BEEN\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E4197
      </td>

      <td>
        Transaction failed as original transaction\
         details not found during status check
      </td>

      <td>
        TRANSACTION ID IS NOT PRESENT
      </td>

      <td>
        TRANSACTION\_ID\_IS\_NOT\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4155
      </td>

      <td>
        TRANSACTION ID IS MISMATCHED\
         VALIDATION ERROR
      </td>

      <td>
        TRANSACTION ID IS MISMATCHED VALIDATION ERROR
      </td>

      <td>
        TRANSACTION\_ID\_IS\_MISMATCHED\_VALIDATION\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4369
      </td>

      <td>
        Transaction declined as count of transactions\
         increased as set by customer's bank
      </td>

      <td>
        TRANSACTION FREQUENCY LIMIT EXCEEDED AS SET BY REMITTING MEMBER
      </td>

      <td>
        TRANSACTION\_FREQUENCY\_LIMIT\_EXCEEDED\_AS\_SET\_BY\_REMITTING\_MEMBER\_BD
      </td>
    </tr>

    <tr>
      <td>
        E1655
      </td>

      <td>
        Transaction could not be completed due to violation of law
      </td>

      <td>
        TRANSACTION CANNOT BE COMPLETED. COMPLIANCE VIOLATION (REMITTER)
      </td>

      <td>
        DECLINING\_DUE\_TO\_VOILATION\_OF\_LAW
      </td>
    </tr>

    <tr>
      <td>
        E217
      </td>

      <td>
        This error comes when Bank does some changes\
         in the terminal/plug-in profile of the merchant.\
        If merchant receives this error Bank should generate\
         new resource file and forward the same to the merchant.
      </td>

      <td>
        TRANPORTAL\_ID\_ERROR
      </td>

      <td>
        TRANPORTAL\_ID\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E1911
      </td>

      <td>
        User entered wrong VPA too many times
      </td>

      <td>
        TOO\_MANY\_WRONG\_VPA
      </td>

      <td>
        TOO\_MANY\_WRONG\_VPA
      </td>
    </tr>

    <tr>
      <td>
        E9226
      </td>

      <td>
        TID not present on host
      </td>

      <td>
        TID not present on host
      </td>

      <td>
        TID\_NOT\_PRESENT\_ON\_HOST
      </td>
    </tr>

    <tr>
      <td>
        E4516
      </td>

      <td>
        Refund failed as original transaction details not valid
      </td>

      <td>
        This transaction is already processed ("ICICI", Online duplicate
      </td>

      <td>
        This\_Transaction\_Is\_Already\_Processed\_ICICI\_Online\_Duplicate\_Transaction
      </td>
    </tr>

    <tr>
      <td>
        E4119
      </td>

      <td>
        Revoke is not allowed for this mandate
      </td>

      <td>
        THIS MANDATE IS NON REVOKEABLE BD
      </td>

      <td>
        THIS\_MANDATE\_IS\_NON\_REVOKEABLE\_BD
      </td>
    </tr>

    <tr>
      <td>
        E4150
      </td>

      <td>
        Transaction declined due to duplicate request
      </td>

      <td>
        THE REQUEST IS DUPLICATE
      </td>

      <td>
        THE\_REQUEST\_IS\_DUPLICATE
      </td>
    </tr>

    <tr>
      <td>
        E223
      </td>

      <td>
        Transaction not approved
      </td>

      <td>
        The order has been rejected by Decision Manager
      </td>

      <td>
        TRANSACTION\_REJECTED\_BY\_CHECKER
      </td>
    </tr>

    <tr>
      <td>
        E338
      </td>

      <td>
        Transaction denied because one or more risk rules failed
      </td>

      <td>
        The customer matched the Denied Parties List
      </td>

      <td>
        RISK\_RULE\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E335
      </td>

      <td>
        Transaction failed due to incomplete authentication process
      </td>

      <td>
        The cardholder is enrolled in Payer Authentication. Please authe
      </td>

      <td>
        AUTHENTICATION\_INCOMPLETE
      </td>
    </tr>

    <tr>
      <td>
        E2405
      </td>

      <td>
        Sorry, you are not eligible for the selected tenure. Please select another tenure
      </td>

      <td>
        TENURE\_NOT\_FOUND
      </td>

      <td>
        TENURE\_NOT\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E4157
      </td>

      <td>
        SYSTEM EXCEPTION
      </td>

      <td>
        SYSTEM EXCEPTION
      </td>

      <td>
        SYSTEM\_EXCEPTION
      </td>
    </tr>

    <tr>
      <td>
        E4004
      </td>

      <td>
        SUSPECTED FRAUD, DECLINE/TRANSACTIONS\
        DECLINED BASED ON RISKSCORE BY REMITTER
      </td>

      <td>
        SUSPECTED\_FRAUD\_DECLINE\_TRANSACTIONS\_DECLINED\_BASED\_ON\_RISKSCORE\_BY\_REMITTER
      </td>

      <td>
        SUSPECTED\_FRAUD\_DECLINE\_TRANSACTIONS\_DECLINED\_BASED\_ON\_RISKSCORE\_BY\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E9208
      </td>

      <td>
        Suspected Malfunction
      </td>

      <td>
        Suspected Malfunction
      </td>

      <td>
        SUSPECTED\_MALFUNCTION
      </td>
    </tr>

    <tr>
      <td>
        E4378
      </td>

      <td>
        Transaction declined due to risk score by beneficiary bank
      </td>

      <td>
        SUSPECTED FRAUD, DECLINE / TRANSACTIONS DECLINED BASED ON RISK S
      </td>

      <td>
        SUSPECTED\_FRAUD\_DECLINE\_TRANSACTIONS\_DECLINED\_BASED\_ON\_RISK\_SCORE\_BY\_BD\_BENEFICIARY
      </td>
    </tr>

    <tr>
      <td>
        E1611
      </td>

      <td>
        UserCancelled as the Transaction was left orphan during sure\_pay
      </td>

      <td>
        SURE\_PAY\_USER\_CANCELLED
      </td>

      <td>
        SURE\_PAY\_USER\_CANCELLED
      </td>
    </tr>

    <tr>
      <td>
        E1613
      </td>

      <td>
        SurePay usercancelled
      </td>

      <td>
        SURE\_PAY\_PROCESSED
      </td>

      <td>
        SURE\_PAY\_PROCESSED
      </td>
    </tr>

    <tr>
      <td>
        E1657
      </td>

      <td>
        Surcharge amount not permitted
      </td>

      <td>
        SURCHARGE\_AMOUNT\_NOT\_PERMITTED
      </td>

      <td>
        SURCHARGE\_AMOUNT\_NOT\_PERMITTED
      </td>
    </tr>

    <tr>
      <td>
        E000
      </td>

      <td>
        No Error
      </td>

      <td>
        Successful transaction
      </td>

      <td>
        NO\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E1631
      </td>

      <td>
        Merchant Validation Failed
      </td>

      <td>
        Sorry! Transaction could not be processed as the limit of your m
      </td>

      <td>
        MERCHANT\_VALIDATION\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E1630
      </td>

      <td>
        Invalid Bank ME Code
      </td>

      <td>
        Sorry! Transaction could not be processed as limit is exhausted
      </td>

      <td>
        INVALID\_BANK\_ME\_CODE
      </td>
    </tr>

    <tr>
      <td>
        E4520
      </td>

      <td>
        Refund failed as online refund not enabled on merchant
      </td>

      <td>
        Sorry you canNULLt initiate refund request
      </td>

      <td>
        Sorry\_You\_Cant\_Initiate\_Refund\_Request
      </td>
    </tr>

    <tr>
      <td>
        E337
      </td>

      <td>
        Transaction declined by the issuer
      </td>

      <td>
        Soft Decline - The authorization request was approved by the iss
      </td>

      <td>
        NOT\_CAPTURED
      </td>
    </tr>

    <tr>
      <td>
        E4025
      </td>

      <td>
        SIGNATURE MISMATCH
      </td>

      <td>
        SIGNATURE MISMATCH
      </td>

      <td>
        SIGNATURE\_MISMATCH
      </td>
    </tr>

    <tr>
      <td>
        E4024
      </td>

      <td>
        SIGNATURE ERROR
      </td>

      <td>
        SIGNATURE ERROR
      </td>

      <td>
        SIGNATURE\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4093
      </td>

      <td>
        SHARETOPAYEE=Y FOR PAYER\
         INITIATED IF PURPOSE=01
      </td>

      <td>
        SHARETOPAYEE=Y FOR PAYER INITIATED IF PURPOSE=01
      </td>

      <td>
        SHARETOPAYEE\_Y\_FOR\_PAYER\_INITIATED\_IF\_PURPOSE\_01
      </td>
    </tr>

    <tr>
      <td>
        E1658
      </td>

      <td>
        Service not available
      </td>

      <td>
        SERVICE\_NOT\_AVAILABLE
      </td>

      <td>
        SERVICE\_NOT\_AVAILABLE
      </td>
    </tr>

    <tr>
      <td>
        E1201
      </td>

      <td>
        You are not authorized to do this transaction.
      </td>

      <td>
        SERVICE\_AUTHORIZATION\_ERROR
      </td>

      <td>
        SERVICE\_AUTHORIZATION\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4147
      </td>

      <td>
        Transaction failed as customer is not active on UPI
      </td>

      <td>
        Service disable on UPI/ Customer is not active
      </td>

      <td>
        Service\_Disable\_On\_UPI\_\_Customer\_is\_Not\_Active
      </td>
    </tr>

    <tr>
      <td>
        E4105
      </td>

      <td>
        Transaction failed due to recurring sequence mismatch
      </td>

      <td>
        SEQNUM MISMATCH (PAYER PSP)
      </td>

      <td>
        SEQNUM\_MISMATCH\_PAYER\_PSP
      </td>
    </tr>

    <tr>
      <td>
        E1633
      </td>

      <td>
        Separate Authentication Failed
      </td>

      <td>
        SEPARATE\_AUTHENTICATION\_FAILED
      </td>

      <td>
        SEPARATE\_AUTHENTICATION\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E1663
      </td>

      <td>
        Failure received in send OTP API call
      </td>

      <td>
        SEND\_OTP\_API\_FAILURE
      </td>

      <td>
        SEND\_OTP\_API\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E1670
      </td>

      <td>
        Card authentication failed at the bank\
         due to invalid CVV (or CVC or Card Security Code)
      </td>

      <td>
        Security violation
      </td>

      <td>
        ISSUER\_RISK\_RULE\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E700
      </td>

      <td>
        Validation of secure hash failed
      </td>

      <td>
        SECURE\_HASH\_FAILURE
      </td>

      <td>
        SECURE\_HASH\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E300
      </td>

      <td>
        Card failed 3D authentication as 3 D Secure signatures did not match
      </td>

      <td>
        SECURE\_3D\_PASSWORD\_ERROR
      </td>

      <td>
        SECURE\_3D\_PASSWORD\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E1000
      </td>

      <td>
        3-D secure authentication failed.
      </td>

      <td>
        SECURE\_3D\_AUTHENTICATION\_ERROR\_S3A
      </td>

      <td>
        SECURE\_3D\_AUTHENTICATION\_ERROR\_S3A
      </td>
    </tr>

    <tr>
      <td>
        E317
      </td>

      <td>
        Payer could not be authenticated
      </td>

      <td>
        SECURE\_3D\_AUTHENTICATION\_ERROR
      </td>

      <td>
        SECURE\_3D\_AUTHENTICATION\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E1662
      </td>

      <td>
        ATM PIN monthly limit exceeded for this card.\
         Please retry using OTP or any other payment option.
      </td>

      <td>
        SBI\_DI\_MONTHLY\_CARD\_LIMIT\_EXCEEDED
      </td>

      <td>
        SBI\_DI\_MONTHLY\_CARD\_LIMIT\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E1661
      </td>

      <td>
        ATM PIN daily limit exceeded for this card.\
         Please retry using OTP or any other payment option.
      </td>

      <td>
        SBI\_DI\_DAILY\_CARD\_LIMIT\_EXCEEDED
      </td>

      <td>
        SBI\_DI\_DAILY\_CARD\_LIMIT\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E1664
      </td>

      <td>
        Card blocked by the issuer.\
        Please contact the bank to get it enabled for online transactions.
      </td>

      <td>
        SBI\_DI\_BLOCKED\_CARD
      </td>

      <td>
        SBI\_DI\_BLOCKED\_CARD
      </td>
    </tr>

    <tr>
      <td>
        E1615
      </td>

      <td>
        txn\_s2s\_flow missing parameter
      </td>

      <td>
        S2S\_PARAMETER\_MISSING
      </td>

      <td>
        S2S\_PARAMETER\_MISSING
      </td>
    </tr>

    <tr>
      <td>
        E1622
      </td>

      <td>
        S2S flow not enabled on selected payment gateway
      </td>

      <td>
        S2S\_NOT\_ENABLED\_PAYMENTGATEWAY
      </td>

      <td>
        S2S\_NOT\_ENABLED\_PAYMENTGATEWAY
      </td>
    </tr>

    <tr>
      <td>
        E1621
      </td>

      <td>
        Merchant does not have access to S2S flow
      </td>

      <td>
        S2S\_NOT\_ENABLED\_MERCHANT
      </td>

      <td>
        S2S\_NOT\_ENABLED\_MERCHANT
      </td>
    </tr>

    <tr>
      <td>
        E199
      </td>

      <td>
        Rreq not received from the Network Scheme
      </td>

      <td>
        RREQ\_NOT\_RECEIVED
      </td>

      <td>
        RREQ\_NOT\_RECEIVED
      </td>
    </tr>

    <tr>
      <td>
        E1654
      </td>

      <td>
        Route to merchant unavailable
      </td>

      <td>
        ROUTE\_UNAVAILABLE
      </td>

      <td>
        ROUTE\_UNAVAILABLE
      </td>
    </tr>

    <tr>
      <td>
        E4034
      </td>

      <td>
        REVOKE MANDATE AFTER THE REMITTER\
         UNBLOCKED THE AMOUNT
      </td>

      <td>
        REVOKE MANDATE AFTER THE REMITTER UNBLOCKED THE AMOUNT
      </td>

      <td>
        REVOKE\_MANDATE\_AFTER\_THE\_REMITTER\_UNBLOCKED\_THE\_AMOUNT
      </td>
    </tr>

    <tr>
      <td>
        E4183
      </td>

      <td>
        REVERTED
      </td>

      <td>
        REVERTED
      </td>

      <td>
        REVERTED
      </td>
    </tr>

    <tr>
      <td>
        E4186
      </td>

      <td>
        REVERSAL HAS BEEN SENT
      </td>

      <td>
        REVERSAL HAS BEEN SENT
      </td>

      <td>
        REVERSAL\_HAS\_BEEN\_SENT
      </td>
    </tr>

    <tr>
      <td>
        E1500
      </td>

      <td>
        Retry not allowed
      </td>

      <td>
        RETRY\_NOT\_ALLOWED
      </td>

      <td>
        RETRY\_NOT\_ALLOWED
      </td>
    </tr>

    <tr>
      <td>
        E1626
      </td>

      <td>
        Restricted card
      </td>

      <td>
        RESTRICTED CARD, DECLINE (REMITTER)
      </td>

      <td>
        RESTRICTED\_CARD\_TYPE
      </td>
    </tr>

    <tr>
      <td>
        E4268
      </td>

      <td>
        Response ValQR TimeOut
      </td>

      <td>
        Response ValQR TimeOut
      </td>

      <td>
        Response\_ValQR\_TimeOut
      </td>
    </tr>

    <tr>
      <td>
        E9220
      </td>

      <td>
        Response Received Too Late
      </td>

      <td>
        Response Received Too Late
      </td>

      <td>
        RESPONSE\_RECEIVED\_TOO\_LATE
      </td>
    </tr>

    <tr>
      <td>
        E4187
      </td>

      <td>
        RESPONSE IS ALREADY BEEN SENT
      </td>

      <td>
        RESPONSE IS ALREADY BEEN SENT
      </td>

      <td>
        RESPONSE\_IS\_ALREADY\_BEEN\_SENT
      </td>
    </tr>

    <tr>
      <td>
        E4184
      </td>

      <td>
        RESPONSE IS ALREADY BEEN RECEIVED
      </td>

      <td>
        RESPONSE IS ALREADY BEEN RECEIVED
      </td>

      <td>
        RESPONSE\_IS\_ALREADY\_BEEN\_RECEIVED
      </td>
    </tr>

    <tr>
      <td>
        E4267
      </td>

      <td>
        Response Activation TimeOut
      </td>

      <td>
        Response Activation TimeOut
      </td>

      <td>
        Response\_Activation\_TimeOut
      </td>
    </tr>

    <tr>
      <td>
        E4279
      </td>

      <td>
        Transaction declined due to timeout\
         at customer's bank
      </td>

      <td>
        RESPMANDATE TIMEOUT AT REMITTER END
      </td>

      <td>
        RESPMANDATE\_TIMEOUT\_AT\_REMITTER\_END
      </td>
    </tr>

    <tr>
      <td>
        E4278
      </td>

      <td>
        Transaction failed as mandate setup\
         failed from customer's bank
      </td>

      <td>
        RESPMANDATE DECLINED BY REMITTER BANK
      </td>

      <td>
        RESPMANDATE\_DECLINED\_BY\_REMITTER\_BANK
      </td>
    </tr>

    <tr>
      <td>
        E4283
      </td>

      <td>
        RESPMANDATE ACK NOT RECEIVED\
         FROM PAYER
      </td>

      <td>
        RESPMANDATE ACK NOT RECEIVED FROM PAYER
      </td>

      <td>
        RESPMANDATE\_ACK\_NOT\_RECEIVED\_FROM\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4272
      </td>

      <td>
        Transaction declined due to timeout\
         at Issuer/Acquirer end
      </td>

      <td>
        RESPAUTHMANDATE TIMEOUT
      </td>

      <td>
        RESPAUTHMANDATE\_TIMEOUT
      </td>
    </tr>

    <tr>
      <td>
        E4275
      </td>

      <td>
        RESPAUTHMANDATE NEGATIVE\
         ACK SENT FROM UPI TO PSP
      </td>

      <td>
        RESPAUTHMANDATE NEGATIVE ACK SENT FROM UPI TO PSP
      </td>

      <td>
        RESPAUTHMANDATE\_NEGATIVE\_ACK\_SENT\_FROM\_UPI\_TO\_PSP
      </td>
    </tr>

    <tr>
      <td>
        E4273
      </td>

      <td>
        Transaction failed due to mandate request expired
      </td>

      <td>
        RESPAUTHMANDATE EXPIRED
      </td>

      <td>
        RESPAUTHMANDATE\_EXPIRED
      </td>
    </tr>

    <tr>
      <td>
        E4271
      </td>

      <td>
        Mandate request declined by the customer
      </td>

      <td>
        RESPAUTHMANDATE DECLINED BY PSP
      </td>

      <td>
        RESPAUTHMANDATE\_DECLINED\_BY\_PSP
      </td>
    </tr>

    <tr>
      <td>
        E215
      </td>

      <td>
        Unknown Error
      </td>

      <td>
        RESERVED\_USAGE\_ERROR
      </td>

      <td>
        RESERVED\_USAGE\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E9231
      </td>

      <td>
        Reserved for National Use
      </td>

      <td>
        Reserved for National Use
      </td>

      <td>
        RESERVED\_FOR\_NATIONAL\_USE
      </td>
    </tr>

    <tr>
      <td>
        E4342
      </td>

      <td>
        REQUESTED FUNCTION NOT\
         SUPPORTED (REMITTER)
      </td>

      <td>
        REQUESTED FUNCTION NOT SUPPORTED (REMITTER)
      </td>

      <td>
        REQUESTED\_FUNCTION\_NOT\_SUPPORTED\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4343
      </td>

      <td>
        REQUESTED FUNCTION NOT\
         SUPPORTED (BENEFICIARY)
      </td>

      <td>
        REQUESTED FUNCTION NOT SUPPORTED (BENEFICIARY)
      </td>

      <td>
        REQUESTED\_FUNCTION\_NOT\_SUPPORTED\_BENEFICIARY
      </td>
    </tr>

    <tr>
      <td>
        E9218
      </td>

      <td>
        Requested Function not Supported
      </td>

      <td>
        Requested Function not Supported
      </td>

      <td>
        REQUESTED\_FUNCTION\_NOT\_SUPPORTED
      </td>
    </tr>

    <tr>
      <td>
        E4200
      </td>

      <td>
        REQUEST REFUND IS NOT FOUND
      </td>

      <td>
        REQUEST REFUND IS NOT FOUND
      </td>

      <td>
        REQUEST\_REFUND\_IS\_NOT\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E4605
      </td>

      <td>
        Request Processed Successfully
      </td>

      <td>
        Request Processed Successfully
      </td>

      <td>
        Request\_Processed\_Successfully
      </td>
    </tr>

    <tr>
      <td>
        E4198
      </td>

      <td>
        REQUEST MESSAGE ID IS NOT PRESENT
      </td>

      <td>
        REQUEST MESSAGE ID IS NOT PRESENT
      </td>

      <td>
        REQUEST\_MESSAGE\_ID\_IS\_NOT\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4153
      </td>

      <td>
        REQUEST IS NOT FOUND
      </td>

      <td>
        REQUEST IS NOT FOUND
      </td>

      <td>
        REQUEST\_IS\_NOT\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E4185
      </td>

      <td>
        REQUEST IS ALREADY BEEN SENT
      </td>

      <td>
        REQUEST IS ALREADY BEEN SENT
      </td>

      <td>
        REQUEST\_IS\_ALREADY\_BEEN\_SENT
      </td>
    </tr>

    <tr>
      <td>
        E4608
      </td>

      <td>
        Request has been timed out
      </td>

      <td>
        Request has been timed out
      </td>

      <td>
        Request\_Has\_Been\_Timed\_Out
      </td>
    </tr>

    <tr>
      <td>
        E4517
      </td>

      <td>
        Offline Refund request already raised
      </td>

      <td>
        Request has already been initiated for this transaction ("ICICI"
      </td>

      <td>
        Request\_Has\_Already\_Been\_Initiated\_For\_This\_Transaction\_ICICI\_Offline\_Duplicate\_Transaction
      </td>
    </tr>

    <tr>
      <td>
        E4140
      </td>

      <td>
        Transaction declined by the bank
      </td>

      <td>
        Request Decline by the bank
      </td>

      <td>
        Request\_Decline\_By\_The\_Bank
      </td>
    </tr>

    <tr>
      <td>
        E4196
      </td>

      <td>
        REQUEST DEBIT IS NOT FOUND
      </td>

      <td>
        REQUEST DEBIT IS NOT FOUND
      </td>

      <td>
        REQUEST\_DEBIT\_IS\_NOT\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E4195
      </td>

      <td>
        REQUEST CREDIT IS NOT FOUND
      </td>

      <td>
        REQUEST CREDIT IS NOT FOUND
      </td>

      <td>
        REQUEST\_CREDIT\_IS\_NOT\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E4170
      </td>

      <td>
        REQUEST AUTHORISATION IS NOT FOUND
      </td>

      <td>
        REQUEST AUTHORISATION IS NOT FOUND
      </td>

      <td>
        REQUEST\_AUTHORISATION\_IS\_NOT\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E4167
      </td>

      <td>
        Transaction failed as authorisation\
        acknowledgement not received
      </td>

      <td>
        REQUEST AUTHORISATION ACKNOWLEDGEMENT IS NOT
      </td>

      <td>
        REQUEST\_AUTHORISATION\_ACKNOWLEDGEMENT\_IS\_NOT
      </td>
    </tr>

    <tr>
      <td>
        E4284
      </td>

      <td>
        REQMANDATECONFIRMATION ACK\
         NOT RECEIVED FROM PAYER
      </td>

      <td>
        REQMANDATECONFIRMATION ACK NOT RECEIVED FROM PAYER
      </td>

      <td>
        REQMANDATECONFIRMATION\_ACK\_NOT\_RECEIVED\_FROM\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4280
      </td>

      <td>
        REQMANDATE NEGATIVE ACK\
         RECEIVED FROM REMITTER
      </td>

      <td>
        REQMANDATE NEGATIVE ACK RECEIVED FROM REMITTER
      </td>

      <td>
        REQMANDATE\_NEGATIVE\_ACK\_RECEIVED\_FROM\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4277
      </td>

      <td>
        REQMANDATE ACK NOT RECEIVED\
         FROM REMITTER BANK
      </td>

      <td>
        REQMANDATE ACK NOT RECEIVED FROM REMITTER BANK
      </td>

      <td>
        REQMANDATE\_ACK\_NOT\_RECEIVED\_FROM\_REMITTER\_BANK
      </td>
    </tr>

    <tr>
      <td>
        E4274
      </td>

      <td>
        REQAUTHMANDATE NEGATIVE\
         ACK RECEIVED FROM PSP
      </td>

      <td>
        REQAUTHMANDATE NEGATIVE ACK RECEIVED FROM PSP
      </td>

      <td>
        REQAUTHMANDATE\_NEGATIVE\_ACK\_RECEIVED\_FROM\_PSP
      </td>
    </tr>

    <tr>
      <td>
        E4363
      </td>

      <td>
        Transaction declined due to\
         customer's account blocked or frozen
      </td>

      <td>
        REMITTING ACCOUNT BLOCKED/FROZEN
      </td>

      <td>
        REMITTING\_ACCOUNT\_BLOCKED\_FROZEN
      </td>
    </tr>

    <tr>
      <td>
        E4294
      </td>

      <td>
        Transaction declined due to\
         timeout at Issuer/Customer's end
      </td>

      <td>
        REMITTER/ISSUER UNAVAILABLE (TIMEOUT)
      </td>

      <td>
        REMITTER\_ISSUER\_UNAVAILABLE\_TIMEOUT
      </td>
    </tr>

    <tr>
      <td>
        E4357
      </td>

      <td>
        Transaction failed due to\
        customer's bank CBS offline
      </td>

      <td>
        REMITTER CBS OFFLINE
      </td>

      <td>
        REMITTER\_CBS\_OFFLINE
      </td>
    </tr>

    <tr>
      <td>
        E4258
      </td>

      <td>
        REMITTER BANK,VERSION/TAGS\
         SENT NOT SUPPORTED BY BANK
      </td>

      <td>
        REMITTER BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK
      </td>

      <td>
        REMITTER\_BANK\_VERSION\_TAGS\_SENT\_NOT\_SUPPORTED\_BY\_BANK
      </td>
    </tr>

    <tr>
      <td>
        E4256
      </td>

      <td>
        REMITTER BANK,REQUEST\
         & RESPONSE HEADER VERSION MISMATCH
      </td>

      <td>
        REMITTER BANK,REQUEST & RESPONSE HEADER VERSION MISMATCH
      </td>

      <td>
        REMITTER\_BANK\_REQUEST\_RESPONSE\_HEADER\_VERSION\_MISMATCH
      </td>
    </tr>

    <tr>
      <td>
        E4257
      </td>

      <td>
        REMITTER BANK,HEADER\
         OR URL VERSION MISMATCHED
      </td>

      <td>
        REMITTER BANK,HEADER OR URL VERSION MISMATCHED
      </td>

      <td>
        REMITTER\_BANK\_HEADER\_OR\_URL\_VERSION\_MISMATCHED
      </td>
    </tr>

    <tr>
      <td>
        E4290
      </td>

      <td>
        Mandate not supported by customer's bank
      </td>

      <td>
        REMITTER BANK NOT REGISTERED (MANDATE)
      </td>

      <td>
        REMITTER\_BANK\_NOT\_REGISTERED\_MANDATE
      </td>
    </tr>

    <tr>
      <td>
        E4177
      </td>

      <td>
        Debit failed due to technical issue at customer's bank
      </td>

      <td>
        REMITTER BANK NOT AVAILABLE
      </td>

      <td>
        REMITTER\_BANK\_NOT\_AVAILABLE
      </td>
    </tr>

    <tr>
      <td>
        E4096
      </td>

      <td>
        REMITTER BANK DOES NOT\
         SUPPORT VERSION MANDATE 2.1
      </td>

      <td>
        REMITTER BANK DOES NOT SUPPORT VERSION MANDATE 2.1
      </td>

      <td>
        REMITTER\_BANK\_DOES\_NOT\_SUPPORT\_VERSION\_MANDATE\_2\_1
      </td>
    </tr>

    <tr>
      <td>
        E4265
      </td>

      <td>
        REMITTER BANK DOES NOT\
         SUPPORT VERSION
      </td>

      <td>
        REMITTER BANK DOES NOT SUPPORT VERSION
      </td>

      <td>
        REMITTER\_BANK\_DOES\_NOT\_SUPPORT\_VERSION
      </td>
    </tr>

    <tr>
      <td>
        E4009
      </td>

      <td>
        Transaction failed due to mobile\
         number linked to account is changed
      </td>

      <td>
        REGISTERED MOBILE NUMBER LINKED TO THE ACCOUNT HAS BEEN CHANGED/
      </td>

      <td>
        REGISTERED\_MOBILE\_NUMBER\_LINKED\_TO\_THE\_ACCOUNT\_HAS\_BEEN\_CHANGED\_REMOVED
      </td>
    </tr>

    <tr>
      <td>
        E348
      </td>

      <td>
        Transaction declined by the issuer
      </td>

      <td>
        Refer to card issuer
      </td>

      <td>
        ISSUER\_DECLINED
      </td>
    </tr>

    <tr>
      <td>
        E4649
      </td>

      <td>
        Ref Url is not valid or proper format. e.g. [http://www.yyy.zzz](http://www.yyy.zzz)
      </td>

      <td>
        Ref Url is not valid or proper format. e.g. [http://www.yyy.zzz](http://www.yyy.zzz)
      </td>

      <td>
        Ref\_Url\_Is\_Not\_Valid\_Or\_Proper\_Format
      </td>
    </tr>

    <tr>
      <td>
        E1206
      </td>

      <td>
        Transaction interrupted by pressing back button
      </td>

      <td>
        REDIRECTED\_BY\_BACK\_BUTTON
      </td>

      <td>
        REDIRECTED\_BY\_BACK\_BUTTON
      </td>
    </tr>

    <tr>
      <td>
        E4682
      </td>

      <td>
        Recurrence Payment is in progress
      </td>

      <td>
        Recurrence Payment is in progress
      </td>

      <td>
        Recurrence\_Payment\_Is\_In\_Progress
      </td>
    </tr>

    <tr>
      <td>
        E4683
      </td>

      <td>
        Recurrence Payment is already completed
      </td>

      <td>
        Recurrence Payment is already completed
      </td>

      <td>
        Recurrence\_Payment\_Is\_Already\_Completed
      </td>
    </tr>

    <tr>
      <td>
        E4091
      </td>

      <td>
        RECURRENCE PATTERN IS\
        ALWAYS ONETIME IF PURPOSE=01
      </td>

      <td>
        RECURRENCE PATTERN IS ALWAYS ONETIME IF PURPOSE=01
      </td>

      <td>
        RECURRENCE\_PATTERN\_IS\_ALWAYS\_ONETIME\_IF\_PURPOSE\_01
      </td>
    </tr>

    <tr>
      <td>
        E4063
      </td>

      <td>
        RECURRENCE PATTERN AS\
         WELL AS FOR PAYER INITIATED
      </td>

      <td>
        RECURRENCE PATTERN AS WELL AS FOR PAYER INITIATED
      </td>

      <td>
        RECURRENCE\_PATTERN\_AS\_WELL\_AS\_FOR\_PAYER\_INITIATED
      </td>
    </tr>

    <tr>
      <td>
        E4106
      </td>

      <td>
        Transaction failed due to recurrence\
         pattern, value and amount rule mismatch
      </td>

      <td>
        RECURRENCE PATTERN AND VALUE MISMATCH (PAYER)
      </td>

      <td>
        RECURRENCE\_PATTERN\_AND\_VALUE\_MISMATCH\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4526
      </td>

      <td>
        Transaction not found in status check
      </td>

      <td>
        Record not found against given parameters
      </td>

      <td>
        Record\_Not\_Found\_Against\_Given\_Parameters
      </td>
    </tr>

    <tr>
      <td>
        E9229
      </td>

      <td>
        Reconciliation Totals Reset
      </td>

      <td>
        Reconciliation Totals Reset
      </td>

      <td>
        RECONCILIATION\_TOTALS\_RESET
      </td>
    </tr>

    <tr>
      <td>
        E1656
      </td>

      <td>
        Reconcile Error
      </td>

      <td>
        RECONCILE\_ERROR
      </td>

      <td>
        RECONCILE\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4168
      </td>

      <td>
        Transaction declined by the customer
      </td>

      <td>
        RECEIVED REQUEST AUTHORISATION IS DECLINED
      </td>

      <td>
        RECEIVED\_REQUEST\_AUTHORISATION\_IS\_DECLINED
      </td>
    </tr>

    <tr>
      <td>
        E4219
      </td>

      <td>
        RECEIVED LATE RESPONSE
      </td>

      <td>
        RECEIVED LATE RESPONSE
      </td>

      <td>
        RECEIVED\_LATE\_RESPONSE
      </td>
    </tr>

    <tr>
      <td>
        E4381
      </td>

      <td>
        RECEIVED LATE RESPONSE
      </td>

      <td>
        RECEIVED LATE RESPONSE
      </td>

      <td>
        RECEIVED\_LATE\_RESPONSE\_1
      </td>
    </tr>

    <tr>
      <td>
        E704
      </td>

      <td>
        Authorization request declined by\
         the bank due to an internal error
      </td>

      <td>
        RECEIPT\_NUMBER\_ERROR
      </td>

      <td>
        RECEIPT\_NUMBER\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4301
      </td>

      <td>
        Transaction failed as revoke should\
         be allowed for recurring mandate
      </td>

      <td>
        Purpose Code=14, Revocable= N ( Revokable tag must always be Y f
      </td>

      <td>
        Purpose\_Code\_14\_Revocable\_N\_Revokable\_Tag\_Must\_Always\_Be\_Y\_For\_For\_SI\_\_Recurring\_Mandate\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4107
      </td>

      <td>
        Transaction failed as blocking of funds\
         not allowed for recurring mandate
      </td>

      <td>
        Purpose code=14, Block fund = Y ( Block Fund must be N always fo
      </td>

      <td>
        Purpose\_Code\_14\_Block\_Fund\_Y\_Block\_Fund\_Must\_Be\_N\_Always\_For\_SI\_Recurring\_Mandate\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4292
      </td>

      <td>
        Transaction declined due to timeout\
        at Issuer's end
      </td>

      <td>
        PSP TIME-OUT
      </td>

      <td>
        PSP\_TIME\_OUT
      </td>
    </tr>

    <tr>
      <td>
        E4202
      </td>

      <td>
        PSP REQUEST PAY DEBIT\
        ACKNOWLEDGEMENT NOT RECEIVED
      </td>

      <td>
        PSP REQUEST PAY DEBIT ACKNOWLEDGEMENT NOT RECEIVED
      </td>

      <td>
        PSP\_REQUEST\_PAY\_DEBIT\_ACKNOWLEDGEMENT\_NOT\_RECEIVED
      </td>
    </tr>

    <tr>
      <td>
        E4175
      </td>

      <td>
        PSP REQUEST CREDIT PAY\
         ACKNOWLEDGEMENT IS NOT RECEIVED
      </td>

      <td>
        PSP REQUEST CREDIT PAY ACKNOWLEDGEMENT IS NOT RECEIVED
      </td>

      <td>
        PSP\_REQUEST\_CREDIT\_PAY\_ACKNOWLEDGEMENT\_IS\_NOT\_RECEIVED
      </td>
    </tr>

    <tr>
      <td>
        E4201
      </td>

      <td>
        PSP ORGID NOT FOUND
      </td>

      <td>
        PSP ORGID NOT FOUND
      </td>

      <td>
        PSP\_ORGID\_NOT\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E4249
      </td>

      <td>
        PSP NOT SUPPORTED BY UPI
      </td>

      <td>
        PSP NOT SUPPORTED BY UPI
      </td>

      <td>
        PSP\_NOT\_SUPPORTED\_BY\_UPI
      </td>
    </tr>

    <tr>
      <td>
        E4658
      </td>

      <td>
        PSP not found or configured
      </td>

      <td>
        PSP not found or configured
      </td>

      <td>
        PSP\_Not\_Found\_Or\_Configured
      </td>
    </tr>

    <tr>
      <td>
        E4166
      </td>

      <td>
        Transaction failed as handle used is not registered
      </td>

      <td>
        PSP IS NOT REGISTERED
      </td>

      <td>
        PSP\_IS\_NOT\_REGISTERED\_NEW
      </td>
    </tr>

    <tr>
      <td>
        E800
      </td>

      <td>
        Transaction failed due to error at the merchant's end
      </td>

      <td>
        PREFERED\_GATEWAY\_NOT\_SET
      </td>

      <td>
        PREFERED\_GATEWAY\_NOT\_SET
      </td>
    </tr>

    <tr>
      <td>
        E4527
      </td>

      <td>
        Refund failed due to invalid amount
      </td>

      <td>
        Please enter valid refund amount
      </td>

      <td>
        Please\_Enter\_Valid\_Refund\_Amount
      </td>
    </tr>

    <tr>
      <td>
        E9244
      </td>

      <td>
        PIN required
      </td>

      <td>
        PIN required
      </td>

      <td>
        PIN\_REQUIRED
      </td>
    </tr>

    <tr>
      <td>
        E4298
      </td>

      <td>
        PIN Cred Block is missing (txns > 2000)
      </td>

      <td>
        PIN Cred Block is missing (txns > 2000)
      </td>

      <td>
        PIN\_Cred\_Block\_Is\_Missing\_txns\_\_2000
      </td>
    </tr>

    <tr>
      <td>
        E4299
      </td>

      <td>
        PIN Cred Block is missing (txns \< 2000 and Seq No = 1)
      </td>

      <td>
        PIN Cred Block is missing (txns \< 2000 and Seq No = 1)
      </td>

      <td>
        PIN\_Cred\_Block\_Is\_Missing\_txns\_\_2000\_And\_Seq\_No\_1
      </td>
    </tr>

    <tr>
      <td>
        E310
      </td>

      <td>
        Card has been classified as lost\
         and has been blocked.
      </td>

      <td>
        Pick Up Card
      </td>

      <td>
        LOST\_CARD
      </td>
    </tr>

    <tr>
      <td>
        E1907
      </td>

      <td>
        We are unable to fetch status of transaction\
         right now. Check with merchant for order confirmation
      </td>

      <td>
        PHONE\_PE\_VERIFY\_ERROR
      </td>

      <td>
        PHONE\_PE\_VERIFY\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E1905
      </td>

      <td>
        Transaction could not be processed due to some internal error
      </td>

      <td>
        PHONE\_PE\_JS\_EXCEPTION
      </td>

      <td>
        PHONE\_PE\_JS\_EXCEPTION
      </td>
    </tr>

    <tr>
      <td>
        E1906
      </td>

      <td>
        Error while initiating payment with PhonePe!
      </td>

      <td>
        PHONE\_PE\_INITIATE\_ERROR
      </td>

      <td>
        PHONE\_PE\_INITIATE\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E1203
      </td>

      <td>
        You have exceeded your third party\
         funds transfer limit for the day.You cannot\
         transfer any more funds.
      </td>

      <td>
        PER TRANSACTION LIMIT EXCEEDED AS SET BY REMITTING MEMBER
      </td>

      <td>
        LIMIT\_EXCEED
      </td>
    </tr>

    <tr>
      <td>
        E330
      </td>

      <td>
        Validation Failure at PG End
      </td>

      <td>
        PAYMENT\_GATEWAY\_VALIDATION\_FAILURE
      </td>

      <td>
        PAYMENT\_GATEWAY\_VALIDATION\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E4103
      </td>

      <td>
        Payment validity expired
      </td>

      <td>
        Payment validity expired
      </td>

      <td>
        Payment\_Validity\_Expired
      </td>
    </tr>

    <tr>
      <td>
        E4315
      </td>

      <td>
        PAYMENT STOPPED BY COURT ORDER
      </td>

      <td>
        PAYMENT STOPPED BY COURT ORDER
      </td>

      <td>
        PAYMENT\_STOPPED\_BY\_COURT\_ORDER
      </td>
    </tr>

    <tr>
      <td>
        E4326
      </td>

      <td>
        PAYMENT STOPPED BY ATTACHMENT ORDER BD
      </td>

      <td>
        PAYMENT STOPPED BY ATTACHMENT ORDER BD
      </td>

      <td>
        PAYMENT\_STOPPED\_BY\_ATTACHMENT\_ORDER\_BD
      </td>
    </tr>

    <tr>
      <td>
        E1903
      </td>

      <td>
        Authorization failed at Bank
      </td>

      <td>
        Payment could not be authorised
      </td>

      <td>
        AUTHORIZATION\_FAILED\_BY\_BANK
      </td>
    </tr>

    <tr>
      <td>
        E4030
      </td>

      <td>
        PAYER/PAYEE.INFO.IDENTITY.TYPE MUST\
         BE PRESENT MINLENGTH 1 MAXLENGTH 20
      </td>

      <td>
        PAYER/PAYEE.INFO.IDENTITY.TYPE MUST BE PRESENT MINLENGTH 1 MAXLE
      </td>

      <td>
        PAYER\_PAYEE\_INFO\_IDENTITY\_TYPE\_MUST\_BE\_PRESENT\_MINLENGTH\_1\_MAXLENGTH\_20
      </td>
    </tr>

    <tr>
      <td>
        E4028
      </td>

      <td>
        PAYER/PAYEE.INFO MUST BE PRESENT
      </td>

      <td>
        PAYER/PAYEE.INFO MUST BE PRESENT
      </td>

      <td>
        PAYER\_PAYEE\_INFO\_MUST\_BE\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4017
      </td>

      <td>
        PAYER/PAYEE.DEVICE MUST BE PRESENT
      </td>

      <td>
        PAYER/PAYEE.DEVICE MUST BE PRESENT
      </td>

      <td>
        PAYER\_PAYEE\_DEVICE\_MUST\_BE\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4018
      </td>

      <td>
        PAYER/PAYEE. DEVICE.TAGS MUST BE\
         PRESENT PAYER/PAYEE.TAG.DEVICE\
        .NAME/VALUE MUST BE PRESENT
      </td>

      <td>
        PAYER/PAYEE. DEVICE.TAGS MUST BE PRESENT PAYER/PAYEE.TAG.DEVICE.
      </td>

      <td>
        PAYER\_PAYEE\_\_DEVICE\_TAGS\_MUST\_BE\_PRESENT\_PAYER\_PAYEE\_TAG\_DEVICE\_NAME\_VALUE\_MUST\_BE\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4254
      </td>

      <td>
        PAYER/PAYEE PSP,VERSION/TAGS\
         NOT SUPPORTED BY PSP/BANK
      </td>

      <td>
        PAYER/PAYEE PSP,VERSION/TAGS NOT SUPPORTED BY PSP/BANK
      </td>

      <td>
        PAYER\_PAYEE\_PSP\_VERSION\_TAGS\_NOT\_SUPPORTED\_BY\_PSP\_BANK
      </td>
    </tr>

    <tr>
      <td>
        E4253
      </td>

      <td>
        PAYER/PAYEE PSP,REQUEST & RESPONSE\
         HEADER VERSION MISMATCH
      </td>

      <td>
        PAYER/PAYEE PSP,REQUEST & RESPONSE HEADER VERSION MISMATCH
      </td>

      <td>
        PAYER\_PAYEE\_PSP\_REQUEST\_RESPONSE\_HEADER\_VERSION\_MISMATCH
      </td>
    </tr>

    <tr>
      <td>
        E4252
      </td>

      <td>
        PAYER/PAYEE PSP,HEADER OR URL\
         VERSION MISMATCHED
      </td>

      <td>
        PAYER/PAYEE PSP,HEADER OR URL VERSION MISMATCHED
      </td>

      <td>
        PAYER\_PAYEE\_PSP\_HEADER\_OR\_URL\_VERSION\_MISMATCHED
      </td>
    </tr>

    <tr>
      <td>
        E4032
      </td>

      <td>
        PAYER/PAYEE .INFO.RATING WHITELISTED\
         MUST BE PRESENT MINLENGTH 1 MAXLENGTH 5
      </td>

      <td>
        PAYER/PAYEE .INFO.RATING WHITELISTED MUST BE PRESENT MINLENGTH 1
      </td>

      <td>
        PAYER\_PAYEE\_INFO\_RATING\_WHITELISTED\_MUST\_BE\_PRESENT\_MINLENGTH\_1\_MAXLENGTH\_5
      </td>
    </tr>

    <tr>
      <td>
        E4031
      </td>

      <td>
        PAYER/PAYEE .INFO.IDENTITY VERIFIEDNAME\
         MUST BE PRESENT ALPHANUMERIC\
         MINLENGTH 1 MAXLENGTH 99
      </td>

      <td>
        PAYER/PAYEE .INFO.IDENTITY VERIFIEDNAME MUST BE PRESENT ALPHANUM
      </td>

      <td>
        PAYER\_PAYEE\_INFO\_IDENTITY\_UERIFIEDNAME\_MUST\_BE\_PRESENT\_ALPHANUMERIC\_MINLENGTH\_1\_MAXLENGTH\_99
      </td>
    </tr>

    <tr>
      <td>
        E4029
      </td>

      <td>
        PAYER/PAYEE .INFO.IDENTITY\
         MUST BE PRESENT
      </td>

      <td>
        PAYER/PAYEE .INFO.IDENTITY MUST BE PRESENT
      </td>

      <td>
        PAYER\_PAYEE\_INFO\_IDENTITY\_MUST\_BE\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4136
      </td>

      <td>
        PAYER.TYPE MUST BE PRESENT/VALID
      </td>

      <td>
        PAYER.TYPE MUST BE PRESENT/VALID
      </td>

      <td>
        PAYER\_TYPE\_MUST\_BE\_PRESENT\_VALID
      </td>
    </tr>

    <tr>
      <td>
        E4135
      </td>

      <td>
        PAYER.SEQNUM NUMERIC\
         MINLENGTH 1 MAXLENGTH 3
      </td>

      <td>
        PAYER.SEQNUM NUMERIC MINLENGTH 1 MAXLENGTH 3
      </td>

      <td>
        PAYER\_SEQNUM\_NUMERIC\_MINLENGTH\_1\_MAXLENGTH\_3
      </td>
    </tr>

    <tr>
      <td>
        E4134
      </td>

      <td>
        PAYER.NAME ALPHANUMERIC\
         MINLENGTH 1 MAXLENGTH 99
      </td>

      <td>
        PAYER.NAME ALPHANUMERIC MINLENGTH 1 MAXLENGTH 99
      </td>

      <td>
        PAYER\_NAME\_ALPHANUMERIC\_MINLENGTH\_1\_MAXLENGTH\_99
      </td>
    </tr>

    <tr>
      <td>
        E4026
      </td>

      <td>
        PAYER.INFO MUST BE PRESENT
      </td>

      <td>
        PAYER.INFO MUST BE PRESENT
      </td>

      <td>
        PAYER\_INFO\_MUST\_BE\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4137
      </td>

      <td>
        PAYER.CODE NUMERIC OF LENGTH 4
      </td>

      <td>
        PAYER.CODE NUMERIC OF LENGTH 4
      </td>

      <td>
        PAYER\_CODE\_NUMERIC\_OF\_LENGTH\_4
      </td>
    </tr>

    <tr>
      <td>
        E4133
      </td>

      <td>
        PAYER.ADDR MUST BE VALID\
         VPA MAXLENGTH 255
      </td>

      <td>
        PAYER.ADDR MUST BE VALID VPA MAXLENGTH 255
      </td>

      <td>
        PAYER\_ADDR\_MUST\_BE\_VALID\_VPA\_MAXLENGTH\_255
      </td>
    </tr>

    <tr>
      <td>
        E4117
      </td>

      <td>
        Transaction failed as payer\
         details are not correct in mandate
      </td>

      <td>
        PAYER VPA IS INCORRECT (PAYER)
      </td>

      <td>
        PAYER\_VPA\_IS\_INCORRECT\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4288
      </td>

      <td>
        PAYER PSP NOT REGISTERED
      </td>

      <td>
        PAYER PSP NOT REGISTERED
      </td>

      <td>
        PAYER\_PSP\_NOT\_REGISTERED
      </td>
    </tr>

    <tr>
      <td>
        E4285
      </td>

      <td>
        PAYER PSP NOT AVAILABLE
      </td>

      <td>
        PAYER PSP NOT AVAILABLE
      </td>

      <td>
        PAYER\_PSP\_NOT\_AVAILABLE
      </td>
    </tr>

    <tr>
      <td>
        E4264
      </td>

      <td>
        PAYER PSP DOES NOT SUPPORTS VERSION
      </td>

      <td>
        PAYER PSP DOES NOT SUPPORTS VERSION
      </td>

      <td>
        PAYER\_PSP\_DOES\_NOT\_SUPPORTS\_VERSION
      </td>
    </tr>

    <tr>
      <td>
        E4094
      </td>

      <td>
        PAYER PSP DOES NOT SUPPORT VERSION MANDATE 2.1
      </td>

      <td>
        PAYER PSP DOES NOT SUPPORT VERSION MANDATE 2.1
      </td>

      <td>
        PAYER\_PSP\_DOES\_NOT\_SUPPORT\_VERSION\_MANDATE\_2\_1
      </td>
    </tr>

    <tr>
      <td>
        E4295
      </td>

      <td>
        Transaction failed as vpa is not valid/expired
      </td>

      <td>
        PAYER PROFILE DOES NOT EXIST (DE REGISTRATION/VPA REMOVED/UPDATE
      </td>

      <td>
        EXPIRED\_VIRTUAL\_ADDRESS
      </td>
    </tr>

    <tr>
      <td>
        E4132
      </td>

      <td>
        PAYER NOT PRESENT
      </td>

      <td>
        PAYER NOT PRESENT
      </td>

      <td>
        PAYER\_NOT\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4120
      </td>

      <td>
        Modification not allowed by\
        merchant for payer initiated mandate
      </td>

      <td>
        PAYER INITIATED MANDATE CANNOT BE MODIFIED BY PAYEE
      </td>

      <td>
        PAYER\_INITIATED\_MANDATE\_CANNOT\_BE\_MODIFIED\_BY\_PAYEE
      </td>
    </tr>

    <tr>
      <td>
        E4210
      </td>

      <td>
        PAYER INFO DIFFERS FROM\
         ORIGINAL REQUEST
      </td>

      <td>
        PAYER INFO DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        PAYER\_INFO\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4211
      </td>

      <td>
        PAYER INFO DIFFERS FROM\
         ORIGINAL REQUEST
      </td>

      <td>
        PAYER INFO DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        PAYER\_INFO\_DIFFERS\_FROM\_ORIGINAL\_REQUEST\_1
      </td>
    </tr>

    <tr>
      <td>
        E4050
      </td>

      <td>
        PAYER AND PAYEE TOTAL\
         AMOUNT NOT MATCHING
      </td>

      <td>
        PAYER AND PAYEE TOTAL AMOUNT NOT MATCHING
      </td>

      <td>
        PAYER\_AND\_PAYEE\_TOTAL\_AMOUNT\_NOT\_MATCHING
      </td>
    </tr>

    <tr>
      <td>
        E4138
      </td>

      <td>
        Transaction failed as payer and payee account cannot be same
      </td>

      <td>
        PAYER AND PAYEE ACCOUNT SHOULD NOT BE EQUAL
      </td>

      <td>
        PAYER\_AND\_PAYEE\_ACCOUNT\_SHOULD\_NOT\_BE\_EQUAL
      </td>
    </tr>

    <tr>
      <td>
        E4052
      </td>

      <td>
        PAYER AMOUNT SHOULD BE\
         GREATER THAN TOTAL PAYEE AMOUNT
      </td>

      <td>
        PAYER AMOUNT SHOULD BE GREATER THAN TOTAL PAYEE AMOUNT
      </td>

      <td>
        PAYER\_AMOUNT\_SHOULD\_BE\_GREATER\_THAN\_TOTAL\_PAYEE\_AMOUNT
      </td>
    </tr>

    <tr>
      <td>
        E4222
      </td>

      <td>
        PAYER ACCOUNT MISMATCH
      </td>

      <td>
        PAYER ACCOUNT MISMATCH
      </td>

      <td>
        PAYER\_ACCOUNT\_MISMATCH
      </td>
    </tr>

    <tr>
      <td>
        E4125
      </td>

      <td>
        Transaction declined as customer account has changed
      </td>

      <td>
        PAYER ACCOUNT HAS CHANGED (PAYER)
      </td>

      <td>
        PAYER\_ACCOUNT\_HAS\_CHANGED\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4048
      </td>

      <td>
        PAYER & PAYEE TOTAL AMOUNT NOT MATCHING
      </td>

      <td>
        PAYER & PAYEE TOTAL AMOUNT NOT MATCHING
      </td>

      <td>
        PAYER\_PAYEE\_TOTAL\_AMOUNT\_NOT\_MATCHING
      </td>
    </tr>

    <tr>
      <td>
        E4006
      </td>

      <td>
        PAYEES NOT PRESENT
      </td>

      <td>
        PAYEES NOT PRESENT
      </td>

      <td>
        PAYEES\_NOT\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4008
      </td>

      <td>
        PAYEE.ADDR MUST BE VALID\
         VPA MAXLENGTH 255
      </td>

      <td>
        PAYEE.ADDR MUST BE VALID VPA MAXLENGTH 255
      </td>

      <td>
        PAYEE\_ADDR\_MUST\_BE\_UALID\_UPA\_MAXLENGTH\_255
      </td>
    </tr>

    <tr>
      <td>
        E4325
      </td>

      <td>
        Transaction declined as merchant vpa is not correct
      </td>

      <td>
        PAYEE VPA IS INCORRECT (REMITTER)
      </td>

      <td>
        PAYEE\_VPA\_IS\_INCORRECT\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4113
      </td>

      <td>
        Transaction failed as payee details are not correct in mandate
      </td>

      <td>
        PAYEE VPA IS INCORRECT (PAYER)
      </td>

      <td>
        PAYEE\_VPA\_IS\_INCORRECT\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4242
      </td>

      <td>
        PAYEE VPA AADHAAR OR IIN VPA IS DISABLED
      </td>

      <td>
        PAYEE VPA AADHAAR OR IIN VPA IS DISABLED
      </td>

      <td>
        PAYEE\_VPA\_AADHAAR\_OR\_IIN\_VPA\_IS\_DISABLED
      </td>
    </tr>

    <tr>
      <td>
        E4244
      </td>

      <td>
        PAYEE VPA AADHAAR OR IIN VPA IS DISABLED
      </td>

      <td>
        PAYEE VPA AADHAAR OR IIN VPA IS DISABLED
      </td>

      <td>
        PAYEE\_VPA\_AADHAAR\_OR\_IIN\_VPA\_IS\_DISABLED\_1
      </td>
    </tr>

    <tr>
      <td>
        E4289
      </td>

      <td>
        PAYEE PSP NOT REGISTERED
      </td>

      <td>
        PAYEE PSP NOT REGISTERED
      </td>

      <td>
        PAYEE\_PSP\_NOT\_REGISTERED
      </td>
    </tr>

    <tr>
      <td>
        E4286
      </td>

      <td>
        PAYEE PSP NOT AVAILABLE
      </td>

      <td>
        PAYEE PSP NOT AVAILABLE
      </td>

      <td>
        PAYEE\_PSP\_NOT\_AVAILABLE
      </td>
    </tr>

    <tr>
      <td>
        E4095
      </td>

      <td>
        PAYEE PSP DOES NOT SUPPORT VERSION MANDATE 2.1
      </td>

      <td>
        PAYEE PSP DOES NOT SUPPORT VERSION MANDATE 2.1
      </td>

      <td>
        PAYEE\_PSP\_DOES\_NOT\_SUPPORT\_VERSION\_MANDATE\_2\_1
      </td>
    </tr>

    <tr>
      <td>
        E4038
      </td>

      <td>
        PAYEE PSP DOES NOT SUPPORT VERSION 2
      </td>

      <td>
        PAYEE PSP DOES NOT SUPPORT VERSION 2
      </td>

      <td>
        PAYEE\_PSP\_DOES\_NOT\_SUPPORT\_VERSION\_2
      </td>
    </tr>

    <tr>
      <td>
        E4007
      </td>

      <td>
        PAYEE NOT PRESENT
      </td>

      <td>
        PAYEE NOT PRESENT
      </td>

      <td>
        PAYEE\_NOT\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4143
      </td>

      <td>
        Transaction failed as merchant\
         is reported SPAM by the customer
      </td>

      <td>
        PAYEE IS REPORTED AS SPAM UNDER RULE 1
      </td>

      <td>
        PAYEE\_IS\_REPORTED\_AS\_SPAM\_UNDER\_RULE\_1
      </td>
    </tr>

    <tr>
      <td>
        E4130
      </td>

      <td>
        Modification not allowed by payer\
         for merchant initiated mandate
      </td>

      <td>
        PAYEE INITIATED MANDATE CANNOT BE MODIFIED BY PAYER
      </td>

      <td>
        PAYEE\_INITIATED\_MANDATE\_CANNOT\_BE\_MODIFIED\_BY\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4047
      </td>

      <td>
        PAYEE AMOUNTCUR IS INVALID
      </td>

      <td>
        PAYEE AMOUNTCUR IS INVALID
      </td>

      <td>
        PAYEE\_AMOUNTCUR\_IS\_INVALID
      </td>
    </tr>

    <tr>
      <td>
        E4206
      </td>

      <td>
        PAYEE AMOUNT DIFFERS FROM\
         ORIGINAL REQUEST
      </td>

      <td>
        PAYEE AMOUNT DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        PAYEE\_AMOUNT\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4207
      </td>

      <td>
        PAYEE AMOUNT DIFFERS FROM\
         ORIGINAL REQUEST
      </td>

      <td>
        PAYEE AMOUNT DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        PAYEE\_AMOUNT\_DIFFERS\_FROM\_ORIGINAL\_REQUEST\_1
      </td>
    </tr>

    <tr>
      <td>
        E4046
      </td>

      <td>
        PAYEE AMOUNT CUR MUST BE CONSISTENT
      </td>

      <td>
        PAYEE AMOUNT CUR MUST BE CONSISTENT
      </td>

      <td>
        PAYEE\_AMOUNT\_CUR\_MUST\_BE\_CONSISTENT
      </td>
    </tr>

    <tr>
      <td>
        E4208
      </td>

      <td>
        PAYEE ADDRESS DIFFERS FROM\
         ORIGINAL REQUEST
      </td>

      <td>
        PAYEE ADDRESS DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        PAYEE\_ADDRESS\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4209
      </td>

      <td>
        PAYEE ADDRESS DIFFERS FROM\
         ORIGINAL REQUEST
      </td>

      <td>
        PAYEE ADDRESS DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        PAYEE\_ADDRESS\_DIFFERS\_FROM\_ORIGINAL\_REQUEST\_1
      </td>
    </tr>

    <tr>
      <td>
        E4223
      </td>

      <td>
        PAYEE ACCOUNT MISMATCH
      </td>

      <td>
        PAYEE ACCOUNT MISMATCH
      </td>

      <td>
        PAYEE\_ACCOUNT\_MISMATCH
      </td>
    </tr>

    <tr>
      <td>
        E326
      </td>

      <td>
        Authentication failed due to invalid password.
      </td>

      <td>
        PASSWORD\_ERROR
      </td>

      <td>
        PASSWORD\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4003
      </td>

      <td>
        PARTIAL REVERSAL
      </td>

      <td>
        PARTIAL REVERSAL
      </td>

      <td>
        PARTIAL\_REVERSAL
      </td>
    </tr>

    <tr>
      <td>
        E4141
      </td>

      <td>
        Transaction failed as partial debit request\
         timeout at customer's bank
      </td>

      <td>
        PARTIAL DEBIT REVERSAL TIMEOUT
      </td>

      <td>
        PARTIAL\_DEBIT\_REVERSAL\_TIMEOUT
      </td>
    </tr>

    <tr>
      <td>
        E1648
      </td>

      <td>
        Partial Approval
      </td>

      <td>
        Partial amount was approved
      </td>

      <td>
        PARTIAL\_APPROVAL
      </td>
    </tr>

    <tr>
      <td>
        E9202
      </td>

      <td>
        Partial Amount Approved
      </td>

      <td>
        Partial Amount Approved
      </td>

      <td>
        PARTIAL\_AMOUNT\_APPROVED
      </td>
    </tr>

    <tr>
      <td>
        E1606
      </td>

      <td>
        Transaction failed due to user\
         pressing refresh button.
      </td>

      <td>
        PAGE\_REFRESHED\_BY\_USER
      </td>

      <td>
        PAGE\_REFRESHED\_BY\_USER
      </td>
    </tr>

    <tr>
      <td>
        E1610
      </td>

      <td>
        Transaction failed. Page expired\
         due to no user input.
      </td>

      <td>
        PAGE\_EXPIRED
      </td>

      <td>
        PAGE\_EXPIRED
      </td>
    </tr>

    <tr>
      <td>
        E9246
      </td>

      <td>
        Over Daily Limit
      </td>

      <td>
        Over Daily Limit
      </td>

      <td>
        OVER\_DAILY\_LIMIT
      </td>
    </tr>

    <tr>
      <td>
        E2404
      </td>

      <td>
        OTP Validation Failed
      </td>

      <td>
        OTP\_VALIDATION\_FAILED
      </td>

      <td>
        OTP\_VALIDATION\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E1604
      </td>

      <td>
        Transaction failed due to\
         incorrect user action.
      </td>

      <td>
        OTP\_MAX\_RESEND\_ATTEMPT
      </td>

      <td>
        OTP\_MAX\_RESEND\_ATTEMPT
      </td>
    </tr>

    <tr>
      <td>
        E1601
      </td>

      <td>
        Customer Authentication failed\
         due to incorrect OTP.
      </td>

      <td>
        OTP\_MAX\_LIMIT\_EXCEEDED
      </td>

      <td>
        OTP\_MAX\_LIMIT\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E4388
      </td>

      <td>
        OTP TRANSACTION LIMIT EXCEEDED
      </td>

      <td>
        OTP TRANSACTION LIMIT EXCEEDED
      </td>

      <td>
        OTP\_TRANSACTION\_LIMIT\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E4387
      </td>

      <td>
        OTP EXPIRED
      </td>

      <td>
        OTP EXPIRED
      </td>

      <td>
        OTP\_EXPIRED
      </td>
    </tr>

    <tr>
      <td>
        E4263
      </td>

      <td>
        OTHER BANK/PSP IS NOT\
         SUPPORTED IN 2 VERSION
      </td>

      <td>
        OTHER BANK/PSP IS NOT SUPPORTED IN 2 VERSION
      </td>

      <td>
        OTHER\_BANK\_PSP\_IS\_NOT\_SUPPORTED\_IN\_2\_VERSION
      </td>
    </tr>

    <tr>
      <td>
        E4282
      </td>

      <td>
        ORIGINAL REQMANDATE NOT FOUND
      </td>

      <td>
        ORIGINAL REQMANDATE NOT FOUND
      </td>

      <td>
        ORIGINAL\_REQMANDATE\_NOT\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E4276
      </td>

      <td>
        ORIGINAL REQAUTHMANDATE\
         NOT FOUND
      </td>

      <td>
        ORIGINAL REQAUTHMANDATE NOT FOUND
      </td>

      <td>
        ORIGINAL\_REQAUTHMANDATE\_NOT\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E9253
      </td>

      <td>
        Amount Incorrect / Mismatch
      </td>

      <td>
        Original Amount Incorrect
      </td>

      <td>
        AMOUNT\_INCORRECT\_MISMATCH
      </td>
    </tr>

    <tr>
      <td>
        E1668
      </td>

      <td>
        Failing as no gateway found\
         for One Click transaction
      </td>

      <td>
        ONE\_CLICK\_PG  

        * SELECTION\_FAILED
      </td>

      <td>
        ONE\_CLICK\_PG\_SELECTION\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E1667
      </td>

      <td>
        Failing as One Click only option\
        was used and data validation checks failed
      </td>

      <td>
        ONE\_CLICK\_DATA  

        * VALIDATION\_FAILED
      </td>

      <td>
        ONE\_CLICK\_DATA\_VALIDATION\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E1666
      </td>

      <td>
        Failing as One Click only option\
         was used and transaction failed in authentication
      </td>

      <td>
        ONE\_CLICK\_AUTHENTICATION  

        * FAILED
      </td>

      <td>
        ONE\_CLICK\_AUTHENTICATION\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E4049
      </td>

      <td>
        ONE OR MORE PAYEE AMOUNT IS MISSING
      </td>

      <td>
        ONE OR MORE PAYEE AMOUNT IS MISSING
      </td>

      <td>
        ONE\_OR\_MORE\_PAYEE\_AMOUNT\_IS\_MISSING
      </td>
    </tr>

    <tr>
      <td>
        E9250
      </td>

      <td>
        Offline Approved
      </td>

      <td>
        Offline Approved
      </td>

      <td>
        OFFLINE\_APPROVED
      </td>
    </tr>

    <tr>
      <td>
        E1800
      </td>

      <td>
        The transaction cannot be processed\
         as discount given exceeds the allowed limit.\
         If money is debited from your account\
         then it will be auto refunded. Please try again
      </td>

      <td>
        OFFER\_AMOUNT\_EXCEEDED  

        * DURING\_TRANSACTION
      </td>

      <td>
        OFFER\_AMOUNT\_EXCEEDED\_DURING\_TRANSACTION
      </td>
    </tr>

    <tr>
      <td>
        E1303
      </td>

      <td>
        Transaction declined due to technical failure
      </td>

      <td>
        OBJECT\_CREATION\_FAILED
      </td>

      <td>
        OBJECT\_CREATION\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E4205
      </td>

      <td>
        NUMBER OF PAYEES DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        NUMBER OF PAYEES DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        NUMBER\_OF\_PAYEES\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4312
      </td>

      <td>
        Transaction failed as number of mandates allowed exceeded
      </td>

      <td>
        NUMBER OF MANDATES ALLOWED ON THIS ACCOUNT HAS EXCEEDED ISSUER'S
      </td>

      <td>
        NUMBER\_OF\_MANDATES\_ALLOWED\_ON\_THIS\_ACCOUNT\_HAS\_EXCEEDED\_ISSUER\_S\_LIMIT\_BD\_OPTIONAL\_AS\_PER\_BANKS\_POLICY
      </td>
    </tr>

    <tr>
      <td>
        E4247
      </td>

      <td>
        NULL ACK RECEIVED BY UPI FOR META TRANSACTION
      </td>

      <td>
        NULL ACK RECEIVED BY UPI FOR META TRANSACTION
      </td>

      <td>
        NULL\_ACK\_RECEIVED\_BY\_UPI\_FOR\_META\_TRANSACTION
      </td>
    </tr>

    <tr>
      <td>
        E1618
      </td>

      <td>
        No form post variables found [S2S Flow]
      </td>

      <td>
        NO\_FORM\_POST  

        * VARS\_S2SFLOW
      </td>

      <td>
        NO\_FORM\_POST\_VARS\_S2SFLOW
      </td>
    </tr>

    <tr>
      <td>
        E803
      </td>

      <td>
        Payment gateway seems\
         to be down at this moment.
      </td>

      <td>
        NO\_ELIGIBLE\_PG
      </td>

      <td>
        NO\_ELIGIBLE\_PG
      </td>
    </tr>

    <tr>
      <td>
        E222
      </td>

      <td>
        Debit account number is not\
         received in transaction response
      </td>

      <td>
        NO\_DEBIT\_ACCOUNT  

        * NUMBER
      </td>

      <td>
        NO\_DEBIT\_ACCOUNT\_NUMBER
      </td>
    </tr>

    <tr>
      <td>
        E221
      </td>

      <td>
        Bank reference number is not\
         received in transaction response
      </td>

      <td>
        NO\_BANK\_REFERENCE  

        * NUMBER
      </td>

      <td>
        NO\_BANK\_REFERENCE\_NUMBER
      </td>
    </tr>

    <tr>
      <td>
        E1624
      </td>

      <td>
        No Active Authentication Option Eligible
      </td>

      <td>
        NO\_ACTIVE\_PAYMENT  

        * ELIGIBLE
      </td>

      <td>
        NO\_ACTIVE\_PAYMENT\_ELIGIBLE
      </td>
    </tr>

    <tr>
      <td>
        E2402
      </td>

      <td>
        The customer does not have\
         an active credit line to book\
         a consumer loan
      </td>

      <td>
        NO\_ACTIVE\_CREDIT\_LINE  

        * WITH\_THE\_CUSTOMER
      </td>

      <td>
        NO\_ACTIVE\_CREDIT\_LINE\_WITH\_THE\_CUSTOMER
      </td>
    </tr>

    <tr>
      <td>
        E1650
      </td>

      <td>
        No action taken
      </td>

      <td>
        NO\_ACTION\_TAKEN
      </td>

      <td>
        NO\_ACTION\_TAKEN
      </td>
    </tr>

    <tr>
      <td>
        E342
      </td>

      <td>
        Transaction not initiated
      </td>

      <td>
        NOT\_INITIATED
      </td>

      <td>
        NOT\_INITIATED
      </td>
    </tr>

    <tr>
      <td>
        E1609
      </td>

      <td>
        Transaction declined due to the registered\
         mobile number being international. It should be\
         a domestic number to process the transaction.
      </td>

      <td>
        NOT\_DOMESTIC\_NUMBER
      </td>

      <td>
        NOT\_DOMESTIC\_NUMBER
      </td>
    </tr>

    <tr>
      <td>
        E343
      </td>

      <td>
        Transaction not approved
      </td>

      <td>
        NOT\_APPROVED
      </td>

      <td>
        NOT\_APPROVED
      </td>
    </tr>

    <tr>
      <td>
        E347
      </td>

      <td>
        Transaction failed because of non whitelisted domain
      </td>

      <td>
        NON\_WHITELISTED\_DOMAIN
      </td>

      <td>
        NON\_WHITELISTED\_DOMAIN
      </td>
    </tr>

    <tr>
      <td>
        E1616
      </td>

      <td>
        Non-seamless not allowed in S2S Flow
      </td>

      <td>
        NONSEAMLESS\_NOT  

        * ALLOWED\_S2SFLOW
      </td>

      <td>
        NONSEAMLESS\_NOT\_ALLOWED\_S2SFLOW
      </td>
    </tr>

    <tr>
      <td>
        E9252
      </td>

      <td>
        The customer's card issuer has declined\
         the transaction as the account type selected\
        is not valid for this credit card number.
      </td>

      <td>
        No Universal Account
      </td>

      <td>
        NO\_UNIVERSAL\_ACCOUNT
      </td>
    </tr>

    <tr>
      <td>
        E4176
      </td>

      <td>
        Transaction failed as no response\
         received from merchant/customer
      </td>

      <td>
        NO RESPONSE FROM PSP
      </td>

      <td>
        NO\_RESPONSE\_FROM\_PSP
      </td>
    </tr>

    <tr>
      <td>
        E4522
      </td>

      <td>
        Refund failed due to no response\
         from Customer's bank
      </td>

      <td>
        No response from Beneficiary Bank
      </td>

      <td>
        No\_Response\_From\_Beneficiary\_Bank
      </td>
    </tr>

    <tr>
      <td>
        E4101
      </td>

      <td>
        Transaction failed due to technical\
         issue at Issuer/Acquirer end
      </td>

      <td>
        NO ORIGINAL REQUEST FOUND DURING DEBIT/CREDIT BD
      </td>

      <td>
        NO\_ORIGINAL\_REQUEST\_FOUND\_DURING\_DEBIT\_CREDIT\_BD
      </td>
    </tr>

    <tr>
      <td>
        E4680
      </td>

      <td>
        No Mandate data found to Modify
      </td>

      <td>
        No Mandate data found to Modify
      </td>

      <td>
        No\_Mandate\_Data\_Found\_To\_Modify
      </td>
    </tr>

    <tr>
      <td>
        E4356
      </td>

      <td>
        NO FINANCIAL ADDRESS RECORD FOUND
      </td>

      <td>
        NO FINANCIAL ADDRESS RECORD FOUND
      </td>

      <td>
        NO\_FINANCIAL\_ADDRESS\_RECORD\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E9224
      </td>

      <td>
        No Envelope Inserted
      </td>

      <td>
        No Envelope Inserted
      </td>

      <td>
        NO\_ENVELOPE\_INSERTED
      </td>
    </tr>

    <tr>
      <td>
        E4346
      </td>

      <td>
        Transaction failed due to no\
         card details from customer's bank
      </td>

      <td>
        NO CARD RECORD (REMITTER)
      </td>

      <td>
        NO\_CARD\_RECORD\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4347
      </td>

      <td>
        Transaction failed due to no\
         card details from acquirer's bank
      </td>

      <td>
        NO CARD RECORD (BENEFICIARY)
      </td>

      <td>
        NO\_CARD\_RECORD\_BENEFICIARY
      </td>
    </tr>

    <tr>
      <td>
        E4533
      </td>

      <td>
        No active mandates found
      </td>

      <td>
        No Approved Mandates are available
      </td>

      <td>
        No\_Approved\_Mandates\_Are\_Available
      </td>
    </tr>

    <tr>
      <td>
        E4002
      </td>

      <td>
        NO ACTION TAKEN (FULL REVERSAL)
      </td>

      <td>
        NO ACTION TAKEN (FULL REVERSAL)
      </td>

      <td>
        NO\_ACTION\_TAKEN\_FULL\_REVERSAL
      </td>
    </tr>

    <tr>
      <td>
        E9207
      </td>

      <td>
        No Action Taken
      </td>

      <td>
        No Action Taken
      </td>

      <td>
        NO*ACTION\_TAKEN*
      </td>
    </tr>

    <tr>
      <td>
        E211
      </td>

      <td>
        The Bank servers are unreachable over the network
      </td>

      <td>
        NETWORK\_ERROR
      </td>

      <td>
        NETWORK\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E801
      </td>

      <td>
        Netbanking option was temporarily not available so set as bounced.
      </td>

      <td>
        NETBANKING\_GATEWAY  

        * DOWN
      </td>

      <td>
        NETBANKING\_GATEWAY\_DOWN
      </td>
    </tr>

    <tr>
      <td>
        E1204
      </td>

      <td>
        Transaction Failed at bank end.
      </td>

      <td>
        NETBANKING\_AUTHENTICATION  

        * ERROR
      </td>

      <td>
        NETBANKING\_AUTHENTICATION\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4152
      </td>

      <td>
        Transaction failed due to debit limit on customer exceeded
      </td>

      <td>
        NET DEBIT CAP IS EXCEEDED
      </td>

      <td>
        NET\_DEBIT\_CAP\_IS\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E4248
      </td>

      <td>
        NEGATIVE ACK RECEIVED BY UPI FOR META TRANSACTION
      </td>

      <td>
        NEGATIVE ACK RECEIVED BY UPI FOR META TRANSACTION
      </td>

      <td>
        NEGATIVE\_ACK\_RECEIVED\_BY\_UPI\_FOR\_META\_TRANSACTION
      </td>
    </tr>

    <tr>
      <td>
        E4314
      </td>

      <td>
        Transaction failed as debit not allowed
      </td>

      <td>
        NATURE OF DEBIT NOT ALLOWED IN ACCOUNT TYPE
      </td>

      <td>
        NATURE\_OF\_DEBIT\_NOT\_ALLOWED\_IN\_ACCOUNT\_TYPE
      </td>
    </tr>

    <tr>
      <td>
        E4525
      </td>

      <td>
        Multiple transactions found in status check
      </td>

      <td>
        Multiple transactions against given parameter
      </td>

      <td>
        Multiple\_Transactions\_Against\_Given\_Parameter
      </td>
    </tr>

    <tr>
      <td>
        E4005
      </td>

      <td>
        Transaction failed due to MPIN not set by customer
      </td>

      <td>
        MPIN NOT SET BY CUSTOMER
      </td>

      <td>
        MPIN\_NOT\_SET\_BY\_CUSTOMER
      </td>
    </tr>

    <tr>
      <td>
        E4051
      </td>

      <td>
        MORE THAN ONE PAYEE AMOUNT IS MISSING
      </td>

      <td>
        MORE THAN ONE PAYEE AMOUNT IS MISSING
      </td>

      <td>
        MORE\_THAN\_ONE\_PAYEE\_AMOUNT\_IS\_MISSING
      </td>
    </tr>

    <tr>
      <td>
        E4012
      </td>

      <td>
        MOBILE NUMBER REGISTERED WITH MULTIPLE CUSTOMER IDS
      </td>

      <td>
        MOBILE NUMBER REGISTERED WITH MULTIPLE CUSTOMER IDS
      </td>

      <td>
        MOBILE\_NUMBER\_REGISTERED\_WITH\_MULTIPLE\_CUSTOMER\_IDS
      </td>
    </tr>

    <tr>
      <td>
        E9221
      </td>

      <td>
        Mobile number record not found / mis-match
      </td>

      <td>
        Mobile number record not found / mis-match
      </td>

      <td>
        MOBILE\_NUMBER\_RECORD\_NOT\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E4224
      </td>

      <td>
        MOBILE BANKING REGISTRATION FORMAT\
         NOT SUPPORTED BY THE ISSUER BANK
      </td>

      <td>
        MOBILE BANKING REGISTRATION FORMAT NOT SUPPORTED BY THE ISSUER B
      </td>

      <td>
        MOBILE\_BANKING\_REGISTRATION\_FORMAT\_NOT\_SUPPORTED\_BY\_THE\_ISSUER\_BANK
      </td>
    </tr>

    <tr>
      <td>
        E1700
      </td>

      <td>
        Term URL is missing in the request
      </td>

      <td>
        MISSING\_TERM\_URL
      </td>

      <td>
        MISSING\_TERM\_URL
      </td>
    </tr>

    <tr>
      <td>
        E1644
      </td>

      <td>
        Empty Otp Received
      </td>

      <td>
        MISSING\_OTP
      </td>

      <td>
        MISSING\_OTP
      </td>
    </tr>

    <tr>
      <td>
        E226
      </td>

      <td>
        Security Signature missing or mismatched
      </td>

      <td>
        MISSING\_MISMATCHED\_SIGNATURE
      </td>

      <td>
        MISSING\_MISMATCHED\_SIGNATURE
      </td>
    </tr>

    <tr>
      <td>
        E1651
      </td>

      <td>
        Mismatch in retrieval reference number
      </td>

      <td>
        MISMATCH\_RETRIEVAL\_REFERENCE\_NUMBER
      </td>

      <td>
        MISMATCH\_RETRIEVAL\_REFERENCE\_NUMBER
      </td>
    </tr>

    <tr>
      <td>
        E4011
      </td>

      <td>
        MISMATCH IN PAYMENT DETAILS
      </td>

      <td>
        MISMATCH IN PAYMENT DETAILS
      </td>

      <td>
        MISMATCH\_IN\_PAYMENT\_DETAILS
      </td>
    </tr>

    <tr>
      <td>
        E4204
      </td>

      <td>
        MESSAGE INTEGRITY FAILED DUE TO ORGID MISMATCH
      </td>

      <td>
        MESSAGE INTEGRITY FAILED DUE TO ORGID MISMATCH
      </td>

      <td>
        MESSAGE\_INTEGRITY\_FAILED\_DUE\_TO\_ORGID\_MISMATCH
      </td>
    </tr>

    <tr>
      <td>
        E346
      </td>

      <td>
        Merchant Not Eligible for this transaction
      </td>

      <td>
        MERCHANT\_NOT\_ELIGIBLE
      </td>

      <td>
        MERCHANT\_NOT\_ELIGIBLE
      </td>
    </tr>

    <tr>
      <td>
        E4666
      </td>

      <td>
        Merchant Account details not found or configured
      </td>

      <td>
        Merchant\_Account\_Details  

        * Not\_Found\_Or\_Configured
      </td>

      <td>
        Merchant\_Account\_Details\_Not\_Found\_Or\_Configured
      </td>
    </tr>

    <tr>
      <td>
        E4512
      </td>

      <td>
        Transaction details not present at bank's end
      </td>

      <td>
        Merchant TranId is not available
      </td>

      <td>
        Merchant\_TranId\_Is\_Not\_Available
      </td>
    </tr>

    <tr>
      <td>
        E4333
      </td>

      <td>
        MERCHANT NOT REACHABLE (ACQURIER)
      </td>

      <td>
        MERCHANT NOT REACHABLE (ACQURIER)
      </td>

      <td>
        MERCHANT\_NOT\_REACHABLE\_ACQURIER
      </td>
    </tr>

    <tr>
      <td>
        EA09
      </td>

      <td>
        Alt ID Provisioning Failed
      </td>

      <td>
        Merchant not onboarded, please contact PayU Support
      </td>

      <td>
        ALT\_ID\_PROV\_MERCHANT
      </td>
    </tr>

    <tr>
      <td>
        E4365
      </td>

      <td>
        Transaction declined due to merchant error
      </td>

      <td>
        MERCHANT ERROR (PAYEE PSP)
      </td>

      <td>
        MERCHANT\_ERROR\_PAYEE\_PSP
      </td>
    </tr>

    <tr>
      <td>
        E9237
      </td>

      <td>
        Merchant Daily Limit Exceeded
      </td>

      <td>
        Merchant Daily Limit Exceeded
      </td>

      <td>
        MERCHANT\_DAILY\_LIMIT\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E4220
      </td>

      <td>
        MERCHANT CREDIT NOT SUPPORTED IN IMPS
      </td>

      <td>
        MERCHANT CREDIT NOT SUPPORTED IN IMPS
      </td>

      <td>
        MERCHANT\_CREDIT\_NOT\_SUPPORTED\_IN\_IMPS
      </td>
    </tr>

    <tr>
      <td>
        E4225
      </td>

      <td>
        Transaction failed as merchant is blocked
      </td>

      <td>
        MERCHANT BLOCKED
      </td>

      <td>
        MERCHANT\_BLOCKED
      </td>
    </tr>

    <tr>
      <td>
        E1643
      </td>

      <td>
        Mecode Not Permitted
      </td>

      <td>
        MECODE\_NOT\_PERMITTED
      </td>

      <td>
        MECODE\_NOT\_PERMITTED
      </td>
    </tr>

    <tr>
      <td>
        E1669
      </td>

      <td>
        MCP lookup details tampered
      </td>

      <td>
        MCP\_LOOKUP\_DETAILS\_TAMPERED
      </td>

      <td>
        MCP\_LOOKUP\_DETAILS\_TAMPERED
      </td>
    </tr>

    <tr>
      <td>
        E2406
      </td>

      <td>
        You have entered incorrect otp too many times, Please try again
      </td>

      <td>
        MAXIMUM\_OTP\_LIMIT\_REACHED
      </td>

      <td>
        MAXIMUM\_OTP\_LIMIT\_REACHED
      </td>
    </tr>

    <tr>
      <td>
        E9242
      </td>

      <td>
        Maximum refund credit reached
      </td>

      <td>
        Maximum refund credit reached
      </td>

      <td>
        MAXIMUM\_REFUND\_CREDIT\_REACHED
      </td>
    </tr>

    <tr>
      <td>
        E9241
      </td>

      <td>
        Maximum off-line refund reached
      </td>

      <td>
        Maximum off-line refund reached
      </td>

      <td>
        MAXIMUM\_OFFLINE\_REFUND\_REACHED
      </td>
    </tr>

    <tr>
      <td>
        E9243
      </td>

      <td>
        Maximum number refund credits
      </td>

      <td>
        Maximum number refund credits
      </td>

      <td>
        MAXIMUM\_NUMBER\_REFUND\_CREDITS
      </td>
    </tr>

    <tr>
      <td>
        E4104
      </td>

      <td>
        MAXIMUM BALANCE EXCEEDED AS SET BY BENEFICIARY BANK
      </td>

      <td>
        MAXIMUM BALANCE EXCEEDED AS SET BY BENEFICIARY BANK
      </td>

      <td>
        MAXIMUM\_BALANCE\_EXCEEDED\_AS\_SET\_BY\_BENEFICIARY\_BANK
      </td>
    </tr>

    <tr>
      <td>
        E1640
      </td>

      <td>
        Offus Master Card Not Approved Transaction
      </td>

      <td>
        MASTER\_CARD\_NOT\_APPROVED
      </td>

      <td>
        MASTER\_CARD\_NOT\_APPROVED
      </td>
    </tr>

    <tr>
      <td>
        E1641
      </td>

      <td>
        Cancellation not allowed for offus master card
      </td>

      <td>
        MASTER\_CARD\_CANCELLATION\_NOT\_ALLOWED
      </td>

      <td>
        MASTER\_CARD\_CANCELLATION\_NOT\_ALLOWED
      </td>
    </tr>

    <tr>
      <td>
        E4065
      </td>

      <td>
        MANDATE.VALIDITY.START MUST\
         BE PRESENT, DATE FORMAT
      </td>

      <td>
        MANDATE.VALIDITY.START MUST BE PRESENT, DATE FORMAT
      </td>

      <td>
        MANDATE\_VALIDITY\_START\_MUST\_BE\_PRESENT\_DATE\_FORMAT
      </td>
    </tr>

    <tr>
      <td>
        E4099
      </td>

      <td>
        MANDATE.VALIDITY.START DIFFERS\
         FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE.VALIDITY.START DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE\_VALIDITY\_START\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4066
      </td>

      <td>
        MANDATE.VALIDITY.END MUST BE\
         PRESENT, DATE FORMAT DDMMYYYY,\
         END DATE MUST BE GREATER THAN TODAY'S DATE
      </td>

      <td>
        MANDATE.VALIDITY.END MUST BE PRESENT, DATE FORMAT DDMMYYYY, END
      </td>

      <td>
        MANDATE\_VALIDITY\_END\_MUST\_BE\_PRESENT\_DATE\_FORMAT\_DDMMYYYY\_END\_DATE\_MUST\_BE\_GREATER\_THAN\_TODAYS\_DATE
      </td>
    </tr>

    <tr>
      <td>
        E4100
      </td>

      <td>
        MANDATE.VALIDITY.END DIFFERS\
         FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE.VALIDITY.END DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE\_VALIDITY\_END\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4064
      </td>

      <td>
        MANDATE.VALIDITY MUST BE PRESENT
      </td>

      <td>
        MANDATE.VALIDITY MUST BE PRESENT
      </td>

      <td>
        MANDATE\_VALIDITY\_MUST\_BE\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4098
      </td>

      <td>
        MANDATE.VALIDITY DIFFERS\
         FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE.VALIDITY DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE\_VALIDITY\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4056
      </td>

      <td>
        MANDATE.UMN SHOULD NOT BE\
         PRESENT FOR PAYEE INITIATED
      </td>

      <td>
        MANDATE.UMN SHOULD NOT BE PRESENT FOR PAYEE INITIATED
      </td>

      <td>
        MANDATE\_UMN\_SHOULD\_NOT\_BE\_PRESENT\_FOR\_PAYEE\_INITIATED
      </td>
    </tr>

    <tr>
      <td>
        E4060
      </td>

      <td>
        MANDATE.UMN MUST BE PRESENT, LENGTH 32
      </td>

      <td>
        MANDATE.UMN MUST BE PRESENT, LENGTH 32
      </td>

      <td>
        MANDATE\_UMN\_MUST\_BE\_PRESENT\_Length\_32
      </td>
    </tr>

    <tr>
      <td>
        E4059
      </td>

      <td>
        MANDATE.UMN MUST BE PRESENT
      </td>

      <td>
        MANDATE.UMN MUST BE PRESENT
      </td>

      <td>
        MANDATE\_UMN\_MUST\_BE\_PRESENT\_1
      </td>
    </tr>

    <tr>
      <td>
        E4081
      </td>

      <td>
        MANDATE.UMN DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE.UMN DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE\_UMN\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4075
      </td>

      <td>
        MANDATE.UMN CANNOT BE GENERATED BY PAYEE
      </td>

      <td>
        MANDATE.UMN CANNOT BE GENERATED BY PAYEE
      </td>

      <td>
        MANDATE\_UMN\_CANNOT\_BE\_GENERATED\_BY\_PAYEE
      </td>
    </tr>

    <tr>
      <td>
        E4086
      </td>

      <td>
        MANDATE.TYPE DIFFERS FROM\
         ORIGINAL REQUEST,MANDATE.AMOUNT\
         DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE.TYPE DIFFERS FROM ORIGINAL REQUEST,MANDATE.AMOUNT DIFFER
      </td>

      <td>
        MANDATE\_TYPE\_DIFFERS\_FROM\_ORIGINAL\_REQUEST\_MANDATE\_AMOUNT\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4057
      </td>

      <td>
        MANDATE.TXNID MUST BE PRESENT,\
         MUST BE 35 CHARACTERS OF ALPHANUMERIC
      </td>

      <td>
        MANDATE.TXNID MUST BE PRESENT, MUST BE 35 CHARACTERS OF ALPHANUM
      </td>

      <td>
        MANDATE\_TXNID\_MUST\_BE\_PRESENT\_MUST\_BE\_35\_CHARACTERS\_OF\_ALPHANUMERIC
      </td>
    </tr>

    <tr>
      <td>
        E4080
      </td>

      <td>
        MANDATE.TXNID DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE.TXNID DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE\_TXNID\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4058
      </td>

      <td>
        MANDATE.TXNID AND TXN.ID MUST BE SAME
      </td>

      <td>
        MANDATE.TXNID AND TXN.ID MUST BE SAME
      </td>

      <td>
        MANDATE\_TXNID\_AND\_TXN\_ID\_MUST\_BE\_SAME
      </td>
    </tr>

    <tr>
      <td>
        E4061
      </td>

      <td>
        MANDATE.TS MUST BE PRESENT AND SHOULD BE IN ISO\_ZONE
      </td>

      <td>
        MANDATE.TS MUST BE PRESENT AND SHOULD BE IN ISO\_ZONE
      </td>

      <td>
        MANDATE\_TS\_MUST\_BE\_PRESENT\_AND\_SHOULD\_BE\_IN\_ISO\_ZONE
      </td>
    </tr>

    <tr>
      <td>
        E4084
      </td>

      <td>
        MANDATE.SHARETOPAYEE DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE.SHARETOPAYEE DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE\_SHARETOPAYEE\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4062
      </td>

      <td>
        MANDATE.REVOKEABLE MUST BE PRESENT
      </td>

      <td>
        MANDATE.REVOKEABLE MUST BE PRESENT
      </td>

      <td>
        MANDATE\_REVOKEABLE\_MUST\_BE\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4072
      </td>

      <td>
        MANDATE.RECURRENCE.RULE NOT APPLICABLE\
         FOR MANDATE.RECURRENCE.PATTERN ONETIME/DAILY/WEEKLY/FORTNIGHTLY/MONTHLY\
        /BIMONTHLY/QUARTERLY/HALFYEARLY\
        /YEARLY/ASPRESENTED
      </td>

      <td>
        MANDATE.RECURRENCE.RULE NOT APPLICABLE FOR MANDATE.RECURRENCE.PA
      </td>

      <td>
        MANDATE\_RECURRENCE\_RULE\_NOT\_APPLICABLE\_FOR\_MANDATE\_RECURRENCE\_PATTERN\_ONETIME\_DAILY\_WEEKLY\_FORTNIGHTLY\_MONTHLY\_BIMONTHLY\_QUARTERLY\_HALFYEARLY\_YEARLY\_ASPRESENTED
      </td>
    </tr>

    <tr>
      <td>
        E4070
      </td>

      <td>
        MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.TYPE MUST BE AFTER OR ON OR BEFORE
      </td>

      <td>
        MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.
      </td>

      <td>
        MANDATE\_RECURRENCE\_RULE\_MUST\_BE\_PRESENT\_MANDATE\_RECURRENCE\_RULE\_TYPE\_MUST\_BE\_AFTER\_OR\_ON\_OR\_BEFORE
      </td>
    </tr>

    <tr>
      <td>
        E4071
      </td>

      <td>
        MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.VALUE IN BETWEEN 1 TO 7 ONLY WHEN MANDATE.RECURRENCE.PATTERN IS WEEKLY
      </td>

      <td>
        MANDATE.RECURRENCE.RULE MUST BE PRESENT,MANDATE.RECURRENCE.RULE.
      </td>

      <td>
        MANDATE\_RECURRENCE\_RULE\_MUST\_BE\_PRESENT\_MANDATE\_RECURRENCE\_RULE\_VALUE\_IN\_BETWEEN\_1\_TO\_7\_ONLY\_WHEN\_MANDATE\_RECURRENCE\_PATTERN\_IS\_WEEKLY
      </td>
    </tr>

    <tr>
      <td>
        E4087
      </td>

      <td>
        MANDATE.RECURRENCE.PATTERN DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE.RECURRENCE.PATTERN DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE\_RECURRENCE\_PATTERN\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4327
      </td>

      <td>
        MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTREMITTER BANK NOT CERTIFIED FOR 2.7
      </td>

      <td>
        MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTREMITTER BANK N
      </td>

      <td>
        MANDATE\_RECURRENCE\_RULE\_TAG\_SHOULD\_NOT\_BE\_PRESENTREMITTER\_BANK\_NOT\_CERTIFIED\_FOR\_2\_7
      </td>
    </tr>

    <tr>
      <td>
        E4328
      </td>

      <td>
        MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTBENEFICIARY BANK NOT CERTIFIED FOR 2.7
      </td>

      <td>
        MANDATE.RECURRENCE RULE TAG SHOULD NOT BE PRESENTBENEFICIARY BAN
      </td>

      <td>
        MANDATE\_RECURRENCE\_RULE\_TAG\_SHOULD\_NOT\_BE\_PRESENTBENEFICIARY\_BANK\_NOT\_CERTIFIED\_FOR\_2\_7
      </td>
    </tr>

    <tr>
      <td>
        E4069
      </td>

      <td>
        MANDATE.RECURRENCE MUST BE PRESENT,MANDATE.RECURRENCE.PATTERN MUST BE ONETIME OR DAILYOR WEEKLY
      </td>

      <td>
        MANDATE.RECURRENCE MUST BE PRESENT,MANDATE.RECURRENCE.PATTERN MU
      </td>

      <td>
        MANDATE\_RECURRENCE\_MUST\_BE\_PRESENT\_MANDATE\_RECURRENCE\_PATTERN\_MUST\_BE\_ONETIME\_OR\_DAILYOR\_WEEKLY
      </td>
    </tr>

    <tr>
      <td>
        E4079
      </td>

      <td>
        MANDATE.NAME DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE.NAME DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE\_NAME\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4054
      </td>

      <td>
        MANDATE.NAME ALPHANUMERIC; MINLENGTH 1 , MAXLENGTH 99
      </td>

      <td>
        MANDATE.NAME ALPHANUMERIC; MINLENGTH 1 , MAXLENGTH 99
      </td>

      <td>
        MANDATE\_NAME\_ALPHANUMERIC\_MINLENGTH\_1\_MAXLENGTH\_99
      </td>
    </tr>

    <tr>
      <td>
        E4085
      </td>

      <td>
        MANDATE.BLOCKFUND DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE.BLOCKFUND DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE\_BLOCKFUND\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4068
      </td>

      <td>
        MANDATE.AMOUNT.RULE MUST BE PRESENT, RULE MUST BE EXACT/MAX
      </td>

      <td>
        MANDATE.AMOUNT.RULE MUST BE PRESENT, RULE MUST BE EXACT/MAX
      </td>

      <td>
        MANDATE\_AMOUNT\_RULE\_MUST\_BE\_PRESENT\_RULE\_MUST\_BE\_EXACT\_MAX
      </td>
    </tr>

    <tr>
      <td>
        E4067
      </td>

      <td>
        MANDATE.AMOUNT MUST BE PRESENT, VALUE AND RULE SHOULD NOT BE EMPTY
      </td>

      <td>
        MANDATE.AMOUNT MUST BE PRESENT, VALUE AND RULE SHOULD NOT BE EMP
      </td>

      <td>
        MANDATE\_AMOUNT\_MUST\_BE\_PRESENT\_VALUE\_AND\_RULE\_SHOULD\_NOT\_BE\_EMPTY
      </td>
    </tr>

    <tr>
      <td>
        E4090
      </td>

      <td>
        MANDATE.AMOUNT CAN ONLY BE UPDATED IF PURPOSE=01
      </td>

      <td>
        MANDATE.AMOUNT CAN ONLY BE UPDATED IF PURPOSE=01
      </td>

      <td>
        MANDATE\_AMOUNT\_CAN\_ONLY\_BE\_UPDATED\_IF\_PURPOSE\_01
      </td>
    </tr>

    <tr>
      <td>
        E4679
      </td>

      <td>
        Modification request already initiated
      </td>

      <td>
        Mandate Update Request already initiated for Same UMN
      </td>

      <td>
        Mandate\_Update\_Request\_Already\_Initiated\_For\_Same\_UMN
      </td>
    </tr>

    <tr>
      <td>
        E4055
      </td>

      <td>
        MANDATE UMN MUST BE PRESENT
      </td>

      <td>
        MANDATE UMN MUST BE PRESENT
      </td>

      <td>
        MANDATE\_UMN\_MUST\_BE\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4082
      </td>

      <td>
        MANDATE TS DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE TS DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE\_TS\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4078
      </td>

      <td>
        MANDATE TAG DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE TAG DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE\_TAG\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4309
      </td>

      <td>
        Transaction failed as mandate signature is tampered
      </td>

      <td>
        MANDATE SIGNATURE IS TAMPERED OR CORRUPT (REMITTER)
      </td>

      <td>
        MANDATE\_SIGNATURE\_IS\_TAMPERED\_OR\_CORRUPT\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4083
      </td>

      <td>
        MANDATE REVOKEABLE DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE REVOKEABLE DIFFERS FROM ORIGINAL REQUEST
      </td>

      <td>
        MANDATE\_REVOKEABLE\_DIFFERS\_FROM\_ORIGINAL\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E4532
      </td>

      <td>
        Mandate request not created
      </td>

      <td>
        Mandate request not created
      </td>

      <td>
        Mandate\_Request\_Not\_Created
      </td>
    </tr>

    <tr>
      <td>
        E4115
      </td>

      <td>
        Transaction failed as mandate request limit is breached
      </td>

      <td>
        MANDATE REQUEST LIMIT HAS BREACHED
      </td>

      <td>
        MANDATE\_REQUEST\_LIMIT\_HAS\_BREACHED
      </td>
    </tr>

    <tr>
      <td>
        E4077
      </td>

      <td>
        MANDATE REQUEST IS DECLINED BY MERCHANT (PAYEE)
      </td>

      <td>
        MANDATE REQUEST IS DECLINED BY MERCHANT (PAYEE)
      </td>

      <td>
        MANDATE\_REQUEST\_IS\_DECLINED\_BY\_MERCHANT\_PAYEE
      </td>
    </tr>

    <tr>
      <td>
        E4607
      </td>

      <td>
        Mandate Request Approved
      </td>

      <td>
        Mandate Request Approved
      </td>

      <td>
        Mandate\_Request\_Approved
      </td>
    </tr>

    <tr>
      <td>
        E4313
      </td>

      <td>
        MANDATE REGISTRATION NOT ALLOWED FOR CC PF PPF ACT (BANK'S POLICY)
      </td>

      <td>
        MANDATE REGISTRATION NOT ALLOWED FOR CC PF PPF ACT (BANKNULLS PO
      </td>

      <td>
        MANDATE\_REGISTRATION\_NOT\_ALLOWED\_FOR\_CC\_PF\_PPF\_ACT\_BANKS\_POLICY
      </td>
    </tr>

    <tr>
      <td>
        E4329
      </td>

      <td>
        MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENTPAYER PSP NOT CERTIFIED FOR 2.7
      </td>

      <td>
        MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENTPAYER PSP NOT C
      </td>

      <td>
        MANDATE\_RECURRENCE\_RULE\_TAG\_SHOULD\_NOT\_BE\_PRESENTPAYER\_PSP\_NOT\_CERTIFIED\_FOR\_2\_7
      </td>
    </tr>

    <tr>
      <td>
        E4330
      </td>

      <td>
        MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENT PAYEE PSP NOT CERTIFIED FOR 2.7
      </td>

      <td>
        MANDATE RECURRENCE RULE TAG SHOULD NOT BE PRESENT PAYEE PSP NOT
      </td>

      <td>
        MANDATE\_RECURRENCE\_RULE\_TAG\_SHOULD\_NOT\_BE\_PRESENT\_PAYEE\_PSP\_NOT\_CERTIFIED\_FOR\_2\_7
      </td>
    </tr>

    <tr>
      <td>
        E4073
      </td>

      <td>
        MANDATE RECURRENCE PATTERN.BLOCK=N IS ALLOWED ONLY IF THE PURPOSE CODE=14
      </td>

      <td>
        MANDATE RECURRENCE PATTERN.BLOCK=N IS ALLOWED ONLY IF THE PURPOS
      </td>

      <td>
        MANDATE\_RECURRENCE\_PATTERN\_BLOCK\_N\_IS\_ALLOWED\_ONLY\_IF\_THE\_PURPOSE\_CODE\_14
      </td>
    </tr>

    <tr>
      <td>
        E4074
      </td>

      <td>
        MANDATE RECURRENCE PATTERN. REVOKABLE=Y, ONLY Y IS ALLOWED IF THE PURPOSE CODE=14
      </td>

      <td>
        MANDATE RECURRENCE PATTERN. REVOKABLE=Y, ONLY Y IS ALLOWED IF TH
      </td>

      <td>
        MANDATE\_RECURRENCE\_PATTERN\_\_REVOKABLE\_Y\_ONLY\_Y\_IS\_ALLOWED\_IF\_THE\_PURPOSE\_CODE\_14
      </td>
    </tr>

    <tr>
      <td>
        E4053
      </td>

      <td>
        Transaction failed due to mandate not present
      </td>

      <td>
        MANDATE NOT PRESENT
      </td>

      <td>
        MANDATE\_NOT\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4124
      </td>

      <td>
        Modification request declined by the customer
      </td>

      <td>
        MANDATE MODIFY REQUEST IS DECLINED (PAYER)
      </td>

      <td>
        MANDATE\_MODIFY\_REQUEST\_IS\_DECLINED\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4131
      </td>

      <td>
        Modification request declined by merchant
      </td>

      <td>
        MANDATE MODIFICATION DECLINED BY MERCHANT
      </td>

      <td>
        MANDATE\_MODIFICATION\_DECLINED\_BY\_MERCHANT
      </td>
    </tr>

    <tr>
      <td>
        E4108
      </td>

      <td>
        Transaction failed as mandate is paused by the user
      </td>

      <td>
        MANDATE IS PAUSED BY USER
      </td>

      <td>
        MANDATE\_IS\_PAUSED\_BY\_USER
      </td>
    </tr>

    <tr>
      <td>
        E4109
      </td>

      <td>
        Transaction failed as mandate is already honoured
      </td>

      <td>
        MANDATE IS ALREADY HONOURED
      </td>

      <td>
        MANDATE\_IS\_ALREADY\_HONOURED\_1
      </td>
    </tr>

    <tr>
      <td>
        E4111
      </td>

      <td>
        Transaction failed as mandate is expired
      </td>

      <td>
        MANDATE HAS EXPIRED
      </td>

      <td>
        MANDATE\_HAS\_EXPIRED
      </td>
    </tr>

    <tr>
      <td>
        E4110
      </td>

      <td>
        Transaction failed as mandate is revoked by the user
      </td>

      <td>
        MANDATE HAS BEEN REVOKED
      </td>

      <td>
        MANDATE\_HAS\_BEEN\_REVOKED
      </td>
    </tr>

    <tr>
      <td>
        E4127
      </td>

      <td>
        Transaction declined as payee is a non-merchant
      </td>

      <td>
        MANDATE DECLINED AS PAYEE IS NON-MERCHANT (PAYER)
      </td>

      <td>
        MANDATE\_DECLINED\_AS\_PAYEE\_IS\_NON\_MERCHANT\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4116
      </td>

      <td>
        Transaction failed as mandate amount is higher than allowed by customer's application
      </td>

      <td>
        MANDATE DEBIT IS BEYOND PSP SPECIFIED AMOUNT CAP
      </td>

      <td>
        MANDATE\_DEBIT\_IS\_BEYOND\_PSP\_SPECIFIED\_AMOUNT\_CAP
      </td>
    </tr>

    <tr>
      <td>
        E4121
      </td>

      <td>
        Transaction failed as mandate is not allowed to be created on this merchant
      </td>

      <td>
        MANDATE CANNOT BE CREATED ON THIS VPA (PAYER)
      </td>

      <td>
        MANDATE\_CANNOT\_BE\_CREATED\_ON\_THIS\_VPA\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4535
      </td>

      <td>
        Transaction failed due to amount mismatch error
      </td>

      <td>
        Mandate amounts mis-matched
      </td>

      <td>
        Mandate\_Amounts\_Mis\_matched
      </td>
    </tr>

    <tr>
      <td>
        E4293
      </td>

      <td>
        Transaction declined as mandate amount limit exceeded
      </td>

      <td>
        MANDATE AMOUNT CAP IS EXCEEDED
      </td>

      <td>
        MANDATE\_AMOUNT\_CAP\_IS\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E806
      </td>

      <td>
        You have opted out of Lazypay service
      </td>

      <td>
        LP\_USER\_OPTED\_OUT
      </td>

      <td>
        LP\_USER\_OPTED\_OUT
      </td>
    </tr>

    <tr>
      <td>
        E807
      </td>

      <td>
        Sorry! You are currently not registered for LazyPay
      </td>

      <td>
        LP\_USER\_INELIGIBLE
      </td>

      <td>
        LP\_USER\_INELIGIBLE
      </td>
    </tr>

    <tr>
      <td>
        E805
      </td>

      <td>
        Your Lazypay account is blocked
      </td>

      <td>
        LP\_USER\_BLOCKED
      </td>

      <td>
        LP\_USER\_BLOCKED
      </td>
    </tr>

    <tr>
      <td>
        E4001
      </td>

      <td>
        ISSUER NOT LIVE ON UPI
      </td>

      <td>
        Low confidence
      </td>

      <td>
        ISSUER\_NOT\_LIVE\_ON\_UPI
      </td>
    </tr>

    <tr>
      <td>
        E4359
      </td>

      <td>
        Transaction failed due to lost or stolen card from customer's bank
      </td>

      <td>
        LOST OR STOLEN CARD (REMITTER)
      </td>

      <td>
        LOST\_OR\_STOLEN\_CARD\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4360
      </td>

      <td>
        Transaction failed due to lost or stolen card from acquirer's bank
      </td>

      <td>
        LOST OR STOLEN CARD (BENEFICIARY)
      </td>

      <td>
        LOST\_OR\_STOLEN\_CARD\_BENEFICIARY
      </td>
    </tr>

    <tr>
      <td>
        E1505
      </td>

      <td>
        You don't have sufficient credit limit to complete this transaction.
      </td>

      <td>
        LOAN\_AMOUNT\_GREATER  

        * THAN\_ELIGIBLITY
      </td>

      <td>
        LOAN\_AMOUNT\_GREATER\_THAN\_ELIGIBLITY
      </td>
    </tr>

    <tr>
      <td>
        E2408
      </td>

      <td>
        Link and Pay not Eligible
      </td>

      <td>
        LINK\_AND\_PAY\_NOT\_ELIGIBLE
      </td>

      <td>
        LINK\_AND\_PAY\_NOT\_ELIGIBLE
      </td>
    </tr>

    <tr>
      <td>
        E4389
      </td>

      <td>
        LIMIT EXCEEDED FOR REMITTING BANK/ISSUING BANK
      </td>

      <td>
        LIMIT EXCEEDED FOR REMITTING BANK/ISSUING BANK
      </td>

      <td>
        LIMIT\_EXCEEDED\_FOR\_REMITTING\_BANK\_ISSUING\_BANK
      </td>
    </tr>

    <tr>
      <td>
        E2503
      </td>

      <td>
        Late otp submission on Headless
      </td>

      <td>
        LATE\_OTP\_SUBMISSSION  

        * ON\_HEADLESS
      </td>

      <td>
        LATE\_OTP\_SUBMISSSION\_ON\_HEADLESS
      </td>
    </tr>

    <tr>
      <td>
        E4158
      </td>

      <td>
        Transaction failed due to timeout at acquirer's end
      </td>

      <td>
        Issuer unavailable or switch inoperative
      </td>

      <td>
        REQAUTH\_TIME\_OUT\_FOR\_PAY
      </td>
    </tr>

    <tr>
      <td>
        E9254
      </td>

      <td>
        Authorization Platform or Switch / Issuer system inoperative or Not Supported
      </td>

      <td>
        Issuer or Switch is Inoperative
      </td>

      <td>
        BANK\_NOT\_SUPPORTED\_BY\_SWITCH
      </td>
    </tr>

    <tr>
      <td>
        E9254
      </td>

      <td>
        ACQUIRER/BENEFICIARY UNAVAILABLE(TIMEOUT)&#x9;
      </td>

      <td>
        ACQUIRER\_BENEFICIARY\_UNAVAILABLE\_TIMEOUT
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        E714
      </td>

      <td>
        Card authentication failed due to invalid ZIP code
      </td>

      <td>
        INVALID\_ZIP
      </td>

      <td>
        INVALID\_ZIP
      </td>
    </tr>

    <tr>
      <td>
        E1020
      </td>

      <td>
        Transaction ID you've generated isn't valid
      </td>

      <td>
        INVALID\_TRANSACTION\_ID
      </td>

      <td>
        INVALID\_TRANSACTION\_ID
      </td>
    </tr>

    <tr>
      <td>
        E1603
      </td>

      <td>
        Transaction failed. Mobile number not registered for the given card.
      </td>

      <td>
        INVALID\_PHONE\_NO
      </td>

      <td>
        INVALID\_PHONE\_NO
      </td>
    </tr>

    <tr>
      <td>
        E1646
      </td>

      <td>
        Invalid PayU ID
      </td>

      <td>
        INVALID\_PAYU\_ID
      </td>

      <td>
        INVALID\_PAYU\_ID
      </td>
    </tr>

    <tr>
      <td>
        E707
      </td>

      <td>
        Transaction failed due to invalid Primary Account Number. (Primary Account Number or PAN is the number that is embossed and/or encoded on a plastic card that identifies the issuer and the particular cardholder account.)
      </td>

      <td>
        INVALID\_PAN
      </td>

      <td>
        INVALID\_PAN
      </td>
    </tr>

    <tr>
      <td>
        E340
      </td>

      <td>
        Transaction failed due to invalid OTP
      </td>

      <td>
        INVALID\_OTP
      </td>

      <td>
        INVALID\_OTP
      </td>
    </tr>

    <tr>
      <td>
        E1665
      </td>

      <td>
        Incorrect request received for one click transaction
      </td>

      <td>
        INVALID\_ONE\_CLICK  

        * REQUEST\_RECEIVED
      </td>

      <td>
        INVALID\_ONE\_CLICK\_REQUEST\_RECEIVED
      </td>
    </tr>

    <tr>
      <td>
        E339
      </td>

      <td>
        Transaction failed due to invalid mobile number
      </td>

      <td>
        INVALID\_MOBILE\_NUMBER
      </td>

      <td>
        INVALID\_MOBILE\_NUMBER
      </td>
    </tr>

    <tr>
      <td>
        E1501
      </td>

      <td>
        Transaction amount is less than the minimum amount accepted by issuing bank for processing EMI.
      </td>

      <td>
        INVALID\_MIN\_AMOUNT\_EMI
      </td>

      <td>
        INVALID\_MIN\_AMOUNT\_EMI
      </td>
    </tr>

    <tr>
      <td>
        E1637
      </td>

      <td>
        Merchant Type Not Supported
      </td>

      <td>
        INVALID\_MERCHANT\_TYPE
      </td>

      <td>
        INVALID\_MERCHANT\_TYPE
      </td>
    </tr>

    <tr>
      <td>
        E1647
      </td>

      <td>
        Invalid Merchant Key
      </td>

      <td>
        INVALID\_MERCHANT\_KEY
      </td>

      <td>
        INVALID\_MERCHANT\_KEY
      </td>
    </tr>

    <tr>
      <td>
        E2409
      </td>

      <td>
        Transaction amount is more than the maximum amount accepted by issuing bank for processing EMI.
      </td>

      <td>
        INVALID\_MAX\_AMOUNT\_EMI
      </td>

      <td>
        INVALID\_MAX\_AMOUNT\_EMI
      </td>
    </tr>

    <tr>
      <td>
        E327
      </td>

      <td>
        Authentication failed to due invalid login
      </td>

      <td>
        INVALID\_LOGIN
      </td>

      <td>
        INVALID\_LOGIN
      </td>
    </tr>

    <tr>
      <td>
        E2407
      </td>

      <td>
        Missing User details
      </td>

      <td>
        INVALID\_LINK\_AND\_PAY  

        * REQUEST\_RECEIVED
      </td>

      <td>
        INVALID\_LINK\_AND\_PAY\_REQUEST\_RECEIVED
      </td>
    </tr>

    <tr>
      <td>
        E332
      </td>

      <td>
        Card authentication failed due to invalid FAX number
      </td>

      <td>
        INVALID\_FAX
      </td>

      <td>
        INVALID\_FAX
      </td>
    </tr>

    <tr>
      <td>
        E323
      </td>

      <td>
        Card authentication failed due to invalid card expiry date.
      </td>

      <td>
        INVALID\_EXPIRY\_DATE
      </td>

      <td>
        INVALID\_EXPIRY\_DATE
      </td>
    </tr>

    <tr>
      <td>
        E910
      </td>

      <td>
        EMI is not supported on this card
      </td>

      <td>
        INVALID\_EMI\_CARD\_BIN
      </td>

      <td>
        INVALID\_EMI\_CARD\_BIN
      </td>
    </tr>

    <tr>
      <td>
        E331
      </td>

      <td>
        Card authentication failed due to invalid email id
      </td>

      <td>
        INVALID\_EMAIL\_ID
      </td>

      <td>
        INVALID\_EMAIL\_ID
      </td>
    </tr>

    <tr>
      <td>
        E2081
      </td>

      <td>
        Invalid Device Id
      </td>

      <td>
        INVALID\_DEVICE\_ID
      </td>

      <td>
        INVALID\_DEVICE\_ID
      </td>
    </tr>

    <tr>
      <td>
        E333
      </td>

      <td>
        Card authentication failed due to invalid contact/phone details
      </td>

      <td>
        INVALID\_CONTACT
      </td>

      <td>
        INVALID\_CONTACT
      </td>
    </tr>

    <tr>
      <td>
        E709
      </td>

      <td>
        Transaction failed due to invalid credit card name
      </td>

      <td>
        INVALID\_CARD\_NAME
      </td>

      <td>
        INVALID\_CARD\_NAME
      </td>
    </tr>

    <tr>
      <td>
        E1702
      </td>

      <td>
        Invalid Action
      </td>

      <td>
        INVALID\_ACTION
      </td>

      <td>
        INVALID\_ACTION
      </td>
    </tr>

    <tr>
      <td>
        E1625
      </td>

      <td>
        Card not enabled for Ecomm transactions, either the card is newly issued or has not been used for any online transaction during last 12 months
      </td>

      <td>
        Invalid/nonexistent account specified (general)
      </td>

      <td>
        CARD\_NOT\_ENABLED\_FOR\_ECOMM\_TXN
      </td>
    </tr>

    <tr>
      <td>
        E4148
      </td>

      <td>
        INVALID/INCORRECT ATM PIN
      </td>

      <td>
        INVALID/INCORRECT ATM PIN
      </td>

      <td>
        INVALID\_INCORRECT\_ATM\_PIN
      </td>
    </tr>

    <tr>
      <td>
        E4042
      </td>

      <td>
        Invalid verification token
      </td>

      <td>
        Invalid verification token
      </td>

      <td>
        Invalid\_Verification\_Token
      </td>
    </tr>

    <tr>
      <td>
        E207
      </td>

      <td>
        Bank denied transaction on the card.
      </td>

      <td>
        Invalid transaction
      </td>

      <td>
        INVALID\_TRANSACTION
      </td>
    </tr>

    <tr>
      <td>
        E4521
      </td>

      <td>
        Transaction failed due to invalid MCC details
      </td>

      <td>
        Invalid Terminal Id
      </td>

      <td>
        Invalid\_Terminal\_Id
      </td>
    </tr>

    <tr>
      <td>
        E2110
      </td>

      <td>
        Unable to process the request.
      </td>

      <td>
        Invalid Response From Up Streaming Server
      </td>

      <td>
        INVALID\_REQUEST\_FROM\_PG\_TO\_DOWNSTREAM
      </td>
    </tr>

    <tr>
      <td>
        E4367
      </td>

      <td>
        INVALID RESPONSE CODE
      </td>

      <td>
        INVALID RESPONSE CODE
      </td>

      <td>
        INVALID\_RESPONSE\_CODE
      </td>
    </tr>

    <tr>
      <td>
        E710
      </td>

      <td>
        Transaction failed due to invalid PIN
      </td>

      <td>
        Invalid PIN
      </td>

      <td>
        INVALID\_PIN
      </td>
    </tr>

    <tr>
      <td>
        E4386
      </td>

      <td>
        INVALID OTP
      </td>

      <td>
        INVALID OTP
      </td>

      <td>
        INVALID\_OTP\_1
      </td>
    </tr>

    <tr>
      <td>
        E4371
      </td>

      <td>
        Transaction declined due to invalid merchant details
      </td>

      <td>
        INVALID MERCHANT (PAYEE PSP)
      </td>

      <td>
        INVALID\_MERCHANT\_PAYEE\_PSP
      </td>
    </tr>

    <tr>
      <td>
        E4332
      </td>

      <td>
        INVALID MERCHANT (ACQURIER)
      </td>

      <td>
        INVALID MERCHANT (ACQURIER)
      </td>

      <td>
        INVALID\_MERCHANT\_ACQURIER
      </td>
    </tr>

    <tr>
      <td>
        E341
      </td>

      <td>
        Transaction failed due to invalid merchant
      </td>

      <td>
        Invalid Merchant
      </td>

      <td>
        INVALID\_MERCHANT
      </td>
    </tr>

    <tr>
      <td>
        E305
      </td>

      <td>
        The transaction failed due to invalid or absent card number.
      </td>

      <td>
        Invalid issuer
      </td>

      <td>
        CARD\_NUMBER\_INVALID
      </td>
    </tr>

    <tr>
      <td>
        E1632
      </td>

      <td>
        Transaction declined due to either incorrect cvv/expiry or card validation failure
      </td>

      <td>
        Invalid card number
      </td>

      <td>
        CARD\_VALIDATION\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E4368
      </td>

      <td>
        INVALID BENEFICIARY CREDENTIALS
      </td>

      <td>
        INVALID BENEFICIARY CREDENTIALS
      </td>

      <td>
        INVALID\_BENEFICIARY\_CREDENTIALS
      </td>
    </tr>

    <tr>
      <td>
        E4336
      </td>

      <td>
        INVALID AMOUNT (REMITTER)
      </td>

      <td>
        INVALID AMOUNT (REMITTER)
      </td>

      <td>
        INVALID\_AMOUNT\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4337
      </td>

      <td>
        INVALID AMOUNT (BENEFICIARY)
      </td>

      <td>
        INVALID AMOUNT (BENEFICIARY)
      </td>

      <td>
        INVALID\_AMOUNT\_BENEFICIARY
      </td>
    </tr>

    <tr>
      <td>
        E715
      </td>

      <td>
        Invalid amount sent to the bank
      </td>

      <td>
        Invalid amount
      </td>

      <td>
        INVALID\_AMOUNT
      </td>
    </tr>

    <tr>
      <td>
        E903
      </td>

      <td>
        International cards are not accepted
      </td>

      <td>
        INTERNATIONAL\_CARD  

        * NOT\_ALLOWED
      </td>

      <td>
        INTERNATIONAL\_CARD\_NOT\_ALLOWED
      </td>
    </tr>

    <tr>
      <td>
        E4040
      </td>

      <td>
        International Service not activated/disabled
      </td>

      <td>
        International Service not activated/disabled
      </td>

      <td>
        International\_Service\_Not\_Activated\_disabled
      </td>
    </tr>

    <tr>
      <td>
        E9239
      </td>

      <td>
        International Acceptance not enabled
      </td>

      <td>
        International Acceptance not enabled
      </td>

      <td>
        INTERNATIONAL\_ACCEPTANCE\_NOT\_ENABLED
      </td>
    </tr>

    <tr>
      <td>
        E1617
      </td>

      <td>
        Internal server Error [S2S FLow]
      </td>

      <td>
        INTERNAL\_SERVER  

        * ERROR\_S2SFLOW
      </td>

      <td>
        INTERNAL\_SERVER\_ERROR\_S2SFLOW
      </td>
    </tr>

    <tr>
      <td>
        E1901
      </td>

      <td>
        Customer chose Collect over Intent
      </td>

      <td>
        INTENT\_SDK\_FALLBACK
      </td>

      <td>
        INTENT\_SDK\_FALLBACK
      </td>
    </tr>

    <tr>
      <td>
        E1900
      </td>

      <td>
        Unable to open intent, switched to collect
      </td>

      <td>
        INTENT\_OPENING\_FAILED
      </td>

      <td>
        INTENT\_OPENING\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E1208
      </td>

      <td>
        Transaction failed because the customer does not have the necessary funds or he has given a wrong expiry date.
      </td>

      <td>
        INSUFFICIENT\_FUNDS  

        * INCORRECT\_EXPIRY
      </td>

      <td>
        INSUFFICIENT\_FUNDS\_INCORRECT\_EXPIRY
      </td>
    </tr>

    <tr>
      <td>
        E713
      </td>

      <td>
        The account against which the payment was made has insufficient funds,or, card authentication failed due to invalid card expiry date
      </td>

      <td>
        INSUFFICIENT\_FUNDS  

        * EXPIRY\_INVALID
      </td>

      <td>
        INSUFFICIENT\_FUNDS\_EXPIRY\_INVALID
      </td>
    </tr>

    <tr>
      <td>
        E719
      </td>

      <td>
        Transaction failed due to card authentication failure and/or insufficient funds
      </td>

      <td>
        INSUFFICIENT\_FUNDS  

        * AUTHENTICATION\_FAILURE
      </td>

      <td>
        INSUFFICIENT\_FUNDS\_AUTHENTICATION\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E706
      </td>

      <td>
        The account against which the payment was made has insufficient funds.
      </td>

      <td>
        Insufficient funds/over credit limit / Not sufficient funds
      </td>

      <td>
        INSUFFICIENT\_FUNDS
      </td>
    </tr>

    <tr>
      <td>
        E4390
      </td>

      <td>
        INCORRECT OTP
      </td>

      <td>
        INCORRECT OTP
      </td>

      <td>
        INCORRECT\_OTP
      </td>
    </tr>

    <tr>
      <td>
        E1502
      </td>

      <td>
        Incorrect request for SI, CC received in drop\_category.
      </td>

      <td>
        INCOMPLETE\_SI\_REQUEST
      </td>

      <td>
        INCOMPLETE\_SI\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E219
      </td>

      <td>
        Error at the Bank Server end
      </td>

      <td>
        INCOMPLETE\_BANK\_RESPONSE
      </td>

      <td>
        INCOMPLETE\_BANK\_RESPONSE
      </td>
    </tr>

    <tr>
      <td>
        E4391
      </td>

      <td>
        Transaction failed due to customer's account being inactive or dormant
      </td>

      <td>
        INACTIVE OR DORMANT ACCOUNT (REMITTER)
      </td>

      <td>
        INACTIVE\_OR\_DORMANT\_ACCOUNT\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4392
      </td>

      <td>
        Transaction failed due to acquirer' account being inactive or dormant
      </td>

      <td>
        INACTIVE OR DORMANT ACCOUNT (BENEFICIARY)
      </td>

      <td>
        INACTIVE\_OR\_DORMANT\_ACCOUNT\_BENEFICIARY
      </td>
    </tr>

    <tr>
      <td>
        E4191
      </td>

      <td>
        IMPS TRANSACTION IS ALREADY BEEN PROCESSED
      </td>

      <td>
        IMPS TRANSACTION IS ALREADY BEEN PROCESSED
      </td>

      <td>
        IMPS\_TRANSACTION\_IS\_ALREADY\_BEEN\_PROCESSED
      </td>
    </tr>

    <tr>
      <td>
        E4189
      </td>

      <td>
        IMPS PROCESSING FAILED IN UPI
      </td>

      <td>
        IMPS PROCESSING FAILED IN UPI
      </td>

      <td>
        IMPS\_PROCESSING\_FAILED\_IN\_UPI
      </td>
    </tr>

    <tr>
      <td>
        E4190
      </td>

      <td>
        IMPS IS SIGNED OFF
      </td>

      <td>
        IMPS IS SIGNED OFF
      </td>

      <td>
        IMPS\_IS\_SIGNED\_OFF
      </td>
    </tr>

    <tr>
      <td>
        E4192
      </td>

      <td>
        IMPS IS DECLINED
      </td>

      <td>
        IMPS IS DECLINED
      </td>

      <td>
        IMPS\_IS\_DECLINED
      </td>
    </tr>

    <tr>
      <td>
        E4159
      </td>

      <td>
        ILLEGAL OPERATION
      </td>

      <td>
        ILLEGAL OPERATION
      </td>

      <td>
        ILLEGAL\_OPERATION
      </td>
    </tr>

    <tr>
      <td>
        E4199
      </td>

      <td>
        IFSC IS NOT PRESENT
      </td>

      <td>
        IFSC IS NOT PRESENT
      </td>

      <td>
        IFSC\_IS\_NOT\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E1639
      </td>

      <td>
        Host down
      </td>

      <td>
        HOST\_DOWN
      </td>

      <td>
        HOST\_DOWN
      </td>
    </tr>

    <tr>
      <td>
        E2502
      </td>

      <td>
        Payu unable to parse ACS page for native
      </td>

      <td>
        HEADLESS\_ELEMENT\_MISSING
      </td>

      <td>
        HEADLESS\_ELEMENT\_MISSING
      </td>
    </tr>

    <tr>
      <td>
        E4250
      </td>

      <td>
        HEADER & URL VERSION IS MISMATCHED
      </td>

      <td>
        HEADER & URL VERSION IS MISMATCHED
      </td>

      <td>
        HEADER\_URL\_VERSION\_IS\_MISMATCHED
      </td>
    </tr>

    <tr>
      <td>
        E4076
      </td>

      <td>
        GLOBAL ADDRESS NOT SUPPORTED IN MANDATE
      </td>

      <td>
        GLOBAL ADDRESS NOT SUPPORTED IN MANDATE
      </td>

      <td>
        GLOBAL\_ADDRESS\_NOT\_SUPPORTED\_IN\_MANDATE
      </td>
    </tr>

    <tr>
      <td>
        E4933
      </td>

      <td>
        NPCI General error
      </td>

      <td>
        GENERAL ERROR
      </td>

      <td>
        NPCI\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4382
      </td>

      <td>
        FUNCTIONALITY NOT YET AVAILABLE FOR MERCHANT THROUGH THE ACQUIRING BANK
      </td>

      <td>
        FUNCTIONALITY NOT YET AVAILABLE FOR MERCHANT THROUGH THE ACQUIRI
      </td>

      <td>
        FUNCTIONALITY\_NOT\_YET\_AVAILABLE\_FOR\_MERCHANT\_THROUGH\_THE\_ACQUIRING\_BANK
      </td>
    </tr>

    <tr>
      <td>
        E4383
      </td>

      <td>
        FUNCTIONALITY NOT YET AVAILABLE FOR CUSTOMER THROUGH THE PAYEE PSP
      </td>

      <td>
        FUNCTIONALITY NOT YET AVAILABLE FOR CUSTOMER THROUGH THE PAYEE P
      </td>

      <td>
        FUNCTIONALITY\_NOT\_YET\_AVAILABLE\_FOR\_CUSTOMER\_THROUGH\_THE\_PAYEE\_PSP
      </td>
    </tr>

    <tr>
      <td>
        E4022
      </td>

      <td>
        Transaction failed due to freeze period for the first time customer
      </td>

      <td>
        FREEZE PERIOD FOR FIRST TIME USER
      </td>

      <td>
        FREEZE\_PERIOD\_FOR\_FIRST\_TIME\_USER
      </td>
    </tr>

    <tr>
      <td>
        E4154
      </td>

      <td>
        FORMATION IS NOT PROPER
      </td>

      <td>
        FORMATION IS NOT PROPER
      </td>

      <td>
        FORMATION\_IS\_NOT\_PROPER
      </td>
    </tr>

    <tr>
      <td>
        E4338
      </td>

      <td>
        FORMAT ERROR (INVALID FORMAT) (REMITTER)
      </td>

      <td>
        FORMAT ERROR (INVALID FORMAT) (REMITTER)
      </td>

      <td>
        FORMAT\_ERROR\_INVALID\_FORMAT\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4339
      </td>

      <td>
        FORMAT ERROR (INVALID FORMAT) (BENEFICIARY)
      </td>

      <td>
        FORMAT ERROR (INVALID FORMAT) (BENEFICIARY)
      </td>

      <td>
        FORMAT\_ERROR\_INVALID\_FORMAT\_BENEFICIARY
      </td>
    </tr>

    <tr>
      <td>
        E2102
      </td>

      <td>
        Transaction not approved
      </td>

      <td>
        Format error
      </td>

      <td>
        TXN\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E4194
      </td>

      <td>
        FORM PROCESSING HAS BEEN FAILED IN UPI
      </td>

      <td>
        FORM PROCESSING HAS BEEN FAILED IN UPI
      </td>

      <td>
        FORM\_PROCESSING\_HAS\_BEEN\_FAILED\_IN\_UPI
      </td>
    </tr>

    <tr>
      <td>
        E4193
      </td>

      <td>
        FORM HAS BEEN SIGNED OFF
      </td>

      <td>
        FORM HAS BEEN SIGNED OFF
      </td>

      <td>
        FORM\_HAS\_BEEN\_SIGNED\_OFF
      </td>
    </tr>

    <tr>
      <td>
        E4269
      </td>

      <td>
        FOREX Error in ValQR
      </td>

      <td>
        FOREX Error in ValQR
      </td>

      <td>
        FOREX\_Error\_In\_ValQR
      </td>
    </tr>

    <tr>
      <td>
        E9245
      </td>

      <td>
        Force Post
      </td>

      <td>
        Force Post
      </td>

      <td>
        FORCE\_POST
      </td>
    </tr>

    <tr>
      <td>
        E4021
      </td>

      <td>
        Transaction failed due to first transaction limit exceeded by the customer
      </td>

      <td>
        FIRST TRANSACTION LIMIT EXCEEDED
      </td>

      <td>
        FIRST\_TRANSACTION\_LIMIT\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E9210
      </td>

      <td>
        File Update not Supported by receiver
      </td>

      <td>
        File Update not Supported by receiver
      </td>

      <td>
        FILE\_UPDATE\_NOT\_SUPPORTED\_BY\_RECEIVER
      </td>
    </tr>

    <tr>
      <td>
        E9215
      </td>

      <td>
        File Update not Successful
      </td>

      <td>
        File Update not Successful
      </td>

      <td>
        FILE\_UPDATE\_NOT\_SUCCESSFUL
      </td>
    </tr>

    <tr>
      <td>
        E9214
      </td>

      <td>
        File Update File Locked Out
      </td>

      <td>
        File Update File Locked Out
      </td>

      <td>
        FILE\_UPDATE\_FILE\_LOCKED\_OUT
      </td>
    </tr>

    <tr>
      <td>
        E9213
      </td>

      <td>
        File Update Field Edit Error
      </td>

      <td>
        File Update Field Edit Error
      </td>

      <td>
        FILE\_UPDATE\_FIELD\_EDIT\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4888
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE\_3
      </td>
    </tr>

    <tr>
      <td>
        E4890
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE\_5
      </td>
    </tr>

    <tr>
      <td>
        E4891
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE\_6
      </td>
    </tr>

    <tr>
      <td>
        E4892
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE\_7
      </td>
    </tr>

    <tr>
      <td>
        E4897
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE\_11
      </td>
    </tr>

    <tr>
      <td>
        E4900
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE\_13
      </td>
    </tr>

    <tr>
      <td>
        E4903
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE\_16
      </td>
    </tr>

    <tr>
      <td>
        E4904
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE\_17
      </td>
    </tr>

    <tr>
      <td>
        E4907
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE\_19
      </td>
    </tr>

    <tr>
      <td>
        E4909
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE\_21
      </td>
    </tr>

    <tr>
      <td>
        E4910
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE
      </td>

      <td>
        FAILURE\_22
      </td>
    </tr>

    <tr>
      <td>
        E4803
      </td>

      <td>
        Transaction failed at bank end
      </td>

      <td>
        Failed
      </td>

      <td>
        Failed
      </td>
    </tr>

    <tr>
      <td>
        E1202
      </td>

      <td>
        Third Party Funds Transfer facility and Secure Access not enabled.
      </td>

      <td>
        FACILITY\_UNAVAILABLE
      </td>

      <td>
        FACILITY\_UNAVAILABLE
      </td>
    </tr>

    <tr>
      <td>
        E336
      </td>

      <td>
        Transaction failed due to incorrect card expiry date and/or insufficient funds
      </td>

      <td>
        EXPIRY\_DATE\_LOW\_FUNDS
      </td>

      <td>
        EXPIRY\_DATE\_LOW\_FUNDS
      </td>
    </tr>

    <tr>
      <td>
        E311
      </td>

      <td>
        Transaction declined due to invalid expiry details or the card is expired
      </td>

      <td>
        Expired card
      </td>

      <td>
        EXPIRED\_CARD
      </td>
    </tr>

    <tr>
      <td>
        E4122
      </td>

      <td>
        Transaction failed as execution day and execution rule mismatch
      </td>

      <td>
        EXECUTION DAY AND EXECUTION RULE MISMATCH (PAYER)
      </td>

      <td>
        EXECUTION\_DAY\_AND\_EXECUTION\_RULE\_MISMATCH\_PAYER
      </td>
    </tr>

    <tr>
      <td>
        E4536
      </td>

      <td>
        Transaction failed as execution amount is higher than mandate created amount
      </td>

      <td>
        Execution amount exceeded to Mandate approved amount
      </td>

      <td>
        Execution\_Amount\_Exceeded\_To\_Mandate\_Approved\_Amount
      </td>
    </tr>

    <tr>
      <td>
        E909
      </td>

      <td>
        Transaction amount exceeds the withdrawal limit of the user account
      </td>

      <td>
        Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc
      </td>

      <td>
        TRANSACTION\_MAX\_LIMIT\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E9230
      </td>

      <td>
        Exceeds Cash Limit
      </td>

      <td>
        Exceeds Cash Limit
      </td>

      <td>
        EXCEEDS\_CASH\_LIMIT
      </td>
    </tr>

    <tr>
      <td>
        E1645
      </td>

      <td>
        Transaction failed during authentication
      </td>

      <td>
        ERROR\_OCCURRED\_IN  

        * ENROLLMENT\_VALIDATION
      </td>

      <td>
        ERROR\_OCCURRED\_IN\_ENROLLMENT\_VALIDATION
      </td>
    </tr>

    <tr>
      <td>
        E209
      </td>

      <td>
        No Bank response
      </td>

      <td>
        Error: The request was received, but a service did not finish ru
      </td>

      <td>
        NO\_BANK\_RESPONSE
      </td>
    </tr>

    <tr>
      <td>
        E210
      </td>

      <td>
        Authentication failure or there is a delay in processing the transaction.
      </td>

      <td>
        Error - The request was received, but there was a timeout at the
      </td>

      <td>
        COMMUNICATION\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E208
      </td>

      <td>
        Error at the Bank Server end
      </td>

      <td>
        Error - The request was received but there was a server timeout.
      </td>

      <td>
        BANK\_SERVER\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E309
      </td>

      <td>
        Bank denied transaction on the card.
      </td>

      <td>
        Error - General system failure
      </td>

      <td>
        GENERAL\_SYSTEM\_ERROR\_PG
      </td>
    </tr>

    <tr>
      <td>
        E1909
      </td>

      <td>
        Error while processing enstage request
      </td>

      <td>
        ENSTAGE\_PROCESSING\_ERROR
      </td>

      <td>
        ENSTAGE\_PROCESSING\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E1908
      </td>

      <td>
        BIN not supported for pureS2S
      </td>

      <td>
        ENSTAGE\_BIN\_NOT  

        * ELIGIBLE\_PURES2S
      </td>

      <td>
        ENSTAGE\_BIN\_NOT\_ELIGIBLE\_PURES2S
      </td>
    </tr>

    <tr>
      <td>
        E4178
      </td>

      <td>
        Transaction failed due to technical error at customer's application
      </td>

      <td>
        ENCRYPTION ERROR
      </td>

      <td>
        ADDRESS\_RESOLUTION\_IS\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E303
      </td>

      <td>
        Payer could not be authenticated
      </td>

      <td>
        Encountered a Payer Authentication problem. Payer could not be a
      </td>

      <td>
        AUTHENTICATION\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E1301
      </td>

      <td>
        EMI not applicable for this transactions.
      </td>

      <td>
        EMI\_NOT\_APPLICABLE
      </td>

      <td>
        EMI\_NOT\_APPLICABLE
      </td>
    </tr>

    <tr>
      <td>
        E9236
      </td>

      <td>
        E-commerce Decline
      </td>

      <td>
        E-commerce Decline
      </td>

      <td>
        ECOMMERCE\_DECLINE
      </td>
    </tr>

    <tr>
      <td>
        E1300
      </td>

      <td>
        Customer has pressed the refresh key during the payment process.
      </td>

      <td>
        DUPLICATE\_SESSION\_ID
      </td>

      <td>
        DUPLICATE\_SESSION\_ID
      </td>
    </tr>

    <tr>
      <td>
        E344
      </td>

      <td>
        Transaction Failed
      </td>

      <td>
        DUPLICATE\_CONTACT
      </td>

      <td>
        DUPLICATE\_CONTACT
      </td>
    </tr>

    <tr>
      <td>
        E504
      </td>

      <td>
        The transaction has been identified as duplicate transaction.
      </td>

      <td>
        Duplicate Transaction
      </td>

      <td>
        DUPLICATE\_TRANSACTION
      </td>
    </tr>

    <tr>
      <td>
        E4020
      </td>

      <td>
        DUPLICATE RRN FOUND IN THE TRANSACTION. (REMITTER)
      </td>

      <td>
        DUPLICATE RRN FOUND IN THE TRANSACTION. (REMITTER)
      </td>

      <td>
        DUPLICATE\_RRN\_FOUND\_IN\_THE\_TRANSACTION\_\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4019
      </td>

      <td>
        DUPLICATE RRN FOUND IN THE TRANSACTION. (BENEFICIARY)
      </td>

      <td>
        DUPLICATE RRN FOUND IN THE TRANSACTION. (BENEFICIARY)
      </td>

      <td>
        DUPLICATE\_RRN\_FOUND\_IN\_THE\_TRANSACTION\_\_BENEFICIARY
      </td>
    </tr>

    <tr>
      <td>
        E4319
      </td>

      <td>
        DUPLICATE MANDATE REQUEST FOR SAME ITEM
      </td>

      <td>
        DUPLICATE MANDATE REQUEST FOR SAME ITEM
      </td>

      <td>
        DUPLICATE\_MANDATE\_REQUEST\_FOR\_SAME\_ITEM
      </td>
    </tr>

    <tr>
      <td>
        E4118
      </td>

      <td>
        Transaction failed due to duplicate mandate request
      </td>

      <td>
        DUPLICATE MANDATE REQUEST BD
      </td>

      <td>
        DUPLICATE\_MANDATE\_REQUEST\_BD
      </td>
    </tr>

    <tr>
      <td>
        E9212
      </td>

      <td>
        Duplicate File Update Record
      </td>

      <td>
        Duplicate File Update Record
      </td>

      <td>
        DUPLICATE\_FILE\_UPDATE\_RECORD
      </td>
    </tr>

    <tr>
      <td>
        E4033
      </td>

      <td>
        DUPLICATE BLOCKFUND FOR MANDATE REQUEST
      </td>

      <td>
        DUPLICATE BLOCKFUND FOR MANDATE REQUEST
      </td>

      <td>
        DUPLICATE\_BLOCKFUND\_FOR\_MANDATE\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E307
      </td>

      <td>
        Transaction declined with do not honor
      </td>

      <td>
        Do not honor
      </td>

      <td>
        DO\_NOT\_HONOUR
      </td>
    </tr>

    <tr>
      <td>
        E307
      </td>

      <td>
        Risk Service denied transaction
      </td>

      <td>
        Risk Service denied transaction - DO\_NOT\_HONOUR
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        E804
      </td>

      <td>
        Payment gateway seems to be down at this moment.
      </td>

      <td>
        DISABLE\_PG\_NOT\_AVAILABLE\_HANDLING
      </td>

      <td>
        DISABLE\_PG\_NOT\_AVAILABLE\_HANDLING
      </td>
    </tr>

    <tr>
      <td>
        E4212
      </td>

      <td>
        DEVICE REGISTRATION FAILED IN UPI
      </td>

      <td>
        DEVICE REGISTRATION FAILED IN UPI
      </td>

      <td>
        DEVICE\_REGISTRATION\_FAILED\_IN\_UPI
      </td>
    </tr>

    <tr>
      <td>
        E225
      </td>

      <td>
        Transaction in Progress
      </td>

      <td>
        Destination cannot be found for routing / Unable to route transa
      </td>

      <td>
        TRANSACTION\_IN\_PROGRESS
      </td>
    </tr>

    <tr>
      <td>
        DEFAULT
      </td>

      <td>
        Bank was unable to authenticate.
      </td>

      <td>
        DEFAULT\_VALUE
      </td>

      <td>
        DEFAULT\_VALUE
      </td>
    </tr>

    <tr>
      <td>
        E712
      </td>

      <td>
        The transaction could not be processed due to incomplete data provided at the users end.
      </td>

      <td>
        Declined - The request is missing one or more fields
      </td>

      <td>
        INCOMPLETE\_DATA
      </td>
    </tr>

    <tr>
      <td>
        E2100
      </td>

      <td>
        Invalid Request received for processing.
      </td>

      <td>
        Declined - One or more fields in the request contains invalid da
      </td>

      <td>
        INVALID\_DATA\_RECEIVED\_IN\_REQUEST
      </td>
    </tr>

    <tr>
      <td>
        E1638
      </td>

      <td>
        Transaction Already Reversed
      </td>

      <td>
        Decline - The transaction has already been settled or reversed.
      </td>

      <td>
        TRANSACTION\_REVERSED
      </td>
    </tr>

    <tr>
      <td>
        E1701
      </td>

      <td>
        Invalid Payment ID
      </td>

      <td>
        Decline - The request ID is invalid.
      </td>

      <td>
        INVALID\_PAYMENT\_ID
      </td>
    </tr>

    <tr>
      <td>
        E1623
      </td>

      <td>
        Customer Authentication failed due to incorrect ATM PIN.
      </td>

      <td>
        Decline - The Pinless Debit card's use frequency or maximum amou
      </td>

      <td>
        ATM\_MAX\_LIMIT\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E329
      </td>

      <td>
        Transaction declined by the issuer
      </td>

      <td>
        Decline - The issuing bank has questions about the request. You
      </td>

      <td>
        ISSUER\_DECLINED\_LOW\_FUNDS
      </td>
    </tr>

    <tr>
      <td>
        E902
      </td>

      <td>
        Invalid Card Number
      </td>

      <td>
        Decline - The card type is not accepted by the payment processor
      </td>

      <td>
        INVALID\_CARD\_TYPE
      </td>
    </tr>

    <tr>
      <td>
        E1628
      </td>

      <td>
        Daily limit exceeded
      </td>

      <td>
        Decline - The card has reached the credit limit
      </td>

      <td>
        LIMIT\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E1653
      </td>

      <td>
        Card Issuer Unavailable
      </td>

      <td>
        Decline - Issuing bank unavailable
      </td>

      <td>
        ISSUER\_UNAVAILABLE
      </td>
    </tr>

    <tr>
      <td>
        E312
      </td>

      <td>
        Bank denied transaction on the card.
      </td>

      <td>
        Decline - General decline of the card. No other information prov
      </td>

      <td>
        BANK\_DENIED
      </td>
    </tr>

    <tr>
      <td>
        E2111
      </td>

      <td>
        Transaction failed due to technical issue at Issuer/Acquirer end
      </td>

      <td>
        Decline - General decline by the processor.
      </td>

      <td>
        GENERAL\_DECLINE\_BY\_PROCESSOR
      </td>
    </tr>

    <tr>
      <td>
        E1400
      </td>

      <td>
        Invalid data received from bank.
      </td>

      <td>
        Decline - card verification number (CVN) did not match
      </td>

      <td>
        INVALID\_DATA\_NEW
      </td>
    </tr>

    <tr>
      <td>
        E4182
      </td>

      <td>
        Transaction failed as debit reversal failed in the customer's account
      </td>

      <td>
        DEBIT REVERT HAS BEEN FAILED
      </td>

      <td>
        DEBIT\_REVERT\_HAS\_BEEN\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E4142
      </td>

      <td>
        Debit failed due to timeout at customer's bank
      </td>

      <td>
        DEBIT REVERSAL TIMEOUT(REVERSAL)
      </td>

      <td>
        DEBIT\_REVERSAL\_TIMEOUT\_REVERSAL
      </td>
    </tr>

    <tr>
      <td>
        E4179
      </td>

      <td>
        Transaction failed as debit failed from the customer's account
      </td>

      <td>
        DEBIT HAS BEEN FAILED
      </td>

      <td>
        DEBIT\_HAS\_BEEN\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E4035
      </td>

      <td>
        DEBIT AMOUNT IS NOT BLOCKED FOR THE CUSTOMER
      </td>

      <td>
        DEBIT AMOUNT IS NOT BLOCKED FOR THE CUSTOMER
      </td>

      <td>
        DEBIT\_AMOUNT\_IS\_NOT\_BLOCKED\_FOR\_THE\_CUSTOMER
      </td>
    </tr>

    <tr>
      <td>
        E4036
      </td>

      <td>
        DEBIT AMOUNT GREATER THAN BLOCKED AMOUNT
      </td>

      <td>
        DEBIT AMOUNT GREATER THAN BLOCKED AMOUNT
      </td>

      <td>
        DEBIT\_AMOUNT\_GREATER\_THAN\_BLOCKED\_AMOUNT
      </td>
    </tr>

    <tr>
      <td>
        E4213
      </td>

      <td>
        DATA TAG SHOULD CONTAIN 4 PARTS DURING DEVICE REGISTRATION
      </td>

      <td>
        DATA TAG SHOULD CONTAIN 4 PARTS DURING DEVICE REGISTRATION
      </td>

      <td>
        DATA\_TAG\_SHOULD\_CONTAIN\_4\_PARTS\_DURING\_DEVICE\_REGISTRATION
      </td>
    </tr>

    <tr>
      <td>
        E1627
      </td>

      <td>
        Daily limit for wrong ATM PIN attempts reached
      </td>

      <td>
        DAILY\_ATM\_MAX\_LIMIT\_EXCEEDED
      </td>

      <td>
        DAILY\_ATM\_MAX\_LIMIT\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E9235
      </td>

      <td>
        CVR validation failed by Issuer
      </td>

      <td>
        CVR validation failed by Issuer
      </td>

      <td>
        CVR\_VALIDATION\_FAILED\_BY\_ISSUER
      </td>
    </tr>

    <tr>
      <td>
        E206
      </td>

      <td>
        Transaction failed as the bank servers are blocked for end of the day processing. Consequently, its servers are temporarily closed to any authentication requests.
      </td>

      <td>
        CUTOFF\_ERROR
      </td>

      <td>
        CUTOFF\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4352
      </td>

      <td>
        Transaction failed due to CBS cut-off at customer's bank
      </td>

      <td>
        CUT-OFF IS IN PROCESS (REMITTER)
      </td>

      <td>
        CUT\_OFF\_IS\_IN\_PROCESS\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4353
      </td>

      <td>
        Transaction failed due to CBS cut-off at acquirer's end
      </td>

      <td>
        CUT-OFF IS IN PROCESS (BENEFICIARY)
      </td>

      <td>
        CUT\_OFF\_IS\_IN\_PROCESS\_BENEFICIARY
      </td>
    </tr>

    <tr>
      <td>
        E9227
      </td>

      <td>
        Cut-off in Progress
      </td>

      <td>
        Cut-off in Progress
      </td>

      <td>
        CUTOFF\_IN\_PROGRESS
      </td>
    </tr>

    <tr>
      <td>
        E2401
      </td>

      <td>
        The customer is not eligible for this transaction
      </td>

      <td>
        CUSTOMER\_NOT\_ELIGIBLE  

        * FOR\_THIS\_TRANSACTION
      </td>

      <td>
        CUSTOMER\_NOT\_ELIGIBLE\_FOR\_THIS\_TRANSACTION
      </td>
    </tr>

    <tr>
      <td>
        E2403
      </td>

      <td>
        Customer KYC is pending at Issuer's end
      </td>

      <td>
        CUSTOMER\_KYC\_PENDING
      </td>

      <td>
        CUSTOMER\_KYC\_PENDING
      </td>
    </tr>

    <tr>
      <td>
        E9206
      </td>

      <td>
        Customer Dispute
      </td>

      <td>
        Customer Dispute
      </td>

      <td>
        CUSTOMER\_DISPUTE
      </td>
    </tr>

    <tr>
      <td>
        E9205
      </td>

      <td>
        Customer Cancellation
      </td>

      <td>
        Customer Cancellation
      </td>

      <td>
        CUSTOMER\_CANCELLATION
      </td>
    </tr>

    <tr>
      <td>
        E205
      </td>

      <td>
        Error at the Bank Server end
      </td>

      <td>
        CURL\_ERROR\_ENROLLED
      </td>

      <td>
        CURL\_ERROR\_ENROLLED
      </td>
    </tr>

    <tr>
      <td>
        E214
      </td>

      <td>
        The Bank servers are unreachable over the network
      </td>

      <td>
        CURL\_CALL\_FAILURE
      </td>

      <td>
        CURL\_CALL\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E9223
      </td>

      <td>
        Cryptographic Error
      </td>

      <td>
        Cryptographic Error
      </td>

      <td>
        CRYPTOGRAPHIC\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        EX311
      </td>

      <td>
        Transaction Failed
      </td>

      <td>
        CROSS\_BORDER  

        * IMPORT\_ERROR
      </td>

      <td>
        CROSS\_BORDER\_IMPORT\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4214
      </td>

      <td>
        CREDS BLOCK SHOULD CONTAIN CORRECT ELEMENTS DURING DEVICE REGISTRATION
      </td>

      <td>
        CREDS BLOCK SHOULD CONTAIN CORRECT ELEMENTS DURING DEVICE REGIST
      </td>

      <td>
        CREDS\_BLOCK\_SHOULD\_CONTAIN\_CORRECT\_ELEMENTS\_DURING\_DEVICE\_REGISTRATION
      </td>
    </tr>

    <tr>
      <td>
        E4181
      </td>

      <td>
        Transaction failed as credit reversal failed from the acquirer's account
      </td>

      <td>
        CREDIT REVERT HAS BEEN FAILED
      </td>

      <td>
        CREDIT\_REVERT\_HAS\_BEEN\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E4180
      </td>

      <td>
        Credit failed due to technical issue at acquirer's bank
      </td>

      <td>
        CREDIT HAS BEEN FAILED
      </td>

      <td>
        CREDIT\_HAS\_BEEN\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E4160
      </td>

      <td>
        CREDENTIALS IS NOT PRESENT
      </td>

      <td>
        CREDENTIALS IS NOT PRESENT
      </td>

      <td>
        CREDENTIALS\_IS\_NOT\_PRESENT
      </td>
    </tr>

    <tr>
      <td>
        E4016
      </td>

      <td>
        Transaction failed due to currency not supported
      </td>

      <td>
        Country/ Currency not supported
      </td>

      <td>
        Country\_\_Currency\_Not\_Supported
      </td>
    </tr>

    <tr>
      <td>
        E1629
      </td>

      <td>
        Transaction declined due to technical failure at bank end
      </td>

      <td>
        Contact Card Issuer
      </td>

      <td>
        BANK\_TECHNICAL\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E4015
      </td>

      <td>
        COMPLIANCE ERROR CODE FOR ISSUER BD
      </td>

      <td>
        COMPLIANCE ERROR CODE FOR ISSUER BD
      </td>

      <td>
        COMPLIANCE\_ERROR\_CODE\_FOR\_ISSUER\_BD
      </td>
    </tr>

    <tr>
      <td>
        E9232
      </td>

      <td>
        Compliance error code for issuer
      </td>

      <td>
        Compliance error code for issuer
      </td>

      <td>
        COMPLIANCE\_ERROR\_CODE\_FOR\_ISSUER
      </td>
    </tr>

    <tr>
      <td>
        E4014
      </td>

      <td>
        COMPLIANCE ERROR CODE FOR ACQUIRER
      </td>

      <td>
        COMPLIANCE ERROR CODE FOR ACQUIRER
      </td>

      <td>
        COMPLIANCE\_ERROR\_CODE\_FOR\_ACQUIRER
      </td>
    </tr>

    <tr>
      <td>
        E9216
      </td>

      <td>
        Completed Partially
      </td>

      <td>
        Completed Partially
      </td>

      <td>
        COMPLETED\_PARTIALLY
      </td>
    </tr>

    <tr>
      <td>
        E1902
      </td>

      <td>
        VPA is blank.Either validations have failed or merchant has not passed VPA
      </td>

      <td>
        COLLECT\_EMPTY\_VPA
      </td>

      <td>
        COLLECT\_EMPTY\_VPA
      </td>
    </tr>

    <tr>
      <td>
        E4149
      </td>

      <td>
        Transaction request declined as merchant is blocked by the customer
      </td>

      <td>
        COLLECT REQUEST IS DECLINED AS REQUESTOR IS BLOCKED BY CUSTOMER
      </td>

      <td>
        COLLECT\_REQUEST\_IS\_DECLINED\_AS\_REQUESTOR\_IS\_BLOCKED\_BY\_CUSTOMER
      </td>
    </tr>

    <tr>
      <td>
        E4218
      </td>

      <td>
        Transaction failed due to collect request expired
      </td>

      <td>
        COLLECT EXPIRED
      </td>

      <td>
        COLLECT\_EXPIRED
      </td>
    </tr>

    <tr>
      <td>
        E4511
      </td>

      <td>
        Transaction declined due to collect by date less that current date
      </td>

      <td>
        Collect By date should be greater than or equal to Current date
      </td>

      <td>
        Collect\_By\_Date\_Should\_Be\_Greater\_Than\_Or\_Equal\_To\_Current\_Date
      </td>
    </tr>

    <tr>
      <td>
        E4174
      </td>

      <td>
        CM URL IS NOT FOUND
      </td>

      <td>
        CM URL IS NOT FOUND
      </td>

      <td>
        CM\_URL\_IS\_NOT\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E4172
      </td>

      <td>
        CM REQUEST TIMEOUT
      </td>

      <td>
        CM REQUEST TIMEOUT
      </td>

      <td>
        CM\_REQUEST\_TIMEOUT
      </td>
    </tr>

    <tr>
      <td>
        E4171
      </td>

      <td>
        CM REQUEST IS DECLINED
      </td>

      <td>
        CM REQUEST IS DECLINED
      </td>

      <td>
        CM\_REQUEST\_IS\_DECLINED
      </td>
    </tr>

    <tr>
      <td>
        E4173
      </td>

      <td>
        CM REQUEST ACKNOWLEDGEMENT IS NOT RECEIVED
      </td>

      <td>
        CM REQUEST ACKNOWLEDGEMENT IS NOT RECEIVED
      </td>

      <td>
        CM\_REQUEST\_ACKNOWLEDGEMENT\_IS\_NOT\_RECEIVED
      </td>
    </tr>

    <tr>
      <td>
        E717
      </td>

      <td>
        Transaction declined as bank reported account to be closed
      </td>

      <td>
        Closed account
      </td>

      <td>
        INVALID\_ACCOUNT\_NUMBER
      </td>
    </tr>

    <tr>
      <td>
        E213
      </td>

      <td>
        Card authentication failure
      </td>

      <td>
        CHECKSUM\_FAILURE
      </td>

      <td>
        CHECKSUM\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E4164
      </td>

      <td>
        CHECKSUM FAILED
      </td>

      <td>
        CHECKSUM FAILED
      </td>

      <td>
        CHECKSUM\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E601
      </td>

      <td>
        Challan Generation Failed
      </td>

      <td>
        CHALLAN\_PAYMENT  

        * TRANSACTION\_FAILED
      </td>

      <td>
        CHALLAN\_PAYMENT\_TRANSACTION\_FAILED
      </td>
    </tr>

    <tr>
      <td>
        E4023
      </td>

      <td>
        CERTIFICATE NOT FOUND
      </td>

      <td>
        CERTIFICATE NOT FOUND
      </td>

      <td>
        CERTIFICATE\_NOT\_FOUND
      </td>
    </tr>

    <tr>
      <td>
        E802
      </td>

      <td>
        Issuing Bank was temporarily not available so set as bounced.
      </td>

      <td>
        CC\_DC\_ISSUING\_BANK\_DOWN
      </td>

      <td>
        CC\_DC\_ISSUING\_BANK\_DOWN
      </td>
    </tr>

    <tr>
      <td>
        E1619
      </td>

      <td>
        Category or ibibo code not recieved
      </td>

      <td>
        CATEGORY\_IBIBO\_NOT\_RCVD\_S2SFLOW
      </td>

      <td>
        CATEGORY\_IBIBO\_NOT\_RCVD\_S2SFLOW
      </td>
    </tr>

    <tr>
      <td>
        E9249
      </td>

      <td>
        Cash back exceeds daily limit
      </td>

      <td>
        Cash back exceeds daily limit
      </td>

      <td>
        CASH\_BACK\_EXCEEDS\_DAILY\_LIMIT
      </td>
    </tr>

    <tr>
      <td>
        E9238
      </td>

      <td>
        Card Re-use Limit Exceeded
      </td>

      <td>
        Card Re-use Limit Exceeded
      </td>

      <td>
        CARD\_REUSE\_LIMIT\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E9247
      </td>

      <td>
        Card Not Supported
      </td>

      <td>
        Card Not Supported
      </td>

      <td>
        CARD\_NOT\_SUPPORTED
      </td>
    </tr>

    <tr>
      <td>
        E9219
      </td>

      <td>
        Card Acceptor Call Acquirer Security
      </td>

      <td>
        Card Acceptor Call Acquirer Security
      </td>

      <td>
        CARD\_ACCEPTOR\_CALL\_ACQUIRER\_SECURITY
      </td>
    </tr>

    <tr>
      <td>
        E4519
      </td>

      <td>
        Refund failed due to insufficient amount
      </td>

      <td>
        Cannot verify PIN
      </td>

      <td>
        Insufficient\_Amount
      </td>
    </tr>

    <tr>
      <td>
        E4930
      </td>

      <td>
        Refund cannot be processed
      </td>

      <td>
        Cannot process Refund
      </td>

      <td>
        Cannot\_Process\_Refund
      </td>
    </tr>

    <tr>
      <td>
        E1605
      </td>

      <td>
        Transaction failed due to customer pressing cancel button.
      </td>

      <td>
        CANCEL\_BUTTON\_PRESSED\_BY\_USER
      </td>

      <td>
        CANCEL\_BUTTON\_PRESSED\_BY\_USER
      </td>
    </tr>

    <tr>
      <td>
        E9248
      </td>

      <td>
        Transaction is decline by issuing bank
      </td>

      <td>
        CAF status = 0 or 9
      </td>

      <td>
        CAF\_STATUS
      </td>
    </tr>

    <tr>
      <td>
        E1635
      </td>

      <td>
        Broker failure received from bank
      </td>

      <td>
        BROKER\_FAILURE
      </td>

      <td>
        BROKER\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E201
      </td>

      <td>
        The transaction failed due to invalid or absent card number.
      </td>

      <td>
        BRAND\_INVALID
      </td>

      <td>
        BRAND\_INVALID
      </td>
    </tr>

    <tr>
      <td>
        E1210
      </td>

      <td>
        Credit card used in Debit Card PG.
      </td>

      <td>
        BLOCK\_CREDIT\_CARDS
      </td>

      <td>
        BLOCK\_CREDIT\_CARDS
      </td>
    </tr>

    <tr>
      <td>
        E4089
      </td>

      <td>
        BLOCKFUND=Y IS ALLOWED FOR CREATE/UPDATE AND BLOCKFUND=N IS ALLOWED FOR REVOKE
      </td>

      <td>
        BLOCKFUND=Y IS ALLOWED FOR CREATE/UPDATE AND BLOCKFUND=N IS ALLO
      </td>

      <td>
        BLOCKFUND\_Y\_IS\_ALLOWED\_FOR\_CREATE\_UPDATE\_AND\_BLOCKFUND\_N\_IS\_ALLOWED\_FOR\_REVOKE
      </td>
    </tr>

    <tr>
      <td>
        E4088
      </td>

      <td>
        BLOCKFUND IS ALLOWED ONLY IF THE PURPOSE=01
      </td>

      <td>
        BLOCKFUND IS ALLOWED ONLY IF THE PURPOSE=01
      </td>

      <td>
        BLOCKFUND\_IS\_ALLOWED\_ONLY\_IF\_THE\_PURPOSE\_01
      </td>
    </tr>

    <tr>
      <td>
        E1660
      </td>

      <td>
        MCP Lookup api failed after sending S2S response
      </td>

      <td>
        BLAZE\_MCP\_LOOKUP\_ERROR
      </td>

      <td>
        BLAZE\_MCP\_LOOKUP\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E1659
      </td>

      <td>
        Error while connecting with blaze net encryption utility
      </td>

      <td>
        BLAZE\_ENCRYPTION\_ERROR
      </td>

      <td>
        BLAZE\_ENCRYPTION\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E4935
      </td>

      <td>
        Cryptogram missing
      </td>

      <td>
        Blank or null card token crypto
      </td>

      <td>
        CRYPTOGRAM\_MISSING
      </td>
    </tr>

    <tr>
      <td>
        E4934
      </td>

      <td>
        Invalid BIN
      </td>

      <td>
        Bin Not Found
      </td>

      <td>
        INVALID\_BIN
      </td>
    </tr>

    <tr>
      <td>
        E4262
      </td>

      <td>
        BENIFICIARY BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK
      </td>

      <td>
        BENIFICIARY BANK,VERSION/TAGS SENT NOT SUPPORTED BY BANK
      </td>

      <td>
        BENIFICIARY\_BANK\_VERSION\_TAGS\_SENT\_NOT\_SUPPORTED\_BY\_BANK
      </td>
    </tr>

    <tr>
      <td>
        E4260
      </td>

      <td>
        BENIFICIARY BANK,REQUEST & RESPONSE HEADER VERSION MISMATCH
      </td>

      <td>
        BENIFICIARY BANK,REQUEST & RESPONSE HEADER VERSION MISMATCH
      </td>

      <td>
        BENIFICIARY\_BANK\_REQUEST\_RESPONSE\_HEADER\_VERSION\_MISMATCH
      </td>
    </tr>

    <tr>
      <td>
        E4261
      </td>

      <td>
        BENIFICIARY BANK,HEADER OR URL VERSION MISMATCHED
      </td>

      <td>
        BENIFICIARY BANK,HEADER OR URL VERSION MISMATCHED
      </td>

      <td>
        BENIFICIARY\_BANK\_HEADER\_OR\_URL\_VERSION\_MISMATCHED
      </td>
    </tr>

    <tr>
      <td>
        E4097
      </td>

      <td>
        BENIFICIARY BANK DOES NOT SUPPORTS VERSION MANDATE 2.1
      </td>

      <td>
        BENIFICIARY BANK DOES NOT SUPPORTS VERSION MANDATE 2.1
      </td>

      <td>
        BENIFICIARY\_BANK\_DOES\_NOT\_SUPPORTS\_VERSION\_MANDATE\_2\_1
      </td>
    </tr>

    <tr>
      <td>
        E4358
      </td>

      <td>
        Transaction failed due to acquirers bank CBS offline
      </td>

      <td>
        BENEFICIARY CBS OFFLINE
      </td>

      <td>
        BENEFICIARY\_CBS\_OFFLINE
      </td>
    </tr>

    <tr>
      <td>
        E4291
      </td>

      <td>
        Mandate not supported by acquirer's bank
      </td>

      <td>
        BENEFICIARY BANK NOT REGISTERED (MANDATE)
      </td>

      <td>
        BENEFICIARY\_BANK\_NOT\_REGISTERED\_MANDATE
      </td>
    </tr>

    <tr>
      <td>
        E4364
      </td>

      <td>
        Transaction declined due to acquirer's account blocked or frozen
      </td>

      <td>
        BENEFICIARY ACCOUNT BLOCKED/FROZEN
      </td>

      <td>
        BENEFICIARY\_ACCOUNT\_BLOCKED\_FROZEN
      </td>
    </tr>

    <tr>
      <td>
        E4027
      </td>

      <td>
        BANKS HSM IS DOWN(REMITTER)
      </td>

      <td>
        BANKS HSM IS DOWN(REMITTER)
      </td>

      <td>
        BANKS\_HSM\_IS\_DOWN\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4384
      </td>

      <td>
        BANKS AS BENEFICIARY NOT LIVE ON PARTICULAR TXN TYPE
      </td>

      <td>
        BANKS AS BENEFICIARY NOT LIVE ON PARTICULAR TXN TYPE
      </td>

      <td>
        BANKS\_AS\_BENEFICIARY\_NOT\_LIVE\_ON\_PARTICULAR\_TXN\_TYPE
      </td>
    </tr>

    <tr>
      <td>
        E4039
      </td>

      <td>
        BANK/PSP IS NOT SUPPORTING VERSION 2
      </td>

      <td>
        BANK/PSP IS NOT SUPPORTING VERSION 2
      </td>

      <td>
        BANK\_PSP\_IS\_NOT\_SUPPORTING\_VERSION\_2
      </td>
    </tr>

    <tr>
      <td>
        E4281
      </td>

      <td>
        BANK TD RESPMANDATE NEGATIVE ACK SENT FROM UPI TO REMITTER BANK
      </td>

      <td>
        BANK TD RESPMANDATE NEGATIVE ACK SENT FROM UPI TO REMITTER BANK
      </td>

      <td>
        BANK\_TD\_RESPMANDATE\_NEGATIVE\_ACK\_SENT\_FROM\_UPI\_TO\_REMITTER\_BANK
      </td>
    </tr>

    <tr>
      <td>
        E9251
      </td>

      <td>
        Bank Settlement Limit Exceeded
      </td>

      <td>
        Bank Settlement Limit Exceeded
      </td>

      <td>
        BANK\_SETTLEMENT\_LIMIT\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E9251
      </td>

      <td>
        PAYER PSP THROTTLE DECLINE
      </td>

      <td>
        ADDRESS\_RESOLUTION\_IS\_FAILED
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        E9252
      </td>

      <td>
        PSP REQUEST META ACKNOWLEDGEMENT NOT RECEIVED
      </td>

      <td>
        ADDRESS\_RESOLUTION\_IS\_FAILED
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        E1607
      </td>

      <td>
        Transaction failed due to user pressing back button.
      </td>

      <td>
        BACK\_BUTTON\_PRESSED
      </td>

      <td>
        BACK\_BUTTON\_PRESSED
      </td>
    </tr>

    <tr>
      <td>
        E1703
      </td>

      <td>
        Auth Data mismatch
      </td>

      <td>
        AUTH\_DATA\_MISMATCH
      </td>

      <td>
        AUTH\_DATA\_MISMATCH
      </td>
    </tr>

    <tr>
      <td>
        E1001
      </td>

      <td>
        Bank network is unavailable at the moment.
      </td>

      <td>
        AUTHENTICATION\_SERVICE\_UNAVAILABLE\_ASU
      </td>

      <td>
        AUTHENTICATION\_SERVICE\_UNAVAILABLE\_ASU
      </td>
    </tr>

    <tr>
      <td>
        E334
      </td>

      <td>
        Authentication service not available
      </td>

      <td>
        AUTHENTICATION\_SERVICE\_UNAVAILABLE
      </td>

      <td>
        AUTHENTICATION\_SERVICE\_UNAVAILABLE
      </td>
    </tr>

    <tr>
      <td>
        E1003
      </td>

      <td>
        Card not enabled for Ecomm transactions, either the card is newly issued or has not been used for any online transaction during last 12 months
      </td>

      <td>
        AUTHENTICATION\_NOT\_ATTEMPTED
      </td>

      <td>
        AUTHENTICATION\_NOT\_ATTEMPTED
      </td>
    </tr>

    <tr>
      <td>
        E914
      </td>

      <td>
        Transaction failed by Acquirer due to invalid request
      </td>

      <td>
        AUTHENTICATION\_INVALID\_REQUEST\_ERROR
      </td>

      <td>
        AUTHENTICATION\_INVALID\_REQUEST\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E1910
      </td>

      <td>
        Authentication failed or invalid PaRes received
      </td>

      <td>
        AUTHENTICATION\_INVALID\_PARES
      </td>

      <td>
        AUTHENTICATION\_INVALID\_PARES
      </td>
    </tr>

    <tr>
      <td>
        E916
      </td>

      <td>
        Transaction failed due to invalid merchant config at Acquirer
      </td>

      <td>
        AUTHENTICATION\_INVALID\_MERCHANT\_CONFIG
      </td>

      <td>
        AUTHENTICATION\_INVALID\_MERCHANT\_CONFIG
      </td>
    </tr>

    <tr>
      <td>
        E915
      </td>

      <td>
        Transaction failed by Acquirer due to invalid request data
      </td>

      <td>
        AUTHENTICATION\_INVALID\_DATA\_ERROR
      </td>

      <td>
        AUTHENTICATION\_INVALID\_DATA\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E917
      </td>

      <td>
        Transaction failed due to card authentication failure
      </td>

      <td>
        AUTHENTICATION\_FAILURE
      </td>

      <td>
        AUTHENTICATION\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E232
      </td>

      <td>
        Payer could not be authenticated
      </td>

      <td>
        AUTHENTICATION\_ATTEMPTS
      </td>

      <td>
        AUTHENTICATION\_ATTEMPTS
      </td>
    </tr>

    <tr>
      <td>
        E1002
      </td>

      <td>
        Authentication was attempted but was not available at banks end
      </td>

      <td>
        AUTHENTICATION\_ATTEMPTED
      </td>

      <td>
        AUTHENTICATION\_ATTEMPTED
      </td>
    </tr>

    <tr>
      <td>
        E600
      </td>

      <td>
        Bank denied transaction on the card.
      </td>

      <td>
        Authentication declined by issuer
      </td>

      <td>
        PAYU\_API\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E1602
      </td>

      <td>
        Transaction failed. Page expired due to no user input.
      </td>

      <td>
        ATM\_PIN\_PAGE\_EXPIRED
      </td>

      <td>
        OTP\_PAGE\_EXPIRED
      </td>
    </tr>

    <tr>
      <td>
        E9233
      </td>

      <td>
        ARQC validation failed by Issuer
      </td>

      <td>
        ARQC validation failed by Issuer
      </td>

      <td>
        ARQC\_VALIDATION\_FAILED\_BY\_ISSUER
      </td>
    </tr>

    <tr>
      <td>
        E9203
      </td>

      <td>
        Approved VIP (not used)
      </td>

      <td>
        Approved VIP (not used)
      </td>

      <td>
        APPROVED\_VIP
      </td>
    </tr>

    <tr>
      <td>
        E9204
      </td>

      <td>
        Approved Update Track 3 (not used)
      </td>

      <td>
        Approved Update Track 3 (not used)
      </td>

      <td>
        APPROVED\_TRACK
      </td>
    </tr>

    <tr>
      <td>
        E9222
      </td>

      <td>
        Approved (ANZ only)
      </td>

      <td>
        Approved (ANZ only)
      </td>

      <td>
        APPROVED\_ANZ\_ONLY
      </td>
    </tr>

    <tr>
      <td>
        E220
      </td>

      <td>
        Amount or transaction doesnt match
      </td>

      <td>
        AMOUNT\_TRANSACTION\_MISMATCH
      </td>

      <td>
        AMOUNT\_TRANSACTION\_MISMATCH
      </td>
    </tr>

    <tr>
      <td>
        E4092
      </td>

      <td>
        AMOUNT RULE SHOULD BE ALWAYS MAX IF PURPOSE=01
      </td>

      <td>
        AMOUNT RULE SHOULD BE ALWAYS MAX IF PURPOSE=01
      </td>

      <td>
        AMOUNT\_RULE\_SHOULD\_BE\_ALWAYS\_MAX\_IF\_PURPOSE\_01
      </td>
    </tr>

    <tr>
      <td>
        E4161
      </td>

      <td>
        AMOUNT OR CURRENCY MISMATCH
      </td>

      <td>
        AMOUNT OR CURRENCY MISMATCH
      </td>

      <td>
        AMOUNT\_OR\_CURRENCY\_MISMATCH
      </td>
    </tr>

    <tr>
      <td>
        E4151
      </td>

      <td>
        Transaction failed due to amount limit on merchant exceeded
      </td>

      <td>
        AMOUNT CAP IS EXCEEDED
      </td>

      <td>
        AMOUNT\_CAP\_IS\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        EA08
      </td>

      <td>
        Alt ID Provisioning Failed
      </td>

      <td>
        Alt ID Provisioning Failed due to incorrect Card Details
      </td>

      <td>
        ALT\_ID\_PROV
      </td>
    </tr>

    <tr>
      <td>
        E9217
      </td>

      <td>
        Allowable PIN Tries Exceeded
      </td>

      <td>
        Allowable PIN Tries Exceeded
      </td>

      <td>
        ALLOWABLE\_PIN\_TRIES\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E708
      </td>

      <td>
        Card authentication failed as user exceeded maximum number of permitted retries for PIN.
      </td>

      <td>
        Allowable number of PIN tries exceeded
      </td>

      <td>
        PIN\_RETRIES\_EXCEEDED
      </td>
    </tr>

    <tr>
      <td>
        E4037
      </td>

      <td>
        Transaction failed due to funds blocked for mandate in customer's account
      </td>

      <td>
        ADEQUATE FUNDS NOT AVAILABLE IN THE ACCOUNT BECAUSE FUNDS HAVE B
      </td>

      <td>
        ADEQUATE\_FUNDS\_NOT\_AVAILABLE\_IN\_THE\_ACCOUNT\_BECAUSE\_FUNDS\_HAVE\_BEEN\_BD\_BLOCKED\_FOR\_MANDATE
      </td>
    </tr>

    <tr>
      <td>
        E304
      </td>

      <td>
        The address needs to match with the records of card issuing bank
      </td>

      <td>
        ADDRESS\_INVALID
      </td>

      <td>
        ADDRESS\_INVALID
      </td>
    </tr>

    <tr>
      <td>
        E4013
      </td>

      <td>
        Transaction failed due to beneficiary timeout
      </td>

      <td>
        ACQUIRER/BENEFICIARY UNAVAILABLE(TIMEOUT)
      </td>

      <td>
        ACQUIRER\_BENEFICIARY\_UNAVAILABLE\_TIMEOUT
      </td>
    </tr>

    <tr>
      <td>
        E4232
      </td>

      <td>
        ACCTYPE IS NOT SUPPORTED (OD)
      </td>

      <td>
        ACCTYPE IS NOT SUPPORTED (OD)
      </td>

      <td>
        ACCTYPE\_IS\_NOT\_SUPPORTED\_OD
      </td>
    </tr>

    <tr>
      <td>
        E4340
      </td>

      <td>
        Transaction failed due to account details not found at customer's bank
      </td>

      <td>
        ACCOUNT DOES NOT EXIST (REMITTER)
      </td>

      <td>
        ACCOUNT\_DOES\_NOT\_EXIST\_REMITTER
      </td>
    </tr>

    <tr>
      <td>
        E4341
      </td>

      <td>
        Transaction failed due to account details not found at acquirer's bank
      </td>

      <td>
        ACCOUNT DOES NOT EXIST (BENEFICIARY)
      </td>

      <td>
        ACCOUNT\_DOES\_NOT\_EXIST\_BENEFICIARY
      </td>
    </tr>

    <tr>
      <td>
        E324
      </td>

      <td>
        Transaction was declined by the issuing bank due to suspected fraudulent activities
      </td>

      <td>
        Suspected Fraud, Retain Card
      </td>

      <td>
        CARD\_FRAUD\_SUSPECTED
      </td>
    </tr>

    <tr>
      <td>
        E325
      </td>

      <td>
        Transaction declined due to card not enabled for online transactions or user / Bank Defined Restrictions
      </td>

      <td>
        Restricted Card, Retain Card
      </td>

      <td>
        RESTRICTED\_CARD
      </td>
    </tr>

    <tr>
      <td>
        E313
      </td>

      <td>
        Card authentication failed at the bank due to invalid CVV (or CVC or Card Security Code)
      </td>

      <td>
        Negative online CAM, dCVV, iCVV, CVV, or CAVV results or Offlin
      </td>

      <td>
        CVC\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E1652
      </td>

      <td>
        Card blocked
      </td>

      <td>
        nan
      </td>

      <td>
        CARD\_BLOCKED
      </td>
    </tr>

    <tr>
      <td>
        E502
      </td>

      <td>
        Transaction cancelled by customer
      </td>

      <td>
        nan
      </td>

      <td>
        TRANSACTION\_ABORTED
      </td>
    </tr>

    <tr>
      <td>
        E228
      </td>

      <td>
        Transaction is Deferred
      </td>

      <td>
        nan
      </td>

      <td>
        TRANSACTION\_DEFERRED
      </td>
    </tr>

    <tr>
      <td>
        E501
      </td>

      <td>
        Bank was unable to authenticate.
      </td>

      <td>
        nan
      </td>

      <td>
        DEFAULT\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E905
      </td>

      <td>
        Transaction declined
      </td>

      <td>
        nan
      </td>

      <td>
        USER\_DECLINED
      </td>
    </tr>

    <tr>
      <td>
        E314
      </td>

      <td>
        The address needs to match with the records of card issuing bank
      </td>

      <td>
        nan
      </td>

      <td>
        ADDRESS\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E216
      </td>

      <td>
        Submitting multiple transactions in a single file is an efficient way to upload credit card and electronic check transaction data from enterprise applications or other file-based systems. Error occurred during batch processing of the cards.
      </td>

      <td>
        nan
      </td>

      <td>
        BATCH\_ERROR
      </td>
    </tr>

    <tr>
      <td>
        E316
      </td>

      <td>
        Bank failed to authenticate the customer due to 3D Secure Authentication decline
      </td>

      <td>
        nan
      </td>

      <td>
        SECURE\_3D\_NOT\_ENROLLED
      </td>
    </tr>

    <tr>
      <td>
        E1636
      </td>

      <td>
        Transaction time out
      </td>

      <td>
        nan
      </td>

      <td>
        TRANSACTION\_TIMEOUT
      </td>
    </tr>

    <tr>
      <td>
        E1302
      </td>

      <td>
        Bank failed to authenticate the customer due to 3D Secure Enrollment decline
      </td>

      <td>
        nan
      </td>

      <td>
        NOT\_ENROLLED\_FAILURE
      </td>
    </tr>

    <tr>
      <td>
        E202
      </td>

      <td>
        Card authentication failure
      </td>

      <td>
        nan
      </td>

      <td>
        TRANSACTION\_INVALID
      </td>
    </tr>
  </tbody>
</Table>
