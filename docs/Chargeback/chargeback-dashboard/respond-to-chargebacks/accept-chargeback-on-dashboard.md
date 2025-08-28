---
title: Accept Chargeback on Dashboard
deprecated: false
hidden: true
metadata:
  robots: index
---
Process chargeback acceptance when the customer claim is valid.

### Full Acceptance

Use when the customer deserves a complete refund:

> **Important**: You cannot process refunds for transactions marked as chargebacks through PayU or directly to customers. The chargeback process handles the refund.

1. Navigate to the chargeback details.

2. Expand the **Accept/Contest** expandable pane using the **+** button.

<Image align="center" className="border" border={true} src="https://files.readme.io/3f3588bb64f8dbb20a93ad95a9ba41b050572595901731b5a0a4c1cc6f8829cd-chargeback_dashboard_accept_contest_pane.png" />

3. Click **Fully Accept**.

   <Image align="center" src="https://files.readme.io/23101e659f44fa0987b981cfeb0d68d37e22188289f0d94b10f3ec8e13059d56-chargeback_dashboard_fully_accept.png" />

4. Select the appropriate reason.

   <Image align="center" className="border" border={true} src="https://files.readme.io/9f54e3f00bd2ed75eb650de7af74184e43d57ce08a808f09ae8ceb71e6226b55-chargeback_dashboard_reasons_selections.png" />

5. Click **Submit** to finalize

<Callout icon="📘" theme="info">
  **Note**: After you accept, the case moves to "Closed in Customer Favor" status and cannot be modified.
</Callout>

### Partial Acceptance

Use when the customer deserves a partial refund:

1. Navigate to the chargeback details.

2. Expand the **Accept/Contest** expandable pane using the **+** button.

<Image align="center" className="border" border={true} src="https://files.readme.io/3f3588bb64f8dbb20a93ad95a9ba41b050572595901731b5a0a4c1cc6f8829cd-chargeback_dashboard_accept_contest_pane.png" />

3. Click **Partially Accept**.

The _Partially Accept Chargeback form_ page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/772613b3501c92c8ce16dbde319dd94bc4fc96970ab724ce7b6e958703d963e6-chargeback_dashboard_partially_accept_reasons.png" />

4. Select the appropriate reason.

<Callout icon="📘" theme="info">
  **Note**:  Steps 5 is not applicable for **Full refund not due as per our T&C** option.
</Callout>

5. Enter the partial acceptance amount (must be less than chargeback amount)in the **Partially Accept Amount** field.
6. Provide supporting documents using the **Browse** button in the **Supporting documents** field. (max 5MB)

<Callout icon="📘" theme="info">
  **File Upload Guidelines**

  * **File Size**: Maximum 5MB per upload
  * **File Types**: PDF, Word documents, or image files
  * **Organization**: Combine multiple screenshots into a single document
  * **Documentation**: Add brief descriptions for each piece of evidence

  > **Best Practice**: Merge all screenshots into a single MS Word or PDF file with descriptive captions for each piece of evidence.
</Callout>

7. Add detailed comments explaining the partial acceptance in the **Comments** field.
8. Click **Submit**.
