---
title: UPI OTM Status Check API
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: UPI OTM Status Check API
excerpt: 'UPI Authorization Status Check API'
deprecated: false
hidden: false
metadata:
  title: UPI OTM Status Check API
  description: >-
    API documentation for checking the status of a UPI OTM authorization/mandate. Provides details about authorization status, authorized amount, and validity period.
  keywords:
    - UPI OTM Status Check
    - UPI Authorization Status
    - UPI Mandate
    - OTM Status
  robots: index
next:
  description: ''
---

The **UPI OTM Status Check** API allows you to check the status of a UPI (Unified Payments Interface) OTM authorization/mandate. It provides details about the authorization status, authorized amount, and validity period.

<br />

<Callout icon="👍" theme="okay">
  Experience the end-to-end **Merchant Hosted Checkout**> **UPI** flow and instantly generate the complete code for seamless, zero-coding integration into your website. 

  <HTMLBlock>{`
                            <style>
                            .tooltip-btn {
                                position: relative;
                                background-color: #4CAF50;
                                color: white;
                                padding: 10px 20px;
                                border: none;
                                border-radius: 5px;
                                cursor: pointer;
                                font-weight: bold; /* Added this line */
                            }
                            .tooltip-btn:hover::after {
                                content: attr(data-tooltip);
                                position: absolute;
                                bottom: 125%;
                                left: 50%;
                                transform: translateX(-50%);
                                background-color: #333;
                                color: white;
                                padding: 5px 10px;
                                border-radius: 4px;
                                white-space: nowrap;
                                font-size: 12px;
                                z-index: 1;
                            }
                            </style>

                            <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-otm-status', '_blank')" 
                                    class="tooltip-btn" 
                                    data-tooltip="Click here to see the Merchant Hosted Checkout > UPI OTM Status Check API and instantly generate the complete code needed for a zero-coding setup on your website.">
                                Experience the flow and get the code
                            </button>
  `}</HTMLBlock>
</Callout>

**HTTP Method**: GET

**Endpoint**: `/v1/transaction/upi_otm_status_check`

**Environment**

|                        |                                                  |
| :--------------------- | :----------------------------------------------- |
| Production Environment | \<[https://info.payu.in>](https://info.payu.in>) |

<Callout icon="📘" theme="info">
  **Notes and Best Practices**:

  * This API should be used to verify the status of a UPI mandate before attempting to process a transaction.
  * The paymentStartDate and paymentEndDate fields indicate the validity period of the mandate.
  * Always check the authRecordStatus field to ensure the mandate is "Active" before proceeding with any transaction.
</Callout>

## Request headers

<V2_paymentHeader />

## Request parameters

### Query parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Required</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Type</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>payuId</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Yes</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The unique PayU ID for the authorization.</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>25026596803</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Response parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Field</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Type</strong></th>
  <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>message</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Response message indicating success or failure.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>status</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Integer</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Status code (1 for success, 0 for failure).</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>authRecordStatus</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Status of the authorization record (e.g., "Active", "inactive").</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>authpayuid</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The PayU ID associated with the authorization.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>amount</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Decimal</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The authorized amount.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentStartDate</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The start date for the mandate validity (format: "YYYY-MM-DD HH:MM:SS").</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentEndDate</p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>The end date for the mandate validity (format: "YYYY-MM-DD HH:MM:SS").</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

## Status codes

| Status | Description |
| ------ | ----------- |
| 1      | Success     |
| 0      | Failure     |

## Sample request

```curl
curl --location 'https://info.payu.in/v1/transaction/upi_otm_status_check?payuId=25026596803' \
--header 'Content-Type: application/json' \
--header 'Date: {{date}}' \
--header 'Digest: {{digest}}' \
--header 'Authorization: {{authorization}}'
```

For creating HMAC authorization headers, replace the `{{date}}`, `{{digest}}`, and `{{authorization}}` with values generated from the pre script added in the documentation.

## Sample response

### Success scenario

```json
{
  "message": "Success",
  "status": 1,
  "authRecordStatus": "inactive",
  "authpayuid": "25026596803",
  "amount": 15675.0,
  "paymentStartDate": "2025-09-05 00:00:00",
  "paymentEndDate": "2025-09-18 00:00:00"
}
```

### Failure scenario (Error)

```json
{
  "status": 0,
  "message": "Failed"
}
```
