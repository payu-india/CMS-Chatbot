---
title: Decoupled Flow Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The S2S decoupled flow for cards involves the following steps for the **redirect** experience.

<Cards_PayU_Labs />

**Steps to integrate**

<Cards columns={2}>
  <Card title="1. Initiate payment request with PayU" href="#step-1-Initiate-payment-request-with-payU">
    Create and send a payment request to PayU with all required parameters and merchant configuration
  </Card>

  <Card title="2. Card Authentication" href="#step-2-card-authenication">
    Redirect the customer to PayU's secure payment gateway to complete the transaction
  </Card>

  <Card title="3. Authorize (charge) the Payment" href="#step-3-authorize-charge-the-payment">
    Process the payment authorization and charge the customer's selected payment method
  </Card>

  <Card title="4. Check the response from PayU" href="#step-4-check-the-response-from-payu">
    Handle and process the response received from PayU after payment completion
  </Card>

  <Card title="5. Verify payment" href="#step-5-verify-the-payment">
    Verify the payment status using PayU's verification API and implement proper validation

    <br />
  </Card>
</Cards>

<RegisterMerchantPrerequiste />

> 📘
>
> **Notes**:
>
> - This API is backward compatible and you can continue to the existing integration parameters to process the 3DS 1.0.2 transactions.
> - If you are using legacy integration of decoupled flow for S2S, refer to [Legacy Flow for Server-to-Server](legacy-flow-for-server-to-server).

## Step 1: Initiate payment request with PayU

The merchant initiates PayU with the required transaction mandatory or optional parameters. This needs to be a server-to-server curl call request. URL, parameters, and their descriptions. For more information, refer to [Cards Decoupled Flow](ref:_payment_s2s_decoupled_flow).

<PaymentAPIEnvironment />

