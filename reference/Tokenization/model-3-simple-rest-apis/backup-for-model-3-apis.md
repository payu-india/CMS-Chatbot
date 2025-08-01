---
title: Backup for Model 3 APIs
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
# Save a Card API

The Save Card API is used for saving a card to the vault. After successfully storing a card, it returns the `cardToken`.

> 📘 Note
>
> As per RBI guidelines, taking consent from the customer and doing an additional factor of authentication is mandatory to tokenize the card. You must ensure this is done before using this API.

## Response Parameters

For the response parameter descriptions, refer to[ Additional Info for Simple REST APIs](/reference/additional-info-for-model-3-parameters#response-parameters-for-save-a-card-api).

## Request Parameters

# Edit a Card API

The **Edit a Card** API is used to edit the details of an existing stored card on the vault. In this case, along with all the parameters required to save to the card, the **cardToken** has to be posted. After successfully editing the card, it returns the **cardToken** of the card.

## Response Parameters

For the response parameter description, refer to [Additional Info for Simple REST APIs](/reference/additional-info-for-model-3-parameters#response-parameters-for-edit-card-api).

## Request Parameters

# Get User Cards

The **Get User Cards** API is used to fetch all the cards corresponding to the user. In this API, the card number and other sensitive information are not returned.

## Response Parameters

For the response parameters, refer to [Additional Info for Model 3 Parameters](ref:additional-info-for-model-3-parameters).

## Request Parameters

# Delete a Card

This API is used to delete an existing card stored on PayU Vault.

## Response Parameters

| **Parameter** | **Description**                                                                                    | **Example**                   |
| ------------- | -------------------------------------------------------------------------------------------------- | ----------------------------- |
| status        | The status of the response can be any of the following:                                            | 1                             |
| msg           | The description of the response whether the card details were deleted successfully or not deleted. | My\_card deleted successfully |

## Request Parameters
