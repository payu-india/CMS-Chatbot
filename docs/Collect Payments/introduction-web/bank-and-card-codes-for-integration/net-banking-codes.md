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

> 📘 **Note on merged bank codes:**&#x20;
>
> After RBI-led mergers, customers may still identify with the former bank name. On the PayU platform, Net Banking continues to support the relevant **bankcode** values for both the **successor bank** and the **erstwhile (pre-merger)** bank rows in the listed below so you need to change a stored **bankcode** solely because the customer’s account was migrated to a successor bank.&#x20;

Use the **bankcode** from the row that matches how you onboarded the customer or how your checkout labels the bank. The table below maps common merger cases to the corresponding entries in the searchable list.

| Erstwhile bank            | Successor bank       | Supported **bankcode** values |
| ------------------------- | -------------------- | ----------------------------- |
| Allahabad Bank            | Indian Bank          | `INDB` (Indian Bank)          |
| Oriental Bank of Commerce | Punjab National Bank | `PNBB` (Punjab National Bank) |
| United Bank of India      | Punjab National Bank | `PNBB` (Punjab National Bank) |
| Syndicate Bank            | Canara Bank          | `CABB` (Canara Bank)          |

<br />
