---
title: Direct Authorization Integration (copy)
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU enables merchants to process direct authorization for pre-authenticated transactions (external MPI/3DSS). This section describes how to integrate with PayU’s direct authorization flow.

This part of the document also includes how to integrate using 3DS Secure 2.0 Transaction. For more information, refer to [3DS Secure 2.0 Transaction](https://docs.payu.in/docs/prebuilt-checkout-page-integration?isFramePreview=true#3ds-secure-20-transaction).

**Steps to integrate**

<Cards columns={3}>
  <Card title="1. Post the Parameters to PayU" href="https://docs.payu.in/docs/integrate-with-direct-authorization-s2s#step-1-post-the-parameters-to-payu">
    Post the required parameters to PayU for direct authorization S2S integration
  </Card>

  <Card title="2. Check Response from PayU" href="https://docs.payu.in/docs/integrate-with-direct-authorization-s2s#step-2-check-response-from-payu">
    Check and handle the response received from PayU after posting parameters
  </Card>

  <Card title="3. Verify the payment" href="https://docs.payu.in/docs/integrate-with-direct-authorization-s2s#step-3-verify-the-payment">
    Verify the payment status and ensure transaction completion
  </Card>
</Cards>

<br />
