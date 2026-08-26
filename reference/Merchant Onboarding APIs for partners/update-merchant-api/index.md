---
title: Update Merchant API
excerpt: >-
  The Update merchant API let's you update the required details for your
  merchant including


  1. PAN detail
      
  2. Bank detail
      
  3. Operating & Registered addess
      
  4. Website details
      
  5. GST
      
  6. CIN number.
      

  ## Caution


  It is recommended to update the following details in the same order as below
  to avoid race conditions & failures:


  1. PAN detail
      
  2. Bank detail
      
  3. GST
      
  4. CIN number.
      

  Since, these information are validated in realtime, sending all at once may
  cause validation failure
hidden: false
---