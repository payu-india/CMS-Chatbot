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

<SearchableTableSimple
  headers={['Bank', 'Type', 'Status']}
  rowsJson='[["HDFC Bank","Netbanking / Cards","Active"],["ICICI Bank","Netbanking / Cards","Active"],["State Bank of India","Netbanking","Active"],["Axis Bank","Cards","Active"]]'
  placeholder="Search"
  maxHeight="500px"
/>

<br />
