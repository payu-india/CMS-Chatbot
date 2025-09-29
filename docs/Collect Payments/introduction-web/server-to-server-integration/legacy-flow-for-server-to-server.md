---
title: Legacy Flow for Server-to-Server
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
The integration allows merchants to redirect to the bank page directly from their checkout page and let customers complete the transaction.

### Steps to Integrate

1. [Step 1: Initiate payment request with PayU](#step-1-initiate-payment-request-with-PayU)
2. [Step 2: Redirect the Customer](#step2-redirect-the-customer)
3. [Step 3: Check the response from PayU](#step-3-check-the-payment-response-from-payu)

## Step 1: Initiate Payment Request with PayU

The first request from you to PayU with the required transaction mandatory/ optional parameters. This needs to be a server-to-server cURL call request.

### Request Parameters

Some of the parameters are mandatory for S2S integration, and a few are optional. In addition to the parameters listed in the [Collect Payment API - Server-to-Server](ref:_payment_server_to_server) you need to include the following parameter:

| **Parameter**  | **Description**                                                       | **Example** |
| -------------- | --------------------------------------------------------------------- | ----------- |
| txn\_s2s\_flow | This parameter must be passed with the value as 1 for legacy S2S flow | 1           |

Collect the response in the [Collect Payment API - Server-to-Server](ref:_payment_server_to_server) under API Reference. The response for the S2S payment request is not similar to Merchant Hosted or PayU Hosted Checkout. For description of response parameters, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis#response-for-initial-server-to-server-request).

## Step 2: Redirect the Customer

Redirect the customer to the bank page using the **post\_data** field of **result** parameter the as received in [Step 1](#Initiate-payment-request-with-payu). 

## **Step 3: Check Response from PayU**

This will be a call back on the URL provided by you.

### Response Parameters

The parameters in the response for similar for all the S2S flows. For more information, refer to the [Additional Info for Payment APIs](ref:backup-of-payment-apis)

The final response is similar to the following:

```plaintext
{ 
    "mihpayid" :  "16331433547" 
    "mode" :  "DC" 
    "status" :  "success" 
    "unmappedstatus" :  "captured" 
    "key" :  "smsplus" 
    "txnid" :  "payuTestTransaction5700849" 
    "amount" :  "1.00" 
    "cardCategory" :  "domestic" 
    "discount" :  "0.00" 
    "net_amount_debit" :  "1.00" 
    "addedon" :  "2022-12-03 15:03:08" 
    "productinfo" :  "Product Info" 
    "firstname" :  "Ashish" 
    "lastname" :  "" 
    "address1" :  "" 
    "address2" :  "" 
    "city" :  "" 
    "state" :  "" 
    "country" : ""  
    "zipcode" :  "" 
    "email" :  "test@payu.in" 
    "phone" :  "9876543210" 
    "udf1" :  "" 
    "udf2" :  "" 
    "udf3" :  "" 
    "udf4" :  "" 
    "udf5" :  "" 
    "udf6" :  "" 
    "udf7" :  "" 
    "udf8" :  "" 
    "udf9" :  "" 
    "udf10" :  "" 
    "hash" :  "6586bb33ed936d07f866cfeb42b9af99e9408270bd31c722ab3a11e61f6b6581cee3cd4f1b8b4aec3a6695c764e5cd76597832735e1e924f2ac0defbd6b3b68f" 
    "field1" :  "" 
    "field2" :  "" 
    "field3" :  "" 
    "field4" :  "" 
    "field5" :  "" 
    "field6" :  "" 
    "field7" :  "AUTHPOSITIVE" 
    "field8" :  "" 
    "field9" :  "Success Transaction" 
    "payment_source" :  "payuS2S" 
    "PG_TYPE" :  "DC-PG" 
    "bank_ref_num" :   
    "bankcode" :  "VISA" 
    "error" :  "E000" 
    "error_Message" : "success"  
    "cardnum" :  XXXXXXXXXXXX8811 
    "cardhash" :  "This field is no longer supported in postback params." 
    "issuing_bank" :  "UBI" 
    "card_type" :  "VISA" 
} 
```

## Decoupled Flow over Redirect Experience

### Step 1: Initiate Payment Request with PayU

The merchant initiates PayU with the required transaction mandatory or optional parameters. This needs to be a server-to-server curl call request. URL, parameters, and descriptions are listed in the following tables.

#### Endpoint

<table style={{border:"0.1rem solid rgb(242, 242, 242)"}}><tbody><tr><td style={{border: "0.1rem solid rgb(242, 242, 242)", padding:"0.8em"}}>Test</td><td style={{border: "0.1rem solid rgb(242, 242, 242)", padding:"0.8em"}}>https://test.payu.in/_payment</td></tr><tr><td style={{border: "0.1rem solid rgb(242, 242, 242)", padding:"0.8em"}}>Production</td><td style={{border: "0.1rem solid rgb(242, 242, 242)", padding:"0.8em"}}>https://secure.payu.in/_payment</td></tr></tbody></table>

#### Request Parameters

Some of the parameters are mandatory for S2S integration, and a few are optional. In addition to the parameters listed in the [Collect Payment API - Server-to-Server](ref:_payment_server_to_server) you need to include the following parameters:

| **Parameter**                 | **Description**                                                                            | **Example** |
| ----------------------------- | ------------------------------------------------------------------------------------------ | ----------- |
| txn\_s2s\_flow  **mandatory** | `String`  This parameter must be passed with the value as **1** for Legacy Decoupled flow. | 1           |
| auth\_only  **mandatory**     | `String` This parameter must be passed with the value as 1 for this parameter.             | 1           |

### Step 2: Redirect the Customer

Basis a successful response of the authentication API, you need to redirect the user to the bank page using **acsTemplate**.  This API specifies the response that is posted to `termurl` after the authentication for the transaction has been processed.

> 📘 Notes:
>
> * All callbacks POST form data on the merchant’s `termurl` that is passed in Initiate Transaction API. 
> * Validation of the response happens on the basis of the hash value being returned in the hash value of the response.

#### Request Parameters

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        rawBankData
        **mandatory**
      </td>

      <td>
        `String` This parameter contains the raw response that is received from bank after authentication. The response is urlencoded and in query string format.
      </td>
    </tr>

    <tr>
      <td>
        referenceId\
        **mandatory**
      </td>

      <td>
        `String` This parameter contains the reference id being returned for the transaction
      </td>
    </tr>

    <tr>
      <td>
        bankData\
        **mandatory**
      </td>

      <td>
        `JSON` This parameter contains the JSON string that is to be used for authorization call.This parameter is received in case of successful OTP submission of decoupled transactions. The postToBank contains messageDigest and pares that is to be posted back for authorization. For more information on the fields in this JSON, refer to bankData [JSON Fields Description](#bankdata-json-fields-description).
      </td>
    </tr>

    <tr>
      <td>
        authenticationStatus\
        **mandatory**
      </td>

      <td>
        `String` This parameter contains the authentication status of the transaction
      </td>
    </tr>

    <tr>
      <td>
        hash\
        **mandatory**
      </td>

      <td>
        `String` This parameter contains the calculated hash of the data that is posted to the merchant. For security purpose it is recommended to validate the hash value before consuming the response
      </td>
    </tr>
  </tbody>
</Table>

**bankData JSON Fields Description**

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Applicable for EMV 3DS**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        cres
      </td>

      <td>
        `String` This field contains the Base64 encoded value received from ACS as part of the authentication response.
      </td>

      <td>
        Yes
      </td>
    </tr>

    <tr>
      <td>
        referenceId\
        **mandatory**
      </td>

      <td>
        `String` This field is returned in case of decoupled flow. This field contains the reference id for the transaction
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        messageDigest\
        **mandatory**
      </td>

      <td>
        `String` This field is returned in case of decoupled flow. This field contains the MD value being returned by the bank.
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        pares\
        **mandatory**
      </td>

      <td>
        `String` This field is returned in case of decoupled flow. This field contains the pares being returned by the bank
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        additionalInfo\
        **mandatory**
      </td>

      <td>
        `String` This field is returned in case of decoupled flow. This field contains the data that is being used for the gateways that do not return pares.
      </td>

      <td>
         
      </td>
    </tr>

    <tr>
      <td>
        authorizationUrl\
        **mandatory**
      </td>

      <td>
         `String` This integration document assumes that you have opt-ed out for the particular configuration. The authorization URL in legacy integrations are present basis the config at PayU. Please reach out to [integration@payu.in](mailto:integration@payu.in) to know more about.
      </td>

      <td>
         
      </td>
    </tr>
  </tbody>
</Table>

#### Sample Response

```plaintext
{ 
    "rawBankData" : "" 
    "referenceId" : "d78a00cef2b413e9969d122c7d8899f5" 
    "bankData" : "eyJyZWZlcmVuY2VJZCI6ImQ3OGEwMGNlZjJiNDEzZTk5NjlkMTIyYzdkODg5OWY1IiwibWVzc2FnZURpZ2VzdCI6ImMyZTllNDU2MDM3ZjAzM2U1Y2MzZDdiNmU1NTYxODlhNzgwNThjNjFjZjZiNWVkNzM4MWU4ZTM3MWQyZjQ5NGUxNjEwMjU1YzczNjk1MjA5NGM1NmU2MTFjOGUyNTEwOHwwNjQyMmY4MDQwZGVlOTkzNmNlNTJiNGM1Y2ZiNzgyNjY3MzMxY2RmIiwicGFyZXMiOiJlTnJWbWRtU284aTJwbCtsck02bHJEWXpnbTFSWWNZOGlIa1UzREhQUW9BWW43NkppTXlzM0xtcno5QVhiZDB5azhubDRNc1g3cjdXXC96bis1cFJqbHJGMmxzeGo5djZtWnRNVUZkbHZWZnJuN3dtR2dsR0VaSDljd1NUN0EwVkk2QThDdXlaXC9nRENFNVJHR3BCQUJcL1wvNytabEJXTm4wMitDeWROVXMyVGxYXC9lSWYrQWY0RGZnTytcL3oyTmowa1pQVjd2YjFFeTBKTDJqaElJZWNYZWdHOVwvMzdwc2xOaDNHSUpKbEFBeEFrUVFFTVRmZ0tcL3FOK0N2OXNiOFVacE9oN2NxZmRjZDdxV3pMaExzNEtyV0hCUjJIS1RDNXFhejBwOXZ3TWNkYjJuMHl0NWhFRDV0Z1wvQnZJUDVQR1BzbmNwcitySDk3ZnBpanVuNCtiVU1RK0FiOFhQRjJqc3lZUFpMOUhjSE9GalwvK3ZXWGJzMzlrNXgzbk1cLzRvdndGXC8rZmFNSHVcL2dUeDhVQksrbjdiUDJ6Ym1cL3Y3MnE3dDk4d3RBMzRMUCtiWHBGcjNsNkQ5NkFiNlczSkZxV2Q0cWlhSVkzS1VvSUt0dVRLcHY2OFRtZjlmT1d0eXlwM3NGeldEOStQMXRSYmRHUDFhdnNQbHo5MTRvMzRNTVY0SFBxM3RcL3NxbmljblkzWmIxdlhQcVlcL2Z5OWZyK2NcL0FXQmQxMytzeURcLzZzUURnODBFQWtBVE9HOUtwS3Y3ajk2OVdXU285OHY1XC8xSXlKSHYyalNxSzJPcUxYdVVEVTdGWDI2VzhcL2ZQczdNNDcxWVFrQ0xJNzU0elQxUndLaGp6OCtha0FFd2s2YndOOGJcL2VuSlwvanU5XC9PcnNPRVZcL1RHVUVmWFR3aTZIM055dkxzNDhWa2YzbVd0S2Z2XC9cL0g5eWhncXlLYlh2OG4zWDN2Nm1jTDMrMTVVVHRuNzAzTE5wZFpnSThrTCsreVZvWUVRTlo2TXVMQit1ZjNkbDkzdmdFXC9cL1B2bVwvTmRNXC9UUWlYemRTbFJnTldiS0VmWWpiUkM2TFVwUmQxVWNDUzRDekhkclZmS3hneFc0WTdaZCtGOEhla0Q5RDBGYkNjTHFaMWtHXC9Pc0lJUnpKbDhEWmlGXC8wd25HaUhKYWJ1Y3p6MEZmXC9KcGZLUXVRMU5vbkxVdTFrcmNrQzdFTVF0anEzT2VDSWRpRnhzaHlqcFJ1SG1GTlJrMVwvWVUzaGdubEZmYkZmY2ZvUXRKNXNHQ21qVkVDbE94N1ZWRmlhMHpvWUJOdkJHM3NDMUdPZ2ZyMXZhVjNKR1I3NjFKbjFKek1PU3R2VjNRYXpGc1ViY3FTSEtPZm9rYUwzRysrYjdnZEk2K3J2ZnU2WnBQbmFCSHR6dkdZUVI1cGRkdXFKNUx5bkF4WXRQTDBFUWpGK1dLWmhkNWxLY1d6c3ZhSjQweGtlbGNtSVU3Qkc1RkJ1eGlNRWJJZ0Izc25xYk52ZXF2OVBybm56K3RtRzh6Y3N2MnJ4bTRZeURKUnFcL29xOFJrNDZ2S3o2VjdaaVJWa25pa1poaUtpQXBxbFdpcWtFeEprTzc0Q0s2bW5xa3VBUXBEUWdXOVEybDAwUXhsVXdua0N0S1VPZkVVUzhPcU9hMk1HYkNlYVFyY0tudnV3V2txTlFrVTVISk1zWEplMHpxbXd5MHFBMzdWcld2bmRlMFIyTFFjUDZ3MjZiQXlGZG9sN3ZoSjRyVTJlWVRQQUhZTDg2NGRNYXc5Zzd2MWpHRjBrdytxcFF2Tm95bFZGZHZ3bWNCY0VicmFFdnZRYVVOckphNDlFc1I3eGwxU21DQlhLRFl0cWpXVjhTdTRuNytIV3F2bnI3dHByQng5MWgwXC8xXC9HUktvSWJlM3c4NDBjZmlVbzNFQlQ3Y2hrNW5LdlMwcGZ2MUtvNFB0OEhkN2xNNEJKTU9tNWpEa3IrYWhNNFZOUHFxcVd1M05kNDNGanFLWnRneTlvMnpRUStOcW9XdDdMcjV6V0ZwWW9qRkxVMlFMdzlkTGhjcGJcL0doMXBYMzNhMXMxMVRxTEIxaEw0R0paMWJ1SEQ3aUx0MkRvOXpybXhwWmMxQXZ2V2hWQzZKUnBrY1Rac1VXeFNjUWJIbmRiTm56akpOYVFHZFJYZG1kYXZidkNuS1RjZlR3YXp1YmwrQ1JrSGVqb2Z3U3VnWnZ0TzNUdDZTRmFCbGVhbjlHOGVodExEUndYcWRESzNxWDRObWd1cVRqaUJaTDEyVGhBU3ZuYTk2SVFJU2JpZEFnM0ZYd1Fxam5QTGFESEZxWUNaeWRBYXdNclwvSjY5U05cL2RXbXhrcVZ2THNEc3hJN3crWExVZXRNRWFRS3huekJZNStHMVwvQndCYko5VVJmMEFwRXdzYzE3alwvbU9uSklieE1lc3VqVmNnNmc1SHJzVFUxelJKYXN5aWJ1NVJyT25VS29LMk9VQ0lIZURkNWxlQ3BOaEUxK0ZRRUs0SXd6bzlVd2NxSzgreU1DeEdtbVNpVVBiQlI2QU5Gd0VCRzNvSWgrNkl5bkd4aHlST09OamVoUTI2UFhrU09XQzVZbUQ2bXdsRW9ONWZqT0p5a3d6NFpDSmN4bHdGQlhwRE9VUmExSHdzVXF0SDNPWGNpdEhBNnZKcUJTMWloXC96YklFMVRSY3IzMVB1WXFmMTdXYlBucEpMMGpXbk5mZU1zU1JFNzZpN2htc2czZGJnbkVOWFBPZVM4dzg2VkZsS1lKZ3pqa3lYcHcrS0tTdXJUMFZyMVN0aUNYMXNqK0Z0VWg0ZmNjRFhnWTNWTVF3dTMrSkJWQ3VzVGg3bUtwdFwvMlZVcFFSRDhFa3hGQ2xkMmNna1FiZjFxejgwQlRMNFVtS3dUaEZxdDR0UHZnbWFKMVhDb2pTNktrUzQ0bmpZVGhuS29WbVhVdlwvdzY4d1ZmcGpcLzhTcEVVK1JlYkNEMUdEaVhSUmZnb1RQWE1HZExLZlkxTFM1OExuU2wrZXU1VldqWHo4MXBPTStoNkJzalFNMVVoOTBFVGlSYVlzUDJpd042Y2RPUVVNeGdjM2JVeStPRzd4OFl3OUxJT2FRNFFlZm9XU3lsYm1ENU5PeEZWNGU1eDFSZHYzanIrb1BRb2xDcDlVY3l3cHZTUDJCVk5ncVp5NGd3WWxhRlI2dGZZVXI1aTY4eU5MUEtRcDBrZ1d2bmUyQklQVDdrYWRwcUhWdjFUcUdWK2EyQlphTU93S3JNZHNuWEdESXY2TXM3UllJWVNVbldPY3FiKzFndHZIRDRrOVwvZ1JiY0E5bXBDTUxXcFYzbDhjUUIxbTlKQUdxZ1dlSnM5dzl0SmlpN1dmTEdpUU04alRrdHNhVnBJdWUzUDN4aWhZS3p0ZVkwZFh5VHVCYjV5VkxSNjZvWGlTSm8wU2VxNElVXC9Vb1ZFNXJDeXl1dGZCb1BHS0NCTnc3bk9ONlhkZlNhUGNYa1U2WDFlbk9VTWl4blU0dDNwTHVLTGRWRis1cE0zNjM4YnM5aU1pT1pGQnl6azhhZE1tMEdjc3RBMWdTZVdoK1lTXC9EbG9maTgzVTdWTFN6bEo1dEFib3cwbU5kWTVOQjdkdkxidUpiaE5Pcm1vdGI3eU9LMnVvUzFHNmN1ZTFEWTlUUWM1dGVkZE9URU9QdDNsQTZEeko2K0ttcStJZmRpRHlPN2NCNndYVkdkZFRIR29ZUitVUWVnWnprRjM1WnlvNTZMZzZheDVaS2t6d0Y5cXBKcjJJRE9qdnNYOHROdGlWV3NsSklmdUxMZmhLc2dORWxWalR1b0dPdTlTb0NhendWNENsU0tHOXUyUVc0T2haS2RcL3RCMHhRM0M2VXBPS0trSFwvVnJXWUxDaWRDcmlVbzhobDNic29ra3VoUXU0Zjdrcmk4emdPS0hickIzKzFJZ1huNHBFMmNpaXdvV3dVYUZPVDMxSFFCdmNOQm1hTVFFKzB5RHB0UkdyOW90czBuWmJzdm5pMlplbFwvRFM2SVFmUlgwYmpFS1VOSHJ0NlFuTyt5XC8wWlVxMkV5VnphQnZpVGVHaWc3bklZVTJPdGtCWDQ1VyszMU5JNnNRUXRpcGYwTGowMVZ2TXN1QUtPd0p2d0s5S1wvM2ZTTDZBT3c5QnE5MTM2RGRmQlwvUVwvQ3h5THRWUnBPaWtsMHExS2d3TmlEWUVzeHdwNVNjK29KcFFyRXYwcGY2em1xQ2E3TStsMzZMTlwvMk5GcTFpVlV4djBrZUVcL29mWVh0Szlad0szbjVLUGhqNTVCejQ2eWx2M3A1MmJSM2FOSjBnMmhMQTdSY1cxRnloMHVoM2FieFwvUXdjejllVXA4dFhDYlRWYTR1VWxSc3dQMlZcL0ZNdEhPamRtcWZVZytTNjBmWFwvK3MwMWh1VlE5dSsxRlhcLzcrT0xxZU1WXC84N21aZStaTDc0a1BsejNpU1NhNTRVWURBVFljVUhBZmhPNjkyMisxS1RBVWFmTXZQd1JBK0dKTTZOY2kyZ0ZtWlFvSjRzWDJNNmRtNGRQdkNrd2dLb0lITkJ6Qm9ucjJLMm41bXlhYmE5OGlhNFBRaTU1NFJaem1kV0J0emFsUzBybnpDbEZabkZyK0pTcmU0QTlVcjU0SWc5dzlSZlwvbk0zdWh6SVE5ZGFvek0zdjFxS0UwYzhHeWwzVVB5NnUxNmZlNStiZnJLTERubHhpelB0VHJ5TldCYmw0NUtpVmJjNzQ1R2hMV3FLNHZOZFU4Ukx2aTgwZFwvVTZTbzZXZ0ljVFh0S1pGejNlMlhEeWdHVGpEejFtQUU1bDl2Qko2bjBFVm9ITmIwcTB2K3lOZUs2ZEJFNWxtXC9HV2VPdVRLNTU1U2Q4NzE2Q0RrSElzRVlJUUhnWENvS0dGdXRJYzlWcGIya3J1UG5xKzFTeFdNdFpteDI0TURzK3pRWmQ0SkxhM1R0V25KM2c1bkh3Z1ptZzZFZktZK1YxK05BQUx3VTJqR0xYenBHaDdnWTdNcTl2YmRpenQ2R2x0WmhRQjJ0ckc4cEppSmFFZmNDQnlyWk9oUVJcL2VJRmdrTEtFdFo1NDl0QTZWZkRZZkpMNHkyT3N0NFAzYkU4UkpDdWNFaWxCSXBMTjdRNXBJbTVIV0NoNlFxVFJwXC9ZT21icVZDMFpCV1dCSzBKQW9CcE5uOGZHYjdkYXB1NVFYQ2RBcDAwT1dWS05MNm1oR2IzOVdGUGRTa01qMG9pSVd3MnlXZkNsZWhIVjRpZUU2OXVXYytNekpMSlNWZWlLaDNQRjB1dmNWQlFTbVI3VDJVNG1kVDVoZEppeW5cLzZoWGNjYU5XWjV5cHJNdXVqa0pEN3RJSHNvZDBMbU9DTnpPaXNncXdnb3dqWHp4MVJqTkZDZldKVGR1WmYrallvZkpQQ2JaVlRtQXB2NkF0eFlrQ1wvWUpURm40REZmUjBreW1vWlpRbVwvM0pRNlpkY294eGZtUDhwVW5GZkdPTlFwZ2ljaVcwOUVlWkVzdzhKXC8zZkpwOHhnOWRkdjJNT2JxMXRUK3lcL1kwNm1NK1F2MmxKXC9Za3h3bmxwellrKzVmU0tKMFoxemI1QnJCemNwUWdSQ2luSHBpejRtRWhVQjMyVWs5WjVlXC9JSkZvZmtPaWs3aDU2bWNrNG43cTh3UXZsdmpFR25FMVVaVU5WdTFHN1QzTENFcjNBK3ZhK0hIbVFtR2QwNDg4NWZcL3c1elB2dXFKWHhVSmJmK1JNdHlPWGxEa3hzVnRYdVwvaFhcL0RScWlsRFpcL2hmOHhQNUxcL1B6TWpSNE5CZDMyRENEWk1iM1B2UHlCWk9EZmFRaUZTdWZZTTdUdnhVeHBIdDJkcWZWMUlOMnVaeFZBdGVxY2FVb291dkRrSlVCNDRkS2xFc0xGQmptQUxwa1dJanpacG9yN2ZJbG9tSkZSYmdqVkEwV2NBQW85ZHZ2TWIwRGNXcnNLTHhWM0JNcG03aFVsdHV0QnJRdHpvTW91a3Zxb3lhVGkzcDhScXB4NGRHdW9rUkJGQm1zdGw3a0RWVUcxM04zT1RBTW8xZmpLeVBmcU9pWmhiVjg1cys2THBhTnJCUjVFRUJVMHVISGJXZmV4Vk1xRndkbTJtOWFSbTE1RWpMQkRuZlVZSWNwSWpEVFEwVlNsZ1p4TFREemtRVjFUbVd6YU5IZzl4TTAySjRiaVowcEVkOXFicDl4ZzQrMDYyWTFEVGtFM3pRWjRxeEYxOCs4WnZyenl4cmtZaXA2alk4ZGZTV2dmU2pvMlVPZFdHeExKTjhNT2Voakh4Z2JWOEJxRnRPWlRrbEVCbml3aXZWZlJYZTdYbXZFUlVEejRsbmFYMkpWMW1wVE1sWDdtczNyTWkrMkZMVUZtdTg3QmVMdG9zUVVlSGNmcThBdm5RMEZQZU94K2JpWExvQ3FleVRUTzdOeHkxdXU2NVhjV1kwWFpjSUdEV1VjUXRpWTZnTVRYcWVIc3RpY0xCY1d4dDRROW1uVUh6QjBtNW9YcGRXaGpvcng2MFlBejhpRzJlWFVqYkZVT2lIWGxGekN4a05LNGpzSFJHb0xXNWk0QWM4SUxaZldaQkh1c3lFS2NGVGNXbXJEcW5DRXVYaXJsTUpiaUR0SkZ2aHo4ZUs1alwvTG52bUYyME50WWt2TGtNdGNid0pNbG5KRTYrWHNmbEtzR1hBaCsyU1BmRkF4dzF1NmRNZ0Y3QmhiRjBcL01vOUlYeFl2UDdjZ1RZWWRtNDZrVDNqTjc1Q09QUGpIY3RcL0I2djQ0Y1FxQ2hQK0RhdGcwSHhjaDZOWVpsNzZcL3hHclRvU0NcL3dhcm9KK3dhdm1cL2hWVVNTMlhmc1lxSHZyRHFlNG83ZlhkTW03WmptQVFsN2h3dlNXS2srdGMzV0J4UFVlY3V2aUNvait0TWNUdkxIQVg3WEh4WGJLU1FjRVVQU0NRMnJyY0Q1M1JTZ2N4N094THRKWGNhMlFcL2JWTWJOZVEyaFpFR1JjMkhsZFNZVE9yYmFjc1VtM25yTnRGUTNyb2lTVTY5VmJKMkgrNGpCakpRVXg2bWVDUlkzMm9QS2xqNFpaWXFaeG1kbEVqVXRuY3Z6bVF3M041T0x3MGVsRE1iMlp6WGV4dDVqVVRoR09iQ1NtQnVjaEppWnN5aHRIKzRqZnoxUmVpZ0pLbjhLaXdDMVk4WkVMSVlNNDNSR2dCdWxBYUJGbVN2b3paQWFDMnRyUFN1bFk4eHQ2eU9NYk43dGF0T0JwdVcycW9QUXd3SVwvRmpLYXVBcjNSRFd0eHNZaUlnTEhDYVwvM0hsUGpWaHlWcDIzb25ad3RDSGp6SzRCTzR1WEZhSUhtMDA1eGRkWERRSktiYWtKUFFWa0UyQ2dXM2dsdGF4RVI4M2dVc2xXTWJCRG9NdDdVWkxSa0YzelhkWDZvQ1RCa1poSFU1dUlGZDZxTkpNaEZhNmJvM1BhSlNHSWFFd2NJQzNiVStYUnJNNnZrK0JjSEZmdVl1Z1hFcXNWTTlFQlEzdFFyVHczTjNYMWMwV1B0TGI3WUVMWEM5RWh3ekxpNGFPMHFGeFk2ZWVMSmx1aEV4b1JSUHpLbFBIejFnV0FuRFZFV1Q2WVBcL2FxdzlEQzh6bGh0WFwvSU1IZVFHaHhub2VscTRiRGNoMlpsRzZkTWRKbldpSmdGVkNBbGJ0OTBaZFhGTkhMUDROczg1eVpldkIyNE1Kdm84Q1duSEp5dTdaeDZtZVVMdVBjK0h4MExxeHZtREV4U3FxXC9oUEV6WjJsQmFlXC9FRm40TFcrTlwvdmNXc1wvK3Rod1FXdDJ6YzBzN1FIaENvdXpJQjNldzdrWmZ5VncwQWh3bU5CVmVtcjY5aWRJWTlZemlieGlobnhqQjhkeExleGJYYTArTFwvV2d1RldHb040cTVUTlVXWDFXSytQbHRGYTlTNmdjS3Jld1hNaGxmeUdTeVp5d0lcLzRsc1k3UkxEcVlkQmtaU01FOTRBK1Y1d01oRzdlNHozZTdnNlhURVBZemhYQlwvRnVsTFYyQ3pFUmdDbXJXK1Y3MWZ6NWJGaysyeGRhbHc0Z0Z5T1BIUyt5SmpKc1h1U254dG1URjBSVVVwa1BRc1h0bWlnVTVPNms4d01QQVRvMUhRMHVRdEpPQ1RTUk1CMm45a1VlaHdNOFRyMmlEM1ZaVENRNlN6SjdyWE9xNE9SR1EzMWlkY1RaT0duVDJjUXdBVGF0QnFvb0U1WWJXS1gwTHhwZ0lMSmZMcDZ6bnk5R3k4aXhvNjhpTHZPZkhxZCt3QjdmdTBRWGJwY1FyemdubHJuWTNFS3dMMHJoYjFBNG1hZXczazBleW9WVkw2NWFBOEYyYUdpc1lyWjBXM1ZjeG1tRXZKMFdXZHNMXC9xMWF0dkZneDlpZkwwRVZXeVNHaGJDMDlNQWV6SnM4Nk9QWHZEVjU1XC83RGIwNmxadk9BUHJxbzFHNUNhRnhLV01LNE5HdGZhZ0F3ZVZodzBGczVqZ1MySllhb2hNN040bmp5Mm9oZlRaRFFNbzJVU2Rjd2NYcjVZRTZmZytCWXBEZGoxRklHdVhhU1wvZGNjTWJhT1BJQWh4MU1aUDF6eXJuUXZwQk9VOVVIakFVcW1CdkdjWlhTbGhNdURUcWd3Um9TY0gxRkFySmhPUlZEWWVSY2p2MDRBUFJ3bGJDQVdFREZDVWpCRjRQeHliVkJEdnFwZnFmaUtWXC9OeXNHSGgxWDFseWR4NnRIUUJvVDh3ajJQd2hsMkJ5cnh0aVkxeENuY2d6VnpieUhMTE8yMzdtSGlXd1k4YmtSeUpPMU1scVpzTFpoU2trVkRtZ1I3dThHUHJqak9DTFROU3p1ZXV5STdPNjNxcXRWeUYrdVc2aWR5bFwvNnJkT1JiZVYzXC9WcmFCdjg1RWdCXC9uSkgrZG9Id2VBbitlVUg4Y1hQNThjdjJcL0FLSDRMUnM9IiwiYWRkaXRpb25hbEluZm8iOnsiYXV0aFVkZjEiOiIiLCJhdXRoVWRmMiI6IiIsImF1dGhVZGYzIjoiIiwiYXV0aFVkZjQiOiIiLCJhdXRoVWRmNSI6IiIsImF1dGhVZGY2IjoiIiwiYXV0aFVkZjciOiIiLCJhdXRoVWRmOCI6IiIsImF1dGhVZGY5IjoiIiwiYXV0aFVkZjEwIjoiIn0sImF1dGhvcml6YXRpb25VcmwiOiJodHRwczpcL1wvc2VjdXJlLnBheXUuaW5cLzQzYjM5YTYwMzkwOGFmNzMyNWMyNGM3OWYzMWY1Zjg0XC9kZWNvdXBsZWRcL0F1dGhvcml6ZVR4biJ9" 
    "authenticationStatus" : "success" 
    "hash" : "2d87a411991566566a2efacc926e1bb60f7b850f7812c49343af4fa43ed5939252a17d11cd7a0a78ff9605cb5fdc3407de0ae9a5c54bf9240f6df9334cdecc64" 
} 
```

Decoded **bankData** example 

```plaintext
{
   "referenceId": "d78a00cef2b413e9969d122c7d8899f5",
   "messageDigest": "c2e9e456037f033e5cc3d7b6e556189a78058c61cf6b5ed7381e8e371d2f494e1610255c736952094c56e611c8e25108|06422f8040dee9936ce52b4c5cfb782667331cdf",
   "pares": "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",
   "additionalInfo": {
      "authUdf1": "",
      "authUdf2": "",
      "authUdf3": "",
      "authUdf4": "",
      "authUdf5": "",
      "authUdf6": "",
      "authUdf7": "",
      "authUdf8": "",
      "authUdf9": "",
      "authUdf10": ""
   },
   "authorizationUrl": "https://secure.payu.in/43b39a603908af7325c24c79f31f5f84/decoupled/AuthorizeTxn"
}
```

## **Step 3: Authorize (Charge) the Payment**

The authorization request is the final step of transaction processing. This again needs to be an S2S call from the merchant’s server to PayU server.

### **Request Parameters**

**Post URL**: Use the **authorizationUrl** received in [Step 2](http://10.251.7.113:8080/wordpress/wp-admin/post.php?post=28933\&action=edit#Step2) to post the following request parameters.

In the request parameters, you will be appending the JSON values received in [Step 2](http://10.251.7.113:8080/wordpress/wp-admin/post.php?post=28933\&action=edit#Step2) on `termUrl` to the request, so the list of the request parameters will be as in the following request parameters table:  

| **Field**      | **Description**                                                                                        | **Applicable to EMV 3DS** |
| -------------- | ------------------------------------------------------------------------------------------------------ | ------------------------- |
| cres           | This field contains the Base 64 encoded value received from ACS as part of the authentication response | Yes                       |
| referenceId    | This field contains the same referenceId which sent in response of the first call                      |                           |
| additionalInfo | This field can be used in the case of schemes where different parameters may need from merchant side.  |                           |
| messageDigest  | This field includes the Base 64 encoding of (sha56 hash of the JSON data (post to server).             |                           |
| pares          | This parameter contains the pares being returned by the bank.                                          |                           |

#### Sample Request

```curl
curl -X POST "{{termurl from Step 2}}"
-H "Content-Type: application/x-www-form-urlencoded" -d "key= {{merchKey}}&amount= {{amount}},&hash&{{auth_hash}}&txnid= {{txnId}}&referenceId= b6035f64240b1862295bc571952cf98&pares=””,&cres=”” &messageDigest=“”&additionalInfo={ "authUdf1": "", "authUdf2": "", "authUdf3": "", "authUdf4": "", "authUdf5": "", "authUdf6": "", "authUdf7": "", "authUdf8": "", "authUdf9": "", "authUdf10": "" }"
```

#### Response Parameters

The parameters in the response for similar for all the S2S flows. For more information, refer to the [Additional Info for Payment APIs](ref:backup-of-payment-apis).

#### Sample Response

```plaintext
{
   "metaData": {
      "message": "No Error",
      "referenceId": "b6035f64240b1862295bc571952cf984",
      "statusCode": "E000",
      "txnId": "payuTestTransaction2746829",
      "unmappedStatus": "success",
      "submitOtp": {
         "status": "success"
      }
   },
   "result": {
      "mihpayid": "15270336226",
      "mode": "CC",
      "status": "success",
      "key": "4wvMqy",
      "txnid": "payuTestTransaction2746829",
      "amount": "1.10",
      "addedon": "2022-06-01 17:39:29",
      "productinfo": "Product Info",
      "firstname": "Postman",
      "lastname": "",
      "address1": "",
      "address2": "",
      "city": "",
      "state": "",
      "country": "",
      "zipcode": "",
      "email": "test@payu.in",
      "phone": "9988776655",
      "udf1": "",
      "udf2": "",
      "udf3": "",
      "udf4": "",
      "udf5": "",
      "udf6": "",
      "udf7": "",
      "udf8": "",
      "udf9": "",
      "udf10": "",
      "card_token": "",
      "card_no": "XXXXXXXXXXXX8006",
      "field0": "",
      "field1": "6540854745166970506094",
      "field2": "947167",
      "field3": "1.10",
      "field4": "15270336226",
      "field5": "100",
      "field6": "",
      "field7": "AUTHPOSITIVE",
      "field8": "",
      "field9": "Transaction is Successful",
      "payment_source": "payuPureS2SAuth",
      "PG_TYPE": "CC-PG",
      "error": "E000",
      "error_Message": "No Error",
      "cardToken": "",
      "net_amount_debit": "1.1",
      "discount": "0.00",
      "offer_key": "",
      "offer_availed": "",
      "unmappedstatus": "captured",
      "hash": "cdc409dfd15a842b8d15d6627d0027619882ed800773fa413cef491ae8ff2ef0cdfa654680ba4c8f3567313c6a6b00b94cb3bb5e16bad21d26be01216a69af41",
      "bank_ref_no": "6540854745166970506094",
      "bank_ref_num": "6540854745166970506094",
      "bankcode": "CC",
      "surl": "",
      "curl": "",
      "furl": "",
      "card_hash": "fdb59253e36daf8b3969525ae3799ccb4bb41993a5d2fcaf22737ec3ac8b90ab"
   }
}
```