---
title: Get Checkout Details – NTB Seamless Journey
deprecated: false
hidden: true
metadata:
  robots: index
---
This is used in the **NTB Seamless Journey** flow. 

## Sample request

  ```cUrl
  curl --location 'https://test.payu.in/merchant/postservice.php?form=2' \
  --form 'key="0d5aDh"' \
  --form 'command="get_checkout_details"' \
  --form 'var1="{\"requestId\":\"9920371372_38\",\"transactionDetails\":{\"amount\":8000},\"useCase\":{\"getExtendedPaymentDetails\":true}}"' \
  --form 'hash="5c4784472c10fab50be3730a923474925c477e0fdd9a4957d5b0e0469cca3144cb74670ddc5cbe0e3edcbcd04dae64792a93989e99fd17b1cb4ce561659ce24a"'
  ```

## Sample response

  ```json
  {
    "status": 1,
    "details": {
      "paymentOptions": {
        "emi": {
          "all": {
            "dc": {
              "hasEligible": true,
              "all": {
                "UTIB": {
                  "title": "Axis Bank",
                  "shortName": "Axis",
                  "minimumAmount": 1000,
                  "maximumAmount": null,
                  "eligibility": {"status": true},
                  "tenureOptions": {
                    "AXISD03": {
                      "tenure": 3,
                      "interestRate": 10.5,
                      "interestCharged": 200.45,
                      "monthlyEmi": 400.5,
                      "minimumAmount": 1000,
                      "maximumAmount": null,
                      "eligibility": {"status": true}
                    }
                  }
                }
              },
              "minimumAmount": 1000,
              "maximumAmount": null
            }
          }
        },
        "nb": { "all": { "SBIB": { "title": "State Bank of India" } } },
        "dc": { "all": { "MAST": { "title": "MasterCard Debit Cards" } } },
        "cc": { "all": { "CC": { "title": "Credit Card" } } },
        "cash": { "all": { "PAYTM": { "title": "Paytm" } } }
      }
    }
  }
  ```