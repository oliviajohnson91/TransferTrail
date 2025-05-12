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
  Interactive, semester-by-semester suggested course sequence.  
  Drag-and-drop support (in progress) for reordering courses between semesters.

- **✅ Completion Tracking**  
  Check off courses you've already completed and visually track progress.

- **🔄 Articulation Lookup**  
  See which community college courses articulate to CSU requirements.

- **🎓 GE Area Progress**  
  Automatically shows which GE areas are completed and which are still needed.

---

## 🛠 Tech Stack

- **Oracle APEX** (App Builder, Page Designer, Dynamic Actions)  
- **SQL / PL/SQL**  
- **JavaScript** (SortableJS for drag-and-drop interactivity)  
- **Python** (for scraping course catalog data — planned)

---

## 📂 Repository Structure
TransferTrail/
├── apexExport/f100        # APEX app export (SQL + readable YAML files)
├── scrapers               # Python scripts for scraping Chico and Butte catalogs
├── .gitignore             # (likely ignores .DS_Store etc.)
└── README.md              # Project overview and documentation

---

## 📥 How to Import the APEX App

1. Log into Oracle APEX.
2. Navigate to **App Builder** > **Import**.
3. Upload `f100.sql` or the ZIP from `apexExport/`.
4. Follow the wizard to install the app and supporting objects.

---

## 🚧 Planned Features

- [ ] Save user-created course plans with reorderable terms  
- [ ] Integrate transfer GPA calculator  
- [ ] Mobile-friendly UI with REST API backend  
- [ ] Admin interface to manage programs and articulation mappings

---

## 👩‍💻 Author

**Olivia Johnson**  
[LinkedIn](https://linkedin.com/in/oliviajohnson76)  
📧 olivia@chicojohnsons.com

---
