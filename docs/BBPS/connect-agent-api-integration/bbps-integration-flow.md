---
title: BBPS Integration Flow
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
Before you start the integration process, it is recommended to test the transaction with the **Test setup** provided by PayU, where you would be given a test agent account and test credentials to have first-hand experience of the overall transaction flow.

The following flow diagram illustrates the data flow in BBPS integration:

<Image align="center" width="500px" src="https://files.readme.io/6e0f3f1-untitled_4.png" />

The steps for integrating with PayU are:

1. Make the transaction request to ​the PayU Test server. After completing your testing, you will be ready to move to the PayU Production server. 
2. Generate a token from OAuth API with the mentioned scopes for each API. For more information, refer to [Get Token API for BBPS](https://devguide.payu.in/agent-api-integration/get-token-api-for-bbps/).
3. Agents also need to fetch all the categories or regions, and then, based on billers, agents can fetch the information through mentioned APIs. The category and biller APIs can be fetched once or twice a week because the information will not frequently change for both categories and billers.  
4. To initiate a transaction, fetch the bill for a particular biller, and this fetch request will only be initiated when the **fetchOption** parameter in the **Get All Billers by Category Name** API response has the values:  
   * **MANDATORY:** The agent needs to fetch the bill and then allow the payment. 
   * **OPTIONAL:** The agent may fetch the bill or not and then allow the payment. 
   * **NOT\_SUPPORTED:** The agent is not allowed to initiate a request for bill fetch, and the agent must send the payment request to PayU.\
     For more information on **Get All Billers by Category Name** API, refer to [Get All Billers by Category Name API](https://devguide.payu.in/agent-api-integration/biller-apis/get-all-billers-by-category-name/).
5. Similarly, the other options like **isAdhoc** are for identifying whether a biller is accepting the Adhoc payment or not.  
6. **billerMode** is for identifying the type of biller. A biller can fall under three categories:
   * ONLINE
   * OFFLINE A  
   * OFFLINE B
7. **supportBillValidation** is for identifying whether the biller should validate a bill payment request before accepting actual payment or not. It can be of the following types: 
   * MANDATORY
   * OPTIONAL
   * NOT\_SUPPORTED 
8. **blrResponseParams** will contain a breakup set of amount details. It is explained in a later stage in biller MDM API. 
9. **blrAdditionalInfo** includes the informative type that the agent will show on the agent platform. 
10. The other details like **paymentModesAllowed** and **paymentChannelsAllowed** provide the information about the particular biller’s allowed payment modes and channels through which it can pay the bills. For more information, refer to [Bill Payment API](https://devguide.payu.in/agent-api-integration/bill-apis/bbps-bill-payment-api/).
11. The agent should pass the agentTxnID in additional parameters as it is mandatory at the PayU end to identify the transaction in the recon file.
12. For a particular transaction journey, the agent needs to ensure that the reference ID is the same in both fetch and payment requests as it identifies the whole transaction journey at PayU’s end. Also, the length of the reference ID can be between 24 to 35 for Non-BBPS billers, but for BBPS billers, it should be equal to 35 as it is mandatory according to NPCI guidelines.RefId should be unique in every call for fetch and pay. 
13. Similarly, there are Prepaid  Recharge, CMS (Complaint Management System), and Plans APIs. For more information, refer to Biller Plans API.
14. When the fetch request comes to the PayU system, the PayU system identifies the biller based on the mentioned biller ID in the POST request and initiates a bill fetch request to the biller and fetches the bill from it, and sends back the information to agents as the response of fetch request. 
15. Similarly, when the payment confirmation request comes to the PayU system than PayU system identifies the biller based on the mentioned biller ID in the POST request and initiates a bill payment confirmation request to the biller and based on the requested amount and other information, the biller sends back the response as failure or success or pending to the PayU system than PayU sends back the response to the agent based on the biller response. 
16. For pending transactions, agents can request the latest status of the particular transaction using the **Payment Transaction Status** API. For more information, refer to [Bill Payment Transaction Status API](https://devguide.payu.in/agent-api-integration/bill-apis/bill-payment-transaction-status/).

To understand the fetch and pay and validation and pay kind of billers call, refer to [Biller Types in BBPS](https://devguide.payu.in/agent-api-integration/bbps-integration-flow/biller-types-in-bbps/).
