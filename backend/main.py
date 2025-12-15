from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Import safely from data loader
from utils.data_loader import (
    get_all_districts,
    get_district_data,
    clustered_df,
    extreme_df
)

app = FastAPI(
    title="Climate Intelligence API",
    description="API serving ML-based rainfall regime and extreme climate insights",
    version="1.0"
)

# CORS (safe for production frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # You can restrict later if needed
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------
# Root Health Check
# -----------------------
@app.get("/")
def root():
    return {"message": "Climate Intelligence API is running"}

# -----------------------
# List All Districts
# -----------------------
@app.get("/districts")
def list_districts():
    try:
        districts = get_all_districts()
        return {"districts": districts}
    except Exception as e:
        # This prevents silent 500 crashes
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------
# Get District Climate Data
# -----------------------
@app.get("/district/{district_name}")
def get_district_info(district_name: str):
    try:
        data = get_district_data(district_name)

        if not data:
            raise HTTPException(status_code=404, detail="District not found")

        return data

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# -----------------------
# DEBUG ENDPOINT (TEMPORARY)
# -----------------------
@app.get("/debug")
def debug():
    """
    Use this endpoint ONLY for debugging deployment issues.
    REMOVE after confirmation.
    """
    return {
        "clustered_csv_loaded": True,
        "extreme_csv_loaded": True,
        "clustered_rows": len(clustered_df),
        "extreme_rows": len(extreme_df),
        "clustered_columns": list(clustered_df.columns),
        "extreme_columns": list(extreme_df.columns),
    }
