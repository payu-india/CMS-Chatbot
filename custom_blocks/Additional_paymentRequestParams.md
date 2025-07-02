---
name: Additional_paymentRequestParams
---
\<Accordion title="Additional info for Request parameters" icon="fa-info-circle">

<br />

> 📘 Reference
>
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

&#x20; \<Table align=\{\["left","left"]}>
&#x20;   \<thead>
&#x20;     \<tr>
&#x20;       \<th style=\{\{ textAlign: "left" }}>
&#x20;         Parameter
&#x20;       \</th>

&#x20;       \<th style=\{\{ textAlign: "left" }}>
&#x20;         Reference
&#x20;       \</th>
&#x20;     \</tr>
&#x20;   \</thead>

&#x20;   \<tbody>
&#x20;     \<tr>
&#x20;       \<td style=\{\{ textAlign: "left" }}>
&#x20;         \<Glossary>key\</Glossary>
&#x20;       \</td>

&#x20;       \<td style=\{\{ textAlign: "left" }}>
&#x20;         For more information on how to generate the Key and Salt, refer to any of the following:

&#x20;         \* \*\*Production\*\*: \[Generate Merchant Key and Salt]\(doc:generate-merchant-key-and-salt-on-payu-dashboard)

&#x20;         \* \*\*Test\*\*: \[Generate Test Merchant Key and Salt]\(doc:generate-test-merchant-key-and-salt)
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td style=\{\{ textAlign: "left" }}>
&#x20;         \<Glossary>hash\</Glossary>
&#x20;       \</td>

&#x20;       \<td style=\{\{ textAlign: "left" }}>
&#x20;         Hash logic for \*\*\\\_payment\*\* API is:\\
&#x20;         sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
&#x20;         For more information about the hash generation process, refer to \[Generate Hash]\(doc:generate-hash-merchant-hosted).
&#x20;       \</td>
&#x20;     \</tr>

&#x20;     \<tr>
&#x20;       \<td style=\{\{ textAlign: "left" }} />

&#x20;       \<td style=\{\{ textAlign: "left" }} />
&#x20;     \</tr>
&#x20;   \</tbody>
&#x20; \</Table>
\</Accordion>