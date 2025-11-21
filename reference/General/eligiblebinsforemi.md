---
title: Eligible BINs for EMI API v1.0
api:
  file: eligible_bins_emi.json
  operationId: EligibleBINsforEMI
hidden: false
---
The Eligible BINs for EMI API (**eligibleBinsForEMI**) version 1.0 is used only when the merchant needs the EMI feature of PayU. If you are managing card details on your website, this API can tell the issuing bank of the card bin. It also provides the minimum eligible amount for a particular bank.

<Image alt="EMI Eligible BINs Flow" border={false} src="https://files.readme.io/2eaac64-emi_eligible_bins_flow.png" />

You can post a request using any of the following methods:

* **Request without Bank Selection**: This is submitting API without bank name in var3 field.
* **Request with Bank Selection**: This is submitting API with bank name in var3 field so that you will get the details for the specified bank.

<GENERALAPIsEnvironment />

## Request parameters

<Accordion title="Additional information for request parameters" icon="fa-book">
  | Parameter | Description                                                                 |
  | :-------- | :-------------------------------------------------------------------------- |
  | key       | Merchant key provided by PayU                                               |
  | command   | Must be set to "eligibleBinsForEMI" for this API                            |
  | var1      | Parameter type - should be "Bin" for card BIN check or "NET" for Netbanking |
  | var2      | The first 6/8/9 digits of the card when var1=Bin                            |
  | var3      | Optional - Bank name to check eligibility for a specific bank               |
  | hash      | Security hash calculated using merchant key, salt and command               |

  ## Hash Calculation

  Hash for this API is calculated using:

  ```
  sha512(key|command|var1|salt) sha512
  ```

  ## Example Values

  Use the following sample values while trying out the API:

  * `var1`: Bin or NET
  * `var2` (first 6/8/9 digits of the card):
    * **AXIS EMI**: 4453-3410-6587-6437
    * **ICICI EMI**: 4808-5578-4874-1463

  ## Important Notes:

  1. **BIN Length**: For most cards, use the first 6 digits. Some banks may require 8 or 9 digits for accurate identification.

  2. **Bank Selection**:
     * Without bank selection (var3 empty): Get eligibility for any bank matching the BIN
     * With bank selection (var3 populated): Verify if the specific bank offers EMI for the BIN

  3. **Minimum Amount**: The response includes the minimum transaction amount that qualifies for EMI with the identified bank.

  4. **EMI Implementation Flow**:
     * Check BIN eligibility using this API
     * If eligible (isEligible=1), offer EMI option to customer
     * Use bank and minAmount to show appropriate EMI options
     * Ensure transaction amount is ≥ minAmount

  5. **Integration with Payment Flow**: This API is typically called before initiating the payment to determine if EMI should be presented as an option to the customer.
</Accordion>