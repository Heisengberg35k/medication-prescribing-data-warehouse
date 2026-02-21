\# Medication Prescribing Data Warehouse with Analytics Dashboard



\## Project Overview



This project implements a dimensional Star Schema Data Warehouse using PostgreSQL and a Python-based Extract, Transform, Load (ETL) pipeline to process anonymised NHS prescribing data.



The system enables structured storage, optimised analytical querying, and interactive visualisation of prescribing trends through a Streamlit dashboard.



This project demonstrates practical data engineering, dimensional modelling, database optimisation, and analytics delivery aligned with final-year Computing outcomes.



---



\##  System Architecture



Data Source → Python ETL → PostgreSQL Data Warehouse → SQL Analytics → Streamlit Dashboard



\- Data Source: NHS Open Prescribing Dataset

\- ETL Layer: Python (pandas, psycopg2)

\- Database: PostgreSQL

\- Dashboard: Streamlit



---



\##  Dimensional Model (Star Schema)



\### Fact Table

\- `fact\_prescribing`

&nbsp; - quantity

&nbsp; - items

&nbsp; - total\_cost

&nbsp; - foreign keys to dimensions



\### Dimension Tables

\- `dim\_medication`

\- `dim\_practice`

\- `dim\_date`



This structure enables fast analytical queries and follows industry-standard data warehouse design principles.



---



\##  ETL Pipeline Features



\- Extraction from NHS open datasets

\- Data cleaning:

&nbsp; - Null handling

&nbsp; - Duplicate removal

&nbsp; - Data type standardisation

\- Validation rules:

&nbsp; - Range checks

&nbsp; - Foreign key integrity

\- Transformation into dimensional format

\- Controlled loading into PostgreSQL



---



\##  Performance Optimisation



\- Indexed primary and foreign keys

\- Query performance analysis

\- Structured relational constraints



---



\##  Example Analytical Queries



\- Top 10 most prescribed medications

\- Monthly prescribing cost trends

\- Regional prescribing comparison

\- Practice-level expenditure analysis



---



\##  Dashboard Features



Interactive Streamlit dashboard including:



\- Year filtering

\- Medication filtering

\- Trend visualisation

\- Cost analysis charts



---



\##  Technologies Used



\- Python

\- pandas

\- psycopg2

\- PostgreSQL

\- Streamlit

\- SQL



---



\## Project Structure





medication-prescribing-data-warehouse/

│

├── etl/

├── database/

├── dashboard/

├── tests/

├── main.py

├── requirements.txt

└── README.md





---



\## How to Run



1\. Install dependencies:



pip install -r requirements.txt





2\. Run ETL:



python main.py





3\. Launch dashboard:



streamlit run dashboard/app.py





---



\## Data Source



NHS Business Services Authority (NHSBSA) Open Prescribing Data  

https://www.nhsbsa.nhs.uk



All datasets are publicly available and anonymised.



---



\## Academic Context



This project was developed as part of the COM668 Computing Project module and aligns with database design, data engineering, and analytics learning outcomes.

