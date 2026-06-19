---
title: POC 1
deprecated: false
hidden: true
metadata:
  robots: index
---
<HTMLBlock>{`
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PayU Hosted Checkout — Interactive Integration Guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{
  --ink:#0A0E0D;
  --surface:#121817;
  --surface-2:#161F1D;
  --line:#223330;
  --mint:#6CFFB8;
  --mint-dim:#2E5C49;
  --violet:#B69CFF;
  --amber:#FFB454;
  --paper:#EAF2EE;
  --muted:#8FA39B;
  --mono:'JetBrains Mono', monospace;
  --display:'Space Grotesk', sans-serif;
  --body:'Inter', sans-serif;
  --radius:14px;
}
*{box-sizing:border-box;}
html{scroll-behavior:smooth;}
body{
  margin:0;
  background:var(--ink);
  color:var(--paper);
  font-family:var(--body);
  line-height:1.55;
  -webkit-font-smoothing:antialiased;
}
@media (prefers-reduced-motion: reduce){
  *{animation-duration:0.01ms !important; animation-iteration-count:1 !important; transition-duration:0.01ms !important; scroll-behavior:auto !important;}
}
::selection{background:var(--mint); color:var(--ink);}
a{color:var(--mint);}
.eyebrow{
  font-family:var(--mono);
  font-size:12px;
  letter-spacing:.14em;
  text-transform:uppercase;
  color:var(--mint);
  display:flex;
  align-items:center;
  gap:8px;
  margin:0 0 10px;
}
.eyebrow::before{content:"";width:6px;height:6px;border-radius:50%;background:var(--mint);box-shadow:0 0 8px var(--mint);}
h1,h2,h3{font-family:var(--display); font-weight:700; margin:0; letter-spacing:-0.01em;}
.container{max-width:1180px; margin:0 auto; padding:0 28px;}
code, .mono{font-family:var(--mono);}

/* ---------- TOP NAV ---------- */
.topbar{
  position:sticky; top:0; z-index:50;
  background:rgba(10,14,13,0.86);
  backdrop-filter:blur(10px);
  border-bottom:1px solid var(--line);
}
.topbar-inner{
  max-width:1180px; margin:0 auto; padding:14px 28px;
  display:flex; align-items:center; justify-content:space-between;
}
.brand{display:flex; align-items:center; gap:10px; font-family:var(--display); font-weight:700; font-size:15px;}
.brand .dot{width:9px;height:9px;border-radius:50%;background:var(--mint); box-shadow:0 0 10px var(--mint);}
.brand .sub{color:var(--muted); font-weight:500; font-size:13px;}
.topbar-meta{font-family:var(--mono); font-size:11px; color:var(--muted); display:flex; gap:18px;}
.topbar-meta span{display:flex; align-items:center; gap:6px;}
.pulse{width:7px;height:7px;border-radius:50%;background:var(--mint); animation:pulse 1.8s infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:.3;}}

/* ---------- HERO ---------- */
.hero{padding:64px 0 40px; position:relative; overflow:hidden;}
.hero::before{
  content:"";
  position:absolute; inset:-20% -10% auto -10%; height:480px;
  background:radial-gradient(ellipse at 30% 0%, rgba(108,255,184,0.10), transparent 60%),
             radial-gradient(ellipse at 80% 20%, rgba(182,156,255,0.08), transparent 55%);
  pointer-events:none;
}
.hero-grid{display:grid; grid-template-columns:1.05fr 1fr; gap:48px; align-items:start; position:relative;}
@media (max-width:980px){.hero-grid{grid-template-columns:1fr;}}
.hero h1{font-size:clamp(34px,4.4vw,52px); line-height:1.05; margin-bottom:18px;}
.hero h1 .accent{color:var(--mint);}
.hero p.lede{color:var(--muted); font-size:16.5px; max-width:48ch; margin-bottom:26px;}
.hero-tags{display:flex; gap:8px; flex-wrap:wrap; margin-bottom:30px;}
.tag{
  font-family:var(--mono); font-size:11.5px; padding:6px 11px; border:1px solid var(--line);
  border-radius:100px; color:var(--muted);
}
.cta-row{display:flex; gap:12px; flex-wrap:wrap;}
.btn{
  font-family:var(--body); font-weight:600; font-size:14px; padding:12px 20px; border-radius:10px;
  border:1px solid transparent; cursor:pointer; transition:transform .15s ease, background .15s ease;
  display:inline-flex; align-items:center; gap:8px;
}
.btn-primary{background:var(--mint); color:#06120D;}
.btn-primary:hover{transform:translateY(-2px);}
.btn-ghost{background:transparent; border-color:var(--line); color:var(--paper);}
.btn-ghost:hover{border-color:var(--mint); color:var(--mint);}

/* ---------- HASH TERMINAL (signature element) ---------- */
.terminal{
  background:var(--surface); border:1px solid var(--line); border-radius:var(--radius);
  overflow:hidden; box-shadow:0 30px 60px -30px rgba(0,0,0,0.7);
}
.terminal-head{
  display:flex; align-items:center; justify-content:space-between;
  padding:10px 16px; border-bottom:1px solid var(--line); background:var(--surface-2);
}
.terminal-dots{display:flex; gap:6px;}
.terminal-dots span{width:9px;height:9px;border-radius:50%; background:#3A4A46;}
.terminal-title{font-family:var(--mono); font-size:11.5px; color:var(--muted);}
.terminal-body{padding:18px 18px 20px; font-family:var(--mono); font-size:12.5px;}
.t-field{display:grid; grid-template-columns:88px 1fr; gap:10px; align-items:center; margin-bottom:9px;}
.t-field label{color:var(--violet); font-size:11.5px;}
.t-field input{
  width:100%; background:#0D1413; border:1px solid var(--line); color:var(--paper);
  font-family:var(--mono); font-size:12.5px; padding:8px 10px; border-radius:7px; outline:none;
}
.t-field input:focus{border-color:var(--mint);}
.t-divider{border-top:1px dashed var(--line); margin:14px 0;}
.t-string{
  background:#0D1413; border:1px solid var(--line); border-radius:8px; padding:10px 12px;
  color:var(--muted); font-size:11.5px; word-break:break-all; margin-bottom:12px; min-height:36px;
}
.t-string b{color:var(--mint); font-weight:500;}
.t-string .pipe{color:var(--violet);}
.t-hashrow{display:flex; align-items:center; gap:10px; margin-bottom:4px;}
.t-hashrow .lbl{color:var(--amber); font-size:11.5px; white-space:nowrap;}
.t-hash{
  flex:1; background:linear-gradient(180deg,#0D1413,#0A0F0E); border:1px solid var(--mint-dim);
  border-radius:8px; padding:10px 12px; color:var(--mint); font-size:11.5px; word-break:break-all;
  min-height:36px; box-shadow:inset 0 0 20px rgba(108,255,184,0.04);
}
.t-foot{display:flex; justify-content:space-between; align-items:center; margin-top:10px;}
.t-foot .ok{font-size:11px; color:var(--muted);}
.copy-btn{
  font-family:var(--mono); font-size:10.5px; background:transparent; border:1px solid var(--line);
  color:var(--muted); padding:5px 10px; border-radius:6px; cursor:pointer;
}
.copy-btn:hover{color:var(--mint); border-color:var(--mint);}

/* ---------- LAYOUT: RAIL + CONTENT ---------- */
.layout{display:grid; grid-template-columns:240px 1fr; gap:48px; padding:30px 0 100px;}
@media (max-width:900px){.layout{grid-template-columns:1fr;} .rail{display:none;}}
.rail{position:sticky; top:78px; align-self:start; height:fit-content;}
.rail-title{font-family:var(--mono); font-size:11px; color:var(--muted); letter-spacing:.1em; text-transform:uppercase; margin-bottom:14px;}
.rail-list{list-style:none; padding:0; margin:0; border-left:1px solid var(--line);}
.rail-list li{position:relative;}
.rail-list a{
  display:block; padding:9px 0 9px 18px; color:var(--muted); text-decoration:none; font-size:13.5px;
  border-left:2px solid transparent; margin-left:-1px; transition:color .15s ease, border-color .15s ease;
}
.rail-list a:hover{color:var(--paper);}
.rail-list a.active{color:var(--mint); border-left-color:var(--mint); font-weight:500;}
.rail-list .num{font-family:var(--mono); font-size:10px; margin-right:7px; color:var(--violet);}
.rail-progress{margin-top:18px; padding-top:16px; border-top:1px solid var(--line);}
.rail-progress .pct{font-family:var(--display); font-size:26px; color:var(--mint);}
.rail-progress .lbl{font-size:11px; color:var(--muted);}
.rail-bar{height:4px; background:var(--surface-2); border-radius:4px; margin-top:8px; overflow:hidden;}
.rail-bar-fill{height:100%; background:var(--mint); width:0%; transition:width .3s ease;}

section.block{margin-bottom:72px; scroll-margin-top:88px;}
.block-head{margin-bottom:24px;}
.block-head h2{font-size:clamp(22px,2.6vw,30px);}
.block-head p{color:var(--muted); max-width:62ch; margin-top:8px; font-size:14.5px;}

/* ---------- PREREQ CHECKLIST ---------- */
.checklist{display:grid; gap:10px;}
.check-item{
  display:flex; gap:12px; align-items:flex-start; background:var(--surface); border:1px solid var(--line);
  border-radius:10px; padding:13px 15px; cursor:pointer; transition:border-color .15s ease, background .15s ease;
}
.check-item:hover{border-color:var(--mint-dim);}
.check-item.done{background:rgba(108,255,184,0.05); border-color:var(--mint-dim);}
.check-box{
  width:18px; height:18px; border-radius:5px; border:1.5px solid var(--line); flex-shrink:0; margin-top:2px;
  display:flex; align-items:center; justify-content:center; transition:all .15s ease;
}
.check-item.done .check-box{background:var(--mint); border-color:var(--mint);}
.check-box svg{width:11px; height:11px; opacity:0; transition:opacity .15s ease;}
.check-item.done .check-box svg{opacity:1;}
.check-text{font-size:14px; color:var(--paper);}
.check-item.done .check-text{color:var(--muted); text-decoration:line-through;}

/* ---------- ENV CARDS ---------- */
.env-toggle{display:inline-flex; background:var(--surface); border:1px solid var(--line); border-radius:10px; padding:4px; margin-bottom:20px;}
.env-toggle button{
  font-family:var(--mono); font-size:12px; padding:8px 16px; border-radius:7px; border:none; background:transparent;
  color:var(--muted); cursor:pointer; transition:all .15s ease;
}
.env-toggle button.active{background:var(--mint); color:#06120D; font-weight:600;}
.env-card{
  background:var(--surface); border:1px solid var(--line); border-radius:var(--radius); padding:22px 24px;
  display:none; align-items:center; justify-content:space-between; gap:20px; flex-wrap:wrap;
}
.env-card.active{display:flex;}
.env-url{font-family:var(--mono); font-size:15px; color:var(--mint);}
.env-badge{font-family:var(--mono); font-size:11px; padding:5px 10px; border-radius:100px; border:1px solid var(--line); color:var(--muted);}

/* ---------- PARAMS EXPLORER ---------- */
.params-toolbar{display:flex; gap:10px; margin-bottom:18px; flex-wrap:wrap; align-items:center;}
.filter-btn{
  font-family:var(--mono); font-size:11.5px; padding:7px 14px; border-radius:100px; border:1px solid var(--line);
  background:transparent; color:var(--muted); cursor:pointer; transition:all .15s ease;
}
.filter-btn.active{background:var(--violet); color:#1A0F33; border-color:var(--violet); font-weight:600;}
.search-box{
  margin-left:auto; background:var(--surface); border:1px solid var(--line); border-radius:100px;
  padding:7px 16px; font-family:var(--mono); font-size:12px; color:var(--paper); min-width:200px; outline:none;
}
.search-box:focus{border-color:var(--mint);}
.params-grid{display:grid; grid-template-columns:repeat(auto-fill,minmax(280px,1fr)); gap:12px;}
.param-card{
  background:var(--surface); border:1px solid var(--line); border-radius:10px; padding:15px 16px;
  cursor:pointer; transition:border-color .15s ease;
}
.param-card:hover{border-color:var(--mint-dim);}
.param-top{display:flex; justify-content:space-between; align-items:center; gap:8px;}
.param-name{font-family:var(--mono); font-size:13.5px; color:var(--paper); font-weight:600;}
.param-req{font-family:var(--mono); font-size:9.5px; padding:3px 8px; border-radius:100px; text-transform:uppercase; letter-spacing:.05em;}
.param-req.mandatory{background:rgba(255,180,84,0.12); color:var(--amber);}
.param-req.optional{background:rgba(182,156,255,0.12); color:var(--violet);}
.param-desc{font-size:12.5px; color:var(--muted); margin-top:8px; max-height:0; overflow:hidden; transition:max-height .25s ease, margin .25s ease;}
.param-card.open .param-desc{max-height:120px; margin-top:8px;}
.param-example{font-family:var(--mono); font-size:11px; color:var(--mint); margin-top:6px; display:none;}
.param-card.open .param-example{display:block;}

/* ---------- CODE TABS ---------- */
.code-tabs{background:var(--surface); border:1px solid var(--line); border-radius:var(--radius); overflow:hidden;}
.tab-bar{display:flex; gap:2px; padding:8px 8px 0; border-bottom:1px solid var(--line); overflow-x:auto; background:var(--surface-2);}
.tab-btn{
  font-family:var(--mono); font-size:12px; padding:9px 16px; background:transparent; border:none; color:var(--muted);
  cursor:pointer; white-space:nowrap; border-bottom:2px solid transparent; transition:all .15s ease;
}
.tab-btn.active{color:var(--mint); border-bottom-color:var(--mint);}
.tab-panel{display:none; position:relative;}
.tab-panel.active{display:block;}
.tab-panel pre{
  margin:0; padding:20px 22px; font-family:var(--mono); font-size:12px; line-height:1.65; color:#C9D6D0;
  overflow-x:auto; max-height:420px;
}
.tab-panel .copy-btn{position:absolute; top:14px; right:16px;}
.code-kw{color:var(--violet);} .code-str{color:var(--mint);} .code-com{color:var(--muted); font-style:italic;}

/* ---------- FLOW STEPPER (replaces flow diagram) ---------- */
.flow-stepper{display:flex; gap:10px; margin-bottom:22px; flex-wrap:wrap;}
.flow-step-btn{
  flex:1; min-width:160px; background:var(--surface); border:1px solid var(--line); border-radius:10px;
  padding:14px 16px; cursor:pointer; text-align:left; transition:all .2s ease; position:relative;
}
.flow-step-btn .fn{font-family:var(--mono); font-size:10px; color:var(--violet); margin-bottom:4px; display:block;}
.flow-step-btn .ft{font-size:13.5px; font-weight:600; color:var(--paper);}
.flow-step-btn.active{border-color:var(--mint); background:rgba(108,255,184,0.06);}
.flow-step-btn.active .fn{color:var(--mint);}
.flow-step-btn::after{
  content:"→"; position:absolute; right:-22px; top:50%; transform:translateY(-50%); color:var(--line); font-size:14px;
}
.flow-step-btn:last-child::after{display:none;}
@media (max-width:700px){.flow-step-btn::after{display:none;}}
.flow-detail{
  background:var(--surface); border:1px solid var(--mint-dim); border-radius:var(--radius); padding:24px 26px;
  min-height:140px;
}
.flow-detail h4{font-family:var(--display); font-size:17px; margin-bottom:8px; color:var(--mint);}
.flow-detail p{color:var(--muted); font-size:14px; margin:0 0 10px;}
.flow-detail .payload{font-family:var(--mono); font-size:11.5px; background:#0D1413; border:1px solid var(--line); border-radius:8px; padding:12px 14px; color:var(--paper);}

/* ---------- RESPONSE TOGGLE ---------- */
.resp-toggle{display:inline-flex; background:var(--surface); border:1px solid var(--line); border-radius:10px; padding:4px; margin-bottom:16px;}
.resp-toggle button{font-family:var(--mono); font-size:12px; padding:8px 18px; border-radius:7px; border:none; background:transparent; color:var(--muted); cursor:pointer;}
.resp-toggle button.success-active{background:var(--mint); color:#06120D; font-weight:600;}
.resp-toggle button.failure-active{background:var(--amber); color:#3A1F00; font-weight:600;}
.resp-payload{display:none; font-family:var(--mono); font-size:12px; background:var(--surface); border:1px solid var(--line); border-radius:var(--radius); padding:20px 22px; color:#C9D6D0; line-height:1.8; white-space:pre-wrap;}
.resp-payload.active{display:block;}
.resp-payload .k{color:var(--violet);}
.resp-payload .v-ok{color:var(--mint);}
.resp-payload .v-fail{color:var(--amber);}

/* ---------- VERIFY DEMO ---------- */
.verify-box{background:var(--surface); border:1px solid var(--line); border-radius:var(--radius); padding:24px 26px; display:grid; grid-template-columns:1fr auto 1fr; gap:16px; align-items:center;}
@media (max-width:700px){.verify-box{grid-template-columns:1fr;}}
.verify-side h5{font-family:var(--mono); font-size:11px; color:var(--muted); text-transform:uppercase; letter-spacing:.08em; margin-bottom:8px;}
.verify-hash{font-family:var(--mono); font-size:11px; word-break:break-all; background:#0D1413; border:1px solid var(--line); border-radius:8px; padding:10px 12px; color:var(--paper);}
.verify-result{text-align:center; font-family:var(--mono); font-size:24px;}
.verify-result.match{color:var(--mint);}

/* ---------- CHECKLIST PROGRESS BAR (testing/golive) ---------- */
.checklist-wrap{background:var(--surface); border:1px solid var(--line); border-radius:var(--radius); padding:22px 24px;}
.checklist-bar{height:6px; background:var(--surface-2); border-radius:6px; overflow:hidden; margin-bottom:18px;}
.checklist-bar-fill{height:100%; background:linear-gradient(90deg,var(--mint),var(--violet)); width:0%; transition:width .3s ease;}

/* ---------- FOOTER ---------- */
footer{border-top:1px solid var(--line); padding:40px 0; text-align:center;}
footer p{color:var(--muted); font-size:12.5px; font-family:var(--mono);}

.kbd{font-family:var(--mono); font-size:10.5px; background:var(--surface-2); border:1px solid var(--line); border-radius:5px; padding:2px 6px; color:var(--muted);}
</style>
</head>
<body>

<div class="topbar">
  <div class="topbar-inner">
    <div class="brand"><span class="dot"></span>PayU Hosted Checkout <span class="sub">/ Integration Guide</span></div>
    <div class="topbar-meta">
      <span><span class="pulse"></span> Live demo</span>
      <span id="topbar-pct">0% read</span>
    </div>
  </div>
</div>

<header class="hero">
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">Web Integration · PayU Hosted</p>
      <h1>Redirect customers to checkout.<br><span class="accent">Verify everything with one hash.</span></h1>
      <p class="lede">A server-generated redirect sends customers to PayU's hosted payment page, then back to your success or failure URL. This guide walks through the exact request, the hash that protects it, and the response you must verify.</p>
      <div class="hero-tags">
        <span class="tag">SHA-512 signed</span>
        <span class="tag">Server-to-server safe</span>
        <span class="tag">~15 min integration</span>
      </div>
      <div class="cta-row">
        <button class="btn btn-primary" onclick="document.getElementById('step1').scrollIntoView()">Start integration ↓</button>
        <button class="btn btn-ghost" onclick="document.getElementById('hash-gen').scrollIntoView()">Jump to hash logic</button>
      </div>
    </div>

    <div class="terminal" id="hero-terminal">
      <div class="terminal-head">
        <div class="terminal-dots"><span></span><span></span><span></span></div>
        <div class="terminal-title">hash_preview.sh — live SHA-512</div>
      </div>
      <div class="terminal-body">
        <div class="t-field"><label>txnid</label><input id="hf-txnid" value="t6svtqtjRdl4ws"></div>
        <div class="t-field"><label>amount</label><input id="hf-amount" value="499.00"></div>
        <div class="t-field"><label>product</label><input id="hf-product" value="Pro Plan"></div>
        <div class="t-field"><label>name</label><input id="hf-name" value="Aditi"></div>
        <div class="t-field"><label>email</label><input id="hf-email" value="aditi@shop.dev"></div>
        <div class="t-field"><label>salt</label><input id="hf-salt" value="yourSalt123"></div>
        <div class="t-divider"></div>
        <div class="t-string" id="hf-string"></div>
        <div class="t-hashrow">
          <span class="lbl">sha512()</span>
          <div class="t-hash" id="hf-hash">computing…</div>
        </div>
        <div class="t-foot">
          <span class="ok" id="hf-status">● computed in your browser, nothing sent anywhere</span>
          <button class="copy-btn" data-copy-target="hf-hash">copy hash</button>
        </div>
      </div>
    </div>
  </div>
</header>

<div class="container layout">
  <nav class="rail">
    <div class="rail-title">On this page</div>
    <ul class="rail-list" id="rail-list">
      <li><a href="#prereq" data-num="00"><span class="num">00</span>Prerequisites</a></li>
      <li><a href="#step1" data-num="01"><span class="num">01</span>Build the request</a></li>
      <li><a href="#env" data-num="—"><span class="num">—</span>Environments</a></li>
      <li><a href="#params" data-num="—"><span class="num">—</span>Parameters</a></li>
      <li><a href="#hash-gen" data-num="02"><span class="num">02</span>Generate hash</a></li>
      <li><a href="#post-form" data-num="03"><span class="num">03</span>POST the form</a></li>
      <li><a href="#flow" data-num="—"><span class="num">—</span>Redirect flow</a></li>
      <li><a href="#response" data-num="04"><span class="num">04</span>Handle response</a></li>
      <li><a href="#verify" data-num="05"><span class="num">05</span>Verify hash</a></li>
      <li><a href="#test" data-num="06"><span class="num">06</span>Test integration</a></li>
      <li><a href="#golive" data-num="07"><span class="num">07</span>Go live</a></li>
    </ul>
    <div class="rail-progress">
      <div class="pct" id="rail-pct">0%</div>
      <div class="lbl">page progress</div>
      <div class="rail-bar"><div class="rail-bar-fill" id="rail-bar-fill"></div></div>
    </div>
  </nav>

  <main id="main-content">

    <section class="block" id="prereq">
      <div class="block-head">
        <h2>Before you start</h2>
        <p>Check these off as you go — your progress is tracked at the top of this page.</p>
      </div>
      <div class="checklist" id="prereq-list"></div>
    </section>

    <section class="block" id="step1">
      <div class="block-head">
        <h2><span style="color:var(--violet)">01</span> Build the request</h2>
        <p>Every transaction starts as a set of fields collected on your server — some mandatory, some optional. Explore them below.</p>
      </div>
    </section>

    <section class="block" id="env">
      <div class="block-head">
        <h2>Environments</h2>
        <p>Same integration, two endpoints. Flip the switch.</p>
      </div>
      <div class="env-toggle">
        <button class="active" onclick="setEnv('test')">Test</button>
        <button onclick="setEnv('prod')">Production</button>
      </div>
      <div class="env-card active" id="env-test">
        <div>
          <div class="env-badge">test environment</div>
          <div class="env-url" style="margin-top:8px;">https://test.payu.in/_payment</div>
        </div>
        <button class="copy-btn" data-copy-text="https://test.payu.in/_payment">copy URL</button>
      </div>
      <div class="env-card" id="env-prod">
        <div>
          <div class="env-badge">production environment</div>
          <div class="env-url" style="margin-top:8px;">https://secure.payu.in/_payment</div>
        </div>
        <button class="copy-btn" data-copy-text="https://secure.payu.in/_payment">copy URL</button>
      </div>
    </section>

    <section class="block" id="params">
      <div class="block-head">
        <h2>Parameters explorer</h2>
        <p>Click any card to expand its description and example. Filter by requirement or search by name.</p>
      </div>
      <div class="params-toolbar">
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="mandatory">Mandatory</button>
        <button class="filter-btn" data-filter="optional">Optional</button>
        <input class="search-box" id="param-search" placeholder="search parameter…">
      </div>
      <div class="params-grid" id="params-grid"></div>
    </section>

    <section class="block" id="hash-gen">
      <div class="block-head">
        <h2><span style="color:var(--violet)">02</span> Generate the hash</h2>
        <p>Concatenate fields in this exact sequence, then SHA-512 the result. Pick your language below — they all produce the same digest.</p>
      </div>
      <div class="code-tabs" id="hash-code-tabs"></div>
    </section>

    <section class="block" id="post-form">
      <div class="block-head">
        <h2><span style="color:var(--violet)">03</span> POST the form</h2>
        <p>Render an auto-submitting form server-side, or POST directly from your backend in any language binding.</p>
      </div>
      <div class="code-tabs" id="post-code-tabs"></div>
    </section>

    <section class="block" id="flow">
      <div class="block-head">
        <h2>The redirect, step by step</h2>
        <p>Click through each actor in the flow to see exactly what happens and what data moves.</p>
      </div>
      <div class="flow-stepper" id="flow-stepper"></div>
      <div class="flow-detail" id="flow-detail"></div>
    </section>

    <section class="block" id="response">
      <div class="block-head">
        <h2><span style="color:var(--violet)">04</span> Handle the response</h2>
        <p>PayU POSTs back to your surl/furl with the outcome. Toggle between a successful and a failed transaction payload.</p>
      </div>
      <div class="resp-toggle">
        <button class="success-active" onclick="setResp('success')" id="resp-btn-success">Success</button>
        <button onclick="setResp('failure')" id="resp-btn-failure">Failure</button>
      </div>
      <div class="resp-payload active" id="resp-success"></div>
      <div class="resp-payload" id="resp-failure"></div>
    </section>

    <section class="block" id="verify">
      <div class="block-head">
        <h2><span style="color:var(--violet)">05</span> Verify with reverse hash</h2>
        <p>The response hash uses the <em>same fields in reverse order</em>. Compute it server-side and compare — never trust the response without this.</p>
      </div>
      <div class="verify-box">
        <div class="verify-side">
          <h5>You compute</h5>
          <div class="verify-hash" id="verify-computed">05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072</div>
        </div>
        <div class="verify-result match">=</div>
        <div class="verify-side">
          <h5>PayU sends</h5>
          <div class="verify-hash">05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072</div>
        </div>
      </div>
      <p style="color:var(--muted); font-size:13px; margin-top:14px;">Reverse sequence: <code class="mono" style="color:var(--mint);">sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)</code></p>
    </section>

    <section class="block" id="test">
      <div class="block-head">
        <h2><span style="color:var(--violet)">06</span> Test the integration</h2>
        <p>Work through this checklist in the test environment before requesting production keys.</p>
      </div>
      <div class="checklist-wrap">
        <div class="checklist-bar"><div class="checklist-bar-fill" id="test-bar-fill"></div></div>
        <div class="checklist" id="test-list"></div>
      </div>
    </section>

    <section class="block" id="golive">
      <div class="block-head">
        <h2><span style="color:var(--violet)">07</span> Go live</h2>
        <p>Final checks before you flip the switch to production.</p>
      </div>
      <div class="checklist-wrap">
        <div class="checklist-bar"><div class="checklist-bar-fill" id="golive-bar-fill"></div></div>
        <div class="checklist" id="golive-list"></div>
      </div>
    </section>

  </main>
</div>

<footer>
  <p>PayU Hosted Checkout — Interactive Guide · built for developers, not for skimming</p>
</footer>

<script>
/* ===================== UTIL ===================== */
function escapeHtml(s){
  return s.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}
async function sha512Hex(str){
  const enc = new TextEncoder().encode(str);
  const buf = await crypto.subtle.digest('SHA-512', enc);
  return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2,'0')).join('');
}
function copyToClipboard(text, btn){
  navigator.clipboard.writeText(text).then(()=>{
    const orig = btn.textContent;
    btn.textContent = 'copied ✓';
    btn.style.color = 'var(--mint)';
    setTimeout(()=>{ btn.textContent = orig; btn.style.color=''; }, 1400);
  });
}
document.addEventListener('click', (e)=>{
  const btn = e.target.closest('.copy-btn');
  if(!btn) return;
  if(btn.dataset.copyText){ copyToClipboard(btn.dataset.copyText, btn); return; }
  if(btn.dataset.copyTarget){
    const el = document.getElementById(btn.dataset.copyTarget);
    if(el) copyToClipboard(el.textContent.trim(), btn);
  }
});

/* ===================== HERO HASH TERMINAL ===================== */
const hfIds = ['hf-txnid','hf-amount','hf-product','hf-name','hf-email','hf-salt'];
async function updateHashTerminal(){
  const [txnid, amount, product, name, email, salt] = hfIds.map(id => document.getElementById(id).value || '');
  const key = 'gtKNFy'; // demo merchant key
  const fields = [key, txnid, amount, product, name, email, '', '', '', '', ''];
  const stringPreview = \`<b>${escapeHtml(key)}</b><span class="pipe">|</span>${escapeHtml(txnid)}<span class="pipe">|</span>${escapeHtml(amount)}<span class="pipe">|</span>${escapeHtml(product)}<span class="pipe">|</span>${escapeHtml(name)}<span class="pipe">|</span>${escapeHtml(email)}<span class="pipe">|||||</span><span class="pipe">|</span>${escapeHtml(salt)}\`;
  document.getElementById('hf-string').innerHTML = stringPreview;

  const fullString = \`${key}|${txnid}|${amount}|${product}|${name}|${email}|||||| ${salt}\`.replace(' ', '');
  const hashEl = document.getElementById('hf-hash');
  hashEl.textContent = 'computing…';
  try{
    const hash = await sha512Hex(fullString);
    // typewriter reveal
    hashEl.textContent = '';
    let i = 0;
    const chars = hash.split('');
    const reveal = () => {
      if(i < chars.length){
        hashEl.textContent += chars[i];
        i++;
        requestAnimationFrame(()=> setTimeout(reveal, 2));
      }
    };
    reveal();
  }catch(err){
    hashEl.textContent = 'sha512 unavailable in this context';
  }
}
hfIds.forEach(id => document.getElementById(id).addEventListener('input', updateHashTerminal));
updateHashTerminal();

/* ===================== PREREQ CHECKLIST ===================== */
const prereqItems = [
  'Create an account with PayU (test + production)',
  'Generate test merchant key and salt from the dashboard',
  'Have HTTPS success (surl) and failure (furl) URLs reachable from the public internet',
  'Confirm you can compute SHA-512 server-side — never in the browser for real transactions'
];
function renderChecklist(containerId, items, barFillId, topbarSync){
  const container = document.getElementById(containerId);
  container.innerHTML = items.map((text,i)=>\`
    <div class="check-item" data-index="${i}">
      <div class="check-box"><svg viewBox="0 0 16 16" fill="none"><path d="M2 8.5L6 12.5L14 3.5" stroke="#06120D" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      <div class="check-text">${text}</div>
    </div>\`).join('');
  container.querySelectorAll('.check-item').forEach(el=>{
    el.addEventListener('click', ()=>{
      el.classList.toggle('done');
      const done = container.querySelectorAll('.check-item.done').length;
      const pct = Math.round((done/items.length)*100);
      if(barFillId) document.getElementById(barFillId).style.width = pct + '%';
      updateGlobalProgress();
    });
  });
}
renderChecklist('prereq-list', prereqItems);

const testItems = [
  'Double-check key & salt match the test environment',
  'Print the pre-hash string server-side and compare field order against the docs',
  'Submit a transaction with all mandatory fields and confirm redirect to PayU',
  'Simulate a successful payment using test cards/UPI and confirm surl receives the POST',
  'Simulate a failed payment and confirm furl receives the POST with status=failure',
  'Recompute the reverse hash on the response and confirm it matches'
];
renderChecklist('test-list', testItems, 'test-bar-fill');

const goLiveItems = [
  'Swap the form action / endpoint to https://secure.payu.in/_payment',
  'Replace test key & salt with production credentials',
  'Re-run hash generation against production salt',
  'Configure production webhooks for payment status updates',
  'Confirm surl/furl are publicly reachable over HTTPS in production'
];
renderChecklist('golive-list', goLiveItems, 'golive-bar-fill');

/* ===================== ENV TOGGLE ===================== */
function setEnv(which){
  document.querySelectorAll('.env-toggle button').forEach(b=>b.classList.remove('active'));
  event.target.classList.add('active');
  document.getElementById('env-test').classList.toggle('active', which==='test');
  document.getElementById('env-prod').classList.toggle('active', which==='prod');
}

/* ===================== PARAMETERS EXPLORER ===================== */
const params = [
  {name:'key', req:'mandatory', desc:'Merchant key provided by PayU during onboarding.', example:'JPG****.k'},
  {name:'txnid', req:'mandatory', desc:'Reference number for a specific order, generated by the merchant.', example:'ypl938459435'},
  {name:'amount', req:'mandatory', desc:'The payment amount for the transaction.', example:'10.00'},
  {name:'productinfo', req:'mandatory', desc:'A brief description of the product.', example:'iPhone'},
  {name:'firstname', req:'mandatory', desc:"The customer's first name.", example:'Ashish'},
  {name:'email', req:'mandatory', desc:"The customer's email address.", example:'ashish@example.com'},
  {name:'phone', req:'mandatory', desc:"The customer's phone number.", example:'9999999999'},
  {name:'lastname', req:'optional', desc:"The customer's last name.", example:'Kumar'},
  {name:'surl', req:'mandatory', desc:'Success URL — page PayU redirects to if the transaction succeeds.', example:'https://yourapp.com/payu/success'},
  {name:'furl', req:'mandatory', desc:'Failure URL — page PayU redirects to if the transaction fails.', example:'https://yourapp.com/payu/failure'},
  {name:'curl', req:'optional', desc:'Cancel URL — page PayU redirects to if the transaction is cancelled.', example:'https://yourapp.com/payu/cancel'},
  {name:'hash', req:'mandatory', desc:'SHA-512 hash calculated by the merchant for integrity. See the hash generator above.', example:'05a397…b072'},
  {name:'address1', req:'optional', desc:'First line of billing address — helps with fraud detection and chargebacks.', example:'H.No 17, Block C'},
  {name:'address2', req:'optional', desc:'Second line of billing address.', example:'34 Saikripa Estate'},
  {name:'city', req:'optional', desc:"Customer's billing city.", example:'Mumbai'},
  {name:'state', req:'optional', desc:"Customer's billing state.", example:'Maharashtra'},
  {name:'country', req:'optional', desc:"Customer's billing country.", example:'India'},
  {name:'zipcode', req:'optional', desc:'Billing zip code — mandatory if offering cardless EMI. Max 20 characters.', example:'400004'},
  {name:'enforced_payment', req:'optional', desc:'Restrict the transaction to specific payment modes, card schemes, or banks.', example:'creditcard|debitcard'},
  {name:'drop_category', req:'optional', desc:'Hide one or more payment options from the checkout page.', example:'CC'},
  {name:'udf1–udf5', req:'optional', desc:'Up to five user-defined fields for storing custom transaction metadata.', example:'AELPR****E'},
  {name:'custom_note', req:'optional', desc:'A message shown on the PayU payment page, e.g. an extra surcharge notice.', example:'Extra ₹100 charge applies'},
  {name:'note_category', req:'optional', desc:'Comma-separated payment options the custom_note should display for.', example:'CC, NB'},
];
function renderParams(filter='all', search=''){
  const grid = document.getElementById('params-grid');
  const list = params.filter(p=>{
    const matchesFilter = filter==='all' || p.req===filter;
    const matchesSearch = p.name.toLowerCase().includes(search.toLowerCase());
    return matchesFilter && matchesSearch;
  });
  grid.innerHTML = list.map(p=>\`
    <div class="param-card" data-name="${p.name}">
      <div class="param-top">
        <span class="param-name">${p.name}</span>
        <span class="param-req ${p.req}">${p.req}</span>
      </div>
      <div class="param-desc">${p.desc}</div>
      <div class="param-example">e.g. <span>${escapeHtml(p.example)}</span></div>
    </div>\`).join('') || \`<p style="color:var(--muted); font-family:var(--mono); font-size:13px;">No parameters match.</p>\`;
  grid.querySelectorAll('.param-card').forEach(card=>{
    card.addEventListener('click', ()=> card.classList.toggle('open'));
  });
}
renderParams();
document.querySelectorAll('.filter-btn').forEach(btn=>{
  btn.addEventListener('click', ()=>{
    document.querySelectorAll('.filter-btn').forEach(b=>b.classList.remove('active'));
    btn.classList.add('active');
    renderParams(btn.dataset.filter, document.getElementById('param-search').value);
  });
});
document.getElementById('param-search').addEventListener('input', (e)=>{
  const activeFilter = document.querySelector('.filter-btn.active').dataset.filter;
  renderParams(activeFilter, e.target.value);
});

/* ===================== CODE TABS ===================== */
function renderCodeTabs(containerId, tabs){
  const container = document.getElementById(containerId);
  const bar = tabs.map((t,i)=>\`<button class="tab-btn ${i===0?'active':''}" data-i="${i}">${t.label}</button>\`).join('');
  const panels = tabs.map((t,i)=>\`
    <div class="tab-panel ${i===0?'active':''}" data-i="${i}">
      <button class="copy-btn" data-copy-text-id="${containerId}-code-${i}">copy</button>
      <pre id="${containerId}-code-${i}">${t.code}</pre>
    </div>\`).join('');
  container.innerHTML = \`<div class="tab-bar">${bar}</div>${panels}\`;
  container.querySelectorAll('.tab-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      container.querySelectorAll('.tab-btn').forEach(b=>b.classList.remove('active'));
      container.querySelectorAll('.tab-panel').forEach(p=>p.classList.remove('active'));
      btn.classList.add('active');
      container.querySelector(\`.tab-panel[data-i="${btn.dataset.i}"]\`).classList.add('active');
    });
  });
  container.querySelectorAll('[data-copy-text-id]').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      const pre = document.getElementById(btn.dataset.copyTextId);
      copyToClipboard(pre.textContent, btn);
    });
  });
}

const hashCode = [
{label:'JavaScript', code:\`const crypto = require('crypto');

function generateHash(params, salt) {
  const { key, txnid, amount, productinfo, firstname, email,
          udf1 = '', udf2 = '', udf3 = '', udf4 = '', udf5 = '' } = params;

  const hashString = \`\${key}|\${txnid}|\${amount}|\${productinfo}|\${firstname}|\${email}|\${udf1}|\${udf2}|\${udf3}|\${udf4}|\${udf5}||||||\${salt}\`;

  return crypto.createHash('sha512').update(hashString).digest('hex');
}\`},
{label:'Python', code:\`import hashlib

def generate_hash(params, salt):
    key, txnid, amount = params['key'], params['txnid'], params['amount']
    productinfo, firstname, email = params['productinfo'], params['firstname'], params['email']
    udf1, udf2, udf3 = params.get('udf1',''), params.get('udf2',''), params.get('udf3','')
    udf4, udf5 = params.get('udf4',''), params.get('udf5','')

    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}"
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()\`},
{label:'PHP', code:\`function generateHash($params, $salt) {
    $key = $params['key'];
    $txnid = $params['txnid'];
    $amount = $params['amount'];
    $productinfo = $params['productinfo'];
    $firstname = $params['firstname'];
    $email = $params['email'];
    $udf1 = $params['udf1'] ?? '';
    $udf2 = $params['udf2'] ?? '';
    $udf3 = $params['udf3'] ?? '';
    $udf4 = $params['udf4'] ?? '';
    $udf5 = $params['udf5'] ?? '';

    $hashString = "$key|$txnid|$amount|$productinfo|$firstname|$email|$udf1|$udf2|$udf3|$udf4|$udf5||||||$salt";
    return strtolower(hash('sha512', $hashString));
}\`},
{label:'Java', code:\`public static String generateHash(Map<String,String> params, String salt) {
    String key = params.get("key");
    String txnid = params.get("txnid");
    String amount = params.get("amount");
    String productinfo = params.get("productinfo");
    String firstname = params.get("firstname");
    String email = params.get("email");
    String udf1 = params.getOrDefault("udf1", "");
    String udf2 = params.getOrDefault("udf2", "");
    String udf3 = params.getOrDefault("udf3", "");
    String udf4 = params.getOrDefault("udf4", "");
    String udf5 = params.getOrDefault("udf5", "");

    String hashString = key+"|"+txnid+"|"+amount+"|"+productinfo+"|"+firstname+"|"+email+"|"
        +udf1+"|"+udf2+"|"+udf3+"|"+udf4+"|"+udf5+"||||||"+salt;
    return sha512(hashString);
}\`},
{label:'C#', code:\`public static string GenerateHash(Dictionary<string,string> p, string salt)
{
    string hashString = $"{p["key"]}|{p["txnid"]}|{p["amount"]}|{p["productinfo"]}|{p["firstname"]}|{p["email"]}|" +
        $"{Get(p,"udf1")}|{Get(p,"udf2")}|{Get(p,"udf3")}|{Get(p,"udf4")}|{Get(p,"udf5")}||||||{salt}";

    using (SHA512 sha512 = SHA512.Create())
    {
        byte[] bytes = sha512.ComputeHash(Encoding.UTF8.GetBytes(hashString));
        return string.Concat(bytes.Select(b => b.ToString("x2")));
    }
}
static string Get(Dictionary<string,string> p, string k) => p.ContainsKey(k) ? p[k] : "";\`},
];
renderCodeTabs('hash-code-tabs', hashCode.map(t=>({label:t.label, code:escapeHtml(t.code)})));

const postCode = [
{label:'HTML form', code:\`<!doctype html>
<html>
  <body onload="document.forms.payu.submit()">
    <form name="payu" method="post" action="https://test.payu.in/_payment">
      <input type="hidden" name="key" value="JP***g">
      <input type="hidden" name="txnid" value="t6svtqtjRdl4ws">
      <input type="hidden" name="amount" value="499.00">
      <input type="hidden" name="productinfo" value="Pro Plan">
      <input type="hidden" name="firstname" value="Aditi">
      <input type="hidden" name="email" value="aditi@shop.dev">
      <input type="hidden" name="phone" value="9999999999">
      <input type="hidden" name="surl" value="https://yourapp.com/payu/success">
      <input type="hidden" name="furl" value="https://yourapp.com/payu/failure">
      <input type="hidden" name="hash" value="sha512(...hash sequence...)">
      <input type="submit" value="Submit" />
    </form>
  </body>
</html>\`},
{label:'cURL', code:\`curl -X POST "https://test.payu.in/_payment" \\
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d \\
"key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00 \\
&firstname=PayU User&email=test@example.com&phone=9876543210 \\
&productinfo=iPhone&surl=https://yourapp.com/success \\
&furl=https://yourapp.com/failure \\
&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"\`},
{label:'JavaScript', code:\`async function makePayURequest() {
  const formData = new URLSearchParams({
    key: 'JP***g',
    txnid: 'PQI6MqpYrjEefU',
    amount: '10.00',
    firstname: 'PayU User',
    email: 'test@example.com',
    phone: '9876543210',
    productinfo: 'iPhone',
    surl: 'https://yourapp.com/success',
    furl: 'https://yourapp.com/failure',
    hash: '05a397...b072'
  });

  const response = await fetch('https://test.payu.in/_payment', {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: formData
  });

  console.log(await response.text());
}\`},
{label:'Python', code:\`import requests

data = {
    'key': 'JP***g',
    'txnid': 'PQI6MqpYrjEefU',
    'amount': '10.00',
    'firstname': 'PayU User',
    'email': 'test@example.com',
    'phone': '9876543210',
    'productinfo': 'iPhone',
    'surl': 'https://yourapp.com/success',
    'furl': 'https://yourapp.com/failure',
    'hash': '05a397...b072'
}

response = requests.post('https://test.payu.in/_payment', data=data)
print(response.status_code, response.text)\`},
];
renderCodeTabs('post-code-tabs', postCode.map(t=>({label:t.label, code:escapeHtml(t.code)})));

/* ===================== FLOW STEPPER ===================== */
const flowSteps = [
  {tag:'01 · customer', title:'Initiates checkout', body:'Customer confirms their order on your site or app and triggers payment.', payload:'No payload yet — this is a UI action on your frontend.'},
  {tag:'02 · merchant server', title:'Builds & signs the request', body:'Your server assembles the transaction fields and computes the SHA-512 hash using your salt.', payload:'key, txnid, amount, productinfo,\nfirstname, email, surl, furl, hash'},
  {tag:'03 · redirect', title:'POSTs to PayU', body:'An auto-submitting form (or direct POST) sends the signed payload to the PayU hosted endpoint.', payload:'POST https://test.payu.in/_payment'},
  {tag:'04 · payu', title:'Renders payment UI', body:'PayU shows cards, UPI, netbanking and wallet options, and handles authentication.', payload:'Customer completes 3DS / OTP / UPI approval'},
  {tag:'05 · payu → merchant', title:'POSTs the result back', body:'PayU redirects the customer to your surl or furl with the transaction outcome and a response hash.', payload:'status, mihpayid, txnid, amount, hash'},
  {tag:'06 · merchant server', title:'Verifies & confirms', body:'You recompute the reverse hash, confirm it matches, then update the order and show confirmation.', payload:'sha512(SALT|status|...|key) === hash ?'},
];
function renderFlowStepper(){
  const stepper = document.getElementById('flow-stepper');
  stepper.innerHTML = flowSteps.map((s,i)=>\`
    <button class="flow-step-btn ${i===0?'active':''}" data-i="${i}">
      <span class="fn">${s.tag}</span>
      <span class="ft">${s.title}</span>
    </button>\`).join('');
  stepper.querySelectorAll('.flow-step-btn').forEach(btn=>{
    btn.addEventListener('click', ()=>{
      stepper.querySelectorAll('.flow-step-btn').forEach(b=>b.classList.remove('active'));
      btn.classList.add('active');
      showFlowDetail(parseInt(btn.dataset.i));
    });
  });
  showFlowDetail(0);
}
function showFlowDetail(i){
  const s = flowSteps[i];
  document.getElementById('flow-detail').innerHTML = \`
    <h4>${s.title}</h4>
    <p>${s.body}</p>
    <div class="payload">${escapeHtml(s.payload)}</div>\`;
}
renderFlowStepper();

/* ===================== RESPONSE TOGGLE ===================== */
function setResp(which){
  document.getElementById('resp-btn-success').classList.toggle('success-active', which==='success');
  document.getElementById('resp-btn-failure').classList.toggle('failure-active', which==='failure');
  document.getElementById('resp-success').classList.toggle('active', which==='success');
  document.getElementById('resp-failure').classList.toggle('active', which==='failure');
}
document.getElementById('resp-success').innerHTML =
\`<span class="k">mihpayid</span> = 403993715531077182
<span class="k">status</span>    = <span class="v-ok">success</span>
<span class="k">mode</span>      = CC
<span class="k">txnid</span>     = TXN12345
<span class="k">amount</span>    = 1000.00
<span class="k">productinfo</span> = Pro Plan
<span class="k">firstname</span> = Aditi
<span class="k">bank_ref_num</span> = 896193988312194700
<span class="k">field9</span>    = Transaction is Successful
<span class="k">hash</span>      = &lt;response_hash&gt;\`;
document.getElementById('resp-failure').innerHTML =
\`<span class="k">mihpayid</span> = 403993715531077182
<span class="k">status</span>    = <span class="v-fail">failure</span>
<span class="k">mode</span>      = CC
<span class="k">txnid</span>     = TXN12345
<span class="k">amount</span>    = 1000.00
<span class="k">bank_ref_num</span> =
<span class="k">error</span>     = E000
<span class="k">error_Message</span> = Bank was unable to authenticate
<span class="k">field9</span>    = Transaction Failed
<span class="k">hash</span>      = &lt;response_hash&gt;\`;

/* ===================== SCROLL SPY + GLOBAL PROGRESS ===================== */
const sections = document.querySelectorAll('section.block');
const railLinks = document.querySelectorAll('.rail-list a');
function onScroll(){
  let current = sections[0]?.id;
  sections.forEach(sec=>{
    const rect = sec.getBoundingClientRect();
    if(rect.top <= 140) current = sec.id;
  });
  railLinks.forEach(a=>{
    a.classList.toggle('active', a.getAttribute('href') === '#' + current);
  });
  updateGlobalProgress();
}
function updateGlobalProgress(){
  const scrollPct = Math.min(100, Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100));
  document.getElementById('rail-pct').textContent = scrollPct + '%';
  document.getElementById('rail-bar-fill').style.width = scrollPct + '%';
  document.getElementById('topbar-pct').textContent = scrollPct + '% read';
}
window.addEventListener('scroll', onScroll, {passive:true});
onScroll();

</script>
</body>
</html>
`}</HTMLBlock>

<br />
