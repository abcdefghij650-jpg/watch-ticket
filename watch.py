import requests

URL = "https://nft.rakuten.co.jp/marketplace/?type=ticket&provider=nogizaka"

def main():
    r = requests.get(URL)
    if "該当するチケットは見つかりません" not in r.text:
        raise Exception("TICKET FOUND")

if __name__ == "__main__":
    main()
