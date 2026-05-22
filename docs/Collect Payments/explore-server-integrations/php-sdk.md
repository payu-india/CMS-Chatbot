---
title: PHP SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: PHP SDK for Server-side Integration
  description: ''
  keywords:
    - PHP SDK for Server-side integration
    - Server-side integration PHP SDK
    - Integrate Server-side with PHP SDK
  robots: index
next:
  description: ''
---
---
title: PHP SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: PHP SDK for Server-side Integration
  description: >-
    PayU PHP server SDK: Composer install, key/salt config, payment form/API, verify transaction, refunds, sandbox, and go-live.
  robots: index
  keywords:
    - payu php sdk payment gateway integration india
    - php server side payment gateway sdk integration steps
    - integrate payu payment api php laravel backend
    - payment gateway php sdk composer integration payu
    - server to server payment integration php sdk payu
    - php payment api sdk hash verification integration payu
    - backend payment gateway integration php rest api payu
    - payu php sdk test credentials sandbox integration guide
    - enterprise php payment integration sdk payu hosted checkout
    - php payment gateway sdk documentation integration india payu
    - php java python payment gateway api sdk integration payu
    - payu server sdk node java php python payment api india

next:
  description: ''
---
The PayU SDK for PHP enables you to easily work with the APIs of PayU by integrating this SDK within your base system. With our SDK, you do not need to worry about low-level details for API integration and with a few lines of code and a function call, get started within a few minutes. To install PHP Web SDK, refer to Install PHP Web SDK.

## Features Supported

The following features are supported in the PHP SDK:

* Create a Payment form.
* Verify the transaction or check the transaction status.
* Initiate/cancel refunds and check the status of a refund.
* Retrieve settlement details that the bank has to settle you.
* Get information on eligible payment options and PG/BANK downtime details.
* Check the customer’s eligibility for EMI and get the amount according to the EMI interest.
* Create/Expire invoice link through the function.

## Prerequistes
* PHP version >= 7
* Enable the payment methods that you want to offer to your customers from Dashboard > Settings > Payment methods. We enable Cards, UPI, and other payment methods by default, and PayU recommends that you enable other payment methods that are relevant to you.

## Steps to Integrate

