---
title: Change Wallet Status API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **Change Wallet Status** API allows you to change the operational status of a wallet. This includes temporarily blocking, marking as dormant, or permanently closing a wallet. This API is essential for wallet lifecycle management and compliance requirements.

<br />

| Status       | Description                                                                                                                                                                  |   |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | - |
| Active       | Wallet is in the active state, it can used for all sorts of transactions.                                                                                                    |   |
| Custom       | Wallet will be Custom Blocked (partial transactions will be allowed): <br/> * Cashback and refund can be received.<br/> * Load can be blocked while unload may work or vice versa.  |   |
| Temporary    | Wallet will be Temporary Blocked (No transactions will be permitted)                                                                                                         |   |
| Permanent    | Wallet will be permanently blocked                                                                                                                                           |   |
| Closed       | Wallet will be closed                                                                                                                                                        |   |
| Debit        | All debits from the wallet will be temporarily blocked                                                                                                                       |   |
| Credit       | All credits to the wallet will be temporarily blocked                                                                                                                        |   |
| CreditDebit  | All Credits and Debits will not be allowed, except system reversal credits and debits.                                                                                       |   |
| Dormant      | Wallet will be in a dormant state. (same as temporary blocked)                                                                                                               |   |

## Environment

| Environment | URL                                                                        |
| ----------- | -------------------------------------------------------------------------- |
| Test        | `https://apitest.payu.in/loyalty-points/v1/wallet/onboarding/walletStatus` |
| Production  | `https://api.payu.in/loyalty-points/v1/wallet/onboarding/walletStatus`     |

**HTTP Method**: PATCH

## Request Headers

<Closed_Loop_HMAC />

## Request Parameters

<HTMLBlock>{`
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Description</th>
            <th>Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>messageCode<br><code>mandatory</code></td>
            <td><code>Numeric(4)</code> Unique API ID for wallet status change. Only the value <code>3530</code> is allowed</td>
            <td>3530</td>
        </tr>
        <tr>
            <td>clientTxnId<br><code>mandatory</code></td>
            <td><code>String(100)</code> Unique transaction ID for each request</td>
            <td>CBL-458</td>
        </tr>
        <tr>
            <td>requestDateTime<br><code>mandatory</code></td>
            <td><code>Numeric(14)</code> Local timestamp when request was initiated (YYYYMMDDHHMMSS)</td>
            <td>20220514181818</td>
        </tr>
        <tr>
            <td>accountNumber<br><code>mandatory</code></td>
            <td><code>String(15)</code> Unique account number for the sub-wallet</td>
            <td>2000123hh</td>
        </tr>
        <tr>
            <td>statusType<br><code>mandatory</code></td>
            <td><code>String(10)</code> Status type to set</td>
            <td>CreditDebit</td>
        </tr>
        <tr>
            <td>reason<br><code>optional</code></td>
            <td><code>String(100)</code> Reason for status change</td>
            <td>Customer request</td>
        </tr>
        <tr>
            <td>remarks<br><code>optional</code></td>
            <td><code>String(255)</code> Additional remarks</td>
            <td>Temporary block due to suspicious activity</td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

## Sample Request

```curl
curl --location --request PATCH 'https://apitest.payu.in/loyalty-points/v1/wallet/onboarding/walletStatus' \
--header 'walletIdentifier: CLW' \
--header 'date: Wed, 12 Jun 2024 08:53:43 GMT' \
--header 'authorization: hmac username="smsplus", algorithm="sha512", headers="date", signature="v15rnvh1InSEWRq6EW9BCfXlxO0QI/4Sxxmdxd2f4Q0="' \
--header 'Content-Type: application/json' \
--data-raw '{
  "messageCode": "3530",
  "clientTxnId": "CBL-458",
  "requestDateTime": "20161011221416",
  "accountNumber": "2000123hh",
  "statusType": "Credit"
}'
```

## Response Parameters

<HTMLBlock>{`
<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>messageCode</td>
      <td>API Unique IDentifier</td>
      <td>1073</td>
    </tr>
    <tr>
      <td>clientTxnId</td>
      <td>Value echoed from the request</td>
      <td>statementinqtes22</td>
    </tr>
    <tr>
      <td>accountNumber</td>
      <td>Value echoed from the request</td>
      <td>1234567890123456</td>
    </tr>
    <tr>
      <td>accosaTransactionId</td>
      <td>Unique ID for a particular transaction generated in Prepaid</td>
      <td>3591893</td>
    </tr>
    <tr>
      <td>description</td>
      <td>Reserved field to send information to client</td>
      <td>Statement inquiry completed</td>
    </tr>
    <tr>
      <td>accosaRefNo</td>
      <td>Auto-generated sequence number</td>
      <td>20240522001234</td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>

## Sample Response

```json
"accountNumber": "30003958135_1",
"description": "[Reserve_1]",
"responseCode": "00”,
"messageCode": “3531”,
"clientTxnId": "BLOCK_JM_aax11LrjoCV-f34",
"clientId": "2000",
"responseDateTime": "20230615234800",
"responseMessage": "SUCCESS",
"bankId": 7000,
"accosaRefNo": “52”
}

```

<br />
