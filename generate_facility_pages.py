#!/usr/bin/env python3
"""Generate individual facility profile pages from CMS nursing home data."""
import csv
import os
import sys
import html as html_mod
import random
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'facility')
COST_REPORT_PATH = os.path.join(DATA_DIR, 'Skilled Nursing Facility Cost Report', '2023', 'CostReportsnf_Final_23.csv')

STATE_MIN_WAGES = {
    'AL': 7.25, 'AK': 11.91, 'AZ': 14.70, 'AR': 11.00, 'CA': 16.50,
    'CO': 14.81, 'CT': 16.35, 'DE': 15.00, 'DC': 17.50, 'FL': 13.00,
    'GA': 7.25, 'HI': 14.00, 'ID': 7.25, 'IL': 15.00, 'IN': 7.25,
    'IA': 7.25, 'KS': 7.25, 'KY': 7.25, 'LA': 7.25, 'ME': 14.65,
    'MD': 15.00, 'MA': 15.00, 'MI': 10.56, 'MN': 11.13, 'MS': 7.25,
    'MO': 13.75, 'MT': 10.55, 'NE': 13.50, 'NV': 12.00, 'NH': 7.25,
    'NJ': 15.49, 'NM': 12.00, 'NY': 15.50, 'NC': 7.25, 'ND': 7.25,
    'OH': 10.70, 'OK': 7.25, 'OR': 14.70, 'PA': 7.25, 'RI': 15.00,
    'SC': 7.25, 'SD': 11.50, 'TN': 7.25, 'TX': 7.25, 'UT': 7.25,
    'VT': 14.01, 'VA': 12.41, 'WA': 16.66, 'WV': 8.75, 'WI': 7.25,
    'WY': 7.25,
}

WAGE_MULT = {'NP': 3.0, 'RN': 2.2, 'LPN': 1.4, 'CNA': 0.7}
WAGE_BOUNDS = {'NP': (20, 250), 'RN': (15, 180), 'LPN': (8, 120), 'CNA': (5, 60)}
IQR_UPPER = {'NP': 172.08, 'RN': 126.20, 'LPN': 80.32, 'CNA': 36.12}

# ── Image handling ─────────────────────────────────────────────────────────────
IMAGES_DIR = os.path.join(BASE_DIR, 'images', 'facilities')
FALLBACK_IMAGES = ['facility1.png', 'facility2.png', 'facility3.png', 'facility4.png']
MIN_IMAGE_SIZE = 10000  # Images under 10KB are likely grey placeholders

def get_valid_images():
    """Scan facilities images folder and return set of CCNs with valid (non-grey) images."""
    valid = set()
    if os.path.exists(IMAGES_DIR):
        for f in os.listdir(IMAGES_DIR):
            if f.endswith('.jpg'):
                path = os.path.join(IMAGES_DIR, f)
                if os.path.getsize(path) >= MIN_IMAGE_SIZE:
                    valid.add(f.replace('.jpg', ''))
    return valid

def get_image_path(ccn, valid_images):
    """Return image path for a facility - real image or random fallback."""
    if ccn in valid_images:
        return f'../images/facilities/{ccn}.jpg'
    else:
        return f'../images/facilities2/{random.choice(FALLBACK_IMAGES)}'

# ── Utility functions ──────────────────────────────────────────────────────────

def safe_float(v):
    if v is None or str(v).strip() == '':
        return None
    try:
        return float(str(v).replace(',', '').replace('$', '').replace('%', '').strip())
    except (ValueError, TypeError):
        return None

def safe_int(v):
    f = safe_float(v)
    return int(f) if f is not None else None

def esc(s):
    return html_mod.escape(str(s)) if s else ''

def fmt_pct(v):
    f = safe_float(v)
    if f is None:
        return 'N/A'
    return f'{int(f)}%' if f == int(f) else f'{f:.1f}%'

def fmt_pct_val(f):
    """Format a float percentage, stripping .0 if whole number"""
    return f'{int(f)}%' if f == int(f) else f'{f:.1f}%'

def fmt_dollars(v):
    f = safe_float(v)
    if f is None:
        return 'N/A'
    return f'${f:,.0f}'

def fmt_hrs(v):
    f = safe_float(v)
    return f'{f:.2f}' if f is not None else 'N/A'

def fmt_wage(v):
    if v is None:
        return 'N/A'
    return f'${v:.2f}'

def star_rating_html(rating):
    r = safe_int(rating)
    if r is None:
        return '<span class="na">N/A</span>'
    stars = ''
    for i in range(1, 6):
        cls = 'filled' if i <= r else 'empty'
        stars += f'<svg class="star {cls}" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>'
    return f'<div class="stars">{stars}</div>'

def rating_card_bg(rating):
    r = safe_int(rating)
    bgs = {
        5: 'linear-gradient(135deg, #10b981, #059669)',
        4: 'linear-gradient(135deg, #14b8a6, #0d9488)',
        3: 'linear-gradient(135deg, #f59e0b, #d97706)',
        2: 'linear-gradient(135deg, #f97316, #ea580c)',
        1: 'linear-gradient(135deg, #ef4444, #dc2626)',
    }
    return bgs.get(r, 'linear-gradient(135deg, #9ca3af, #6b7280)')

# ── Data loading ───────────────────────────────────────────────────────────────

def read_csv(path, encoding='utf-8-sig'):
    with open(path, 'r', encoding=encoding, errors='replace') as f:
        return list(csv.DictReader(f))

def load_provider_info():
    rows = read_csv(os.path.join(DATA_DIR, 'NH_ProviderInfo_Nov2025.csv'))
    providers = {}
    for r in rows:
        ccn = r.get('CMS Certification Number (CCN)', '').strip()
        if ccn:
            providers[ccn] = r
    return providers

def load_quality_measures():
    rows = read_csv(os.path.join(DATA_DIR, 'NH_QualityMsr_MDS_Nov2025.csv'))
    measures = defaultdict(list)
    for r in rows:
        ccn = r.get('CMS Certification Number (CCN)', '').strip()
        if ccn:
            measures[ccn].append(r)
    return dict(measures)

def load_penalties():
    rows = read_csv(os.path.join(DATA_DIR, 'NH_Penalties_Nov2025.csv'))
    penalties = defaultdict(list)
    for r in rows:
        ccn = r.get('CMS Certification Number (CCN)', '').strip()
        if ccn:
            penalties[ccn].append(r)
    return dict(penalties)

def load_survey_summary():
    rows = read_csv(os.path.join(DATA_DIR, 'NH_SurveySummary_Nov2025.csv'))
    surveys = defaultdict(list)
    for r in rows:
        ccn = r.get('CMS Certification Number (CCN)', '').strip()
        if ccn:
            surveys[ccn].append(r)
    return dict(surveys)

def load_cost_report():
    rows = read_csv(COST_REPORT_PATH)
    costs = {}
    for r in rows:
        ccn = r.get('Provider CCN', '').strip()
        if ccn:
            costs[ccn] = r
    return costs

# ── Wage computation ───────────────────────────────────────────────────────────

