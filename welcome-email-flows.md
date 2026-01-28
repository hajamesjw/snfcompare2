# SNF Compare — Welcome Email Flows

> 3 flows. 9 emails total. Copy each HTML block into Klaviyo.

---

## Table of Contents

| # | Flow | Klaviyo List | Emails |
|---|------|-------------|--------|
| 1 | [Nurses](#flow-1--nurses) | `Y6tGhQ` | 3 emails over 5 days |
| 2 | [Patients & Families](#flow-2--patients--families) | `Ty5RgF` | 3 emails over 5 days |
| 3 | [Newsletter](#flow-3--newsletter) | `WKL5Uq` | 3 emails over 6 days |

### Klaviyo Setup (all flows)

1. Go to **Flows** > **Create Flow** > **Build your own**
2. Set trigger: **List** > select the list ID above
3. Add 3 **Email** actions with time delays between them
4. For each email: paste the subject line, preview text, then switch to **Source** editor and paste the HTML

---

## Quick Reference

| Flow | Email | Send | Subject Line |
|------|-------|------|-------------|
| Nurses | 1/3 | Immediate | Here's the pay data your facility doesn't want you to see |
| Nurses | 2/3 | Day 2 | The 3 numbers that predict a bad workplace |
| Nurses | 3/3 | Day 5 | Your facility comparison checklist (save this) |
| Families | 1/3 | Immediate | How to tell if a nursing home is actually safe |
| Families | 2/3 | Day 2 | 5 red flags in a nursing home's record |
| Families | 3/3 | Day 5 | Questions to ask on your nursing home tour (print this) |
| Newsletter | 1/3 | Immediate | Your first briefing: what's happening in skilled nursing right now |
| Newsletter | 2/3 | Day 3 | The compare tool most subscribers don't know about |
| Newsletter | 3/3 | Day 6 | What to expect every Monday |

---
---

# Flow 1 — Nurses

**Klaviyo List:** `Y6tGhQ`
**Brand color:** `#10b981` (teal/green)
**CTA style:** Green buttons linking to `https://snfcompare.com/#tool`

---

## Nurse Email 1/3 — Immediate

> **Subject:** Here's the pay data your facility doesn't want you to see
> **Preview text:** Compare estimated wages at 15,000+ facilities — filtered by your role.

<details>
<summary>View HTML</summary>

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Welcome to SNF Compare</title>
<style>
  body { margin:0; padding:0; background:#f8fafb; font-family:'Helvetica Neue',Arial,sans-serif; color:#1a1a1a; line-height:1.6; }
  .wrapper { max-width:600px; margin:0 auto; }
  .header { background:#111827; padding:32px 40px; text-align:center; }
  .header h1 { margin:0; color:white; font-size:22px; font-weight:700; }
  .header p { margin:6px 0 0; color:rgba(255,255,255,.5); font-size:13px; }
  .body { background:white; padding:40px; }
  .body h2 { font-size:20px; font-weight:700; color:#111827; margin:0 0 8px; line-height:1.3; }
  .body p { font-size:15px; color:#4b5563; margin:0 0 16px; }
  .divider { border:none; border-top:1px solid #f0f0f0; margin:24px 0; }
  .step { display:table; width:100%; margin-bottom:20px; }
  .step-num { display:table-cell; width:36px; vertical-align:top; }
  .step-num span { display:inline-block; width:28px; height:28px; border-radius:50%; background:#10b981; color:white; font-size:13px; font-weight:700; text-align:center; line-height:28px; }
  .step-text { display:table-cell; vertical-align:top; padding-left:12px; }
  .step-text strong { color:#111827; font-size:14px; }
  .step-text p { font-size:13px; color:#6b7280; margin:2px 0 0; }
  .cta { display:block; text-align:center; background:#10b981; color:white; text-decoration:none; padding:16px 32px; border-radius:10px; font-size:16px; font-weight:700; margin:8px 0; }
  .tip-box { background:#f0fdf4; border:1px solid #bbf7d0; border-radius:10px; padding:20px; margin-top:24px; }
  .tip-box h3 { font-size:14px; font-weight:700; color:#065f46; margin:0 0 6px; }
  .tip-box p { font-size:13px; color:#047857; margin:0; }
  .footer { padding:32px 40px; text-align:center; }
  .footer p { font-size:12px; color:#9ca3af; margin:0 0 4px; }
  .footer a { color:#9ca3af; }
</style>
</head>
<body>
<div class="wrapper">
  <div class="header">
    <h1>SNF Compare</h1>
    <p>For Nurses</p>
  </div>
  <div class="body">
    <h2>You're in. Here's how to use this.</h2>
    <p>SNF Compare gives you estimated pay, patient loads, and turnover rates at 15,000+ skilled nursing facilities — data most nurses never see until they're already hired.</p>

    <hr class="divider">

    <div class="step">
      <div class="step-num"><span>1</span></div>
      <div class="step-text">
        <strong>Pick your role</strong>
        <p>Filter by NP, RN, LPN, or CNA to see role-specific estimated wages and patient ratios.</p>
      </div>
    </div>
    <div class="step">
      <div class="step-num"><span>2</span></div>
      <div class="step-text">
        <strong>Search by location</strong>
        <p>Type a city, state, or facility name to narrow down your options.</p>
      </div>
    </div>
    <div class="step">
      <div class="step-num"><span>3</span></div>
      <div class="step-text">
        <strong>Compare side by side</strong>
        <p>Select 2-3 facilities and see pay, turnover, staffing, and inspection data in one view.</p>
      </div>
    </div>

    <a href="https://snfcompare.com/#tool" class="cta">Open the Compare Tool &rarr;</a>

    <div class="tip-box">
      <h3>Quick tip</h3>
      <p>Sort by "Best Pay" to instantly surface the highest-paying facilities in your search area. Then check the turnover rate — high pay + low turnover usually signals a well-run workplace.</p>
    </div>
  </div>
  <div class="footer">
    <p>SNF Compare — Powered by CMS data</p>
    <p><a href="#">Unsubscribe</a></p>
  </div>
</div>
</body>
</html>
```

</details>

---

## Nurse Email 2/3 — Day 2

> **Subject:** The 3 numbers that predict a bad workplace
> **Preview text:** Turnover, patient load, and deficiency count — here's what to look for.

<details>
<summary>View HTML</summary>

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>3 Numbers That Predict a Bad Workplace</title>
<style>
  body { margin:0; padding:0; background:#f8fafb; font-family:'Helvetica Neue',Arial,sans-serif; color:#1a1a1a; line-height:1.6; }
  .wrapper { max-width:600px; margin:0 auto; }
  .header { background:#111827; padding:32px 40px; text-align:center; }
  .header h1 { margin:0; color:white; font-size:22px; font-weight:700; }
  .header p { margin:6px 0 0; color:rgba(255,255,255,.5); font-size:13px; }
  .body { background:white; padding:40px; }
  .body h2 { font-size:20px; font-weight:700; color:#111827; margin:0 0 12px; line-height:1.3; }
  .body p { font-size:15px; color:#4b5563; margin:0 0 16px; }
  .divider { border:none; border-top:1px solid #f0f0f0; margin:24px 0; }
  .metric { border-radius:10px; padding:20px; margin-bottom:16px; }
  .metric.green { background:#f0fdf4; border-left:4px solid #10b981; }
  .metric.yellow { background:#fffbeb; border-left:4px solid #f59e0b; }
  .metric.red { background:#fef2f2; border-left:4px solid #ef4444; }
  .metric h3 { font-size:15px; font-weight:700; margin:0 0 4px; }
  .metric.green h3 { color:#065f46; }
  .metric.yellow h3 { color:#92400e; }
  .metric.red h3 { color:#991b1b; }
  .metric p { font-size:13px; margin:0; }
  .metric.green p { color:#047857; }
  .metric.yellow p { color:#b45309; }
  .metric.red p { color:#dc2626; }
  .cta { display:block; text-align:center; background:#10b981; color:white; text-decoration:none; padding:16px 32px; border-radius:10px; font-size:16px; font-weight:700; margin:8px 0; }
  .callout { background:#f8fafc; border-radius:10px; padding:20px; margin-top:24px; text-align:center; }
  .callout p { font-size:13px; color:#6b7280; margin:0; }
  .callout strong { color:#111827; }
  .footer { padding:32px 40px; text-align:center; }
  .footer p { font-size:12px; color:#9ca3af; margin:0 0 4px; }
  .footer a { color:#9ca3af; }
</style>
</head>
<body>
<div class="wrapper">
  <div class="header">
    <h1>SNF Compare</h1>
    <p>For Nurses</p>
  </div>
  <div class="body">
    <h2>3 numbers that tell you everything about a facility</h2>
    <p>Before you accept a position, check these three data points. They're publicly available on every facility in our tool — most nurses just don't know where to look.</p>

    <hr class="divider">

    <div class="metric red">
      <h3>1. Staff Turnover Rate</h3>
      <p><strong>Above 50%?</strong> That means more than half the nursing staff left in the past year. It almost always signals poor management, unsafe ratios, or burnout culture. Look for facilities under 30%.</p>
    </div>

    <div class="metric yellow">
      <h3>2. Patient-to-Nurse Ratio</h3>
      <p><strong>Compare your role specifically.</strong> A facility might advertise great RN numbers but overload CNAs. Use the role filter (NP/RN/LPN/CNA) to see the ratio that actually applies to you.</p>
    </div>

    <div class="metric green">
      <h3>3. Health Inspection Deficiencies</h3>
      <p><strong>0-2 deficiencies = strong.</strong> More than 5 means CMS found recurring problems. Check the facility detail page for the breakdown — infection control and resident rights deficiencies are the biggest red flags.</p>
    </div>

    <a href="https://snfcompare.com/#tool" class="cta">Check These Numbers Now &rarr;</a>

    <div class="callout">
      <p><strong>Pro move:</strong> Sort by "Low Turnover" in the compare tool, then cross-check pay. The sweet spot is facilities with under 30% turnover AND above-average wages for your role.</p>
    </div>
  </div>
  <div class="footer">
    <p>SNF Compare — Powered by CMS data</p>
    <p><a href="#">Unsubscribe</a></p>
  </div>
</div>
</body>
</html>
```

</details>

---

## Nurse Email 3/3 — Day 5

> **Subject:** Your facility comparison checklist (save this)
> **Preview text:** The exact process smart nurses use before accepting a position.

<details>
<summary>View HTML</summary>

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Your Facility Comparison Checklist</title>
<style>
  body { margin:0; padding:0; background:#f8fafb; font-family:'Helvetica Neue',Arial,sans-serif; color:#1a1a1a; line-height:1.6; }
  .wrapper { max-width:600px; margin:0 auto; }
  .header { background:#111827; padding:32px 40px; text-align:center; }
  .header h1 { margin:0; color:white; font-size:22px; font-weight:700; }
  .header p { margin:6px 0 0; color:rgba(255,255,255,.5); font-size:13px; }
  .body { background:white; padding:40px; }
  .body h2 { font-size:20px; font-weight:700; color:#111827; margin:0 0 12px; line-height:1.3; }
  .body p { font-size:15px; color:#4b5563; margin:0 0 16px; }
  .divider { border:none; border-top:1px solid #f0f0f0; margin:24px 0; }
  .checklist { margin:0; padding:0; list-style:none; }
  .checklist li { padding:12px 0; border-bottom:1px solid #f3f4f6; font-size:14px; color:#374151; display:flex; align-items:flex-start; gap:10px; }
  .checklist li:last-child { border-bottom:none; }
  .check { color:#10b981; font-size:16px; flex-shrink:0; line-height:1.4; }
  .checklist li strong { color:#111827; }
  .cta { display:block; text-align:center; background:#10b981; color:white; text-decoration:none; padding:16px 32px; border-radius:10px; font-size:16px; font-weight:700; margin:8px 0; }
  .cta-secondary { display:block; text-align:center; background:white; color:#10b981; text-decoration:none; padding:14px 32px; border-radius:10px; font-size:15px; font-weight:600; margin:8px 0; border:2px solid #10b981; }
  .closing { background:#f0fdf4; border-radius:10px; padding:20px; margin-top:24px; }
  .closing p { font-size:13px; color:#047857; margin:0; }
  .footer { padding:32px 40px; text-align:center; }
  .footer p { font-size:12px; color:#9ca3af; margin:0 0 4px; }
  .footer a { color:#9ca3af; }
</style>
</head>
<body>
<div class="wrapper">
  <div class="header">
    <h1>SNF Compare</h1>
    <p>For Nurses</p>
  </div>
  <div class="body">
    <h2>The facility comparison checklist</h2>
    <p>Bookmark this. Before you interview or accept a position at any SNF, run through this list using the compare tool. Takes about 5 minutes and could save you from a bad situation.</p>

    <hr class="divider">

    <ul class="checklist">
      <li><span class="check">&#9745;</span> <span><strong>Search the facility by name</strong> — confirm it's in the CMS database and check its overall star rating.</span></li>
      <li><span class="check">&#9745;</span> <span><strong>Filter by your role</strong> — switch to NP, RN, LPN, or CNA to see role-specific estimated wages and patient ratios.</span></li>
      <li><span class="check">&#9745;</span> <span><strong>Check turnover rate</strong> — under 30% is solid. Over 50% means something is wrong. This is the single best predictor of workplace quality.</span></li>
      <li><span class="check">&#9745;</span> <span><strong>Compare against 2 nearby facilities</strong> — use side-by-side comparison. Don't evaluate a facility in isolation; compare it against alternatives.</span></li>
      <li><span class="check">&#9745;</span> <span><strong>Open the full facility page</strong> — review inspection history, deficiency categories, penalty fines, and staffing hours per resident per day.</span></li>
      <li><span class="check">&#9745;</span> <span><strong>Check weekend staffing</strong> — some facilities staff well on weekdays and skeleton-crew on weekends. The facility detail page shows weekend hours separately.</span></li>
      <li><span class="check">&#9745;</span> <span><strong>Look at complaint history</strong> — substantiated complaints from residents and families often reveal issues that star ratings miss.</span></li>
    </ul>

    <a href="https://snfcompare.com/#tool" class="cta">Run Your Comparison Now &rarr;</a>
    <a href="https://snfcompare.com/#newsletter" class="cta-secondary">Get Weekly Industry Updates &rarr;</a>

    <div class="closing">
      <p>That's the end of the welcome series. From here, you'll receive periodic updates when we add new features or when CMS drops new data. Reply to any email if you have questions — we read everything.</p>
    </div>
  </div>
  <div class="footer">
    <p>SNF Compare — Powered by CMS data</p>
    <p><a href="#">Unsubscribe</a></p>
  </div>
</div>
</body>
</html>
```

</details>

---
---

# Flow 2 — Patients & Families

**Klaviyo List:** `Ty5RgF`
**Brand color:** `#4f46e5` (indigo)
**CTA style:** Indigo buttons linking to `https://snfcompare.com/#tool`

---

## Family Email 1/3 — Immediate

> **Subject:** How to tell if a nursing home is actually safe
> **Preview text:** CMS rates every facility in the US. Here's how to read the data.

<details>
<summary>View HTML</summary>

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Welcome to SNF Compare</title>
<style>
  body { margin:0; padding:0; background:#f8fafb; font-family:'Helvetica Neue',Arial,sans-serif; color:#1a1a1a; line-height:1.6; }
  .wrapper { max-width:600px; margin:0 auto; }
  .header { background:#111827; padding:32px 40px; text-align:center; }
  .header h1 { margin:0; color:white; font-size:22px; font-weight:700; }
  .header p { margin:6px 0 0; color:rgba(255,255,255,.5); font-size:13px; }
  .body { background:white; padding:40px; }
  .body h2 { font-size:20px; font-weight:700; color:#111827; margin:0 0 12px; line-height:1.3; }
  .body p { font-size:15px; color:#4b5563; margin:0 0 16px; }
  .divider { border:none; border-top:1px solid #f0f0f0; margin:24px 0; }
  .rating-row { display:table; width:100%; margin-bottom:16px; }
  .rating-icon { display:table-cell; width:44px; vertical-align:top; }
  .rating-icon span { display:inline-block; width:36px; height:36px; border-radius:8px; background:#eef2ff; color:#4f46e5; font-size:18px; text-align:center; line-height:36px; }
  .rating-text { display:table-cell; vertical-align:top; padding-left:12px; }
  .rating-text strong { font-size:14px; color:#111827; }
  .rating-text p { font-size:13px; color:#6b7280; margin:2px 0 0; }
  .cta { display:block; text-align:center; background:#4f46e5; color:white; text-decoration:none; padding:16px 32px; border-radius:10px; font-size:16px; font-weight:700; margin:8px 0; }
  .warn-box { background:#fef2f2; border:1px solid #fecaca; border-radius:10px; padding:20px; margin-top:24px; }
  .warn-box h3 { font-size:14px; font-weight:700; color:#991b1b; margin:0 0 6px; }
  .warn-box p { font-size:13px; color:#dc2626; margin:0; }
  .footer { padding:32px 40px; text-align:center; }
  .footer p { font-size:12px; color:#9ca3af; margin:0 0 4px; }
  .footer a { color:#9ca3af; }
</style>
</head>
<body>
<div class="wrapper">
  <div class="header">
    <h1>SNF Compare</h1>
    <p>For Families</p>
  </div>
  <div class="body">
    <h2>Every nursing home in the US is rated. Here's how to read it.</h2>
    <p>CMS (the government agency that oversees Medicare) inspects and rates every skilled nursing facility on a 1-5 star scale. SNF Compare puts all of that data in one place so you can compare facilities before making a decision.</p>

    <hr class="divider">

    <p style="font-size:14px;font-weight:700;color:#111827;margin-bottom:16px;">The 4 ratings that matter:</p>

    <div class="rating-row">
      <div class="rating-icon"><span>&#9733;</span></div>
      <div class="rating-text">
        <strong>Overall Rating</strong>
        <p>The combined score. 5 stars is the top 10% nationally. Below 3 means CMS has flagged consistent problems.</p>
      </div>
    </div>
    <div class="rating-row">
      <div class="rating-icon"><span>&#9736;</span></div>
      <div class="rating-text">
        <strong>Health Inspection</strong>
        <p>Based on the last 3 annual inspections. Measures how many deficiencies were found and how serious they were.</p>
      </div>
    </div>
    <div class="rating-row">
      <div class="rating-icon"><span>&#9678;</span></div>
      <div class="rating-text">
        <strong>Quality Measures</strong>
        <p>Tracks outcomes like falls, pressure ulcers, UTIs, and use of antipsychotic medications.</p>
      </div>
    </div>
    <div class="rating-row">
      <div class="rating-icon"><span>&#9734;</span></div>
      <div class="rating-text">
        <strong>Staffing</strong>
        <p>Nursing hours per resident per day. More staff time generally means better care and faster response.</p>
      </div>
    </div>

    <a href="https://snfcompare.com/#tool" class="cta">Compare Facilities Now &rarr;</a>

    <div class="warn-box">
      <h3>Important</h3>
      <p>Never rely on a facility's own website or brochure alone. CMS data comes from independent inspections. If a facility has a 1- or 2-star health inspection rating, that's based on documented problems found by government surveyors.</p>
    </div>
  </div>
  <div class="footer">
    <p>SNF Compare — Powered by CMS data</p>
    <p><a href="#">Unsubscribe</a></p>
  </div>
</div>
</body>
</html>
```

</details>

---

## Family Email 2/3 — Day 2

> **Subject:** 5 red flags in a nursing home's record
> **Preview text:** What deficiencies, complaints, and fines actually mean for your loved one.

<details>
<summary>View HTML</summary>

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>5 Red Flags in a Nursing Home Record</title>
<style>
  body { margin:0; padding:0; background:#f8fafb; font-family:'Helvetica Neue',Arial,sans-serif; color:#1a1a1a; line-height:1.6; }
  .wrapper { max-width:600px; margin:0 auto; }
  .header { background:#111827; padding:32px 40px; text-align:center; }
  .header h1 { margin:0; color:white; font-size:22px; font-weight:700; }
  .header p { margin:6px 0 0; color:rgba(255,255,255,.5); font-size:13px; }
  .body { background:white; padding:40px; }
  .body h2 { font-size:20px; font-weight:700; color:#111827; margin:0 0 12px; line-height:1.3; }
  .body p { font-size:15px; color:#4b5563; margin:0 0 16px; }
  .divider { border:none; border-top:1px solid #f0f0f0; margin:24px 0; }
  .flag { border-radius:10px; padding:16px 20px; margin-bottom:12px; background:#fef2f2; border-left:4px solid #ef4444; }
  .flag h3 { font-size:14px; font-weight:700; color:#991b1b; margin:0 0 4px; }
  .flag p { font-size:13px; color:#7f1d1d; margin:0; }
  .safe { border-radius:10px; padding:16px 20px; margin-top:24px; background:#f0fdf4; border-left:4px solid #10b981; }
  .safe h3 { font-size:14px; font-weight:700; color:#065f46; margin:0 0 4px; }
  .safe p { font-size:13px; color:#047857; margin:0; }
  .cta { display:block; text-align:center; background:#4f46e5; color:white; text-decoration:none; padding:16px 32px; border-radius:10px; font-size:16px; font-weight:700; margin:24px 0 8px; }
  .footer { padding:32px 40px; text-align:center; }
  .footer p { font-size:12px; color:#9ca3af; margin:0 0 4px; }
  .footer a { color:#9ca3af; }
</style>
</head>
<body>
<div class="wrapper">
  <div class="header">
    <h1>SNF Compare</h1>
    <p>For Families</p>
  </div>
  <div class="body">
    <h2>5 red flags to check before placing a loved one</h2>
    <p>Every facility page on SNF Compare shows detailed inspection, complaint, and penalty data. Here's what to watch for — and what each one means for your family member's safety.</p>

    <hr class="divider">

    <div class="flag">
      <h3>1. More than 5 health inspection deficiencies</h3>
      <p>The national average is about 7, but top-rated facilities have 2 or fewer. High deficiency counts across multiple inspection cycles mean the problems are systemic, not one-off.</p>
    </div>

    <div class="flag">
      <h3>2. Substantiated complaints</h3>
      <p>These are complaints filed by residents or families that CMS investigators confirmed to be valid. Even one substantiated complaint about abuse, neglect, or safety is serious.</p>
    </div>

    <div class="flag">
      <h3>3. Monetary fines or payment denials</h3>
      <p>CMS only fines facilities for serious or repeated violations. If a facility has been fined, check the facility detail page to see exactly when and how much — a pattern of fines means ongoing problems.</p>
    </div>

    <div class="flag">
      <h3>4. Infection control deficiencies</h3>
      <p>Infection control failures are the most common and most dangerous deficiency category. Look at the inspection breakdown on the facility detail page — recurring infection control issues put residents at direct risk.</p>
    </div>

    <div class="flag">
      <h3>5. Low staffing with high resident count</h3>
      <p>A facility with 150+ residents and a 1- or 2-star staffing rating means nurses are spread too thin. Check daily nursing hours per resident — below 3.5 total hours is a concern.</p>
    </div>

    <div class="safe">
      <h3>What a safe facility looks like</h3>
      <p>4-5 star overall rating, 2 or fewer deficiencies, zero substantiated complaints, no fines, and above-average nursing hours per resident per day. Use the compare tool to find these facilities in your area.</p>
    </div>

    <a href="https://snfcompare.com/#tool" class="cta">Check Facility Records &rarr;</a>
  </div>
  <div class="footer">
    <p>SNF Compare — Powered by CMS data</p>
    <p><a href="#">Unsubscribe</a></p>
  </div>
</div>
</body>
</html>
```

</details>

---

## Family Email 3/3 — Day 5

> **Subject:** Questions to ask on your nursing home tour (print this)
> **Preview text:** Pair these questions with the CMS data to get the real picture.

<details>
<summary>View HTML</summary>

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Questions for Your Nursing Home Tour</title>
<style>
  body { margin:0; padding:0; background:#f8fafb; font-family:'Helvetica Neue',Arial,sans-serif; color:#1a1a1a; line-height:1.6; }
  .wrapper { max-width:600px; margin:0 auto; }
  .header { background:#111827; padding:32px 40px; text-align:center; }
  .header h1 { margin:0; color:white; font-size:22px; font-weight:700; }
  .header p { margin:6px 0 0; color:rgba(255,255,255,.5); font-size:13px; }
  .body { background:white; padding:40px; }
  .body h2 { font-size:20px; font-weight:700; color:#111827; margin:0 0 12px; line-height:1.3; }
  .body p { font-size:15px; color:#4b5563; margin:0 0 16px; }
  .divider { border:none; border-top:1px solid #f0f0f0; margin:24px 0; }
  .question { padding:14px 0; border-bottom:1px solid #f3f4f6; }
  .question:last-child { border-bottom:none; }
  .question strong { font-size:14px; color:#111827; display:block; margin-bottom:2px; }
  .question p { font-size:13px; color:#6b7280; margin:0; }
  .question em { font-size:12px; color:#9ca3af; font-style:italic; }
  .cta { display:block; text-align:center; background:#4f46e5; color:white; text-decoration:none; padding:16px 32px; border-radius:10px; font-size:16px; font-weight:700; margin:8px 0; }
  .cta-secondary { display:block; text-align:center; background:white; color:#4f46e5; text-decoration:none; padding:14px 32px; border-radius:10px; font-size:15px; font-weight:600; margin:8px 0; border:2px solid #4f46e5; }
  .closing { background:#eef2ff; border:1px solid #e0e7ff; border-radius:10px; padding:20px; margin-top:24px; }
  .closing p { font-size:13px; color:#3730a3; margin:0; }
  .footer { padding:32px 40px; text-align:center; }
  .footer p { font-size:12px; color:#9ca3af; margin:0 0 4px; }
  .footer a { color:#9ca3af; }
</style>
</head>
<body>
<div class="wrapper">
  <div class="header">
    <h1>SNF Compare</h1>
    <p>For Families</p>
  </div>
  <div class="body">
    <h2>8 questions to ask when you visit a facility</h2>
    <p>A tour only shows you what they want you to see. These questions, paired with the CMS data you already have from SNF Compare, will give you the full picture.</p>

    <hr class="divider">

    <div class="question">
      <strong>"What is your current nurse-to-resident ratio on each shift?"</strong>
      <p>Compare their answer to the CMS staffing data on the facility page. If the numbers don't match, ask why.</p>
      <em>Cross-reference: Staffing section on the facility detail page</em>
    </div>

    <div class="question">
      <strong>"How many agency or temporary staff do you use?"</strong>
      <p>Heavy agency use often means high turnover. Consistent staff know the residents and provide better continuity of care.</p>
      <em>Cross-reference: Turnover rates in the compare tool</em>
    </div>

    <div class="question">
      <strong>"What were the findings from your last state inspection?"</strong>
      <p>You already have this data from SNF Compare. See if they're transparent about it or try to minimize deficiencies.</p>
      <em>Cross-reference: Inspection History section on the facility detail page</em>
    </div>

    <div class="question">
      <strong>"How do you handle falls prevention?"</strong>
      <p>Falls are the most common quality issue in nursing homes. Look for specific protocols, not vague assurances.</p>
      <em>Cross-reference: Quality Measures section — long-stay falls rate</em>
    </div>

    <div class="question">
      <strong>"What happens if my family member's condition changes?"</strong>
      <p>Ask about their escalation process, hospital transfer rates, and whether they offer different levels of care on-site.</p>
    </div>

    <div class="question">
      <strong>"Can I visit at any time, including evenings and weekends?"</strong>
      <p>Unrestricted visiting hours are a good sign. Facilities that limit visits may be hiding inadequate weekend staffing.</p>
      <em>Cross-reference: Weekend staffing hours on the facility detail page</em>
    </div>

    <div class="question">
      <strong>"Have you received any fines or penalties in the past 3 years?"</strong>
      <p>You already know the answer from SNF Compare. This question tests whether the facility is honest with families.</p>
      <em>Cross-reference: Penalty History section on the facility detail page</em>
    </div>

    <div class="question">
      <strong>"What is your staff turnover rate?"</strong>
      <p>National average is around 50%. Below 30% is excellent. If they can't answer or deflect, that's a red flag.</p>
      <em>Cross-reference: Turnover rate in the compare tool</em>
    </div>

    <a href="https://snfcompare.com/#tool" class="cta">Pull Up Facility Data Before Your Visit &rarr;</a>
    <a href="https://snfcompare.com/#newsletter" class="cta-secondary">Get Weekly Safety Updates &rarr;</a>

    <div class="closing">
      <p>That's the end of the welcome series. You'll continue to receive alerts when CMS releases new inspection data or rating changes for facilities in the database. Reply to any email if you need help — we're here.</p>
    </div>
  </div>
  <div class="footer">
    <p>SNF Compare — Powered by CMS data</p>
    <p><a href="#">Unsubscribe</a></p>
  </div>
</div>
</body>
</html>
```

</details>

---
---

# Flow 3 — Newsletter

**Klaviyo List:** `WKL5Uq`
**Brand color:** `#111827` (dark) with accent `#10b981`
**CTA style:** Dark buttons linking to `https://snfcompare.com/#newsletter` and `#tool`

---

## Newsletter Email 1/3 — Immediate

> **Subject:** Your first briefing: what's happening in skilled nursing right now
> **Preview text:** Rate increases, staffing mandates, and the data that matters this week.

<details>
<summary>View HTML</summary>

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Your First SNF Compare Briefing</title>
<style>
  body { margin:0; padding:0; background:#f8fafb; font-family:'Helvetica Neue',Arial,sans-serif; color:#1a1a1a; line-height:1.6; }
  .wrapper { max-width:600px; margin:0 auto; }
  .header { background:#111827; padding:32px 40px; text-align:center; }
  .header h1 { margin:0; color:white; font-size:22px; font-weight:700; }
  .header p { margin:6px 0 0; color:rgba(255,255,255,.5); font-size:13px; }
  .body { background:white; padding:40px; }
  .body h2 { font-size:20px; font-weight:700; color:#111827; margin:0 0 12px; line-height:1.3; }
  .body p { font-size:15px; color:#4b5563; margin:0 0 16px; }
  .divider { border:none; border-top:1px solid #f0f0f0; margin:24px 0; }
  .story { padding:16px 0; border-bottom:1px solid #f3f4f6; }
  .story:last-child { border-bottom:none; }
  .story-tag { display:inline-block; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:.05em; padding:2px 8px; border-radius:4px; margin-bottom:6px; }
  .story-tag.policy { background:#eef2ff; color:#4338ca; }
  .story-tag.staffing { background:#f0fdf4; color:#065f46; }
  .story-tag.finance { background:#fffbeb; color:#92400e; }
  .story-tag.compliance { background:#fef2f2; color:#991b1b; }
  .story h3 { font-size:15px; font-weight:700; color:#111827; margin:0 0 4px; }
  .story p { font-size:13px; color:#6b7280; margin:0; }
  .cta { display:block; text-align:center; background:#111827; color:white; text-decoration:none; padding:16px 32px; border-radius:10px; font-size:16px; font-weight:700; margin:24px 0 8px; }
  .footer { padding:32px 40px; text-align:center; }
  .footer p { font-size:12px; color:#9ca3af; margin:0 0 4px; }
  .footer a { color:#9ca3af; }
</style>
</head>
<body>
<div class="wrapper">
  <div class="header">
    <h1>SNF Compare</h1>
    <p>Weekly Briefing</p>
  </div>
  <div class="body">
    <h2>Welcome. Here's what you need to know right now.</h2>
    <p>Every Monday, you'll get a short briefing on the policy changes, market moves, and CMS data that affect skilled nursing. Here's a snapshot of what's happening this week.</p>

    <hr class="divider">

    <div class="story">
      <span class="story-tag policy">Reimbursement</span>
      <h3>CMS finalizes 3.7% SNF rate increase for FY2026</h3>
      <p>The final rule updates the SNF PPS rates effective October 2025, including adjustments to the parity adjustment and PDPM recalibration. Net positive for most operators.</p>
    </div>

    <div class="story">
      <span class="story-tag staffing">Staffing</span>
      <h3>Federal staffing mandate deadline: May 2026</h3>
      <p>Facilities must meet minimum RN (0.55 HPRD) and nurse aide (2.45 HPRD) thresholds. CMS estimates 75% of facilities currently fall short of at least one requirement.</p>
    </div>

    <div class="story">
      <span class="story-tag compliance">Compliance</span>
      <h3>OIG flags infection control gaps in 30% of surveyed facilities</h3>
      <p>New oversight report recommends stricter enforcement, targeted training, and more frequent infection control surveys in underperforming facilities.</p>
    </div>

    <div class="story">
      <span class="story-tag finance">M&amp;A</span>
      <h3>$820M acquisition reshapes Southeast market</h3>
      <p>Major regional chain acquires 45 facilities across five states. Expected to close Q2 2026. Watch for staffing and operational changes at affected locations.</p>
    </div>

    <table role="presentation" width="100%" cellspacing="8" style="margin-top:24px;">
      <tr>
        <td style="text-align:center;padding:16px;background:#f8fafc;border-radius:10px;width:25%"><div style="font-size:22px;font-weight:800;color:#111827">15K+</div><div style="font-size:11px;color:#6b7280;margin-top:2px">Facilities</div></td>
        <td style="text-align:center;padding:16px;background:#f8fafc;border-radius:10px;width:25%"><div style="font-size:22px;font-weight:800;color:#111827">3.7%</div><div style="font-size:11px;color:#6b7280;margin-top:2px">Rate Increase</div></td>
        <td style="text-align:center;padding:16px;background:#f8fafc;border-radius:10px;width:25%"><div style="font-size:22px;font-weight:800;color:#111827">1.3M</div><div style="font-size:11px;color:#6b7280;margin-top:2px">Residents</div></td>
        <td style="text-align:center;padding:16px;background:#f8fafc;border-radius:10px;width:25%"><div style="font-size:22px;font-weight:800;color:#111827">$108B</div><div style="font-size:11px;color:#6b7280;margin-top:2px">Industry Revenue</div></td>
      </tr>
    </table>

    <a href="https://snfcompare.com/#newsletter" class="cta">Read Full Coverage &rarr;</a>
  </div>
  <div class="footer">
    <p>SNF Compare — Powered by CMS data</p>
    <p>You're receiving this because you subscribed to the SNF Compare newsletter.</p>
    <p><a href="#">Unsubscribe</a></p>
  </div>
</div>
</body>
</html>
```

</details>

---

## Newsletter Email 2/3 — Day 3

> **Subject:** The compare tool most subscribers don't know about
> **Preview text:** Side-by-side facility data for 15,000+ nursing homes — free.

<details>
<summary>View HTML</summary>

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The SNF Compare Tool</title>
<style>
  body { margin:0; padding:0; background:#f8fafb; font-family:'Helvetica Neue',Arial,sans-serif; color:#1a1a1a; line-height:1.6; }
  .wrapper { max-width:600px; margin:0 auto; }
  .header { background:#111827; padding:32px 40px; text-align:center; }
  .header h1 { margin:0; color:white; font-size:22px; font-weight:700; }
  .header p { margin:6px 0 0; color:rgba(255,255,255,.5); font-size:13px; }
  .body { background:white; padding:40px; }
  .body h2 { font-size:20px; font-weight:700; color:#111827; margin:0 0 12px; line-height:1.3; }
  .body p { font-size:15px; color:#4b5563; margin:0 0 16px; }
  .divider { border:none; border-top:1px solid #f0f0f0; margin:24px 0; }
  .feature { display:table; width:100%; margin-bottom:20px; }
  .feature-icon { display:table-cell; width:44px; vertical-align:top; }
  .feature-icon span { display:inline-block; width:36px; height:36px; border-radius:8px; background:#f0fdf4; color:#10b981; font-size:18px; text-align:center; line-height:36px; }
  .feature-text { display:table-cell; vertical-align:top; padding-left:12px; }
  .feature-text strong { font-size:14px; color:#111827; }
  .feature-text p { font-size:13px; color:#6b7280; margin:2px 0 0; }
  .cta { display:block; text-align:center; background:#10b981; color:white; text-decoration:none; padding:16px 32px; border-radius:10px; font-size:16px; font-weight:700; margin:8px 0; }
  .cta-alt { display:block; text-align:center; background:#4f46e5; color:white; text-decoration:none; padding:16px 32px; border-radius:10px; font-size:16px; font-weight:700; margin:8px 0; }
  .or-text { text-align:center; font-size:13px; color:#9ca3af; margin:12px 0; }
  .footer { padding:32px 40px; text-align:center; }
  .footer p { font-size:12px; color:#9ca3af; margin:0 0 4px; }
  .footer a { color:#9ca3af; }
</style>
</head>
<body>
<div class="wrapper">
  <div class="header">
    <h1>SNF Compare</h1>
    <p>Weekly Briefing</p>
  </div>
  <div class="body">
    <h2>We also built a free compare tool.</h2>
    <p>In addition to the newsletter, SNF Compare has a side-by-side facility comparison tool covering 15,000+ skilled nursing facilities. It's free, uses official CMS data, and works on desktop and mobile.</p>

    <hr class="divider">

    <div class="feature">
      <div class="feature-icon"><span>$</span></div>
      <div class="feature-text">
        <strong>For Nurses</strong>
        <p>Estimated wages by role (NP/RN/LPN/CNA), patient-to-nurse ratios, turnover rates, and quality ratings. Sort by best pay or lowest patient load.</p>
      </div>
    </div>

    <div class="feature">
      <div class="feature-icon"><span>&#9829;</span></div>
      <div class="feature-text">
        <strong>For Families</strong>
        <p>CMS star ratings, inspection deficiencies, complaint history, fines, staffing levels, and quality measures. Everything you need before placing a loved one.</p>
      </div>
    </div>

    <div class="feature">
      <div class="feature-icon"><span>&#9776;</span></div>
      <div class="feature-text">
        <strong>Facility Detail Pages</strong>
        <p>Every facility has a dedicated page with full inspection history, penalty records, quality measure trends, and staffing breakdowns including weekend hours.</p>
      </div>
    </div>

    <div class="feature">
      <div class="feature-icon"><span>&#8646;</span></div>
      <div class="feature-text">
        <strong>Side-by-Side Comparison</strong>
        <p>Select 2-3 facilities and compare them across every data point. Ratings, staffing, wages, deficiencies, and quality — all in one view.</p>
      </div>
    </div>

    <a href="https://snfcompare.com/#tool" class="cta">Try the Nurse View &rarr;</a>
    <p class="or-text">or</p>
    <a href="https://snfcompare.com/#tool" class="cta-alt">Try the Family View &rarr;</a>
  </div>
  <div class="footer">
    <p>SNF Compare — Powered by CMS data</p>
    <p><a href="#">Unsubscribe</a></p>
  </div>
</div>
</body>
</html>
```

</details>

---

## Newsletter Email 3/3 — Day 6

> **Subject:** What to expect every Monday
> **Preview text:** Here's exactly what the weekly briefing covers and why it matters.

<details>
<summary>View HTML</summary>

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>What to Expect Every Monday</title>
<style>
  body { margin:0; padding:0; background:#f8fafb; font-family:'Helvetica Neue',Arial,sans-serif; color:#1a1a1a; line-height:1.6; }
  .wrapper { max-width:600px; margin:0 auto; }
  .header { background:#111827; padding:32px 40px; text-align:center; }
  .header h1 { margin:0; color:white; font-size:22px; font-weight:700; }
  .header p { margin:6px 0 0; color:rgba(255,255,255,.5); font-size:13px; }
  .body { background:white; padding:40px; }
  .body h2 { font-size:20px; font-weight:700; color:#111827; margin:0 0 12px; line-height:1.3; }
  .body p { font-size:15px; color:#4b5563; margin:0 0 16px; }
  .divider { border:none; border-top:1px solid #f0f0f0; margin:24px 0; }
  .topic { display:table; width:100%; margin-bottom:16px; padding-bottom:16px; border-bottom:1px solid #f3f4f6; }
  .topic:last-child { border-bottom:none; padding-bottom:0; margin-bottom:0; }
  .topic-tag { display:table-cell; width:100px; vertical-align:top; }
  .topic-tag span { display:inline-block; font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:.05em; padding:4px 8px; border-radius:4px; }
  .t-policy { background:#eef2ff; color:#4338ca; }
  .t-staffing { background:#f0fdf4; color:#065f46; }
  .t-finance { background:#fffbeb; color:#92400e; }
  .t-compliance { background:#fef2f2; color:#991b1b; }
  .t-data { background:#f0f9ff; color:#0c4a6e; }
  .topic-text { display:table-cell; vertical-align:top; padding-left:12px; }
  .topic-text strong { font-size:14px; color:#111827; }
  .topic-text p { font-size:13px; color:#6b7280; margin:2px 0 0; }
  .cta { display:block; text-align:center; background:#111827; color:white; text-decoration:none; padding:16px 32px; border-radius:10px; font-size:16px; font-weight:700; margin:24px 0 8px; }
  .closing { background:#f8fafc; border-radius:10px; padding:20px; margin-top:24px; text-align:center; }
  .closing p { font-size:13px; color:#6b7280; margin:0; }
  .closing strong { color:#111827; }
  .footer { padding:32px 40px; text-align:center; }
  .footer p { font-size:12px; color:#9ca3af; margin:0 0 4px; }
  .footer a { color:#9ca3af; }
</style>
</head>
<body>
<div class="wrapper">
  <div class="header">
    <h1>SNF Compare</h1>
    <p>Weekly Briefing</p>
  </div>
  <div class="body">
    <h2>Here's what you'll get every Monday.</h2>
    <p>The SNF Compare briefing is a short, no-fluff digest of what's happening in skilled nursing. We cover the topics that actually affect operations, staffing, and patient care — sourced from CMS releases, OIG reports, state surveys, and industry filings.</p>

    <hr class="divider">

    <div class="topic">
      <div class="topic-tag"><span class="t-policy">Policy</span></div>
      <div class="topic-text">
        <strong>Reimbursement &amp; Regulation</strong>
        <p>Medicare/Medicaid rate changes, PDPM updates, proposed rules, and final rule analysis. What it means for your bottom line.</p>
      </div>
    </div>

    <div class="topic">
      <div class="topic-tag"><span class="t-staffing">Staffing</span></div>
      <div class="topic-text">
        <strong>Workforce &amp; Mandates</strong>
        <p>Federal and state staffing requirements, turnover trends, wage benchmarking, and recruitment strategies that are working.</p>
      </div>
    </div>

    <div class="topic">
      <div class="topic-tag"><span class="t-compliance">Compliance</span></div>
      <div class="topic-text">
        <strong>Surveys &amp; Enforcement</strong>
        <p>OIG reports, state survey trends, enforcement actions, deficiency patterns, and what surveyors are focusing on.</p>
      </div>
    </div>

    <div class="topic">
      <div class="topic-tag"><span class="t-finance">Finance</span></div>
      <div class="topic-text">
        <strong>M&amp;A &amp; Market Moves</strong>
        <p>Acquisitions, divestitures, bankruptcies, and ownership changes. Who's buying, who's selling, and what it means for the market.</p>
      </div>
    </div>

    <div class="topic">
      <div class="topic-tag"><span class="t-data">Data</span></div>
      <div class="topic-text">
        <strong>CMS Data Drops</strong>
        <p>When CMS releases new quality ratings, inspection results, or staffing data, we break down the highlights and what changed.</p>
      </div>
    </div>

    <a href="https://snfcompare.com/#newsletter" class="cta">Read This Week's Briefing &rarr;</a>

    <div class="closing">
      <p>That's the welcome series. Starting next Monday, you'll receive the weekly briefing. <strong>Reply to any email if you have feedback or topic requests</strong> — we read everything and build coverage around what readers ask for.</p>
    </div>
  </div>
  <div class="footer">
    <p>SNF Compare — Powered by CMS data</p>
    <p><a href="#">Unsubscribe</a></p>
  </div>
</div>
</body>
</html>
```

</details>

---
---

# Summary

| Flow | List | Email 1 (Day 0) | Email 2 (Day 2-3) | Email 3 (Day 5-6) |
|------|------|-----------------|--------------------|--------------------|
| **Nurses** | `Y6tGhQ` | How to use the tool | 3 numbers that predict a bad workplace | Facility comparison checklist |
| **Families** | `Ty5RgF` | How CMS ratings work | 5 red flags to check | Questions for your facility tour |
| **Newsletter** | `WKL5Uq` | This week's top stories | Intro to the compare tool | What to expect every Monday |

### Design Specs

| Element | Nurses | Families | Newsletter |
|---------|--------|----------|------------|
| Header | `#111827` dark | `#111827` dark | `#111827` dark |
| Subtitle | "For Nurses" | "For Families" | "Weekly Briefing" |
| CTA color | `#10b981` green | `#4f46e5` indigo | `#111827` dark |
| Accent | Green tips/steps | Red flags / indigo | Category tags |
| Primary link | `/#tool` | `/#tool` | `/#newsletter` |
