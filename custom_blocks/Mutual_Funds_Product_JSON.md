---
name: Mutual_Funds_Product_JSON
---
<Accordion title="Wealth Tech Object (wtParams) Fields" icon="fa-cog">

  <Accordion title="Sample JSON" icon="fa-code">
    ```
    "product": {
        "wtParams": [
          {
            "type": "mutual_fund",
            "plan": "GD",
            "amount": "50000",
            "option": "G",
            "scheme": "LT",
            "receipt": "77407",
            "mf_member_id": "123445",
            "mf_user_id": "77407",
            "mf_partner": "cams",
            "mf_investment_type": "L",
            "mf_amc_code": "UTB"
          }
        ]
      }
    ```
  </Accordion>

  <Accordion title="Wealth Tech object (wtParams) fields Description" icon="fa-cog">
    These parameters are included within the `product` field as a JSON array under the fiedl `wtParams`:

    <Table align={["left","left","left"]}>
      <thead>
        <tr>
          <th style={{ textAlign: "left" }}>
            Parameter
          </th>

          <th style={{ textAlign: "left" }}>
            Description
          </th>

          <th style={{ textAlign: "left" }}>
            Example
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td style={{ textAlign: "left" }}>
            type <br />
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `string` - Transaction type, must be "mutual\_fund"
          </td>

          <td style={{ textAlign: "left" }}>
            `"mutual_fund"`
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            amount <br />
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `float` - The transaction amount, must match order amount
          </td>

          <td style={{ textAlign: "left" }}>
            `50000`
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            receipt <br />
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `string` - Unique PG reference number (max 25 chars)
          </td>

          <td style={{ textAlign: "left" }}>
            `"77407"`
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            mf\_member\_id <br />
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `numeric` - Member ID issued by mutual fund platform (5-20 chars)
          </td>

          <td style={{ textAlign: "left" }}>
            `"123445"`
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            mf\_user\_id <br />
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `string` - Unique mutual fund user/client ID (max 10 chars)
          </td>

          <td style={{ textAlign: "left" }}>
            `"77407"`
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            mf\_partner <br />
            `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `string` - Mutual fund platform: cams, kfin, bse, nse (max 4 chars)
          </td>

          <td style={{ textAlign: "left" }}>
            `"cams"`
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            mf\_investment\_type <br /> `mandatory`
          </td>

          <td style={{ textAlign: "left" }}>
            `string` - Investment type: L (Lump Sum) or S (SIP) (single char)
          </td>

          <td style={{ textAlign: "left" }}>
            `"L"`
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            plan <br />
            `optional`
          </td>

          <td style={{ textAlign: "left" }}>
            `string` - Mutual fund plan name
          </td>

          <td style={{ textAlign: "left" }}>
            `"GD"`
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            folio
            `optional`
          </td>

          <td style={{ textAlign: "left" }}>
            `string` - Unique mutual fund account identifier
          </td>

          <td style={{ textAlign: "left" }}>
            `"12345678"`
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            option <br />
            `optional`
          </td>

          <td style={{ textAlign: "left" }}>
            `string` - Mutual fund plan option
          </td>

          <td style={{ textAlign: "left" }}>
            `"G"`
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            scheme <br />
            `optional`
          </td>

          <td style={{ textAlign: "left" }}>
            `string` - Mutual fund type/scheme
          </td>

          <td style={{ textAlign: "left" }}>
            `"LT"`
          </td>
        </tr>

        <tr>
          <td style={{ textAlign: "left" }}>
            mf\_amc\_code <br />
            `optional`
          </td>

          <td style={{ textAlign: "left" }}>
            `string` - Asset Management Company code (max 5 chars)
          </td>

          <td style={{ textAlign: "left" }}>
            `"UTB"`
          </td>
        </tr>
      </tbody>
    </Table>

    <Accordion title="Validation Rules" icon="fa-code">
      <Accordion title="Mandatory Field Validations" icon="fa-code">
        * **type**: Must always be `"mutual_fund"`
        * **amount**: Must match the overall order amount and be in paise
        * **receipt**: Must be unique across transactions
        * **mf\_member\_id**: Must be numeric with length between 5-20 characters
        * **mf\_user\_id**: Maximum 10 characters allowed
        * **mf\_partner**: Must be one of: `"cams"`, `"kfin"`, `"bse"`, `"nse"`
        * **mf\_investment\_type**: Only `"L"` (Lump Sum) or `"S"` (SIP) allowed
      </Accordion>

      <Accordion title="Optional Field Validations" icon="fa-code">
        * **mf\_amc\_code**: Maximum 5 characters
        * **receipt**: Maximum 25 characters for SIP registration ID

        ***
      </Accordion>
    </Accordion>
  </Accordion>
</Accordion>