<Accordion title="Request parameters" icon="fa-code">
<HTMLBlock>{/*RDMX_HTMLBLOCK:CiA8dGFibGUgc3R5bGU9IndpZHRoOiAxMDAlOyBib3JkZXItY29sbGFwc2U6IGNvbGxhcHNlOyI+Cjx0aGVhZD4KPHRyPgogIDx0aCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHN0cm9uZz5QYXJhbWV0ZXI8L3N0cm9uZz48L3RoPgogIDx0aCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHN0cm9uZz5EZXNjcmlwdGlvbjwvc3Ryb25nPjwvdGg+CiAgPHRoIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48c3Ryb25nPkV4YW1wbGU8L3N0cm9uZz48L3RoPgo8L3RyPgo8L3RoZWFkPgo8dGJvZHk+Cjx0cj4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPmtleTxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5TdHJpbmc8L2NvZGU+IE1lcmNoYW50IGtleSBwcm92aWRlZCBieSBQYXlVIGR1cmluZyBvbmJvYXJkaW5nLjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PC9wPjwvdGQ+CjwvdHI+Cjx0cj4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPnR4bmlkPGJyPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVGhlIHRyYW5zYWN0aW9uIElEIGlzIGEgcmVmZXJlbmNlIG51bWJlciBmb3IgYSBzcGVjaWZpYyBvcmRlciB0aGF0IGlzIGdlbmVyYXRlZCBieSB0aGUgbWVyY2hhbnQuPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+YW1vdW50PGJyPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVGhlIHBheW1lbnQgYW1vdW50IGZvciB0aGUgdHJhbnNhY3Rpb24uPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+cHJvZHVjdGluZm88YnI+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PGNvZGU+U3RyaW5nPC9jb2RlPiBBIGJyaWVmIGRlc2NyaXB0aW9uIG9mIHRoZSBwcm9kdWN0LjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PC9wPjwvdGQ+CjwvdHI+Cjx0cj4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPmZpcnN0bmFtZTxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5TdHJpbmc8L2NvZGU+IFRoZSBmaXJzdCBuYW1lIG9mIHRoZSBjdXN0b21lci48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPkFzaGlzaDwvcD48L3RkPgo8L3RyPgo8dHI+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5lbWFpbDxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5TdHJpbmc8L2NvZGU+IFRoZSBlbWFpbCBhZGRyZXNzIG9mIHRoZSBjdXN0b21lci48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjwvcD48L3RkPgo8L3RyPgo8dHI+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5waG9uZTxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5TdHJpbmc8L2NvZGU+IFRoZSBwaG9uZSBudW1iZXIgb2YgdGhlIGN1c3RvbWVyLjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PC9wPjwvdGQ+CjwvdHI+Cjx0cj4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPnBnPGJyPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVGhlIHBnIHBhcmFtZXRlciBkZXRlcm1pbmVzIHdoaWNoIHBheW1lbnQgdGFicyB3aWxsIGJlIGRpc3BsYXllZCBvbiB0aGUgUGF5VSBwYWdlLiBGb3IgY2FyZHMsICdDQycgd2lsbCBiZSB0aGUgdmFsdWUuPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5DQzwvcD48L3RkPgo8L3RyPgo8dHI+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5iYW5rY29kZTxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5TdHJpbmc8L2NvZGU+IEVhY2ggcGF5bWVudCBvcHRpb24gaXMgaWRlbnRpZmllZCB3aXRoIGEgdW5pcXVlIGJhbmsgY29kZSBhdCBQYXlVLiBUaGUgbWVyY2hhbnQgbXVzdCBwb3N0IHRoaXMgcGFyYW1ldGVyIHdpdGggdGhlIGNvcnJlc3BvbmRpbmcgcGF5bWVudCBvcHRpb24ncyBiYW5rIGNvZGUgdmFsdWUgaW4gaXQuIEZvciBtb3JlIGluZm9ybWF0aW9uLCByZWZlciB0byBDYXJkIFR5cGUgQ29kZXMgYW5kIFN1cHBvcnRlZCBCYW5rcyBmb3IgQ2FyZHMuPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5BTUVYPC9wPjwvdGQ+CjwvdHI+Cjx0cj4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPmNjbnVtPGJyPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVXNlIDEzLTE5IGRpZ2l0IGNhcmQgbnVtYmVyIGZvciBjcmVkaXQvZGViaXQgY2FyZHMgKDE1IGRpZ2l0cyBmb3IgQU1FWCwgMTMtMTkgZm9yIE1hZXN0cm8pIGFuZCB2YWxpZGF0ZSB3aXRoIExVSE4gYWxnb3JpdGhtLiBSZWZlciB0byBDYXJkIE51bWJlciBGb3JtYXRzIGFuZCBkaXNwbGF5IGVycm9yIG1lc3NhZ2Ugb24gaW52YWxpZCBpbnB1dC48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjUxMjM0NTY3ODkwMTIzNDY8L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+Y2NuYW1lPGJyPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVGhpcyBwYXJhbWV0ZXIgbXVzdCBjb250YWluIHRoZSBuYW1lIG9uIGNhcmQg4oCTIGFzIGVudGVyZWQgYnkgdGhlIGN1c3RvbWVyIGZvciB0aGUgdHJhbnNhY3Rpb24uPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5Bc2hpc2ggS3VtYXI8L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+Y2N2djxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5TdHJpbmc8L2NvZGU+IFVzZSAzLWRpZ2l0IENWViBudW1iZXIgZm9yIGNyZWRpdC9kZWJpdCBjYXJkcyBhbmQgNC1kaWdpdCBzZWN1cml0eSBjb2RlICg0REJDL0NJRCkgZm9yIEFNRVggY2FyZHMuIFZhbGlkYXRlIHdpdGggQklOIEFQSS48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjEyMzwvcD48L3RkPgo8L3RyPgo8dHI+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5jY2V4cG1vbjxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5TdHJpbmc8L2NvZGU+IFRoaXMgcGFyYW1ldGVyIG11c3QgY29udGFpbiB0aGUgY2FyZCdzIGV4cGlyeSBtb250aCDigJMgYXMgZW50ZXJlZCBieSB0aGUgdXNlciBmb3IgdGhlIHRyYW5zYWN0aW9uLiBJdCBtdXN0IGFsd2F5cyBiZSBpbiAyIGRpZ2l0cyBvciBpbiBNTSBmb3JtYXQuIEZvciBtb250aHMgMS05LCB0aGlzIHBhcmFtZXRlciBtdXN0IGJlIGFwcGVuZGVkIHdpdGggMCDigJMgbGlrZSAwMSwgMDLigKYwOS4gRm9yIG1vbnRocyAxMC0xMiwgdGhpcyBwYXJhbWV0ZXIgbXVzdCBub3QgYmUgYXBwZW5kZWQg4oCTIEl0IHNob3VsZCBiZSAxMCwgMTEgYW5kIDEyIHJlc3BlY3RpdmVseS48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjEwPC9wPjwvdGQ+CjwvdHI+Cjx0cj4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPmNjZXhweXI8YnI+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PGNvZGU+U3RyaW5nPC9jb2RlPiBUaGlzIHBhcmFtZXRlciBtdXN0IGNvbnRhaW4gdGhlIGNhcmQncyBleHBpcnkgeWVhciDigJMgYXMgZW50ZXJlZCBieSB0aGUgY3VzdG9tZXIgZm9yIHRoZSB0cmFuc2FjdGlvbi4gSXQgbXVzdCBiZSBvZiBmb3VyIGRpZ2l0cy48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjIwMjU8L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+ZnVybDxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5TdHJpbmc8L2NvZGU+IFRoZSBzdWNjZXNzIFVSTCwgd2hpY2ggaXMgdGhlIHBhZ2UgUGF5VSB3aWxsIHJlZGlyZWN0IHRvIGlmIHRoZSB0cmFuc2FjdGlvbiBpcyBzdWNjZXNzZnVsLjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PC9wPjwvdGQ+CjwvdHI+Cjx0cj4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPnN1cmw8YnI+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PGNvZGU+U3RyaW5nPC9jb2RlPiBUaGUgRmFpbHVyZSBVUkwsIHdoaWNoIGlzIHRoZSBwYWdlIFBheVUgd2lsbCByZWRpcmVjdCB0byBpZiB0aGUgdHJhbnNhY3Rpb24gaXMgZmFpbGVkLjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PC9wPjwvdGQ+CjwvdHI+Cjx0cj4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPmhhc2g8YnI+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PGNvZGU+U3RyaW5nPC9jb2RlPiBJdCBpcyB0aGUgaGFzaCBjYWxjdWxhdGVkIGJ5IHRoZSBtZXJjaGFudC4gVGhlIGhhc2ggY2FsY3VsYXRpb24gbG9naWMgaXM6IDxjb2RlPnNoYTUxMihrZXl8dHhuaWR8YW1vdW50fHByb2R1Y3RpbmZvfGZpcnN0bmFtZXxlbWFpbHx1ZGYxfHVkZjJ8dWRmM3x1ZGY0fHVkZjV8fHxTQUxUKTwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjwvcD48L3RkPgo8L3RyPgo8dHI+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD50eG5fczJzX2Zsb3c8YnI+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PGNvZGU+U3RyaW5nPC9jb2RlPiBUaGlzIHBhcmFtZXRlciBtdXN0IGJlIHBhc3NlZCB3aXRoIHRoZSB2YWx1ZSBhcyA8c3Ryb25nPjQ8L3N0cm9uZz4gZm9yIExlZ2FjeSBEZWNvdXBsZWQgZmxvdy48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjQ8L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+YXV0aF9vbmx5PGJyPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVGhpcyBwYXJhbWV0ZXIgbXVzdCBiZSBwYXNzZWQgd2l0aCB0aGUgdmFsdWUgYXMgPHN0cm9uZz4yPC9zdHJvbmc+IGZvciBhdXRoZW50aWNhdGlvbi1vbmx5IGZsb3cuIFdoZW4gc2V0IHRvIDIsIHlvdSBtdXN0IGNhbGwgdGhlIEF1dGhEYXRhIEFQSSB0byByZXRyaWV2ZSBhdXRoZW50aWNhdGlvbiByZXN1bHRzLjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+MjwvcD48L3RkPgo8L3RyPgo8dHI+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5hdXRoZW50aWNhdGlvbl9mbG93PGJyPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVGhpcyBwYXJhbWV0ZXIgY29udGFpbnMgdGhlIGF1dGhlbnRpY2F0aW9uIGZsb3cgb2YgdGhlIHRyYW5zYWN0aW9uIGFzIFJFRElSRUNULiA8c3Ryb25nPk5vdGVzPC9zdHJvbmc+OjxiciAvPi0gSWYgYmVpbmcgcGFzc2VkIGFzIFJFRElSRUNULCBQYXlVIHdpbGwgbm90IGJlIHByb3ZpZGluZyB0aGUgTmF0aXZlIE9UUCBzdWJtaXNzaW9uIGZsb3cgaW4gSW5pdGlhdGUgcmVzcG9uc2UuPGJyIC8+LSBJZiBub3QgcGFzc2VkIHdpdGggdmFsdWUgYXMgUkVESVJFQ1QsIFBheVUgd2lsbCByZXR1cm4gYmFzaXMgb24gdGhlIEJpbiBzdXBwb3J0ZWQgZm9yIE5hdGl2ZSBPVFAgb3Igbm90LjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+UkVESVJFQ1Q8L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+dGVybVVybDxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5TdHJpbmc8L2NvZGU+IFRoaXMgcGFyYW1ldGVyIG11c3QgY29udGFpbiB0aGUgVVJMIHdoaWNoIHdpbGwgcmVjZWl2ZSB0aGUgYXV0aGVudGljYXRpb24gcmVzcG9uc2UgZnJvbSBBQ1MuPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+czJzX2NsaWVudF9pcDxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5TdHJpbmc8L2NvZGU+IFRoaXMgcGFyYW1ldGVyIG11c3QgaGF2ZSB0aGUgc291cmNlIElQIG9mIHRoZSBjdXN0b21lci48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjwvcD48L3RkPgo8L3RyPgo8dHI+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5zMnNfZGV2aWNlX2luZm88YnI+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PGNvZGU+U3RyaW5nPC9jb2RlPiBUaGlzIHBhcmFtZXRlciBtdXN0IGhhdmUgdGhlIGN1c3RvbWVyIGFnZW50J3MgZGV2aWNlLjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PC9wPjwvdGQ+CjwvdHI+Cjx0cj4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPm5vdGlmeXVybDxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gSXQgaXMgdXNlZCB0byBzZW5kIHJlc3BvbnNlIHJlZ2FyZGluZyBjdXJyZW50IHRyYW5zYWN0aW9uIHRvIG5vdGlmeSBhYm91dCB0aGUgY3VycmVudCB0cmFuc2FjdGlvbiBkb25lIGluIG1lcmNoYW50IHNpdGUuPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+YWRkcmVzczE8YnI+PGNvZGU+b3B0aW9uYWw8L2NvZGU+PC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5TdHJpbmc8L2NvZGU+IFRoZSBmaXJzdCBsaW5lIG9mIHRoZSBiaWxsaW5nIGFkZHJlc3MuIDxzdHJvbmc+Rm9yIEZyYXVkIERldGVjdGlvbjwvc3Ryb25nPjogVGhpcyBpbmZvcm1hdGlvbiBpcyBoZWxwZnVsIHdoZW4gaXQgY29tZXMgdG8gaXNzdWVzIHJlbGF0ZWQgdG8gZnJhdWQgZGV0ZWN0aW9uIGFuZCBjaGFyZ2ViYWNrcy4gSGVuY2UsIGl0IGlzIG11c3QgdG8gcHJvdmlkZSB0aGUgY29ycmVjdCBpbmZvcm1hdGlvbi48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjwvcD48L3RkPgo8L3RyPgo8dHI+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5hZGRyZXNzMjxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVGhlIHNlY29uZCBsaW5lIG9mIHRoZSBiaWxsaW5nIGFkZHJlc3MuPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+Y2l0eTxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVGhlIGNpdHkgd2hlcmUgeW91ciBjdXN0b21lciByZXNpZGVzIGFzIHBhcnQgb2YgdGhlIGJpbGxpbmcgYWRkcmVzcy48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjwvcD48L3RkPgo8L3RyPgo8dHI+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5zdGF0ZTxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVGhlIHN0YXRlIHdoZXJlIHlvdXIgY3VzdG9tZXIgcmVzaWRlcyBhcyBwYXJ0IG9mIHRoZSBiaWxsaW5nIGFkZHJlc3MuPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+Y291bnRyeTxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVGhlIGNvdW50cnkgd2hlcmUgeW91ciBjdXN0b21lciByZXNpZGVzLjwvcD48L3RkPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PC9wPjwvdGQ+CjwvdHI+Cjx0cj4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPnppcGNvZGU8YnI+PGNvZGU+b3B0aW9uYWw8L2NvZGU+PC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5TdHJpbmc8L2NvZGU+IEJpbGxpbmcgYWRkcmVzcyB6aXAgY29kZSBpcyBtYW5kYXRvcnkgZm9yIHRoZSBjYXJkbGVzcyBFTUkgb3B0aW9uLiA8Y29kZT5DaGFyYWN0ZXIgTGltaXQ8L2NvZGU+LTIwPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+dWRmMTxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVXNlci1kZWZpbmVkIGZpZWxkcyAodWRmKSBhcmUgdXNlZCB0byBzdG9yZSBhbnkgaW5mb3JtYXRpb24gY29ycmVzcG9uZGluZyB0byBhIHBhcnRpY3VsYXIgdHJhbnNhY3Rpb24uIFlvdSBjYW4gdXNlIHVwIHRvIGZpdmUgdWRmcyBpbiB0aGUgcG9zdCBkZXNpZ25hdGVkIGFzIHVkZjEsIHVkZjIsIHVkZjMsIHVkZjQsIHVkZjUuPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+dWRmMjxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVXNlci1kZWZpbmVkIGZpZWxkcyAodWRmKSBhcmUgdXNlZCB0byBzdG9yZSBhbnkgaW5mb3JtYXRpb24gY29ycmVzcG9uZGluZyB0byBhIHBhcnRpY3VsYXIgdHJhbnNhY3Rpb24uIFlvdSBjYW4gdXNlIHVwIHRvIGZpdmUgdWRmcyBpbiB0aGUgcG9zdCBkZXNpZ25hdGVkIGFzIHVkZjEsIHVkZjIsIHVkZjMsIHVkZjQsIHVkZjUuPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+dWRmMzxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVXNlci1kZWZpbmVkIGZpZWxkcyAodWRmKSBhcmUgdXNlZCB0byBzdG9yZSBhbnkgaW5mb3JtYXRpb24gY29ycmVzcG9uZGluZyB0byBhIHBhcnRpY3VsYXIgdHJhbnNhY3Rpb24uPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+dWRmNDxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVXNlci1kZWZpbmVkIGZpZWxkcyAodWRmKSBhcmUgdXNlZCB0byBzdG9yZSBhbnkgaW5mb3JtYXRpb24gY29ycmVzcG9uZGluZyB0byBhIHBhcnRpY3VsYXIgdHJhbnNhY3Rpb24uPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48L3A+PC90ZD4KPC90cj4KPHRyPgogIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+dWRmNTxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPlN0cmluZzwvY29kZT4gVXNlci1kZWZpbmVkIGZpZWxkcyAodWRmKSBhcmUgdXNlZCB0byBzdG9yZSBhbnkgaW5mb3JtYXRpb24gY29ycmVzcG9uZGluZyB0byBhIHBhcnRpY3VsYXIgdHJhbnNhY3Rpb24uPC9wPjwvdGQ+CiAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48L3A+PC90ZD4KPC90cj4KPC90Ym9keT4KPC90YWJsZT4KCg==:RDMX_HTMLBLOCK*/}</HTMLBlock>

