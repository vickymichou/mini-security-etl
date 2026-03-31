# 🚀 Mini Security ETL Pipeline

A lightweight end-to-end ETL pipeline that simulates security log processing using Python, Pandas, PostgreSQL, Docker, and SQL.

---

## 📌 Project Overview

This project demonstrates a simple **data engineering workflow** for processing synthetic security logs.

The pipeline performs:

- 🧾 Data generation (synthetic logs)
- 🧹 Data cleaning & validation
- 🗄 Data loading into PostgreSQL
- 📊 SQL-based analysis

👉 Built as a portfolio project to showcase core data engineering concepts.

---

## 🛠 Tech Stack

- 🐍 Python  
- 🐼 Pandas  
- 🐘 PostgreSQL  
- 🐳 Docker / Docker Compose  
- 🔗 SQLAlchemy  
- ⚡ psycopg2  
- 🧮 SQL  

---

## 📁 Project Structure

```text
mini-security-etl/
│
├── app/
│   ├── generate_logs.py        # 📥 Extract
│   ├── transform_logs.py       # 🔄 Transform
│   └── load_to_postgres.py     # 📤 Load
│
├── sql/
│   └── queries.sql             # 📊 Analysis
│
├── docker-compose.yml          # 🐳 Database setup
├── requirements.txt
├── security_logs_raw.csv       # 📄 Raw data
└── security_logs_cleaned.csv   # ✅ Clean data
