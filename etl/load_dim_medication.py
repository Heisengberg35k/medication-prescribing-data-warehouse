import pandas as pd
import psycopg2

# --------------------------------------------------
# STEP 1: Load medication reference CSV
# --------------------------------------------------

file_path = "data/raw/T201901CHEM SUBS.csv"

df = pd.read_csv(file_path)

# --------------------------------------------------
# STEP 2: Keep only required columns
# --------------------------------------------------

df = df[["CHEM SUB", "NAME"]]

# Rename columns to match database naming
df = df.rename(columns={
    "CHEM SUB": "bnf_code",
    "NAME": "bnf_name"
})

# --------------------------------------------------
# STEP 3: Clean data
# --------------------------------------------------

# Remove null codes
df = df[df["bnf_code"].notna()]

# Convert to string to preserve leading zeros
df["bnf_code"] = df["bnf_code"].astype(str)

# Remove duplicates
df = df.drop_duplicates(subset=["bnf_code"])

# --------------------------------------------------
# STEP 4: Connect to PostgreSQL
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
# STEP 5: Insert into dim_medication
# --------------------------------------------------

insert_query = """
INSERT INTO dim_medication (bnf_code, bnf_name)
VALUES (%s, %s)
ON CONFLICT (bnf_code) DO NOTHING;
"""

data_tuples = [
    (row.bnf_code, row.bnf_name)
    for row in df.itertuples(index=False)
]

cur.executemany(insert_query, data_tuples)

conn.commit()
cur.close()
conn.close()

print("dim_medication loaded successfully.")


