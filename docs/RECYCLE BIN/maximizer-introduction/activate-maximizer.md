---
title: Activate Maximizer
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  keywords:
    - Enabling PayU Maximizer
    - Start Using PayU Maximizer
    - Transaction Routing Setup
    - Activating Maximizer
    - Activate Maximizer
  robots: index
next:
  description: ''
---
If you are an existing PayU merchant; then you can add credentials of your respective aggregators using Dashboard. 

> 🚧 Enable Maximizer
>
> If you are interested in Switch Pay product and have not done technical Integration with PayU, contact your PayU Key Account Manager or [PayU Support](help.payu.in).

To activate Maximizer on Dashboard

1. Log on to PayU Dashboard. For more information, refer to [Log in to Dashboard](doc:log-in-to-dashboard).
2. Select **Maximizer** from the menu on left-pane. 

   The **Payment Gateways** tab is displayed on the right.

<Image align="center" className="border" width="632px" border={true} src="https://files.readme.io/0a853b4-48c3167-activate_swtichpay_step1.png" />

3. Navigate to the required aggregator and click **Activate** to add credentials.

<Image align="center" className="border" width="232px" border={true} src="https://files.readme.io/f35ad45-razorpay_manage.png" />

The *Manage RazorPay* pop-up page is displayed.  

<Image align="center" className="border" width="432px" border={true} src="https://files.readme.io/c3814ce-activate_swtich_pay_step3.png" />

4. Enter the the credentials (secret key, salt) received from the aggregator, select payment options required to activate as described in the following table and then click **Update**.

| Field           | Description                                                                  |
| :-------------- | :--------------------------------------------------------------------------- |
| Secret Key      | Enter the secret key provided to you by Razorpay.                            |
| Salt            | Enter the Salt provided to you by Razorpay.                                  |
| Account Id      | Enter the account ID provided to you by Razorpay.                            |
| Payment Methods | Select the applicable payment methods that requires Switch Pay to be active. |

 The status **Activation in Progress** displayed for Razorpay. After activation is done by PayU, status will change to **Active**.

> 📘 Notes:
>
> * After entering the credentials, it will take 2-3 working days to do back-end configurations. The status will be in-progress and after configuration is complete, the status changes to **Active** from **Activation in Progress**.
> * You can manage the credentials for a payment aggregator using the **Manage** button.