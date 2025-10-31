---
title: Webhook Alerts
deprecated: false
hidden: true
metadata:
  robots: index
---
This section provides how to configure webhook alerts to receive real-time notifications about transaction anomalies and system events. It covers the essential prerequisites for setting up your webhook endpoint, including network requirements and response specifications, followed by detailed examples of the POST request format and payload structure. By following this guide, developers can successfully configure their applications to receive and process Beacon alerts for monitoring PayU transaction engine performance and detecting critical issues.

## Prerequisites

<Accordion title="HTTP/HTTPS Endpoint URL" icon="fa-table">
  * **Requirement**: You must provide a publicly accessible HTTPS URL endpoint
  * **Format**: `https://your-domain.com/webhook-endpoint`
  * **Examples**:
    * `https://api.yourcompany.com/webhooks/alerts`
    * `https://yourapp.com/notifications/receive`
</Accordion>

<Accordion title="Filter Conditions (Optional)" icon="fa-table">
  * **Alert Types**: Specify which alert types you want to receive basis
    * different entities
    * different stats
</Accordion>

<Accordion title="Network Access Requirements" icon="fa-table">
  * **Firewall Configuration**: Ensure your endpoint is accessible from our service
  * **Port Access**: HTTPS (443) ports
  * **Response Time**: Your endpoint should respond within **5 seconds**
  * **Availability**: Recommended uptime of 99%+ for reliable delivery
</Accordion>

<Accordion title="Endpoint Response Requirements" icon="fa-table">
  * **Success Response**: Return HTTP status 200 OK
  * **Response Body**: Empty body or simple acknowledgment
  * **Failure Handling**: Non-200 responses will trigger retries
  * **Timeout**: Must respond within 5 seconds
</Accordion>

## Post Request Format

<Accordion title="Headers" icon="fa-table">
  ```
  POST /webhook-endpoint HTTP/1.1  
  Host: [domain]  
  Content-Type: application/json  
  User-Agent: axios/[version]  
  Content-Length: [auto-calculated]  
  Accept: application/json, text/plain, */*  
  ```
</Accordion>

<Accordion title="Request Body" icon="fa-table">
  ```json
  {
    "alert_id": "e58a1a37-496e-4d49-b9bd-88b3029c97ac",
    "alert_group_id": "7595875a-3557-4e90-a61a-b0406e987b3f",
    "notification_id": "8cf84511-430d-4de5-aa1d-ffb2072b39ca",
    "notification_triggered_at": "2025-05-03T10:14:23+05:30",
    "notification_type": "detection",
    "product": "PayuBizTransactionEngine",
    "metric": "success_rate",
    "entity_identifier": "flipkart",
    "entity_type": "merchant",
    "entity_name": "flipkart",
    "started_at": "2025-05-03T05:17:00+05:30",
    "ended_at": null,
    "current_state": "ongoing",
    "criticality_score": 45,
    "stats": {
      "failed_count": 1000,
      "success_rate_during_downtime": 33.75,
      "reference_srt": 51.629999999999995,
      "srt_drop_abs": 17.88,
      "srt_drop_rel": 34.63,
      "zero_srt": false,
      "duration": 262
    },
    "schema_version": "1.0"
  }
  ```

  Response detail:

  | **key**                     | **Sample value**                       | **Description**           |
  | --------------------------- | -------------------------------------- | ------------------------- |
  | `alert_id`                  | `e58a1a37-496e-4d49-b9bd-88b3029c97ac` | PayU Alert ID             |
  | `alert_group_id`            | `7595875a-3557-4e90-a61a-b0406e987b3f` | PayU Alert Parent ID      |
  | `notification_id`           | `8cf84511-430d-4de5-aa1d-ffb2072b39ca` | PayU Notification ID      |
  | `notification_triggered_at` | `2025-05-03T10:14:23+05:30`            | Alert Notification Time   |
  | `notification_type`         | `detection`                            | Alert Notification Type   |
  | `product`                   | `PayuBizTransactionEngine`             | Alerting Product          |
  | `metric`                    | `success_rate`                         | Alerting Metric           |
  | `entity_identifier`         | `flipkart`                             | Impacted Area entity Name |
  | `entity_type`               | `merchant`                             | Impacted Area             |
  | `entity_name`               | `flipkart`                             | Impacted Area entity Name |
  | `started_at`                | `2025-05-03T05:17:00+05:30`            | Issue Detected At         |
  | `ended_at`                  |                                        | Issue Resolved At         |
  | `current_state`             | `ongoing`                              | Issue Status              |
  | `criticality_score`         | `45`                                   | Alert Severity            |

  1. `[0-30]` is LOW
  2. `[31-60]` is MEDIUM
  3. `[61-100]` is HIGH                           |\
     \| `stats`                        | **key** | **value** | Basis stats of Alert                               |\
     \| `failed_count`                 | `1000`                                     | Number transaction failure detected             |\
     \| `success_rate_during_downtime` | `33.75`                                    | Success Rate (SRT) during Downtime              |\
     \| `reference_srt`                | `51.63`                                    | Success Rate Reference to Past 10 days trend    |\
     \| `srt_drop_abs`                 | `17.88`                                    | Absolute Drop identified in Success Rate        |\
     \| `srt_drop_rel`                 | `34.63`                                    | Relative Drop Identified                        |\
     \| `zero_srt`                     | `FALSE`                                    | Is ZERO SRT Detected                            |\
     \| `duration`                     | `262`                                      | Anomaly Duration                                |\
     \| `schema_version`               | `1`                                        | Alert Version                                   |
</Accordion>

<Accordion title="Retry Configuration" icon="fa-table">
  ```javascript
  axiosRetry(axios, {
    retries: 3,
    shouldResetTimeout: true,
    retryCondition: () => true
  });
  ```
</Accordion>
