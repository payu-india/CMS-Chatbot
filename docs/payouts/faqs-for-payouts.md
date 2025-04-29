---
title: FAQs for Payouts
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
- **What is PayU Payouts?**  
        **PayU Payouts** is a service offered by PayU that allows merchants to make instant payments to beneficiaries through APIs. It simplifies the process of securely transferring funds to recipients.

- **Why should merchants integrate with PayU Payouts?**  
        Integrating with **PayU Payouts** provides several benefits:
  - Efficient management of payments, including refunds, commissions, and other disbursements.
  - Seamless experience for both merchants and beneficiaries.
  - Streamlined payment processing.

- **How can merchants integrate PayU Payouts?**  
        The integration process involves the following steps:  
          - Understand the flow and implementation details. For more information, refer to [Process Flow for Payouts](doc:process-flow-for-payouts) and [Payouts Integration](doc:payouts-integration).  
          - Ensure you have the necessary credentials and access to the required APIs. For more information, refer to [Test Credentials](doc:test-credentials-for-payouts) and [Authentication for Payouts](ref:authentication-for-payouts).  
          - Utilize the **Single Transfer Integration** to initiate instant payments to beneficiaries. Refer to [Single Transfer Integration](doc:single-transfer-integration-for-payouts) and [Initiate Transfer API](ref:initiate-transfer-api-bckup).

- **What payment modes are supported for Payouts?**  
        **PayU Payouts** supports various payment modes, including UPI, wallets, and bank transfers. Merchants can choose the most suitable option based on beneficiary preferences.

- **Why should merchants integrate with PayU Payouts?**  
         By integrating with **PayU Payouts**, merchants can efficiently manage payments to beneficiaries, whether it’s for refunds, commissions, or other disbursements. The integration ensures a seamless experience for both merchants and recipients.

- **What payment modes are supported for Mobile Payouts?**  
      **PayU Payouts** supports various payment modes, including UPI, wallets, and bank transfers. Merchants can choose the most suitable option based on their beneficiaries’ preferences.

- **How do I generate an authentication token for PayU Payouts integration?**  
      To access Payouts endpoints, you need an **Access Token** for authentication. PayU provides two methods to generate this token:
  - **Merchant’s Credentials API**: Obtain the token using your merchant credentials.
  - **Private Client ID**: Generate the token using a private client ID.
  - Remember that authentication tokens have a **Time To Live (TTL)** and need to be refreshed periodically. You can request a **Refresh Token API** to obtain a renewed access token.

- **What information does the Get Account Details API provide?**  
      The **Get Account Details API** returns comprehensive account information related to your merchant’s Payouts account. Use this API to retrieve essential details for seamless integration.

- **How can I initiate a single transfer to a beneficiary?**  
      Use the **Initiate Single Transfer API** to request the initiation of a single transfer to the beneficiary. You can transfer funds through various payment modes, including:

  - IMPS, NEFT, or RTGS Payment Request
  - UPI Payment Request
  - MasterCard Payment Request
  - VISA Card Payment Request
  - Credit Card Payment Request

- **How do I check the status of a transfer?**  
      Fetch the status of a transfer by posting the merchant’s reference ID as a parameter using the **Check Transfer Status API**. This API provides real-time information on the progress of your payouts. For more information, refer to [Check Transfer Status API](ref:check-transfer-status-api).
  - For more details on Payouts statuses, refer to [Payouts Lifecycle](doc:payouts-lifecycle).
  - To integrate Webhooks and get updates on the payouts, refer to [Payouts Webhooks](doc:payouts-webhooks).

- **How do I set up an Individual Webhook?**  
      To listen to a particular event (e.g., Payouts transfer success), create an HTTP POST API at your server’s end. Ensure that you whitelist PayU’s IP address if you have IP whitelisting enabled. Individual webhooks allow targeted event notifications.

- **What is the default Webhook in PayU Payouts?**  
      PayU offers a solution for setting up a **default webhook**. If you haven’t set individual webhooks for specific events, the default webhook captures events that don’t have a dedicated webhook. For example, if you’ve set webhooks for transfer success and failure, the default webhook handles other events like deposits or low balance notifications. For more information, refer to [Payouts Webhooks](doc:payouts-webhooks).

