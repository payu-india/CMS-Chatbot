---
title: Webhook Alerts
deprecated: false
hidden: true
metadata:
  robots: index
---
# Beacon Webhook Alerts - Developer Guide

## 📚 **Getting Started**

<Accordion title="What are Webhooks?" icon="fa-question-circle">

**Simple Explanation:** Think of webhooks as automatic phone calls from our system to yours. When something important happens (like a transaction failure), Beacon automatically sends a message to your application with all the details.

**Why Use Webhooks?**
- Get **instant notifications** when issues occur
- **Automate responses** to problems
- **Monitor your business** in real-time
- **Reduce manual monitoring** work

**Real-World Example:** When your payment success rate drops below normal, Beacon immediately notifies your app so you can investigate or alert your team.

</Accordion>

<Accordion title="How Webhooks Work" icon="fa-cogs">

```
1. Issue Detected → 2. Beacon Sends Alert → 3. Your App Receives → 4. You Take Action
   (Low success rate)    (HTTP POST to your URL)    (Process the data)    (Notify team/fix)
```

**Flow Breakdown:**
1. **Beacon monitors** your transaction data 24/7
2. **Algorithm detects** anomalies or issues  
3. **HTTP POST request** sent to your endpoint URL
4. **Your application** receives and processes the alert
5. **You respond** with actions (notifications, auto-scaling, etc.)

</Accordion>

<Accordion title="Quick Start Checklist" icon="fa-rocket">

✅ **Before You Begin:**
- [ ] You have a web server that can receive HTTP requests
- [ ] Your server has a public URL (not localhost)
- [ ] You can modify your server code to handle new endpoints
- [ ] You have basic knowledge of JSON and HTTP

