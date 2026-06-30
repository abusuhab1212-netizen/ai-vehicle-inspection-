import os
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

# रेंडर से पासवर्ड उठाएं
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

@app.get("/")
def home():
    return {"message": "Vehicle Inspection API is Running!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/admin")
def admin_login(x_password: str = Header(None)):
    if x_password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid Admin Password")
    return {"message": "Welcome, Shoaib! Admin panel is open."}
