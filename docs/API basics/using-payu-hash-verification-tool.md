---
title: Using PayU Hash Verification Tool
deprecated: false
hidden: true
metadata:
  robots: index
---
## Step 1: Open the PayU Hash Verification Tool

Navigate to the following URL on your browser:

<Anchor label="https://payu-hashverificationtool.onrender.com/" target="_blank" href="https://payu-hashverificationtool.onrender.com/">https://payu-hashverificationtool.onrender.com/</Anchor>

<Image align="center" border={true} src="https://files.readme.io/75fb157bf54d764aaf1692a9b6744de07bec1ddcdffad59c95d14c03f68255d6-Screenshot_2026-02-04_at_2.34.04_PM.png" className="border" />

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

<Image align="center" border={true} src="https://files.readme.io/0ddb50a1e38351c32cce9f97b3ae57b6e8fa3c9d7b7abb835dfd2b3d178a4b1b-image_8.png" className="border" />

## Step 4: Compute the hash

Click **"Verify Hash"** on the tool.

The tool will recompute the hash using the provided data and your salt.

<Image align="center" border={true} src="https://files.readme.io/24a0be047e99105ceaefcd9bb818c76fb15d4f6ca00833cfafc948f00f26e594-image_9.png" className="border" />

## Step 5: Compare the Hashes

* The tool will display the hash calculated under **Calculated Hash** and  hash what you filled earlier in **Response Hash**.
* Compare the  hash values under **Calculated Hash** with that of under **Response Hash**

<br />
