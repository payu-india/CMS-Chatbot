---
name: Partner_Webhook_Handler
---
<Accordion title="Sample Python Flask Webhook Handler" icon="fa-code">
  ```python
  from flask import Flask, request, jsonify
  import hashlib

  app = Flask(__name__)

  @app.route('/partner/webhook/success', methods=['POST'])
  def handle_success_webhook():
      webhook_data = request.json
      
      # Verify hash
      if not verify_webhook_hash(webhook_data, "your_client_secret"):
          return jsonify({"error": "Invalid hash"}), 400
      
      # Extract details
      txnid = webhook_data.get('txnid')
      mihpayid = webhook_data.get('mihpayid')
      status = webhook_data.get('status')
      mode = webhook_data.get('mode')
      amount = webhook_data.get('amount')
      
      # Update database
      # db.update_payment_status(txnid=txnid, mihpayid=mihpayid, status=status)
      
      print(f"✅ Payment Success: {txnid} | PayU ID: {mihpayid} | Mode: {mode} | Amount: ₹{amount}")
      
      # Respond with 200 OK
      return jsonify({"message": "Webhook received"}), 200

  if __name__ == '__main__':
      app.run(port=5000)
  ```
</Accordion>
