import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

clustered_path = os.path.join(BASE_DIR, "data", "clustered_rainfall_regimes.csv")
extreme_path = os.path.join(BASE_DIR, "data", "extreme_rainfall_districts_dbscan.csv")

try:
    clustered_df = pd.read_csv(clustered_path)
except Exception as e:
    raise RuntimeError(f"Failed to load clustered CSV: {e}")

try:
    extreme_df = pd.read_csv(extreme_path)
except Exception as e:
    raise RuntimeError(f"Failed to load extreme CSV: {e}")



def get_all_districts():
    return sorted(clustered_df["DISTRICT"].unique().tolist())

def get_district_data(district_name: str):
    row = clustered_df[clustered_df["DISTRICT"] == district_name]

    if row.empty:
        return None
    
    is_extreme = district_name in extreme_df["DISTRICT"].values

    import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

clustered_path = os.path.join(BASE_DIR, "data", "clustered_rainfall_regimes.csv")
extreme_path = os.path.join(BASE_DIR, "data", "extreme_rainfall_districts_dbscan.csv")

try:
    clustered_df = pd.read_csv(clustered_path)
except Exception as e:
    raise RuntimeError(f"Failed to load clustered CSV: {e}")

try:
    extreme_df = pd.read_csv(extreme_path)
except Exception as e:
    raise RuntimeError(f"Failed to load extreme CSV: {e}")



def get_all_districts():
    return sorted(clustered_df["DISTRICT"].unique().tolist())

def get_district_data(district_name: str):
    row = clustered_df[clustered_df["DISTRICT"] == district_name]

    if row.empty:
        return None
    
    is_extreme = district_name in extreme_df["DISTRICT"].values

    return {
        "district": district_name,
        "climate_regime": row.iloc[0]["Climate_Regime"],
        "annual_intensity": float(row.iloc[0]["annual_intensity"]),
        "monsoon_dominance": float(row.iloc[0]["monsoon_dominance"]),
        "rainfall_cv": float(row.iloc[0]["rainfall_cv"]),
        "seasonal_entropy": float(row.iloc[0]["seasonal_entropy"]),
        "extreme_risk": is_extreme,
        "seasonal_distribution": {
            "winter": float(row.iloc[0]["winter_pct"] * 100),
            "summer": float(row.iloc[0]["summer_pct"] * 100),
            "monsoon": float(row.iloc[0]["monsoon_pct"] * 100),
            "post_monsoon": float(row.iloc[0]["post_monsoon_pct"] * 100)
        }

    }




    }