</Accordion>

<Accordion title="Understanding Hashing and sample code" icon="fa-code">
  <HashingRequestParameters />

  #### Hashing Sample Code

  <HashingSample />
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl --location \
   --request \
   POST 'https://secure.payu.in/_payment' --header 'Content-Type: application/x-www-form-urlencoded' \
   --header 'Cookie: PHPSESSID=mj185cifujktpv1igu9tmuoaal; PAYUID=6b0d4cbbe43702a8a938a4d4c546ae01; PHPSESSID=6388ab6306272' \
   --data \
  -urlencode 'hash=5e0f040fb08759d621caf04baab4bd893e1d9f5d3edfc2aa42bea00c2ac7140b14b7883028a3b7fc5df6fb728f7542d85c2930c3f3dc4bab6a8b3da1ff33d9fe' --data \
  -urlencode 'key=smsplus' --data \
  -urlencode 'txnid=payuTestTransaction8169502' --data \
  -urlencode 'amount=1.1' --data \
  -urlencode 'firstname=Postman' --data \
  -urlencode 'email=test@payu.in' --data \
  -urlencode 'phone=9988776655' --data \
  -urlencode 'productinfo=Product Info' --data \
  -urlencode 'surl=https://admin.payu.in/test_response' --data \
  -urlencode 'furl=https://admin.payu.in/test_response' --data \
  -urlencode 'notifyurl=https://admin.payu.in/test_response' --data \
  -urlencode 'codurl=https://admin.payu.in/test_response' --data \
  -urlencode 'ipurl=https://admin.payu.in/test_response' --data \
  -urlencode 'lastname=' --data \
  -urlencode 'udf1=' --data \
  -urlencode 'udf2=' --data \
  -urlencode 'udf3=' --data \
  -urlencode 'udf4=' --data \
  -urlencode 'udf5=' --data \
  -urlencode 'pg=CC' --data \
  -urlencode 'bankcode=CC' --data \
  -urlencode 'ccnum=XXXXXXXXXXX8006' --data \
  -urlencode 'ccname=ASHISH' --data \
  -urlencode 'ccvv=XXX' --data \
  -urlencode 'ccexpmon=05' --data \
  -urlencode 'ccexpyr=2023' --data \
  -urlencode 'txn_s2s_flow=4' --data \
  -urlencode 'auth_only=1' --data \
  -urlencode 'termUrl=https://admin.payu.in/test_response' --data \
  -urlencode 'authentication_flow=REDIRECT' 
  ```
  ```python
  import requests

  url = "https://secure.payu.in/_payment"

  headers = {
      "Content-Type": "application/x-www-form-urlencoded"
  }

  data = {
      "hash": "5e0f040fb08759d621caf04baab4bd893e1d9f5d3edfc2aa42bea00c2ac7140b14b7883028a3b7fc5df6fb728f7542d85c2930c3f3dc4bab6a8b3da1ff33d9fe",
      "key": "smsplus",
      "txnid": "payuTestTransaction8169502",
      "amount": "1.1",
      "firstname": "Postman",
      "email": "test@payu.in",
      "phone": "9988776655",
      "productinfo": "Product Info",
      "surl": "https://admin.payu.in/test_response",
      "furl": "https://admin.payu.in/test_response",
      "notifyurl": "https://admin.payu.in/test_response",
      "codurl": "https://admin.payu.in/test_response",
      "ipurl": "https://admin.payu.in/test_response",
      "lastname": "",
      "udf1": "",
      "udf2": "",
      "udf3": "",
      "udf4": "",
      "udf5": "",
      "pg": "CC",
      "bankcode": "CC",
      "ccnum": "XXXXXXXXXXX8006",
      "ccname": "ASHISH",
      "ccvv": "XXX",
      "ccexpmon": "05",
      "ccexpyr": "2023",
      "txn_s2s_flow": "4",
      "auth_only": "1",
      "termUrl": "https://admin.payu.in/test_response",
      "authentication_flow": "REDIRECT"
  }

  response = requests.post(url, headers=headers, data=data)

  print("Status Code:", response.status_code)
  print("Response:", response.text)
  ```
  ```java
  import java.io.IOException;
  import java.net.URI;
  import java.net.URLEncoder;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import java.nio.charset.StandardCharsets;
  import java.util.LinkedHashMap;
  import java.util.Map;
  import java.util.stream.Collectors;

  public class PayUPayment {
      public static void main(String[] args) throws IOException, InterruptedException {
          String url = "https://secure.payu.in/_payment";
          
          Map<String, String> formData = new LinkedHashMap<>();
          formData.put("hash", "5e0f040fb08759d621caf04baab4bd893e1d9f5d3edfc2aa42bea00c2ac7140b14b7883028a3b7fc5df6fb728f7542d85c2930c3f3dc4bab6a8b3da1ff33d9fe");
          formData.put("key", "smsplus");
          formData.put("txnid", "payuTestTransaction8169502");
          formData.put("amount", "1.1");
          formData.put("firstname", "Postman");
          formData.put("email", "test@payu.in");
          formData.put("phone", "9988776655");
          formData.put("productinfo", "Product Info");
          formData.put("surl", "https://admin.payu.in/test_response");
          formData.put("furl", "https://admin.payu.in/test_response");
          formData.put("notifyurl", "https://admin.payu.in/test_response");
          formData.put("codurl", "https://admin.payu.in/test_response");
          formData.put("ipurl", "https://admin.payu.in/test_response");
          formData.put("lastname", "");
          formData.put("udf1", "");
          formData.put("udf2", "");
          formData.put("udf3", "");
          formData.put("udf4", "");
          formData.put("udf5", "");
          formData.put("pg", "CC");
          formData.put("bankcode", "CC");
          formData.put("ccnum", "XXXXXXXXXXX8006");
          formData.put("ccname", "ASHISH");
          formData.put("ccvv", "XXX");
          formData.put("ccexpmon", "05");
          formData.put("ccexpyr", "2023");
          formData.put("txn_s2s_flow", "4");
          formData.put("auth_only", "1");
          formData.put("termUrl", "https://admin.payu.in/test_response");
          formData.put("authentication_flow", "REDIRECT");
          
          String formBody = formData.entrySet()
              .stream()
              .map(entry -> URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8) + "=" + 
                            URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8))
              .collect(Collectors.joining("&"));
          
          HttpClient client = HttpClient.newHttpClient();
          
          HttpRequest request = HttpRequest.newBuilder()
              .uri(URI.create(url))
              .header("Content-Type", "application/x-www-form-urlencoded")
              .POST(HttpRequest.BodyPublishers.ofString(formBody))
              .build();
          
          HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
          
          System.out.println("Status Code: " + response.statusCode());
          System.out.println("Response: " + response.body());
      }
  }
  ```
  ```php
  <?php

  $url = "https://secure.payu.in/_payment";

  $data = array(
      'hash' => '5e0f040fb08759d621caf04baab4bd893e1d9f5d3edfc2aa42bea00c2ac7140b14b7883028a3b7fc5df6fb728f7542d85c2930c3f3dc4bab6a8b3da1ff33d9fe',
      'key' => 'smsplus',
      'txnid' => 'payuTestTransaction8169502',
      'amount' => '1.1',
      'firstname' => 'Postman',
      'email' => 'test@payu.in',
      'phone' => '9988776655',
      'productinfo' => 'Product Info',
      'surl' => 'https://admin.payu.in/test_response',
      'furl' => 'https://admin.payu.in/test_response',
      'notifyurl' => 'https://admin.payu.in/test_response',
      'codurl' => 'https://admin.payu.in/test_response',
      'ipurl' => 'https://admin.payu.in/test_response',
      'lastname' => '',
      'udf1' => '',
      'udf2' => '',
      'udf3' => '',
      'udf4' => '',
      'udf5' => '',
      'pg' => 'CC',
      'bankcode' => 'CC',
      'ccnum' => 'XXXXXXXXXXX8006',
      'ccname' => 'ASHISH',
      'ccvv' => 'XXX',
      'ccexpmon' => '05',
      'ccexpyr' => '2023',
      'txn_s2s_flow' => '4',
      'auth_only' => '1',
      'termUrl' => 'https://admin.payu.in/test_response',
      'authentication_flow' => 'REDIRECT'
  );

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, $url);
  curl_setopt($ch, CURLOPT_POST, true);
  curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
  curl_setopt($ch, CURLOPT_HTTPHEADER, array(
      'Content-Type: application/x-www-form-urlencoded'
  ));
  curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);

  $response = curl_exec($ch);
  $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
  $error = curl_error($ch);
  curl_close($ch);

  if ($error) {
      echo "cURL Error: " . $error . "\n";
  } else {
      echo "Status Code: " . $httpCode . "\n";
      echo "Response: " . $response . "\n";
  }
  ?>
  ```
  ```perl
  #!/usr/bin/perl
  use strict;
  use warnings;
  use LWP::UserAgent;
  use HTTP::Request::Common qw(POST);
  use URI::Escape;

  my $url = "https://secure.payu.in/_payment";

  my $ua = LWP::UserAgent->new;
  $ua->timeout(30);

  my %data = (
      'hash'                => '5e0f040fb08759d621caf04baab4bd893e1d9f5d3edfc2aa42bea00c2ac7140b14b7883028a3b7fc5df6fb728f7542d85c2930c3f3dc4bab6a8b3da1ff33d9fe',
      'key'                 => 'smsplus',
      'txnid'               => 'payuTestTransaction8169502',
      'amount'              => '1.1',
      'firstname'           => 'Postman',
      'email'               => 'test@payu.in',
      'phone'               => '9988776655',
      'productinfo'         => 'Product Info',
      'surl'                => 'https://admin.payu.in/test_response',
      'furl'                => 'https://admin.payu.in/test_response',
      'notifyurl'           => 'https://admin.payu.in/test_response',
      'codurl'              => 'https://admin.payu.in/test_response',
      'ipurl'               => 'https://admin.payu.in/test_response',
      'lastname'            => '',
      'udf1'                => '',
      'udf2'                => '',
      'udf3'                => '',
      'udf4'                => '',
      'udf5'                => '',
      'pg'                  => 'CC',
      'bankcode'            => 'CC',
      'ccnum'               => 'XXXXXXXXXXX8006',
      'ccname'              => 'ASHISH',
      'ccvv'                => 'XXX',
      'ccexpmon'            => '05',
      'ccexpyr'             => '2023',
      'txn_s2s_flow'        => '4',
      'auth_only'           => '1',
      'termUrl'             => 'https://admin.payu.in/test_response',
      'authentication_flow' => 'REDIRECT'
  );

  my $response = $ua->request(POST $url,
      Content_Type => 'application/x-www-form-urlencoded',
      Content => [%data]
  );

  if ($response->is_success) {
      print "Status Code: " . $response->code . "\n";
      print "Response: " . $response->decoded_content . "\n";
  } else {
      print "Error: " . $response->status_line . "\n";
      print "Response: " . $response->decoded_content . "\n";
  }
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-code">
  > 📘 Understanding response parameters:
  >
  > The response for the S2S payment request is not similar to Merchant Hosted or PayU Hosted Checkout. For description of response parameters, refer to  [Additional Info for Payment APIs](ref:addl_info-payment-apis#response-for-initial-server-to-server-request").

  ```json
  {
     "metaData": {
        "message": null,
        "referenceId": "00c44a4c8306f9cbe5ecf6133afe08a7",
        "statusCode": null,
        "txnId": "payuTestTransaction447674",
        "txnStatus": "Enrolled",
        "unmappedStatus": "pending"
     },
     "result": {
        "otpPostUrl": "",
        "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vd3d3LjNkc2VjdXJlMS5pY2ljaWJhbmsuY29tL0FDU1dlYi9FbnJvbGxXZWIvSUNJQ0lCYW5rL3NlcnZlci9BY2Nlc3NDb250cm9sU2VydmVyP2lkY3Q9ODExMi5WIiBtZXRob2Q9InBvc3QiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9Ik1EIiB2YWx1ZT0iYzJlOWU0NTYwMzdmMDMzZTVjYzNkN2I2ZTU1NjE4OWFkZjQxZWVhYmY3MDY4NDRkZmY3MGFhYzkxZjZiOGU3M2JiMTg0NjI4NmM4Zjk5ZWE3NjhjZjM4ZjdjMTIzNjljfDUyMzcyNzQ5MzY0Nzk1MGYzMjY4NGJkNmYxYWIwN2FhNjQ3NDAxNmYiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9IlBhUmVxIiB2YWx1ZT0iZU5wVlVrMXYyekFNL1N0Qjc3RytyTW9PV0FGTkRhdzVKTTNTN3RLYmJER3hoL2lqbGowMCsvV1RIR2ZkVHVLamlFZStSOEpiMlNObXIxaU1QV3JZb25QbWhJdktQdHpsOFQzbE9lVkxMbzkyR1Z0TWxvbFE2VkpZeFRrMVZDcGw3elRzSHcvNG9lRVg5cTVxRzgwaUduRWdOK2daKzZJMHphREJGQi9yelU3SGlVaVZCREpEcUxIZlpKb3puc1lKbFFrVmd0SjdJTmMwTktaRzdXclhuVWNIWkVKUXRHTXo5QmN0cEsrN0FSajdzeTZIb1hNclF0d2tKK3JNWll5cWh1UW1UMWw4dElVNVdta1pUeFJGcTR4TUZVdXBORGw1YXV1NmJmYW5BN3F1YlJ3K204YWVzUWNTU0lGOGFkaVBJWEoraU0vSzZ2ZTMwL0NTYmNYTEsvMzluaFdYN2M5MXVjMStpQjMvL2dBa1ZJQTFBMnBPdWRkSDJZS0psVkFyNGYyWjhtRHFNTDNlN0E0TEZqSHFUYmttb0F0OUhxK0FoWTkvRStERjlkZ1VOd2R1Q1FEVFQ0Kyt3amY0RzRORlYzZ1I4L09sNE9rNTdLUVlndnZ6Z040T0pTU1RLc2wzL0xSVzViZXdwNmtra0ZmZVp5Nm9uTmdEQUJKSXlId0NaTDRlSC8xM1ZYOEFEOUxGSGc9PSI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iVGVybVVybCIgdmFsdWU9Imh0dHBzOi8vc2VjdXJlLnBheXUuaW4vYmFiOTE0ZmRjYWZkNWQxMjg3MGVkN2E1OTcxOTA1YWIvQ29tbW9uUGdSZXNwb25zZUhhbmRsZXIiPjwvZm9ybT48c2NyaXB0IHR5cGU9J3RleHQvamF2YXNjcmlwdCc+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB3aW5kb3cub25sb2FkPWZ1bmN0aW9uKCl7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZG9jdW1lbnQuZm9ybXNbJ3BheW1lbnRfcG9zdCddLnN1Ym1pdCgpOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgICAgICAgICA8L3NjcmlwdD48L2JvZHk+PC9odG1sPg=="
     },
     "binData": {
        "pureS2SSupported": false,
        "issuingBank": "ICICI",
        "category": "creditcard",
        "cardType": "VISA",
        "isDomestic": true
     }
  }
  ```
</Accordion>

## Step 2: Card Authentication Flow

This step can be either any of the following:

- [Step 2a: Native OTP Flow](#step-2a-native-otp-flow)
- [Step 2b: Non-Native OTP Flow](#step-2b-non-native-otp-flow)

### Step 2a: Native OTP Flow

The **\_payment** API response is similar to the following:

> 👍
>
> Experience the end-to-end **Merchant Hosted Checkout** flow and instantly generate the complete code for seamless, zero-coding integration into your website. Navigate to **ACS Template Decoder** under **Tools & Utilities** to generate code for decoding the ACS template in the response:
>
> <HTMLBlock>{`
>                       <style>
>                       .tooltip-btn {
>                           position: relative;
>                           background-color: #4CAF50;
>                           color: white;
>                           padding: 10px 20px;
>                           border: none;
>                           border-radius: 5px;
>                           cursor: pointer;
>                           font-weight: bold; /* Added this line */
>                       }
>                       .tooltip-btn:hover::after {
>                           content: attr(data-tooltip);
>                           position: absolute;
>                           bottom: 125%;
>                           left: 50%;
>                           transform: translateX(-50%);
>                           background-color: #333;
>                           color: white;
>                           padding: 5px 10px;
>                           border-radius: 4px;
>                           white-space: nowrap;
>                           font-size: 12px;
>                           z-index: 1;
>                       }
>                       </style>
>
>                       <button onclick="window.open('https://payu.in/integrationlab/seamless/cards', '_blank')" 
>                               class="tooltip-btn" 
>                               data-tooltip="Click here to see the Merchant Hosted Checkout end-to-end integration and instantly generate the complete code needed for a zero-coding setup on your website.">
>                           Experience the flow and get the code
>                       </button>
> `}</HTMLBlock>

<br />

<Accordion title="Sample response" icon="fa-code">
  The response from \_payment API is similar to the following:

  ```json
  {
      "metaData": {
          "message": null,
          "referenceId": "8f856a1e76ba1cb93ebc27cc82f4186d3fda065c359f528c3ebcb47fba71096d",
          "statusCode": null,
          "txnId": "my_order_37616",
          "txnStatus": "Enrolled",
          "unmappedStatus": "pending",
          "resendOtp": {
              "isSupported": true,
              "attemptsLeft": 2
          },
          "submitOtp": {
              "attemptsLeft": 3
          }
      },
      "result": {
          "otpPostUrl": "https://test.payu.in/ResponseHandler.php",
          "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vdGVzdC5wYXl1LmluLzhmODU2YTFlNzZiYTFjYjkzZWJjMjdjYzgyZjQxODZkZmIxNTQ1ZGU0MmIwNjRiNjk1N2Y3ZjY4ZGVmMzYwNWYxN2UzMDgyOTI5OGZiNjIyMjk4NDIwYzU0OTg3M2I2Zi9iYW5rQWNzIiBtZXRob2Q9InBvc3QiPjwvZm9ybT48c2NyaXB0IHR5cGU9J3RleHQvamF2YXNjcmlwdCc+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB3aW5kb3cub25sb2FkPWZ1bmN0aW9uKCl7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZG9jdW1lbnQuZm9ybXNbJ3BheW1lbnRfcG9zdCddLnN1Ym1pdCgpOwogICAgICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgICAgICAgICA8L3NjcmlwdD48L2JvZHk+PC9odG1sPg=="
      },
      "binData": {
          "pureS2SSupported": true,
          "issuingBank": "AXIS",
          "category": "creditcard",
          "cardType": "MAST",
          "isDomestic": true
      }
  }
  ```
</Accordion>

#### Check metaData.unmappedStatus field value

You must rely on the **metaData.unmappedStatus** field from the response JSON. Perform the following actions based on its value: 

- **If&#x20;**`metaData.unmappedStatus = 'pending'`**:**

  - Check the value of the `binData.pureS2SSupported` parameter:

    - **If&#x20;**`binData.pureS2SSupported = true`**:**
      - Invoke the OTP page and present it to the customer
      - Use Submit OTP API to collect & submit OTP from your page. For more information, refer to [Submit OTP API](ref:submit-otp-to-payu). The response for this API as in [Sample response for authentication only flow on Submit OTP API.](<#sample-response-for-authentication-only-flow on-submit-otp-api>)
      - If the customer opts to redirect to the bank ACS for entering the OTP:
        - Provide a "Redirect to Bank Page" link
        - Upon selection, load the value of the `result.acsTemplate` parameter as the Bank Form by decoding it using base64 encoding formula
    - **If&#x20;**`binData.pureS2SSupported = false`**:**
      - Redirect the customer using the `result.acsTemplate` parameter, which contains a Base64-encoded HTML form

> 📘
>
> **Note:** The `metaData.referenceId` value from the response JSON will be used as the input for the `referenceId` parameter in both the `submitOtp` and `resentOtp` APIs

- **If&#x20;**`metaData.unmappedStatus = 'failure'`**:**
  - Refer to the `metaData.statusCode` and `metaData.msg` fields for details on the failure reasons

#### Sample response for authentication only flow on Submit OTP API

<Accordion title="Sample response" icon="fa-code">
  ```json
  {
      "metaData": {
          "message": null,
          "referenceId": "51e428f4a4bb0feca97ba2b8c617df846fda061ee1b7ede115bb19c031b4b154",
          "statusCode": null,
          "txnId": "my_order_6292",
          "unmappedStatus": "pending",
          "submitOtp": {
              "status": "success"
          },
          "txnStatus": "Authenticated"
      },
      "result": {
          "postToBank": {
              "referenceId": "51e428f4a4bb0feca97ba2b8c617df846fda061ee1b7ede115bb19c031b4b154",
              "cres": "eyJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiJmNDQ4ZTQ0ZS1lYTg3LTEyOTctOTk3MC04YWU3YTM3ZTYyN2UiLCJUcmFuc2FjdGlvbklkIjoiNWE4MjQzMDktMzc4OS0xODIyLTAyNjItMWRkNjA5NzYiLCJjcmVzIjoiZXlKMGFISmxaVVJUVTJWeWRtVnlWSEpoYm5OSlJDSTZJbVkwTkRobE5EUmxMV1ZoT0RjdE1USTVOeTA1T1Rjd0xUaGhaVGRoTXpkbE5qSTNaU0lzSW1GamMxUnlZVzV6U1VRaU9pSXpOVGd3TWpZME1pMHpPVGc1TFRWa05UQXRPVEUwTlMwek5qQmtZekkyWWpaak1qQWlMQ0p0WlhOellXZGxWSGx3WlNJNklrTlNaWE1pTENKdFpYTnpZV2RsVm1WeWMybHZiaUk2SWpJdU1pNHdJaXdpWTJoaGJHeGxibWRsUTI5dGNHeGxkR2x2YmtsdVpDSTZJbGtpTENKMGNtRnVjMU4wWVhSMWN5STZJbGtpTENKbFkya2lPaUl3TWlKOSJ9",
              "additionalInfo": {
                  "authUdf1": "",
                  "authUdf2": "",
                  "authUdf3": "",
                  "authUdf4": "",
                  "authUdf5": "",
                  "authUdf6": "",
                  "authUdf7": "",
                  "authUdf8": "",
                  "authUdf9": "",
                  "authUdf10": ""
              }
          },
          "rawBankData": "cres=eyJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiJmNDQ4ZTQ0ZS1lYTg3LTEyOTctOTk3MC04YWU3YTM3ZTYyN2UiLCJUcmFuc2FjdGlvbklkIjoiNWE4MjQzMDktMzc4OS0xODIyLTAyNjItMWRkNjA5NzYiLCJjcmVzIjoiZXlKMGFISmxaVVJUVTJWeWRtVnlWSEpoYm5OSlJDSTZJbVkwTkRobE5EUmxMV1ZoT0RjdE1USTVOeTA1T1Rjd0xUaGhaVGRoTXpkbE5qSTNaU0lzSW1GamMxUnlZVzV6U1VRaU9pSXpOVGd3TWpZME1pMHpPVGc1TFRWa05UQXRPVEUwTlMwek5qQmtZekkyWWpaak1qQWlMQ0p0WlhOellXZGxWSGx3WlNJNklrTlNaWE1pTENKdFpYTnpZV2RsVm1WeWMybHZiaUk2SWpJdU1pNHdJaXdpWTJoaGJHeGxibWRsUTI5dGNHeGxkR2x2YmtsdVpDSTZJbGtpTENKMGNtRnVjMU4wWVhSMWN5STZJbGtpTENKbFkya2lPaUl3TWlKOSJ9"
      }
  }
  ```
</Accordion>

### Step 2b: Non-Native OTP Flow

On basis of a successful response of the Collect Payment (**\_payment**) API, you need to redirect the user to the bank page using **acsTemplate**. In case of Bank page authentication (Non-Native OTP),  ACS server will redirect the customer to termUrl passed in the payment request during initiation and authenticationResult will be posted along "cres" over the termUrl.

> 📘 Notes:
>
> - All callbacks POST form data on the merchant's `termUrl` that is passed in Initiate Transaction API.
> - Validation of the response happens on the basis of the hash value being returned in the hash value of the response.

<Accordion title="Response parameters over termURL" icon="fa-table">
  | Parameter                                        |                                                                                                                                                                                                                                                                                                                                                                                                                  Description | Example                                                          |
  | ------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------- |
  | rawBankData<br /><code>mandatory</code>          |                                                                                                                                                                                                                                                         <code>String</code> This parameter contains the raw response that is received from bank after authentication. The response is urlencoded and in query string format. | bankRespId=123\&status=success\&amount=1000                      |
  | referenceId<br /><code>mandatory</code>          |                                                                                                                                                                                                                                                                                                                             <code>String</code> This parameter contains the reference id being returned for the transaction. | TXN\_REF\_123456789                                              |
  | bankData<br /><code>mandatory</code>             | <code>JSON</code> This parameter contains the JSON string that is to be used for authorization call.This parameter is received in case of successful OTP submission of decoupled transactions. The postToBank contains messageDigest and pares that is to be posted back for authorization. For more information on the fields in this JSON, refer to [bankData JSON Fields Description](#bankdata-json-fields-description). |                                                                  |
  | authenticationStatus<br /><code>mandatory</code> |                                                                                                                                                                                                                                                                                                                                     <code>String</code> This parameter contains the authentication status of the transaction | SUCCESS                                                          |
  | hash<br /><code>mandatory</code>                 |                                                                  <code>String</code> This parameter contains the calculated hash of the data that is posted to the merchant. For security purpose it is recommended to validate the hash value before consuming the response. The hash calculation logic is: <code>sha512(authenticationStatus\\\|bankData\\\|rawBankData\\\|referenceId\\\|salt)</code> <code>String</code> | 5d41402abc4b2a76b9719d911017c592b2d4c3ef45d0b9e1c9b5a7b2c8f9e0d3 |
</Accordion>

<Accordion title="bankData JSON fields description" icon="fa-table">
  #### bankData JSON Fields Description

  | Field                                        |                                                                                                                                                                                                                                                                            Description | Applicable for EMV 3DS                                                                                               |
  | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | -------------------------------------------------------------------------------------------------------------------- |
  | cres<br /><code>mandatory</code>             |                                                                                                                                                             This field contains the Base64 encoded value received from ACS as part of the authentication response. <code>String</code> | Yes                                                                                                                  |
  | referenceId<br /><code>mandatory</code>      |                                                                                                                                                         This field is returned in case of decoupled flow. This field contains the reference id for the transaction <code>String</code> | REF\_12345                                                                                                           |
  | messageDigest<br /><code>mandatory</code>    |                                                                                                                                                     This field is returned in case of decoupled flow. This field contains the MD value being returned by the bank. <code>String</code> | d41d8cd98f00b204e9800998ecf8427e                                                                                     |
  | pares<br /><code>mandatory</code>            |                                                                                                                                                         This field is returned in case of decoupled flow. This field contains the pares being returned by the bank <code>String</code> | eJyrVkosLcmIz8nPS1WyUorPTFGyMjJQUkoD8ZNrAQytCFn                                                                      |
  | additionalInfo<br /><code>mandatory</code>   |                                                                                                                       This field is returned in case of decoupled flow. This field contains the data that is being used for the gateways that do not return pares. <code>String</code> | transaction\_id=12345\&status=pending                                                                                |
  | authorizationUrl<br /><code>mandatory</code> | This integration document assumes that you have opt-ed out for the particular configuration. The authorization URL in legacy integrations are present basis the config at PayU. Reach out to [integration@payu.in](mailto:integration@payu.in) to know more about. <code>String</code> | [https://secure.payu.in/merchant/postservice?form=5ea3a2d](https://secure.payu.in/merchant/postservice?form=5ea3a2d) |
</Accordion>

## Step 3: Authorize (charge) the payment

The authorization request is the final step of transaction processing. This again needs to be an S2S call from the merchant's server to PayU server.

> 📘
>
> **Note:**
>
> - **For Redirection Based authentication from termUrl(if being sent by PayU)**: If` authenticationStatus=success`, use `bankData` parameter value as it is to be passed under **authentication\_info** parameter of **Authorize Transaction API**
> - **For Native OTP based Authentication**: If **metaData.txnStatus**is "Authenticated",  use `result.postToBank `object value to be passed in the authentication\_info parameter of **Authorize Transaction API**.

#### Environment

|            |                                                                                                    |
| ---------- | -------------------------------------------------------------------------------------------------- |
| Test       | [https://test.payu.in/AuthorizeTransaction.php](https://test.payu.in/AuthorizeTransaction.php)     |
| Production | [https://secure.payu.in/AuthorizeTransaction.php](https://secure.payu.in/AuthorizeTransaction.php) |

<Accordion title="Request parameters" icon="fa-code">
  **Post URL**: The data to be posted has to be exactly the same as the JSON response received in the authentication response in [Step 2](#step-2-redirect-the-customer). The data must include the following parameters.

  | Parameter                                        |                                                                                                                                                                                                                                        Description | Example                                                          |
  | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | ---------------------------------------------------------------- |
  | key<br /><code>mandatory</code>                  |                                                                                                       The merchant key is provided by PayU and acts as a unique identifier for a specific merchant account in PayU's database. <code>String</code> | gtKFFx                                                           |
  | txnid<br /><code>mandatory</code>                |                                 The transaction ID is the order reference number generated by the merchant to track a particular order. It can be used only once and PayU's system does not accept a duplicate Transaction ID. <code>String</code> | ORD\_123456789                                                   |
  | amount<br /><code>mandatory</code>               |                                                                                      It should contain the payment amount of the particular transaction. The amount must be greater than Rs. 8000 for the cardless EMI option. <code>String</code> | 10000.00                                                         |
  | hash<br /><code>mandatory</code>                 | It is used to avoid the possibility of transaction tampering. The hash must in the following structure: <code>valueOf(key)\\\| valueOf(txnid) \\\| valueOf(amount) \\\|valueOf(authentication\_info) \\\| valueOf(salt)</code> <code>String</code> | 3af7c2b8e6f9d4e1a9b7c5e2f8d3a6b9e1c4f7a2d5e8b1c3f6a9d2e5b8c1a4f7 |
  | authentication\_info<br /><code>mandatory</code> |                                                                                                                               The JSON value received in the bankData on the Term URL or pass the fields as in the JSON example. <code>JSON</code> |                                                                  |

  #### Example for authentication\_info JSON

  ```json
  {
  "referenceId": "4b6dcb255093a92dc38599b82ac0f796619410e322a2b68ba69a6c7aa5dfb78d",
  "cres": "eyJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiIxMDY3ZjkyNi00YTJjLTE2MGMtOWU0ZS1lZmIxNjBiNjkwMGYiLCJUcmFuc2FjdGlvbklkIjoiNWU4NDE4ZDYtMWI4Ny01NzVhLWJkMzUtYjRkOWU0NjUiLCJjcmVzIjoiZXlKMGFISmxaVVJUVTJWeWRtVnlWSEpoYm5OSlJDSTZJakV3TmpkbU9USTJMVFJoTW1NdE1UWXdZeTA1WlRSbExXVm1ZakUyTUdJMk9UQXdaaUlzSW1GamMxUnlZVzV6U1VRaU9pSm1Zems1WkdJNU1pMWhOVGczTFRNek5qUXRNRFEzTXkxaE1HUTVPR1kwTnpReFptTWlMQ0p0WlhOellXZGxWSGx3WlNJNklrTlNaWE1pTENKdFpYTnpZV2RsVm1WeWMybHZiaUk2SWpJdU1pNHdJaXdpWTJoaGJHeGxibWRsUTI5dGNHeGxkR2x2YmtsdVpDSTZJbGtpTENKMGNtRnVjMU4wWVhSMWN5STZJbGtpTENKbFkya2lPaUl3TWlKOSJ9",
  "additionalInfo": {
    "authUdf1": "",
    "authUdf2": "",
    "authUdf3": "",
    "authUdf4": "",
    "authUdf5": "",
    "authUdf6": "",
    "authUdf7": "",
    "authUdf8": "",
    "authUdf9": "",
    "authUdf10": ""
  }
  }

  ```

  #### authentication\_info JSON Fields Description

  | **Field**      | **Description**                                                                                        | **Applicable to EMV 3DS** |
  | -------------- | ------------------------------------------------------------------------------------------------------ | ------------------------- |
  | cres           | This field contains the Base 64 encoded value received from ACS as part of the authentication response | Yes                       |
  | referenceId    | This field contains the same referenceId which sent in response of the first call                      |                           |
  | additionalInfo | This field can be used in the case of schemes where different parameters may need from merchant side.  |                           |
  | messageDigest  | This field includes the Base 64 encoding of (sha56 hash of the JSON data (post to server).             |                           |
  | pares          | This parameter contains the pares being returned by the bank.                                          |                           |
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```
  curl POST 'https://test.payu.in/AuthorizeTransaction' \
    --header 'Cookie: PHPSESSID=ca4slgf2hlcc3a80tauvnh96cr; PHPSESSID=69c3e6c6a9ee8' \
     --form 'key=PRiQvJ' \
     --form 'txnid=my_order_75942' \
     --form 'amount=2' \
     --form 'authentication_info={
    "referenceId": "4b6dcb255093a92dc38599b82ac0f796619410e322a2b68ba69a6c7aa5dfb78d",
    "cres": "eyJtZXNzYWdlVHlwZSI6IkNSZXMiLCJtZXNzYWdlVmVyc2lvbiI6IjIuMi4wIiwidGhyZWVEU1NlcnZlclRyYW5zSUQiOiIxMDY3ZjkyNi00YTJjLTE2MGMtOWU0ZS1lZmIxNjBiNjkwMGYiLCJUcmFuc2FjdGlvbklkIjoiNWU4NDE4ZDYtMWI4Ny01NzVhLWJkMzUtYjRkOWU0NjUiLCJjcmVzIjoiZXlKMGFISmxaVVJUVTJWeWRtVnlWSEpoYm5OSlJDSTZJakV3TmpkbU9USTJMVFJoTW1NdE1UWXdZeTA1WlRSbExXVm1ZakUyTUdJMk9UQXdaaUlzSW1GamMxUnlZVzV6U1VRaU9pSm1Zems1WkdJNU1pMWhOVGczTFRNek5qUXRNRFEzTXkxaE1HUTVPR1kwTnpReFptTWlMQ0p0WlhOellXZGxWSGx3WlNJNklrTlNaWE1pTENKdFpYTnpZV2RsVm1WeWMybHZiaUk2SWpJdU1pNHdJaXdpWTJoaGJHeGxibWRsUTI5dGNHeGxkR2x2YmtsdVpDSTZJbGtpTENKMGNtRnVjMU4wWVhSMWN5STZJbGtpTENKbFkya2lPaUl3TWlKOSJ9",
    "additionalInfo": {
      "authUdf1": "",
      "authUdf2": "",
      "authUdf3": "",
      "authUdf4": "",
      "authUdf5": "",
      "authUdf6": "",
      "authUdf7": "",
      "authUdf8": "",
      "authUdf9": "",
      "authUdf10": ""
    }
  }
  '
  ```
</Accordion>

## Step 4: Check the response from PayU

The response from PayU for Merchant Hosted and S2S integration is similar.

<ReverseHashing />

<Accordion title="Response parameters" icon="fa-code">
  The parameters in the response for similar for all S2S flows. For more information, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#response-for-initial-server-to-server-request).
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  The formatted JSON response is similar to the following:

  ```json
  {
     "metaData": {
        "message": "No Error",
        "referenceId": "b6035f64240b1862295bc571952cf984",
        "statusCode": "E000",
        "txnId": "payuTestTransaction2746829",
        "unmappedStatus": "success",
        "submitOtp": {
           "status": "success"
        }
     },
     "result": {
        "mihpayid": "15270336226",
        "mode": "CC",
        "status": "success",
        "key": "4wvMqy",
        "txnid": "payuTestTransaction2746829",
        "amount": "1.10",
        "addedon": "2022-06-01 17:39:29",
        "productinfo": "Product Info",
        "firstname": "Postman",
        "lastname": "",
        "address1": "",
        "address2": "",
        "city": "",
        "state": "",
        "country": "",
        "zipcode": "",
        "email": "test@payu.in",
        "phone": "9988776655",
        "udf1": "",
        "udf2": "",
        "udf3": "",
        "udf4": "",
        "udf5": "",
        "udf6": "",
        "udf7": "",
        "udf8": "",
        "udf9": "",
        "udf10": "",
        "card_token": "",
        "card_no": "XXXXXXXXXXXX8006",
        "field0": "",
        "field1": "6540854745166970506094",
        "field2": "947167",
        "field3": "1.10",
        "field4": "15270336226",
        "field5": "100",
        "field6": "",
        "field7": "AUTHPOSITIVE",
        "field8": "",
        "field9": "Transaction is Successful",
        "payment_source": "payuPureS2SAuth",
        "PG_TYPE": "CC-PG",
        "error": "E000",
        "error_Message": "No Error",
        "cardToken": "",
        "net_amount_debit": "1.1",
        "discount": "0.00",
        "offer_key": "",
        "offer_availed": "",
        "unmappedstatus": "captured",
        "hash": "cdc409dfd15a842b8d15d6627d0027619882ed800773fa413cef491ae8ff2ef0cdfa654680ba4c8f3567313c6a6b00b94cb3bb5e16bad21d26be01216a69af41",
        "bank_ref_no": "6540854745166970506094",
        "bank_ref_num": "6540854745166970506094",
        "bankcode": "CC",
        "surl": "",
        "curl": "",
        "furl": "",
        "card_hash": "fdb59253e36daf8b3969525ae3799ccb4bb41993a5d2fcaf22737ec3ac8b90ab"
     }
  }
  ```
</Accordion>

## Step 5. Verify the payment

<Verify_Payment_Tabs />

<br />
