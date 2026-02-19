# 📦 Warehouse Inventory Data Warehouse Project

## 📌 Overview

This project builds a **Data Warehouse for Warehouse Inventory Management** using SQL and Python.

It covers:

- SQL Queries  
- Joins & CTEs  
- Data Modeling (Star Schema)  
- ETL using Python  
- Business Analysis  

The project analyzes warehouse inventory performance, stock levels, demand forecasting, and operational KPIs.

---

## 🎯 Objectives

- Clean raw warehouse inventory data
- Load data into MySQL database
- Design dimension and fact tables
- Perform analytical SQL queries
- Generate business insights

---

## 🗂️ Project Structure
```
warehouse-inventory-project/
│
├── data/
│   ├── raw/
│   │     └── raw_inventory_data.csv
│   └── processed/
│         └── clean_inventory_data.csv
│
├── etl/
│   └── etl_script.py
│
├── sql/
│   ├── create_tables.sql
│   ├── insert_data.sql
│   └── analysis_queries.sql
│
├── requirements.txt
└── README.md
```
---

## 🛠️ Technologies Used

- Python (Pandas, SQLAlchemy, PyMySQL)
- MySQL
- Git & GitHub

---

## 🔄 ETL Process

### Extract
Load raw CSV file using Pandas.

### Transform
- Convert date columns  
- Remove duplicates  
- Remove missing values  

### Load
- Connect to MySQL
- Load cleaned data into `inventory_raw` table

---

## 🏗️ Data Modeling

Star Schema Design:

Dimension Tables:
- dim_category
- dim_location
- dim_date

Fact Table:
- fact_inventory

This structure supports efficient analytical queries.

---

## 📊 Analysis Performed

- Total stock by category  
- Stockout analysis  
- Order fulfillment rate analysis  
- Inventory turnover analysis  
- Zone performance comparison  
- Forecasted vs actual demand analysis  

---

## 🚀 How to Run the Project

1. Clone the repository  
2. Install dependencies:

pip install -r requirements.txt

3. Create MySQL database:

CREATE DATABASE ecommerce_dw;

4. Run ETL script:

python etl/etl_script.py

5. Execute SQL files in MySQL Workbench.

---

## 📌 Key Learnings

- Data cleaning using Pandas  
- Connecting Python with MySQL  
- Star schema data modeling  
- Writing joins and CTE queries  
- Handling duplicate primary key issues  
- Managing SQL safe update mode  

---

## 👩‍💻 Author

Shraddha Patil  
Data Science 
