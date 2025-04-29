---
title: Refunds for EMI
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Debit Card Workflow

This section describes the Debit Card EMI workflow with an example transaction. The Debit Card EMI refund workflow involves the following:

### 1. Customer initiates transaction

1. The customer does a transaction of ₹10,000 through their ICICI bank Debit card with the merchant for an order of a mobile phone (₹9,500) and earbuds (₹500).
2. A Loan of ₹10,000 is created in the customer’s account with ICICI bank. For more information on the Debit Card EMI workflow, refer to Debit Card EMI Workflow.
3. Assuming a 3% MDR on the transaction, ₹9,700 would be settled into the merchant’s account.

### 2. Customer cancels order

The workflow involved when the customer has canceled the entire order and is looking for a refund:

#### **Full Refund**

1. The merchant initiates a full refund on the transaction.
2. PayU will send the refund request to ICICI Bank for ₹10,000
3. The bank would cancel the loan. If one or more EMI have been paid, the principal of the EMI would be reversed in the customer’s bank account.
4. ₹10,000 will be deducted from the merchant’s account or subsequent settlement.

#### **Partial Refund**

The workflow involved when the customer has returned the earbuds (₹500) and is now looking for a refund:

> 📘 Note:
> 
> Not all banks support partial refund. For more information, refer to[Supported banks](#supported-banks).

1. For a partial refund of, say, ₹500, the merchant initiates a refund of ₹500 on the transaction.
2. PayU will send the refund request to ICICI Bank for ₹500.
3. The bank would adjust the EMI’s principal amount and reduce it by ₹500.
4. The remaining amount will be settled in the customer’s bank account if the EMI principal is less than the refund amount.
5. Merchant can do multiple partial refunds until the total refunded amount\<= transaction amount.

### Supported banks

<table style="border:0.1rem solid rgb(242, 242, 242);"><tbody><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;"><strong>Bank Name</strong></td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;"><strong>Full Refund</strong></td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;"><strong>Partial Refund</strong></td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Axis Bank</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Not allowed</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Bank of Baroda</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Federal Bank</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">HDFC Bank</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">ICICI Bank</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Not allowed</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Kotak Bank</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">State Bank of India</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Not allowed</td></tr></tbody></table>

## Credit Card

This section describes the Credit Card EMI workflow with an example transaction. The Credit Card EMI refund workflow involves the following:

### 1. Customer initiates transaction

1. The customer does a transaction of ₹10,000 via their ICICI bank credit card with the merchant for an order of a mobile phone (₹9,500) and earbuds (₹500).
2. ₹10,000 are deducted from the customer’s account card. Later, ₹10,000 would be reversed back to the customer’s card, and monthly EMI will be set up. For more information on Credit Card EMI workflow, refer to Credit Card EMI Workflow.
3. Assuming a 3% MDR on the transaction, ₹9,700 would be settled into the merchant’s account.

### 2. Customer cancels order

#### Full Refund

The workflow involved when the customer has canceled the entire order and is looking for a refund:

1. The merchant initiates a full refund on the transaction.
2. PayU will send the refund request to ICICI Bank for ₹10,000
3. Bank would refund ₹10,000 to customer’s credit card. The amount would come as a credit to the customer’s card.
4. ₹10,000 will be deducted from the merchant’s account/subsequent settlement.

## Cardless EMI Workflow

This section describes the Cardless EMI workflow with an example transaction. The Cardless EMI refund workflow involves the following:

### 1. Customer initiates transaction

1. Customer does a transaction of ₹10,000 via their Zestmoney account with the merchant for an order of a mobile phone (₹9,500) and earbuds (₹500).
2. A Loan of ₹10,000 is created in customer’s account with Zestmoney. (Click here for details of how Cardless EMI works).
3. Assuming a 3% MDR on the transaction, ₹9,700 would be settled into merchant’s account.

### 2. Customer cancels the order

#### Full Refund

The workflow involved when the customer has canceled the entire order and is looking for a refund:

1. The merchant initiates a full refund on the transaction.
2. PayU will send the refund request to ZestMoney for ₹10,000
3. ZestMoney would cancel the EMI. If one or more EMI have been paid, the principal of the EMI paid would be reversed in the customer’s ZestMoney account.
4. ₹10,000 will be deducted from the merchant’s account/subsequent settlement.
5. All Cardless EMIs support full refund.

#### Partial Refund

The customer has returned the earbuds (₹500) and is now looking for a refund:

1. For a partial refund of say ₹500, the process is the same. The merchant initiates a refund of ₹500 on the transaction.
2. PayU will send the refund request to ZestMoney for ₹500.
3. ZestMoney would adjust the principal amount of the EMI and reduce it by ₹500.
4. If the EMI principal is less than the refund amount, the remaining amount will be reversed in the customer’s ZestMoney account.
5. Merchant can do multiple partial refunds until total refunded amount less than or equal to transaction amount.

> 📘 Notes:
> 
> - On refund of the transaction, the processing fee charged by the lender may or may not be reversed depending on the lender’s policy. If the customer has paid any EMI to the lender, the lender will not reverse the interest charged to the customer.
> - Whether a partial or full refund, the GST and other charges already levied by the bank may not get refunded.
> - Any charges levied by PayU to get the transaction converted into EMI will not be reversed.

### Supported Banks or Firms List

<table style="border:0.1rem solid rgb(242, 242, 242);"><tbody><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;"><strong>Bank Name</strong></td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;"><strong>Full Refund</strong></td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;"><strong>Partial Refund</strong></td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Bajaj Finserv</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Liquiloans</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">ZestMoney</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">HDFC Bank</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">ICICI Bank</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Yes</td></tr></tbody></table>

## No Cost EMI Workflow

The No-Cost EMI refund process is similar to a regular EMI refund process. The only difference is that the principal amount used in the calculation is the amount after subtracting the No-Cost EMI discount.

This means the merchant can only refund up to a maximum payment minus No-Cost EMI discount.

For example, if a customer has bought ₹10,000 products through a Credit card EMI with a No-Cost EMI discount, the payment amount is ₹10,000, and the No-Cost EMI discount is ₹411. Hence, the total amount that can be refunded to the customer is ₹9,589 (₹10,000 – ₹411).