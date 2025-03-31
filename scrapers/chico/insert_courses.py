import csv
import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# === CONFIG ===
API_URL = os.getenv("API_URL")
USERNAME = os.getenv("API_USERNAME")
PASSWORD = os.getenv("API_PASSWORD")

SCRAPED_DIR = "scraped_courses"

def insert_course(course_data):
    response = requests.post(API_URL, json=course_data, auth=(USERNAME, PASSWORD))
    subject = course_data.get("subject", "")
    catalog_number = course_data.get("catalog_number", "")
    if response.status_code == 201:
        print(f"✔ Inserted: {subject} {catalog_number}")
    elif response.status_code == 200:
        print(f"🟡 Updated: {subject} {catalog_number}")
    else:
        print(f"❌ Failed: {subject} {catalog_number} | Status: {response.status_code}")
        print(f"Response: {response.text}")

def read_courses_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def main():
    if not os.path.exists(SCRAPED_DIR):
        print(f"Folder not found: {SCRAPED_DIR}")
        return

    all_files = [f for f in os.listdir(SCRAPED_DIR) if f.endswith(".csv")]
    if not all_files:
        print("No CSV files found.")
        return

    for filename in all_files:
        filepath = os.path.join(SCRAPED_DIR, filename)
        print(f"\n📂 Processing: {filename}")
        courses = read_courses_from_csv(filepath)

        for course in courses:
            insert_course(course)

if __name__ == "__main__":
    main()

