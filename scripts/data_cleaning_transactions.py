import pandas as pd

try:
    # Load dataset
    transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

    print("File loaded successfully!\n")

    print("Columns:")
    print(transactions.columns.tolist())

    print("\nFirst 5 rows:")
    print(transactions.head())

    print("\nInfo:")
    print(transactions.info())

    # Convert transaction_date to datetime
    transactions["transaction_date"] = pd.to_datetime(
        transactions["transaction_date"],
        errors="coerce"
    )

    print("\nDate converted successfully!")

    # Check transaction types
    print("\nTransaction Types:")
    print(transactions["transaction_type"].unique())

    # Check KYC status
    print("\nKYC Status:")
    print(transactions["kyc_status"].unique())

    # Validate amount > 0
    print("\nInvalid Amount Count:")
    print((transactions["amount_inr"] <= 0).sum())

    # Standardize transaction types
    transactions["transaction_type"] = (
        transactions["transaction_type"]
        .replace({
            "Sip": "SIP",
            "sip": "SIP",
            "Lumpsum": "Lumpsum",
            "lumpsum": "Lumpsum",
            "Redemption": "Redemption",
            "redemption": "Redemption"
        })
    )

    print("\nTransaction Types After Cleaning:")
    print(transactions["transaction_type"].unique())

    # Save cleaned dataset
    transactions.to_csv(
        "data/processed/08_investor_transactions_clean.csv",
        index=False
    )

    print("\nCleaned file saved successfully!")

except Exception as e:
    print("ERROR:")
    print(e)

