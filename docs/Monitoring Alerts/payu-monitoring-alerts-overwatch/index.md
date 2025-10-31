---
title: Payu Overwatch
deprecated: false
hidden: false
metadata:
  robots: index
---
PayU Overwatch is a real-time monitoring and anomaly detection platform designed for ensuring smooth payment operations across the PayU transactional ecosystem. Its main features include observing transactional metrics and early issue detection.

## Core Objectives

The platform has four clearly defined goals:

1. **Proactive Detection:** Quickly identify anomalies in transaction performance within minutes.
2. **Intelligent Correlation:** Provide root-cause insights by linking anomalies across merchants, banks, and payment modes.
3. **Automated Communication:** Send structured alerts via **webhooks**, **Teams**, or **Email**.
4. **Continuous Learning:** Adapt dynamically to historical data and trends by learning over time.

## How It Works

This section breaks down the operational workflow of PayU Overwatch into **four steps**:

1. **Data Collection:** Ingest live transactional and performance data from PayU's ecosystem.
2. **Anomaly Detection:** Use machine learning and rule-based logic to detect deviations in metrics such as success rates or error rates.
3. **Alert Generation:** Generate alerts with context (e.g., affected entities, duration, severity) upon detecting anomalies.
4. **Notification Delivery:** Send alerts via **webhook callbacks** to configured destinations for automated responses.

## Benefits

* **Early Visibility:** Detect and mitigate potential issues before merchants notice them.
* **Operational Efficiency:** Reduce manual workload and improve mean time to detect (MTTD).
* **Automated Response:** Facilitate incident management workflows.
* **Enhanced Transparency:** Equip stakeholders with clear, data-backed information about system health.

## Key Monitoring Capabilities

### 1. Transaction Success Rate Monitoring

* Continuously tracks success rate metrics across merchants and banks.
* Detects deviations and performance degradation.
* Triggers alerts for irregularities based on historical trends.

### 2. Failure Pattern Detection

* Identifies sudden spikes in failure rates across merchants, acquirers, and product modes.
* Helps trace the root causes of failure (e.g., gateway downtimes or configuration problems).

### 3. Real-Time Anomaly Detection

* Uses statistical and behavioral models to detect unusual patterns.
* Captures issues before merchants escalate them.
* Contextualizes alerts with **stats** like `srt_drop_abs` and `srt_drop_rel`.

### 4. Multi-Entity Monitoring

Allows alerting at multiple levels:

* Merchant level
* Acquirer/Bank level
* Card Scheme level
* Product level

Supports selective alert subscriptions for specific entities.

### 5. Severity Classification

All alerts are rated with a **criticality score (0–100)**:

* **0–30:** Low Severity
* **31–60:** Medium Severity
* **61–100:** High Severity

Enables prioritization of investigations.

### 6. Continuous Health Tracking

* Tracks alert duration.
* Resolves alerts if performance normalcy is restored automatically.
* Enables performance benchmarking with correlations to other system metrics.

## Alert Delivery Methods

The platform supports three methods for delivering alerts:

* **Email**
* **Teams**
* **Webhook**

### 📨 Webhook Alerts

For additional details about webhook alerts implementation and configurations, refer to:
[Webhook Alerts Documentation](https://docs.payu.in/docs/webhook-alerts/)

## Use Cases & Scenarios

### 1. Merchant Performance Degradation

**Scenario:** A merchant's transaction success rate decreases compared to historical data.  
**Webhook Trigger:** Metric: `"success_rate"` and a criticality score ranging between low, medium, and high.

### 2. Early Warning for Zero Success Rate

**Scenario:** All merchant transactions fail, leading to a zero success rate.  
**Webhook Trigger:** Metric: `stats.zero_srt: true` and `criticality_score ≥ 60`.

### 3. SLA Compliance & Reporting

**Scenario:** Teams require data on uptime and anomaly durations across merchants/products.  
**Webhook Trigger:** Notifications for anomaly start and end times (`started_at`, `ended_at`) are utilized.

### 4. Intelligent Alert Routing

**Scenario:** Dedicated teams manage specific merchants or product lines.  
**Webhook Trigger:** Payload includes `entity_type` and `product` information for routing alerts.

## Support & Resources

For further assistance, contact: **[overwatch.support@payu.in](mailto:overwatch.support@payu.in)**.