def compute_wages(provider, cost_data):
    total_sal = safe_float(cost_data.get('Total Salaries (adjusted)'))
    contract = safe_float(cost_data.get('Contract Labor'))
    avg_res = safe_float(provider.get('Average Number of Residents per Day'))
    rn_hrs = safe_float(provider.get('Reported RN Staffing Hours per Resident per Day'))
    lpn_hrs = safe_float(provider.get('Reported LPN Staffing Hours per Resident per Day'))
    cna_hrs = safe_float(provider.get('Reported Nurse Aide Staffing Hours per Resident per Day'))
    state = provider.get('State', '').strip()

    if total_sal is None or avg_res is None or avg_res <= 0:
        return None
    if rn_hrs is None or lpn_hrs is None or cna_hrs is None:
        return None

    contract = contract or 0
    emp_sal = total_sal - contract
    if emp_sal <= 0:
        return None
    nursing_budget = emp_sal * 0.72

    np_hrs = 8.0 / avg_res
    annual = {
        'NP': np_hrs * avg_res * 365,
        'RN': rn_hrs * avg_res * 365,
        'LPN': lpn_hrs * avg_res * 365,
        'CNA': cna_hrs * avg_res * 365,
    }

    weighted = sum(annual[role] * WAGE_MULT[role] for role in WAGE_MULT)
    if weighted <= 0:
        return None

    base_wage = nursing_budget / weighted
    wages = {role: base_wage * mult for role, mult in WAGE_MULT.items()}

    # Apply state minimum wage floor for CNA
    min_wage = STATE_MIN_WAGES.get(state, 7.25)
    if wages['CNA'] < min_wage:
        wages['CNA'] = min_wage
        cna_cost = annual['CNA'] * min_wage
        remaining = nursing_budget - cna_cost
        if remaining <= 0:
            return None
        weighted_rem = sum(annual[r] * WAGE_MULT[r] for r in ('NP', 'RN', 'LPN'))
        if weighted_rem <= 0:
            return None
        adj_base = remaining / weighted_rem
        for r in ('NP', 'RN', 'LPN'):
            wages[r] = adj_base * WAGE_MULT[r]

    # Bounds check
    for role, (lo, hi) in WAGE_BOUNDS.items():
        if wages[role] < lo or wages[role] > hi:
            return None

    return wages

def apply_iqr_filter(all_wages):
    for ccn, w in list(all_wages.items()):
        if w is None:
            continue
        for role, upper in IQR_UPPER.items():
            if w[role] > upper:
                all_wages[ccn] = None
                break
    return all_wages

# ── CSS ────────────────────────────────────────────────────────────────────────

