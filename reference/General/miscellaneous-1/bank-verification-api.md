---
title: Bank Verification API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Bank Verification API
  description: >-
    The Bank Verification API allows for the verification of bank accounts using
    a penny drop or penniless transaction, requiring an access token with
    specific scopes and client credentials for authentication.
  robots: index
next:
  description: ''
---
The **Bank Verification** API is used to verify bank account using penny drop/penniless transaction.

## Environment

<Table>
  <thead>
    <tr>
      <th>Environment</th>
      <th>URL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>**Production Environment**</td>
      <td>https://onepayuonboarding.payu.in/dvs/bank_accounts/acc_verification</td>
    </tr>
  </tbody>
</Table>

> 📘 **Note:**
> 
> The access token with the scope as **verify_bank_account** and grant type as **client_credentials** are required on the header. For more information on getting the access token, refer to [Get Token API - Bank Verification](ref:gettoken-bank-verification).

## Request parameters

### Header

<Table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bearer token<br/><code>mandatory</code></td>
      <td>The access token with the scope as **verify_bank_account** and grant type as **client_credentials** are required on the header. For more information on getting the access token, refer to [Get Token API - Bank Verification](ref:gettoken-bank-verification).</td>
    </tr>
  </tbody>
</Table>

### Body

<Table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>account_number<br/><code>mandatory</code></td>
      <td><code>String</code> This parameter must contain the account number to be verified.</td>
    </tr>
    <tr>
      <td>ifsc<br/><code>mandatory</code></td>
      <td><code>String</code> This parameter must contain the bank IFSC code.</td>
    </tr>
    <tr>
      <td>name<br/><code>mandatory</code></td>
      <td><code>String</code> This parameter must contain the account holder name.</td>
    </tr>
    <tr>
      <td>name_match_required<br/><code>optional</code></td>
      <td><code>Boolean</code> This parameter must be set to <code>true</code> if the name must match along with bank account verification.</td>
    </tr>
    <tr>
      <td>leniency<br/><code>optional</code></td>
      <td><code>String</code> If name_match_required is set to <code>true</code>, this parameter must contain any of the following:- Medium - High - Lo</td>
    </tr>
  </tbody>
</Table>

## Sample request

```bash
curl --location 'https://uat-onepayuonboarding.payu.in/dvs/bank_accounts/acc_verification' \
--header 'clientId: <client Id>' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--header 'Cookie: Path=/' \
--data '{
"account_number": "0514100000****",
"ifsc": "HDFC0000514",
"name" : "R******* P"
}
'
```

## Response parameters

<Table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>payuRequestId</td>
      <td>This parameter returns the PayU request ID.</td>
    </tr>
    <tr>
      <td>result</td>
      <td>This parameter returns the results of the verification in a JSON format. For more information, refer to <a href="#result-json-fields-description">result JSON fields description</a> table.</td>
    </tr>
    <tr>
      <td>requestAttributes</td>
      <td>This parameter contains the following details posted in the request in a JSON format: - name - ifsc - accountNumber</td>
    </tr>
  </tbody>
</Table>

### result JSON fields description

<Table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>accountName</td>
      <td>The masked name of the account holder for privacy.</td>
      <td>Ashish</td>
    </tr>
    <tr>
      <td>bankResponse</td>
      <td>The response message from the bank regarding the transaction status.</td>
      <td>Transaction successful</td>
    </tr>
    <tr>
      <td>bankTxnStatus</td>
      <td>A boolean value indicating if the bank transaction was successful.</td>
      <td>true</td>
    </tr>
    <tr>
      <td>accountStatus</td>
      <td>The current status of the account.</td>
      <td>ACTIVE</td>
    </tr>
  </tbody>
</Table>

## Sample response

### Success scenario

```json
{
  "payuRequestId": "ba659237-34de-4805-a5cf-ef9dd7a1cda2",
  "result": {
    "accountName": "P R*******",
    "bankResponse": "Transaction successful",
    "bankTxnStatus": "true",
    "accountStatus": "ACTIVE"
  },
  "requestAttributes": {
    "name": "R******* P",
    "ifsc": "HDFC0000514",
    "accountNumber": "0514100000****"
  }
}
```

### Failure scenario

- Missing client_id value in header

```json
{
  "error": "Missing required client_id header"
}
```

- Invalid account number

```json
{
  "payuRequestId": "0aeb7a65-cea3-4e81-9355-38548bb8f795",
  "error": {
    "reason": "Invalid account number or IFSC provided"
  },
  "requestAttributes": {
    "name": "test",
    "ifsc": "HDFC0000514",
    "accountNumber": "0514100000***",
    "verficationMode": 1
  }
}
```