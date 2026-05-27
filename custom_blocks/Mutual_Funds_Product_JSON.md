---
name: Mutual_Funds_Product_JSON
---
<Accordion title="Wealth Tech Object (wtParams) Fields" icon="fa-cog">

  <Accordion title="Sample JSON" icon="fa-code">
    ```
    "product": {
        "wtParams": [
          {
            "type": "mutual_fund",
            "plan": "GD",
            "amount": "50000",
            "option": "G",
            "scheme": "LT",
            "receipt": "77407",
            "mf_member_id": "123445",
            "mf_user_id": "77407",
            "mf_partner": "cams",
            "mf_investment_type": "L",
            "mf_amc_code": "UTB"
          }
        ]
      }
    ```
  </Accordion>

  <Accordion title="Wealth Tech object (wtParams) fields Description" icon="fa-cog">
    These parameters are included within the `product` field as a JSON array under the fiedl `wtParams`:

   <HTMLBlock>{/*RDMX_HTMLBLOCK:Cgo8dGFibGUgc3R5bGU9IndpZHRoOiAxMDAlOyBib3JkZXItY29sbGFwc2U6IGNvbGxhcHNlOyI+CiAgPHRoZWFkPgogICAgPHRyPgogICAgICA8dGggc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxzdHJvbmc+UGFyYW1ldGVyPC9zdHJvbmc+PC90aD4KICAgICAgPHRoIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48c3Ryb25nPkRlc2NyaXB0aW9uPC9zdHJvbmc+PC90aD4KICAgICAgPHRoIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48c3Ryb25nPkV4YW1wbGU8L3N0cm9uZz48L3RoPgogICAgPC90cj4KICA8L3RoZWFkPgogIDx0Ym9keT4KICAgIDx0cj4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD50eXBlPGJyPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5zdHJpbmc8L2NvZGU+IFRyYW5zYWN0aW9uIHR5cGUsIG11c3QgYmUgIm11dHVhbF9mdW5kIjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPiJtdXR1YWxfZnVuZCI8L3A+PC90ZD4KICAgIDwvdHI+CiAgICA8dHI+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+YW1vdW50PGJyPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5mbG9hdDwvY29kZT4gVGhlIHRyYW5zYWN0aW9uIGFtb3VudCwgbXVzdCBtYXRjaCBvcmRlciBhbW91bnQ8L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD41MDAwMDwvcD48L3RkPgogICAgPC90cj4KICAgIDx0cj4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5yZWNlaXB0PGJyPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5zdHJpbmc8L2NvZGU+IFVuaXF1ZSBQRyByZWZlcmVuY2UgbnVtYmVyIChtYXggMjUgY2hhcnMpPC9wPjwvdGQ+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+Ijc3NDA3IjwvcD48L3RkPgogICAgPC90cj4KICAgIDx0cj4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5tZl9tZW1iZXJfaWQ8YnI+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPm51bWVyaWM8L2NvZGU+IE1lbWJlciBJRCBpc3N1ZWQgYnkgbXV0dWFsIGZ1bmQgcGxhdGZvcm0gKDUtMjAgY2hhcnMpPC9wPjwvdGQ+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+IjEyMzQ0NSI8L3A+PC90ZD4KICAgIDwvdHI+CiAgICA8dHI+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+bWZfdXNlcl9pZDxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PGNvZGU+c3RyaW5nPC9jb2RlPiBVbmlxdWUgbXV0dWFsIGZ1bmQgdXNlci9jbGllbnQgSUQgKG1heCAxMCBjaGFycyk8L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD4iNzc0MDciPC9wPjwvdGQ+CiAgICA8L3RyPgogICAgPHRyPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPm1mX3BhcnRuZXI8YnI+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPnN0cmluZzwvY29kZT4gTXV0dWFsIGZ1bmQgcGxhdGZvcm06IGNhbXMsIGtmaW4sIGJzZSwgbnNlIChtYXggNCBjaGFycyk8L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD4iY2FtcyI8L3A+PC90ZD4KICAgIDwvdHI+CiAgICA8dHI+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+bWZfaW52ZXN0bWVudF90eXBlPGJyPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5zdHJpbmc8L2NvZGU+IEludmVzdG1lbnQgdHlwZTogTCAoTHVtcCBTdW0pIG9yIFMgKFNJUCkgKHNpbmdsZSBjaGFyKTwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPiJMIjwvcD48L3RkPgogICAgPC90cj4KICAgIDx0cj4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5wbGFuPGJyPjxjb2RlPm9wdGlvbmFsPC9jb2RlPjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPnN0cmluZzwvY29kZT4gTXV0dWFsIGZ1bmQgcGxhbiBuYW1lPC9wPjwvdGQ+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+IkdEIjwvcD48L3RkPgogICAgPC90cj4KICAgIDx0cj4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5mb2xpbzxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5zdHJpbmc8L2NvZGU+IFVuaXF1ZSBtdXR1YWwgZnVuZCBhY2NvdW50IGlkZW50aWZpZXI8L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD4iMTIzNDU2NzgiPC9wPjwvdGQ+CiAgICA8L3RyPgogICAgPHRyPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPm9wdGlvbjxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5zdHJpbmc8L2NvZGU+IE11dHVhbCBmdW5kIHBsYW4gb3B0aW9uPC9wPjwvdGQ+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+IkciPC9wPjwvdGQ+CiAgICA8L3RyPgogICAgPHRyPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPnNjaGVtZTxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5zdHJpbmc8L2NvZGU+IE11dHVhbCBmdW5kIHR5cGUvc2NoZW1lPC9wPjwvdGQ+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+IkxUIjwvcD48L3RkPgogICAgPC90cj4KICAgIDx0cj4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5tZl9hbWNfY29kZTxicj48Y29kZT5vcHRpb25hbDwvY29kZT48L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5zdHJpbmc8L2NvZGU+IEFzc2V0IE1hbmFnZW1lbnQgQ29tcGFueSBjb2RlIChtYXggNSBjaGFycyk8L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD4iVVRCIjwvcD48L3RkPgogICAgPC90cj4KICA8L3Rib2R5Pgo8L3RhYmxlPgoK:RDMX_HTMLBLOCK*/}</HTMLBlock>


    <Accordion title="Validation Rules" icon="fa-code">
      <Accordion title="Mandatory Field Validations" icon="fa-code">
       - **type**: Must always be `"mutual_fund"`
       - **amount**: Must match the overall order amount and be in paise
       - **receipt**: Must be unique across transactions
       - **mf\_member\_id**: Must be numeric with length between 5-20 characters
       - **mf\_user\_id**: Maximum 10 characters allowed
       - **mf\_partner**: Must be one of: `"cams"`, `"kfin"`, `"bse"`, `"nse"`
       - **mf\_investment\_type**: Only `"L"` (Lump Sum) or `"S"` (SIP) allowed
      </Accordion>

      <Accordion title="Optional Field Validations" icon="fa-code">
       - **mf\_amc\_code**: Maximum 5 characters
       - **receipt**: Maximum 25 characters for SIP registration ID
      </Accordion>
    </Accordion>
  </Accordion>
</Accordion>

<br />
