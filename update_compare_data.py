#!/usr/bin/env python3
"""
Update snf-facility-compare.html with address and phone data from CSV.
"""

import csv
import json
import re

# Read the provider info CSV
providers = {}
with open('data/NH_ProviderInfo_Nov2025.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ccn = row.get('CMS Certification Number (CCN)', '').strip()
        if ccn:
            providers[ccn] = {
                'address': row.get('Provider Address', '').strip(),
                'phone': row.get('Telephone Number', '').strip()
            }

# Read the current HTML file
with open('deploy/snf-facility-compare.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the _raw data
match = re.search(r'const _raw = (\[\[.*?\]\]);', html, re.DOTALL)
if not match:
    print("Could not find _raw data in HTML")
    exit(1)

# Parse the current data
raw_data = json.loads(match.group(1))
print(f"Found {len(raw_data)} facilities")

# Update each facility with address and phone
# Current indices: [id,ccn,name,city,state,zip,overall,healthInsp,quality,staffing,
#                   avgRes,turnover,rnHrs,lpnHrs,cnaHrs,totalHrs,def,complaints,fines,
#                   abuseIcon,medicaid,medicare,beds,wageNP,wageRN,wageLPN,wageCNA,npHrs]
# New: add address at 28, phone at 29

updated_data = []
for row in raw_data:
    ccn = row[1]
    provider = providers.get(ccn, {})
    address = provider.get('address', '')
    phone = provider.get('phone', '')
    # Add address and phone to end of row
    new_row = row + [address, phone]
    updated_data.append(new_row)

# Generate new _raw string
new_raw = 'const _raw = ' + json.dumps(updated_data, separators=(',', ':')) + ';'

# Update the comment to reflect new structure
old_comment = """// [id,ccn,name,city,state,zip,overall,healthInsp,quality,staffing,
    //  avgRes,turnover,rnHrs,lpnHrs,cnaHrs,totalHrs,def,complaints,fines,
    //  abuseIcon,medicaid,medicare,beds,wageNP,wageRN,wageLPN,wageCNA,npHrs]"""

new_comment = """// [id,ccn,name,city,state,zip,overall,healthInsp,quality,staffing,
    //  avgRes,turnover,rnHrs,lpnHrs,cnaHrs,totalHrs,def,complaints,fines,
    //  abuseIcon,medicaid,medicare,beds,wageNP,wageRN,wageLPN,wageCNA,npHrs,address,phone]"""

# Replace in HTML
html = html.replace(old_comment, new_comment)
html = re.sub(r'const _raw = \[\[.*?\]\];', new_raw, html, flags=re.DOTALL)

# Write back
with open('deploy/snf-facility-compare.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Updated {len(updated_data)} facilities with address and phone data")
print(f"Sample: {updated_data[0][2]} - {updated_data[0][28]}, {updated_data[0][29]}")