PAGE_CSS = """
*{margin:0;padding:0;box-sizing:border-box}
:root{--primary:#0d9488;--primary-dark:#0f766e;--accent:#10b981;--text:#111827;--text-muted:#6b7280;--bg:#f8fafc;--card:#ffffff;--border:#e5e7eb;--shadow-sm:0 1px 2px rgba(0,0,0,0.04);--shadow:0 4px 6px -1px rgba(0,0,0,0.07),0 2px 4px -1px rgba(0,0,0,0.04);--shadow-lg:0 20px 40px -12px rgba(0,0,0,0.12);--radius:16px;--radius-sm:12px}
body{font-family:'Plus Jakarta Sans',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:linear-gradient(180deg,#f0fdfa 0%,#f8fafc 100%);background-attachment:fixed;color:var(--text);line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--primary);text-decoration:none;transition:color .2s}
a:hover{color:var(--primary-dark)}
.container{max-width:980px;margin:0 auto;padding:0 24px}
.header{background:rgba(255,255,255,0.85);border-bottom:1px solid rgba(229,231,235,0.8);padding:14px 0;position:sticky;top:0;z-index:250;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.header-inner{display:flex;align-items:center;justify-content:space-between;max-width:980px;margin:0 auto;padding:0 24px}
.back-link{display:flex;align-items:center;gap:8px;color:var(--text-muted);font-size:14px;font-weight:600;padding:8px 14px;border-radius:10px;transition:all .2s}
.back-link:hover{color:var(--text);background:rgba(0,0,0,0.04);text-decoration:none}
.logo{display:flex;align-items:center;gap:8px;font-weight:800;font-size:18px;color:var(--text);text-decoration:none}
.logo-badge{background:linear-gradient(135deg,#10b981 0%,#059669 100%);color:white;padding:4px 10px;border-radius:8px;font-size:12px;font-weight:700;letter-spacing:0.3px;box-shadow:0 2px 8px rgba(16,185,129,0.3)}
.hero{background:linear-gradient(135deg,#ffffff 0%,#f0fdfa 100%);border-bottom:1px solid var(--border);padding:40px 0 36px;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;top:-50%;right:-20%;width:60%;height:200%;background:radial-gradient(circle,rgba(16,185,129,0.06) 0%,transparent 70%);pointer-events:none}
.hero .container{position:relative}
.hero-badge{display:inline-flex;align-items:center;gap:6px;background:linear-gradient(135deg,#ecfdf5,#d1fae5);color:#065f46;padding:6px 14px;border-radius:20px;font-size:12px;font-weight:600;margin-bottom:16px;border:1px solid rgba(16,185,129,0.2)}
.hero-badge svg{width:14px;height:14px}
.hero h1{font-size:32px;font-weight:800;color:var(--text);margin-bottom:8px;letter-spacing:-0.5px}
.hero .address{color:var(--text-muted);font-size:15px;margin-bottom:4px;display:flex;align-items:center;gap:6px}
.hero .address svg{width:16px;height:16px;opacity:0.5}
.hero .phone{font-size:15px;font-weight:600}
.hero .phone a{color:var(--primary);display:inline-flex;align-items:center;gap:6px}
.hero .phone a:hover{color:var(--primary-dark)}
.hero .phone svg{width:16px;height:16px}
.hero-grid{display:grid;grid-template-columns:1fr 1fr;gap:32px;align-items:center}
.hero-image{border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow-lg)}
.hero-image img{width:100%;height:260px;object-fit:cover;display:block}
@media(max-width:700px){.hero-grid{grid-template-columns:1fr;gap:20px}.hero-image{order:-1}.hero-image img{height:200px}}
.section{margin:28px auto;max-width:980px;padding:0 24px}
.card{background:var(--card);border-radius:var(--radius);box-shadow:var(--shadow);border:1px solid rgba(0,0,0,0.04);overflow:hidden;margin-bottom:24px;transition:box-shadow .3s,transform .3s}
.card:hover{box-shadow:var(--shadow-lg);transform:translateY(-2px)}
.card-header{padding:18px 24px;border-bottom:1px solid #f3f4f6;background:linear-gradient(180deg,#fafbfc 0%,#f8f9fa 100%);display:flex;align-items:center;justify-content:space-between}
.card-header h2{font-size:15px;font-weight:700;color:var(--text);text-transform:uppercase;letter-spacing:0.5px;display:flex;align-items:center;gap:10px}
.card-header h2::before{content:'';width:4px;height:18px;background:linear-gradient(180deg,var(--accent),var(--primary));border-radius:2px}
.section-info{position:relative;display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;border-radius:50%;background:#e5e7eb;cursor:pointer;flex-shrink:0}
.section-info svg{width:12px;height:12px;stroke:#6b7280}
.section-info .tip{position:absolute;left:50%;top:calc(100% + 8px);transform:translateX(-50%);background:#1f2937;color:white;padding:10px 14px;border-radius:8px;font-size:12px;font-weight:500;white-space:normal;width:280px;text-transform:none;letter-spacing:normal;line-height:1.5;opacity:0;visibility:hidden;transition:all .2s;z-index:100;box-shadow:0 4px 12px rgba(0,0,0,0.2);text-align:left}
.section-info .tip::before{content:'';position:absolute;top:-6px;left:50%;transform:translateX(-50%);border:6px solid transparent;border-bottom-color:#1f2937}
.section-info:hover .tip{opacity:1;visibility:visible}
@media(max-width:600px){.section-info .tip{width:220px;left:0;transform:none}.section-info .tip::before{left:9px;transform:none}}
.card-body{padding:24px}
.ratings-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
@media(max-width:700px){.ratings-grid{grid-template-columns:repeat(2,1fr)}}
.rating-card{border-radius:var(--radius);padding:24px 16px;text-align:center;color:white;position:relative;overflow:hidden;box-shadow:0 4px 15px rgba(0,0,0,0.1);transition:transform .2s,box-shadow .2s}
.rating-card:hover{transform:translateY(-3px);box-shadow:0 8px 25px rgba(0,0,0,0.15)}
.rating-card::before{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:linear-gradient(180deg,rgba(255,255,255,0.15) 0%,transparent 50%);pointer-events:none}
.rating-card .val{font-size:42px;font-weight:800;text-shadow:0 2px 10px rgba(0,0,0,0.15);position:relative}
.rating-card .stars{display:flex;justify-content:center;gap:4px;margin:10px 0 8px;position:relative}
.rating-card .stars svg{width:22px;height:22px;filter:drop-shadow(0 1px 2px rgba(0,0,0,0.2))}
.rating-card .stars .filled{color:#fbbf24}
.rating-card .stars .empty{color:rgba(255,255,255,0.3)}
.rating-card .lbl{font-size:11px;font-weight:700;opacity:0.95;text-transform:uppercase;letter-spacing:0.8px;position:relative}
.rating-card .na{font-size:32px;font-weight:700;opacity:0.7}
table{width:100%;border-collapse:separate;border-spacing:0;font-size:14px}
th{text-align:left;padding:12px 16px;background:#f8fafc;color:var(--text-muted);font-weight:700;font-size:12px;text-transform:uppercase;letter-spacing:0.5px;border-bottom:2px solid var(--border)}
td{padding:14px 16px;border-bottom:1px solid #f3f4f6;color:#374151;transition:background .15s}
tr:last-child td{border-bottom:none}
tbody tr:hover td{background:#f8fdfb}
tbody tr:nth-child(even) td{background:#fafbfc}
tbody tr:nth-child(even):hover td{background:#f0fdf9}
.val-good{color:#059669;font-weight:700}
.val-warn{color:#d97706;font-weight:700}
.val-bad{color:#dc2626;font-weight:700}
.val-na{color:#9ca3af}
.wages-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
@media(max-width:700px){.wages-grid{grid-template-columns:repeat(2,1fr)}}
.wage-card{background:linear-gradient(135deg,#ecfdf5 0%,#d1fae5 100%);border-radius:var(--radius-sm);padding:24px 16px;text-align:center;border:1px solid rgba(16,185,129,0.15);transition:transform .2s,box-shadow .2s}
.wage-card:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(16,185,129,0.15)}
.wage-card .val{font-size:28px;font-weight:800;color:#047857;letter-spacing:-0.5px}
.wage-card .lbl{font-size:11px;color:#059669;font-weight:700;margin-top:6px;text-transform:uppercase;letter-spacing:0.5px}
.info-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}
@media(max-width:700px){.info-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:480px){.info-grid{grid-template-columns:1fr}}
.info-item{padding:16px;background:#fafbfc;border-radius:var(--radius-sm);border:1px solid #f0f0f0;transition:all .2s}
.info-item:hover{background:#f0fdf9;border-color:rgba(16,185,129,0.2)}
.info-item .lbl{font-size:11px;color:var(--text-muted);font-weight:600;margin-bottom:4px;text-transform:uppercase;letter-spacing:0.4px}
.info-item .val{font-size:15px;color:var(--text);font-weight:700}
.turnover-grid{display:flex;gap:16px;flex-wrap:wrap;margin-top:20px}
.turnover-card{background:#fafbfc;border:1px solid #e5e7eb;border-radius:var(--radius-sm);padding:20px 24px;min-width:140px;text-align:center}
.turnover-val{font-size:24px;font-weight:800;color:var(--text);margin-bottom:4px}
.turnover-lbl{font-size:11px;color:var(--text-muted);font-weight:600;text-transform:uppercase;letter-spacing:0.3px}
.badge{display:inline-flex;align-items:center;padding:4px 12px;border-radius:20px;font-size:12px;font-weight:700}
.badge-green{background:linear-gradient(135deg,#ecfdf5,#d1fae5);color:#065f46;border:1px solid rgba(16,185,129,0.2)}
.badge-red{background:linear-gradient(135deg,#fef2f2,#fee2e2);color:#991b1b;border:1px solid rgba(239,68,68,0.2)}
.badge-amber{background:linear-gradient(135deg,#fffbeb,#fef3c7);color:#92400e;border:1px solid rgba(245,158,11,0.2)}
.badge-blue{background:linear-gradient(135deg,#eff6ff,#dbeafe);color:#1e40af;border:1px solid rgba(59,130,246,0.2)}
.badge-gray{background:#f3f4f6;color:#374151;border:1px solid #e5e7eb}
.safety-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
@media(max-width:800px){.safety-grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:480px){.safety-grid{grid-template-columns:1fr}}
.safety-card{border-radius:var(--radius-sm);padding:20px;text-align:center;border:1px solid #f0f0f0;background:linear-gradient(180deg,#ffffff 0%,#fafbfc 100%);transition:all .2s}
.safety-card:hover{border-color:rgba(16,185,129,0.3);box-shadow:0 4px 12px rgba(0,0,0,0.06)}
.safety-card .val{font-size:28px;font-weight:800;letter-spacing:-0.5px}
.safety-card .lbl{font-size:11px;color:var(--text-muted);font-weight:600;margin-top:6px;text-transform:uppercase;letter-spacing:0.3px;line-height:1.4}
.qm-type{font-size:12px;font-weight:700;color:#065f46;padding:14px 24px;background:linear-gradient(90deg,#ecfdf5,#d1fae5);border-bottom:1px solid rgba(16,185,129,0.2);text-transform:uppercase;letter-spacing:0.8px;display:flex;align-items:center;gap:8px}
.qm-type::before{content:'';width:8px;height:8px;background:var(--accent);border-radius:50%}
.empty-state{padding:40px 24px;text-align:center;color:var(--text-muted);font-size:14px;font-weight:500}
@media(max-width:480px){
.container{padding:0 16px}
.hero{padding:24px 0 20px}
.hero h1{font-size:22px;line-height:1.3}
.hero .address{font-size:13px;flex-wrap:wrap}
.hero .phone{font-size:14px}
.hero-badge{font-size:11px;padding:5px 10px;margin-bottom:12px}
.section{padding:0 12px;margin:20px auto}
.card{margin-bottom:16px;border-radius:12px}
.card-header{padding:14px 16px}
.card-header h2{font-size:13px;gap:8px}
.card-header h2::before{width:3px;height:14px}
.card-body{padding:16px}
.rating-card{padding:16px 12px;border-radius:10px}
.rating-card .val{font-size:32px}
.rating-card .stars svg{width:16px;height:16px}
.rating-card .lbl{font-size:10px}
table{font-size:12px}
th,td{padding:10px 12px}
th{font-size:10px}
td:first-child{min-width:180px;white-space:normal}
.wage-card{padding:16px 12px}
.wage-card .val{font-size:22px}
.wage-card .lbl{font-size:10px}
.info-item{padding:12px}
.info-item .lbl{font-size:10px}
.info-item .val{font-size:14px}
.turnover-grid{gap:10px}
.turnover-card{padding:14px 16px;min-width:auto;flex:1}
.turnover-val{font-size:20px}
.turnover-lbl{font-size:10px}
.safety-card{padding:14px}
.safety-card .val{font-size:22px}
.safety-card .lbl{font-size:10px}
.qm-type{padding:10px 16px;font-size:11px}
.disclaimer{padding:16px;font-size:11px;margin:16px 12px 0}
}
.footer{background:linear-gradient(180deg,#111827 0%,#0f172a 100%);padding:48px 24px;margin-top:48px;color:#9ca3af;font-size:13px}
.footer-inner{max-width:980px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:20px}
.footer-logo{display:flex;align-items:center;gap:8px;color:white;font-weight:800;font-size:16px}
.footer-links{display:flex;gap:24px}
.footer-links a{color:#9ca3af;font-size:14px;font-weight:500;transition:color .2s}
.footer-links a:hover{color:white}
.disclaimer{max-width:980px;margin:24px auto 0;padding:20px 24px;font-size:12px;color:#9ca3af;line-height:1.7;text-align:center;background:rgba(255,255,255,0.5);border-radius:var(--radius-sm);border:1px solid rgba(0,0,0,0.04)}
.content-gated{filter:blur(8px);-webkit-filter:blur(8px);pointer-events:none;user-select:none;transition:filter .4s}
.gate-overlay{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.6);z-index:200;display:flex;align-items:center;justify-content:center;padding:20px;backdrop-filter:blur(4px)}
.gate-overlay.gate-hidden{display:none}
.gate-modal{background:white;border-radius:24px;max-width:420px;width:100%;text-align:center;box-shadow:0 32px 100px rgba(0,0,0,.4);overflow:hidden}
.gate-modal .gate-accent{height:5px;background:linear-gradient(90deg,#10b981,#0d9488,#14b8a6,#10b981);background-size:200% 100%;animation:shimmer 3s ease infinite}
@keyframes shimmer{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
.gate-modal .gate-body{padding:40px 36px 32px}
.gate-modal h2{font-size:24px;font-weight:800;color:var(--text);margin-bottom:8px;letter-spacing:-0.3px}
.gate-modal .gate-sub{font-size:14px;color:var(--text-muted);margin-bottom:28px;line-height:1.6}
.gate-modal .gate-form{display:flex;flex-direction:column;gap:12px}
.gate-modal input[type=email]{width:100%;padding:16px 18px;border:2px solid var(--border);border-radius:14px;font-size:16px;font-family:inherit;outline:none;transition:all .2s;box-sizing:border-box}
.gate-modal input[type=email]:focus{border-color:var(--accent);box-shadow:0 0 0 4px rgba(16,185,129,0.1)}
.gate-modal button[type=submit]{width:100%;padding:16px;border:none;border-radius:14px;background:linear-gradient(135deg,#10b981,#059669);color:white;font-size:16px;font-weight:700;font-family:inherit;cursor:pointer;transition:all .2s;box-shadow:0 4px 14px rgba(16,185,129,.3)}
.gate-modal button[type=submit]:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(16,185,129,.4)}
.gate-modal button[type=submit]:active{transform:scale(.98)}
.gate-modal button[type=submit]:disabled{opacity:.5;cursor:not-allowed;transform:none;box-shadow:none}
.gate-modal .gate-privacy{font-size:12px;color:#9ca3af;margin-top:20px}
.gate-modal .gate-error{color:#dc2626;font-size:13px;margin-top:8px;display:none}
.gate-modal .gate-divider{height:1px;background:#f0f0f0;margin:24px 0 0}
.gate-modal .gate-back{display:block;padding:16px;color:var(--text-muted);font-size:14px;font-weight:600;text-decoration:none;transition:all .2s}
.gate-modal .gate-back:hover{color:var(--text);background:#fafbfc;text-decoration:none}
"""

