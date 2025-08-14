---
title: 'Launch Chargeback Dashboard '
deprecated: false
hidden: false
metadata:
  robots: index
---

## Respond to Chargebacks

### **[Accept Chargeback](https://docs.payu.in/docs/accept-chargeback)**: Process full or partial acceptance of chargeback cases when appropriate.

### **[Contest Chargeback](https://docs.payu.in/docs/contest-chargeback)**: Submit documentation and evidence to dispute invalid chargeback claims.

### **[Update Contact Details](https://docs.payu.in/docs/update-merchant-contacts)**: Maintain current contact information for chargeback notifications and alerts.

## Access Dashboard

Learn how to navigate to and use the Chargeback Management Dashboard.

### Navigate to Dashboard

The Chargeback Management Dashboard can only be accessed by super users or users with the chargeback role.

1. **Locate Chargeback Link**
   - Find the **CHARGEBACKS** link in the left navigation panel
   - This link appears below **BULK UPLOAD** for authorized users

2. **Open Dashboard**
   - Click the **CHARGEBACKS** link
   - The dashboard opens in a new browser tab

3. **Review Timeframe Notifications**
   - Pay attention to the timeframe information displayed at the top
   - Click **Show/Hide** to manage notification visibility

### Chargeback Timeframes

<HTMLBlock>{`
<table>
<thead>
<tr>
<th>Chargeback Type</th>
<th>Response Timeframe</th>
</tr>
</thead>
<tbody>
<tr>
<td>1st Level Chargeback</td>
<td>1 Day to 5 Days (Calendar Days)</td>
</tr>
<tr>
<td>2nd Level Chargeback & Pre-arbitration</td>
<td>1 Day to 3 Days (Calendar Days)</td>
</tr>
<tr>
<td>Pre-Compliance, Arbitration</td>
<td>1 Day (Calendar Day)</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

> **Critical**: Each case displays a "Reply Before" date. Failure to respond before this deadline will result in automatic case closure and transaction reversal in favor of the customer.

### Dashboard Overview

The dashboard provides:
- **Status Analysis**: Chart view showing case distribution across different statuses
- **Case Listing**: Comprehensive table with all chargeback cases
- **Filter Options**: Advanced search and filtering capabilities
- **Export Functionality**: Download options for case data

---

## View Cases

Understand the different chargeback statuses and how to review cases effectively.

### Chargeback Status Categories
<HTMLBlock>{`
<table>
<thead>
<tr>
<th>Status</th>
<th>Description</th>
<th>Action Required</th>
<th>Display</th>
</tr>
</thead>
<tbody>
<tr>
<td>NEW</td>
<td>Cases uploaded by PayU but not yet reviewed by the merchant</td>
<td>Review and respond to these cases first</td>
<td>Shows total count and amount for all NEW cases</td>
</tr>
<tr>
<td>PENDING RESPONSE</td>
<td>Cases already viewed by the user but awaiting merchant response</td>
<td>Provide response before the deadline</td>
<td>Shows total count and amount requiring immediate attention</td>
</tr>
<tr>
<td>PENDING DOC REVIEW</td>
<td>Cases with merchant responses submitted to the bank for review according to Visa/MasterCard chargeback guidelines</td>
<td>No action required - under bank review</td>
<td>Bank review process in progress</td>
</tr>
<tr>
<td>INSUFFICIENT DOCUMENT</td>
<td>Cases where submitted documentation was deemed insufficient</td>
<td>Urgent response needed with updated documentation before deadline</td>
<td>High priority - requires immediate attention</td>
</tr>
<tr>
<td>SUBMITTED TO BANK</td>
<td>Cases submitted to the bank as re-presentment by PayU Chargeback team</td>
<td>No action required - awaiting bank decision</td>
<td>Awaiting bank decision on the dispute</td>
</tr>
<tr>
<td>CLOSED IN CUSTOMER FAVOR</td>
<td>Cases settled in favor of the customer due to merchant acceptance or invalid documentation</td>
<td>No action required - case closed</td>
<td>Final status - customer refund processed</td>
</tr>
<tr>
<td>CLOSED</td>
<td>Cases reviewed and submitted to the acquiring bank</td>
<td>No action required - case closed</td>
<td>Considered closed in merchant's favor unless further disputes arise</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>
### Filter Cases

Use the available filters to efficiently locate specific cases:

- **PayU ID[s]**: Search using comma-separated PayU IDs
- **Transaction ID[s]**: Search using comma-separated transaction IDs  
- **Bank Case[s]**: Search specific bank case numbers
- **Chargeback Status**: Filter by case status
- **Date Range**: Set "From" and "To" dates for chargeback cases

---

## Case Details

View comprehensive information for individual chargeback cases.

### Transaction Information

Each case displays detailed transaction data:

- **Merchant Transaction ID**: Your internal reference
- **PayU ID**: PayU system identifier
- **Transaction Details**: Date, amount, payment gateway
- **Card Information**: Masked card number for security
- **Settlement Data**: Bank reference, settlement date, UTR details
- **Product Information**: Associated product details and fees

### Chargeback Information

Detailed chargeback-specific data includes:

- **Chargeback Amount**: Disputed transaction amount
- **Important Dates**: Chargeback date and reply deadline
- **Reason Code**: Specific reason for the chargeback
- **Bank Case Number**: Reference for bank communications
- **Current Status**: Real-time case status
- **Debit Information**: Details if amount has been debited

### Customer Details

When available, customer information includes:
- Contact details (name, email, phone)
- Relevant customer communication history

---

## Filter & Export

Efficiently manage and export chargeback data using advanced filtering options.

### Advanced Filtering

Use multiple filter criteria to refine your case view:

1. **Single ID Search**: Enter one PayU ID or Transaction ID
2. **Multiple ID Search**: Use comma-separated values for bulk searches
3. **Status Filtering**: Select one or multiple status categories
4. **Date Range**: Specify exact date parameters for targeted searches
5. **Bank Case Filter**: Search using specific bank case numbers

### Export Functionality

#### Export Current View
- Click **Export** to download visible cases
- Applies current filter settings to export
- Downloads as Excel (.xlsx) format

#### Download Management
1. Click **Download Results** to access the downloads page
2. View file creation status and download links
3. Files remain available for 7 days post-creation
4. Download completed files by clicking the file link

---

## Accept Chargeback

Process chargeback acceptance when the customer claim is valid.

### Full Acceptance

Use when the customer deserves a complete refund:

> **Important**: You cannot process refunds for transactions marked as chargebacks through PayU or directly to customers. The chargeback process handles the refund.

1. **Select Accept Option**
   - Click **"Fully Accept"** button
   - Choose from predefined reason categories

2. **Provide Reason**
   Select the appropriate reason:
   - Customer cancelled the order
   - Product out of stock  
   - Product returned by customer
   - Product lost in transit
   - Incorrect delivery address
   - Order/booking unsuccessful
   - Other reasons

3. **Submit Response**
   - Add any additional comments
   - Click **Submit** to finalize

> **Note**: Once accepted, the case moves to "Closed in Customer Favor" status and cannot be modified.

### Partial Acceptance

Use when the customer deserves a partial refund:

1. **Select Partial Accept**
   - Click **"Partially Accept"** button
   - Choose appropriate reason category

2. **Specify Details**
   - Enter the partial acceptance amount (must be less than chargeback amount)
   - Select reason from available options:
     - Product/Services partially delivered
     - Transaction partially refunded
     - Partial refund per terms and conditions

3. **Upload Documentation**
   - Provide supporting documents (max 5MB)
   - Add detailed comments explaining the partial acceptance
   - Submit the response

---

## Contest Chargeback

Dispute invalid chargeback claims with proper documentation.

### When to Contest

Contest chargebacks when:
- Product/services were delivered successfully
- Customer claim is invalid or fraudulent  
- Transaction was already refunded
- Customer has withdrawn the dispute

### Contest Process

1. **Initiate Contest**
   - Click **"Contest CB"** button
   - Select appropriate reason for contesting

2. **Choose Contest Reason**
   - **Product/Services Delivered**: Complete fulfillment proof required
   - **Partially Delivered**: Partial fulfillment documentation
   - **Customer Withdrawn**: Evidence of customer withdrawal
   - **Already Refunded**: Proof of prior refund processing

3. **Provide Documentation**

   For **Product/Services Delivered**, submit:
   - **Service Details**: Comprehensive description of services provided
   - **Proof of Services**: Evidence of successful delivery/completion
   - **Fulfillment Screenshots**: Visual proof of service completion
   - **Invoice Screenshots**: Billing and payment confirmation
   - **Additional Evidence**: Any other relevant supporting documentation

4. **File Upload Guidelines**
   - **File Size**: Maximum 5MB per upload
   - **File Types**: PDF, Word documents, or image files
   - **Organization**: Combine multiple screenshots into a single document
   - **Documentation**: Add brief descriptions for each piece of evidence

> **Best Practice**: Merge all screenshots into a single MS Word or PDF file with descriptive captions for each piece of evidence.

### Response Timeline

- Submit all documentation before the "Reply Before" deadline
- PayU chargeback team reviews submitted evidence
- Team creates comprehensive case for bank submission
- Bank reviews according to Visa/MasterCard guidelines

---

## Update Contact Details

Maintain current contact information to receive timely chargeback notifications.

### Importance of Current Contacts

All chargeback notifications, fraud alerts, and dispute communications are sent to registered email addresses. Outdated contact information can result in:
- Missed critical deadlines
- Automatic case closures
- Financial losses from uncontested chargebacks

### Update Process

1. **Access System Settings**
   - Navigate to **My Account** → **System Settings**

2. **Locate Dispute Alerts**
   - Scroll to **"Dispute Transaction Alert"** section
   - Toggle the alert to **ON** status

3. **Add Contact Information**
   - **Email Addresses**: Enter multiple emails separated by commas
   - **Phone Numbers**: Add multiple numbers separated by commas
   - **Group Emails**: Recommended for team notifications

4. **Save Changes**
   - Click **Save** to confirm updates
   - Verify notification settings are active

### Best Practices

- **Use Group Emails**: Create team distribution lists instead of individual addresses
- **Multiple Contacts**: Add several responsible team members
- **Regular Updates**: Review and update contacts quarterly
- **Test Notifications**: Verify alert delivery after setup

---

## Support

### Contact Information

For chargeback-related assistance:

**PayU Chargeback Support Team**
- **Email**: Payu-chargeback@payu.in
- **Phone**: 
  - 0124-6786255
  - 0124-6786262  
  - 0124-6786223

### Additional Resources

- **Key Account Manager**: Contact your assigned account manager for strategic guidance
- **Documentation**: Refer to this guide for step-by-step procedures
- **Dashboard Help**: Use the Help section within the merchant panel

### Important Legal Notice

This document provides educational guidance for using the merchant chargeback management dashboard and should be used for general information purposes only. PayU disclaims all warranties and is not responsible for merchant use of this information. Individual chargeback cases should be reviewed independently, and procedures may be amended as appropriate.

No information in this guide alters existing contractual obligations between PayU Payments Private Limited and the merchant.

---

*Version 2.0 | Updated: January 2020*  
*© PayU Payments Pvt Ltd - Confidential & Proprietary*
