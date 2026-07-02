-- SQLite Database Schema
-- Mutual Fund Analytics Project

CREATE TABLE fund_master (
    amfi_code TEXT PRIMARY KEY,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan_type TEXT,
    launch_date DATE,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount REAL,
    min_lumpsum_amount REAL
);

CREATE TABLE nav_history (
    amfi_code TEXT,
    date DATE,
    nav REAL
);

CREATE TABLE transactions (
    investor_id INTEGER,
    transaction_date DATE,
    amfi_code TEXT,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    city_tier TEXT,
    age_group TEXT,
    gender TEXT,
    annual_income_lakh REAL,
    payment_mode TEXT,
    kyc_status TEXT
);

CREATE TABLE portfolio (
    amfi_code TEXT,
    stock_symbol TEXT,
    stock_name TEXT,
    sector TEXT,
    weight_pct REAL,
    market_value_cr REAL,
    current_price_inr REAL,
    portfolio_date DATE
);
