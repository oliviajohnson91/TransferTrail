# Transfer Trail

**Transfer Trail** is a web-based academic advising tool built with Oracle APEX to help transfer students efficiently plan and track their academic journey. It simplifies the course planning process by centralizing degree requirements, articulation information, and term-by-term course pathways in a single, interactive platform.

---

## 🎯 Purpose

Transfer students often struggle to find consistent, centralized information about which classes to take and when — especially when navigating articulation between community colleges and CSUs. Transfer Trail solves this by bringing:

- Degree requirements  
- Course planning  
- Articulation lookups  
- GE progress tracking  

...all into one app.

---

## ✨ Features

- **📋 Degree Requirement Viewer**  
  View required and elective courses by category (e.g., Lower Division, Upper Division, GE).

- **📆 Recommended Pathway**  
  Semester-by-semester suggested course sequence.

- **✅ Completion Tracking**  
  Check off courses you've already completed and visually track progress.

- **🔄 Articulation Lookup**  
  See which community college courses articulate to CSU requirements.

- **🎓 GE Area Progress**  
  Shows which GE areas are completed and which are still needed.

---

## 🛠 Tech Stack

- **Oracle APEX** (App Builder, Page Designer, Dynamic Actions)  
- **SQL / PL/SQL**  
- **Python**

---

## 📂 Repository Structure
TransferTrail/
- `apexExport/f100`: APEX app export (SQL + readable YAML files)
- `scrapers`: Python scripts for scraping Chico and Butte catalogs
- `README.md`: Project overview and documentation

---

## 📥 How to Import the APEX App

1. Log into Oracle APEX.
2. Navigate to **App Builder** > **Import**.
3. Upload `f100.sql` or the ZIP from `apexExport/`.
4. Follow the wizard to install the app and supporting objects.

---

## 👩‍💻 Author

**Olivia Johnson**  
[LinkedIn](https://linkedin.com/in/oliviajohnson76)  

---