# ── HTML generation ────────────────────────────────────────────────────────────

def build_ratings_section(p):
    cards = []
    for key, label in [('Overall Rating', 'Overall'), ('Health Inspection Rating', 'Health Inspection'),
                        ('QM Rating', 'Quality Measures'), ('Staffing Rating', 'Staffing')]:
        r = safe_int(p.get(key))
        bg = rating_card_bg(r)
        val_html = f'<div class="val">{r}</div>{star_rating_html(r)}' if r else '<div class="na">N/A</div>'
        cards.append(f'<div class="rating-card" style="background:{bg}">{val_html}<div class="lbl">{label}</div></div>')
    return f'<div class="ratings-grid">{"".join(cards)}</div>'

def build_staffing_table(p):
    rows_data = [
        ('Registered Nurse (RN)',
         p.get('Reported RN Staffing Hours per Resident per Day'),
         p.get('Case-Mix RN Staffing Hours per Resident per Day'),
         p.get('Registered Nurse hours per resident per day on the weekend')),
        ('Licensed Practical Nurse (LPN)',
         p.get('Reported LPN Staffing Hours per Resident per Day'),
         p.get('Case-Mix LPN Staffing Hours per Resident per Day'),
         None),
        ('Certified Nursing Assistant (CNA)',
         p.get('Reported Nurse Aide Staffing Hours per Resident per Day'),
         p.get('Case-Mix Nurse Aide Staffing Hours per Resident per Day'),
         None),
        ('Physical Therapist (PT)',
         p.get('Reported Physical Therapist Staffing Hours per Resident Per Day'),
         None, None),
        ('Total Nursing',
         p.get('Reported Total Nurse Staffing Hours per Resident per Day'),
         p.get('Case-Mix Total Nurse Staffing Hours per Resident per Day'),
         p.get('Total number of nurse staff hours per resident per day on the weekend')),
    ]
    rows_html = ''
    for label, reported, casemix, weekend in rows_data:
        rows_html += f'<tr><td style="font-weight:600">{label}</td><td>{fmt_hrs(reported)}</td><td>{fmt_hrs(casemix)}</td><td>{fmt_hrs(weekend)}</td></tr>'

    turnover = safe_float(p.get('Total nursing staff turnover'))
    rn_turnover = safe_float(p.get('Registered Nurse turnover'))
    admin_left = p.get('Number of administrators who have left the nursing home', '').strip()

    turnover_html = '<div class="turnover-grid">'
    if turnover is not None:
        tc = 'val-good' if turnover < 30 else ('val-warn' if turnover < 50 else 'val-bad')
        turnover_html += f'<div class="turnover-card"><div class="turnover-val {tc}">{fmt_pct_val(turnover)}</div><div class="turnover-lbl">Total Nursing Turnover</div></div>'
    if rn_turnover is not None:
        rc = 'val-good' if rn_turnover < 30 else ('val-warn' if rn_turnover < 50 else 'val-bad')
        turnover_html += f'<div class="turnover-card"><div class="turnover-val {rc}">{fmt_pct_val(rn_turnover)}</div><div class="turnover-lbl">RN Turnover</div></div>'
    if admin_left:
        turnover_html += f'<div class="turnover-card"><div class="turnover-val">{esc(admin_left)}</div><div class="turnover-lbl">Administrators Left</div></div>'
    turnover_html += '</div>'

    return f'''<table>
<thead><tr><th>Role</th><th>Reported Hrs/Res/Day</th><th>Case-Mix Adjusted</th><th>Weekend</th></tr></thead>
<tbody>{rows_html}</tbody>
</table>{turnover_html}'''

