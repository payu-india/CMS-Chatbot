---
name: Mutual_Funds_Product_JSON
---
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

<HTMLBlock>{`

<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Parameter</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Example</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>type<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Transaction type, must be "mutual_fund"</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"mutual_fund"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>float</code> The transaction amount, must match order amount</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>50000</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>receipt<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Unique PG reference number (max 25 chars)</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"77407"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>mf_member_id<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>numeric</code> Member ID issued by mutual fund platform (5-20 chars)</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"123445"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>mf_user_id<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Unique mutual fund user/client ID (max 10 chars)</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"77407"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>mf_partner<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Mutual fund platform: cams, kfin, bse, nse (max 4 chars)</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"cams"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>mf_investment_type<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Investment type: L (Lump Sum) or S (SIP) (single char)</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"L"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>plan<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Mutual fund plan name</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"GD"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>folio<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Unique mutual fund account identifier</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"12345678"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>option<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Mutual fund plan option</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"G"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>scheme<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Mutual fund type/scheme</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"LT"</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>mf_amc_code<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>string</code> Asset Management Company code (max 5 chars)</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>"UTB"</p></td>
    </tr>
  </tbody>
</table>

`}</HTMLBlock>

    <Accordion title="Validation Rules" icon="fa-code">
    #### Mandatory Field Validations
       - **type**: Must always be `"mutual_fund"`
       - **amount**: Must match the overall order amount and be in paise
       - **receipt**: Must be unique across transactions
       - **mf\_member\_id**: Must be numeric with length between 5-20 characters
       - **mf\_user\_id**: Maximum 10 characters allowed
       - **mf\_partner**: Must be one of: `"cams"`, `"kfin"`, `"bse"`, `"nse"`
       - **mf\_investment\_type**: Only `"L"` (Lump Sum) or `"S"` (SIP) allowed

    #### Optional Field Validations
       - **mf\_amc\_code**: Maximum 5 characters
       - **receipt**: Maximum 25 characters for SIP registration ID
    </Accordion>
  </Accordion>
