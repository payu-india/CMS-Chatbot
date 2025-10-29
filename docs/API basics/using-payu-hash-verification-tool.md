---
title: Using PayU Hash Verification Tool
deprecated: false
hidden: true
metadata:
  robots: index
---
## Step 1: Open the PayU Hash Verification Tool

Navigate to the following URL on your browser:

<Anchor label="[https://payu-hashverificationtool.onrender.com/](https://payu-hashverificationtool.onrender.com/)" target="_blank" href="https://payu-hashverificationtool.onrender.com/">[https://payu-hashverificationtool.onrender.com/](https://payu-hashverificationtool.onrender.com/)</Anchor>

<Image align="center" border={false} src="https://files.readme.io/0e04fd9f9bc081db879aa2532f4aa72ac3f51c09de513cd21e127fe8f033e10f-payu_response_validator_page1.png" />

## Step 2: Parse the required fields

From the sample response, extract the following key fields:

1. Paste the sample response in the **Callback Response Data** field.
2. Click **Parse & Fill Form** to populate the following fields based on the data in the response
   • txnid
   • amount
   • productinfo
   • firstname
   • email
   • udf1 to udf10
   • status
   • additionalCharges
   • hash (from PayU)

## Step 3: Enter your merchant Salt

You must enter your merchant salt (provided by PayU) in the **SALT** field. This is essential for recomputing the hash.

<Callout icon="⚠️" theme="warn">
  **Important:** Never share your salt publicly. It is a secret key used for security.
</Callout>

<Image align="center" border={false} src="https://files.readme.io/32f0a267baecea562d04e80f662f42d0c4567f73fd70f679a43323642156255e-payu_response_validator_page2.png" />

## Step 4: Compute the hash

Click **"Verify Hash"** on the tool.

The tool will recompute the hash using the provided data and your salt.

<Image align="center" border={false} src="https://files.readme.io/494174d76f593ba6e36ebf2bc086540f04b8bfd4ed909d43d3c77a9cfb855950-payu_response_validator_page3.png" />

## Step 5: Compare the Hashes

* The tool will display the hash calculated under **Calculated Hash** and  hash what you filled earlier in **Response Hash**.
* Compare the  hash values under **Calculated Hash** with that of under **Response Hash**

<br />