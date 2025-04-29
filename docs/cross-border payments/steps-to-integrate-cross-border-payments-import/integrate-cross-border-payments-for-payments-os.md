---
title: Integrate Import for Payments OS
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Integrate Import for Payments OS
  description: >-
    Learn how to integrate cross-border payments using Payments OS. This guide
    provides detailed instructions, request parameters, and sample responses for
    seamless international transactions.
  keywords:
    - Integrate Import for Payments OS
    - Integrate Cross-Border Import for Payments OS
    - Integrate Cross Border Import for Payments OS
    - Cross Border Import Integration for Payments OS
    - Cross Border Import for merchants outside India
    - Outside india ntegrate Cross Border Import integration
    - ' cross-border payments'
    - ' Payments OS'
    - ' international import transactions'
    - ' secure cross-border payment integration'
    - ' cross-border payments'
    - ' cross border payments'
  robots: index
next:
  description: ''
---
If you do not have a local entity in India and your business is classified as software, digital goods, or gaming, you can register for an PACB flow with PayU India.

For the **Create Payment** request. the following object contains the mandatory parameters for Cross-Border integration:

> 📘 **Reference**:
>
> For more information on **Create Change** request, refer to the [PayU Payments OS](https://developers.paymentsos.com/docs/connect/payu-countries-and-regions/payu-india.html#implementing-an-opgsp-flow) documentation.

```
    "billing_address": {
        "city": "Saharanpur",
        "phone": "98989889898",
        "country": "IND",
        "first_name": "NA",
        "last_name": "NA",
        "line1": "Saharanpur",
        "line2": "Saharanpur",
        "state": "UP",
        "zip_code": "247001"
    }
```

After registering for an PACB flow, you must post the following using the **Create Change** request (similar to the following sample code):

* invoice ID using the **invoice\_id** parameter
* buyer’s permanent account number using the **additionalDescription1** parameter
* buyers’s date of birth using the **additionalDescription3** parameter.

```javascript
{
"provider_specific_data": {
    "payu_india": {
      "additional_details": {
        ...
        "additionalDescription1": "AAAPZ1234C",
        "additionalDescription3": "22/08/1972",
        "invoice_id": "1234",
        ...
      }
    }
  },
  ...
}  
```
