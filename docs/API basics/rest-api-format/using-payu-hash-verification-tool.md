---
title: Using PayU Hash Verification Tool
deprecated: false
hidden: false
metadata:
  robots: index
---
## Step 1: Open the PayU Hash Verification Tool

Navigate to the following URL on your browser:

<Anchor label="https://payu-hashverificationtool.onrender.com/" target="_blank" href="https://payu-hashverificationtool.onrender.com/">https://payu-hashverificationtool.onrender.com/</Anchor>

<Image border={false} />

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

You must enter your **merchant salt** (provided by PayU) in the tool. This is essential for recomputing the hash.

<Callout icon="⚠️" theme="warn">
  **Important:** Never share your salt publicly. It is a secret key used for security.
</Callout>

***

## Step 4: Compute the hash

Click **"Verify Hash"** or equivalent button on the tool.

The tool will recompute the hash using the provided data and your salt.

## Step 5: Compare the Hashes

* The tool will display the **calculated hash**.
* Compare it with the **hash received from PayU** (`59ee485e093e4452...`).
* If both hashes match, the response is **authentic** and **untampered**.

<br />
