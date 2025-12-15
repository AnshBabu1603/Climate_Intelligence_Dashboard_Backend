from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from utils.data_loader import get_all_districts, get_district_data

app = FastAPI(
    title = "Climate Intelligence API",
    description = "API serving ML-based rainfall regime and extreme climate insights",
    version = "1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def root():
    return {"message": "Climate Intelligence API is running"}

@app.get("/districts")
def list_districts():
    return {"districts": get_all_districts()}

@app.get("/district/{district_name}")
def get_district_info(district_name: str):
    data = get_district_data(district_name)

    if not data:
        raise HTTPException(status_code = 404, detail = "District not found")
    
    return data