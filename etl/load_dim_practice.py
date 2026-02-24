import pandas as pd
import psycopg2

# --------------------------------------------------
# STEP 1: Load CSV file (no header in file)
# --------------------------------------------------

file_path = "data/raw/T201901ADDR BNFT.csv"

df = pd.read_csv(file_path, header=None)

# --------------------------------------------------
# STEP 2: Assign proper column names
# --------------------------------------------------

df.columns = [
    "period",
    "practice_code",
    "practice_name",
    "address_line1",
    "address_line2",
    "city",
    "region",
    "postcode"
]

# --------------------------------------------------
# STEP 3: Create full address column
# --------------------------------------------------

df["address"] = (
    df["address_line1"].fillna("") + " " +
    df["address_line2"].fillna("") + " " +
    df["city"].fillna("") + " " +
    df["region"].fillna("")
)

# --------------------------------------------------
# STEP 4: Keep only required columns
# --------------------------------------------------

df = df[["practice_code", "practice_name", "address", "postcode"]]

# Remove duplicates just in case
df = df.drop_duplicates(subset=["practice_code"])

# --------------------------------------------------
# STEP 5: Connect to PostgreSQL
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
# STEP 6: Insert into dim_practice
# --------------------------------------------------

insert_query = """
INSERT INTO dim_practice (practice_code, practice_name, address, postcode)
VALUES (%s, %s, %s, %s)
ON CONFLICT (practice_code) DO NOTHING;
"""

data_tuples = [
    (row.practice_code, row.practice_name, row.address, row.postcode)
    for row in df.itertuples(index=False)
]

cur.executemany(insert_query, data_tuples)

conn.commit()
cur.close()
conn.close()

print("dim_practice loaded successfully.")