✅ **What You'll Need:**
- Public HTTPS URL endpoint (we'll show you how to create one)
- Way to receive POST requests (we provide code examples)
- 5 minutes to set up and test

</Accordion>

## 🔧 **Prerequisites & Setup**

<Accordion title="1. HTTP/HTTPS Endpoint URL" icon="fa-link">

### **What is an Endpoint?**
An endpoint is a specific URL on your server that receives webhook notifications. Think of it as your mailbox address where Beacon delivers alerts.

### **Requirements:**
* **Must be HTTPS** (secure connection required)
* **Publicly accessible** (not behind firewall/localhost)
* **Responds quickly** (within 5 seconds)

### **URL Format:**
```
https://your-domain.com/webhook-endpoint
```

### **Examples:**
```
✅ Good: https://api.yourcompany.com/webhooks/beacon-alerts
✅ Good: https://yourapp.herokuapp.com/notifications/receive
❌ Bad:  http://localhost:3000/webhook (not public)
❌ Bad:  http://yoursite.com/webhook (not HTTPS)
```

### **Quick Setup Options:**

**Option A: Using Your Existing Server**
```javascript
// Node.js/Express example
app.post('/webhook/beacon-alerts', (req, res) => {
    console.log('Alert received:', req.body);
    res.status(200).send('OK');
});
```

**Option B: Using Cloud Functions (Beginner-Friendly)**
```python
# Google Cloud Function example
def beacon_webhook(request):
    alert_data = request.get_json()
    print(f"Alert received: {alert_data}")
    return 'OK', 200
```

</Accordion>

<Accordion title="2. Filter Conditions (Optional)" icon="fa-filter">

### **What are Filters?**
Filters let you choose which types of alerts you want to receive. Without filters, you get ALL alerts.

### **Filter Options:**
* **By Entity Type**: Only get alerts for specific merchants, products, etc.
* **By Alert Type**: Only receive certain types of problems (success rate, timeouts, etc.)

### **Example Use Cases:**
```
📊 E-commerce Store: "Only alert me about my top 5 merchants"
🏦 Payment Processor: "Only send critical alerts (score > 60)"
📱 Mobile App: "Only alert about API endpoint failures"
```

### **How to Set Filters:**
Contact your Beacon administrator with your requirements:
- Which merchants/entities you care about
- What alert severity levels you want
- Which metrics are most important to you

</Accordion>

<Accordion title="3. Network Access Requirements" icon="fa-network-wired">

### **Firewall Configuration**
Your endpoint must be reachable from the internet. If you're behind a corporate firewall:

**Steps to Check:**
1. Test your endpoint with an online tool like [webhook.site](https://webhook.site)
2. Ask your IT team to whitelist Beacon's IP ranges (contact support for IPs)
3. Ensure port 443 (HTTPS) is open for incoming connections

### **Performance Requirements:**
* **Response Time**: Your server must respond within **5 seconds**
* **Availability**: Aim for **99%+ uptime** to avoid missing alerts
* **Concurrent Handling**: Be ready to handle multiple alerts simultaneously

### **Testing Your Setup:**
```bash
# Test if your endpoint is publicly accessible
curl -X POST https://yourdomain.com/webhook-endpoint \
  -H "Content-Type: application/json" \
  -d '{"test": "connection"}'
```

</Accordion>

<Accordion title="4. Endpoint Response Requirements" icon="fa-check-circle">

### **What Your Endpoint Must Do:**

**✅ Success Response:**
```http
HTTP/1.1 200 OK
Content-Type: text/plain

OK
```

**❌ Failure Response (triggers retries):**
```http
HTTP/1.1 500 Internal Server Error
HTTP/1.1 404 Not Found
HTTP/1.1 403 Forbidden
```

### **Code Examples:**

**Python (Flask):**
```python
from flask import Flask, request, jsonify

@app.route('/webhook/beacon', methods=['POST'])
def handle_beacon_alert():
    try:
        alert_data = request.json
        # Process your alert here
        process_alert(alert_data)
        return 'OK', 200
    except Exception as e:
        print(f"Error: {e}")
        return 'Error', 500
```

**Node.js (Express):**
```javascript
app.post('/webhook/beacon', (req, res) => {
    try {
        const alertData = req.body;
        // Process your alert here
        processAlert(alertData);
        res.status(200).send('OK');
    } catch (error) {
        console.error(error);
        res.status(500).send('Error');
    }
});
```

**PHP:**
```php
<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $alertData = json_decode(file_get_contents('php://input'), true);
    
    try {
        // Process your alert here
        processAlert($alertData);
        http_response_code(200);
        echo 'OK';
    } catch (Exception $e) {
        http_response_code(500);
        echo 'Error';
    }
}
?>
```

</Accordion>

## 📨 **Understanding the Alert Data**

<Accordion title="Request Headers Explained" icon="fa-file-code">

When Beacon sends an alert, it includes these HTTP headers:

```http
POST /webhook-endpoint HTTP/1.1  
Host: yourdomain.com  
Content-Type: application/json  
User-Agent: axios/[version]  
Content-Length: [auto-calculated]  
Accept: application/json, text/plain, */*  
```

**What Each Header Means:**
- `Content-Type: application/json` → The data is in JSON format
- `User-Agent: axios/[version]` → Identifies Beacon as the sender
- `Content-Length` → Size of the alert data being sent

</Accordion>

<Accordion title="Alert Payload Structure" icon="fa-database">

### **Sample Alert (with explanations):**

```json
{
  "alert_id": "e58a1a37-496e-4d49-b9bd-88b3029c97ac",
  "alert_group_id": "7595875a-3557-4e90-a61a-b0406e987b3f", 
  "notification_triggered_at": "2025-05-03T10:14:23+05:30",
  "notification_type": "detection",
  "product": "PayuBizTransactionEngine",
  "metric": "success_rate",
  "entity_identifier": "flipkart",
  "entity_type": "merchant", 
  "started_at": "2025-05-03T05:17:00+05:30",
  "current_state": "ongoing",
  "criticality_score": 45,
  "stats": {
    "failed_count": 1000,
    "success_rate_during_downtime": 33.75,
    "reference_srt": 51.63,
    "duration": 262
  }
}
```

### **Field Explanations (Beginner-Friendly):**

| **Key** | **Description** | **Example Use** |
|---------|-----------------|-----------------|
| `alert_id` | Unique ID for this specific alert | Use for logging/tracking |
| `notification_type` | What kind of alert this is | "detection" = problem found |
| `entity_identifier` | Which merchant/system has the issue | "flipkart" = Focus on this merchant |
| `criticality_score` | How serious the problem is (0-100) | 45 = Medium priority |
| `current_state` | Is the problem ongoing or resolved? | "ongoing" = Still happening |
| `failed_count` | How many transactions failed | 1000 = A lot of failures! |
| `success_rate_during_downtime` | Current success rate | 33.75% = Very low! |
| `duration` | How long the problem has lasted | 262 minutes = Over 4 hours |

### **Alert Severity Levels:**
- 🟢 **0-30**: LOW (minor issues)
- 🟡 **31-60**: MEDIUM (needs attention) 
- 🔴 **61-100**: HIGH (critical issues)

</Accordion>

<Accordion title="Retry Configuration Explained" icon="fa-redo">

### **What Happens if Your Endpoint Fails?**

Beacon automatically retries failed webhook deliveries using this configuration:

```javascript
axiosRetry(axios, {
  retries: 3,                    // Try 3 times total
  shouldResetTimeout: true,      // Reset timeout for each retry
  retryCondition: () => true     // Retry on any error
});
```

### **Retry Schedule:**
1. **First attempt**: Immediate
2. **Retry 1**: After 1 minute
3. **Retry 2**: After 5 minutes  
4. **Retry 3**: After 15 minutes
5. **Give up**: Alert marked as failed

### **Best Practices:**
- Make your endpoint **idempotent** (safe to call multiple times)
- **Log all received alerts** to avoid processing duplicates
- **Handle retries gracefully** in your application

```python
# Example: Handle duplicate alerts
processed_alerts = set()

def handle_alert(alert_data):
    alert_id = alert_data['alert_id']
    
    if alert_id in processed_alerts:
        print(f"Alert {alert_id} already processed, skipping")
        return 'OK', 200
    
    # Process the alert
    process_new_alert(alert_data)
    processed_alerts.add(alert_id)
    return 'OK', 200
```

</Accordion>

## 🧪 **Testing Your Implementation**

<Accordion title="Test Your Webhook Endpoint" icon="fa-vial">

### **Step 1: Basic Connectivity Test**
```bash
# Test if your endpoint responds
curl -X POST https://yourdomain.com/webhook/beacon \
  -H "Content-Type: application/json" \
  -d '{"test": "ping"}'

# Expected response: HTTP 200 OK
```

### **Step 2: Simulate Real Alert**
```bash
# Send a sample alert payload
curl -X POST https://yourdomain.com/webhook/beacon \
  -H "Content-Type: application/json" \
  -d '{
    "alert_id": "test-123",
    "notification_type": "detection", 
    "criticality_score": 45,
    "entity_identifier": "test-merchant"
  }'
```

### **Step 3: Verify Processing**
Check your application logs to ensure:
- ✅ Alert was received
- ✅ Data was parsed correctly  
- ✅ Your processing logic ran
- ✅ Response was sent quickly (< 5 seconds)

### **Common Testing Tools:**
- [Webhook.site](https://webhook.site) - Test endpoint URLs
- [Postman](https://postman.com) - Send test requests
- [ngrok](https://ngrok.com) - Expose localhost for testing

</Accordion>

## ❓ **Troubleshooting & FAQ**

<Accordion title="Common Issues & Solutions" icon="fa-tools">

### **❌ "Webhook delivery failed"**

**Possible Causes:**
- Your endpoint returned non-200 status code
- Request timed out (> 5 seconds)
- Network connectivity issues

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
- URL not publicly accessible
- Firewall blocking requests
- Wrong URL format

**Solutions:**
1. Test with online tools: `curl -I https://yourdomain.com/webhook`
2. Check firewall settings
3. Verify HTTPS certificate is valid

### **❌ "Receiving duplicate alerts"**

**Possible Causes:**
- Your endpoint returned error on first attempt
- Network issues caused retries

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

<Accordion title="Frequently Asked Questions" icon="fa-question">

### **Q: How often will I receive alerts?**
A: It depends on your system's health. During normal operations, you might receive 0-5 alerts per day. During issues, you could receive multiple alerts per hour.

### **Q: Can I test webhooks before going live?**
A: Yes! Contact your Beacon administrator to set up a test environment with sample alerts.

### **Q: What if my server is down when an alert is sent?**
A: Beacon will retry 3 times over 21 minutes. If all retries fail, you'll need to check Beacon's dashboard for missed alerts.

### **Q: Can I receive alerts via email instead?**
A: Webhooks are for real-time integration. For email alerts, check Beacon's notification settings in the dashboard.

### **Q: How do I handle alerts during maintenance windows?**
A: Implement a maintenance mode that still responds with 200 OK but queues alerts for later processing.

```python
MAINTENANCE_MODE = False

def handle_alert(alert_data):
    if MAINTENANCE_MODE:
        # Queue for later processing
        alert_queue.append(alert_data)
        return 'Queued', 200
    else:
        # Process normally
        return process_alert(alert_data)
```

</Accordion>

## 🚀 **Next Steps**

<Accordion title="After Setup" icon="fa-forward">

### **1. Monitor Your Integration**
- Set up logging for all webhook calls
- Monitor response times and error rates
- Create alerts if webhook processing fails

### **2. Build Alert Processing Logic**
```python
def process_alert(alert_data):
    criticality = alert_data['criticality_score']
    
    if criticality >= 61:      # HIGH
        send_sms_alert(alert_data)
        call_on_call_engineer()
    elif criticality >= 31:   # MEDIUM  
        send_slack_notification(alert_data)
    else:                     # LOW
        log_for_review(alert_data)
```

### **3. Create Dashboards**
- Visualize alert trends over time
- Track response times to alerts
- Monitor which entities generate most alerts

### **4. Set Up Team Workflows**
- Define who responds to different alert types
- Create runbooks for common issues
- Set up escalation procedures

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

## 📖 **Glossary**

<Accordion title="Technical Terms Explained" icon="fa-book">

**Webhook**: An automated HTTP POST request sent when an event occurs

**Endpoint**: A specific URL that receives webhook requests

**Payload**: The JSON data sent in the webhook request

**Idempotent**: Safe to call multiple times with the same result

**Retry Logic**: Automatic re-sending of failed webhook deliveries

**Criticality Score**: Number (0-100) indicating alert severity

**Entity**: The business object being monitored (merchant, product, etc.)

**SRT**: Success Rate - percentage of successful transactions

**Downtime**: Period when success rate is below normal levels

**Anomaly**: Unusual pattern detected by Beacon's algorithms

</Accordion>
