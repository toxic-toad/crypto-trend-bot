import os
import requests
import random

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = "1237652497"

trends = [
    "Solana",
    "Jupiter",
    "Pump.fun",
    "Bitcoin ETF",
    "Hyperliquid",
    "Ethereum",
    "BONK",
    "DePIN",
    "AI Agents",
    "Base"
]

trend = random.choice(trends)

message = f"""
🔥 Crypto Trend Alert

Topic: {trend}

Tweet Idea:

🚀 {trend} is one of the most discussed topics in crypto right now.

Smart money follows narratives before the crowd.

What's your take?

#Crypto #Web3
"""

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
