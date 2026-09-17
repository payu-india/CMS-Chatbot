---
title: Payment Mechanism to Instrument Mapping
deprecated: false
hidden: false
metadata:
  robots: index
---
This page lists all valid `payment_mechanism` and `instrument` combinations for the Partner Merchant Rates API.

When setting rates, the `instrument` value **must belong to** the specified `payment_mechanism`. Using an instrument from a different mode returns:

```json
{ "status": "error", "message": "Invalid instrument '<INSTR>' for payment_mechanism '<MECH>'" }
```

> **All codes are case-sensitive.** Availability of specific instruments depends on your PayU environment configuration.

***

## Table of Contents

- [Card Payments](#card-payments)
- [UPI](#upi)
- [Net Banking](#net-banking)
- [EMI](#emi)
- [Buy Now Pay Later](#buy-now-pay-later)
- [Digital Wallets & Cash](#digital-wallets-cash)
- [Standing Instructions](#standing-instructions)
- [eNACH / Auto-Debit](#enach-auto-debit)
- [QR Code Payments](#qr-code-payments)
- [Bill Payments](#bill-payments)
- [Connected Payments](#connected-payments)
- [UPI Offline / PPI](#upi-offline-ppi)
- [Bank Transfers](#bank-transfers)
- [IVR Payments](#ivr-payments)
- [Offline & Challan](#offline-challan)
- [Other Modes](#other-modes)

***

## Card Payments

### `CC`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `AMEX`     | `AMEX_DI`  | `CARD_TSP` |
| `CC`       | `DINR`     | `MASTCC`   |
| `RUPAYCC`  | `VISACC`   |            |

**Total:** 8 instruments

### `DC`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `BMD`      | `BOID`     | `CANB`     |
| `CITD`     | `DC`       | `IOBD`     |
| `IODB`     | `LVDB`     | `MAES`     |
| `MAST`     | `PNDB`     | `RUPAY`    |
| `SBDB`     | `SBID`     | `SMAE`     |
| `SMAST`    | `UBID`     | `UNID`     |
| `VISA`     |            |            |

**Total:** 19 instruments

***

## UPI

### `UPI`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `INAPP`    | `INTENT`   | `INTTPV`   |
| `PP_UPI`   | `PUSH`     | `SQR`      |
| `TEZ`      | `TEZOMNI`  | `TEZSPOT`  |
| `TEZTPV`   | `UPI`      | `UPITPV`   |

**Total:** 12 instruments

### `UPICC`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `INAPPCC`  | `INTCC`    | `INTCCSI`  |
| `PPUPICC`  | `PUSHCC`   | `TEZCC`    |
| `TEZTPVCC` | `TOMNICC`  | `TSPOTCC`  |
| `UPICC`    | `UPICCSI`  |            |

**Total:** 11 instruments

### `UPIPPI`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `INAPPPPI` | `INTPPI`   | `INTPPISI` |
| `INTTVPPI` | `PUSHPPI`  | `TEZPPI`   |
| `TEZTVPPI` | `TOMNIPPI` | `TSPOTPPI` |
| `UPIPPI`   | `UPIPPISI` | `UPITVPPI` |

**Total:** 12 instruments

### `UPICCEMI`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `INTAX03`  | `INTAX06`  | `INTAX09`  |
| `INTAX12`  | `INTAX24`  | `INTYES03` |
| `INTYES06` | `INTYES09` | `INTYES12` |
| `INTYES18` | `INTYES24` | `UPIAX03`  |
| `UPIAX06`  | `UPIAX09`  | `UPIAX12`  |
| `UPIAX24`  | `UPIYES03` | `UPIYES06` |
| `UPIYES09` | `UPIYES12` | `UPIYES18` |
| `UPIYES24` |            |            |

**Total:** 22 instruments

***

## Net Banking

### `NB`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `162B`     | `ABIRLA`   | `ABNBTPV`  |
| `ADBB`     | `AIRNB`    | `ALLB`     |
| `AUNBTPV`  | `AUSFCNB`  | `AUSFNB`   |
| `AXIB`     | `AXISCNB`  | `AXNBTPV`  |
| `BANDNB`   | `BANDTPV`  | `BBCB`     |
| `BBKB`     | `BBRB`     | `BBRNBTPV` |
| `BMNN`     | `BOIB`     | `BOINBTPV` |
| `BOMB`     | `CABB`     | `CBIB`     |
| `CBITPV`   | `CBNBTPV`  | `CITNB`    |
| `CPNB`     | `CRBP`     | `CRPB`     |
| `CSBN`     | `CSBNBTPV` | `CSFBC`    |
| `CSFBR`    | `CSMSNB`   | `CUBB`     |
| `CUBNBTPV` | `DBS`      | `DBSB`     |
| `DCBB`     | `DCBCORP`  | `DCBNBTPV` |
| `DENN`     | `DLNBCORP` | `DLSB`     |
| `DLSBCORP` | `DLSNBTPV` | `DSHB`     |
| `FEDB`     | `FEDCORP`  | `FEDNBTPV` |
| `HDFB`     | `HDFCCONB` | `HDFNBTPV` |
| `ICIB`     | `ICICB`    | `ICICICNB` |
| `ICINBTPV` | `IDBB`     | `IDBICORP` |
| `IDBITPV`  | `IDFCNB`   | `IDFNBTPV` |
| `INDB`     | `INDBTPV`  | `INDPOST`  |
| `INGB`     | `INIB`     | `INIBTPV`  |
| `INOB`     | `IOBNBTPV` | `JAKB`     |
| `JANANB`   | `JSBNB`    | `KRKB`     |
| `KRKBTPV`  | `KRVB`     | `KRVBC`    |
| `KTKBCORP` | `KTKNBTPV` | `KVBNBTPV` |
| `LVBD`     | `LVBNBTPV` | `LVCB`     |
| `LVRB`     | `NB`       | `OBCB`     |
| `OBCNBTPV` | `PAYTMNB`  | `PAYTMTPV` |
| `PMNB`     | `PNBB`     | `PNBNBTPV` |
| `PSBNB`    | `RBL`      | `RBLCNB`   |
| `RBLNB`    | `RBLTPV`   | `RTN`      |
| `RYBS`     | `SBBJB`    | `SBHB`     |
| `SBIB`     | `SBINBTPV` | `SBMB`     |
| `SBNCORP`  | `SBPB`     | `SBTB`     |
| `SCBNB`    | `SCBNBTPV` | `SDCB`     |
| `SIBNBTPV` | `SOIB`     | `SRSWT`    |
| `SVCB`     | `SVCNB`    | `SYDB`     |
| `SYNDB`    | `TBON`     | `TMBB`     |
| `UBIB`     | `UBIBC`    | `UBIBTPV`  |
| `UCOB`     | `UCOCNB`   | `UCOCTPV`  |
| `UCONBTPV` | `UNIB`     | `VJYB`     |
| `YESB`     | `YESNBTPV` |            |

**Total:** 131 instruments

***

## EMI

### `EMI`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `AUSF03`   | `AUSF06`   | `AUSF09`   |
| `AUSF12`   | `AUSF18`   | `AUSF24`   |
| `AXIO`     | `AXIO03`   | `AXIO06`   |
| `AXIO09`   | `AXIO12`   | `AXIO18`   |
| `AXIO24`   | `AXISD03`  | `AXISD06`  |
| `AXISD09`  | `AXISD12`  | `AXISD18`  |
| `AXISD24`  | `BAJFIN02` | `BAJFIN03` |
| `BAJFIN06` | `BAJFIN08` | `BAJFIN09` |
| `BAJFIN12` | `BOBCC02`  | `BOBCC03`  |
| `BOBCC04`  | `BOBCC05`  | `BOBCC06`  |
| `BOBCC07`  | `BOBCC08`  | `BOBCC09`  |
| `BOBCC12`  | `BOBCC18`  | `BOBCC24`  |
| `BOBCC36`  | `BOBD03`   | `BOBD06`   |
| `BOBD09`   | `BOBD12`   | `BOBD18`   |
| `CANARA03` | `CANARA06` | `CANARA09` |
| `CANARA12` | `CANARA18` | `CANARA24` |
| `DBS03`    | `DBS06`    | `DBS09`    |
| `DBS12`    | `DBS18`    | `DBS24`    |
| `EMAMEX12` | `EMI`      | `EMI012`   |
| `EMI018`   | `EMI024`   | `EMI03`    |
| `EMI06`    | `EMI09`    | `EMI12`    |
| `EMI18`    | `EMI24`    | `EMI30`    |
| `EMI36`    | `EMI48`    | `EMI6`     |
| `EMI9`     | `EMIA12`   | `EMIA18`   |
| `EMIA24`   | `EMIA3`    | `EMIA6`    |
| `EMIA9`    | `EMIAMEX3` | `EMIAMEX6` |
| `EMIAMEX9` | `EMICB12`  | `EMICB6`   |
| `EMICB9`   | `EMICBI12` | `EMICBI3`  |
| `EMICBI6`  | `EMICBI9`  | `EMICD03`  |
| `EMICD06`  | `EMICD09`  | `EMICD12`  |
| `EMICD18`  | `EMICD24`  | `EMICP12`  |
| `EMICP3`   | `EMICP6`   | `EMICP9`   |
| `EMIHS03`  | `EMIHS06`  | `EMIHS09`  |
| `EMIHS12`  | `EMIHS18`  | `EMIHS24`  |
| `EMIIC12`  | `EMIIC18`  | `EMIIC24`  |
| `EMIIC3`   | `EMIIC6`   | `EMIIC9`   |
| `EMIIND12` | `EMIIND18` | `EMIIND24` |
| `EMIIND3`  | `EMIIND36` | `EMIIND6`  |
| `EMIIND9`  | `EMIK12`   | `EMIK18`   |
| `EMIK24`   | `EMIK3`    | `EMIK36`   |
| `EMIK6`    | `EMIK9`    | `EMIKP3`   |
| `EMIRBL12` | `EMIRBL18` | `EMIRBL24` |
| `EMIRBL3`  | `EMIRBL6`  | `EMIRBL9`  |
| `EMISCB12` | `EMISCB18` | `EMISCB24` |
| `EMISCB3`  | `EMISCB6`  | `EMISCB9`  |
| `EMIY03`   | `EMIY06`   | `EMIY09`   |
| `EMIY12`   | `EMIY18`   | `EMIY24`   |
| `FDRL03`   | `FDRL06`   | `FDRL09`   |
| `FDRL12`   | `FDRL18`   | `FDRL24`   |
| `FEDED03`  | `FEDED06`  | `FEDED09`  |
| `FEDED12`  | `HDFCCL03` | `HDFCCL06` |
| `HDFCCL09` | `HDFCCL12` | `HDFCCL18` |
| `HDFCD03`  | `HDFCD06`  | `HDFCD09`  |
| `HDFCD12`  | `HDFCD18`  | `HDFCD24`  |
| `HDFCD24X` | `HDFCD36`  | `HDFCD36X` |
| `HDFCD48`  | `HDFCD48X` | `HDFCDC03` |
| `HDFCDC06` | `HDFCDC09` | `HDFCDC12` |
| `HDFCDC18` | `HDFCDC24` | `HDFCDC36` |
| `HDFCDC48` | `HMECDT03` | `HMECDT06` |
| `HMECDT09` | `HMECDT12` | `ICICIC03` |
| `ICICIC06` | `ICICIC09` | `ICICIC12` |
| `ICICID03` | `ICICID06` | `ICICID09` |
| `ICICID12` | `ICINBEMI` | `IDBI03`   |
| `IDBI06`   | `IDBI09`   | `IDBI12`   |
| `IDBI18`   | `IDBI24`   | `IDBI30`   |
| `IDBI36`   | `IDFC03`   | `IDFC06`   |
| `IDFC09`   | `IDFC12`   | `IDFC15`   |
| `IDFC18`   | `IDFC24`   | `IDFC36`   |
| `KBEE03`   | `KBEE06`   | `KBEE09`   |
| `KBEE12`   | `KBEE18`   | `KOTAKC01` |
| `KOTAKC02` | `KOTAKC03` | `KOTAKC06` |
| `KOTAKC09` | `KOTAKC12` | `KOTAKC18` |
| `KOTAKD01` | `KOTAKD02` | `KOTAKD03` |
| `KOTAKD06` | `KOTAKD09` | `KOTAKD12` |
| `LIQUIL06` | `ONEC03`   | `ONEC06`   |
| `ONEC09`   | `ONEC12`   | `ONEC18`   |
| `ONEC24`   | `SBI03`    | `SBI06`    |
| `SBI09`    | `SBI12`    | `SBI18`    |
| `SBI24`    | `SBID03`   | `SBID06`   |
| `SBID09`   | `SBID12`   | `SBID18`   |
| `SBID24`   | `SBID30`   | `SBID36`   |
| `SBIP03`   | `ZEST03`   | `ZEST06`   |
| `ZEST09`   | `ZEST12`   | `ZESTMON`  |

**Total:** 249 instruments

***

## Buy Now Pay Later

### `BNPL`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `BNPL`     | `HDFCF15`  | `HDFCF30`  |
| `HDFCF60`  | `HDFCF90`  | `ICICPL`   |
| `LAZYPAY`  | `MOBIZIP`  | `POSTPE`   |
| `SIMPL`    |            |            |

**Total:** 10 instruments

***

## Digital Wallets & Cash

### `CASH`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `ADVCLUB`  | `AMON`     | `AMZPAY`   |
| `BFL`      | `CASH`     | `CCD`      |
| `CITRUSW`  | `FREC`     | `IDM`      |
| `ITZC`     | `JIOM`     | `MOBIKWIK` |
| `OLAM`     | `OXYC`     | `PAYTM`    |
| `PAYZ`     | `PAYZP`    | `PHONEPE`  |
| `PMNW`     | `PPINAPP`  | `PPINTENT` |
| `PPSDKLES` | `PYZP`     | `TPAY`     |
| `TWID`     | `WLT`      | `YESW`     |

**Total:** 27 instruments

### `WALLET`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `PAYUW`    | `WALLET`   |            |

**Total:** 2 instruments

***

## Standing Instructions

### `SI`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `ACUXENCR` | `AIRPENCR` | `AKOXENCR` |
| `AMEXSI`   | `ANDBENCR` | `APGBENCR` |
| `AUBLENCR` | `BARBENCR` | `BDBLENCR` |
| `BKIDENCR` | `CBINENCR` | `CCSI`     |
| `CGBXENCR` | `CITIENCR` | `CIUBENCR` |
| `CLBLENCR` | `CNRBENCR` | `CNSXENCR` |
| `COSBENCR` | `CSBKENCR` | `DBSSENCR` |
| `DCBLENCR` | `DCSI`     | `DEUTENCR` |
| `DLXBENCR` | `EDBXENCR` | `ESAFENCR` |
| `ESFBENCR` | `FDRLENCR` | `FINFENCR` |
| `FINOENCR` | `HDFCDCSI` | `HDFCENCR` |
| `HSBCENCR` | `HUTXENCR` | `IBKLENCR` |
| `ICICENCR` | `IDFBENCR` | `IDIBENCR` |
| `INDBENCR` | `INTENTSI` | `INTTPVCC` |
| `IOBAENCR` | `JAKAENCR` | `JSFBENCR` |
| `JUCXENCR` | `KARBENCR` | `KCCBENCR` |
| `KKBKENCR` | `KNSBENCR` | `KVBLENCR` |
| `KVGBENCR` | `MAHBENCR` | `MHSXENCR` |
| `NCBLENCR` | `NSPBENCR` | `ORBCENCR` |
| `PSIBENCR` | `PUNBENCR` | `PYTMENCR` |
| `RATNENCR` | `RSSXENCR` | `SBINENCR` |
| `SCBLENCR` | `SHIXENCR` | `SI`       |
| `SIBLENCR` | `SPCBENCR` | `STCBENCR` |
| `SURYENCR` | `SYNBENCR` | `TMBLENCR` |
| `UBINENCR` | `UCBAENCR` | `UPISI`    |
| `UPITPVCC` | `USFBENCR` | `UTBIENCR` |
| `UTIBENCR` | `UTKSENCR` | `VARAENCR` |
| `YESBENCR` | `ZCBLENCR` |            |

**Total:** 83 instruments

***

## eNACH / Auto-Debit

### `ENACH`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `ACUXENCC` | `AIRPENCC` | `AKOXENCC` |
| `ANDBENCC` | `APGBENCC` | `AUBLENCC` |
| `BARBENCC` | `BDBLENCC` | `BKIDENCC` |
| `CBINENCC` | `CGBXENCC` | `CITIENCC` |
| `CIUBENCC` | `CLBLENCC` | `CNRBENCC` |
| `CNSXENCC` | `COSBENCC` | `CSBKENCC` |
| `DBSSENCC` | `DCBLENCC` | `DEUTENCC` |
| `DLXBENCC` | `EDBXENCC` | `ENACH`    |
| `ESAFENCC` | `ESFBENCC` | `FDRLENCC` |
| `FINFENCC` | `FINOENCC` | `HDFCENCC` |
| `HSBCENCC` | `HUTXENCC` | `IBKLENCC` |
| `ICICENCC` | `IDFBENCC` | `IDIBENCC` |
| `INDBENCC` | `IOBAENCC` | `JAKAENCC` |
| `JSFBENCC` | `JUCXENCC` | `KARBENCC` |
| `KCCBENCC` | `KKBKENCC` | `KNSBENCC` |
| `KVBLENCC` | `KVGBENCC` | `MAHBENCC` |
| `MHSXENCC` | `NCBLENCC` | `NSPBENCC` |
| `ORBCENCC` | `PSIBENCC` | `PUNBENCC` |
| `PYTMENCC` | `RATNENCC` | `RSSXENCC` |
| `SBINENCC` | `SCBLENCC` | `SHIXENCC` |
| `SIBLENCC` | `SPCBENCC` | `STCBENCC` |
| `SURYENCC` | `SYNBENCC` | `TMBLENCC` |
| `UBINENCC` | `UCBAENCC` | `USFBENCC` |
| `UTBIENCC` | `UTIBENCC` | `UTKSENCC` |
| `VARAENCC` | `YESBENCC` | `ZCBLENCC` |

**Total:** 75 instruments

***

## QR Code Payments

### `QR`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `ACCQR`    | `BQR`      | `CCQR`     |
| `DCQR`     | `MCCQR`    | `MDCQR`    |
| `PHNPEQR`  | `QR`       | `QRPPI`    |
| `QRRCC`    | `RCCQR`    | `RDCQR`    |
| `UPIQR`    | `VCCQR`    | `VDCQR`    |

**Total:** 15 instruments

### `DBQR`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `CCDBQR`   | `DBQR`     | `DCDBQR`   |
| `DQRPPI`   | `DQRRCC`   | `MCCDBQR`  |
| `MDCDBQR`  | `RCCDBQR`  | `RDCDBQR`  |
| `UPIDBQR`  | `VCCDBQR`  | `VDCDBQR`  |

**Total:** 12 instruments

### `ISBQR`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `CCIBQR`   | `DCIBQR`   | `ISBQR`    |
| `ISQRPPI`  | `ISQRRCC`  | `MCCIBQR`  |
| `MDCIBQR`  | `RCCIBQR`  | `RDCIBQR`  |
| `UPIIBQR`  | `VCCIBQR`  | `VDCIBQR`  |

**Total:** 12 instruments

### `SBQR`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `CCSBQR`   | `DCSBQR`   | `MCCSBQR`  |
| `MDCSBQR`  | `RCCSBQR`  | `RDCSBQR`  |
| `SBQR`     | `SQRPPI`   | `SQRRCC`   |
| `UPISBQR`  | `VCCSBQR`  | `VDCSBQR`  |

**Total:** 12 instruments

***

## Bill Payments

### `BBPS`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `BBPSACNT` | `BBPSAEPS` | `BBPSBQR`  |
| `BBPSCASH` | `BBPSCC`   | `BBPSDC`   |
| `BBPSIB`   | `BBPSIMPS` | `BBPSNB`   |
| `BBPSNEFT` | `BBPSPC`   | `BBPSUPI`  |
| `BBPSUSSD` | `BBPSWLT`  |            |

**Total:** 14 instruments

***

## Connected Payments

### `CONNECT`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `ADESCASH` | `ADESCC`   | `ADESDC`   |
| `ADESNB`   | `ADESUPI`  | `AIMRCASH` |
| `AIMRCC`   | `AIMRDC`   | `AIMRNB`   |
| `AIMRUPI`  | `AMAZCASH` | `AMAZCC`   |
| `AMAZDC`   | `AMAZNB`   | `AMAZUPI`  |
| `AMPMCASH` | `AMPMCC`   | `AMPMDC`   |
| `AMPMNB`   | `AMPMUPI`  | `CNTCASH`  |
| `CNTCC`    | `CNTDC`    | `CNTNB`    |
| `CNTUPI`   | `DIFMCASH` | `DIFMCC`   |
| `DIFMDC`   | `DIFMNB`   | `DIFMUPI`  |
| `DIGICASH` | `DIGICC`   | `DIGIDC`   |
| `DIGINB`   | `DIGIUPI`  | `ESMYCASH` |
| `ESMYCC`   | `ESMYDC`   | `ESMYNB`   |
| `ESMYUPI`  | `IKEDCASH` | `IKEDCC`   |
| `IKEDDC`   | `IKEDNB`   | `IKEDUPI`  |
| `MOMRCASH` | `MOMRCC`   | `MOMRDC`   |
| `MOMRNB`   | `MOMRUPI`  | `NSTWCASH` |
| `NSTWCC`   | `NSTWDC`   | `NSTWNB`   |
| `NSTWUPI`  | `PAYUCASH` | `PAYUCC`   |
| `PAYUDC`   | `PAYUNB`   | `PAYUUPI`  |
| `PAYZCASH` | `PAYZCC`   | `PAYZDC`   |
| `PAYZNB`   | `PAYZUPI`  | `PYNRCASH` |
| `PYNRCC`   | `PYNRDC`   | `PYNRNB`   |
| `PYNRUPI`  | `RUPECASH` | `RUPECC`   |
| `RUPEDC`   | `RUPENB`   | `RUPEUPI`  |
| `SHOPCASH` | `SHOPCC`   | `SHOPDC`   |
| `SHOPNB`   | `SHOPUPI`  | `SPAYCASH` |
| `SPAYCC`   | `SPAYDC`   | `SPAYNB`   |
| `SPAYUPI`  | `SRPSCASH` | `SRPSCC`   |
| `SRPSDC`   | `SRPSNB`   | `SRPSUPI`  |
| `TRIOCASH` | `TRIOCC`   | `TRIODC`   |
| `TRIONB`   | `TRIOUPI`  | `TWIDCASH` |
| `TWIDCC`   | `TWIDDC`   | `TWIDNB`   |
| `TWIDUPI`  | `UMANCASH` | `UMANCC`   |
| `UMANDC`   | `UMANNB`   | `UMANUPI`  |

**Total:** 105 instruments

***

## UPI Offline / PPI

### `OFUPI`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `INPPI`    | `INTRCC`   | `OFINTENT` |

**Total:** 3 instruments

***

## Bank Transfers

### `NEFTRTGS`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `EFTAXIS`  | `EFTAXTPV` | `EFTHDFCV` |
| `NEFTRTGS` |            |            |

**Total:** 4 instruments

### `DBT`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `DBT`      | `IMPS`     | `NEFT`     |
| `RTGS`     |            |            |

**Total:** 4 instruments

***

## IVR Payments

### `IVR`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `IVR`      | `IVRCC`    | `IVRHEAD`  |
| `IVRRHCC`  |            |            |

**Total:** 4 instruments

### `IVRDC`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `IVRDC`    | `IVRDHEAD` | `IVRRHDC`  |

**Total:** 3 instruments

***

## Offline & Challan

### `CHALLANPAYMENTS`

| Instrument        | Instrument | Instrument |
| ----------------- | ---------- | ---------- |
| `CHALLANPAYMENTS` | `HDFCCASH` | `HDFCCHDD` |
| `HDFCIMPS`        | `HDFCNERT` | `INDIMPS`  |
| `INDNEFT`         |            |            |

**Total:** 7 instruments

### `COD`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `COD`      |            |            |

**Total:** 1 instrument

### `PAISA`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `PAISA`    |            |            |

**Total:** 1 instrument

***

## Other Modes

### `PAYPAL`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `PAYPAL`   |            |            |

**Total:** 1 instrument

### `VISAC`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `VIESC`    | `VIESD`    | `VISAC`    |
| `VISAD`    |            |            |

**Total:** 4 instruments

### `OLAC`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `OLAC`     |            |            |

**Total:** 1 instrument

### `BANGLA`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `BANGLA`   | `SSL`      |            |

**Total:** 2 instruments

### `ADHR`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `ADHR`     |            |            |

**Total:** 1 instrument

### `GC`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `ZAGGLEGC` |            |            |

**Total:** 1 instrument

### `POS`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `POS`      |            |            |

**Total:** 1 instrument

### `OTHERS`

| Instrument | Instrument | Instrument |
| ---------- | ---------- | ---------- |
| `MCC`      | `OTHERS`   |            |

**Total:** 2 instruments

### `PLATFORMFEE`

| Instrument | Instrument | Instrument    |
| ---------- | ---------- | ------------- |
| `DAILY`    | `MONTHLY`  | `PLATFORMFEE` |
| `QUATERLY` | `WEEKLY`   | `YEARLY`      |

**Total:** 6 instruments

***
