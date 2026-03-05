---
name: PACB_Verify_Payment
---
After the payment is complete, verify the transaction status using PayU's verification APIs.

<Accordion title="Verification Methods" icon="fa-check-circle">
  Use one of the following methods to verify the payment:

  1. **Webhook/Callback**: PayU sends a POST request to your `surl` or `furl` with transaction details
  2. **Verify Payment API**: Call the `verify_payment` API with the transaction ID
</Accordion>

<Accordion title="Verify Payment API" icon="fa-code">
  ```bash
  curl --location --request POST 'https://info.payu.in/merchant/postservice.php?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JPM7Fg' \
  --data-urlencode 'command=verify_payment' \
  --data-urlencode 'var1=payuTestTransaction12345' \
  --data-urlencode 'hash=YOUR_CALCULATED_HASH'
  ```
</Accordion>

<Accordion title="Sample Webhook Response" icon="fa-table">
  ```plaintext
  mihpayid=27553369917
  &mode=SBQR
  &status=success
  &key=rZ1fX4
  &txnid=T2603041446091822117753
  &amount=40.00
  &addedon=2026-03-04+14%3A46%3A14
  &productinfo=Static+QR
  &firstname=
  &lastname=
  &address1=
  &address2=
  &city=Gurgaon
  &state=
  &country=
  &zipcode=122001
  &email=
  &phone=##########
  &udf1=
  &udf2=
  &udf3=
  &udf4=SoftQR
  &udf5=BFL0000006601446
  &udf6=
  &udf7=
  &udf8=
  &udf9=
  &udf10=
  &card_token=
  &card_no=
  &field0=STQ9IUFeqlafg78815827
  &field1=PRIYA+SHANKAR+PUSNAKE
  &field2=995486
  &field3=_mobilenum_%40axl
  &field4=bajajpay.6879729.d2m9cckd%40indus
  &field5=AXLd36cfcd317f243b5b3a2d62bc71caf78
  &field6=00000038683323284%7C_mobilenum_%7CSBIN0011418
  &field7=APPROVED+OR+COMPLETED+SUCCESSFULLY%7C00
  &field8=Payment+from+PhonePe
  &field9=Transaction+is+Successful.+Bank+Sent%3ATransaction+success
  &payment_source=payu
  &cardToken=
  &authenticaticationMethod=
  &PG_TYPE=SBQR-PG
  &error=E000
  &error_Message=No+Error
  &net_amount_debit=40
  &discount=0.00
  &offer_key=
  &offer_availed=
  &unmappedstatus=captured
  &hash=aefe0213c4299c7ee2039d5430f7bee63711ee627e1b47d2605d0384abbbf828f3641dae3cb126c8b2f761084cbb0bebad27bb325696cc44ce3061157d7cd9ff
  &bank_ref_no=793887773815
  &bank_ref_num=793887773815
  &bankcode=UPISBQR
  &surl=
  &curl=
  &furl=
  &psp_name=CARDHOLDERXXXXXXXXNAME
  ```
</Accordion>

For more information, refer to (Webhook Events and Sample Payloads)[docs:webhook-events-and-sample-payloads]

<Accordion title="Callback Response Parameters" icon="fa-table">
  | Parameter   | Description                                |
  | ----------- | ------------------------------------------ |
  | status      | Transaction status: `success` or `failure` |
  | txnid       | Your transaction ID                        |
  | mihpayid    | PayU transaction ID                        |
  | amount      | Transaction amount                         |
  | productinfo | Product information                        |
  | hash        | Response hash for verification             |
</Accordion>

<br />
