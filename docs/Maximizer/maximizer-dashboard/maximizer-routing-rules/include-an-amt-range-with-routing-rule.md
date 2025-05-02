---
title: Include an Amount Range with a Routing Rule
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
While creating a SRT, priority or percentage rule, you can add a amount range for a payment method. This section describes how to add a routing rule with Debit Card as an example. 

> 📘 Reference:
>
> For more information, creating a rule, refer to any of the following:
>
> * [Add a SRT Routing Rule](https://docs.payu.in/docs/add-a-routing-rule)
> * [Add a Priority-Based Routing Rule](https://docs.payu.in/docs/add-a-routing-rule-with-srt-copy)
> * [Add a Percentage-Based Routing Rule](doc:add-a-percentage-based-routing-rule)

To include an amount range for a routing rule involving debit cards:

1. Select the **Routing Rules** tab on the Maximizer Dashboard.

   The **Routing Rules** tab is displayed similar to the following screenshot (without any existing rules).

<Image align="center" className="border" border={true} src="https://files.readme.io/6022c93-Screenshot_2024-06-19_at_10.18.01_AM.png" />

<Image align="center" width="00px" src="https://files.readme.io/3e1f65b-Screenshot_2024-06-19_at_10.18.01_AM.png" />

2. Click **Create rule now**.

The *Create Custom Rule* page with the *Rule Configuration* screen is displayed.

3. Select the **Debit Cards** tab.

The **Debit Cards** tab is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/e8d27a3e354873bb690d08bb64dec1760e5a96ebb73105d3a6c10887c4a894ff-maximiser_percentage_based_routing_cards.png" />

4. Perform the steps in in the **Card Based** or **BIN based** tab:

   <Table align={["left","left"]}>
     <thead>
       <tr>
         <th style={{ textAlign: "left" }}>
           Tab
         </th>

         <th style={{ textAlign: "left" }}>
           Steps
         </th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td style={{ textAlign: "left" }}>
           Card Based
         </td>

         <td style={{ textAlign: "left" }}>
           a. Click the **Issuer Bank**drop-down list in and select the banks for which routing rules apply.\
           b. Click the**Card type**drop-down list and select the card type.\
           c. In **Rule 1** pane, enter the condition using the **When** and**Is** drop-down lists.\
           d. . In **Rule 1** pane, enter the amount range in the **Transaction Amount Range** field. For more information, refer to [Include an Amount Range with a Routing Rule](doc:include-an-amt-range-with-routing-rule) .\
           e. Click the **Add Another Rule** button to add another rule and repeat step c and d.\
           ![](https://files.readme.io/19eb874dd78bc12e79d134917006d605e999494feedf8d967fc23151d831f094-maximiser_percentage_based_routing_cards.png)
         </td>
       </tr>

       <tr>
         <td style={{ textAlign: "left" }}>
           BIN based
         </td>

         <td style={{ textAlign: "left" }}>
           a. Click the Upload button.  

           * \*Not&#x65;**: Click the Download button in the Sample File pane and include the BIN list.\
             ![](https://files.readme.io/4a190d95f781f98500a7b0bc88bae8bbb67b798feb004dc8b756933261a9c793-maximiser_percentage_based_routing_cards_bin.png)\
             b. Click the **&#x41;dd Another Rule\*\* button to add another rule.\
               

           > �![](https://files.readme.io/0b0362640594519e0bb83187187bb6ed5cbe6862692143649c4ecf236ea2f297-maximizer_cards_bin_add_another_rule.png)g)\
           > c. In **Rule 1** pane, enter the condition using the **When**, **Is**  and **Then**drop-down lists.  
         </td>
       </tr>
     </tbody>
   </Table>

> Note: If you specify an invalid amount range, an error message similar to the following is displayed:
>
> *Set the range for which this rule applies. If left blank the rule will apply to all transaction amounts. Note: Use only positive amount values that are greater than zero*

4. Click **Next** after you have selected the banks and cards for routing.

<Maximizer_Alert />

The *Payment Aggregator* screen is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/553ab23e4a9329752f075687008fd784d1d3b6f26965089310e2676c0df92032-dashboard-maximizer-amt-based-routing.png" />

6. Select the **Set Custom Baseline** check box to configure custom baseline for this rule/
   > 📘 Baseline Reference:
   >
   > For detailed understanding on baseline, refer to [Understanding Baseline Logic](doc:understanding-baseline-logic).

The *Rule Guidelines* screen is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/422426d590c3a2b4f079e0f641b508f77603cffba822bbf3c614bbe1fbf34bb6-image_21.png" />

7. Enter the name for the rule in the **Title** field.
8. Click **Next**.

The Preview page is displayed.

<Image align="center" className="border" border={true} src="https://files.readme.io/c25b1c2a105deca295cb78fdb821d912cd365a2d37d27f739ceb0b1ec2bb5dda-dashboard-maximizer-rule-preview.png" />

9. Click **Publish Now** to create the rule.

   The rule is added to the **Routing Rules** tab of Maximizer dashboard.

The rule is added to the **Routing Rules** tab of Maximizer dashboard.

<Image align="center" className="border" border={true} src="https://files.readme.io/df9389a-Screenshot_2024-06-19_at_11.00.27_AM.png" />