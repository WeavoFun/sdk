from fastapi import FastAPI
from core.signal import Signal

app = FastAPI(title="WEAVO Intelligence API")

latest_signal = None

@app.get("/")
def root():
    return {"message": "WEAVO API Running"}

@app.get("/signal")
def get_signal():
    if latest_signal:
        return latest_signal
    return {"status": "No signal yet"}
