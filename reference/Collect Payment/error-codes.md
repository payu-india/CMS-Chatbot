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

<SearchableTableRemote
  dataUrl="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/upi-error-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

<br />
