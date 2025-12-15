import pandas as pd

clustered_df = pd.read_csv(r"C:\Users\manis\OneDrive\Desktop\Unsupervised_Rainfall_Pattern_Detection\backend\data\clustered_rainfall_regimes.csv")
extreme_df = pd.read_csv(r"C:\Users\manis\OneDrive\Desktop\Unsupervised_Rainfall_Pattern_Detection\backend\data\extreme_rainfall_districts_dbscan.csv")

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