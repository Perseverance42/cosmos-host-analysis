import json
import time
import csv
import os
import requests
from datetime import datetime

DATA_DIR = './data'
CUTOFF_DATE = datetime(2000, 1, 1)

def parse_timestamp(ts):
    """Parse ISO 8601 timestamp with optional fractional seconds and Zulu time"""
    clean_ts = ts.split('.')[0].rstrip('Z')
    return datetime.strptime(clean_ts, "%Y-%m-%dT%H:%M:%S")

def _parse_addrbook(file_name):
    # Load data from JSON file
    with open(file_name, 'r') as f:
        data = json.load(f)

    # Filter valid entries and extract addr data
    valid_entries = {}

    for entry in data['addrs']:
        try:
            last_success = parse_timestamp(entry.get('last_success', '0001-01-01T00:00:00Z'))
            if last_success > CUTOFF_DATE and 'addr' in entry:
                valid_entries[entry['addr'].get('id')] = entry['addr'].get('ip')
        except Exception as e:
            print(f"Error processing entry: {e}")
            continue

    return valid_entries

# merge all addrbook files
valid_entries = {}
for file in os.listdir(DATA_DIR):
    if file.endswith('.json'):
        valid_entries.update(_parse_addrbook(os.path.join(DATA_DIR, file)))
print(f"Found {len(valid_entries)} valid entries")

# Query geolocation data
results = []
headers = {'User-Agent': 'Python IP Geolocation Script/1.0'}

for id, ip in valid_entries.items():
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}', headers=headers)
        response.raise_for_status()
        geo = response.json()
        if geo.get('status') == 'success':
            results.append({
                'id': id,
                'ip': ip,
                'country': geo.get('country'),
                'countryCode': geo.get('countryCode'),
                'region': geo.get('region'),
                'regionName': geo.get('regionName'),
                'city': geo.get('city'),
                'zip': geo.get('zip'),
                'lat': geo.get('lat'),
                'lon': geo.get('lon'),
                'timezone': geo.get('timezone'),
                'isp': geo.get('isp'),
                'org': geo.get('org'),
                'as': geo.get('as'),
                'asname': geo.get('asname')
            })
            print(f"Successfully processed {ip}")
        else:
            print(f"Error for {ip}: {geo.get('message')}")
    except requests.exceptions.RequestException as e:
        print(f"API Error for {ip}: {e}")
    except json.JSONDecodeError:
        print(f"Invalid JSON response for {ip}")
    time.sleep(0.3) # avoid spamming the API

# save the results to a csv file
with open(os.path.join(DATA_DIR,'host-analysis_full.csv'), 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'ip', 'country', 'countryCode', 'region', 'regionName', 'city', 'zip', 'lat', 'lon', 'timezone', 'isp', 'org', 'as', 'asname'])
    for result in results:
        writer.writerow([result['id'], result['ip'], result['country'], result['countryCode'], result['region'], result['regionName'], result['city'], result['zip'], result['lat'], result['lon'], result['timezone'], result['isp'], result['org'], result['as'], result['asname']])