- **How do Webhooks work in PayU Payouts?**  
      When an event occurs (e.g., a successful transfer), PayU calls the webhook (API) you’ve configured. You can choose to listen to specific events individually or use the default webhook for broader coverage. Implement proper error handling and ensure your webhook endpoints are secure. For more information, refer to [Payouts Webhooks](doc:payouts-webhooks).

- **What Events Can I Configure Webhooks For?**  
      You can create webhooks for various events, including:  
        - **deposit\_success**: Notifies when an amount is successfully deposited/credited.  
        - **transfer\_success**: Indicates a completed transfer.  
        - **transfer\_failed**: Alerts about a transfer failure.

- **What is the initial state of a Payout transaction?**  
      The initial state is **QUEUED**. When you initiate a transfer, the transaction enters the queue for processing. If your merchant account lacks sufficient balance, the payout remains in the queued state until funds are deposited into the virtual account.

- **What does the “IN PROGRESS” status indicate?**  
      When a transaction moves out of the queue and processing begins, it transitions to the **IN PROGRESS** state. This intermediate state precedes the final states (SUCCESS or FAILURE).

- **How does the “PENDING” status work?**  
      The **PENDING** status indicates that the transaction is being processed by the partner bank, and the final status (SUCCESS or FAILURE) is yet to be received. Reconciliation for pending transactions occurs approximately every 5 minutes.

- **What happens when a transaction reaches the “SUCCESS” state?**  
      In the **SUCCESS** state, the transaction is completed successfully, and the amount is transferred to the customer’s account.

- **What if a transaction fails?**

    The **FAILURE** state occurs when a transaction fails. Check for errors (e.g., low balance, invalid account details) and resolve them. You can retry with a new transaction.

- **What if a transaction fails?**  
      The **FAILURE** state occurs when a transaction fails. Check for errors (e.g., low balance, invalid account details) and resolve them. You can retry with a new transaction.

- **What does the “REVERSED” state signify?**  
      A transaction enters the **REVERSED** state due to incorrect account details or reversal by the clearance bank or beneficiary bank. Once in this state, it doesn’t transition to any other state.

- **How does the “WAITING FOR RETRY” status work?**  
      When a transaction encounters issues like “Beneficiary Bank Server Down” or “Request Timeout,” it transitions to the **WAITING FOR RETRY** status. Retry occurs three times at specific intervals.

- **What is the “PENDING FOR APPROVAL” state?**  
      Transactions in the **PENDING FOR APPROVAL** state await approval from the Maker/Checker Approval Workflow. Refer to the workflow documentation for more details.

- **What happens when a transaction is “REJECTED”?**  
        The **REJECTED** state occurs due to incorrect beneficiary details or rejection from the Maker/Checker Approval Workflow.  
  \- **When does a transaction get “CANCELLED”?**  
        The **CANCELLED** state applies only when the payout is in the queued state and is canceled before processing.

- **What Are Webhooks**  
  Webhooks are a way for one server to communicate with another server by sending an HTTP callback or message. These callbacks are triggered by specific events or instances and operate at the server-to-server (S2S) level. In the context of payment processing, webhooks allow real-time updates between the merchant's server and PayU's server when certain events occur within the payment workflow¹.

- **Why Does PayU Use Webhooks?**  
  PayU utilizes webhooks technology to establish a secure and accountable architecture for payment processing. When events like successful transactions or changes in order status occur, webhooks are used to send real-time updates between servers. By setting up a listener on their server, merchants can receive these webhooks. Proper security measures, such as SSL/TLS encryption, should be implemented to ensure the confidentiality and integrity of the information being sent via webhooks.

- **How to configure Webhooks in PayU?**  
  To use webhooks during integration with PayU:
  1. Create a server URL from your business server landscape and share it with PayU, along with its server IP address. This URL is where the transaction response from PayU will hit.
  2. PayU will configure the merchant's server URL at its backend, mapping it against the MID (Merchant ID) and key of that particular merchant.
  3. PayU will whitelist the webhook URL provided by the merchant in its systems.