---
name: Key/Hash for General Parameters Description
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

        * **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)

        * **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        <Glossary>hash</Glossary>
      </td>

      <td style={{ textAlign: "left" }}>
        Hash logic for this API is:\
        `sha512(key\|command\|var1\|salt) sha512`
      </td>
    </tr>
  </tbody>
</Table>
