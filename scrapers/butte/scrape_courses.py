import os
import csv
import time
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
BASE_URL = "https://butte.curriqunet.com/Catalog//iq/13651"
INSTITUTION_ID = 2  # Butte College ID
OUTPUT_DIR = "scraped_courses"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Set up headless Chrome
options = Options()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# Read subject IDs
with open("subject_ids.csv") as f:
    subject_ids = [line.strip().split(",")[0] for line in f if line.strip()]

def parse_units(text):
    import re
    # Match formats like "(3.00 units)" or "(1.00-3.00 units)"
    match_range = re.search(r"\((\d+(?:\.\d+)?)[–-](\d+(?:\.\d+)?) units\)", text)  # handles – or -
    match_single = re.search(r"\((\d+(?:\.\d+)?) units\)", text)

    if match_range:
        return float(match_range.group(1)), float(match_range.group(2))
    elif match_single:
        val = float(match_single.group(1))
        return val, val
    return None, None


# Loop through subjects
for subject_id in subject_ids:
    url = f"{BASE_URL}/{subject_id}"
    print(f"Fetching: {url}")
    driver.get(url)

    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "course-summary-wrapper"))
        )
    except:
        print(f"Timeout loading subject ID {subject_id}")
        continue

    soup = BeautifulSoup(driver.page_source, "html.parser")
    print("Page title:", soup.title.text.strip())

    courses = soup.find_all("div", class_="course-summary-wrapper")
    course_rows = []
    for course in courses:
        subject_el = course.find("b", class_="course-subject")
        number_el = course.find("b", class_="course-number")
        title_el = course.find("b", class_="course-title")

        if not subject_el or not number_el or not title_el:
            continue

        subject = subject_el.text.strip()
        catalog_number = number_el.text.strip()
        title_raw = title_el.text.strip()

        # Remove units from title if present
        if "(" in title_raw:
            title = title_raw.split("(")[0].strip()
        else:
            title = title_raw

        min_units, max_units = parse_units(title_raw)
        scraped_on = datetime.datetime.now().isoformat()

        course_rows.append([
            subject, catalog_number, title, min_units, max_units,
            INSTITUTION_ID, "", "", scraped_on
        ])

    # Save to CSV
    if course_rows:
        filename = f"{OUTPUT_DIR}/{subject_id}_{datetime.date.today()}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "subject", "catalog_number", "title", "min_units", "max_units",
                "institution_id", "attributes", "general_education", "scraped_on"
            ])
            writer.writerows(course_rows)

        print(f"Saved {len(course_rows)} courses to {filename}")
    else:
        print(f"No courses found for subject ID {subject_id}")

driver.quit()

