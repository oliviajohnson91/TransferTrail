import subprocess

def run_scraper():
    print("🔍 Running scraper...")
    result = subprocess.run(["python3", "scrape_courses.py"])
    if result.returncode != 0:
        print("❌ Scraper failed!")
        return False
    print("✅ Scraper finished.\n")
    return True

def run_inserter():
    print("📤 Inserting scraped courses...")
    result = subprocess.run(["python3", "insert_courses.py"])
    if result.returncode != 0:
        print("❌ Insert failed!")
        return False
    print("✅ Insert completed.\n")
    return True

def main():
    if run_scraper():
        run_inserter()

if __name__ == "__main__":
    main()

