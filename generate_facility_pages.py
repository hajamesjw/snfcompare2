#!/usr/bin/env python3
"""Generate individual facility profile pages from CMS nursing home data."""
import csv
import os
import sys
import html as html_mod
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
    return f'{f:.1f}%' if f is not None else 'N/A'

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
body{font-family:'Plus Jakarta Sans',-apple-system,BlinkMacSystemFont,sans-serif;background:#f8fafc;color:#1a1a1a;line-height:1.6}
a{color:#0d9488;text-decoration:none}
a:hover{text-decoration:underline}
.container{max-width:960px;margin:0 auto;padding:0 20px}
.header{background:white;border-bottom:1px solid #e5e7eb;padding:16px 0;position:sticky;top:0;z-index:250;backdrop-filter:blur(12px);background:rgba(255,255,255,0.92)}
.header-inner{display:flex;align-items:center;justify-content:space-between;max-width:960px;margin:0 auto;padding:0 20px}
.back-link{display:flex;align-items:center;gap:6px;color:#4b5563;font-size:14px;font-weight:500}
.back-link:hover{color:#111827;text-decoration:none}
.logo{display:flex;align-items:center;gap:6px;font-weight:800;font-size:16px;color:#1a1a1a;text-decoration:none}
.logo-badge{background:#10b981;color:white;padding:3px 8px;border-radius:6px;font-size:11px;font-weight:700}
.hero{background:white;border-bottom:1px solid #e5e7eb;padding:32px 0 28px}
.hero h1{font-size:28px;font-weight:800;color:#111827;margin-bottom:4px}
.hero .address{color:#6b7280;font-size:15px;margin-bottom:2px}
.hero .phone{color:#4b5563;font-size:14px;font-weight:500}
.section{margin:20px auto;max-width:960px;padding:0 20px}
.card{background:white;border-radius:16px;box-shadow:0 1px 3px rgba(0,0,0,0.06);border:1px solid #f0f0f0;overflow:hidden;margin-bottom:20px}
.card-header{padding:16px 20px;border-bottom:1px solid #f3f4f6;background:#f8fafc}
.card-header h2{font-size:16px;font-weight:700;color:#1f2937}
.card-body{padding:20px}
.ratings-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
@media(max-width:640px){.ratings-grid{grid-template-columns:repeat(2,1fr)}}
.rating-card{border-radius:14px;padding:20px 16px;text-align:center;color:white}
.rating-card .val{font-size:36px;font-weight:800}
.rating-card .stars{display:flex;justify-content:center;gap:4px;margin:8px 0 6px}
.rating-card .stars svg{width:24px;height:24px}
.rating-card .stars .filled{color:#fbbf24}
.rating-card .stars .empty{color:rgba(0,0,0,0.2)}
.rating-card .lbl{font-size:12px;font-weight:600;opacity:0.9;text-transform:uppercase;letter-spacing:0.5px}
.rating-card .na{font-size:28px;font-weight:700;opacity:0.7}
table{width:100%;border-collapse:collapse;font-size:14px}
th{text-align:left;padding:10px 12px;background:#f8fafc;color:#4b5563;font-weight:600;font-size:13px;border-bottom:2px solid #e5e7eb}
td{padding:10px 12px;border-bottom:1px solid #f3f4f6;color:#374151}
tr:last-child td{border-bottom:none}
tr:hover td{background:#fafbfc}
.val-good{color:#059669;font-weight:600}
.val-warn{color:#d97706;font-weight:600}
.val-bad{color:#dc2626;font-weight:600}
.val-na{color:#9ca3af}
.wages-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
@media(max-width:640px){.wages-grid{grid-template-columns:repeat(2,1fr)}}
.wage-card{background:linear-gradient(135deg,#ecfdf5,#d1fae5);border-radius:12px;padding:20px 16px;text-align:center}
.wage-card .val{font-size:24px;font-weight:800;color:#047857}
.wage-card .lbl{font-size:12px;color:#059669;font-weight:600;margin-top:4px;text-transform:uppercase;letter-spacing:0.5px}
.info-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
@media(max-width:640px){.info-grid{grid-template-columns:1fr}}
.info-item .lbl{font-size:12px;color:#6b7280;font-weight:500;margin-bottom:2px;text-transform:uppercase;letter-spacing:0.3px}
.info-item .val{font-size:15px;color:#111827;font-weight:600}
.badge{display:inline-block;padding:3px 10px;border-radius:9999px;font-size:11px;font-weight:600}
.badge-green{background:#ecfdf5;color:#065f46}
.badge-red{background:#fef2f2;color:#991b1b}
.badge-amber{background:#fffbeb;color:#92400e}
.badge-blue{background:#eff6ff;color:#1e40af}
.badge-gray{background:#f3f4f6;color:#374151}
.safety-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
@media(max-width:640px){.safety-grid{grid-template-columns:1fr}}
.safety-card{border-radius:12px;padding:16px;text-align:center;border:1px solid #f0f0f0;background:#fafbfc}
.safety-card .val{font-size:24px;font-weight:700}
.safety-card .lbl{font-size:11px;color:#6b7280;font-weight:500;margin-top:4px;text-transform:uppercase;letter-spacing:0.3px}
.qm-type{font-size:13px;font-weight:700;color:#4b5563;padding:12px;background:#f0fdf4;border-bottom:1px solid #e5e7eb;text-transform:uppercase;letter-spacing:0.5px}
.empty-state{padding:24px;text-align:center;color:#9ca3af;font-size:14px}
.footer{background:#1a1a1a;padding:40px 20px;margin-top:40px;color:#888;font-size:13px}
.footer-inner{max-width:960px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px}
.footer-logo{display:flex;align-items:center;gap:6px;color:white;font-weight:700;font-size:15px}
.footer-links{display:flex;gap:20px}
.footer-links a{color:#888;font-size:13px}
.footer-links a:hover{color:white}
.disclaimer{max-width:960px;margin:20px auto 0;padding:16px 20px;font-size:12px;color:#9ca3af;line-height:1.6;text-align:center}
.content-gated{filter:blur(8px);-webkit-filter:blur(8px);pointer-events:none;user-select:none;transition:filter .4s}
.gate-overlay{position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.55);z-index:200;display:flex;align-items:center;justify-content:center;padding:20px;backdrop-filter:blur(2px)}
.gate-overlay.gate-hidden{display:none}
.gate-modal{background:white;border-radius:20px;max-width:400px;width:100%;text-align:center;box-shadow:0 24px 80px rgba(0,0,0,.35);overflow:hidden}
.gate-modal .gate-accent{height:4px;background:linear-gradient(90deg,#10b981,#0d9488,#14b8a6)}
.gate-modal .gate-body{padding:36px 32px 28px}
.gate-modal h2{font-size:21px;font-weight:800;color:#111827;margin-bottom:6px}
.gate-modal .gate-sub{font-size:13px;color:#6b7280;margin-bottom:22px;line-height:1.5}
.gate-modal .gate-form{display:flex;flex-direction:column;gap:10px}
.gate-modal input[type=email]{width:100%;padding:14px 16px;border:2px solid #e5e7eb;border-radius:12px;font-size:15px;font-family:inherit;outline:none;transition:border-color .2s;box-sizing:border-box}
.gate-modal input[type=email]:focus{border-color:#10b981}
.gate-modal button[type=submit]{width:100%;padding:14px;border:none;border-radius:12px;background:linear-gradient(135deg,#10b981,#059669);color:white;font-size:15px;font-weight:700;font-family:inherit;cursor:pointer;transition:transform .15s,box-shadow .15s}
.gate-modal button[type=submit]:hover{transform:translateY(-1px);box-shadow:0 4px 14px rgba(16,185,129,.4)}
.gate-modal button[type=submit]:active{transform:scale(.98)}
.gate-modal button[type=submit]:disabled{opacity:.5;cursor:not-allowed;transform:none;box-shadow:none}
.gate-modal .gate-privacy{font-size:11px;color:#9ca3af;margin-top:16px}
.gate-modal .gate-error{color:#dc2626;font-size:13px;margin-top:8px;display:none}
.gate-modal .gate-divider{height:1px;background:#f0f0f0;margin:20px 0 0}
.gate-modal .gate-back{display:block;padding:14px;color:#6b7280;font-size:13px;font-weight:600;text-decoration:none;transition:color .2s}
.gate-modal .gate-back:hover{color:#111827;text-decoration:none}
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

    turnover_html = '<div style="margin-top:16px;display:flex;gap:24px;flex-wrap:wrap">'
    if turnover is not None:
        tc = 'val-good' if turnover < 30 else ('val-warn' if turnover < 50 else 'val-bad')
        turnover_html += f'<div><span class="info-item"><span class="lbl">Total Nursing Turnover</span><br><span class="val {tc}">{turnover:.1f}%</span></span></div>'
    if rn_turnover is not None:
        rc = 'val-good' if rn_turnover < 30 else ('val-warn' if rn_turnover < 50 else 'val-bad')
        turnover_html += f'<div><span class="info-item"><span class="lbl">RN Turnover</span><br><span class="val {rc}">{rn_turnover:.1f}%</span></span></div>'
    if admin_left:
        turnover_html += f'<div><span class="info-item"><span class="lbl">Administrators Left</span><br><span class="val">{esc(admin_left)}</span></span></div>'
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

    def measures_table(items, label):
        if not items:
            return ''
        rows = ''
        for m in sorted(items, key=lambda x: x.get('Measure Code', '')):
            desc = esc(m.get('Measure Description', ''))
            q1 = esc(m.get('Q1 Measure Score', 'N/A').strip() or 'N/A')
            q2 = esc(m.get('Q2 Measure Score', 'N/A').strip() or 'N/A')
            q3 = esc(m.get('Q3 Measure Score', 'N/A').strip() or 'N/A')
            q4 = esc(m.get('Q4 Measure Score', 'N/A').strip() or 'N/A')
            avg = esc(m.get('Four Quarter Average Score', 'N/A').strip() or 'N/A')
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
        html += '<p style="padding:12px;font-size:11px;color:#9ca3af">* Used in CMS Five-Star Quality Rating</p>'
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


def generate_html(ccn, p, quality_measures, penalties, surveys, wages):
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

<div class="header">
<div class="header-inner">
<a href="../snf-compare-landing.html#tool" class="back-link">
<svg width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
Back to Compare Tool
</a>
<a href="../snf-compare-landing.html" class="logo"><span class="logo-badge">SNF</span> compare</a>
</div>
</div>

<div class="hero">
<div class="container">
<h1>{name}</h1>
<p class="address">{full_address}</p>
{f'<p class="phone">{phone_link}</p>' if phone else ''}
</div>
</div>

<div class="section">

<div class="card">
<div class="card-header"><h2>Ratings Overview</h2></div>
<div class="card-body">{ratings_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Staffing Details</h2></div>
<div class="card-body">{staffing_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Estimated Wages</h2></div>
<div class="card-body">{wages_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Facility Information</h2></div>
<div class="card-body">{info_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Safety &amp; Compliance</h2></div>
<div class="card-body">{safety_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Quality Measures (MDS)</h2></div>
<div class="card-body" style="padding:0">{qm_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Penalty History</h2></div>
<div class="card-body">{penalties_html}</div>
</div>

<div class="card">
<div class="card-header"><h2>Inspection History</h2></div>
<div class="card-body" style="padding:0">{inspections_html}</div>
</div>

</div>

<div class="disclaimer">
Data sourced from CMS Nursing Home Compare and SNF Cost Reports. Quality measures, inspection results, and staffing data are reported by CMS.
Wage estimates are modeled from cost report data and are not actual wages.
Last updated: November 2025.
</div>

<div class="footer">
<div class="footer-inner">
<a href="../snf-compare-landing.html" class="footer-logo"><span class="logo-badge">SNF</span> compare</a>
<div class="footer-links">
<a href="../snf-compare-landing.html#tool">Compare Tool</a>
<a href="../snf-compare-landing.html">Home</a>
</div>
</div>
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
<a href="../snf-compare-landing.html#tool" class="gate-back">&larr; Go Back to Compare Tool</a>
</div>
</div>

<script>
(function(){{
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

    for i, (ccn, p) in enumerate(providers.items()):
        html = generate_html(
            ccn, p,
            quality.get(ccn, []),
            penalties.get(ccn, []),
            surveys.get(ccn, []),
            all_wages.get(ccn),
        )
        filepath = os.path.join(OUTPUT_DIR, f'{ccn}.html')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        if (i + 1) % 2000 == 0:
            print(f'  {i+1}/{total} pages generated...')

    print(f'Done! Generated {total} facility pages in {OUTPUT_DIR}/')

if __name__ == '__main__':
    main()
