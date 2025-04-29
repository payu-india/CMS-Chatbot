---
name: Additional _payment Request Params
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

        \- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  

        * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
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
