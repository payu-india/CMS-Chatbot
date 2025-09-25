---
title: Partner Webhook
deprecated: false
hidden: true
metadata:
  robots: index
---
<br />

# PayU Merchant Status Webhooks

<div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
  <div className="p-6 border rounded-lg">
    <div className="text-2xl mb-2">🔔</div>
    <h3 className="font-semibold mb-2">Real-time Updates</h3>
    <p className="text-sm text-gray-600">Get instant notifications when merchant onboarding status changes</p>
  </div>

  <div className="p-6 border rounded-lg">
    <div className="text-2xl mb-2">🔐</div>
    <h3 className="font-semibold mb-2">HMAC Secured</h3>
    <p className="text-sm text-gray-600">Every webhook is signed with HMAC-SHA256 for verification</p>
  </div>

  <div className="p-6 border rounded-lg">
    <div className="text-2xl mb-2">⚡</div>
    <h3 className="font-semibold mb-2">Auto Retry</h3>
    <p className="text-sm text-gray-600">5 automatic retries with exponential backoff</p>
  </div>
</div>

Receive real-time notifications for document verification, bank validation, KYC approvals, and other merchant onboarding milestones.

***

## Getting Started

<Accordion title="Prerequisites & Setup" icon="🚀">
  Before integrating webhooks, you'll need:

  <div className="bg-blue-50 border-l-4 border-blue-400 p-4 my-4">
    <div className="flex">
      <div className="ml-3">
        <p className="text-sm text-blue-700">
          <strong>Important:</strong> Contact PayU support or your Key Account Manager to enable real-time merchant status service for your reseller account.
        </p>
      </div>
    </div>
  </div>

  **Required Items:**

  * ✅ PayU partner credentials with `refer_merchant` scope
  * ✅ Your reseller UUID
  * ✅ Client secret for HMAC verification
  * ✅ HTTPS endpoint that returns 200 status codes
  * ✅ Webhook service enabled by PayU support

  **Quick Check:**

  ```bash
  # Test your endpoint accessibility
  curl -X POST https://your-domain.com/payu/webhooks \
    -H "Content-Type: application/json" \
    -d '{"test": "connectivity"}'
  # Should return: 200 OK
  ```
</Accordion>

***

## Register Your Webhook

