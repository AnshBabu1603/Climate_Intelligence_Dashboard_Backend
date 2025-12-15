import pandas as pd
import os

# -------------------------------------------------
# Paths
# -------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

clustered_path = os.path.join(BASE_DIR, "data", "clustered_rainfall_regimes.csv")
extreme_path = os.path.join(BASE_DIR, "data", "extreme_rainfall_districts_dbscan.csv")

# -------------------------------------------------
# Load CSVs safely
# -------------------------------------------------
try:
    clustered_df = pd.read_csv(clustered_path)
except Exception as e:
    raise RuntimeError(f"Failed to load clustered CSV: {e}")

try:
    extreme_df = pd.read_csv(extreme_path)
except Exception as e:
    raise RuntimeError(f"Failed to load extreme CSV: {e}")

# -------------------------------------------------
# 🔐 NORMALIZE DISTRICT NAMES (CRITICAL FIX)
# -------------------------------------------------
clustered_df["DISTRICT_NORM"] = (
    clustered_df["DISTRICT"].astype(str).str.strip().str.lower()
)

extreme_df["DISTRICT_NORM"] = (
    extreme_df["DISTRICT"].astype(str).str.strip().str.lower()
)

# -------------------------------------------------
# Get all districts (for selector)
# -------------------------------------------------
def get_all_districts():
    return sorted(clustered_df["DISTRICT"].dropna().unique().tolist())

# -------------------------------------------------
# Get single district data (CASE-INSENSITIVE)
# -------------------------------------------------
def get_district_data(district_name: str):
    if not district_name:
        return None

    district_key = district_name.strip().lower()

    row = clustered_df[
        clustered_df["DISTRICT_NORM"] == district_key
    ]

    if row.empty:
        return None

    is_extreme = district_key in extreme_df["DISTRICT_NORM"].values

    r = row.iloc[0]

    return {
        "district": r["DISTRICT"],
        "state": r["STATE_UT_"],
        "climate_regime": r["Climate_Regime"],
        "annual_intensity": float(r["annual_intensity"]),
        "monsoon_dominance": float(r["monsoon_dominance"]),
        "rainfall_cv": float(r["rainfall_cv"]),
        "seasonal_entropy": float(r["seasonal_entropy"]),
        "extreme_risk": bool(is_extreme),
        "seasonal_distribution": {
            "winter": float(r["winter_pct"] * 100),
            "summer": float(r["summer_pct"] * 100),
            "monsoon": float(r["monsoon_pct"] * 100),
            "post_monsoon": float(r["post_monsoon_pct"] * 100),
        },
    }


