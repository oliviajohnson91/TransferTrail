import os
import csv
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Constants from environment
API_URL = os.getenv("API_URL")
AUTH = (os.getenv("API_USERNAME"), os.getenv("API_PASSWORD"))
INPUT_DIR = "scraped_courses"

# Loop through each CSV file in the scraped_courses directory
for filename in os.listdir(INPUT_DIR):
    if filename.endswith(".csv"):
        filepath = os.path.join(INPUT_DIR, filename)
        print(f"\n📂 Processing: {filename}")

        with open(filepath, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data = {
                    "subject": row.get("subject", "").strip(),
                    "catalog_number": row.get("catalog_number", "").strip(),
                    "title": row.get("title", "").strip(),
                    "min_units": row.get("min_units", "").strip(),
                    "max_units": row.get("max_units", "").strip(),
                    "institution_id": row.get("institution_id", "").strip(),
                    "attributes": row.get("attributes", "").strip(),
                    "general_education": row.get("general_education", "").strip(),
                    "scraped_on": row.get("scraped_on") or datetime.now().isoformat()
                }

                response = requests.post(API_URL, json=data, auth=AUTH)
                subject = data["subject"]
                catalog_number = data["catalog_number"]
                if response.status_code == 201:
                    print(f"✔ Inserted: {subject} {catalog_number}")
                elif response.status_code == 200:
                    print(f"🟡 Updated: {subject} {catalog_number}")
                else:
                    print(f"❌ Failed: {subject} {catalog_number} | Status: {response.status_code}")
                    print(f"Response: {response.text}")

