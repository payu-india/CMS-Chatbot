---
title: UPI Smart Intent - Non SDK Flow
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: UPI Smart Intent - Non SDK Flow
  description: ''
  keywords:
    - UPI Smart Intent Non SDK integration
    - Non SDK Integration for PayU UPI Smart Intent
    - UPI Smart Intent non SDK implementation
    - Smart Intent UPI payments integration using Non SDK
    - ' PayU UPI Smart Intent with non SDK integration guide'
  robots: index
next:
  description: ''
---
The Non SDK implementation for finding the UPI supported application in the customer's device. The following steps will help you first find the application installed in the customer's device supporting smart intent.

You can use PayU APIs to initiate the transaction and get the Intent payment URI which includes payment details required for the PSP app customer will select for payment. After completion of payment by the customer, you can verify the transaction using the **Verify Payment** API. The following steps are required to enable Smart Intent-based UPI payment in your application.

<Callout icon="❗️" theme="error">
  **Important UPI Integration Changes as per NPCI Mandate on UPI Collect Disablement**

  **Recommended**: For easier integration, merchants can use PayU SDKs for Android and iOS, which have the Smart Intent implementation built-in:

  * [Android UPI SDK](doc:android-upi-sdk) - Supports Collect, Intent, and In-App flows with Smart Intent
  * [Android CheckoutPro SDK](doc:android-checkoutpro-sdk) - Complete checkout solution with Smart Intent
  * [iOS UPI SDK](doc:ios-upi-sdk) - Supports Intent and Collect payments
  * [iOS CheckoutPro SDK](doc:ios-checkoutpro-sdk) - Complete checkout solution for iOS
</Callout>

<br />

<Accordion title="Step 1: Update Manifest File" icon="fa-code">
  Add package ids in your apps manifest file to allow your application to access apps installed on the customer's device. This is required for Android 11 and above.

  ```
   <queries>
          <package android:name="in.amazon.mShop.android.shopping"/>
          <package android:name="com.upi.axispay"/>
          <package android:name="com.axis.mobile"/>
          <package android:name="com.fisglobal.bandhanupi.app"/>
          <package android:name="com.bankofbaroda.upi"/>
          <package android:name="in.org.npci.upiapp"/>
          <package android:name="com.canarabank.mobility"/>
          <package android:name="com.citiuat"/>
          <package android:name="com.dbs.in.digitalbank"/>
          <package android:name="com.olive.dcb.upi"/>
          <package android:name="com.finopaytech.bpayfino"/>
          <package android:name="com.freecharge.android"/>
          <package android:name="com.google.android.apps.nbu.paisa.user"/>
          <package android:name="com.snapwork.hdfc"/>
          <package android:name="com.mgs.hsbcupi"/>
          <package android:name="com.csam.icici.bank.imobile"/>
          <package android:name="com.icicibank.pockets"/>
          <package android:name="com.euronet.iobupi"/>
          <package android:name="com.mgs.induspsp"/>
          <package android:name="com.fss.jnkpsp"/>
          <package android:name="com.jio.myjio"/>
          <package android:name="com.mycompany.kvb"/>
          <package android:name="com.kvb.mobilebanking"/>
          <package android:name="com.lcode.smartz"/>
          <package android:name="com.msf.kbank.mobile"/>
          <package android:name="com.upi.federalbank.org.lotza"/>
          <package android:name="com.infrasofttech.mahaupi"/>
          <package android:name="com.mipay.in.wallet"/>
          <package android:name="com.myairtelapp"/>
          <package android:name="com.mobikwik_new"/>
          <package android:name="com.onymy.paybee.prod"/>
          <package android:name="net.one97.paytm"/>
          <package android:name="com.phonepe.app"/>
          <package android:name="com.Version1"/>
          <package android:name="com.samsung.android.spay"/>
          <package android:name="com.sbi.upi"/>
          <package android:name="com.SIBMobile"/>
          <package android:name="com.truecaller"/>
          <package android:name="com.infrasoft.uboi"/>
          <package android:name="com.lcode.ucoupi"/>
          <package android:name="com.YesBank"/>
          <package android:name="com.dreamplug.androidapp"/>
          <package android:name="money.bullet"/>
      </queries>
  ```

  <br />
</Accordion>

<Accordion title="Step 2: Fetch the List of UPI and Smart Intent Supported Apps" icon="fa-code">
  You need to get the list of UPI and smart intent supported applications installed in the device.

  ```java
  private fun getSmartIntentUPIApps(context: Context?):ArrayList<HashMap<String,String>>?{
          val upiApps = ArrayList<HashMap<String, String>>()
          if (context == null)
              return null

          val intent = Intent()
          intent.data = Uri.parse("upi://pay")
          val activityList = context.packageManager.queryIntentActivities(intent, PackageManager.MATCH_DEFAULT_ONLY)
          for (resolveInfo in activityList){
              var packageInfo: PackageInfo? = null
              try {
                  packageInfo = context.packageManager
                      .getPackageInfo(resolveInfo.activityInfo.packageName, 0)
                  val name =
                      context.packageManager.getApplicationLabel(packageInfo.applicationInfo) as String
                val appInfo = HashMap<String, String?>()
                  appInfo["bankName"] = name ?: "NA"
                  appInfo["packageName"] = packageInfo.packageName
                  upiApps.add(appInfo)
              } catch (e: PackageManager.NameNotFoundException) {
                  e.printStackTrace()
                  return upiApps
              }
          }
          return UPI apps
      }
      /* to get icon of psp app*/
      fun getUpiAppBitmap(context: Context?, packageName: String): Bitmap? {

          var upiAppBitmap: Bitmap? = null
          if (context == null)
              return upiAppBitmap
          upiAppBitmap = context.packageManager.getApplicationIcon(packageName).toBitmap()
          return upiAppBitmap
      }

  ```

  <br />
</Accordion>

<Accordion title="Step 3: Get Intent URI" icon="fa-code">
  Use the **\_payment** API to get Intent URI and transaction details for the UPI app selected by the customer. For more information, refer to <Anchor label="Collect Payment API > UPI Collect" target="_blank" href="ref:_payment_s2s_upi_collection">Collect Payment API > UPI Collect</Anchor>.
</Accordion>

<Accordion title="Step 4: Start Activity" icon="fa-code">
  Start activity using package id and Intent URI. After the intent UI you get from the **\_payment** API, you need to add "upi://pay" as a prefix.

  ```java
  fun makePayment(packageName: String,mActivity: Activity,intentUri:String) {
          val i = Intent()
          i.setPackage(packageName)
          i.action = Intent.ACTION_VIEW
          i.data = Uri.parse("upi://pay" + intentUri)
          if (null != mActivity && !mActivity.isFinishing() && !mActivity.isDestroyed()) {
              mActivity.startActivityForResult(i, 101)
          }
      }
  ```
</Accordion>

<Accordion title="Step 5: Get Callback" icon="fa-code">
  Get a callback in `onActivityResult` for the status of the transaction. Refer to <Anchor label="Verify Payment" target="_blank" href="ref:verify_payment_api">Verify Payment</Anchor> API to get the final status of the transaction.

  ```java
  override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)
        if (requestCode == 101) {
            data?.getStringExtra("Status")?.let { Log.d("result", it) }
            data?.getStringExtra("response")?.let { Log.d("response", it) }
            //get Status
            //if Status == Success
            // Call Verify Payemnt//
        }
  }
  ```
</Accordion>
