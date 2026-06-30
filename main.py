from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Vehicle Inspection API is Running!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
