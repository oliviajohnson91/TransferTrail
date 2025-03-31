import subprocess

print("\n Step 1: Getting catalog HTML...")
subprocess.run(["python3", "get_catalog_html.py"])

print("\n Step 2: Extracting subject IDs...")
subprocess.run(["python3", "get_ids.py"])

print("\n Step 3: Scraping course data...")
subprocess.run(["python3", "scrape_courses.py"])

print("\n Step 4: Inserting courses into the database...")
subprocess.run(["python3", "insert_courses.py"])

print("\n✅ All done!")

