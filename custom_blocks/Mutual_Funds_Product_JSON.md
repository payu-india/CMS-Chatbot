---
name: Mutual_Funds_Product_JSON
---
  <Accordion title="Sample JSON" icon="fa-code">
    ```json
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

<HTMLBlock>{/*RDMX_HTMLBLOCK:Cjx0YWJsZSBzdHlsZT0id2lkdGg6IDEwMCU7IGJvcmRlci1jb2xsYXBzZTogY29sbGFwc2U7Ij4KICA8dGhlYWQ+CiAgICA8dHI+CiAgICAgIDx0aCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHN0cm9uZz5QYXJhbWV0ZXI8L3N0cm9uZz48L3RoPgogICAgICA8dGggc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxzdHJvbmc+RGVzY3JpcHRpb248L3N0cm9uZz48L3RoPgogICAgICA8dGggc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxzdHJvbmc+RXhhbXBsZTwvc3Ryb25nPjwvdGg+CiAgICA8L3RyPgogIDwvdGhlYWQ+CiAgPHRib2R5PgogICAgPHRyPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPnR5cGU8YnI+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPnN0cmluZzwvY29kZT4gVHJhbnNhY3Rpb24gdHlwZSwgbXVzdCBiZSAibXV0dWFsX2Z1bmQiPC9wPjwvdGQ+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+Im11dHVhbF9mdW5kIjwvcD48L3RkPgogICAgPC90cj4KICAgIDx0cj4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5hbW91bnQ8YnI+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPmZsb2F0PC9jb2RlPiBUaGUgdHJhbnNhY3Rpb24gYW1vdW50LCBtdXN0IG1hdGNoIG9yZGVyIGFtb3VudDwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjUwMDAwPC9wPjwvdGQ+CiAgICA8L3RyPgogICAgPHRyPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPnJlY2VpcHQ8YnI+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPnN0cmluZzwvY29kZT4gVW5pcXVlIFBHIHJlZmVyZW5jZSBudW1iZXIgKG1heCAyNSBjaGFycyk8L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD4iNzc0MDciPC9wPjwvdGQ+CiAgICA8L3RyPgogICAgPHRyPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPm1mX21lbWJlcl9pZDxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PGNvZGU+bnVtZXJpYzwvY29kZT4gTWVtYmVyIElEIGlzc3VlZCBieSBtdXR1YWwgZnVuZCBwbGF0Zm9ybSAoNS0yMCBjaGFycyk8L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD4iMTIzNDQ1IjwvcD48L3RkPgogICAgPC90cj4KICAgIDx0cj4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5tZl91c2VyX2lkPGJyPjxjb2RlPm1hbmRhdG9yeTwvY29kZT48L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD48Y29kZT5zdHJpbmc8L2NvZGU+IFVuaXF1ZSBtdXR1YWwgZnVuZCB1c2VyL2NsaWVudCBJRCAobWF4IDEwIGNoYXJzKTwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPiI3NzQwNyI8L3A+PC90ZD4KICAgIDwvdHI+CiAgICA8dHI+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+bWZfcGFydG5lcjxicj48Y29kZT5tYW5kYXRvcnk8L2NvZGU+PC9wPjwvdGQ+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PGNvZGU+c3RyaW5nPC9jb2RlPiBNdXR1YWwgZnVuZCBwbGF0Zm9ybTogY2Ftcywga2ZpbiwgYnNlLCBuc2UgKG1heCA0IGNoYXJzKTwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPiJjYW1zIjwvcD48L3RkPgogICAgPC90cj4KICAgIDx0cj4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD5tZl9pbnZlc3RtZW50X3R5cGU8YnI+PGNvZGU+bWFuZGF0b3J5PC9jb2RlPjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPnN0cmluZzwvY29kZT4gSW52ZXN0bWVudCB0eXBlOiBMIChMdW1wIFN1bSkgb3IgUyAoU0lQKSAoc2luZ2xlIGNoYXIpPC9wPjwvdGQ+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+IkwiPC9wPjwvdGQ+CiAgICA8L3RyPgogICAgPHRyPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPnBsYW48YnI+PGNvZGU+b3B0aW9uYWw8L2NvZGU+PC9wPjwvdGQ+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+PGNvZGU+c3RyaW5nPC9jb2RlPiBNdXR1YWwgZnVuZCBwbGFuIG5hbWU8L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD4iR0QiPC9wPjwvdGQ+CiAgICA8L3RyPgogICAgPHRyPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPmZvbGlvPGJyPjxjb2RlPm9wdGlvbmFsPC9jb2RlPjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPnN0cmluZzwvY29kZT4gVW5pcXVlIG11dHVhbCBmdW5kIGFjY291bnQgaWRlbnRpZmllcjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPiIxMjM0NTY3OCI8L3A+PC90ZD4KICAgIDwvdHI+CiAgICA8dHI+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+b3B0aW9uPGJyPjxjb2RlPm9wdGlvbmFsPC9jb2RlPjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPnN0cmluZzwvY29kZT4gTXV0dWFsIGZ1bmQgcGxhbiBvcHRpb248L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD4iRyI8L3A+PC90ZD4KICAgIDwvdHI+CiAgICA8dHI+CiAgICAgIDx0ZCBzdHlsZT0iYm9yZGVyOiAxcHggc29saWQgI2RkZDsgcGFkZGluZzogOHB4OyI+PHA+c2NoZW1lPGJyPjxjb2RlPm9wdGlvbmFsPC9jb2RlPjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPnN0cmluZzwvY29kZT4gTXV0dWFsIGZ1bmQgdHlwZS9zY2hlbWU8L3A+PC90ZD4KICAgICAgPHRkIHN0eWxlPSJib3JkZXI6IDFweCBzb2xpZCAjZGRkOyBwYWRkaW5nOiA4cHg7Ij48cD4iTFQiPC9wPjwvdGQ+CiAgICA8L3RyPgogICAgPHRyPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPm1mX2FtY19jb2RlPGJyPjxjb2RlPm9wdGlvbmFsPC9jb2RlPjwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPjxjb2RlPnN0cmluZzwvY29kZT4gQXNzZXQgTWFuYWdlbWVudCBDb21wYW55IGNvZGUgKG1heCA1IGNoYXJzKTwvcD48L3RkPgogICAgICA8dGQgc3R5bGU9ImJvcmRlcjogMXB4IHNvbGlkICNkZGQ7IHBhZGRpbmc6IDhweDsiPjxwPiJVVEIiPC9wPjwvdGQ+CiAgICA8L3RyPgogIDwvdGJvZHk+CjwvdGFibGU+Cgo=:RDMX_HTMLBLOCK*/}</HTMLBlock>
  </Accordion>

 <Accordion title="Validation Rules" icon="fa-code">

| Parameter | Description | Example |
|---|---|---|
| type | Must always be `"mutual_fund"` | `"mutual_fund"` |
| amount | Must match the overall order amount and be in paise | - |
| receipt | Must be unique across transactions | - |
| mf_member_id | Must be numeric with length between 5-20 characters | - |
| mf_user_id | Maximum 10 characters allowed | - |
| mf_partner | Must be one of: `"cams"`, `"kfin"`, `"bse"`, `"nse"` | `"cams"` |
| mf_investment_type | Only `"L"` (Lump Sum) or `"S"` (SIP) allowed | `"L"` |
| **Optional Field Validations**| |
| mf_amc_code | Maximum 5 characters | - |
| receipt | Maximum 25 characters for SIP registration ID | - |

</Accordion>

<br />
