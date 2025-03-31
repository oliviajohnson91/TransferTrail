from bs4 import BeautifulSoup
import csv

# Load the HTML
with open("butte_course_catalog.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file.read(), "html.parser")

# Select the subject list in the courses section
subject_list = soup.select(".index-list li.nav-item.index-item")

# Parse subjects and IDs
subjects = []
for li in subject_list:
    subject_id = li.get("data-id")
    name_tag = li.find("a")
    if subject_id and name_tag:
        subject_name = name_tag.get_text(strip=True)
        if "-" in subject_name:
            subjects.append((subject_id, subject_name))

# Save to CSV
with open("subject_ids.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name"])
    writer.writerows(subjects)

print(f"Extracted {len(subjects)} subjects and saved to subject_ids.csv.")