def build_wages_section(wages):
    if wages is None:
        return '<div class="empty-state">Wage estimates not available for this facility</div>'
    cards = []
    for role in ('NP', 'RN', 'LPN', 'CNA'):
        v = wages.get(role)
        cards.append(f'<div class="wage-card"><div class="val">{fmt_wage(v)}</div><div class="lbl">{role} Est. Hourly</div></div>')
    return f'<div class="wages-grid">{"".join(cards)}</div><p style="margin-top:12px;font-size:12px;color:#9ca3af">Estimates derived from CMS Cost Report data and staffing levels.</p>'

def build_facility_info(p):
    beds = p.get('Number of Certified Beds', '').strip()
    avg_res = p.get('Average Number of Residents per Day', '').strip()
    ownership = p.get('Ownership Type', '').strip()
    chain = p.get('Chain Name', '').strip()
    provider_type = p.get('Provider Type', '').strip()
    ccrc = p.get('Continuing Care Retirement Community', '').strip()
    sfs = p.get('Special Focus Status', '').strip()
    abuse = p.get('Abuse Icon', '').strip()
    in_hospital = p.get('Provider Resides in Hospital', '').strip()
    ownership_change = p.get('Provider Changed Ownership in Last 12 Months', '').strip()
    sprinklers = p.get('Automatic Sprinkler Systems in All Required Areas', '').strip()

    def info_item(label, value, badge_class=None):
        v = esc(value) if value else 'N/A'
        if badge_class and value:
            v = f'<span class="badge {badge_class}">{v}</span>'
        return f'<div class="info-item"><div class="lbl">{label}</div><div class="val">{v}</div></div>'

    abuse_badge = ''
    if abuse and abuse.upper() == 'Y':
        abuse_badge = 'badge-red'
    sfs_badge = ''
    if sfs:
        sfs_lower = sfs.lower()
        if 'sff' in sfs_lower or 'focus' in sfs_lower:
            sfs_badge = 'badge-red'
        elif sfs_lower not in ('', 'none', 'n/a'):
            sfs_badge = 'badge-amber'

    items = [
        info_item('Certified Beds', beds),
        info_item('Average Residents/Day', avg_res),
        info_item('Ownership Type', ownership),
        info_item('Chain Affiliation', chain or 'Independent'),
        info_item('Provider Type', provider_type),
        info_item('CCRC', 'Yes' if ccrc and ccrc.upper() == 'Y' else 'No'),
        info_item('Special Focus Status', sfs or 'None', sfs_badge),
        info_item('Abuse Icon', 'Yes' if abuse and abuse.upper() == 'Y' else 'No', abuse_badge if abuse and abuse.upper() == 'Y' else ''),
        info_item('In Hospital', 'Yes' if in_hospital and in_hospital.upper() == 'Y' else 'No'),
        info_item('Ownership Changed (12 mo)', 'Yes' if ownership_change and ownership_change.upper() == 'Y' else 'No'),
        info_item('Sprinkler Systems', 'Yes' if sprinklers and sprinklers.upper() == 'Y' else 'No'),
    ]
    return f'<div class="info-grid">{"".join(items)}</div>'

def build_safety_section(p):
    def safety_card(label, value, color_fn=None):
        v = safe_int(value)
        display = str(v) if v is not None else 'N/A'
        cls = ''
        if color_fn and v is not None:
            cls = color_fn(v)
        return f'<div class="safety-card"><div class="val {cls}">{display}</div><div class="lbl">{label}</div></div>'

    def def_color(v): return 'val-good' if v <= 2 else ('val-warn' if v <= 5 else 'val-bad')
    def low_good(v): return 'val-good' if v == 0 else ('val-warn' if v <= 2 else 'val-bad')

    c1_defs = p.get('Rating Cycle 1 Total Number of Health Deficiencies', '').strip()
    c2_defs = p.get('Rating Cycle 2/3 Total Number of Health Deficiencies', '').strip()
    complaints = p.get('Number of Substantiated Complaints', '').strip()
    incidents = p.get('Number of Facility Reported Incidents', '').strip()
    num_fines = p.get('Number of Fines', '').strip()
    fine_dollars = p.get('Total Amount of Fines in Dollars', '').strip()
    payment_denials = p.get('Number of Payment Denials', '').strip()
    total_penalties = p.get('Total Number of Penalties', '').strip()
    infection_cites = p.get('Number of Citations from Infection Control Inspections', '').strip()

    fine_display = ''
    nf = safe_int(num_fines)
    fd = safe_float(fine_dollars)
    if nf is not None and fd is not None:
        fine_display = f'{nf} (${fd:,.0f})'
    elif nf is not None:
        fine_display = str(nf)
    else:
        fine_display = 'N/A'

    cards = [
        safety_card('Cycle 1 Health Deficiencies', c1_defs, def_color),
        safety_card('Cycle 2/3 Health Deficiencies', c2_defs, def_color),
        safety_card('Substantiated Complaints', complaints, low_good),
        safety_card('Reported Incidents', incidents, low_good),
        f'<div class="safety-card"><div class="val {("val-good" if nf == 0 else "val-bad") if nf is not None else "val-na"}">{fine_display}</div><div class="lbl">Fines (Count & Total)</div></div>',
        safety_card('Payment Denials', payment_denials, low_good),
        safety_card('Total Penalties', total_penalties, low_good),
        safety_card('Infection Control Citations', infection_cites, low_good),
    ]
    return f'<div class="safety-grid">{"".join(cards)}</div>'

