---
title: Error Codes for Offers Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## **Offers Error Codes**

<Table>
  <thead>
    <tr>
      <th>
        **Scenario**
      </th>

      <th>
        **Response**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        If amount is missing in cart\_details
      </td>

      <td>
        \{\
        "status": 0,\
        "message": "amount is mandatory in cart\_details.",\
        "code": 400\
        }
      </td>
    </tr>

    <tr>
      <td>
        If items is missing in cart\_details
      </td>

      <td>
        \{\
        "status": 0,\
        "message": "items is mandatory in cart\_details.",\
        "code": 400\
        }
      </td>
    </tr>

    <tr>
      <td>
         If sku\_details is missing in cart\_details
      </td>

      <td>
        \{\
        "status": 0,\
        "message": "sku\_details is mandatory in cart\_details.",\
        "code": 400\
        }
      </td>
    </tr>

    <tr>
      <td>
        If sku\_id is missing in sku\_details under cart\_details section
      </td>

      <td>
        \{\
        "status": 0,\
        "message": "sku\_id is mandatory in sku\_details.",\
        "code": 400\
        }
      </td>
    </tr>

    <tr>
      <td>
        If sku\_name is missing in sku\_details under cart\_details section
      </td>

      <td>
        \{\
        "status": 0,\
        "message": "sku\_name is mandatory in sku\_details.",\
        "code": 400\
        }
      </td>
    </tr>

    <tr>
      <td>
        If amount\_per\_sku is missing in sku\_details under cart\_details section
      </td>

      <td>
        \{\
        "status": 0,\
        "message": "amount\_per\_sku is mandatory in sku\_details.",\
        "code": 400\
        }
      </td>
    </tr>

    <tr>
      <td>
        If quantity is missing in sku\_details under cart\_details section
      </td>

      <td>
        \{\
        "status": 0,\
        "message": "quantity is mandatory in sku\_details.",\
        "code": 400\
        }
      </td>
    </tr>

    <tr>
      <td>
        If user\_token have special characters apart from alphanumeric
      </td>

      <td>
        \{\
        "status": 0,\
        "message": "user\_token should be alphanumeric.",\
        "code": 400\
        }
      </td>
    </tr>

    <tr>
      <td>
        Items should match with total sum of sku quantities
      </td>

      <td>
        \{\
        "status": 0,\
        "message": "Mismatched cart\_details items and total skus.",\
        "code": 400\
        }
      </td>
    </tr>

    <tr>
      <td>
        Amount in cart\_details should match with total sum of sku details amount
      </td>

      <td>
        \{\
        "status": 0,\
        "message": "Mismatched cart\_details amount and total skus amount.",\
        "code": 400\
        }
      </td>
    </tr>

    <tr>
      <td>
        Amount in cart\_details should match with invoice amount
      </td>

      <td>
        \{\
        "status": 0,\
        "message": "Mismatched cart\_details amount and invoice amount.",\
        "code": 400\
        }
      </td>
    </tr>
  </tbody>
</Table>
