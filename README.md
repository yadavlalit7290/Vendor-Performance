# Vendor-Performance
# Project Overview

### Steps in making this project:

1. **ingesting.py**  
   Created a Python file named `ingesting.py` containing a class called `Database`.  
   This class helps connect to the database, execute SQL queries, upload data, and make changes to the database.

2. **Data_ingesting.ipynb**  
   Used the `Database` class from `ingesting.py` to:
   - Create a new database named `inventory`
   - Load all datasets from the `Dataset` folder into the `inventory` database

3. **EDA_1.ipynb**  
   Performed Exploratory Data Analysis (EDA) on the raw datasets.  
   - Merged all files into a single DataFrame
   - Cleaned and transformed the data into a meaningful format
   - Uploaded the cleaned data back into the `inventory` database

4. **EDA_2.ipynb**  
   Analyzed the cleaned `vendor_sales_summary` data:
   - Created visualizations and charts
   - Explored patterns and insights from individual columns

5. **Power BI Dashboard**  
   Built a dashboard in Power BI using the `vendor_sales_summary` table from the `inventory` database.

   Here is a preview of the final dashboard:
   
   ![Power BI Dashboard](https://github.com/user-attachments/assets/0c5666a1-3364-4179-8f3f-c68bbb2c1209)

## 📌 Project Objective

This project demonstrates the data ingestion and database creation to exploratory data analysis and dashboarding. The goal is to analyze vendor sales data and generate business insights using Python, SQL, and Power BI.