<Accordion title="Create a PayU account" icon="fa-code">
  First, create a PayU account. See [Register for a Merchant Account.](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard)

  ***

  > 🚧 Download php SDK
  >
  > You can download the php web SDK from the following github link: [https://github.com/payu-intrepos/web-sdk-php](https://github.com/payu-intrepos/web-sdk-php)
</Accordion>

<Accordion title="Build PayU object" icon="fa-code">
  Use the following code snippet to create the instance of the PayU class object:

  ```Text PHP
  namespace <namespace_name>;
  require_once('PayU.php');
  $payu_obj = new PayU();
  ```

  Set the credentials data and URL using the following code sample:

  ```Text PHP
  $payu_obj->env_prod = 0;  //  1 for Live Environment/ 0 for SandBox Environment
      $payu_obj->key = '<key>';
      $payu_obj->salt = '<salt>';

      $res = $payu_obj->initGateway();
  ```

  ***
</Accordion>

<Accordion title="Initiate a payment" icon="fa-code">
  This method can be used to submit HTML form code with the required parameters.

  ```Text PHP
      public function showPaymentForm($params) {
          ?>
          <form action="<?= $this->url; ?>" id="payment_form_submit" method="post">
              <input type="hidden" id="surl" name="surl" value="<?= self::SUCCESS_URL; ?>" />
              <input type="hidden" id="furl" name="furl" value="<?= self::FAILURE_URL; ?>" />
              <input type="hidden" id="key" name="key" value="<?= $this->key; ?>" />
              <input type="hidden" id="txnid" name="txnid" value="<?= $params['txnid'] ?>" />
              <input type="hidden" id="amount" name="amount" value="<?= $params['amount']; ?>" />
              <input type="hidden" id="productinfo" name="productinfo" value="<?= $params['productinfo']; ?>" />
              <input type="hidden" id="firstname" name="firstname" value="<?= $params['firstname']; ?>" />
              <input type="hidden" id="lastname" name="lastname" value="<?= $params['lastname']; ?>" />
              <input type="hidden" id="zipcode" name="zipcode" value="<?= $params['zipcode']; ?>" />
              <input type="hidden" id="email" name="email" value="<?= $params['email']; ?>" />
              <input type="hidden" id="phone" name="phone" value="<?= $params['phone']; ?>" />
              <input type="hidden" id="address1" name="address1" value="<?= $params['address1']; ?>" />
              <input type="hidden" id="city" name="city" value="<?= $params['city']; ?>" />
              <input type="hidden" id="state" name="state" value="<?= $params['state']; ?>" />
              <input type="hidden" id="country" name="country" value="<?= $params['country']; ?>" />
              <input type="hidden" id="hash" name="hash" value="<?= $this->getHashKey($params); ?>" />
          </form>
          <script type="text/javascript">
              document.getElementById("payment_form_submit").submit();
          </script>
          <?php
          return null;
      }

      private function getHashKey($params) {
          return hash('sha512', $this->key . '|' . $params['txnid'] . '|' . $params['amount'] . '|' . $params['productinfo'] . '|' . $params['firstname'] . '|' . $params['email'] . '|' . $params['udf1'] . '|' . $params['udf2'] . '|' . $params['udf3'] . '|' . $params['udf4'] . '|' . $params['udf5'] . '||||||' . $this->salt);
      }
  ```

  ***
</Accordion>

<Accordion title="Verify payment" icon="fa-code">
  This method can be used to fetch the status/details of a transaction using txnid or payuid.

  ```Text PHP
      public function verifyPayment($params) {
         if(!empty($params['txnid'])){
              $transaction = $this->getTransactionByTxnId($params['txnid']);
          }
          else{
              $transaction = $this->getTransactionByPayuId($params['payuid']);
          }
          return $transaction;
      }
  ```

  ***
</Accordion>

<Accordion title="Get transaction details" icon="fa-code">
  This method This method can be used to fetch the details of the transactions within a date and time range.

  ```Text PHP
    public function getTransaction($params) {
          $command = ($params['type'] == 'time') ? self::GET_TRANSACTION_INFO_API : self::GET_TRANSACTION_DETAILS_API;
          $this->params['data'] = ['var1' => $params['from'], 'var2' => $params['to'], 'command' => $command];
          return $this->execute();
      }
  ```

  ***
</Accordion>

<Accordion title="Validate VPA" icon="fa-code">
  This method can be used to validate VPA of a user.

  ```Text PHP
   public function validateUpi($params) {
          $this->params['data'] = ['var1' => $params['vpa'], 'var2' => $params['auto_pay_vpa'], 'command' => self::VALIDATE_UPI_HANLE_API];
          return $this->execute();
      }
  ```

  ***
</Accordion>

<Accordion title="Cencel refund transaction" icon="fa-code">
  This method can be used to initiate refunds for a specific transaction.

  ```Text PHP
   public function cancelRefundTransaction($params) {
          $this->params['data'] = ['var1' => $params['payuid'], 'var2' => $params['txnid'], 'var3' => $params['amount'], 'command' => self::CANCEL_REFUND_API];
          return $this->execute();
      }
  ```

  ***
</Accordion>

<Accordion title="Check action status" icon="fa-code">
  This method can be used to check the status of a refund.

  ```Text PHP
      public function checkRefundStatus($params) {
          $this->params['data'] = ['var1' => $params['request_id'], 'command' => self::CHECK_ACTION_STATUS];
          return $this->execute();
      }

      public function checkRefundStatusByPayuId($params) {
          $this->params['data'] = ['var1' => $params['payuid'], 'var2' => 'payuid', 'command' => self::CHECK_ACTION_STATUS];
          return $this->execute();
      }
  ```

  ***
</Accordion>

<Accordion title="Get net banking status" icon="fa-code">
  This method can be used to check status (down/up) of PGs.

  ```Text PHP
      public function getTransaction($params) {
          $this->params['data'] = ['var1' => $params['netbanking_code'], 'command' => self::GET_NETBANKING_STATUS_API];
          return $this->execute();
      }
  ```

  ***
</Accordion>

<Accordion title="Get issuing bank status" icon="fa-code">
  This method can be used to check downtime through bin number.

  ```Text PHP
   public function getIssuingBankStatus($params) {
          $this->params['data'] = ['var1' => $params['cardnum'], 'command' => self::GET_ISSUING_BANK_STATUS_API];
          return $this->execute();
      }
  ```

  ***
</Accordion>

<Accordion title="Check bin type" icon="fa-code">
  This method can be used to check the bin information.

  ```Text PHP
   public function getCardBin($params) {
          $this->params['data'] = ['var1' => $params['cardnum'], 'command' => self::GET_CARD_BIN_API];
          return $this->execute();
      }
  ```

  ***
</Accordion>

<Accordion title="Create invoice" icon="fa-code">
  This method can be used to create email and SMS invoice ( Pay by link ).

  ```Text PHP
   public function createPaymentInvoice($params) {
          $this->params['data'] = ['var1' => $params['details'], 'command' => self::CREATE_INVOICE_API];
          return $this->execute();
      }
  ```

  ***
</Accordion>

<Accordion title="Expire invoice" icon="fa-code">
  This method can be used to expire email and SMS invoice ( Pay by link ).

  ```Text PHP
   public function expirePaymentInvoice($params) {
          $this->params['data'] = ['var1' => $params['txnid'], 'command' => self::EXPIRE_INVOICE_API];
          return $this->execute();
      }
  ```

  ***
</Accordion>

<Accordion title="Elligible bins for EMI" icon="fa-code">
  This method can be used to check the card eligibilty for EMI through the bin number.

  ```Text PHP
   public function checkEligibleEMIBins($params) {
          $this->params['data'] = ['var1' => $params['bin'], 'var2' => $params['card_num'], 'var3' => $params['bank_name'], 'command' => self::CHECK_ELIGIBLE_BIN_FOR_EMI_API];
          return $this->execute();
      }
  ```

  ***
</Accordion>

<Accordion title="Get EMI amount according to interest" icon="fa-code">
  This method can be used to fetch EMI interest amount according to Banks and tenure.

  ```Text PHP
   public function getEmiAmount($params) {
          $this->params['data'] = ['var1' => $params['amount'], 'command' => self::GET_EMI_AMOUNT_ACCORDING_TO_INTEREST_API];
          return $this->execute();
      }
  ```

  ***
</Accordion>

<Accordion title="Get settlement details" icon="fa-code">
  This method can be used to fetch settlement details for a particular date or UTR number.

  ```Text PHP
   public function getSettlementDetails($params) {
          $this->params['data'] = ['var1' => $params['data'], 'command' => self::GET_SETTLEMENT_DETAILS_API];
          return $this->execute();
      }

  ```

  ***
</Accordion>

<Accordion title="Get checkout detail" icon="fa-code">
  This method can be used to fetch payment options, eligibility, recommendations, and downtime details.

  ```Text PHP
   public function getCheckoutDetails($params) {
          $this->params['data'] = ['var1' => $params['data'], 'command' => self::GET_CHECKOUT_DETAILS_API];
          return $this->execute();
      }
  ```
</Accordion>

## Test and Go-live


  <Test_your_integration />

  <br />

  <Go_Live_Checklist />