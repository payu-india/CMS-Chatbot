---
title: Merchant Hosted Checkout Integration
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Merchant Hosted Checkout Integration for Merchant Wallet
  description: ''
  robots: index
next:
  description: ''
---
With the Merchant Hosted Checkout integration, the entire payment experience can be controlled by merchants and PayU provides APIs to power this checkout experience. In this section, we will describe which APIs will be required by Merchant to provide Wallet as a payment instrument on Merchant check-out

To access any of these APIs, the following details needs to be posted with API:

1. Correct Mobile Number of the user
2. Bank code (provided during onboarding)
3. Wallet URN (for debit calls)

### Steps to integrate:

1. [Check balance](#step-1-check-balance)
2. [Initiate the payment](#initiate-the-payment)
3. [Check the response from PayU](#check-the-response-from-payu)

## Step 1: Check balance

Check the balance of the wallet using the **Fetch Balance** API before you can initiate payment. For more  information, refer to [Fetch Balance API](ref:fetch-balance-api).

## Step 2: Initiate the payment

### HTML Code

```html
<body>
<form action='https://test.payu.in/_payment' method='post'>
<input type="hidden" name="key" value="JP***g" />
<input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
<input type="hidden" name="productinfo" value="iPhone" />
<input type="hidden" name="amount" value="10" />
<input type="hidden" name="email" value="test@gmail.com" />
<input type="hidden" name="firstname" value="Ashish" />
<input type="hidden" name="lastname" value="Kumar" />
<input type="hidden" name="walletUrn" value="100000" />
<input type="hidden" name="pg" value="CLW" />
<input type="hidden" name="bankcode" value="PAY" />
<input type="hidden" name="surl" value="your own success url" />
<input type="hidden" name="furl" value="your own failure url" />
<input type="hidden" name="phone" value="9988776655” />
<input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
<input type="submit" value="submit"> </form>
</body>
</html>
```

### Request Parameters and Check Response

Along with the mandatory parameters mentioned in <a href="https://docs.payu.in/reference/_payment-merchant-hosted" target="_blank">Collect Payments API</a>, you must post the following parameters for the wallet.

<Table align={["left","left","left"]}>
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
        walletUrn
        **mandatory for Closed Loop Wallets**
      </td>

      <td>
        `String` It is the Unique Registration Number of the customer to identify them.
      </td>

      <td>
        100000
      </td>
    </tr>

    <tr>
      <td>
        phone
        **mandatory**
      </td>

      <td>
        `String` The phone number of the customer that was registered with the merchant.
      </td>

      <td>
        9876543210
      </td>
    </tr>

    <tr>
      <td>
        pg
        **mandatory**
      </td>

      <td>
        `String` It defines the payment category using the Merchant Hosted Checkout integration. For a Closed Loop Wallet payment, "CLW" must be specified in the **pg** parameter.
      </td>

      <td>
        CLW
      </td>
    </tr>

    <tr>
      <td>
        bankcode
        **mandatory**
      </td>

      <td>
        `String` The merchant must post this parameter with the merchant's corresponding bank code value in it.**Note**: If you are integrating Closed Loop Wallet, you need to get the bankcode from your Key Account Manager (KAM).
      </td>

      <td>
        PAY
      </td>
    </tr>
  </tbody>
</Table>

### Sample Request

```curl
curl -X POST "https://test.payu.in/_payment-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d"key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&walletUrn=10000&pg=CLW&bankcode=PAY&surl=https://ordereasy.gofrugal.com/ecommerce/v1/payu-loading/&furl=https://ordereasy.gofrugal.com/ecommerce/v1/payu-loading&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```

## Step 3: Check the response from PayU

The following is the sample response. For the description of the response parameters, refer to response parameter description in [Additional Info for Payment APIs](ref:backup-of-payment-apis). This is a formatted sample response for a “test” payment wallet.

```
Array  
(  
    [mihpayid] => 403993715527518775  
    [mode] => CLW  
    [status] => success  
    [unmappedstatus] => captured  
    [key] => J**\***g  
    [txnid] => HC13glcAkssIkl  
    [amount] => 10.00  
    [discount] => 0.00  
    [net_amount_debit] => 10  
    [addedon] => 2022-10-21 17:45:24  
    [productinfo] => iPhone  
    [firstname] => Ashish  
    [lastname] =>  
    [address1] =>  
    [address2] =>  
    [city] =>  
    [state] =>  
    [country] =>  
    [zipcode] =>  
    [email] => [test@gmail.com](mailto:test@gmail.com)  
    [phone] => 9876543210  
    [udf1] =>  
    [udf2] =>  
    [udf3] =>  
    [udf4] =>  
    [udf5] =>  
    [udf6] =>  
    [udf7] =>  
    [udf8] =>  
    [udf9] =>  
    [udf10] =>  
    [hash] => 007435a716982c7f5eec5cff95701f65eb1bdbff8f852e461224e3b5e17126ad26bb3a3ffdb95cded6a87d3515fe86fc58925cad024595a4a6825adfed2dc436  
    [field1] =>  
    [field2] =>  
    [field3] =>  
    [field4] =>  
    [field5] =>  
    [field6] =>  
    [field7] =>  
    [field8] =>  
    [field9] => Transaction Completed Successfully  
    [payment_source] => payu  
    [PG_TYPE] => CLW-PG  
    [bank_ref_num] => 540898ed-72e7-40a8-a96e-f17de621cbb4  
    [bankcode] => CLW  
    [error] => E000  
    [error_Message] => No Error  
    [splitInfo] => {"splitStatus":"splitNotReceived","splitSegments":\[]}  
)
```

<br />
