# 🕸️ Web Scraping Automation Project — Hacksprint v3.0

## 🏫 Hackathon Submission
**Event:** Hacksprint v2.0 & v3.0  
**Organized by:** Marathwada Mitra Mandal's College of Engineering, Pune, India  
**Team ID:** HS302_PS11

---

## 📌 Project Overview
This project aims to automate the extraction of company-related data from publicly accessible sources such as **Zauba Corp**, which provides company registry information in India. It is built to support:

- Gathering official company URLs
- Extracting director and corporate structure information
- Exporting scraped data to Excel sheets for analysis and reporting

The solution was implemented using **Python and BeautifulSoup** and includes Jupyter notebooks and a `.py` automation script.

---

## 🔧 Tech Stack
- **Language:** Python 3
- **Libraries:** BeautifulSoup, pandas, requests
- **Tools:** Jupyter Notebook, Excel (for output), Google Colab (optional)

---


## 🧭 Flowchart
```
+---------------------------+
|     User Launches GUI     |
+------------+--------------+
             |
             v
+------------+------------------------------------+
| Select Quarter from CIBIL (Selenium + Tkinter) |
+------------+------------------------------------+
             |
             v
+------------+---------------------------+
| Download Excel Report from CIBIL Site  |
+------------+---------------------------+
             |
             v
+------------+-----------------------------+
| Read Downloaded Excel using xlrd         |
+------------+-----------------------------+
             |
             v
+------------+-----------------------------+
| For Each Company Name:                   |
|  -> Search CIN on ZaubaCorp              |
|  -> Get Company URL                      |
|  -> Scrape Director Names                |
+------------+-----------------------------+
             |
             v
+------------+-----------------------------+
| Write All Results to New Excel (openpyxl) |
+------------+-----------------------------+
             |
             v
+------------+-------------+
|   Show Completion Popup   |
+--------------------------+
```
---

## 📂 Key Components

### 🧠 Core Script Logic
The main application automates:
- Visiting the [CIBIL Suit Filed Data Portal](https://suit.cibil.com/)
- Selecting a reporting period using Selenium and downloading a company report
- Reading the downloaded Excel file (using `xlrd`)
- Searching ZaubaCorp for each company's CIN (Corporate Identification Number), director names, and company profile URL via `requests` and `BeautifulSoup`
- Writing structured results into a new Excel file using `openpyxl`

It features a GUI built with **Tkinter**, allowing users to:
- Choose a reporting quarter (dynamically scraped from CIBIL)
- Click a button to initiate download, scraping, and export
- Receive confirmation popups when tasks are complete
- `ZaubaToExcel.py`: Script to scrape company data and export to Excel
- `Final Project.ipynb`: Main notebook orchestrating the scraping flow
- `companyURL.ipynb` + variants: Extract URLs and information via HTML parsing
- `URL of Companies.xls`: Input Excel file with initial company names or URLs
- `cgSummaryReport_1601003730608.xls`: Sample scraped data output
- `HS302_PS11_Presentation.pptx`: Project presentation slides
- `Demo video_Team CKR.mp4`: Short demo of the working solution

---

## 📊 Features
- Automated web scraping pipeline
- Input-driven company search from Excel
- Extracts structured data (directors, industry codes, registration)
- Handles HTML content parsing and exception control
- Outputs data in a clean, tabular format (XLSX)

---

## 🚀 How to Run
1. Install dependencies: `pip install beautifulsoup4 pandas openpyxl`
2. Place the company names/URLs in `URL of Companies.xls`
3. Run `ZaubaToExcel.py` or execute notebooks in order
4. Output will be saved as `.xls` or `.xlsx` reports

---

## 🎯 Impact & Applications
- Ideal for research on Indian corporate structures
- Time-saving for analysts collecting firmographic data
- Can be adapted for use by incubators, law firms, or finance students

---

## 📽️ Demo & Presentation
- **Demo video:** `Demo video_Team CKR.mp4`
- **Slides:** `HS302_PS11_Presentation.pptx`

---

## ✨ Acknowledgment
We thank **MMCOE Pune** and the organizers of **Hacksprint v3.0** for the opportunity to present our automation project.

---


## 👥 Team
Team CSR 
- Chandramouleesvar V
- Swetha M E
- Raja V