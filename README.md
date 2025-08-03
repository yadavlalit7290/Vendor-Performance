# Vendor Performance Analysis Project

## 📌 Overview
This project analyzes vendor performance and inventory management to help retail and wholesale businesses boost profitability. Using Python, SQL Server, and Power BI, the analysis uncovers insights into vendor contributions, pricing efficiencies, inventory turnover, and profit margins. The aim is to guide smarter decisions in procurement, promotions, and stock control.

---

## 🧠 Business Objective
Efficient inventory and sales management are key to reducing losses from poor pricing, vendor dependency, and slow turnover. This project helps answer:

- Which vendors drive the most revenue and profit?
- Are bulk purchases reducing unit costs effectively?
- Where are inventory inefficiencies or unsold stock occurring?
- Which high-margin brands are underperforming?
- How concentrated is vendor dependency?

---

## 🛠 Tools & Technologies
- **Python**: Data ingestion, preprocessing, EDA  
- **SQL Server**: Database creation, data storage, SQL querying  
- **SQLAlchemy & Pandas**: For ETL and data manipulation  
- **Power BI**: Interactive dashboards and visual analysis  

---

## 🔁 Project Workflow

### 1. Data Ingestion
- All raw CSVs are located in the `/Dataset` folder
- `ingesting.py`: Contains a reusable `Database` class to connect and run SQL on SQL Server
- `Data_ingesting.ipynb`: Loads and creates the `inventory` database and tables
- Cleaned for duplicates, nulls, and incorrect datatypes

### 2. Exploratory Data Analysis (EDA)
- `EDA_1.ipynb`: Combined multiple datasets into a unified DataFrame and uploaded to database
- `EDA_2.ipynb`: Focused on `vendor_sales_summary` table (10,692 rows × 18 columns)
  - Distribution plots, correlations, outlier detection
  - Inventory turnover, bulk pricing analysis, and vendor-level metrics

###  📊 Power BI Dashboard
- Created a Power BI dashboard connected to the SQL Server
- Visuals include vendor rankings, margin analysis, sales vs. purchase comparison, inventory holding
Here’s a snapshot of the interactive Power BI dashboard built from the `vendor_sales_summary` table:

![Dashboard Screenshot](https://github.com/user-attachments/assets/ebcf09ad-b931-463b-a7c2-89ddabde0665)



---

## 📈 Key Insights

- **Bulk Pricing Works**: Large orders reduce unit cost by up to 72%
- **Vendor Dependency**: Top 10 vendors = 66% of total purchases (supply chain risk)
- **Unsold Inventory**: $2.7M of unsold stock found; one vendor holding $722K alone
- **Hidden Potential**: High-margin brands with low sales are ideal for promotions
- **Margin Trends**: Smaller vendors often have higher margins than volume-based giants

---

## 💡 Recommendations

- Promote high-margin, low-sales brands
- Reevaluate inventory strategies for low turnover items
- Diversify suppliers to reduce reliance on top vendors
- Use Power BI dashboard to monitor real-time vendor performance

---

## ▶️ How to Run

1. Install Python + libraries: `pandas`, `sqlalchemy`, `numpy`
2. Setup and configure Microsoft SQL Server
3. Clone the repo and place all datasets in the `/Dataset` folder
4. Run `Data_ingesting.ipynb` to create and load the database
5. Explore analysis in EDA notebooks
6. Open the Power BI `.pbix` file to explore dashboard

---

## 🧠 What This Project Demonstrates

- ETL automation using Python and SQL
- Data cleaning, transformation, and modeling
- Strong analytical reasoning in business context
- End-to-end workflow from raw data to insights and dashboard
- Real-world problem solving using data

## 🔗 Connect with Me

📧 Email: [yadavlalit7290@gmail.com](mailto:yadavlalit7290@gmail.com)  
💼 LinkedIn: [linkedin.com/in/lalit-yad7290](https://www.linkedin.com/in/lalit-yad7290)

💻 Portfolio: [lalit_yadav/github.io](https://yadavlalit7290.github.io/lalit_yadav.github.io/)

