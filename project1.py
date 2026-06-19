import pandas as pd

# Load Excel file
df = pd.read_excel("Dataset for Data Analytics.xlsx")

print("===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Fill missing CouponCode values
if "CouponCode" in df.columns:
    df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Check duplicates
duplicate_rows = df.duplicated().sum()
print("\nDuplicate Rows:", duplicate_rows)

# Remove duplicates
df = df.drop_duplicates()

# Check duplicate IDs
if "OrderID" in df.columns:
    duplicate_ids = df["OrderID"].duplicated().sum()
    print("Duplicate Order IDs:", duplicate_ids)

# Check date format
if "OrderDate" in df.columns:
    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    incorrect_dates = df["OrderDate"].isnull().sum()
    print("Incorrect Dates:", incorrect_dates)

print("\n===== FINAL MISSING VALUES =====")
print(df.isnull().sum())

# Save cleaned file
df.to_excel("Cleaned_Dataset.xlsx", index=False)

print("\nData Cleaning Completed Successfully!")