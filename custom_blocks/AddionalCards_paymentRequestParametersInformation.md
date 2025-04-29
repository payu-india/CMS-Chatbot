---
name: Addional Cards _payment Request Parameters Information
---
<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Parameter
      </th>

      <th style={{ textAlign: "left" }}>
        Reference
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        <Glossary>key</Glossary>
      </td>

      <td style={{ textAlign: "left" }}>
        For more information on how to generate the Key and Salt, refer to any of the following:  

        \- **Production**: [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  

        * **Test**: [Access Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        <Glossary>hash</Glossary>
      </td>

      <td style={{ textAlign: "left" }}>
        Hash logic for **\_payment** API is:\
        sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)\
        For more information about the hash generation process, refer to [Generate Hash](doc:generate-hash-merchant-hosted).  

        * \*Note\*\*: Hash logic for \_payment API version 19:  

        The following hash logic must be used for \_payment API with**api\_version=19**:\
        `key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|udf6\|udf7\|udf8\|udf9\|udf10\|user_token\|offer_key\|offer_auto_apply\|cart_details\|extra_charges\|phone`
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>

      </td>

      <td style={{ textAlign: "left" }}>

      </td>
    </tr>
  </tbody>
</Table>

> 📘 Note:
>
> The following parameters are mandatory for Cross-Border Payments in addition to user-defined parameters specified above:  firstname, lastname, address1, city, state, country and zipcode.
