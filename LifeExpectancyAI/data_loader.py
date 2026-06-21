from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "raw"
CLEANED_DIR = BASE_DIR / "cleaned"
CLEANED_DIR.mkdir(exist_ok=True)

excel_file = RAW_DIR / "2025 County Health Rankings Data - v4.xlsx"


# ------------------------------------------------------------
# Helper: Clean FIPS properly
# ------------------------------------------------------------
def clean_fips(series):
    return (
        series.astype(str)
        .str.replace(".0", "", regex=False)  # remove float artifact
        .str.strip()
        .str.zfill(5)
    )


def require_columns(df, columns, sheet_name):
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise KeyError(
            f"Missing columns in {sheet_name}: {missing}\n"
            f"Available columns include: {df.columns.tolist()[:25]}"
        )


# ------------------------------------------------------------
# 1. Load Life Expectancy
# ------------------------------------------------------------
df_le = pd.read_excel(excel_file, sheet_name="Additional Measure Data", header=1)

le_cols = ["FIPS", "State", "County", "Life Expectancy"]
require_columns(df_le, le_cols, "Additional Measure Data")

df_le = df_le[le_cols].copy()

df_le["FIPS"] = clean_fips(df_le["FIPS"])
df_le = df_le[~df_le["FIPS"].str.endswith("000")]  # remove state rows

df_le["Life Expectancy"] = pd.to_numeric(df_le["Life Expectancy"], errors="coerce")
df_le = df_le.dropna(subset=["Life Expectancy"])

print(f"OK Life Expectancy: {len(df_le)} counties")

# ------------------------------------------------------------
# 2. Load Predictors
# ------------------------------------------------------------
df_select = pd.read_excel(excel_file, sheet_name="Select Measure Data", header=1)
df_additional = pd.read_excel(excel_file, sheet_name="Additional Measure Data", header=1)

select_cols = ["FIPS", "% Some College"]
additional_cols = [
    "FIPS",
    "Median Household Income",
    "% Adults with Obesity",
    "% Adults Reporting Currently Smoking",
]

require_columns(df_select, select_cols, "Select Measure Data")
require_columns(df_additional, additional_cols, "Additional Measure Data")

df_education = df_select[select_cols].copy()
df_education.columns = ["FIPS", "education"]

df_health = df_additional[additional_cols].copy()
df_health.columns = ["FIPS", "income", "obesity", "smoking"]

df_pred = pd.merge(df_education, df_health, on="FIPS", how="inner")

df_pred["FIPS"] = clean_fips(df_pred["FIPS"])
df_pred = df_pred[~df_pred["FIPS"].str.endswith("000")]  # remove state rows

# Convert to numeric
for col in ["income", "education", "obesity", "smoking"]:
    df_pred[col] = pd.to_numeric(df_pred[col], errors="coerce")

df_pred = df_pred.dropna()

print(f"OK Predictors: {len(df_pred)} counties")

# ------------------------------------------------------------
# 3. Merge
# ------------------------------------------------------------
intersection = set(df_le["FIPS"]).intersection(set(df_pred["FIPS"]))
print(f"Matching FIPS: {len(intersection)}")

df_final = pd.merge(df_le, df_pred, on="FIPS", how="inner")
df_final = df_final.dropna()

print(f"OK Merged: {len(df_final)} counties")

# ------------------------------------------------------------
# 4. Save
# ------------------------------------------------------------
out_file = CLEANED_DIR / "health_life_exp.csv"
df_final.to_csv(out_file, index=False)

print(f"\nSaved to {out_file}")
print("Columns:", df_final.columns.tolist())
print(df_final.head())