<Accordion title="API Registration" icon="📝">
  Register a single HTTPS endpoint to receive all merchant status events.

  <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
    <div className="p-4 bg-gray-50 rounded-lg">
      <h4 className="font-semibold mb-2">Test Environment</h4>
      <code className="text-sm">[https://uat-partner.payu.in](https://uat-partner.payu.in)</code>
    </div>

    <div className="p-4 bg-gray-50 rounded-lg">
      <h4 className="font-semibold mb-2">Production</h4>
      <code className="text-sm">[https://partner.payu.in](https://partner.payu.in)</code>
    </div>
  </div>

  **Endpoint:** `POST /api/v1/partners/register_webhook`

  ```bash
  curl https://partner.payu.in/api/v1/partners/register_webhook \
    -H "Authorization: Bearer your_access_token" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d webhook_url=https://your-domain.com/payu/webhooks \
    -d reseller_uuid=83fe-eb64-021844d8-9397-26535b1bf0c2
  ```

  **Parameters:**

  | Field           | Description                   |
  | --------------- | ----------------------------- |
  | `webhook_url`   | Your HTTPS endpoint URL       |
  | `reseller_uuid` | Your PayU reseller identifier |

  **Success Response:**

  ```json
  {
    "message": "Webhook Successfully Registered"
  }
  ```
</Accordion>

***

## Understanding Webhook Events

<Accordion title="Event Types & Payloads" icon="📋">
  PayU sends POST requests when merchant status changes occur during onboarding.

  **Sample Webhook Request:**

  ```json
  {
    "previous_status": "Pending",
    "current_status": "Approved",
    "change_timestamp": 1654812374,
    "mid": 123456,
    "merchant_uuid": "123-abcd-5678-gcjsa",
    "event_name": "Document status update",
    "error": "NA",
    "remarks": "NA"
  }
  ```

  **Merchant Onboarding Events:**

  <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
    <div className="p-4 border rounded-lg">
      <h4 className="font-semibold text-green-700 mb-2">🏢 Business Events</h4>

      <ul className="text-sm space-y-1">
        <li>• Document status update</li>
        <li>• Website status update</li>
        <li>• Agreement status update</li>
        <li>• Settlement status update</li>
      </ul>
    </div>

    <div className="p-4 border rounded-lg">
      <h4 className="font-semibold text-blue-700 mb-2">🏦 Financial Events</h4>

      <ul className="text-sm space-y-1">
        <li>• Bank verification status update</li>
        <li>• Nodal status update</li>
        <li>• Settlement status update</li>
      </ul>
    </div>

    <div className="p-4 border rounded-lg">
      <h4 className="font-semibold text-purple-700 mb-2">📄 KYC Document Events</h4>

      <ul className="text-sm space-y-1">
        <li>• SIGNED\_AUTHORISATION\_LETTER status update</li>
        <li>• PATNERSHIP\_PAN\_CARD status update</li>
        <li>• GOVT\_ISSUED\_CERTIFICATE status update</li>
        <li>• BANK\_PROOF status update</li>
        <li>• ADDRESS\_PROOF\_SIGNED\_AUTHORITY status update</li>
        <li>• PANCARD\_SIGNED\_AUTHORITY status update</li>
      </ul>
    </div>
  </div>

  **Status Values:**

  <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
    <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
      <h4 className="font-semibold text-green-800 mb-2">General Events</h4>

      <div className="text-sm text-green-700">
        <code>Pending</code> • <code>Success</code> • <code>Failed</code> • <code>In Progress</code>
      </div>
    </div>

    <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
      <h4 className="font-semibold text-blue-800 mb-2">KYC Documents</h4>

      <div className="text-sm text-blue-700">
        <code>Pending</code> • <code>Received</code> • <code>Approved</code> • <code>Declined</code> • <code>Reuploaded</code> • <code>Exceptionally</code>
      </div>
    </div>
  </div>
</Accordion>

***

## Implement Webhook Security

<Accordion title="HMAC Signature Verification" icon="🔐">
  Every webhook includes an HMAC signature in the `Authorization` header. **Always validate this** to ensure authenticity.

  **PayU's Signature Process:**

  1. Sort payload keys alphabetically
  2. Concatenate key-value pairs: `"key1value1key2value2..."`
  3. Generate HMAC-SHA256 using your `client_secret`
  4. Send hex digest in Authorization header

  **Example Calculation:**

  <div className="bg-gray-50 p-4 rounded-lg mb-4">
    <div className="text-sm mb-2"><strong>Payload:</strong></div>

    <pre className="text-xs overflow-x-auto">
      {`{
              "previous_status": "Pending",
              "current_status": "Success", 
              "change_timestamp": 18548123746,
              "mid": 123456,
              "merchant_uuid": "123-abcd-5678-gcjsa",
              "event_name": "Document status update",
              "error": "NA",
              "remarks": "NA"
            }`}
    </pre>
  </div>

  <div className="bg-gray-50 p-4 rounded-lg mb-4">
    <div className="text-sm mb-2"><strong>Sorted String:</strong></div>

    <code className="text-xs break-all">
      change\_timestamp18548123746current\_statusSuccesserrorNAevent\_nameDocument status updatemerchant\_uuid123-abcd-5678-gcjsamid123456previous\_statusPendingremarksNA
    </code>
  </div>

  **Implementation:**

  <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div>
      <h4 className="font-semibold mb-2">Python</h4>

      ```python
      import hmac
      import hashlib

      def verify_signature(payload, signature, client_secret):
          # Create sorted string
          items = [f"{k}{v}" for k, v in sorted(payload.items())]
          payload_string = "".join(items)
          
          # Generate expected signature
          expected = hmac.new(
              client_secret.encode('utf-8'),
              payload_string.encode('utf-8'),
              hashlib.sha256
          ).hexdigest()
          
          return hmac.compare_digest(expected, signature)
      ```
    </div>

    <div>
      <h4 className="font-semibold mb-2">Node.js</h4>

      ```javascript
      const crypto = require('crypto');

      function verifySignature(payload, signature, clientSecret) {
          // Create sorted string
          const keys = Object.keys(payload).sort();
          const payloadString = keys.map(k => `${k}${payload[k]}`).join('');
          
          // Generate expected signature
          const expected = crypto
              .createHmac('sha256', clientSecret)
              .update(payloadString)
              .digest('hex');
          
          return crypto.timingSafeEqual(
              Buffer.from(expected), 
              Buffer.from(signature)
          );
      }
      ```
    </div>
  </div>
</Accordion>

***

## Build Your Webhook Endpoint

<Accordion title="Event Processing Implementation" icon="⚙️">
  Create a robust webhook handler that processes merchant status updates.

  **Basic Webhook Handler:**

  ```python
  from flask import Flask, request
  import logging

  app = Flask(__name__)
  CLIENT_SECRET = "your_client_secret"  # Store securely

  @app.route('/payu/webhooks', methods=['POST'])
  def handle_webhook():
      try:
          payload = request.get_json()
          signature = request.headers.get('Authorization', '')
          
          # Verify signature first
          if not verify_signature(payload, signature, CLIENT_SECRET):
              logging.warning('Invalid webhook signature')
              return '', 200  # Return 200 to prevent retries
          
          # Process the merchant event
          process_merchant_event(payload)
          
          return '', 200
          
      except Exception as e:
          logging.error(f"Webhook error: {e}")
          return '', 200  # Always return 200
  ```

  **Event Routing Logic:**

  ```python
  def process_merchant_event(payload):
      event_name = payload['event_name']
      merchant_uuid = payload['merchant_uuid']
      status = payload['current_status']
      
      # Route based on event type
      if event_name == 'Bank verification status update':
          handle_bank_verification(merchant_uuid, status, payload)
      elif event_name == 'Settlement status update':
          handle_settlement_update(merchant_uuid, status, payload)
      elif any(kyc in event_name for kyc in ['SIGNED_', 'PAN', 'GOVT_', 'BANK_PROOF', 'ADDRESS_']):
          handle_kyc_document(merchant_uuid, event_name, status, payload)
      else:
          handle_general_status_update(merchant_uuid, event_name, status, payload)

  def handle_bank_verification(merchant_uuid, status, payload):
      if status == 'Approved':
          # Enable payment processing
          enable_merchant_payments(merchant_uuid)
          send_approval_notification(merchant_uuid, 'bank_verification')
      elif status == 'Declined':
          # Handle rejection
          error_details = payload.get('error', 'Unknown error')
          notify_bank_verification_failure(merchant_uuid, error_details)

  def handle_kyc_document(merchant_uuid, doc_type, status, payload):
      # Update document status in your system
      update_document_status(merchant_uuid, doc_type, status)
      
      if status == 'Approved':
          # Check if all KYC documents are now complete
          if all_kyc_documents_approved(merchant_uuid):
              complete_kyc_process(merchant_uuid)
      elif status == 'Declined':
          # Notify merchant with specific feedback
          error_reason = payload.get('error', 'Document verification failed')
          request_document_resubmission(merchant_uuid, doc_type, error_reason)
  ```

  **Idempotency Handling:**

  ```python
  # Use database or Redis in production
  processed_events = set()

  def is_duplicate_event(payload):
      event_id = f"{payload['merchant_uuid']}_{payload['change_timestamp']}_{payload['event_name']}"
      
      if event_id in processed_events:
          return True
      
      processed_events.add(event_id)
      return False

  @app.route('/payu/webhooks', methods=['POST'])
  def handle_webhook():
      payload = request.get_json()
      
      # Check for duplicates first
      if is_duplicate_event(payload):
          logging.info('Duplicate webhook ignored')
          return '', 200
      
      # Continue with processing...
  ```
</Accordion>

<Accordion title="Error Handling & Retries" icon="🔄">
  PayU implements automatic retries for failed webhook deliveries.

  **PayU Retry Policy:**

  <div className="bg-orange-50 border-l-4 border-orange-400 p-4 mb-4">
    <div className="flex items-center">
      <div className="text-orange-400 mr-2">⚠️</div>

      <div>
        <p className="text-sm"><strong>Retry Schedule:</strong> 5 attempts at 3, 9, 27, 81, 243 seconds</p>
        <p className="text-sm"><strong>Your endpoint must:</strong> Return 200 status, respond within 30 seconds, handle duplicates</p>
      </div>
    </div>
  </div>

  **Robust Error Handling:**

  ```python
  import logging
  from datetime import datetime

  @app.route('/payu/webhooks', methods=['POST'])
  def handle_webhook():
      start_time = datetime.utcnow()
      webhook_id = None
      
      try:
          payload = request.get_json()
          webhook_id = f"{payload.get('merchant_uuid')}_{payload.get('change_timestamp')}"
          
          logging.info(f"Processing webhook: {webhook_id}")
          
          # Validate payload structure
          if not all(key in payload for key in ['merchant_uuid', 'event_name', 'current_status']):
              logging.warning(f"Invalid payload structure: {webhook_id}")
              return '', 200
          
          # Verify signature
          if not verify_signature(payload, request.headers.get('Authorization'), CLIENT_SECRET):
              logging.warning(f"Invalid signature: {webhook_id}")
              return '', 200
          
          # Process webhook
          process_merchant_event(payload)
          
          # Log success
          duration = (datetime.utcnow() - start_time).total_seconds()
          logging.info(f"Webhook processed successfully: {webhook_id} ({duration:.2f}s)")
          
          return '', 200
          
      except Exception as e:
          # Log error with context but always return 200
          duration = (datetime.utcnow() - start_time).total_seconds()
          logging.error(f"Webhook processing failed: {webhook_id} - {e} ({duration:.2f}s)")
          
          # Optional: Queue for manual review or retry
          queue_failed_webhook(payload, str(e))
          
          return '', 200  # Prevent PayU retries
  ```

  **Production Monitoring:**

  ```python
  # Track webhook metrics
  webhook_stats = {
      'total_received': 0,
      'successful': 0,
      'failed': 0,
      'invalid_signatures': 0
  }

  def track_webhook_result(result_type):
      webhook_stats['total_received'] += 1
      webhook_stats[result_type] += 1
      
      # Alert on high failure rate
      failure_rate = webhook_stats['failed'] / webhook_stats['total_received']
      if failure_rate > 0.1:  # 10% threshold
          send_alert(f"High webhook failure rate: {failure_rate:.1%}")
  ```
</Accordion>

***

## Testing Your Integration

<Accordion title="Development & Testing Tools" icon="🧪">
  Test your webhook implementation before production deployment.

  **Local Development Setup:**

  ```bash
  # Use ngrok to expose local development server
  ngrok http 3000

  # Register your ngrok URL with PayU
  curl https://uat-partner.payu.in/api/v1/partners/register_webhook \
    -H "Authorization: Bearer your_test_token" \
    -d webhook_url=https://abc123.ngrok.io/payu/webhooks \
    -d reseller_uuid=your_test_uuid
  ```

  **Webhook Simulation Script:**

  ```python
  import requests
  import hmac
  import hashlib
  import time

  def simulate_payu_webhook(webhook_url, client_secret, event_type="document_approval"):
      # Sample payloads for different scenarios
      scenarios = {
          "document_approval": {
              "previous_status": "Pending",
              "current_status": "Approved",
              "event_name": "Document status update",
              "error": "NA",
              "remarks": "NA"
          },
          "bank_verification": {
              "previous_status": "Pending", 
              "current_status": "Approved",
              "event_name": "Bank verification status update",
              "error": "NA",
              "remarks": "NA"
          },
          "kyc_declined": {
              "previous_status": "Received",
              "current_status": "Declined", 
              "event_name": "SIGNED_AUTHORISATION_LETTER status update",
              "error": "Document clarity insufficient",
              "remarks": "Please resubmit with better quality"
          }
      }
      
      payload = {
          **scenarios.get(event_type, scenarios["document_approval"]),
          "change_timestamp": int(time.time()),
          "mid": 123456,
          "merchant_uuid": "test-merchant-001"
      }
      
      # Generate PayU signature
      sorted_items = [f"{k}{v}" for k, v in sorted(payload.items())]
      payload_string = "".join(sorted_items)
      signature = hmac.new(
          client_secret.encode('utf-8'),
          payload_string.encode('utf-8'),
          hashlib.sha256
      ).hexdigest()
      
      # Send webhook
      response = requests.post(
          webhook_url,
          json=payload,
          headers={'Authorization': signature}
      )
      
      print(f"Test '{event_type}': {response.status_code}")
      return response.status_code == 200

  # Run tests
  webhook_url = "https://your-domain.com/payu/webhooks"
  client_secret = "your_test_client_secret"

  print("Testing PayU webhooks...")
  simulate_payu_webhook(webhook_url, client_secret, "document_approval")
  simulate_payu_webhook(webhook_url, client_secret, "bank_verification") 
  simulate_payu_webhook(webhook_url, client_secret, "kyc_declined")
  ```

  **Validation Checklist:**

  <div className="space-y-2">
    <div className="flex items-center">
      <input type="checkbox" className="mr-2" />

      <span className="text-sm">Endpoint returns 200 for valid requests</span>
    </div>

    <div className="flex items-center">
      <input type="checkbox" className="mr-2" />

      <span className="text-sm">HMAC signature validation working</span>
    </div>

    <div className="flex items-center">
      <input type="checkbox" className="mr-2" />

      <span className="text-sm">Handles all 12+ PayU event types</span>
    </div>

    <div className="flex items-center">
      <input type="checkbox" className="mr-2" />

      <span className="text-sm">Processes duplicate events idempotently</span>
    </div>

    <div className="flex items-center">
      <input type="checkbox" className="mr-2" />

      <span className="text-sm">Returns 200 even for internal errors</span>
    </div>

    <div className="flex items-center">
      <input type="checkbox" className="mr-2" />

      <span className="text-sm">Response time under 30 seconds</span>
    </div>
  </div>
</Accordion>

***

## Production Deployment

<Accordion title="Go-Live Checklist" icon="🚀">
  Final steps before deploying your webhook integration to production.

  **Security Verification:**

  <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
    <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
      <h4 className="font-semibold text-green-800 mb-2">✅ Security Implemented</h4>

      <ul className="text-sm text-green-700 space-y-1">
        <li>• HMAC signature validation</li>
        <li>• HTTPS with valid SSL certificate</li>
        <li>• Client secret stored securely</li>
        <li>• Input validation and sanitization</li>
      </ul>
    </div>

    <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
      <h4 className="font-semibold text-blue-800 mb-2">⚡ Performance Ready</h4>

      <ul className="text-sm text-blue-700 space-y-1">
        <li>• Response time under 30 seconds</li>
        <li>• Idempotent event processing</li>
        <li>• Comprehensive error handling</li>
        <li>• Monitoring and alerting setup</li>
      </ul>
    </div>
  </div>

  **Production Registration:**

  ```bash
  # Register your production webhook URL
  curl https://partner.payu.in/api/v1/partners/register_webhook \
    -H "Authorization: Bearer your_production_token" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d webhook_url=https://your-production-domain.com/payu/webhooks \
    -d reseller_uuid=your_production_reseller_uuid
  ```

  **Post-Deployment Monitoring:**

  ```python
  # Health check endpoint for monitoring
  @app.route('/payu/webhooks/health', methods=['GET'])
  def webhook_health():
      recent_errors = get_recent_webhook_errors()  # Last 24 hours
      
      status = "healthy" if len(recent_errors) < 10 else "degraded"
      
      return {
          "status": status,
          "webhook_stats": webhook_stats,
          "recent_errors": len(recent_errors),
          "last_webhook": get_last_webhook_timestamp()
      }
  ```

  **Launch Strategy:**

  1. Deploy webhook endpoint to production
  2. Register production URL with PayU
  3. Monitor first few webhook deliveries closely
  4. Validate merchant status updates in your system
  5. Confirm alerting and monitoring are working
</Accordion>

***

## Troubleshooting

<Accordion title="Common Issues & Solutions" icon="🔧">
  Quick solutions for frequently encountered webhook problems.

  <div className="space-y-4">
    <div className="p-4 border border-red-200 bg-red-50 rounded-lg">
      <h4 className="font-semibold text-red-800 mb-2">❌ Not Receiving Webhooks</h4>

      <div className="text-sm text-red-700">
        <p><strong>Check:</strong> Webhook service enabled by PayU support</p>
        <p><strong>Verify:</strong> Endpoint returns 200 and is publicly accessible</p>
        <p><strong>Test:</strong> <code>curl -X POST [https://your-domain.com/payu/webhooks](https://your-domain.com/payu/webhooks)</code></p>
      </div>
    </div>

    <div className="p-4 border border-orange-200 bg-orange-50 rounded-lg">
      <h4 className="font-semibold text-orange-800 mb-2">⚠️ Signature Validation Fails</h4>

      <div className="text-sm text-orange-700">
        <p><strong>Verify:</strong> Using correct client\_secret from PayU dashboard</p>
        <p><strong>Check:</strong> Payload keys sorted alphabetically before concatenation</p>
        <p><strong>Ensure:</strong> Using HMAC-SHA256 algorithm exactly</p>
      </div>
    </div>

    <div className="p-4 border border-blue-200 bg-blue-50 rounded-lg">
      <h4 className="font-semibold text-blue-800 mb-2">🔄 Webhook Registration Issues</h4>

      <div className="text-sm text-blue-700">
        <p><strong>Confirm:</strong> Access token has <code>refer\_merchant</code> scope</p>
        <p><strong>Validate:</strong> Reseller UUID is correct and active</p>
        <p><strong>Check:</strong> Webhook URL is HTTPS and publicly accessible</p>
      </div>
    </div>

    <div className="p-4 border border-purple-200 bg-purple-50 rounded-lg">
      <h4 className="font-semibold text-purple-800 mb-2">⚡ Processing Errors</h4>

      <div className="text-sm text-purple-700">
        <p><strong>Always:</strong> Return 200 OK to prevent PayU retries</p>
        <p><strong>Implement:</strong> Comprehensive logging for debugging</p>
        <p><strong>Handle:</strong> Duplicate events gracefully with idempotency</p>
      </div>
    </div>
  </div>

  **Debug Script:**

  ```bash
  # Quick webhook endpoint test
  curl -X POST https://your-domain.com/payu/webhooks \
    -H "Content-Type: application/json" \
    -H "Authorization: test_signature" \
    -d '{
      "merchant_uuid": "test-123",
      "event_name": "Document status update", 
      "current_status": "Approved",
      "change_timestamp": 1654812374,
      "mid": 123456,
      "previous_status": "Pending",
      "error": "NA",
      "remarks": "NA"
    }'
  ```
</Accordion>

***

## Support & Resources

<div className="grid grid-cols-1 md:grid-cols-2 gap-6">
  <div className="p-6 border rounded-lg">
    <h3 className="font-semibold mb-4 flex items-center">
      <span className="mr-2">📞</span> Get Help
    </h3>

    <div className="space-y-2 text-sm">
      <p><strong>Enable Webhooks:</strong> Contact PayU Key Account Manager</p>
      <p><strong>Technical Support:</strong> [developer-support@payu.in](mailto:developer-support@payu.in)</p>
      <p><strong>KYC Issues:</strong> <a href="#" className="text-blue-600">KYC Errors & Solutions</a></p>
    </div>
  </div>

  <div className="p-6 border rounded-lg">
    <h3 className="font-semibold mb-4 flex items-center">
      <span className="mr-2">📚</span> Resources
    </h3>

    <div className="space-y-2 text-sm">
      <p><strong>API Docs:</strong> Complete PayU API reference</p>
      <p><strong>Status Page:</strong> PayU service status</p>
      <p><strong>Partner Dashboard:</strong> Webhook monitoring tools</p>
    </div>
  </div>
</div>

***

<div className="mt-8 p-6 bg-gradient-to-r from-blue-50 to-purple-50 border border-blue-200 rounded-lg">
  <h3 className="font-semibold mb-2 flex items-center">
    <span className="mr-2">🎉</span> Ready to Go Live?
  </h3>

  <p className="text-sm text-gray-700 mb-4">
    Your webhook integration will enable real-time merchant status updates, improving operational efficiency and customer experience.
  </p>

  <div className="flex space-x-4">
    <div className="text-xs bg-white px-3 py-1 rounded border">1. Enable Service</div>
    <div className="text-xs bg-white px-3 py-1 rounded border">2. Register Endpoint</div>
    <div className="text-xs bg-white px-3 py-1 rounded border">3. Implement Handler</div>
    <div className="text-xs bg-white px-3 py-1 rounded border">4. Deploy & Monitor</div>
  </div>
</div>
