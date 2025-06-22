
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/quotex-signals")
def get_signals():
    assets = ["EUR/USD", "GBP/JPY", "AUD/CAD", "USD/CHF"]
    actions = ["BUY", "SELL"]
    confidences = ["High", "Medium", "Low"]
    signals = []
    for _ in range(5):
        signals.append({
            "asset": random.choice(assets),
            "action": random.choice(actions),
            "confidence": random.choice(confidences),
            "time": datetime.now().strftime("%I:%M %p")
        })
    return signals
