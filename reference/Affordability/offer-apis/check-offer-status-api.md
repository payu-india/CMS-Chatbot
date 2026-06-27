---
title: Check Offer Status API
excerpt: 'API Command: **check\_offer\_status**'
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Check Offer Status API (**check\_offer\_status**) can be used for the following scenarios:

- [Check Merchant Specific Offers](https://devguide.payu.in/api/integration-apis/offers/check_offer_status#merchant)
- [Check Card Specific Offers](https://devguide.payu.in/api/integration-apis/offers/check_offer_status#card)

**Environment**

<table style="border:0.1rem solid rgb(242, 242, 242);"><tbody><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Test Environment</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">https://test.payu.in/merchant/postservice.php?form=2</td></tr><tr><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">Production Environment</td><td style="border:0.1rem solid rgb(242, 242, 242);padding:0.8em;">https://info.payu.in/merchant/postservice?form=2</td></tr></tbody></table>

## Check Merchant Specific Offers

The Check Offer Status API is used to check the status of an offer for a particular merchant when all the details are passed. The return parameters are status, msg, discount/error\_code, category, offer\_key, offer\_type (instant or cashback), offer\_availed\_count and offer\_remaining\_count.

### Request Parameters

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Sample Value**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        var1
        **mandatory**
      </td>

      <td>
        The offer Key must be specified in this parameter.
      </td>

      <td>
        offer\@123
      </td>
    </tr>

    <tr>
      <td>
        var2<br />**mandatory**
      </td>

      <td>
        The payment amount of the particular transaction must be specified in this parameter.
      </td>

      <td>
        10000
      </td>
    </tr>

    <tr>
      <td>
        var3<br />**optional**
      </td>

      <td>
        This parameter must contain the payment category that the merchant wants the user to see by default on the PayU’s payment page.
      </td>

      <td>
        CC
      </td>
    </tr>

    <tr>
      <td>
        var4<br />**optional**
      </td>

      <td>
        This parameter must contain the bank code.
      </td>

      <td>
        AMEX
      </td>
    </tr>

    <tr>
      <td>
        var5<br />**mandatory**
      </td>

      <td>
        This parameter must contain the card number.
      </td>

      <td>
        5432112345678901
      </td>
    </tr>

    <tr>
      <td>
        var6<br />**optional**
      </td>

      <td>
        This parameter must contain name of the customer as on the card.
      </td>

      <td>
        Nitesh
      </td>
    </tr>

    <tr>
      <td>
        var7<br />**optional**
      </td>

      <td>
        This parameter must contain the phone number of the customer.
      </td>

      <td>
        9988776655
      </td>
    </tr>

    <tr>
      <td>
        var8<br />**optional**
      </td>

      <td>
        This parameter must contain email address of the customer.
      </td>

      <td>
        [abc@xyz.com](mailto:abc@xyz.com)
      </td>
    </tr>
  </tbody>
</Table>

Error Codes:

- ‘INVALID\_OFFER’=>’E001′
- ‘INVALID\_PAYMENT\_METHOD’=>’E002’

**In the Output:**<br />Parameter ‘status’ = 1, means offer is valid<br />Parameter ‘status’ = 0, means offer is invalid

### Sample Request

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

"key=JP***g&command=check_offer_status&var1=offer1@7788&var2=1000&var3=CC&var4=CC&var5=5123456789012346&var6=test&var7=987654321&var8=tesmm@jm.com&hash=862503800fbd33ac040473bc20e1b6c33b4a575893c0ec48813122f6971e8af2c24d05f1e3da32bc00e416a179f0ae4c46d330141b39d68ba22ff250167d2eb0"
```

### Sample Response

<Callout icon="📘" theme="info">
  ### Note:

  In the response, the category will be the passed Category.
</Callout>

#### Success Scenario

If the offer is valid:

```plaintext
{
      "status": 1,
      "msg": "Valid offer",
      "discount": 100,
      "category": "creditcard",
      "offer_key": "offer1@7788",
      "offer_type": "instant",
      "offer_availed_count": 0,
      "offer_remaining_count": 0
}
```

#### Failure Scenario

- If the offer has expired:

If the offer has expired

```plaintext
Array 
(
[status] => 0
[msg] => Offer expired. 
[error_code] => E001
[category] => creditcard 
[offer_key] => newoffer1@5686 
[offer_type] => instant 
[offer_availed_count] => Unknown 
[offer_remaining_count] => Unknown
)
```

- If the card limit is exhausted:

If the card limit is exhausted

```plaintext
Array 
(
[status] => 0
[msg] => Offer Exhausted 
[error_code] => E001
[category] => creditcard 
[offer_key] => newoffer1@568 
[offer_type] => Unknown 
[offer_availed_count] => Unknown 
[offer_remaining_count => Unknown
)
```

- If the offer\_key is invalid:

If the offer\_key is invalid

```plaintext
Array 
(
[status] => 0
[msg] => Invalid offer Key 
[error_code] => E001
[offer_key] => newoffer1@568 
[offer_type] => Unknown 
[offer_availed_count] => Unknown 
[offer_remaining_count] => Unknown
)
```

## Check Card Specific Offers

The check\_offer\_status API is used to check the status of an offer when only the parameters Offer Key and card number are passed as input. This API is used to check the offer status when the offer is created using bin only. In this case, we can depict that the offer has been created for which category (like CC, DC, NB, or EMI). Hence, for using this API, you need to pass the Offer Key and Card Number in var1 and var5 fields as inputs and leave the remaining fields empty.

The return parameters are status, msg, error\_code (In case of error), category, offer\_key, offer\_type (instant/cashback), offer\_availed\_count, ‘offer\_remaining\_count’.

### Request Parameters

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        var1
        **mandatory**
      </td>

      <td>
        This parameter contains the Offer Key of the merchant.
      </td>

      <td>
        offer\@123
      </td>
    </tr>

    <tr>
      <td>
        var2<br />**mandatory**
      </td>

      <td>
        This parameter must contain the amount.
      </td>

      <td>
        10000
      </td>
    </tr>

    <tr>
      <td>
        var3<br />**optional**
      </td>

      <td>
        This parameter must be left blank.
      </td>

      <td>
        –
      </td>
    </tr>

    <tr>
      <td>
        var4<br />**optional**
      </td>

      <td>
        This parameter must be left blank.
      </td>

      <td>
        –
      </td>
    </tr>

    <tr>
      <td>
        var5<br />**mandatory**
      </td>

      <td>
        This parameter must contain the card number.
      </td>

      <td>
        5432112345678901
      </td>
    </tr>
  </tbody>
</Table>

Error Codes

- ‘INVALID\_OFFER’=>’E001′
- ‘INVALID\_PAYMENT\_METHOD’=>’E002’

**In the Output:**

- Parameter ‘status’ = 1, means offer is valid
- Parameter ‘status’ = 0, means offer is invalid

### Sample Request

```curl
curl -X POST "https://test.payu.in/merchant/postservice?form=2"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

"key=JP***g&command=check_offer_status&var1=offer1@7788&var2=&var3=&var4=&var5=512345&hash=862503800fbd33ac040473bc20e1b6c33b4a575893c0ec48813122f6971e8af2c24d05f1e3da32bc00e416a179f0ae4c46d330141b39d68ba22ff250167d2eb0"
```

### Sample Response

<Callout icon="📘" theme="info">
  ### Note:

  In the response, the category will be the passed Category.
</Callout>

#### Success Scenario

If the offer is valid:

```plaintext
{
      "status": 1,
      "msg": "Valid offer",
      "discount": 100,
      "category": "creditcard",
      "offer_key": "offer1@7788",
      "offer_type": "instant",
      "offer_availed_count": 0,
      "offer_remaining_count": 0
}
```

#### Failure Scenario

- If the offer has expired:

If the offer has expired

```plaintext
Array 
(
[status] => 0
[msg] => Offer expired. 
[error_code] => E001
[category] => creditcard 
[offer_key] => newoffer1@5686 
[offer_type] => instant 
[offer_availed_count] => Unknown 
[offer_remaining_count] => Unknown
)
```

- If the card limit is exhausted:

If the card limit is exhausted

```plaintext
Array 
(
[status] => 0
[msg] => Offer Exhausted 
[error_code] => E001
[category] => creditcard 
[offer_key] => newoffer1@568 
[offer_type] => Unknown 
[offer_availed_count] => Unknown 
[offer_remaining_count => Unknown
)
```

- If the offer\_key is invalid:

If the offer\_key is invalid

```plaintext
Array 
(
[status] => 0
[msg] => Invalid offer Key 
[error_code] => E001
[offer_key] => newoffer1@568 
[offer_type] => Unknown 
[offer_availed_count] => Unknown 
[offer_remaining_count] => Unknown
)
```

<br />
