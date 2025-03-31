import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import re
import os

BASE_URL = "https://catalog.csuchico.edu/courses/"
INSTITUTION_ID = 1
HEADERS = [
    "subject",
    "catalog_number",
    "title",
    "min_units",
    "max_units",
    "institution_id",
    "attributes",
    "general_education",
    "scraped_on"
]

SUBJECTS = [
    "ACCT", "AMAR", "AFAM", "AFRI", "ABUS", "AGED", "AGET", "AGRI", "AIST", "ANSC", "ANTH", "ARAB", "ARTS", "ARTE", "ARTH", "AAST", "ASST", "BIOL", "BADM", "BCOM", "BSIS", "BLAW", "CHEM", "CHLX", "CHLD", "CIVL", "CMSD", "CMST",
    "CAGD", "CINS", "CSCI", "CSED", "CIMT", "CMGT", "CRIM", "DANC", "ESPE", "ERTH", "ECON",
    "EDUC", "EDAD", "BLMC", "EDCI", "EDMA", "RDGL", "EDSL", "SPED", "EDTE", "EECE", "ENGL",
    "EFLN", "ENVL", "FINA", "FREN", "GEOG", "GERM", "HIST", "HNRS", "HUMN", "IDST", "INTD",
    "ARTI", "INTB", "INED", "INTR", "INST", "ITAL", "JAPN", "JOUR", "KINE", "LANC", "LAST",
    "LDRS", "LEGL", "LBST", "LIBR", "MGMT", "MINS", "MKTG", "MATH", "MTHE", "MECH", "MECA",
    "MADT", "MEST", "MJIS", "MCGS", "MUSC", "NURS", "NFSC", "OSCM", "PHIL", "PHYS", "PSSC",
    "POLS", "PSYC", "PADM", "PHHA", "QTST", "REAL", "RHPM", "RELS", "SCED", "SOSC", "SWRK",
    "SOCI", "SPAN", "TECH", "THEA", "UNIV", "WMST"
]


def parse_units(units_text):
    match = re.match(r"(\d+)(?:-(\d+))? Units", units_text)
    if match:
        min_units = int(match.group(1))
        max_units = int(match.group(2)) if match.group(2) else min_units
        return min_units, max_units
    return None, None

def extract_course_info(course):
    code = course.select_one(".detail-code").text.strip()
    subject, catalog_number = code.split()

    title = course.select_one(".detail-title").text.strip()

    units_tag = course.select_one(".detail-hours_html")
    units_text = units_tag.text.strip() if units_tag else ""
    min_units, max_units = parse_units(units_text)

    attr_tag = course.select_one(".detail-crse_attr")
    attributes = attr_tag.text.replace("Course Attributes: ", "").strip(", ").strip() if attr_tag else ""

    ge_tag = course.select_one(".detail-gen_ed")
    ge_value = ge_tag.text.replace("General Education: ", "").strip(", ").strip() if ge_tag else ""

    return [
        subject,
        catalog_number,
        title,
        min_units,
        max_units,
        INSTITUTION_ID,
        attributes,
        ge_value,
        datetime.now().isoformat()
    ]

def scrape_subject(subject):
    url = f"{BASE_URL}{subject.lower()}/"
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch {subject}: status code {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    courses = soup.select(".courseblock")
    return [extract_course_info(course) for course in courses]

def main():
    timestamp_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    os.makedirs("scraped_courses", exist_ok=True)

    for subject in SUBJECTS:
        print(f"Scraping {subject}...")
        courses = scrape_subject(subject)
        filename = f"scraped_courses/{subject}_{timestamp_str}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(HEADERS)
            writer.writerows(courses)

if __name__ == "__main__":
    main()

