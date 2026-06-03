---
title: POC
deprecated: false
hidden: true
metadata:
  robots: index
---
<SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  columnWidths={['18%', '32%', '50%']}
  rows={[
    ['`E000`', 'NO_ERROR', 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'],
    ['`AUCNEGATIVE`', 'OTP Generated Successfully', 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'],
    ['`E348`', 'ISSUER_DECLINED', 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'],
  ]}
  placeholder="Search errors..."
/>

<br />
