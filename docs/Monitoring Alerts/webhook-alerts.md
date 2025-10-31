---
title: Webhook Alerts
deprecated: false
hidden: true
metadata:
  robots: index
---
This documentation provides comprehensive guidance for integrating with webhook alert system to receive real-time notifications about transaction anomalies and system events. It covers the essential prerequisites for setting up your webhook endpoint, including network requirements and response specifications, followed by detailed examples of the POST request format and payload structure. By following this guide, developers can successfully configure their applications to receive and process alerts for monitoring PayU transaction engine performance and detecting critical issues.

## **Getting Started**

**Before You Begin:**

* [ ] You have a web server that can receive HTTP requests
* [ ] Your server has a public URL (not localhost)
* [ ] You can modify your server code to handle new endpoints
* [ ] You have basic knowledge of JSON and HTTP

**What You'll Need:**

* Public HTTPS URL endpoint (we'll show you how to create one)
* Way to receive POST requests (we provide code examples)
* 5 minutes to set up and test

## **Prerequisites**

<Accordion title="1. HTTP/HTTPS Endpoint URL" icon="fa-link">
  * **Requirement**: You must provide a publicly accessible HTTPS URL endpoint
  * **Format**: `https://your-domain.com/webhook-endpoint`
  * **Examples**:
    * `https://api.yourcompany.com/webhooks/alerts`
    * `https://yourapp.com/notifications/receive`
</Accordion>

<Accordion title="2. Filter Conditions (Optional)" icon="fa-filter">
  * **Alert Types**: Specify which alert types you want to receive basis
    * different entities
    * different stats
</Accordion>

<Accordion title="3. Network Access Requirements" icon="fa-network-wired">
  * **Firewall Configuration**: Ensure your endpoint is accessible from our service
  * **Port Access**: HTTPS (443) ports
  * **Response Time**: Your endpoint should respond within **5 seconds**
  * **Availability**: Recommended uptime of 99%+ for reliable delivery
</Accordion>

<Accordion title="4. Endpoint Response Requirements" icon="fa-check-circle">
  * **Success Response**: Return HTTP status 200 OK
  * **Response Body**: Empty body or simple acknowledgment
  * **Failure Handling**: Non-200 responses will trigger retries
  * **Timeout**: Must respond within 5 seconds
</Accordion>

## **POST Request Format**

<Accordion title="Request Headers" icon="fa-file-code">
  ```
  POST /webhook-endpoint HTTP/1.1  
  Host: [domain]  
  Content-Type: application/json  
  User-Agent: axios/[version]  
  Content-Length: [auto-calculated]  
  Accept: application/json, text/plain, */*  
  ```
</Accordion>

<Accordion title="Request Body" icon="fa-database">
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

  ## Response Details

  | Parameter                   | Description                                                                                    | Sample Value                           |
  | --------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------- |
  | `alert_id`                  | PayU Alert ID                                                                                  | `e58a1a37-496e-4d49-b9bd-88b3029c97ac` |
  | `alert_group_id`            | PayU Alert Parent ID                                                                           | `7595875a-3557-4e90-a61a-b0406e987b3f` |
  | `notification_id`           | PayU Notification ID                                                                           | `8cf84511-430d-4de5-aa1d-ffb2072b39ca` |
  | `notification_triggered_at` | Alert Notification Time                                                                        | `2025-05-03T10:14:23+05:30`            |
  | `notification_type`         | Alert Notification Type                                                                        | `detection`                            |
  | `product`                   | Alerting Product                                                                               | `PayuBizTransactionEngine`             |
  | `metric`                    | Alerting Metric                                                                                | `success_rate`                         |
  | `entity_identifier`         | Impacted Area entity Name                                                                      | `flipkart`                             |
  | `entity_type`               | Impacted Area                                                                                  | `merchant`                             |
  | `entity_name`               | Impacted Area entity Name                                                                      | `flipkart`                             |
  | `started_at`                | Issue Detected At                                                                              | `2025-05-03T05:17:00+05:30`            |
  | `ended_at`                  | Issue Resolved At                                                                              |                                        |
  | `current_state`             | Issue Status                                                                                   | `ongoing`                              |
  | `criticality_score`         | Alert Severity <br /> • `[0-30]` is LOW <br />• `[31-60]` is MEDIUM <br />• `[61-100]` is HIGH | `45`                                   |
  | `stats`                     | Basis stats of Alert (object containing detailed metrics). For more information, refer to [stats Object field descriptions](https://docs.payu.in/docs/webhook-alerts#stats-object-field-descriptions).                                      | `{object}`                             |

  ### stats Object field descriptions

  | Field                          | Description                                  | Sample Value |
  | ------------------------------ | -------------------------------------------- | ------------ |
  | `failed_count`                 | Number of transaction failures detected      | `1000`       |
  | `success_rate_during_downtime` | Success Rate (SRT) during Downtime           | `33.75`      |
  | `reference_srt`                | Success Rate Reference to Past 10 days trend | `51.63`      |
  | `srt_drop_abs`                 | Absolute Drop identified in Success Rate     | `17.88`      |
  | `srt_drop_rel`                 | Relative Drop Identified                     | `34.63`      |
  | `zero_srt`                     | Is ZERO SRT Detected                         | `FALSE`      |
  | `duration`                     | Anomaly Duration (in minutes)                | `262`        |
  | `schema_version`               | Alert Schema Version                         | `1.0`        |
</Accordion>

<Accordion title="Retry Configuration" icon="fa-redo">
  ```javascript
  axiosRetry(axios, {
    retries: 3,
    shouldResetTimeout: true,
    retryCondition: () => true
  });
  ```

  **What This Means:**

  * Beacon will try to deliver the webhook **3 times** if your endpoint fails
  * Each retry resets the timeout period
  * Any error response triggers a retry attempt

  **Retry Schedule:**

  1. **First attempt**: Immediate
  2. **Retry 1**: After 1 minute
  3. **Retry 2**: After 5 minutes
  4. **Retry 3**: After 15 minutes
  5. **Give up**: Alert marked as failed
</Accordion>

## **Testing & Troubleshooting**

<Accordion title="Test Your Webhook Endpoint" icon="fa-vial">
  ### **Step 1: Basic Connectivity Test**

  ```bash
  # Test if your endpoint responds
  curl -X POST https://yourdomain.com/webhook/beacon   -H "Content-Type: application/json"   -d '{"test": "ping"}'
  ```

  ### **Step 2: Simulate Real Alert**

  ```bash
  # Send a sample alert payload
  curl -X POST https://yourdomain.com/webhook/beacon   -H "Content-Type: application/json"   -d '{
      "alert_id": "test-123",
      "notification_type": "detection", 
      "criticality_score": 45,
      "entity_identifier": "test-merchant"
    }'
  ```

  ### **Step 3: Verify Processing**

  Check your application logs to ensure:

  * ✅ Alert was received
  * ✅ Data was parsed correctly
  * ✅ Your processing logic ran
  * ✅ Response was sent quickly (\< 5 seconds)

  **Common Testing Tools:**

  * [Webhook.site](https://webhook.site) - Test endpoint URLs
  * [Postman](https://postman.com) - Send test requests
  * [ngrok](https://ngrok.com) - Expose localhost for testing
</Accordion>

<Accordion title="Common Issues & Solutions" icon="fa-tools">
  ### **❌ "Webhook delivery failed"**

  **Possible Causes:**

  * Your endpoint returned non-200 status code
  * Request timed out (> 5 seconds)
  * Network connectivity issues

  **Solutions:**

  ```python
  # Add timeout handling
  import signal

  def timeout_handler(signum, frame):
      raise TimeoutError("Request took too long")

  signal.signal(signal.SIGALRM, timeout_handler)
  signal.alarm(4)  # 4 second timeout

  try:
      # Your alert processing code here
      process_alert(alert_data)
  finally:
      signal.alarm(0)  # Disable timeout
  ```

  ### **❌ "Cannot reach endpoint"**

  **Possible Causes:**

  * URL not publicly accessible
  * Firewall blocking requests
  * Wrong URL format

  **Solutions:**

  1. Test with online tools: `curl -I https://yourdomain.com/webhook`
  2. Check firewall settings
  3. Verify HTTPS certificate is valid

  ### **❌ "Receiving duplicate alerts"**

  **Possible Causes:**

  * Your endpoint returned error on first attempt
  * Network issues caused retries

  **Solutions:**

  ```python
  # Implement idempotency
  alert_cache = {}

  def is_duplicate(alert_id):
      if alert_id in alert_cache:
          return True
      alert_cache[alert_id] = True
      return False
  ```
</Accordion>

<Accordion title="Advanced Features" icon="fa-graduation-cap">
  ### **Webhook Verification (Security)**

  ```python
  import hmac
  import hashlib

  def verify_webhook(payload, signature, secret):
      expected = hmac.new(
          secret.encode('utf-8'),
          payload.encode('utf-8'), 
          hashlib.sha256
      ).hexdigest()
      
      return hmac.compare_digest(signature, expected)
  ```

  ### **Alert Correlation**

  ```python
  # Group related alerts together
  def correlate_alerts(new_alert):
      entity = new_alert['entity_identifier']
      timeframe = datetime.now() - timedelta(minutes=10)
      
      related_alerts = [
          alert for alert in recent_alerts 
          if alert['entity_identifier'] == entity 
          and alert['timestamp'] > timeframe
      ]
      
      return related_alerts
  ```

  ### **Custom Alert Enrichment**

  ```python
  def enrich_alert(alert_data):
      entity = alert_data['entity_identifier']
      
      # Add business context
      alert_data['business_impact'] = get_revenue_impact(entity)
      alert_data['contact_info'] = get_entity_contacts(entity)
      alert_data['escalation_policy'] = get_escalation_rules(entity)
      
      return alert_data
  ```
</Accordion>
