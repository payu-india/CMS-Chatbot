---
title: ' Merchant Upcoming and Pending Settlement API'
deprecated: false
hidden: true
metadata:
  robots: index
---
Retrieve information about upcoming and pending settlements for a merchant. This API provides visibility into future settlements, helping merchants with cash flow planning and financial forecasting.

**Environment**

|                        |                                                                                                                                |
| :--------------------- | :----------------------------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://test.payu.in/settlement/v1/merchantUpcomingSettlement](https://test.payu.in/settlement/v1/merchantUpcomingSettlement) |
| Production Environment | [https://info.payu.in/settlement/v1/merchantUpcomingSettlement](https://info.payu.in/settlement/v1/merchantUpcomingSettlement) |

**HTTP Method**: POST

<Accordion title="Request Parameters" icon="fa-table">
  ### Request Header

  <HeaderAuthentication />

  ### Other Header Parameters

  | Parameter                        | Description                                                                      | Example                       |
  | -------------------------------- | -------------------------------------------------------------------------------- | ----------------------------- |
  | mid<br /><code>mandatory</code>  | <code>String</code> Merchant identifier that the integration was registered with | \<MerchantId>                 |
  | Date<br /><code>mandatory</code> | <code>String</code> Request date header in RFC-1123 format                       | Tue, 07 Apr 2026 06:14:56 GMT |
</Accordion>

<Accordion title="Sample Request" icon="fa-code">
  ```curl
curl --location 'https://test.payu.in/settlement/v1/merchantUpcomingSettlement' \
--header 'mid: 12202' \
--header 'Authorization: {{authorization}}' \
--header 'Date: {{date}}'

  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-code">
  ```json
  {
    "code": "2000",
    "message": "Success",
    "status": 0,
    "result": {
        "holdSettlementStatus": 0,
        "lastSettledAmount": 2197.19,
        "lastSettlementTime": "2026-04-06 14:22:12",
        "upcomingSettlementAmount": 235129.81,
        "upcomingSettlementTime": "2026-04-08 09:15:00",
        "totalSettlementPendingAmount": 73224295.78,
        "currencyType": "USD",
        "merchantId": 8515874,
        "pendingSettlementBreakdown": {
            "saleAmount": 77328963.90,
            "adjustmentAmount": 0.00,
            "refundAmount": -975745.51,
            "chargebackAmount": -120622.04,
            "refundReversalAmount": 0.00,
            "chargebackReversalAmount": 0.00,
            "serviceFee": -2778968.71,
            "serviceTax": -226059.93,
            "convenienceFee": 0.00,
            "convenienceTax": 0.00,
            "additionalServiceFee": -158.58,
            "additionalServiceTax": -28.54,
            "txnCount": 53057
        }
    }
  }
  ```
</Accordion>

<Accordion title="Response Parameters" icon="fa-table">
  | Parameter | Type    | Description                                                                                                                                    |
  | --------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
  | status    | Integer | Response status (1 = success, 0 = failure)                                                                                                     |
  | msg       | String  | Response message                                                                                                                               |
  | result    | Object  | Main response data container in JSON format. For more information, refer to  [result JSON Field Descriptions](#result-json-field-descriptions) |

  ### result JSON Field Descriptions

  | Field                          | Description                                                                                                                                                                                                                                                                                                          |
  | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | `holdSettlementStatus`         | Indicator whether merchant settlements are on hold. Values: `1` = on hold, `0` = not on hold                                                                                                                                                                                                                         |
  | `lastSettledAmount`            | Monetary amount that was settled in the most recent settlement                                                                                                                                                                                                                                                       |
  | `upcomingSettlementAmount`     | Monetary amount expected to be settled in the next settlement cycle                                                                                                                                                                                                                                                  |
  | `upcomingSettlementTime`       | Timestamp (IST date-time format) of the next scheduled settlement                                                                                                                                                                                                                                                    |
  | `totalSettlementPendingAmount` | Total monetary amount still pending settlement (aggregate outstanding balance)                                                                                                                                                                                                                                       |
  | `currencyType`                 | Currency code for amounts (e.g., "INR")                                                                                                                                                                                                                                                                              |
  | `merchantId`                   | Identifier of the merchant for whom the snapshot is returned                                                                                                                                                                                                                                                         |
  | `pendingSettlementBreakdown`   | JSON Object providing a component-wise breakdown of the pending/upcoming settlement amount. Numeric amounts may be 0 or omitted; negative values denote deductions/credits. For more information, refer to [pendingSettlementBreakdown JSON Fields Description](#pendingSettlementBreakdown-json-fields-description) |

  #### pendingSettlementBreakdown JSON Fields Description

  | Field                      | Description                                                   |
  | -------------------------- | ------------------------------------------------------------- |
  | `saleAmount`               | Total transaction (sales) amount                              |
  | `adjustmentAmount`         | Adjustments applied (positive or negative adjustments)        |
  | `refundAmount`             | Total refunds (usually negative when reducing payable amount) |
  | `chargebackAmount`         | Total chargebacks (reductions due to disputes)                |
  | `refundReversalAmount`     | Amounts from reversed refunds (restored to merchant)          |
  | `chargebackReversalAmount` | Amounts from reversed chargebacks                             |
  | `serviceFee`               | Service fees charged                                          |
  | `serviceTax`               | Tax on service fee                                            |
  | `convenienceFee`           | Convenience fees charged to customer (affect settlement)      |
  | `convenienceTax`           | Tax on convenience fee                                        |
  | `additionalServiceFee`     | Any additional service fees                                   |
  | `additionalServiceTax`     | Tax on additional service fee                                 |
  | `txnCount`                 | Number of transactions contributing to the breakdown          |
</Accordion>