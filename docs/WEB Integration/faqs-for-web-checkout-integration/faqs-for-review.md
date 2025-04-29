---
title: FAQs for Review
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
- **I encountered a currency missing error while testing PayU with HDFC net banking. Is this a new HDFC implementation, or is there an issue with PayU?**

The currency error might be due to misconfiguration. Ensure you've set the correct currency in your PayU integration and check HDFC's requirements.

- **While entering the key and salt on my Shopify website, I get a "key and salt do not match" error. What could be causing this, given that I copy/pasted them from my PayU account dashboard?**

Double-check the copied keys for accuracy. If the issue persists, ensure you are using the correct version of the key and salt or contact PayU support for assistance.

- **How can I enable international payments, especially from the USA to India, through PayU? My client wishes to pay with an American Express card via the payment link.**

PayU supports international transactions. Ensure your PayU account is configured for international payments, and your client's American Express card is supported. Contact PayU support for specific assistance.

- **PayU integration on my website stopped working after submitting a new KYC. Is there paid developer help available for resolving this issue?**

PayU provides paid developer support. Reach out to PayU's developer support team for assistance in resolving integration issues post-KYC.

- **My payment integration is not working. How can I troubleshoot and resolve this issue?**

Check the plugin version, ensure correct configuration, and review the provided testing link. If issues persist, provide specific error details for PayU support to assist you better.

- **I can't find Merchant Key Salt One for my integration. Is this a critical issue, and how can it be resolved?**

If Merchant Key or Salt is missing, contact PayU support immediately for a resolution, as it could impact the functionality of your integration.

- **I'm having difficulty integrating PayU with my Shopify store. Is there a specific process for using different versions of merchant keys and salts?**

Ensure you're using the correct version of the merchant key and salt. For Shopify integration, follow PayU's guidelines on key and salt versions. If issues persist, contact PayU support.

- **After clicking Place Order, the website goes directly to the card details page, skipping other payment methods. How can I fix this?**

Check your website's payment settings and ensure that multiple payment methods, such as Net Banking and UPI, are enabled. Adjust the settings accordingly.

1. **UAT Test Card Details**:
   - **Question**: Can the UAT test card details mentioned in the S2S Integration Docs be used?
   - **Answer**: Yes, you can use the following UAT test card details for testing:
     - **Mastercard**: 5497-7744-1517-0603
     - **Expiry**: Any future date
     - **Name**: Any name
     - **CVV**: 123
     - **OTP**: 123456

2. **Test User Credentials**:
   - **Question**: What are the test user credentials required to verify the merchant’s website?
   - **Answer**: Unfortunately, the provided information does not include test user credentials. Please check with the relevant team to obtain the necessary credentials for testing.

3. **Integration with BillEasy**:
   - **Question**: Is PayU integrated with BillEasy?
   - **Answer**: Yes, PayU is already integrated with BillEasy and is the preferred partner. Payment methods supported include Wallets, UPI, and Cards (with Cards being the most important). Separate integration is not required.

4. **KYC Documents**:
   - **Question**: What documents are needed for the Finance process?
   - **Answer**: To start the Finance process, please share the KYC documents with us.

5. **Public IP Addresses for Endpoints**:
   - **Question**: What are the Public IP addresses for UAT and Prod endpoints?
   - **Answer**:
     - **Test Endpoint**:
       - test.payu.in
       - 99.83.199.213
       - 75.2.40.57
     - **Prod Endpoints**:
       - secure.payu.in
       - 15.197.187.164
       - 3.33.169.243
       - info.payu.in
       - 52.223.46.185
       - 35.71.158.222

6. **QR Code Transaction Status Fetch API**:
   - **Question**: How do we segregate the “Result” parameter from the QR Code Transaction Status Fetch API output?
   - **Answer**: The output is not in JSON format; it is encrypted. To extract the “Result” parameter, you’ll need to decode the encrypted data. If the status is “success,” the sample output will contain relevant information.

7. **Can we provide test key/salt along with Test Card Details for UAT environment?**
   - In the UAT environment, you can refer to the provided test credentials, including test key/salt and sample card details, for testing purposes. Always use these credentials in the designated testing environment.

