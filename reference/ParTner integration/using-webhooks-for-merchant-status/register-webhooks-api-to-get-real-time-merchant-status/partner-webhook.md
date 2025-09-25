---
title: Partner Webhook
deprecated: false
hidden: true
metadata:
  robots: index
---
<br />

# PayU Webhook Integration Guide

## Overview

Webhooks allow you to receive real-time notifications about merchant onboarding status changes. Partners can refer multiple merchants, and each merchant goes through their own onboarding journey with PayU. Instead of polling our API, PayU will send secure HTTP POST requests to your specified endpoint whenever a merchant's status updates during the onboarding process.

**What you'll accomplish:**
- Set up secure webhook endpoints for real-time merchant status updates
- Implement HMAC signature validation for security
- Handle all 12+ merchant onboarding event types
- Build production-ready error handling and retry logic

---

## Step 1: Prerequisites & Setup

Follow the below steps to prepare for webhook integration:

<Accordion title="Step 1.1: Gather required credentials and access" icon="fa-key">
  Before starting webhook integration, ensure you have all necessary credentials and access permissions.

  <HTMLBlock>{`
    <div>
      <table>
        <thead>
          <tr>
            <th style="width: 15%;">Requirement</th>
            <th style="width: 70%; white-space: normal; word-break: break-word;">Description & How to Obtain</th>
            <th style="width: 15%;">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              PayU Partner Account<br>
              <code class="inline-block rounded-full bg-red-100 px-2 py-0.5 text-xs font-semibold text-red-800 ring-1 ring-inset ring-red-200">mandatory</code>
            </td>
            <td style="white-space: normal; word-break: break-word;">
              Valid PayU partner credentials with active account status. Contact PayU sales team if you don't have an account.
            </td>
            <td>☐ Ready</td>
          </tr>
          <tr>
            <td>
              Access Token<br>
              <code class="inline-block rounded-full bg-red-100 px-2 py-0.5 text-xs font-semibold text-red-800 ring-1 ring-inset ring-red-200">mandatory</code>
            </td>
            <td style="white-space: normal; word-break: break-word;">
              OAuth access token with <code>refer_merchant</code> scope. Obtain via <a href="#get-token-api">Get Token API</a>.
            </td>
            <td>☐ Ready</td>
          </tr>
          <tr>
            <td>
              Client Secret<br>
              <code class="inline-block rounded-full bg-red-100 px-2 py-0.5 text-xs font-semibold text-red-800 ring-1 ring-inset ring-red-200">mandatory</code>
            </td>
            <td style="white-space: normal; word-break: break-word;">
              Your partner application's client secret for HMAC signature validation. Available in your PayU partner dashboard.
            </td>
            <td>☐ Ready</td>
          </tr>
          <tr>
            <td>
              Reseller UUID<br>
              <code class="inline-block rounded-full bg-red-100 px-2 py-0.5 text-xs font-semibold text-red-800 ring-1 ring-inset ring-red-200">mandatory</code>
            </td>
            <td style="white-space: normal; word-break: break-word;">
              Your unique reseller identifier provided during PayU onboarding.
            </td>
            <td>☐ Ready</td>
          </tr>
          <tr>
            <td>
              HTTPS Endpoint<br>
              <code class="inline-block rounded-full bg-red-100 px-2 py-0.5 text-xs font-semibold text-red-800 ring-1 ring-inset ring-red-200">mandatory</code>
            </td>
            <td style="white-space: normal; word-break: break-word;">
              Publicly accessible HTTPS URL that can receive POST requests and return 200 status codes.
            </td>
            <td>☐ Ready</td>
          </tr>
        </tbody>
      </table>
    </div>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Step 1.2: Understand webhook event types" icon="fa-list">
  PayU sends webhooks for various merchant onboarding events. Understanding these helps you plan your integration architecture.

  <HTMLBlock>{`
    <div>
      <table>
        <thead>
          <tr>
            <th style="width: 35%;">Event Name</th>
            <th style="width: 45%; white-space: normal; word-break: break-word;">Description</th>
            <th style="width: 20%;">Business Impact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Document status update</td>
            <td style="white-space: normal; word-break: break-word;">General document verification status changes during merchant onboarding</td>
            <td>Medium</td>
          </tr>
          <tr>
            <td>Website status update</td>
            <td style="white-space: normal; word-break: break-word;">Merchant website verification and compliance check results</td>
            <td>Medium</td>
          </tr>
          <tr>
            <td>Bank verification status update</td>
            <td style="white-space: normal; word-break: break-word;">Bank account verification and validation status changes</td>
            <td>High</td>
          </tr>
          <tr>
            <td>Settlement status update</td>
            <td style="white-space: normal; word-break: break-word;">Payment settlement configuration and approval status</td>
            <td>High</td>
          </tr>
          <tr>
            <td>Agreement status update</td>
            <td style="white-space: normal; word-break: break-word;">Legal agreement signing and approval status</td>
            <td>High</td>
          </tr>
          <tr>
            <td>SIGNED_AUTHORISATION_LETTER status update</td>
            <td style="white-space: normal; word-break: break-word;">Authorization letter verification status</td>
            <td>Medium</td>
          </tr>
          <tr>
            <td>PATNERSHIP_PAN_CARD status update</td>
            <td style="white-space: normal; word-break: break-word;">Partnership PAN card document verification</td>
            <td>Medium</td>
          </tr>
          <tr>
            <td>GOVT_ISSUED_CERTIFICATE status update</td>
            <td style="white-space: normal; word-break: break-word;">Government certificate verification status</td>
            <td>Medium</td>
          </tr>
          <tr>
            <td>BANK_PROOF status update</td>
            <td style="white-space: normal; word-break: break-word;">Bank proof document verification</td>
            <td>Medium</td>
          </tr>
          <tr>
            <td>ADDRESS_PROOF_SIGNED_AUTHORITY status update</td>
            <td style="white-space: normal; word-break: break-word;">Address proof with signed authority verification</td>
            <td>Medium</td>
          </tr>
          <tr>
            <td>PANCARD_SIGNED_AUTHORITY status update</td>
            <td style="white-space: normal; word-break: break-word;">PAN card with signed authority verification</td>
            <td>Medium</td>
          </tr>
        </tbody>
      </table>
    </div>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Step 1.3: Choose your webhook architecture" icon="fa-sitemap">
  Decide whether to use single or multiple webhook endpoints based on your business needs.

  **Option A: Single Endpoint (Recommended for most cases)**
  ```bash
  # Single URL receives all events, route internally
  https://your-domain.com/webhooks/payu
  ```

  **Option B: Multiple Endpoints (Enterprise/Team-based)**
  ```bash
  # Different endpoints for different event categories
  https://your-domain.com/webhooks/payu/onboarding     # Document, Website, Agreement
  https://your-domain.com/webhooks/payu/financial      # Settlement, Bank verification
  https://your-domain.com/webhooks/payu/compliance     # KYC documents
  ```

  **Business Considerations:**
  - **Single Endpoint:** Simpler management, unified monitoring, easier deployment
  - **Multiple Endpoints:** Team separation, different SLAs, microservice architecture
</Accordion>

---

## Step 2: Enable Webhook Service

<Accordion title="Step 2.1: Contact PayU to enable webhook service" icon="fa-phone">
  Before you can register webhooks, PayU must enable the real-time merchant status service for your partner account.

  **Required Actions:**
  1. **Contact your Key Account Manager** or PayU Support
  2. **Request activation** of real-time merchant status service
  3. **Provide your reseller UUID** for service enablement
  4. **Wait for confirmation** that the service is active

  **What to expect:**
  - Service activation typically takes 1-2 business days
  - You'll receive confirmation via email when enabled
  - Test environment and production require separate enablement

  > **Important:** You cannot proceed to webhook registration until this service is enabled for your account.
</Accordion>

---

## Step 3: Register Your Webhook

<Accordion title="Step 3.1: Prepare webhook registration request" icon="fa-cog">
  Set up the API request to register your webhook URL with PayU.

  **API Endpoints:**

  <HTMLBlock>{`
    <div>
      <table>
        <thead>
          <tr>
            <th style="width: 20%;">Environment</th>
            <th style="width: 80%; white-space: normal; word-break: break-word;">URL</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Test</td>
            <td style="white-space: normal; word-break: break-word;">
              <code>https://uat-partner.payu.in/api/v1/partners/register_webhook</code>
            </td>
          </tr>
          <tr>
            <td>Production</td>
            <td style="white-space: normal; word-break: break-word;">
              <code>https://partner.payu.in/api/v1/partners/register_webhook</code>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  `}</HTMLBlock>

  **Request Headers:**

  <HTMLBlock>{`
    <div>
      <table>
        <thead>
          <tr>
            <th style="width: 25%;">Header</th>
            <th style="width: 75%; white-space: normal; word-break: break-word;">Value</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Authorization</td>
            <td style="white-space: normal; word-break: break-word;">
              <code>Bearer {{access_token}}</code>
            </td>
          </tr>
          <tr>
            <td>Content-Type</td>
            <td style="white-space: normal; word-break: break-word;">
              <code>application/x-www-form-urlencoded</code>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Step 3.2: Configure request parameters" icon="fa-list-check">
  Prepare the required parameters for webhook registration.

  <HTMLBlock>{`
    <div>
      <table>
        <thead>
          <tr>
            <th style="width: 20%;">Parameter</th>
            <th style="width: 60%; white-space: normal; word-break: break-word;">Type & Description</th>
            <th style="width: 20%;">Example</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              webhook_url<br>
              <code class="inline-block rounded-full bg-red-100 px-2 py-0.5 text-xs font-semibold text-red-800 ring-1 ring-inset ring-red-200">mandatory</code>
            </td>
            <td style="white-space: normal; word-break: break-word;">
              <code>String</code> Your HTTPS endpoint URL that will receive webhook notifications. Must be publicly accessible and return 200 status codes.
            </td>
            <td>https://your-domain.com/webhooks/payu</td>
          </tr>
          <tr>
            <td>
              reseller_uuid<br>
              <code class="inline-block rounded-full bg-red-100 px-2 py-0.5 text-xs font-semibold text-red-800 ring-1 ring-inset ring-red-200">mandatory</code>
            </td>
            <td style="white-space: normal; word-break: break-word;">
              <code>String</code> Your unique reseller identifier provided by PayU during partner onboarding.
            </td>
            <td>83fe-eb64-021844d8-9397-26535b1bf0c2</td>
          </tr>
        </tbody>
      </table>
    </div>
  `}</HTMLBlock>
</Accordion>

<Accordion title="Step 3.3: Execute webhook registration" icon="fa-rocket">
  Send the registration request to PayU API.

  **cURL Example:**
  ```bash
  curl -X POST 'https://uat-partner.payu.in/api/v1/partners/register_webhook' \
    -H 'Authorization: Bearer 169e576ee0794085e48f0de683bc39563c43c9493f23867e1c53481bdaa9cada' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'webhook_url=https://your-domain.com/webhooks/payu' \
    -d 'reseller_uuid=83fe-eb64-021844d8-9397-26535b1bf0c2'
  ```

  **Python Example:**
  ```python
  import requests

  url = "https://uat-partner.payu.in/api/v1/partners/register_webhook"
  headers = {
      "Authorization": "Bearer YOUR_ACCESS_TOKEN",
      "Content-Type": "application/x-www-form-urlencoded"
  }
  data = {
      "webhook_url": "https://your-domain.com/webhooks/payu",
      "reseller_uuid": "YOUR_RESELLER_UUID"
  }

  response = requests.post(url, headers=headers, data=data)
  print(f"Status: {response.status_code}")
  print(f"Response: {response.json()}")
  ```

  **Expected Success Response:**
  ```json
  {
      "message": "Webhook Successfully Registered"
  }
  ```

  **Common Error Responses:**
  ```json
  // 401 Unauthorized
  {
      "error": "Invalid or expired access token"
  }

  // 400 Bad Request
  {
      "error": "Invalid webhook_url format"
  }

  // 403 Forbidden
  {
      "error": "Webhook service not enabled for this reseller"
  }
  ```
</Accordion>

---

## Step 4: Implement Webhook Endpoint

<Accordion title="Step 4.1: Understand webhook request format" icon="fa-info">
  Learn the structure of incoming webhook requests from PayU.

  **Webhook Request Details:**

  <HTMLBlock>{`
    <div>
      <table>
        <thead>
          <tr>
            <th style="width: 20%;">Component</th>
            <th style="width: 80%; white-space: normal; word-break: break-word;">Details</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>HTTP Method</td>
            <td style="white-space: normal; word-break: break-word;">POST</td>
          </tr>
          <tr>
            <td>Content-Type</td>
            <td style="white-space: normal; word-break: break-word;"><code>application/json</code></td>
          </tr>
          <tr>
            <td>Authorization Header</td>
            <td style="white-space: normal; word-break: break-word;">Contains HMAC signature for verification</td>
          </tr>
          <tr>
            <td>Request Body</td>
            <td style="white-space: normal; word-break: break-word;">JSON payload with merchant status information</td>
          </tr>
          <tr>
            <td>Expected Response</td>
            <td style="white-space: normal; word-break: break-word;">HTTP 200 with empty body</td>
          </tr>
        </tbody>
      </table>
    </div>
  `}</HTMLBlock>

  **Sample Webhook Payload:**
  ```json
  {
      "previous_status": "Pending",
      "current_status": "Success", 
      "change_timestamp": 1654812374,
      "mid": 123456,
      "merchant_uuid": "123-abcd-5678-gcjsa",
      "event_name": "Document status update",
      "error": "NA",
      "remarks": "NA"
  }
  ```
</Accordion>

<Accordion title="Step 4.2: Implement basic webhook endpoint" icon="fa-code">
  Create a basic webhook endpoint that can receive and acknowledge PayU requests.

  **Python/Flask Implementation:**
  ```python
  from flask import Flask, request, jsonify
  import logging

  app = Flask(__name__)
  logging.basicConfig(level=logging.INFO)

  @app.route('/webhooks/payu', methods=['POST'])
  def handle_webhook():
      try:
          # Log incoming request
          logging.info("Received webhook from PayU")
          
          # Get headers and payload
          auth_header = request.headers.get('Authorization', '')
          payload = request.get_json()
          
          # Basic payload validation
          if not payload:
              logging.warning("Received empty payload")
              return '', 200  # Still return 200 to prevent retries
          
          # Log key information
          merchant_uuid = payload.get('merchant_uuid')
          event_name = payload.get('event_name')
          current_status = payload.get('current_status')
          
          logging.info(f"Webhook received: {merchant_uuid} - {event_name} - {current_status}")
          
          # TODO: Add signature validation (Step 5)
          # TODO: Add business logic processing
          
          # Return 200 OK (required)
          return '', 200
          
      except Exception as e:
          logging.error(f"Webhook processing error: {e}")
          return '', 200  # Always return 200 to prevent retries

  if __name__ == '__main__':
      app.run(debug=True, port=3000)
  ```

  **Node.js/Express Implementation:**
  ```javascript
  const express = require('express');
  const app = express();

  app.use(express.json());

  app.post('/webhooks/payu', (req, res) => {
      try {
          console.log('Received webhook from PayU');
          
          const authHeader = req.headers.authorization || '';
          const payload = req.body;
          
          if (!payload) {
              console.warn('Received empty payload');
              return res.status(200).send('');
          }
          
          const merchantUuid = payload.merchant_uuid;
          const eventName = payload.event_name;
          const currentStatus = payload.current_status;
          
          console.log(`Webhook: ${merchantUuid} - ${eventName} - ${currentStatus}`);
          
          // TODO: Add signature validation (Step 5)
          // TODO: Add business logic processing
          
          res.status(200).send('');
          
      } catch (error) {
          console.error('Webhook processing error:', error);
          res.status(200).send(''); // Always return 200
      }
  });

  app.listen(3000, () => {
      console.log('Webhook server running on port 3000');
  });
  ```
</Accordion>

<Accordion title="Step 4.3: Define payload field structure" icon="fa-database">
  Understand each field in the webhook payload for proper processing.

  <HTMLBlock>{`
    <div>
      <table>
        <thead>
          <tr>
            <th style="width: 20%;">Field</th>
            <th style="width: 15%;">Type</th>
            <th style="width: 50%; white-space: normal; word-break: break-word;">Description</th>
            <th style="width: 15%;">Example</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>previous_status</td>
            <td>String</td>
            <td style="white-space: normal; word-break: break-word;">The merchant's previous status before this change</td>
            <td>Pending</td>
          </tr>
          <tr>
            <td>current_status</td>
            <td>String</td>
            <td style="white-space: normal; word-break: break-word;">The merchant's new status after this change</td>
            <td>Approved</td>
          </tr>
          <tr>
            <td>change_timestamp</td>
            <td>Integer</td>
            <td style="white-space: normal; word-break: break-word;">Unix timestamp when the status change occurred</td>
            <td>1654812374</td>
          </tr>
          <tr>
            <td>mid</td>
            <td>Integer</td>
            <td style="white-space: normal; word-break: break-word;">PayU merchant ID</td>
            <td>123456</td>
          </tr>
          <tr>
            <td>merchant_uuid</td>
            <td>String</td>
            <td style="white-space: normal; word-break: break-word;">Unique merchant identifier</td>
            <td>123-abcd-5678-gcjsa</td>
          </tr>
          <tr>
            <td>event_name</td>
            <td>String</td>
            <td style="white-space: normal; word-break: break-word;">Type of onboarding event that triggered the webhook</td>
            <td>Document status update</td>
          </tr>
          <tr>
            <td>error</td>
            <td>String</td>
            <td style="white-space: normal; word-break: break-word;">Error details if status change failed, otherwise "NA"</td>
            <td>NA</td>
          </tr>
          <tr>
            <td>remarks</td>
            <td>String</td>
            <td style="white-space: normal; word-break: break-word;">Additional remarks or comments, otherwise "NA"</td>
            <td>NA</td>
          </tr>
        </tbody>
      </table>
    </div>
  `}</HTMLBlock>
</Accordion>

---

## Step 5: Implement Signature Validation

<Accordion title="Step 5.1: Understand HMAC signature validation" icon="fa-shield">
  Learn how PayU generates and validates webhook signatures for security.

  **Security Overview:**
  - Every webhook includes an HMAC signature in the Authorization header
  - Signature is generated using SHA-256 algorithm
  - Uses your client_secret as the signing key
  - Payload is sorted alphabetically before signing

  **HMAC Generation Formula:**
  ```
  HMAC = OpenSSL::HMAC.hexdigest("SHA256", client_secret, sorted_payload_string)
  ```

  **Signature Generation Process:**
  1. Take webhook payload JSON object
  2. Sort all keys alphabetically
  3. Concatenate key-value pairs (no separators)
  4. Generate HMAC-SHA256 using client_secret
  5. Send hex digest in Authorization header
</Accordion>

<Accordion title="Step 5.2: Implement signature validation logic" icon="fa-lock">
  Add HMAC signature validation to your webhook endpoint for security.

  **Python Implementation:**
  ```python
  import hmac
  import hashlib
  import json
  from flask import Flask, request

  CLIENT_SECRET = "your_client_secret_here"  # Store securely

  def validate_webhook_signature(payload_dict, received_signature):
      """Validate webhook HMAC signature"""
      
      # Sort payload keys and create concatenated string
      sorted_items = []
      for key in sorted(payload_dict.keys()):
          sorted_items.append(f"{key}{payload_dict[key]}")
      
      payload_string = "".join(sorted_items)
      
      # Generate expected HMAC signature
      expected_signature = hmac.new(
          CLIENT_SECRET.encode('utf-8'),
          payload_string.encode('utf-8'),
          hashlib.sha256
      ).hexdigest()
      
      # Secure comparison
      return hmac.compare_digest(expected_signature, received_signature)

  @app.route('/webhooks/payu', methods=['POST'])
  def handle_webhook():
      try:
          # Get signature from Authorization header
          auth_header = request.headers.get('Authorization', '')
          
          # Parse JSON payload
          payload = request.get_json()
          
          # Validate signature
          if not validate_webhook_signature(payload, auth_header):
              logging.warning("Invalid webhook signature")
              return '', 401  # Or return 200 to prevent retries
          
          # Process the webhook (signature is valid)
          process_merchant_update(payload)
          
          return '', 200
          
      except Exception as e:
          logging.error(f"Webhook processing error: {e}")
          return '', 200
  ```

  **Node.js Implementation:**
  ```javascript
  const crypto = require('crypto');
  const CLIENT_SECRET = 'your_client_secret_here';

  function validateWebhookSignature(payload, receivedSignature) {
      // Sort payload keys and create concatenated string
      const sortedKeys = Object.keys(payload).sort();
      const payloadString = sortedKeys.map(key => `${key}${payload[key]}`).join('');
      
      // Generate expected HMAC signature
      const expectedSignature = crypto
          .createHmac('sha256', CLIENT_SECRET)
          .update(payloadString)
          .digest('hex');
      
      // Secure comparison
      return crypto.timingSafeEqual(
          Buffer.from(expectedSignature, 'hex'),
          Buffer.from(receivedSignature, 'hex')
      );
  }

  app.post('/webhooks/payu', (req, res) => {
      try {
          const authHeader = req.headers.authorization || '';
          const payload = req.body;
          
          // Validate signature
          if (!validateWebhookSignature(payload, authHeader)) {
              console.warn('Invalid webhook signature');
              return res.status(401).json({ error: 'Invalid signature' });
          }
          
          // Process the webhook
          processMerchantUpdate(payload);
          
          res.status(200).send('');
          
      } catch (error) {
          console.error('Webhook processing error:', error);
          res.status(200).send('');
      }
  });
  ```
</Accordion>

<Accordion title="Step 5.3: Test signature validation" icon="fa-test-tube">
  Verify your signature validation implementation with a known example.

  **Test Example:**
  
  **Given Payload:**
  ```json
  { 
      "previous_status": "Pending", 
      "current_status": "Success", 
      "change_timestamp": 18548123746,
      "mid": 123456,
      "merchant_uuid": "123-abcd-5678-gcjsa",
      "event_name": "Document status update",
      "error": "NA",
      "remarks": "NA" 
  }
  ```

  **Sorted String (for HMAC):**
  ```
  change_timestamp18548123746current_statusSuccesserrorNAevent_nameDocument status updatemerchant_uuid123-abcd-5678-gcjsamid123456previous_statusPendingremarksNA
  ```

  **Expected HMAC (with test client_secret):**
  ```
  d59e5be387204e8c37bc8f46306f5013197b2f9d082ec859da1b09f9bc703036
  ```

  **Test Script:**
  ```python
  def test_signature_validation():
      test_payload = {
          "previous_status": "Pending",
          "current_status": "Success", 
          "change_timestamp": 18548123746,
          "mid": 123456,
          "merchant_uuid": "123-abcd-5678-gcjsa",
          "event_name": "Document status update",
          "error": "NA",
          "remarks": "NA"
      }
      
      expected_signature = "d59e5be387204e8c37bc8f46306f5013197b2f9d082ec859da1b09f9bc703036"
      
      # Use your validation function
      is_valid = validate_webhook_signature(test_payload, expected_signature)
      print(f"Signature validation test: {'PASSED' if is_valid else 'FAILED'}")
      
      return is_valid

  # Run the test
  test_signature_validation()
  ```
</Accordion>

---

## Step 6: Handle Webhook Events

<Accordion title="Step 6.1: Implement event routing and processing" icon="fa-route">
  Build business logic to handle different types of merchant onboarding events.

  **Event Router Implementation:**
  ```python
  from enum import Enum
  from typing import Dict, Callable
  import logging

  class PayUEventType(Enum):
      DOCUMENT = "Document status update"
      WEBSITE = "Website status update"
      BANK_VERIFICATION = "Bank verification status update"
      SETTLEMENT = "Settlement status update"
      AGREEMENT = "Agreement status update"
      NODAL = "Nodal status update"
      
      # KYC Document events
      SIGNED_AUTH_LETTER = "SIGNED_AUTHORISATION_LETTER status update"
      PARTNERSHIP_PAN = "PATNERSHIP_PAN_CARD status update"
      GOVT_CERTIFICATE = "GOVT_ISSUED_CERTIFICATE status update"
      BANK_PROOF = "BANK_PROOF status update"
      ADDRESS_PROOF = "ADDRESS_PROOF_SIGNED_AUTHORITY status update"
      PANCARD_AUTHORITY = "PANCARD_SIGNED_AUTHORITY status update"

  class WebhookEventHandler:
      def __init__(self):
          self.handlers: Dict[PayUEventType, Callable] = {
              PayUEventType.DOCUMENT: self.handle_document_update,
              PayUEventType.WEBSITE: self.handle_website_update,
              PayUEventType.BANK_VERIFICATION: self.handle_bank_verification,
              PayUEventType.SETTLEMENT: self.handle_settlement_update,
              PayUEventType.AGREEMENT: self.handle_agreement_update,
          }
          
          # KYC document handlers
          self.kyc_handlers = [
              PayUEventType.SIGNED_AUTH_LETTER,
              PayUEventType.PARTNERSHIP_PAN,
              PayUEventType.GOVT_CERTIFICATE,
              PayUEventType.BANK_PROOF,
              PayUEventType.ADDRESS_PROOF,
              PayUEventType.PANCARD_AUTHORITY,
          ]
      
      def process_webhook(self, payload: dict) -> None:
          """Main webhook processing logic"""
          event_name = payload.get('event_name')
          merchant_uuid = payload.get('merchant_uuid')
          
          logging.info(f"Processing webhook: {event_name} for merchant {merchant_uuid}")
          
          # Find and execute handler
          handler = self.find_handler(event_name)
          if handler:
              handler(payload)
          else:
              self.handle_unknown_event(payload)
      
      def find_handler(self, event_name: str) -> Callable:
          """Find appropriate handler for event type"""
          
          # Check direct event mappings
          for event_type, handler in self.handlers.items():
              if event_type.value == event_name:
                  return handler
          
          # Check KYC document events
          for kyc_event in self.kyc_handlers:
              if kyc_event.value == event_name:
                  return self.handle_kyc_document_update
          
          return None
      
      def handle_document_update(self, payload: dict) -> None:
          """Handle general document status updates"""
          merchant_uuid = payload['merchant_uuid']
          current_status = payload['current_status']
          
          logging.info(f"Document update: {merchant_uuid} -> {current_status}")
          
          # Your business logic here
          # - Update merchant record in database
          # - Send notifications to merchant
          # - Trigger next onboarding step
          
      def handle_bank_verification(self, payload: dict) -> None:
          """Handle bank verification status updates"""
          merchant_uuid = payload['merchant_uuid']
          current_status = payload['current_status']
          
          logging.info(f"Bank verification: {merchant_uuid} -> {current_status}")
          
          if current_status == "Approved":
              # Enable payment processing
              self.enable_payment_processing(merchant_uuid)
          elif current_status == "Declined":
              # Notify merchant of issues
              self.notify_bank_verification_failure(merchant_uuid, payload.get('error'))
      
      def handle_settlement_update(self, payload: dict) -> None:
          """Handle settlement configuration updates"""
          merchant_uuid = payload['merchant_uuid']
          current_status = payload['current_status']
          
          logging.info(f"Settlement update: {merchant_uuid} -> {current_status}")
          
          if current_status == "Approved":
              # Configure settlement parameters
              self.setup_settlement_config(merchant_uuid)
      
      def handle_kyc_document_update(self, payload: dict) -> None:
          """Handle KYC document verification updates"""
          merchant_uuid = payload['merchant_uuid']
          event_name = payload['event_name']
          current_status = payload['current_status']
          
          logging.info(f"KYC document update: {event_name} -> {current_status}")
          
          # Extract document type from event name
          doc_type = event_name.replace(' status update', '')
          
          if current_status == "Declined":
              # Handle document rejection
              self.handle_document_rejection(merchant_uuid, doc_type, payload.get('error'))
          elif current_status == "Approved":
              # Check if all KYC documents are approved
              self.check_kyc_completion(merchant_uuid)
      
      def handle_unknown_event(self, payload: dict) -> None:
          """Handle unknown or new event types"""
          event_name = payload.get('event_name')
          logging.warning(f"Unknown event type: {event_name}")
          
          # Store for analysis and contact PayU support
          self.store_unknown_event(payload)
      
      # Helper methods (implement based on your business logic)
      def enable_payment_processing(self, merchant_uuid: str) -> None:
          # Implementation specific to your system
          pass
      
      def notify_bank_verification_failure(self, merchant_uuid: str, error: str) -> None:
          # Send notification to merchant
          pass
      
      def setup_settlement_config(self, merchant_uuid: str) -> None:
          # Configure settlement parameters
          pass
      
      def handle_document_rejection(self, merchant_uuid: str, doc_type: str, error: str) -> None:
          # Handle document rejection workflow
          pass
      
      def check_kyc_completion(self, merchant_uuid: str) -> None:
          # Check if all required KYC documents are approved
          pass
      
      def store_unknown_event(self, payload: dict) -> None:
          # Store unknown events for analysis
          pass

  # Usage in webhook endpoint
  webhook_handler = WebhookEventHandler()

  @app.route('/webhooks/payu', methods=['POST'])
  def handle_webhook():
      try:
          auth_header = request.headers.get('Authorization', '')
          payload = request.get_json()
          
          # Validate signature
          if not validate_webhook_signature(payload, auth_header):
              return '', 401
          
          # Process the webhook
          webhook_handler.process_webhook(payload)
          
          return '', 200
          
      except Exception as e:
          logging.error(f"Webhook processing error: {e}")
          return '', 200
  ```
</Accordion>

<Accordion title="Step 6.2: Handle KYC document status values" icon="fa-file-check">
  Understand and handle different status values for KYC document events.

  **KYC Document Status Values:**

  <HTMLBlock>{`
    <div>
      <table>
        <thead>
          <tr>
            <th style="width: 20%;">Status</th>
            <th style="width: 50%; white-space: normal; word-break: break-word;">Description</th>
            <th style="width: 30%;">Recommended Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Pending</td>
            <td style="white-space: normal; word-break: break-word;">Document submitted and awaiting review</td>
            <td>No action required, inform merchant</td>
          </tr>
          <tr>
            <td>Received</td>
            <td style="white-space: normal; word-break: break-word;">Document received and queued for verification</td>
            <td>Update status, notify merchant</td>
          </tr>
          <tr>
            <td>Approved</td>
            <td style="white-space: normal; word-break: break-word;">Document verified and approved</td>
            <td>Enable next onboarding step</td>
          </tr>
          <tr>
            <td>Declined</td>
            <td style="white-space: normal; word-break: break-word;">Document rejected due to issues</td>
            <td>Notify merchant, request resubmission</td>
          </tr>
          <tr>
            <td>Reuploaded</td>
            <td style="white-space: normal; word-break: break-word;">Document has been resubmitted after rejection</td>
            <td>Update status, reset review process</td>
          </tr>
          <tr>
            <td>Exceptionally</td>
            <td style="white-space: normal; word-break: break-word;">Special case requiring manual review</td>
            <td>Flag for manual intervention</td>
          </tr>
        </tbody>
      </table>
    </div>
  `}</HTMLBlock>

  **Status Processing Logic:**
  ```python
  def process_kyc_status_change(self, payload: dict) -> None:
      """Process KYC document status changes"""
      status = payload['current_status']
      merchant_uuid = payload['merchant_uuid']
      doc_type = payload['event_name']
      error = payload.get('error', 'NA')
      remarks = payload.get('remarks', 'NA')
      
      if status == "Approved":
          self.handle_document_approval(merchant_uuid, doc_type)
          
      elif status == "Declined":
          self.handle_document_decline(merchant_uuid, doc_type, error, remarks)
          
      elif status == "Reuploaded":
          self.handle_document_reupload(merchant_uuid, doc_type)
          
      elif status == "Exceptionally":
          self.handle_exceptional_case(merchant_uuid, doc_type, remarks)
          
      elif status in ["Pending", "Received"]:
          self.update_document_status(merchant_uuid, doc_type, status)
      
      # Always update merchant record
      self.update_merchant_document_status(merchant_uuid, doc_type, status)
  
  def handle_document_approval(self, merchant_uuid: str, doc_type: str) -> None:
      """Handle approved document"""
      # Update internal status
      # Check if all required documents are approved
      # Progress to next onboarding stage if complete
      # Send approval notification
      pass
  
  def handle_document_decline(self, merchant_uuid: str, doc_type: str, error: str, remarks: str) -> None:
      """Handle declined document"""
      # Log decline reason
      # Send notification to merchant with specific feedback
      # Provide guidance for resubmission
      # Update merchant dashboard with requirements
      pass
  ```
</Accordion>

<Accordion title="Step 6.3: Implement error handling and retry logic" icon="fa-exclamation-triangle">
  Add robust error handling and implement PayU's retry policy understanding.

  **PayU Retry Policy:**
  - **Retry attempts:** 5 times maximum
  - **Retry intervals:** 3, 9, 27, 81, 243 seconds (exponential backoff)
  - **Failure criteria:** Non-200 responses, timeouts, connection errors
  - **Timeout:** 30 seconds per request

  **Robust Error Handling:**
  ```python
  import logging
  from datetime import datetime
  from typing import Set

  # Track processed events (use database in production)
  processed_events: Set[str] = set()

  @app.route('/webhooks/payu', methods=['POST'])
  def handle_webhook():
      start_time = datetime.utcnow()
      webhook_id = None
      
      try:
          # Parse request
          auth_header = request.headers.get('Authorization', '')
          payload = request.get_json()
          
          if not payload:
              logging.warning("Received empty webhook payload")
              return '', 200  # Return 200 to prevent retries
          
          # Create unique webhook ID for deduplication
          webhook_id = f"{payload.get('merchant_uuid')}_{payload.get('change_timestamp')}_{payload.get('event_name')}"
          
          logging.info(f"Processing webhook: {webhook_id}")
          
          # Check for duplicate processing (idempotency)
          if webhook_id in processed_events:
              logging.info(f"Duplicate webhook ignored: {webhook_id}")
              return '', 200
          
          # Validate signature
          if not validate_webhook_signature(payload, auth_header):
              logging.warning(f"Invalid signature for webhook: {webhook_id}")
              # Decide: return 401 to see retry, or 200 to accept but not process
              return '', 200  # Recommended: accept but don't process
          
          # Process the webhook
          webhook_handler.process_webhook(payload)
          
          # Mark as processed
          processed_events.add(webhook_id)
          
          # Log success
          processing_time = (datetime.utcnow() - start_time).total_seconds()
          logging.info(f"Webhook processed successfully: {webhook_id} in {processing_time:.2f}s")
          
          return '', 200
          
      except Exception as e:
          # Log error with context
          processing_time = (datetime.utcnow() - start_time).total_seconds()
          logging.error(f"Webhook processing error for {webhook_id}: {e}", extra={
              'webhook_id': webhook_id,
              'processing_time': processing_time,
              'payload': payload if 'payload' in locals() else None,
              'error_type': type(e).__name__
          })
          
          # Always return 200 to prevent PayU retries
          # Handle the error through internal alerting/retry mechanisms
          return '', 200

  # Production-ready processing with internal error handling
  def process_webhook_safe(self, payload: dict) -> None:
      """Process webhook with comprehensive error handling"""
      try:
          self.process_webhook(payload)
          
      except DatabaseConnectionError as e:
          # Database issues - might want to retry internally
          logging.error(f"Database connection error: {e}")
          self.queue_for_retry(payload)
          
      except ValidationError as e:
          # Data validation error - probably won't succeed on retry
          logging.error(f"Payload validation error: {e}")
          self.store_invalid_payload(payload)
          
      except ExternalAPIError as e:
          # External API failure - might succeed later
          logging.error(f"External API error: {e}")
          self.queue_for_retry(payload)
          
      except Exception as e:
          # Unknown error - log and investigate
          logging.error(f"Unknown error processing webhook: {e}")
          self.store_failed_webhook(payload, str(e))
  ```

  **Monitoring and Alerting:**
  ```python
  import time
  from collections import defaultdict

  # Webhook metrics tracking
  webhook_metrics = {
      'total_received': 0,
      'successful_processed': 0,
      'failed_processing': 0,
      'invalid_signatures': 0,
      'duplicate_events': 0,
      'processing_times': []
  }

  def track_webhook_metrics(webhook_id: str, status: str, processing_time: float):
      """Track webhook processing metrics"""
      webhook_metrics['total_received'] += 1
      webhook_metrics['processing_times'].append(processing_time)
      
      if status == 'success':
          webhook_metrics['successful_processed'] += 1
      elif status == 'failed':
          webhook_metrics['failed_processing'] += 1
      elif status == 'invalid_signature':
          webhook_metrics['invalid_signatures'] += 1
      elif status == 'duplicate':
          webhook_metrics['duplicate_events'] += 1
      
      # Alert on high failure rate
      failure_rate = webhook_metrics['failed_processing'] / webhook_metrics['total_received']
      if failure_rate > 0.1:  # 10% failure rate threshold
          send_alert(f"High webhook failure rate: {failure_rate:.2%}")

  def send_alert(message: str):
      """Send alert to monitoring system"""
      # Implement your alerting mechanism
      # - Email notifications
      # - Slack alerts  
      # - PagerDuty incidents
      # - Monitoring dashboard updates
      pass
  ```
</Accordion>

---

## Step 7: Testing Your Integration

<Accordion title="Step 7.1: Set up test environment" icon="fa-flask">
  Configure your testing environment for webhook development and validation.

  **Local Development Setup:**
  ```bash
  # Install ngrok for local testing
  npm install -g ngrok
  # or
  brew install ngrok

  # Expose your local server
  ngrok http 3000

  # Example output:
  # Forwarding https://abc123.ngrok.io -> http://localhost:3000
  ```

  **Test Environment Registration:**
  ```bash
  # Register webhook in PayU test environment
  curl -X POST 'https://uat-partner.payu.in/api/v1/partners/register_webhook' \
    -H 'Authorization: Bearer YOUR_TEST_TOKEN' \
    -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'webhook_url=https://abc123.ngrok.io/webhooks/payu' \
    -d 'reseller_uuid=YOUR_TEST_RESELLER_UUID'
  ```

  **Environment Variables Setup:**
  ```bash
  # .env file for testing
  PAYU_CLIENT_SECRET=your_test_client_secret
  PAYU_ACCESS_TOKEN=your_test_access_token
  PAYU_RESELLER_UUID=your_test_reseller_uuid
  PAYU_WEBHOOK_URL=https://abc123.ngrok.io/webhooks/payu
  ENVIRONMENT=test
  ```
</Accordion>

<Accordion title="Step 7.2: Create webhook simulation scripts" icon="fa-robot">
  Build scripts to simulate PayU webhook deliveries for testing your implementation.

  **Webhook Simulation Script:**
  ```python
  import requests
  import hmac
  import hashlib
  import json
  import time
  from typing import Dict, Any

  class PayUWebhookSimulator:
      def __init__(self, webhook_url: str, client_secret: str):
          self.webhook_url = webhook_url
          self.client_secret = client_secret
      
      def generate_signature(self, payload: Dict[str, Any]) -> str:
          """Generate HMAC signature for payload"""
          # Sort payload keys and create concatenated string
          sorted_items = []
          for key in sorted(payload.keys()):
              sorted_items.append(f"{key}{payload[key]}")
          
          payload_string = "".join(sorted_items)
          
          # Generate HMAC signature
          signature = hmac.new(
              self.client_secret.encode('utf-8'),
              payload_string.encode('utf-8'),
              hashlib.sha256
          ).hexdigest()
          
          return signature
      
      def send_webhook(self, payload: Dict[str, Any]) -> bool:
          """Send simulated webhook to your endpoint"""
          try:
              signature = self.generate_signature(payload)
              
              response = requests.post(
                  self.webhook_url,
                  json=payload,
                  headers={
                      'Authorization': signature,
                      'Content-Type': 'application/json'
                  },
                  timeout=30
              )
              
              print(f"Response Status: {response.status_code}")
              print(f"Response Body: {response.text}")
              
              return response.status_code == 200
              
          except Exception as e:
              print(f"Error sending webhook: {e}")
              return False
      
      def test_document_approval(self) -> bool:
          """Test document approval webhook"""
          payload = {
              "previous_status": "Pending",
              "current_status": "Approved",
              "change_timestamp": int(time.time()),
              "mid": 123456,
              "merchant_uuid": "test-merchant-001",
              "event_name": "Document status update",
              "error": "NA",
              "remarks": "NA"
          }
          
          print("Testing document approval webhook...")
          return self.send_webhook(payload)
      
      def test_document_decline(self) -> bool:
          """Test document decline webhook"""
          payload = {
              "previous_status": "Pending", 
              "current_status": "Declined",
              "change_timestamp": int(time.time()),
              "mid": 123456,
              "merchant_uuid": "test-merchant-001",
              "event_name": "Document status update",
              "error": "Document quality insufficient",
              "remarks": "Please resubmit with higher resolution"
          }
          
          print("Testing document decline webhook...")
          return self.send_webhook(payload)
      
      def test_bank_verification(self) -> bool:
          """Test bank verification webhook"""
          payload = {
              "previous_status": "Pending",
              "current_status": "Approved", 
              "change_timestamp": int(time.time()),
              "mid": 123456,
              "merchant_uuid": "test-merchant-001",
              "event_name": "Bank verification status update",
              "error": "NA",
              "remarks": "NA"
          }
          
          print("Testing bank verification webhook...")
          return self.send_webhook(payload)
      
      def test_kyc_document(self) -> bool:
          """Test KYC document webhook"""
          payload = {
              "previous_status": "Received",
              "current_status": "Approved",
              "change_timestamp": int(time.time()),
              "mid": 123456,
              "merchant_uuid": "test-merchant-001", 
              "event_name": "SIGNED_AUTHORISATION_LETTER status update",
              "error": "NA",
              "remarks": "NA"
          }
          
          print("Testing KYC document webhook...")
          return self.send_webhook(payload)
      
      def test_invalid_signature(self) -> bool:
          """Test webhook with invalid signature"""
          payload = {
              "previous_status": "Pending",
              "current_status": "Approved",
              "change_timestamp": int(time.time()),
              "mid": 123456,
              "merchant_uuid": "test-merchant-001",
              "event_name": "Document status update",
              "error": "NA",
              "remarks": "NA"
          }
          
          print("Testing invalid signature webhook...")
          
          # Send with invalid signature
          response = requests.post(
              self.webhook_url,
              json=payload,
              headers={
                  'Authorization': 'invalid_signature_here',
                  'Content-Type': 'application/json'
              }
          )
          
          print(f"Response Status: {response.status_code}")
          # Should handle gracefully (return 200 or 401)
          return response.status_code in [200, 401]
      
      def run_all_tests(self) -> bool:
          """Run comprehensive test suite"""
          tests = [
              ("Document Approval", self.test_document_approval),
              ("Document Decline", self.test_document_decline), 
              ("Bank Verification", self.test_bank_verification),
              ("KYC Document", self.test_kyc_document),
              ("Invalid Signature", self.test_invalid_signature),
          ]
          
          results = []
          print("Running PayU Webhook Test Suite...")
          print("=" * 50)
          
          for test_name, test_func in tests:
              try:
                  result = test_func()
                  results.append(result)
                  status = "✅ PASSED" if result else "❌ FAILED"
                  print(f"{test_name}: {status}")
              except Exception as e:
                  results.append(False)
                  print(f"{test_name}: ❌ ERROR - {e}")
              
              print("-" * 30)
              time.sleep(1)  # Brief pause between tests
          
          passed = sum(results)
          total = len(results)
          print(f"\nTest Results: {passed}/{total} tests passed")
          
          return passed == total

  # Usage example
  if __name__ == "__main__":
      simulator = PayUWebhookSimulator(
          webhook_url="https://your-domain.com/webhooks/payu",
          client_secret="your_test_client_secret"
      )
      
      success = simulator.run_all_tests()
      print(f"\nOverall test result: {'SUCCESS' if success else 'FAILURE'}")
  ```
</Accordion>

<Accordion title="Step 7.3: Validate webhook endpoint requirements" icon="fa-check-circle">
  Verify your webhook endpoint meets all PayU requirements before production deployment.

  **Endpoint Validation Checklist:**

  <HTMLBlock>{`
    <div>
      <table>
        <thead>
          <tr>
            <th style="width: 10%;">✓</th>
            <th style="width: 40%; white-space: normal; word-break: break-word;">Requirement</th>
            <th style="width: 50%; white-space: normal; word-break: break-word;">Test Method</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>☐</td>
            <td>Returns HTTP 200 for valid requests</td>
            <td><code>curl -X POST https://your-domain.com/webhooks/payu -d '{"test":"data"}'</code></td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Responds within 30 seconds</td>
            <td>Monitor response times during testing</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Uses HTTPS with valid SSL certificate</td>
            <td><code>curl -I https://your-domain.com/webhooks/payu</code></td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Validates HMAC signatures correctly</td>
            <td>Use webhook simulator with known signatures</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Handles duplicate events idempotently</td>
            <td>Send same webhook payload multiple times</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Processes all event types</td>
            <td>Test each of the 12+ event types</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Handles malformed payloads gracefully</td>
            <td>Send invalid JSON, missing fields</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Returns 200 even for processing errors</td>
            <td>Simulate internal errors, verify response</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Logs webhook events appropriately</td>
            <td>Check logs for proper event tracking</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Implements proper security measures</td>
            <td>Test signature validation, input sanitization</td>
          </tr>
        </tbody>
      </table>
    </div>
  `}</HTMLBlock>

  **Automated Validation Script:**
  ```bash
  #!/bin/bash
  # webhook-validation.sh

  WEBHOOK_URL="https://your-domain.com/webhooks/payu"
  
  echo "PayU Webhook Endpoint Validation"
  echo "================================"
  
  # Test 1: Basic connectivity
  echo "1. Testing basic connectivity..."
  response=$(curl -s -o /dev/null -w "%{http_code}" -X POST $WEBHOOK_URL)
  if [ $response -eq 200 ]; then
      echo "   ✅ Endpoint responds with 200"
  else
      echo "   ❌ Endpoint returned: $response"
  fi
  
  # Test 2: HTTPS certificate
  echo "2. Testing HTTPS certificate..."
  cert_status=$(curl -s -I $WEBHOOK_URL | head -n 1 | grep "200")
  if [ ! -z "$cert_status" ]; then
      echo "   ✅ HTTPS working correctly"
  else
      echo "   ❌ HTTPS issues detected"
  fi
  
  # Test 3: Response time
  echo "3. Testing response time..."
  response_time=$(curl -o /dev/null -s -w "%{time_total}" -X POST $WEBHOOK_URL)
  if (( $(echo "$response_time < 5.0" | bc -l) )); then
      echo "   ✅ Response time: ${response_time}s (good)"
  else
      echo "   ⚠️  Response time: ${response_time}s (slow)"
  fi
  
  # Test 4: Content-Type handling
  echo "4. Testing JSON content handling..."
  response=$(curl -s -o /dev/null -w "%{http_code}" -X POST \
      -H "Content-Type: application/json" \
      -d '{"test": "data"}' \
      $WEBHOOK_URL)
  if [ $response -eq 200 ]; then
      echo "   ✅ JSON content handled correctly"
  else
      echo "   ❌ JSON handling failed: $response"
  fi
  
  echo "Validation complete!"
  ```
</Accordion>

---

## Step 8: Production Deployment

<Accordion title="Step 8.1: Security and compliance checklist" icon="fa-shield-alt">
  Ensure your webhook implementation meets security and compliance requirements for production.

  **Security Checklist:**

  <HTMLBlock>{`
    <div>
      <table>
        <thead>
          <tr>
            <th style="width: 10%;">✓</th>
            <th style="width: 40%; white-space: normal; word-break: break-word;">Security Requirement</th>
            <th style="width: 50%; white-space: normal; word-break: break-word;">Implementation Details</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>☐</td>
            <td>HMAC signature validation implemented</td>
            <td>Always validate webhook signatures before processing</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>HTTPS with valid SSL certificate</td>
            <td>Use TLS 1.2+ with certificate from trusted CA</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Client secret stored securely</td>
            <td>Use environment variables or secure key management</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Input validation and sanitization</td>
            <td>Validate all payload fields, sanitize before database storage</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Rate limiting implemented</td>
            <td>Protect against webhook flooding attacks</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>IP allowlisting (optional)</td>
            <td>Restrict webhook access to PayU IP ranges</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Audit logging enabled</td>
            <td>Log all webhook events for compliance and debugging</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Error handling without data leakage</td>
            <td>Don't expose internal errors in webhook responses</td>
          </tr>
        </tbody>
      </table>
    </div>
  `}</HTMLBlock>

  **Production Security Configuration:**
  ```python
  import os
  from flask import Flask
  from flask_limiter import Limiter
  from flask_limiter.util import get_remote_address

  app = Flask(__name__)

  # Rate limiting
  limiter = Limiter(
      app,
      key_func=get_remote_address,
      default_limits=["100 per hour"]
  )

  # Secure configuration
  CLIENT_SECRET = os.environ.get('PAYU_CLIENT_SECRET')
  if not CLIENT_SECRET:
      raise ValueError("PAYU_CLIENT_SECRET environment variable required")

  # PayU IP allowlist (get current ranges from PayU support)
  PAYU_IP_RANGES = [
      # Add PayU webhook IP ranges here
      "203.0.113.0/24",  # Example range
  ]

  def validate_source_ip(request):
      """Validate request comes from PayU IP ranges"""
      client_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
      
      # In production, implement proper IP range checking
      # For now, log the IP for analysis
      logging.info(f"Webhook received from IP: {client_ip}")
      return True  # Implement proper validation

  @app.route('/webhooks/payu', methods=['POST'])
  @limiter.limit("10 per minute")  # Webhook-specific rate limit
  def handle_webhook():
      # Validate source IP
      if not validate_source_ip(request):
          logging.warning(f"Webhook from unauthorized IP: {request.remote_addr}")
          return '', 403
      
      # Your webhook processing logic here
      return process_webhook_securely()
  ```
</Accordion>

<Accordion title="Step 8.2: Monitoring and alerting setup" icon="fa-chart-line">
  Implement comprehensive monitoring for your webhook integration in production.

  **Monitoring Components:**
  ```python
  import time
  import logging
  from datetime import datetime, timedelta
  from collections import defaultdict
  
  class WebhookMonitor:
      def __init__(self):
          self.metrics = {
              'total_received': 0,
              'successful_processed': 0,
              'failed_processing': 0,
              'invalid_signatures': 0,
              'duplicate_events': 0,
              'processing_times': [],
              'events_by_type': defaultdict(int),
              'events_by_status': defaultdict(int)
          }
          self.alert_thresholds = {
              'failure_rate': 0.05,  # 5% failure rate threshold
              'avg_processing_time': 5.0,  # 5 second average threshold
              'invalid_signature_rate': 0.02  # 2% invalid signature threshold
          }
      
      def record_webhook_event(self, event_type: str, status: str, processing_time: float):
          """Record webhook processing metrics"""
          self.metrics['total_received'] += 1
          self.metrics['events_by_type'][event_type] += 1
          self.metrics['events_by_status'][status] += 1
          self.metrics['processing_times'].append(processing_time)
          
          if status == 'success':
              self.metrics['successful_processed'] += 1
          elif status == 'failed':
              self.metrics['failed_processing'] += 1
          elif status == 'invalid_signature':
              self.metrics['invalid_signatures'] += 1
          elif status == 'duplicate':
              self.metrics['duplicate_events'] += 1
          
          self.check_alert_conditions()
      
      def check_alert_conditions(self):
          """Check if any alert conditions are met"""
          total = self.metrics['total_received']
          if total < 10:  # Need minimum sample size
              return
          
          # Check failure rate
          failure_rate = self.metrics['failed_processing'] / total
          if failure_rate > self.alert_thresholds['failure_rate']:
              self.send_alert(f"High failure rate: {failure_rate:.2%}")
          
          # Check invalid signature rate
          invalid_rate = self.metrics['invalid_signatures'] / total
          if invalid_rate > self.alert_thresholds['invalid_signature_rate']:
              self.send_alert(f"High invalid signature rate: {invalid_rate:.2%}")
          
          # Check average processing time
          if self.metrics['processing_times']:
              avg_time = sum(self.metrics['processing_times']) / len(self.metrics['processing_times'])
              if avg_time > self.alert_thresholds['avg_processing_time']:
                  self.send_alert(f"Slow processing time: {avg_time:.2f}s average")
      
      def send_alert(self, message: str):
          """Send alert to monitoring systems"""
          # Implement your alerting mechanism
          logging.error(f"WEBHOOK ALERT: {message}")
          
          # Examples:
          # - Send to Slack webhook
          # - Create PagerDuty incident
          # - Send email notification
          # - Update monitoring dashboard
      
      def get_health_report(self) -> dict:
          """Generate health report for monitoring dashboard"""
          total = self.metrics['total_received']
          if total == 0:
              return {'status': 'no_data'}
          
          failure_rate = self.metrics['failed_processing'] / total
          success_rate = self.metrics['successful_processed'] / total
          avg_processing_time = sum(self.metrics['processing_times']) / len(self.metrics['processing_times']) if self.metrics['processing_times'] else 0
          
          return {
              'status': 'healthy' if failure_rate < 0.05 else 'degraded',
              'total_webhooks': total,
              'success_rate': f"{success_rate:.2%}",
              'failure_rate': f"{failure_rate:.2%}",
              'avg_processing_time': f"{avg_processing_time:.2f}s",
              'events_by_type': dict(self.metrics['events_by_type']),
              'last_updated': datetime.utcnow().isoformat()
          }

  # Global monitor instance
  webhook_monitor = WebhookMonitor()

  # Enhanced webhook handler with monitoring
  @app.route('/webhooks/payu', methods=['POST'])
  def handle_webhook_with_monitoring():
      start_time = time.time()
      event_type = None
      status = 'unknown'
      
      try:
          payload = request.get_json()
          event_type = payload.get('event_name', 'unknown')
          
          # Validate signature
          if not validate_webhook_signature(payload, request.headers.get('Authorization', '')):
              status = 'invalid_signature'
              return '', 200
          
          # Process webhook
          webhook_handler.process_webhook(payload)
          status = 'success'
          
          return '', 200
          
      except Exception as e:
          status = 'failed'
          logging.error(f"Webhook processing error: {e}")
          return '', 200
          
      finally:
          # Record metrics
          processing_time = time.time() - start_time
          webhook_monitor.record_webhook_event(event_type or 'unknown', status, processing_time)

  # Health check endpoint for monitoring
  @app.route('/webhooks/health', methods=['GET'])
  def webhook_health():
      """Health check endpoint for monitoring systems"""
      health_report = webhook_monitor.get_health_report()
      status_code = 200 if health_report.get('status') == 'healthy' else 503
      return jsonify(health_report), status_code
  ```

  **Monitoring Dashboard Metrics:**
  - Webhook volume (requests per minute/hour)
  - Success/failure rates
  - Processing time percentiles (p50, p95, p99)
  - Event type distribution
  - Invalid signature attempts
  - Error patterns and trends
</Accordion>

<Accordion title="Step 8.3: Production deployment checklist" icon="fa-rocket">
  Final checklist before deploying your webhook integration to production.

  **Pre-Deployment Checklist:**

  <HTMLBlock>{`
    <div>
      <table>
        <thead>
          <tr>
            <th style="width: 10%;">✓</th>
            <th style="width: 40%; white-space: normal; word-break: break-word;">Deployment Task</th>
            <th style="width: 50%; white-space: normal; word-break: break-word;">Verification Method</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>☐</td>
            <td>End-to-end testing in UAT environment</td>
            <td>Complete merchant onboarding flow with webhook notifications</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Load testing completed</td>
            <td>Test with expected webhook volume (10x normal load)</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Security validation passed</td>
            <td>Penetration testing, signature validation, HTTPS verification</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Monitoring and alerting configured</td>
            <td>Dashboards created, alert rules tested, escalation paths defined</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Error handling validated</td>
            <td>Test failure scenarios, verify graceful degradation</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Database scaling configured</td>
            <td>Ensure database can handle webhook processing load</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Backup and recovery procedures</td>
            <td>Document rollback procedures, test data recovery</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Documentation updated</td>
            <td>API docs, runbooks, troubleshooting guides</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Team training completed</td>
            <td>Support team trained on webhook operations and troubleshooting</td>
          </tr>
          <tr>
            <td>☐</td>
            <td>Production webhook registration</td>
            <td>Register production URL with PayU, verify service is enabled</td>
          </tr>
        </tbody>
      </table>
    </div>
  `}</HTMLBlock>

  **Production Deployment Steps:**

  1. **Deploy to production environment**
     ```bash
     # Deploy your webhook service
     docker build -t payu-webhook-service .
     docker push your-registry/payu-webhook-service:latest
     kubectl apply -f webhook-deployment.yaml
     ```

  2. **Register production webhook URL**
     ```bash
     curl -X POST 'https://partner.payu.in/api/v1/partners/register_webhook' \
       -H 'Authorization: Bearer YOUR_PRODUCTION_TOKEN' \
       -H 'Content-Type: application/x-www-form-urlencoded' \
       -d 'webhook_url=https://your-production-domain.com/webhooks/payu' \
       -d 'reseller_uuid=YOUR_PRODUCTION_RESELLER_UUID'
     ```

  3. **Monitor initial deployment**
     ```bash
     # Watch webhook logs
     kubectl logs -f deployment/payu-webhook-service
     
     # Monitor health endpoint
     watch curl -s https://your-domain.com/webhooks/health | jq
     ```

  4. **Validate production webhooks**
     - Create test merchant in production
     - Monitor webhook delivery for test merchant events
     - Verify all processing steps work correctly
     - Confirm monitoring and alerting are functional

  **Post-Deployment Monitoring:**
  - Monitor webhook delivery success rates
  - Track processing times and performance
  - Watch for any error patterns or issues
  - Validate business processes are working correctly
  - Ensure team is receiving monitoring alerts
</Accordion>

---

## Troubleshooting & Support

<Accordion title="Common issues and solutions" icon="fa-tools">
  Solutions for frequently encountered webhook integration problems.

  **Problem: Webhook registration fails**
  - ✅ Verify access token has `refer_merchant` scope
  - ✅ Check webhook URL is HTTPS and publicly accessible
  - ✅ Confirm reseller UUID is correct
  - ✅ Ensure webhook service is enabled with PayU

  **Problem: Not receiving webhooks**
  - ✅ Test endpoint returns 200 status codes
  - ✅ Verify endpoint is publicly accessible (test with curl)
  - ✅ Check firewall allows PayU's webhook requests
  - ✅ Confirm webhook registration was successful

  **Problem: Signature validation fails**
  - ✅ Verify using correct client_secret
  - ✅ Check payload key sorting (alphabetical order)
  - ✅ Ensure using SHA-256 algorithm
  - ✅ Validate payload string construction matches PayU's method

  **Problem: Webhook processing errors**
  - ✅ Always return 200 OK to prevent retries
  - ✅ Implement comprehensive error logging
  - ✅ Handle duplicate events gracefully
  - ✅ Use try-catch blocks for all processing logic
</Accordion>

<Accordion title="Support and resources" icon="fa-life-ring">
  Where to get help and additional resources for PayU webhook integration.

  **PayU Support Channels:**
  - **Developer Support:** Contact PayU technical support team
  - **Key Account Manager:** Your designated PayU account representative
  - **Documentation:** Complete PayU API documentation portal
  - **Status Page:** Check PayU service status and maintenance schedules

  **Additional Resources:**
  - **[KYC Errors and Solutions](ref:kyc-errors-and-solutions)** - Detailed error codes and resolutions
  - **[Get Token API](ref:get_token_api)** - Authentication and token management
  - **PayU Partner Dashboard** - Webhook registration and monitoring tools
  - **Developer Community** - Forums and community support channels

  **Emergency Contact:**
  - For production issues affecting webhook delivery
  - Include webhook URLs, reseller UUID, and error details
  - Provide timeline of when issues started
  - Include relevant log excerpts and error messages
</Accordion>

---

## Next Steps

1. **✅ Complete Prerequisites** - Gather credentials and enable webhook service
2. **✅ Register Webhook** - Use PayU API to register your endpoint  
3. **✅ Implement Endpoint** - Build secure webhook receiver with signature validation
4. **✅ Test Thoroughly** - Validate all event types and error scenarios
5. **✅ Deploy to Production** - Monitor and maintain your webhook integration

**Ready to integrate?** Start with Step 1 and follow this guide sequentially for a successful PayU webhook integration! 🚀

For additional support, contact your PayU Key Account Manager or developer support team.