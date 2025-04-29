---
title: Upload Registration Transactions in Bulk
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: >-
    Upload Subscription Registration Transactions in Bulk or Recurring Payment
    Registration Transactions in Bulk
  description: >-
    Learn how to upload registration transactions in bulk using the PayU
    Dashboard. Follow our detailed guide to streamline your recurring payment
    processes efficiently.
  keywords:
    - upload registration transactions
    - ' bulk upload PayU'
    - ' PayU Dashboard guide'
    - ' recurring payments setup'
    - ' registration transactions bulk'
    - ' PayU bulk upload instructions'
    - ' upload transactions CSV'
    - ' PayU recurring billing'
    - ' bulk registration upload'
    - ' recurring payment registration'
    - ' recurring payment registration transactions in Bulk'
  robots: index
next:
  description: ''
---
This section describes the procedure to upload the registration transactions in bulk for collecting recurring payments.

## Prerequisites

* Download the sample file as in below [procedure](#procedure) (Steps 1 to 5) and update it to include the data to be uploaded.
* Ensure that all mandatory fields in the file are filled with the correct details. The columns in the Excel sheet for upload are described in the following table:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Column Name
      </th>

      <th>
        Field Type (Mandatory/ Optional)
      </th>

      <th>
        Character Limit
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Amount
      </td>

      <td>
        Mandatory
      </td>

      <td>
        No Limit
      </td>
    </tr>

    <tr>
      <td>
        Invoice Id
      </td>

      <td>
        Optional
      </td>

      <td>
        16 (Should be unique)
      </td>
    </tr>

    <tr>
      <td>
        Merchant Ref Id
      </td>

      <td>
        Optional
      </td>

      <td>
        50 (should be unique and to support - "^\[A-Za-z0-9@#().+\_;\\\\-\\\\\[\\\\\]\]\*$" )
      </td>
    </tr>

    <tr>
      <td>
        Product Description
      </td>

      <td>
        Mandatory
      </td>

      <td>
        255
      </td>
    </tr>

    <tr>
      <td>
        Customer Name
      </td>

      <td>
        Optional
      </td>

      <td>
        255
      </td>
    </tr>

    <tr>
      <td>
        Customer Email
      </td>

      <td>
        Optional
      </td>

      <td>
        Basic email validations
      </td>
    </tr>

    <tr>
      <td>
        Customer Phone Number
      </td>

      <td>
        Optional
      </td>

      <td>
        Basic phone number validations
      </td>
    </tr>

    <tr>
      <td>
        Validation Period
      </td>

      <td>
        Optional
      </td>

      <td>
        No max limit. Should be numeric 
      </td>
    </tr>

    <tr>
      <td>
        Time Unit
      </td>

      <td>
        Optional
      </td>

      <td>
        The default value is D (days). Other supported values = M (minutes), H (hours)
      </td>
    </tr>

    <tr>
      <td>
        Sendsms
      </td>

      <td>
        Optional
      </td>

      <td>
        Supported value = 0, 1 or empty   

        * \*Note\*\*: To send a SMS, the following is required:  
        * Phone number must be specified
        * **Sendsms**column = 1
        * **Notify via SMS** check box specified in Step 7  is selected
      </td>
    </tr>

    <tr>
      <td>
        Sendemail
      </td>

      <td>
        Optional
      </td>

      <td>
        Supported value = 0, 1 or empty  

        * \*Note\*\*: To send an email, the following is required:  
        * Email ID must be specified
        * **Sendemail** column = 1
        * **Notify via Email** check box specified in Step 7  is selected
      </td>
    </tr>

    <tr>
      <td>
        Customer Address
      </td>

      <td>
        Optional
      </td>

      <td>
        255
      </td>
    </tr>

    <tr>
      <td>
        Cutomer City
      </td>

      <td>
        Optional
      </td>

      <td>
        255
      </td>
    </tr>

    <tr>
      <td>
        Customer State
      </td>

      <td>
        Optional
      </td>

      <td>
        255
      </td>
    </tr>

    <tr>
      <td>
        Customer Country
      </td>

      <td>
        Optional
      </td>

      <td>
        255
      </td>
    </tr>

    <tr>
      <td>
        Zip code
      </td>

      <td>
        Optional
      </td>

      <td>
        255
      </td>
    </tr>

    <tr>
      <td>
        Udf 1
      </td>

      <td>
        Optional
      </td>

      <td>
        255
      </td>
    </tr>

    <tr>
      <td>
        Udf 2
      </td>

      <td>
        Optional
      </td>

      <td>
        255
      </td>
    </tr>

    <tr>
      <td>
        Udf 3
      </td>

      <td>
        Optional
      </td>

      <td>
        255
      </td>
    </tr>

    <tr>
      <td>
        Udf 4
      </td>

      <td>
        Optional
      </td>

      <td>
        255
      </td>
    </tr>

    <tr>
      <td>
        Udf 5
      </td>

      <td>
        Optional
      </td>

      <td>
        255
      </td>
    </tr>

    <tr>
      <td>
        IsSiEnabled
      </td>

      <td>
        Mandatory
      </td>

      <td>
        Supported value = 0, 1 or empty. If the value = 1 only then SI bulk upload link will be generated and the SI-related parameters will be  mandatory
      </td>
    </tr>

    <tr>
      <td>
        Billing amount
      </td>

      <td>
        Mandatory (if isSienabled =1)
      </td>

      <td>
        Minimum value = 1
      </td>
    </tr>

    <tr>
      <td>
        Billing cycle
      </td>

      <td>
        Mandatory (if isSienabled =1)
      </td>

      <td>
        Value should be monthly, daily, weekly, adhoc, yearly
      </td>
    </tr>

    <tr>
      <td>
        Billing interval
      </td>

      <td>
        Mandatory   a. if isSienabled =1  b. if billing cycle ≠ adhoc
      </td>

      <td>
        For adhoc cycle, it is not mandatory, for other billing cycles, it is mandatory
      </td>
    </tr>

    <tr>
      <td>
        Start date
      </td>

      <td>
        Mandatory (if isSienabled =1)
      </td>

      <td>
        DD/MM/YYYY format
      </td>
    </tr>

    <tr>
      <td>
        End date
      </td>

      <td>
        Mandatory (if isSienabled =1)
      </td>

      <td>
        DD/MM/YYYY format
      </td>
    </tr>

    <tr>
      <td>
        Payment Method
      </td>

      <td>
        Mandatory (if isSienabled =1)
      </td>

      <td>
        `creditcard\|debitcard\|upi\|enach`
      </td>
    </tr>
  </tbody>
</Table>

* Ensure that your bulk upload files are in the CSV format, as this is the only supported file type. 
* The upload file size should not exceed 5 MB to ensure smooth processing. 
* Each batch can contain up to 60,000 records (approximately), which is the maximum number of records processed in a single batch.

## Procedure

1. Login to the Merchant Dashboard. For more information, refer to [Log in to Dashboard](https://docs.payu.in/docs/log-in-to-dashboard). 
2. Navigate to **Subscriptions.** 

The *Subscriptions Overview* page is displayed on the right-pane. 

<Image align="center" className="border" border={true} src="https://files.readme.io/b6a07fd76749d355187ca08a22fdbba9ed1b34147b404b8584e1270e99886f6d-bulk_upload_button.png" />

3. Click **Bulk Upload** at the top-right corner. 

The *Bulk Upload* pop-up page is displayed. 

![](https://files.readme.io/16f626114a4d368f0a1b88113810cadf8875f013df740549c2d14af9f94a9cab-Screenshot_2024-09-16_at_11.03.44_AM.png) 

4. Select **Registration** to upload the registration transactions. 
5. Click **Continue.** 

The **Bulk Upload Registration** screen is displayed. 

![](https://files.readme.io/ff5c2bfc330bdfa1089bcc3897269318decb0d618e678222f2fb24a8051ae68c-bulk_upload_popup-page_details.png) 

6. Enter a batch description in the **Batch Description** to identify this particular upload. 
7. Select the following check boxes if you wish to notify the customer: 

* Email 
* SMS 

8. Click **Continue**. 

> **Note:** Download the sample file for registration of mandate using the **Download** button and update to include the registration transactions. For more information, refer to [Prerequisites](#prerequistes). 

9. Click **Choose file** and select the file containing all the mandates details that need to be created.  
10. Click **Upload.** 

> **Note:** After you submit a batch file, it will be picked up for processing within 60 minutes. 

After uploading the file, the system will automatically check for discrepancies. If there’s an issue, an error message is displayed on the screen. 

![](https://files.readme.io/51ee71e5b3f7b708604844bef0215f970da88238ae368f8da1af089ead9becdf-bulk_upload_popup-page_errors.png) 

After your file is successfully uploaded, a message similar to the following screenshot is displayed and then you will be redirected to the **Bulk Upload** listing screen. 

![](https://files.readme.io/f13ff94f11a504ea8ac1b552c7aaa9674ea6bac69de20e37ab8788501492099c-bulk_upload_popup-page_sucess.png) 

A record is added with the status as “Partially Processed” to the **Registration** tab sub-tab under the **Bulk Upload** tab similar to the following screenshot. 

<Image align="center" className="border" border={true} src="https://files.readme.io/35cc9bc263042e23420dafde87d37f6b212ecce5fd7d6547a4c471e1c5aba69f-bulk_upload_listing.png" />
