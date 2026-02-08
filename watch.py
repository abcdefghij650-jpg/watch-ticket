import requests
import os

URL = "https://nft.rakuten.co.jp/marketplace/?type=ticket&provider=nogizaka"
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def notify(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg}
    )

def main():
    r = requests.get(URL, timeout=10)
    if "該当するチケットは見つかりません" not in r.text:
        notify("🚨 楽天NFTチケット出現！\n" + URL)
        raise Exception("FOUND")

if __name__ == "__main__":
    main()
