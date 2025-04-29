---
title: Refunds for BNPL
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
This section describes the Book Now Pay Later (BNPL) EMI workflow with an example transaction. The BNPL EMI refund workflow involves the following:

## Customer Initiates Transaction

1. The customer does a transaction of Rs. 10,000 via their Lazypay account with the merchant for an order of a mobile phone (Rs. 9,500) and earbuds (Rs.500).
2. Rs. 10,000 will be deducted from the customer’s Lazypay balance. (Click here for details of how Buy Now Pay Later works).
3. Assuming a 3% MDR on the transaction, Rs. 9,700 would be settled into the merchant’s account.

## Customer Cancels the Order

### Full Refund

The workflow involved when the customer has canceled the entire order and is looking for a refund:

1. The merchant initiates a full refund on the transaction.
2. PayU will send the refund request to Lazypay for ₹10,000
3. Lazypay would credit ₹10,000 to the customer’s Lazypay balance and would offset the dues of the customer’s Lazypay account accordingly.
   For example, if the customer has already settled the dues of the previous billing cycle in which the original transaction was done and has outstanding dues of ₹4,000 in the current billing cycle. When a refund of ₹10,000 is received, the customer’s Lazypay account would have a surplus of ₹6,000 (₹10,000 – previous outstanding of 4,000)
4. ₹10,000 will be deducted from the merchant’s account/next settlement.

### Partial Refund

Customer has returned the earbuds (Rs. 500) and is now looking for a refund:

1. For partial refund of say Rs 500, merchant initiates a refund or Rs. 500 on the transaction.
2. PayU will send the refund request to Lazypay for Rs. 500.
3. Lazypay would credit Rs. 10,000 in customer’s Lazypay balance and would offset dues of customer’s Lazypay account accordingly.
4. Merchant can do multiple partial refunds until: total refunded amount&lt;= transaction amount.

> 📘 Notes:
>
> * On refund of the transaction, processing fee charged by the Lender may or may not be reversed depending on the lender’s policy. If any EMI has been paid by the customer to the lender, lender will not reverse the interest charged to the customer.
> * Whether it is a partial refund or a full refund, the GST and other charges already levied by the bank may not get refunded.
> * Any charges levied by PayU to get the transaction converted into EMI will not be reversed.

## Supported Banks or Firm

<table style={{ border: "0.1rem solid rgb(242, 242, 242)" }}>
  <tbody>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Bank Name</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Full Refund</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Partial Refund</strong></td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>HDFC Flexipay</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Yes</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Yes</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>ICICI Bank</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Yes</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Yes</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Lazypay</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Yes</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Yes</td>
    </tr>
  </tbody>
</table>