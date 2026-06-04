---
title: POC
deprecated: false
hidden: true
metadata:
  robots: index
---
> 📘 Note
>
> testing

<SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  columnWidths={['18%', '32%', '50%']}
  codeColumns={[0]}
  rows={[
    ['E000', 'NO_ERROR', 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'],
    ['AUCNEGATIVE', 'OTP Generated Successfully', 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'],
    ['E348', 'ISSUER_DECLINED', 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'],
  ]}
  placeholder="Search errors..."
/>

<SearchableTableSimple tableKey="banksDemo" placeholder="Search" maxHeight="500px" />

<SearchableTableSmall
  headersJson='["Wallet","UPI","Status"]'
  rowsJson='[["Paytm","Yes","Active"],["PhonePe","Yes","Active"]]'
  placeholder="Search wallets"
/>

<Tooltip
  content="Merchant Key issued by PayU"
  label="Click to acess Bank Codes"
  position="right"
  delay="300"
/>

<Tooltip
  content="For setup steps, see"
  label="Click to access link page"
  linkUrl="https://docs.payu.in/docs/merchant-key"
  linkText="Merchant Key documentation"
  linkTarget="_blank"
  position="right"
  delay="300"
/>

<br />
