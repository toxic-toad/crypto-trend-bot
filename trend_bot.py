import requests

BOT_TOKEN = "PASTE_BOT_TOKEN_HERE"
CHAT_ID = "1237652497"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": text
        }
    )

send_message(
    "🚀 Crypto Trend Bot is online!\n\nThis is a test message."
)