def build_quality_measures_section(measures):
    if not measures:
        return '<div class="empty-state">No quality measure data available</div>'

    long_stay = [m for m in measures if m.get('Resident type', '').strip().lower().startswith('long')]
    short_stay = [m for m in measures if m.get('Resident type', '').strip().lower().startswith('short')]

    def fmt_measure(val):
        """Format measure value: round to 1 decimal, add % suffix, strip .0"""
        raw = val.strip() if val else ''
        if not raw or raw == 'N/A':
            return 'N/A'
        try:
            num = float(raw)
            return f'{int(num)}%' if num == int(num) else f'{num:.1f}%'
        except ValueError:
            return esc(raw)

    def measures_table(items, label):
        if not items:
            return ''
        rows = ''
        for m in sorted(items, key=lambda x: x.get('Measure Code', '')):
            desc = esc(m.get('Measure Description', ''))
            q1 = fmt_measure(m.get('Q1 Measure Score', ''))
            q2 = fmt_measure(m.get('Q2 Measure Score', ''))
            q3 = fmt_measure(m.get('Q3 Measure Score', ''))
            q4 = fmt_measure(m.get('Q4 Measure Score', ''))
            avg = fmt_measure(m.get('Four Quarter Average Score', ''))
            used = m.get('Used in Quality Measure Five Star Rating', '').strip()
            star_marker = ' *' if used and used.upper() == 'Y' else ''
            rows += f'<tr><td style="max-width:300px">{desc}{star_marker}</td><td>{q1}</td><td>{q2}</td><td>{q3}</td><td>{q4}</td><td style="font-weight:600">{avg}</td></tr>'
        return f'''<div class="qm-type">{label}</div>
<div style="overflow-x:auto"><table>
<thead><tr><th>Measure</th><th>Q1</th><th>Q2</th><th>Q3</th><th>Q4</th><th>4-Qtr Avg</th></tr></thead>
<tbody>{rows}</tbody>
</table></div>'''

    html = measures_table(long_stay, 'Long-Stay Measures')
    html += measures_table(short_stay, 'Short-Stay Measures')
    if html:
        html += '<p style="padding:12px;font-size:11px;color:#9ca3af">* Used in CMS Five-Star Quality Rating. Values rounded to one decimal place.</p>'
    return html

def build_penalties_section(penalties):
    if not penalties:
        return '<div class="empty-state">No penalty records found</div>'
    sorted_p = sorted(penalties, key=lambda x: x.get('Penalty Date', ''), reverse=True)
    rows = ''
    for p in sorted_p:
        date = esc(p.get('Penalty Date', 'N/A').strip() or 'N/A')
        ptype = esc(p.get('Penalty Type', 'N/A').strip() or 'N/A')
        amount = p.get('Fine Amount', '').strip()
        denial_start = p.get('Payment Denial Start Date', '').strip()
        denial_days = p.get('Payment Denial Length in Days', '').strip()

        detail = ''
        if amount:
            detail = esc(amount)
        elif denial_start:
            detail = f'Denial: {esc(denial_start)}'
            if denial_days:
                detail += f' ({esc(denial_days)} days)'
        else:
            detail = 'N/A'

        rows += f'<tr><td>{date}</td><td>{ptype}</td><td>{detail}</td></tr>'
    return f'''<table>
<thead><tr><th>Date</th><th>Type</th><th>Amount / Details</th></tr></thead>
<tbody>{rows}</tbody>
</table>'''

def build_inspection_section(surveys):
    if not surveys:
        return '<div class="empty-state">No inspection history available</div>'
    sorted_s = sorted(surveys, key=lambda x: safe_int(x.get('Inspection Cycle', 99)) or 99)

    category_keys = [
        ('Freedom from Abuse/Neglect', 'Count of Freedom from Abuse and Neglect and Exploitation Deficiencies'),
        ('Quality of Life & Care', 'Count of Quality of Life and Care Deficiencies'),
        ('Resident Assessment', 'Count of Resident Assessment and Care Planning Deficiencies'),
        ('Nursing & Physician Services', 'Count of Nursing and Physician Services Deficiencies'),
        ('Resident Rights', 'Count of Resident Rights Deficiencies'),
        ('Nutrition & Dietary', 'Count of Nutrition and Dietary Deficiencies'),
        ('Pharmacy Services', 'Count of Pharmacy Service Deficiencies'),
        ('Environmental', 'Count of Environmental Deficiencies'),
        ('Administration', 'Count of Administration Deficiencies'),
        ('Infection Control', 'Count of Infection Control Deficiencies'),
        ('Emergency Preparedness', 'Count of Emergency Preparedness Deficiencies'),
    ]

    header_cells = '<th>Category</th>'
    for s in sorted_s:
        cycle = esc(s.get('Inspection Cycle', '?'))
        date = esc(s.get('Health Survey Date', '').strip() or 'N/A')
        header_cells += f'<th>Cycle {cycle}<br><span style="font-weight:400;font-size:11px">{date}</span></th>'

    rows = ''
    # Total health deficiencies row
    rows += '<tr style="background:#f0fdf4"><td style="font-weight:700">Total Health Deficiencies</td>'
    for s in sorted_s:
        v = s.get('Total Number of Health Deficiencies', '').strip()
        vi = safe_int(v)
        cls = ''
        if vi is not None:
            cls = 'val-good' if vi <= 2 else ('val-warn' if vi <= 5 else 'val-bad')
        rows += f'<td class="{cls}" style="font-weight:700">{esc(v) if v else "N/A"}</td>'
    rows += '</tr>'

    # Total fire safety row
    rows += '<tr style="background:#eff6ff"><td style="font-weight:700">Total Fire Safety Deficiencies</td>'
    for s in sorted_s:
        v = s.get('Total Number of Fire Safety Deficiencies', '').strip()
        rows += f'<td style="font-weight:700">{esc(v) if v else "N/A"}</td>'
    rows += '</tr>'

    # Category breakdown
    for label, key in category_keys:
        rows += f'<tr><td>{label}</td>'
        for s in sorted_s:
            v = s.get(key, '').strip()
            vi = safe_int(v)
            cls = ''
            if vi is not None and vi > 0:
                cls = 'val-warn' if vi <= 2 else 'val-bad'
            rows += f'<td class="{cls}">{esc(v) if v else "0"}</td>'
        rows += '</tr>'

    return f'''<div style="overflow-x:auto"><table>
<thead><tr>{header_cells}</tr></thead>
<tbody>{rows}</tbody>
</table></div>'''

