---
title: Issuer Decline Error Codes
deprecated: false
hidden: false
metadata:
  robots: index
---
<Table align={["right","left","left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "right" }}>
        Response Code
      </th>

      <th style={{ textAlign: "left" }}>
        PayU Error Code
      </th>

      <th style={{ textAlign: "left" }}>
        Title
      </th>

      <th style={{ textAlign: "left" }}>
        Error Description
      </th>

      <th style={{ textAlign: "left" }}>
        Error Message / Reason
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "right" }}>
        0
      </td>

      <td style={{ textAlign: "left" }}>
        E000
      </td>

      <td style={{ textAlign: "left" }}>
        NO\_ERROR
      </td>

      <td style={{ textAlign: "left" }}>
        Approved or completed successfully
      </td>

      <td style={{ textAlign: "left" }}>
        No Error
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        1
      </td>

      <td style={{ textAlign: "left" }}>
        E348
      </td>

      <td style={{ textAlign: "left" }}>
        ISSUER\_DECLINED
      </td>

      <td style={{ textAlign: "left" }}>
        Refer to card issuer
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction declined by the issuer
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        3
      </td>

      <td style={{ textAlign: "left" }}>
        E341
      </td>

      <td style={{ textAlign: "left" }}>
        INVALID\_MERCHANT
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid Merchant
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction failed due to invalid merchant
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        4
      </td>

      <td style={{ textAlign: "left" }}>
        E310
      </td>

      <td style={{ textAlign: "left" }}>
        LOST\_CARD
      </td>

      <td style={{ textAlign: "left" }}>
        Pick Up Card
      </td>

      <td style={{ textAlign: "left" }}>
        Card has been classified as lost and has been blocked.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        5
      </td>

      <td style={{ textAlign: "left" }}>
        E307
      </td>

      <td style={{ textAlign: "left" }}>
        DO\_NOT\_HONOUR
      </td>

      <td style={{ textAlign: "left" }}>
        Do not honor
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction declined with do not honor
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        6
      </td>

      <td style={{ textAlign: "left" }}>
        E1903
      </td>

      <td style={{ textAlign: "left" }}>
        AUTHORIZATION\_FAILED\_
        BY\_BANK
      </td>

      <td style={{ textAlign: "left" }}>
        Payment could not be authorised
      </td>

      <td style={{ textAlign: "left" }}>
        Authorization failed at Bank
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        10
      </td>

      <td style={{ textAlign: "left" }}>
        E9202
      </td>

      <td style={{ textAlign: "left" }}>
        PARTIAL\_AMOUNT\_
        APPROVED
      </td>

      <td style={{ textAlign: "left" }}>
        Partial Amount Approved
      </td>

      <td style={{ textAlign: "left" }}>
        Partial Amount Approved
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        11
      </td>

      <td style={{ textAlign: "left" }}>
        E9203
      </td>

      <td style={{ textAlign: "left" }}>
        APPROVED\_VIP
      </td>

      <td style={{ textAlign: "left" }}>
        Approved VIP (not used)
      </td>

      <td style={{ textAlign: "left" }}>
        Approved VIP (not used)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        12
      </td>

      <td style={{ textAlign: "left" }}>
        E207
      </td>

      <td style={{ textAlign: "left" }}>
        INVALID\_TRANSACTION
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid transaction
      </td>

      <td style={{ textAlign: "left" }}>
        Bank denied transaction on the card.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        13
      </td>

      <td style={{ textAlign: "left" }}>
        E715
      </td>

      <td style={{ textAlign: "left" }}>
        INVALID\_AMOUNT
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid amount
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid amount sent to the bank
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        14
      </td>

      <td style={{ textAlign: "left" }}>
        E1632
      </td>

      <td style={{ textAlign: "left" }}>
        CARD\_VALIDATION\_
        FAILED
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid card number
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction declined due to either incorrect cvv/expiry or card validation failure
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        15
      </td>

      <td style={{ textAlign: "left" }}>
        E305
      </td>

      <td style={{ textAlign: "left" }}>
        CARD\_NUMBER\_
        INVALID
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid issuer
      </td>

      <td style={{ textAlign: "left" }}>
        The transaction failed due to invalid or absent card number.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        16
      </td>

      <td style={{ textAlign: "left" }}>
        E9204
      </td>

      <td style={{ textAlign: "left" }}>
        APPROVED\_TRACK
      </td>

      <td style={{ textAlign: "left" }}>
        Approved Update Track 3 (not used)
      </td>

      <td style={{ textAlign: "left" }}>
        Approved Update Track 3 (not used)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        17
      </td>

      <td style={{ textAlign: "left" }}>
        E9205
      </td>

      <td style={{ textAlign: "left" }}>
        CUSTOMER\_
        CANCELLATION
      </td>

      <td style={{ textAlign: "left" }}>
        Customer Cancellation
      </td>

      <td style={{ textAlign: "left" }}>
        Customer Cancellation
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        18
      </td>

      <td style={{ textAlign: "left" }}>
        E9206
      </td>

      <td style={{ textAlign: "left" }}>
        CUSTOMER\_DISPUTE
      </td>

      <td style={{ textAlign: "left" }}>
        Customer Dispute
      </td>

      <td style={{ textAlign: "left" }}>
        Customer Dispute
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        19
      </td>

      <td style={{ textAlign: "left" }}>
        E345
      </td>

      <td style={{ textAlign: "left" }}>
        TECHNICAL\_FAILURE
      </td>

      <td style={{ textAlign: "left" }}>
        Re-enter Transaction
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction declined due to technical failure
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        20
      </td>

      <td style={{ textAlign: "left" }}>
        E308
      </td>

      <td style={{ textAlign: "left" }}>
        TRANSACTION\_FAILED
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid response
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction Failed at bank end.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        21
      </td>

      <td style={{ textAlign: "left" }}>
        E9207
      </td>

      <td style={{ textAlign: "left" }}>
        NO\_ACTION\_TAKEN\_
      </td>

      <td style={{ textAlign: "left" }}>
        No Action Taken
      </td>

      <td style={{ textAlign: "left" }}>
        No Action Taken
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        22
      </td>

      <td style={{ textAlign: "left" }}>
        E9208
      </td>

      <td style={{ textAlign: "left" }}>
        SUSPECTED\_
        MALFUNCTION
      </td>

      <td style={{ textAlign: "left" }}>
        Suspected Malfunction
      </td>

      <td style={{ textAlign: "left" }}>
        Suspected Malfunction
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        23
      </td>

      <td style={{ textAlign: "left" }}>
        E9209
      </td>

      <td style={{ textAlign: "left" }}>
        UNACCEPTABLE\_
        TRANSACTION\_FEE
      </td>

      <td style={{ textAlign: "left" }}>
        Unacceptable Transaction Fee
      </td>

      <td style={{ textAlign: "left" }}>
        Unacceptable Transaction Fee
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        24
      </td>

      <td style={{ textAlign: "left" }}>
        E9210
      </td>

      <td style={{ textAlign: "left" }}>
        FILE\_UPDATE\_NOT\_
        SUPPORTED\_BY\_RECEIVER
      </td>

      <td style={{ textAlign: "left" }}>
        File Update not Supported by receiver
      </td>

      <td style={{ textAlign: "left" }}>
        File Update not Supported by receiver
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        25
      </td>

      <td style={{ textAlign: "left" }}>
        E9211
      </td>

      <td style={{ textAlign: "left" }}>
        UNABLE\_TO\_LOCATE\_
        RECORD\_ON\_FILE
      </td>

      <td style={{ textAlign: "left" }}>
        Unable to Locate Record on File
      </td>

      <td style={{ textAlign: "left" }}>
        Unable to Locate Record on File
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        26
      </td>

      <td style={{ textAlign: "left" }}>
        E9212
      </td>

      <td style={{ textAlign: "left" }}>
        DUPLICATE\_FILE\_
        UPDATE\_RECORD
      </td>

      <td style={{ textAlign: "left" }}>
        Duplicate File Update Record
      </td>

      <td style={{ textAlign: "left" }}>
        Duplicate File Update Record
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        27
      </td>

      <td style={{ textAlign: "left" }}>
        E9213
      </td>

      <td style={{ textAlign: "left" }}>
        FILE\_UPDATE\_
        FIELD\_EDIT\_ERROR
      </td>

      <td style={{ textAlign: "left" }}>
        File Update Field Edit Error
      </td>

      <td style={{ textAlign: "left" }}>
        File Update Field Edit Error
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        28
      </td>

      <td style={{ textAlign: "left" }}>
        E9214
      </td>

      <td style={{ textAlign: "left" }}>
        FILE\_UPDATE\_
        FILE\_LOCKED\_OUT
      </td>

      <td style={{ textAlign: "left" }}>
        File Update File Locked Out
      </td>

      <td style={{ textAlign: "left" }}>
        File Update File Locked Out
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        29
      </td>

      <td style={{ textAlign: "left" }}>
        E9215
      </td>

      <td style={{ textAlign: "left" }}>
        FILE\_UPDATE\_
        NOT\_SUCCESSFUL
      </td>

      <td style={{ textAlign: "left" }}>
        File Update not Successful
      </td>

      <td style={{ textAlign: "left" }}>
        File Update not Successful
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        30
      </td>

      <td style={{ textAlign: "left" }}>
        E2102
      </td>

      <td style={{ textAlign: "left" }}>
        TXN\_FAILURE
      </td>

      <td style={{ textAlign: "left" }}>
        Format error
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction not approved
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        32
      </td>

      <td style={{ textAlign: "left" }}>
        E9216
      </td>

      <td style={{ textAlign: "left" }}>
        COMPLETED\_
        PARTIALLY
      </td>

      <td style={{ textAlign: "left" }}>
        Completed Partially
      </td>

      <td style={{ textAlign: "left" }}>
        Completed Partially
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        34
      </td>

      <td style={{ textAlign: "left" }}>
        E324
      </td>

      <td style={{ textAlign: "left" }}>
        CARD\_FRAUD\_
        SUSPECTED
      </td>

      <td style={{ textAlign: "left" }}>
        Suspected Fraud, Retain Card
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction was declined by the issuing bank due to suspected fraudulent activities
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        36
      </td>

      <td style={{ textAlign: "left" }}>
        E325
      </td>

      <td style={{ textAlign: "left" }}>
        RESTRICTED\_
        CARD
      </td>

      <td style={{ textAlign: "left" }}>
        Restricted Card, Retain Card
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction declined due to card not enabled for online transactions or user / Bank Defined Restrictions
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        38
      </td>

      <td style={{ textAlign: "left" }}>
        E9217
      </td>

      <td style={{ textAlign: "left" }}>
        ALLOWABLE\_PIN\_
        TRIES\_EXCEEDED
      </td>

      <td style={{ textAlign: "left" }}>
        Allowable PIN Tries Exceeded
      </td>

      <td style={{ textAlign: "left" }}>
        Allowable PIN Tries Exceeded
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        39
      </td>

      <td style={{ textAlign: "left" }}>
        E224
      </td>

      <td style={{ textAlign: "left" }}>
        VIRTUAL\_ACCOUNT\_
        NUMBER\_MISMATCH
      </td>

      <td style={{ textAlign: "left" }}>
        No credit account
      </td>

      <td style={{ textAlign: "left" }}>
        Virtual Account Number Mismatch
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        40
      </td>

      <td style={{ textAlign: "left" }}>
        E9218
      </td>

      <td style={{ textAlign: "left" }}>
        REQUESTED\_FUNCTION\_
        NOT\_SUPPORTED
      </td>

      <td style={{ textAlign: "left" }}>
        Requested Function not Supported
      </td>

      <td style={{ textAlign: "left" }}>
        Requested Function not Supported
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        42
      </td>

      <td style={{ textAlign: "left" }}>
        E9252
      </td>

      <td style={{ textAlign: "left" }}>
        NO\_UNIVERSAL\_
        ACCOUNT
      </td>

      <td style={{ textAlign: "left" }}>
        No Universal Account
      </td>

      <td style={{ textAlign: "left" }}>
        The customer\&#039s card issuer has declined the transaction as the account type selected is not valid for this credit card number.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        46
      </td>

      <td style={{ textAlign: "left" }}>
        E717
      </td>

      <td style={{ textAlign: "left" }}>
        INVALID\_ACCOUNT\_
        NUMBER
      </td>

      <td style={{ textAlign: "left" }}>
        Closed account
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction declined as bank reported account to be closed
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        51
      </td>

      <td style={{ textAlign: "left" }}>
        E706
      </td>

      <td style={{ textAlign: "left" }}>
        INSUFFICIENT\_
        FUNDS
      </td>

      <td style={{ textAlign: "left" }}>
        Insufficient funds/over credit limit / Not sufficient funds
      </td>

      <td style={{ textAlign: "left" }}>
        The account against which the payment was made has insufficient funds.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        52
      </td>

      <td style={{ textAlign: "left" }}>
        E707
      </td>

      <td style={{ textAlign: "left" }}>
        INVALID\_PAN
      </td>

      <td style={{ textAlign: "left" }}>
        No Checking Account
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction failed due to invalid Primary Account Number. (Primary Account Number or PAN is the number that is embossed and/or encoded on a plastic card that identifies the issuer and the particular cardholder account.)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        54
      </td>

      <td style={{ textAlign: "left" }}>
        E311
      </td>

      <td style={{ textAlign: "left" }}>
        EXPIRED\_CARD
      </td>

      <td style={{ textAlign: "left" }}>
        Expired card
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction declined due to invalid expiry details or the card is expired
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        55
      </td>

      <td style={{ textAlign: "left" }}>
        E710
      </td>

      <td style={{ textAlign: "left" }}>
        INVALID\_PIN
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid PIN
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction failed due to invalid PIN
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        56
      </td>

      <td style={{ textAlign: "left" }}>
        E4346
      </td>

      <td style={{ textAlign: "left" }}>
        NO\_CARD\_
        RECORD\_REMITTER
      </td>

      <td style={{ textAlign: "left" }}>
        No Card Record
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction failed due to no card details from customer's bank
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        57
      </td>

      <td style={{ textAlign: "left" }}>
        E1642
      </td>

      <td style={{ textAlign: "left" }}>
        CARD\_NOT\_
        PERMITTED
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction not permitted to issuer/cardholder
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction not permitted to cardholder
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        60
      </td>

      <td style={{ textAlign: "left" }}>
        E337
      </td>

      <td style={{ textAlign: "left" }}>
        NOT\_CAPTURED
      </td>

      <td style={{ textAlign: "left" }}>
        Contact Card Acquirer
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction declined by the issuer
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        61
      </td>

      <td style={{ textAlign: "left" }}>
        E909
      </td>

      <td style={{ textAlign: "left" }}>
        TRANSACTION\_MAX\_
        LIMIT\_EXCEEDED
      </td>

      <td style={{ textAlign: "left" }}>
        Exceeds withdrawal amount limit(s) / Withdrawal amount limit exc
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction amount exceeds the withdrawal limit of the user account
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        62
      </td>

      <td style={{ textAlign: "left" }}>
        E1626
      </td>

      <td style={{ textAlign: "left" }}>
        RESTRICTED\_CARD\_TYPE
      </td>

      <td style={{ textAlign: "left" }}>
        Restricted card
      </td>

      <td style={{ textAlign: "left" }}>
        Restricted card
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        63
      </td>

      <td style={{ textAlign: "left" }}>
        E312
      </td>

      <td style={{ textAlign: "left" }}>
        BANK\_DENIED
      </td>

      <td style={{ textAlign: "left" }}>
        Security violation
      </td>

      <td style={{ textAlign: "left" }}>
        Bank denied transaction on the card.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        64
      </td>

      <td style={{ textAlign: "left" }}>
        E9253
      </td>

      <td style={{ textAlign: "left" }}>
        AMOUNT\_INCORRECT\_
        MISMATCH
      </td>

      <td style={{ textAlign: "left" }}>
        Original Amount Incorrect
      </td>

      <td style={{ textAlign: "left" }}>
        Amount Incorrect / Mismatch
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        66
      </td>

      <td style={{ textAlign: "left" }}>
        E9219
      </td>

      <td style={{ textAlign: "left" }}>
        CARD\_ACCEPTOR\_CALL\_
        ACQUIRER\_SECURITY
      </td>

      <td style={{ textAlign: "left" }}>
        Card Acceptor Call Acquirer Security
      </td>

      <td style={{ textAlign: "left" }}>
        Card Acceptor Call Acquirer Security
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        68
      </td>

      <td style={{ textAlign: "left" }}>
        E9220
      </td>

      <td style={{ textAlign: "left" }}>
        RESPONSE\_RECEIVED\_
        TOO\_LATE
      </td>

      <td style={{ textAlign: "left" }}>
        Response Received Too Late
      </td>

      <td style={{ textAlign: "left" }}>
        Response Received Too Late
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        69
      </td>

      <td style={{ textAlign: "left" }}>
        E9221
      </td>

      <td style={{ textAlign: "left" }}>
        MOBILE\_NUMBER\_
        RECORD\_NOT\_FOUND
      </td>

      <td style={{ textAlign: "left" }}>
        Mobile number record not found / mis-match
      </td>

      <td style={{ textAlign: "left" }}>
        Mobile number record not found / mis-match
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        70
      </td>

      <td style={{ textAlign: "left" }}>
        E1629
      </td>

      <td style={{ textAlign: "left" }}>
        BANK\_TECHNICAL\_
        FAILURE
      </td>

      <td style={{ textAlign: "left" }}>
        Contact Card Issuer
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction declined due to technical failure at bank end
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        75
      </td>

      <td style={{ textAlign: "left" }}>
        E708
      </td>

      <td style={{ textAlign: "left" }}>
        PIN\_RETRIES\_EXCEEDED
      </td>

      <td style={{ textAlign: "left" }}>
        Allowable number of PIN tries exceeded
      </td>

      <td style={{ textAlign: "left" }}>
        Card authentication failed as user exceeded maximum number of permitted retries for PIN.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        77
      </td>

      <td style={{ textAlign: "left" }}>
        E9222
      </td>

      <td style={{ textAlign: "left" }}>
        APPROVED\_ANZ\_
        ONLY
      </td>

      <td style={{ textAlign: "left" }}>
        Approved (ANZ only)
      </td>

      <td style={{ textAlign: "left" }}>
        Approved (ANZ only)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        78
      </td>

      <td style={{ textAlign: "left" }}>
        E1625
      </td>

      <td style={{ textAlign: "left" }}>
        CARD\_NOT\_ENABLED\_
        FOR\_ECOMM\_TXN
      </td>

      <td style={{ textAlign: "left" }}>
        Invalid/nonexistent account specified (general)
      </td>

      <td style={{ textAlign: "left" }}>
        Card not enabled for Ecomm transactions, either the card is newly issued or has not been used for any online transaction during last 12 months
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        81
      </td>

      <td style={{ textAlign: "left" }}>
        E9223
      </td>

      <td style={{ textAlign: "left" }}>
        CRYPTOGRAPHIC\_
        ERROR
      </td>

      <td style={{ textAlign: "left" }}>
        Cryptographic Error
      </td>

      <td style={{ textAlign: "left" }}>
        Cryptographic Error
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        82
      </td>

      <td style={{ textAlign: "left" }}>
        E313
      </td>

      <td style={{ textAlign: "left" }}>
        CVC\_FAILURE
      </td>

      <td style={{ textAlign: "left" }}>
        Negative online CAM, dCVV, iCVV, CVV, or CAVV results or Offlin
      </td>

      <td style={{ textAlign: "left" }}>
        Card authentication failed at the bank due to invalid CVV (or CVC or Card Security Code)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        86
      </td>

      <td style={{ textAlign: "left" }}>
        E4519
      </td>

      <td style={{ textAlign: "left" }}>
        Insufficient\_Amount
      </td>

      <td style={{ textAlign: "left" }}>
        Cannot verify PIN
      </td>

      <td style={{ textAlign: "left" }}>
        Refund failed due to insufficient amount
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        87
      </td>

      <td style={{ textAlign: "left" }}>
        E9224
      </td>

      <td style={{ textAlign: "left" }}>
        NO\_ENVELOPE\_
        INSERTED
      </td>

      <td style={{ textAlign: "left" }}>
        No Envelope Inserted
      </td>

      <td style={{ textAlign: "left" }}>
        No Envelope Inserted
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        88
      </td>

      <td style={{ textAlign: "left" }}>
        E9225
      </td>

      <td style={{ textAlign: "left" }}>
        UNABLE\_TO\_
        DISPENSE
      </td>

      <td style={{ textAlign: "left" }}>
        Unable to Dispense
      </td>

      <td style={{ textAlign: "left" }}>
        Unable to Dispense
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        89
      </td>

      <td style={{ textAlign: "left" }}>
        E9226
      </td>

      <td style={{ textAlign: "left" }}>
        TID\_NOT\_
        PRESENT\_ON\_HOST
      </td>

      <td style={{ textAlign: "left" }}>
        TID not present on host
      </td>

      <td style={{ textAlign: "left" }}>
        TID not present on host
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        90
      </td>

      <td style={{ textAlign: "left" }}>
        E9227
      </td>

      <td style={{ textAlign: "left" }}>
        CUTOFF\_IN\_
        PROGRESS
      </td>

      <td style={{ textAlign: "left" }}>
        Cut-off in Progress
      </td>

      <td style={{ textAlign: "left" }}>
        Cut-off in Progress
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        91
      </td>

      <td style={{ textAlign: "left" }}>
        E9254
      </td>

      <td style={{ textAlign: "left" }}>
        BANK\_NOT\_
        SUPPORTED\_BY\_
        SWITCH
      </td>

      <td style={{ textAlign: "left" }}>
        Issuer or Switch is Inoperative
      </td>

      <td style={{ textAlign: "left" }}>
        Authorization Platform or Switch / Issuer system inoperative or Not Supported
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        91
      </td>

      <td style={{ textAlign: "left" }}>
        E4158
      </td>

      <td style={{ textAlign: "left" }}>
        REQAUTH\_TIME\_
        OUT\_FOR\_PAY
      </td>

      <td style={{ textAlign: "left" }}>
        Issuer unavailable or switch inoperative
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction failed due to timeout at acquirer's end
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        92
      </td>

      <td style={{ textAlign: "left" }}>
        E225
      </td>

      <td style={{ textAlign: "left" }}>
        TRANSACTION\_
        IN\_PROGRESS
      </td>

      <td style={{ textAlign: "left" }}>
        Destination cannot be found for routing / Unable to route transa
      </td>

      <td style={{ textAlign: "left" }}>
        Transaction in Progress
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        94
      </td>

      <td style={{ textAlign: "left" }}>
        E504
      </td>

      <td style={{ textAlign: "left" }}>
        DUPLICATE\_
        TRANSACTION
      </td>

      <td style={{ textAlign: "left" }}>
        Duplicate Transaction
      </td>

      <td style={{ textAlign: "left" }}>
        The transaction has been identified as duplicate transaction.
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        95
      </td>

      <td style={{ textAlign: "left" }}>
        E1656
      </td>

      <td style={{ textAlign: "left" }}>
        RECONCILE\_ERROR
      </td>

      <td style={{ textAlign: "left" }}>
        Reconcile Error
      </td>

      <td style={{ textAlign: "left" }}>
        Reconcile Error
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        97
      </td>

      <td style={{ textAlign: "left" }}>
        E9229
      </td>

      <td style={{ textAlign: "left" }}>
        RECONCILIATION\_
        TOTALS\_RESET
      </td>

      <td style={{ textAlign: "left" }}>
        Reconciliation Totals Reset
      </td>

      <td style={{ textAlign: "left" }}>
        Reconciliation Totals Reset
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        98
      </td>

      <td style={{ textAlign: "left" }}>
        E9230
      </td>

      <td style={{ textAlign: "left" }}>
        EXCEEDS\_CASH\_
        LIMIT
      </td>

      <td style={{ textAlign: "left" }}>
        Exceeds Cash Limit
      </td>

      <td style={{ textAlign: "left" }}>
        Exceeds Cash Limit
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "right" }}>
        99
      </td>

      <td style={{ textAlign: "left" }}>
        E9231
      </td>

      <td style={{ textAlign: "left" }}>
        RESERVED\_FOR\_
        NATIONAL\_USE
      </td>

      <td style={{ textAlign: "left" }}>
        Reserved for National Use
      </td>

      <td style={{ textAlign: "left" }}>
        Reserved for National Use
      </td>
    </tr>
  </tbody>
</Table>