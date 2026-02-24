-- ============================================
-- DIMENSION TABLE: PRACTICE
-- ============================================

CREATE TABLE dim_practice (
    practice_id SERIAL PRIMARY KEY,
    practice_code VARCHAR(10) UNIQUE NOT NULL,
    practice_name VARCHAR(255),
    address VARCHAR(255),
    postcode VARCHAR(20)
);

-- ============================================
-- DIMENSION TABLE: MEDICATION
-- ============================================

CREATE TABLE dim_medication (
    medication_id SERIAL PRIMARY KEY,
    bnf_code VARCHAR(20) UNIQUE NOT NULL,
    bnf_name TEXT
);

-- ============================================
-- DIMENSION TABLE: DATE
-- ============================================

CREATE TABLE dim_date (
    date_id SERIAL PRIMARY KEY,
    period INTEGER UNIQUE NOT NULL,
    year INTEGER,
    month INTEGER,
    month_name VARCHAR(20),
    quarter INTEGER
);

-- ============================================
-- FACT TABLE: PRESCRIBING
-- ============================================

CREATE TABLE fact_prescribing (
    prescribing_id SERIAL PRIMARY KEY,
    practice_id INTEGER REFERENCES dim_practice(practice_id),
    medication_id INTEGER REFERENCES dim_medication(medication_id),
    date_id INTEGER REFERENCES dim_date(date_id),
    items INTEGER,
    nic NUMERIC(12,2),
    act_cost NUMERIC(12,2),
    quantity INTEGER
);