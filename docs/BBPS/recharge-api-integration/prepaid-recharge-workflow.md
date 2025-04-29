---
title: Prepaid Recharge Workflow
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
The following flow diagram illustrates the general workflow for prepaid recharge:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/recharge_api_general_workflow.png)

The following flow diagrams illustrates the technical workflow for Recharge API integration:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/recharge_api_integration_tech_workflow.png)

The Prepaid Recharge workflow involves:

1. Get Category Name using the **Get Biller Categories** API. For more information, refer to [Get Biller Categories API](https://devguide.payu.in/recharge-api-integration/biller-apis-recharge-api-integration/get-biller-categories/).
2. Pass the category name to the **Get All Billers by Category Name** API and get all the updated biller details. For more information, refer to [Get All Billers by Category Name API](https://devguide.payu.in/recharge-api-integration/biller-apis-recharge-api-integration/get-all-billers-by-category-name/).
3. Get all the operator information using the **Get Operator List** API. For more information, refer to [Get Operator List API](https://devguide.payu.in/recharge-api-integration/get-operator-and-circle-apis/get-operator-list/).
4. Get the circle information using the **Get Circle List** API. For more information, refer to [Get Circle List API](https://devguide.payu.in/recharge-api-integration/get-operator-and-circle-apis/get-circle-list-api/).
5. Get all the mobile plans using the **Get Mobile Plans** API. For more information, refer to [Get Mobile Plans API](https://devguide.payu.in/recharge-api-integration/get-operator-and-circle-apis/get-mobile-plans-api/).
6. Call the **Get Operator and Circle Info** API, using the mobile number entered by the customer, to get the circle and operator info. If the circle and operator information are not returned as a response using the API, the customer will need to manually select the operator and circle. For more information, refer to [Get Operator and Circle Info](https://devguide.payu.in/recharge-api-integration/get-operator-and-circle-apis/get-operator-and-circle-info/) API.
7. Validate the mobile number and operator information using the **Bill Payment Validation** API before making the payment. This API is optional. For more information, refer to [Bill Payment Validation API](https://devguide.payu.in/recharge-api-integration/biller-apis-recharge-api-integration/bill-payment-validation-api/).
8. Call the **Bill Payment** API and if the **Bill Paymen**t API returns as pending status in response, use the **Bill Payment Transaction Status** API to check the payment transaction status. For more information, refer to [Bill Payment API](https://devguide.payu.in/recharge-api-integration/biller-apis-recharge-api-integration/bbps-bill-payment-api/) or [Bill Payment Transaction Status API](https://devguide.payu.in/recharge-api-integration/biller-apis-recharge-api-integration/bill-payment-transaction-status/).

## **Customer Journey**

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/06/Recharge_API_Customer_Journey-1024x434.png)