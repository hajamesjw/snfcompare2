#!/usr/bin/env python3
"""
Fetch Google Street View images for all SNF facilities.

Usage:
    python fetch_streetview_images.py YOUR_API_KEY

Requirements:
    pip install requests

The script will:
- Read facility addresses from the CSV
- Fetch Street View images (640x480)
- Save to images/ folder with CCN as filename
- Skip already downloaded images (resume-friendly)
- Track progress and errors
"""

import csv
import os
import sys
import time
import requests
from urllib.parse import quote

# Configuration
CSV_PATH = 'data/NH_ProviderInfo_Nov2025.csv'
OUTPUT_DIR = 'images/facilities'
IMAGE_SIZE = '640x480'  # Max size for free tier
DELAY_BETWEEN_REQUESTS = 0.1  # seconds, to be nice to the API

def fetch_streetview(api_key, address, output_path):
    """Fetch a Street View image for the given address."""
    url = f"https://maps.googleapis.com/maps/api/streetview"
    params = {
        'size': IMAGE_SIZE,
        'location': address,
        'key': api_key,
        'source': 'outdoor'  # Prefer outdoor imagery
    }

    try:
        response = requests.get(url, params=params, timeout=30)

        # Check if we got an actual image (not an error image)
        # Street View returns a gray "no image" placeholder if unavailable
        # We can check content-type and size
        if response.status_code == 200:
            content_type = response.headers.get('content-type', '')
            if 'image' in content_type and len(response.content) > 5000:
                # Likely a real image (error images are typically smaller)
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                return True, "OK"
            else:
                return False, "No imagery available"
        else:
            return False, f"HTTP {response.status_code}"
    except Exception as e:
        return False, str(e)

def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_streetview_images.py YOUR_GOOGLE_API_KEY")
        print("\nTo get an API key:")
        print("1. Go to https://console.cloud.google.com/")
        print("2. Create a project (or select existing)")
        print("3. Enable 'Street View Static API'")
        print("4. Go to Credentials > Create Credentials > API Key")
        print("5. Enable billing (required, but $200/month free credit)")
        sys.exit(1)

    api_key = sys.argv[1]

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Read facilities
    print("Loading facilities...")
    facilities = []
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ccn = row.get('CMS Certification Number (CCN)', '').strip()
            address = row.get('Provider Address', '').strip()
            city = row.get('City/Town', '').strip()
            state = row.get('State', '').strip()
            zip_code = row.get('ZIP Code', '').strip()

            if ccn and address:
                full_address = f"{address}, {city}, {state} {zip_code}"
                facilities.append({
                    'ccn': ccn,
                    'address': full_address
                })

    print(f"Found {len(facilities)} facilities")

    # Check which are already downloaded
    existing = set()
    for f in os.listdir(OUTPUT_DIR):
        if f.endswith('.jpg'):
            existing.add(f.replace('.jpg', ''))

    to_download = [f for f in facilities if f['ccn'] not in existing]
    print(f"Already downloaded: {len(existing)}")
    print(f"Remaining to download: {len(to_download)}")

    if not to_download:
        print("All images already downloaded!")
        return

    # Fetch images
    success_count = 0
    fail_count = 0
    errors = []

    print(f"\nFetching images (this will take ~{len(to_download) * DELAY_BETWEEN_REQUESTS / 60:.1f} minutes)...\n")

    for i, facility in enumerate(to_download):
        ccn = facility['ccn']
        address = facility['address']
        output_path = os.path.join(OUTPUT_DIR, f"{ccn}.jpg")

        success, message = fetch_streetview(api_key, address, output_path)

        if success:
            success_count += 1
        else:
            fail_count += 1
            errors.append((ccn, message))

        # Progress update every 100
        if (i + 1) % 100 == 0:
            print(f"  Progress: {i + 1}/{len(to_download)} ({success_count} ok, {fail_count} failed)")

        time.sleep(DELAY_BETWEEN_REQUESTS)

    # Summary
    print(f"\n{'='*50}")
    print(f"COMPLETE!")
    print(f"  Success: {success_count}")
    print(f"  Failed: {fail_count}")
    print(f"  Images saved to: {OUTPUT_DIR}/")

    if errors and len(errors) <= 20:
        print(f"\nFailed facilities:")
        for ccn, msg in errors[:20]:
            print(f"  {ccn}: {msg}")
    elif errors:
        print(f"\n(First 20 of {len(errors)} failures)")
        for ccn, msg in errors[:20]:
            print(f"  {ccn}: {msg}")

        # Save full error log
        with open('streetview_errors.txt', 'w') as f:
            for ccn, msg in errors:
                f.write(f"{ccn}: {msg}\n")
        print(f"\nFull error log saved to streetview_errors.txt")

if __name__ == '__main__':
    main()
