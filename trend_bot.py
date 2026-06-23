import requests

BOT_TOKEN = "8808812721:AAHxyMi93jJHguMWWXPmFHR6ECC13x_SIOQ"
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
