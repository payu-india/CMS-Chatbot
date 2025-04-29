---
title: Configure Payouts Dashboard Settings
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
You can configure the Payouts Dashboard using the **Settings** option.

To configure the Payouts Dashboard settings:

1. Click the drop-down menu icon placed next to the User Name and click **Settings**.

![image22.png](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image22-png.png)

   On clicking, the _**Settings**_ page is displayed.

2. Click the **Payouts** tile in the page.

![image13.png](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image13-png.png)

   On clicking, the _Payouts Settings_ page is displayed. You will see **Payout Configurations, Manage Checkers and Level Settings,** and **Manage Amount Rule Settings.**

![image5.png](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image5-png.png)

- **Payouts Configurations**: Used to configure the Payouts settings.

![image8.png](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image8-png.png)

   The following table gives detailed information about the fields available in **Payouts Configuration**:

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Field Description",
    "0-0": "Set Default Payout ID",
    "0-1": "Used to define a particular Payouts ID as Default ID out of all the assigned IDs. This ID is selected as a default ID whenever you visit the Payouts Dashboard or perform any actions using it.",
    "1-0": "Set Override Payout ID",
    "1-1": "Used to define a Payouts ID which will be considered for processing all API transactions",
    "2-0": "Smart Send Expiry",
    "2-1": "Used to define number of days after which the Smart Send link will expire",
    "3-0": "Queuing Payout",
    "3-1": "Used to enable or disable queued payouts flow. The valid values are:  \n- true  \n- false  \nBy default, it is set to True.",
    "4-0": "Retry by NEFT",
    "4-1": "Used to indicate whether to retry transfer through NEFT payment mode, if transfer failed done through IMPS. The valid values are:  \n- true  \n- false  \nBy default, it is set to true.",
    "5-0": "Enable Approval Flow",
    "5-1": "Used to indicate whether to enable Approval Flow for a particular amount or not. The valid values are:  \n- true  \n- false  \nBy default, it is set to true. Also, if this field is set to false then associated settings are also disabled."
  },
  "cols": 2,
  "rows": 6,
  "align": [
    null,
    null
  ]
}
[/block]


- **Manage Checkers and Level Settings:** Used to configure the Approval workflow settings such as managing Checkers and their Levels of Approval as per the hierarchy. Refer to the figure below:

![image6.png](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image6-png.png)

[block:parameters]
{
  "data": {
    "h-0": "Field Name",
    "h-1": "Field Description",
    "0-0": "Set Default Payout ID",
    "0-1": "Used to define a particular Payouts ID as Default ID out of all the assigned IDs. This ID is selected as a default ID whenever you visit the Payouts Dashboard or perform any actions using it.",
    "1-0": "Set Override Payout ID",
    "1-1": "Used to define a Payouts ID which will be considered for processing all API transactions",
    "2-0": "Smart Send Expiry",
    "2-1": "Used to define number of days after which the Smart Send link will expire",
    "3-0": "Queuing Payout",
    "3-1": "Used to enable or disable queued payouts flow. The valid values are:  \n- true  \n- false  \nBy default, it is set to True.",
    "4-0": "Retry by NEFT",
    "4-1": "Used to indicate whether to retry transfer through NEFT payment mode, if transfer failed done through IMPS. The valid values are:  \n- true  \n- false  \nBy default, it is set to true.",
    "5-0": "Enable Approval Flow",
    "5-1": "Used to indicate whether to enable Approval Flow for a particular amount or not. The valid values are:  \n- true  \n- false  \nBy default, it is set to true. Also, if this field is set to false then associated settings are also disabled."
  },
  "cols": 2,
  "rows": 6,
  "align": [
    null,
    null
  ]
}
[/block]


- **Manage Checkers and Level Settings:** Used to configure the Approval workflow settings such as managing Checkers and their Levels of Approval as per the hierarchy. Refer to the figure below:

![image6.png](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image6-png.png)

The following table provides detailed information about the fields available on **Manage Checkers and Level Settings**:

| **Field Name**       | **Field Description**                                                                                                         | **Mandatory** |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------- |
| Level Information    | Displays the level of the approval and the name of the Checker assigned to that level. For example, Level 2 (Name of Checker) |               |
| Add Level            | Used to add a new level of approval and assign a Checker                                                                      |               |
| Set Hierarchy Level  | Used to assign a level of approval as per the hierarchy. The valid values are:                                                | Yes           |
| Assign Name to Level | Used to specify a unique name to the level                                                                                    | Yes           |
| Add Approver         | Used to add approver for approving the payout.                                                                                | Yes           |

- **Manage Amount Rule Settings:** Used to define or edit rules to manage Approval workflow for Amount. Refer to the figure below:

The following table gives detailed information about the fields available on **Manage Amount Rule Settings**:

| **Field Name**                      | **Field Description**                                                                                           | **Mandatory** |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------- |
| Rule                                | Displays the amount rule defined in an Approval Workflow                                                        |               |
| Level 2 Settings                    | Displays the information about the Level 2 Settings such as                                                     |               |
| Level 3 Settings                    | Displays the information about the Level 3 Settings such as                                                     |               |
| Actions                             | Perform any of the following:                                                                                   |               |
| Add Workflow                        | Click to define a new Approval Workflow.                                                                        |               |
| Select Amount Rule                  | Used to define a particular condition/rule to validate the approval workflow                                    | Yes           |
| Enter Amount                        | Used to specify a particular amount which will be considered to verify the amount rule                          | Yes           |
| Minimum No. Of Approvals Required   | Used to specify least number of approvals required in a particular approval workflow. The valid values are:     | Yes           |
| Mandatory Level 2 Approval Required | Used to indicate whether to mark Level 2 Approval as mandatory or not                                           |               |
| Minimum No. Of Approvals Required   | Used to specify the least number of approvals required in a particular approval workflow. The valid values are: | Yes           |
| Mandatory Level 2 Approval Required | Used to indicate whether to mark Level 2 Approval as mandatory or not                                           |               |