def build_schema_json(ccn, p, wages):
    """Build JSON-LD structured data for a facility page."""
    import json

    name = p.get('Provider Name', 'Unknown Facility')
    address = p.get('Provider Address', '')
    city = p.get('City/Town', '')
    state = p.get('State', '')
    zipcode = p.get('ZIP Code', '').strip()
    phone = p.get('Telephone Number', '').strip()
    overall = safe_int(p.get('Overall Rating', ''))
    health_insp = safe_int(p.get('Health Inspection Rating', ''))
    quality_rating = safe_int(p.get('QM Rating', ''))
    staffing_rating = safe_int(p.get('Staffing Rating', ''))
    beds = p.get('Number of Certified Beds', '').strip()
    ownership = p.get('Ownership Type', '').strip()
    accepts_medicare = p.get('Medicare', '').strip().upper() == 'Y' if p.get('Medicare') else False
    accepts_medicaid = p.get('Medicaid', '').strip().upper() == 'Y' if p.get('Medicaid') else False

    # LocalBusiness / NursingHome schema
    facility_schema = {
        "@context": "https://schema.org",
        "@type": "NursingHome",
        "name": name,
        "url": f"https://snfcompare.com/facility/{ccn}.html",
        "@id": f"https://snfcompare.com/facility/{ccn}.html",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": address,
            "addressLocality": city,
            "addressRegion": state,
            "postalCode": zipcode,
            "addressCountry": "US"
        },
    }

    if phone:
        facility_schema["telephone"] = phone

    if beds:
        facility_schema["numberOfBeds"] = safe_int(beds)

    payment = []
    if accepts_medicare:
        payment.append("Medicare")
    if accepts_medicaid:
        payment.append("Medicaid")
    if payment:
        facility_schema["paymentAccepted"] = ", ".join(payment)

    if overall is not None:
        facility_schema["aggregateRating"] = {
            "@type": "AggregateRating",
            "ratingValue": str(overall),
            "bestRating": "5",
            "worstRating": "1",
            "ratingCount": "3",
            "reviewAspect": "CMS Overall Rating"
        }

    # MedicalWebPage schema
    webpage_schema = {
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "name": f"{name} — Facility Profile",
        "url": f"https://snfcompare.com/facility/{ccn}.html",
        "description": f"Detailed quality ratings, staffing data, inspection history, and more for {name} in {city}, {state} {zipcode}.",
        "about": {"@id": f"https://snfcompare.com/facility/{ccn}.html"},
        "isPartOf": {"@type": "WebSite", "name": "SNF Compare", "url": "https://snfcompare.com"},
        "lastReviewed": "2025-11-01"
    }

    # BreadcrumbList schema
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://snfcompare.com"},
            {"@type": "ListItem", "position": 2, "name": "Compare Tool", "item": "https://snfcompare.com/#tool"},
            {"@type": "ListItem", "position": 3, "name": name, "item": f"https://snfcompare.com/facility/{ccn}.html"}
        ]
    }

    # FAQPage schema
    overall_txt = f"{overall} out of 5 stars" if overall else "not rated"
    health_txt = f"{health_insp}/5" if health_insp else "N/A"
    quality_txt = f"{quality_rating}/5" if quality_rating else "N/A"
    staffing_txt = f"{staffing_rating}/5" if staffing_rating else "N/A"
    beds_txt = beds if beds else "N/A"

    faqs = [
        {
            "q": f"What is the overall rating for {name}?",
            "a": f"{name} has an overall CMS rating of {overall_txt}. This rating is based on health inspections ({health_txt}), quality measures ({quality_txt}), and staffing ({staffing_txt})."
        },
        {
            "q": f"Where is {name} located?",
            "a": f"{name} is located at {address}, {city}, {state} {zipcode}.{' The phone number is ' + phone + '.' if phone else ''}"
        },
        {
            "q": f"How many beds does {name} have?",
            "a": f"{name} has {beds_txt} certified beds.{' It is ' + ownership.lower() + '.' if ownership else ''}"
        },
    ]

    if wages:
        wage_parts = []
        for role in ('NP', 'RN', 'LPN', 'CNA'):
            w = wages.get(role)
            if w is not None:
                wage_parts.append(f"{role}: ${w:.2f}/hr")
        if wage_parts:
            faqs.append({
                "q": f"What are the estimated wages at {name}?",
                "a": f"Estimated hourly wages at {name} based on CMS cost report data: {', '.join(wage_parts)}. These are modeled estimates, not actual posted wages."
            })

    accept_parts = []
    if accepts_medicare:
        accept_parts.append("Medicare")
    if accepts_medicaid:
        accept_parts.append("Medicaid")
    if accept_parts:
        faqs.append({
            "q": f"Does {name} accept Medicare or Medicaid?",
            "a": f"Yes, {name} accepts {' and '.join(accept_parts)}."
        })

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": faq["q"],
                "acceptedAnswer": {"@type": "Answer", "text": faq["a"]}
            }
            for faq in faqs
        ]
    }

    schemas = [facility_schema, webpage_schema, breadcrumb_schema, faq_schema]
    scripts = []
    for s in schemas:
        j = json.dumps(s, ensure_ascii=False, separators=(',', ':'))
        scripts.append(f'<script type="application/ld+json">{j}</script>')
    return '\n'.join(scripts)


def generate_html(ccn, p, quality_measures, penalties, surveys, wages, image_path):
    name = esc(p.get('Provider Name', 'Unknown Facility'))
    address_parts = [p.get('Provider Address', ''), p.get('City/Town', ''), p.get('State', '')]
    zipcode = p.get('ZIP Code', '').strip()
    city_state_zip = f"{esc(p.get('City/Town', ''))}, {esc(p.get('State', ''))} {esc(zipcode)}"
    full_address = f"{esc(p.get('Provider Address', ''))}, {city_state_zip}"
    phone = esc(p.get('Telephone Number', '').strip())

    ratings_html = build_ratings_section(p)
    staffing_html = build_staffing_table(p)
    wages_html = build_wages_section(wages)
    info_html = build_facility_info(p)
    safety_html = build_safety_section(p)
    qm_html = build_quality_measures_section(quality_measures)
    penalties_html = build_penalties_section(penalties)
    inspections_html = build_inspection_section(surveys)

    phone_link = f'<a href="tel:{phone}" class="phone">{phone}</a>' if phone else ''

    # Get ratings for overview section
    overall = safe_int(p.get('Overall Rating', ''))
    health_insp = safe_int(p.get('Health Inspection Rating', ''))
    quality_rating = safe_int(p.get('QM Rating', ''))
    staffing_rating = safe_int(p.get('Staffing Rating', ''))

    schema_html = build_schema_json(ccn, p, wages)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>{name} — Facility Profile | SNF Compare</title>
<meta name="description" content="Detailed quality ratings, staffing data, inspection history, and more for {name} in {city_state_zip}.">
<meta name="robots" content="index, follow">
<meta property="og:title" content="{name} — Skilled Nursing Facility Profile">
<meta property="og:description" content="Quality ratings, staffing data, inspection history, and estimated wages for {name} in {city_state_zip}.">
<meta property="og:type" content="website">
<meta property="og:url" content="https://snfcompare.com/facility/{ccn}.html">
<link rel="canonical" href="https://snfcompare.com/facility/{ccn}.html">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
{schema_html}
<style>{PAGE_CSS}</style>
</head>
<body>

<div class="hero">
<div class="container">
<div class="hero-grid">
<div class="hero-info">
<div class="hero-badge"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>Verified CMS Data</div>
<h1>{name}</h1>
<p class="address"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>{full_address}</p>
{f'<p class="phone"><svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>{phone_link}</p>' if phone else ''}
</div>
<div class="hero-image">
<img src="{image_path}" alt="{name} facility exterior" loading="lazy">
</div>
</div>
</div>
</div>

<div class="section">