8. **Is it possible to change the email ID on a UAT account?**
   - No, it's not possible to change the email ID on a UAT account. If needed, create a new account with the desired email ID for testing purposes.

9. **Why does the payment page directly show card payment mode without displaying other options?**
   - This behavior is expected; however, if you encounter issues, try clicking the back option to reveal additional payment options such as UPI.

10. **Encountering an error with production payouts credentials - "Invalid client, can't find oauth client with client ID."**
    - Ensure that the provided production payouts credentials (Client ID, Client Secret, Payout Id, and Merchant ID) are correct. Double-check the endpoint and parameters used for authentication.

11. **How to enable S2S Flag for GPay integration?**
    - Contact PayU support or Key Account Manager (KAM) to enable S2S Flag for GPay integration.

12. **Mandatory steps for CheckoutPro SDK integration and hash generation.**
    - Follow the guidelines for integrating CheckoutPro SDK, including the generation of static and dynamic hashes. Refer to the provided link for detailed information.

13. **Where can I find updated plugins and documentation for SDK integration?**
    - For the latest plugins, refer to the official PayU documentation or contact support for updated links.

14. **How to handle recurring subscriptions and create subscription plans?**
    - Currently, WooCommerce does not support SI (Standing Instruction) for recurring subscriptions. Refer to the available documentation for alternative solutions.

15. **Issues with the PayU hosted checkout showing only Credit/Debit card option.**

- Ensure that the merchant is using the latest version of the PayU plugin to avoid any compatibility issues.

11. **Error: "isAggregator parameter not configured for the merchant."**

- This error suggests a configuration issue; discuss with the PayU integration team to understand and resolve the problem.

12. **URL not called after successful payment in webhook configuration.**

- Verify the webhook configuration and URL provided. Contact PayU support for assistance if the issue persists.

13. **Card number validation and format for expiry date during payment.**

- The card number can have 13-19 digits, depending on the card type. Expiry date format in separate selection tabs is not supported in PayU hosted checkout.

14. **Hash generation error in Python.**

- Follow the provided Python SDK logic for hash generation based on different scenarios. Ensure that the payload matches the expected format.

15. **Redirection issue to card details instead of "Choose payment mode."**

- If encountering redirection issues, ensure that the correct PayU plugin is installed. Follow instructions provided by PayU support to resolve the issue.

16. **Unable to access key/salt due to incomplete KYC.**

- Completion of KYC is mandatory for accessing key/salt. Contact PayU support for assistance with KYC completion.

- _Q: SI is not working in the sandbox environment. What steps should be taken to resolve this issue?_

- A: Ensure that the Bearer token in the 'Single Transfer API' is refreshed after expiry. Check the validity period for refresh tokens and review the 'Get account details' requirement for every single transfer.

- _Q: What is the purpose of 'Get account details' before each single transfer, and can retries be safely disabled on 'Single Transfer'?_

- A: 'Get account details' fetches essential information, and disabling retries may improve TAT. However, weigh the impact on SR and evaluate whether 'request processing failed' webhook events are relevant to single transfers.

- _Q: How is the 'BatchID' in the 'initiate payment' API useful? What response can be expected from the webhook?_

- A: 'BatchID' serves a specific purpose in grouping transactions. The expected response body from the webhook depends on the nature of the transaction initiated.

- _Q: Can you provide test credentials and the Pay by Link API documentation for payment link generation?_

- A: Access the PayU devguide link provided for comprehensive documentation on payment link generation using the PayU Payment Links API.

- _Q: I installed a new PayU plugin and need configuration instructions. What details should be filled, especially regarding currency, merchant key, and salt?_

- A: Follow the provided instructions for configuring the PayU plugin. Ensure correct entries for currency, merchant key, and salt. If issues persist, refer to the plugin documentation or contact PayU support.

- _Q: Seeking clarification and documentation on QR generation for UPI payments and payment link generation for online payments. Where can I find this information?_

- A: Documentation for payment link generation is available. For QR code generation, PayU is actively working on providing comprehensive documentation. Stay tuned for updates.

- _Q: How can I modify the color scheme and theme of the PayUCheckoutPro SDK?_

- A: Refer to the provided XML configuration settings for color theme modification in the PayUCheckoutPro SDK. Ensure the correct structure in the colors.xml file.