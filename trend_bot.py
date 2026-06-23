import requests

BOT_TOKEN = "8808812721:AAHxyMi93jJHguMWWXPmFHR6ECC13x_SIOQ"
CHAT_ID = "1237652497"

crypto_trends = [
    "Bitcoin ETF",
    "Solana",
    "Ethereum",
    "Jupiter",
    "Pump.fun",
    "BONK",
    "DePIN",
    "AI Agents",
    "Base Chain",
    "Hyperliquid"
]

trend = crypto_trends[0]

message = f"""
🔥 Crypto Trend Alert

Trending Topic:
{trend}

Tweet Idea:

🚀 {trend} is gaining attention across the crypto ecosystem.

Are you paying attention or are you still early?

#Crypto #Web3
"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
