---
title: Net Banking Codes
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - PayU India Net Banking bankcode
    - Net Banking bankcode
    - NetBanking bankcode
  robots: index
next:
  description: ''
---
In the Seamless integration (Merchant Hosted Checkout or Server-to-Server), you must use **NB** with **pg** parameter for collecting payment using Net Banking. The following table provides the codes for the leading banks in India. This code must be used as a value with the **<Glossary>bankcode</Glossary>** parameter.

<br />

<SearchableTableRemote
  dataUrl="https://raw.githubusercontent.com/palgunams21/payu-docs-assets/refs/heads/main/data/net-banking-codes.json"
  placeholder="Search"
  maxHeight="500px"
/>

<br />
## Merged banks and supported bank codes
<Callout icon="📘" theme="info">
  **Merged banks:** After RBI-led mergers, customers may still identify with the former bank name. On the PayU platform, Net Banking continues to support the relevant **bankcode** values for both the **successor bank** and the **erstwhile (pre-merger)** bank rows in the list below—so you do not need to change a stored **bankcode** solely because the customer’s account was migrated to a successor bank, provided that code remains listed for your integration (same idea as other gateways document in their public NB bank lists).
</Callout>

Use the **bankcode** from the row that matches how you onboarded the customer or how your checkout labels the bank. The table below maps common merger cases to the corresponding entries in the searchable list.
| Erstwhile bank | Successor bank | Supported **bankcode** values (in the list below) |
| -------------- | -------------- | -------------------------------------------------- |
| Allahabad Bank | Indian Bank | `ALLB` (Indian Bank – Erstwhile Allahabad Bank), `INDB` (Indian Bank) |
| Oriental Bank of Commerce | Punjab National Bank | `OBCB` (PNB – Erstwhile Oriental Bank of Commerce), `PNBB` (Punjab National Bank) |
| United Bank of India | Punjab National Bank | `UNIB` (PNB – Erstwhile United Bank of India), `PNBB` (Punjab National Bank) |
| Syndicate Bank | Canara Bank | `SYNDB` (Canara Bank – Erstwhile Syndicate Bank), `CABB` (Canara Bank) |