<div class="card">
<div class="card-header"><h2>Ratings Overview<span class="section-info"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path stroke-linecap="round" d="M12 16v-4m0-4h.01"/></svg><span class="tip">CMS Five-Star ratings based on health inspections, quality measures, and staffing levels. 5 stars = much above average, 1 star = much below average.</span></span></h2></div>
<div class="card-body">{ratings_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Staffing Details<span class="section-info"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path stroke-linecap="round" d="M12 16v-4m0-4h.01"/></svg><span class="tip">Hours of care provided per resident per day by staff type. Higher staffing generally correlates with better outcomes. CMS recommends 4.1+ total hours daily.</span></span></h2></div>
<div class="card-body">{staffing_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Estimated Wages<span class="section-info"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path stroke-linecap="round" d="M12 16v-4m0-4h.01"/></svg><span class="tip">Wages estimated from CMS cost report data. These are modeled averages, not actual job postings. Actual wages may vary based on experience and shift.</span></span></h2></div>
<div class="card-body">{wages_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Facility Information<span class="section-info"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path stroke-linecap="round" d="M12 16v-4m0-4h.01"/></svg><span class="tip">Basic facility details including ownership type, bed count, and insurance accepted. Ownership type can affect staffing and care quality.</span></span></h2></div>
<div class="card-body">{info_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Safety &amp; Compliance<span class="section-info"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path stroke-linecap="round" d="M12 16v-4m0-4h.01"/></svg><span class="tip">Deficiencies found during inspections, complaints filed, and fines issued. Lower numbers indicate better compliance. US average is about 8 deficiencies.</span></span></h2></div>
<div class="card-body">{safety_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Quality Measures (MDS)<span class="section-info"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path stroke-linecap="round" d="M12 16v-4m0-4h.01"/></svg><span class="tip">Clinical outcomes from Minimum Data Set assessments. Lower percentages are generally better (fewer falls, infections, etc). Compare to state and national averages.</span></span></h2></div>
<div class="card-body" style="padding:0">{qm_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Penalty History<span class="section-info"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path stroke-linecap="round" d="M12 16v-4m0-4h.01"/></svg><span class="tip">Fines and payment denials imposed by CMS for serious violations. Frequent or large penalties may indicate ongoing compliance issues.</span></span></h2></div>
<div class="card-body">{penalties_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Inspection History<span class="section-info"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path stroke-linecap="round" d="M12 16v-4m0-4h.01"/></svg><span class="tip">Recent state health inspections and complaint investigations. Click survey dates to see detailed findings. Focus on scope and severity of deficiencies.</span></span></h2></div>
<div class="card-body" style="padding:0">{inspections_html}</div>
</div>

</div>

<div class="disclaimer">
Data sourced from CMS Nursing Home Compare and SNF Cost Reports. Quality measures, inspection results, and staffing data are reported by CMS.
Wage estimates are modeled from cost report data and are not actual wages.
Last updated: November 2025.
</div>


<div id="emailGate" class="gate-overlay gate-hidden">
<div class="gate-modal">
<div class="gate-accent"></div>
<div class="gate-body">
<h2>Unlock Full Facility Data</h2>
<p class="gate-sub">Enter your email for instant access to detailed ratings, staffing data, inspection history, and quality measures.</p>
<form id="gateForm" class="gate-form" onsubmit="return false">
<input type="email" id="gateEmail" placeholder="you@email.com" required autocomplete="email">
<button type="submit" id="gateBtn">Access Data</button>
</form>
<div id="gateError" class="gate-error"></div>
<p class="gate-privacy">We respect your privacy. Unsubscribe anytime.</p>
</div>
<div class="gate-divider"></div>
<a href="../index.html#tool" class="gate-back">&larr; Go Back to Compare Tool</a>
</div>
</div>

<script>
(function(){{
  // TEMPORARILY DISABLED: email gate
  return;
  var SK='snf_email_gate';
  if(localStorage.getItem(SK)) return;
  var s=document.querySelector('.section');
  if(s) s.classList.add('content-gated');
  var o=document.getElementById('emailGate');
  if(o) o.classList.remove('gate-hidden');
  document.body.style.overflow='hidden';

  document.getElementById('gateForm').addEventListener('submit',function(e){{
    e.preventDefault();
    var email=document.getElementById('gateEmail').value.trim();
    if(!email) return;
    var btn=document.getElementById('gateBtn');
    var err=document.getElementById('gateError');
    btn.disabled=true; btn.textContent='Unlocking...'; err.style.display='none';

    var params=new URLSearchParams(window.location.search);
    var ref=params.get('ref');
    var listId=(ref==='pro')?'Y6tGhQ':'Ty5RgF';

    fetch('https://a.klaviyo.com/client/subscriptions/?company_id=TpXnBq',{{
      method:'POST',
      headers:{{'Content-Type':'application/json','revision':'2024-10-15'}},
      body:JSON.stringify({{
        data:{{
          type:'subscription',
          attributes:{{
            custom_source:'SNF Facility Page',
            profile:{{data:{{type:'profile',attributes:{{email:email}}}}}}
          }},
          relationships:{{
            list:{{data:{{type:'list',id:listId}}}}
          }}
        }}
      }})
    }}).then(function(r){{
      if(r.ok||r.status===202){{
        localStorage.setItem(SK,'1');
        unlock();
      }} else {{
        return r.text().then(function(t){{
          console.error('Klaviyo:',r.status,t);
          localStorage.setItem(SK,'1');
          unlock();
        }});
      }}
    }}).catch(function(ex){{
      console.error('Klaviyo catch:',ex);
      localStorage.setItem(SK,'1');
      unlock();
    }});
  }});

  function unlock(){{
    if(s) s.classList.remove('content-gated');
    if(o) o.classList.add('gate-hidden');
    document.body.style.overflow='';
  }}
}})();
</script>

</body>
</html>'''

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    print('Loading provider info...')
    providers = load_provider_info()
    print(f'  {len(providers)} facilities')

    print('Loading quality measures...')
    quality = load_quality_measures()
    print(f'  {len(quality)} facilities with measures')

    print('Loading penalties...')
    penalties = load_penalties()
    print(f'  {len(penalties)} facilities with penalties')

    print('Loading survey summaries...')
    surveys = load_survey_summary()
    print(f'  {len(surveys)} facilities with surveys')

    print('Loading cost report...')
    cost_reports = load_cost_report()
    print(f'  {len(cost_reports)} facilities in cost report')

    print('Computing wages...')
    all_wages = {}
    for ccn, p in providers.items():
        if ccn in cost_reports:
            all_wages[ccn] = compute_wages(p, cost_reports[ccn])
    computed = sum(1 for w in all_wages.values() if w is not None)
    print(f'  {computed} wages computed (pre-filter)')

    all_wages = apply_iqr_filter(all_wages)
    final = sum(1 for w in all_wages.values() if w is not None)
    print(f'  {final} wages after IQR filter')

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    total = len(providers)
    print(f'Generating {total} facility pages...')

    # Get valid facility images
    valid_images = get_valid_images()
    print(f'  {len(valid_images)} valid facility images found')

    for i, (ccn, p) in enumerate(providers.items()):
        image_path = get_image_path(ccn, valid_images)
        html = generate_html(
            ccn, p,
            quality.get(ccn, []),
            penalties.get(ccn, []),
            surveys.get(ccn, []),
            all_wages.get(ccn),
            image_path,
        )
        filepath = os.path.join(OUTPUT_DIR, f'{ccn}.html')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        if (i + 1) % 2000 == 0:
            print(f'  {i+1}/{total} pages generated...')

    print(f'Done! Generated {total} facility pages in {OUTPUT_DIR}/')

if __name__ == '__main__':
    main()
