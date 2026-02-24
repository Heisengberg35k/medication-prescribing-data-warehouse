import pandas as pd
import psycopg2

# --------------------------------------------------
# STEP 1: Extract unique periods from big prescribing file
# --------------------------------------------------

file_path = "data/raw/T201901PDPI BNFT.csv"

# Read only PERIOD column (not whole 804MB into memory)
df = pd.read_csv(file_path, usecols=["PERIOD"])

# Get unique periods
unique_periods = df["PERIOD"].drop_duplicates()

# --------------------------------------------------
# STEP 2: Create structured date dataframe
# --------------------------------------------------

date_rows = []

for period in unique_periods:
    period = int(period)

    year = period // 100
    month = period % 100

    month_name = pd.to_datetime(str(period), format="%Y%m").strftime("%B")

    quarter = (month - 1) // 3 + 1

    date_rows.append((period, year, month, month_name, quarter))

date_df = pd.DataFrame(
    date_rows,
    columns=["period", "year", "month", "month_name", "quarter"]
)

# --------------------------------------------------
# STEP 3: Connect to PostgreSQL
# --------------------------------------------------

conn = psycopg2.connect(
    dbname="nhs_prescribing_dwh",
    user="postgres",
    password="13006",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# --------------------------------------------------
# STEP 4: Insert into dim_date
# --------------------------------------------------

insert_query = """
INSERT INTO dim_date (period, year, month, month_name, quarter)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (period) DO NOTHING;
"""

data_tuples = [
    (row.period, row.year, row.month, row.month_name, row.quarter)
    for row in date_df.itertuples(index=False)
]

cur.executemany(insert_query, data_tuples)

conn.commit()
cur.close()
conn.close()

print("dim_date loaded successfully.")