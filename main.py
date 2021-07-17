import requests

from configuration import positions, websites

HEADERS = {
    "User-Agent": """Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0)
                     Gecko/20100101 Firefox/76.0"""
}


def main():
    for url in websites:
        try:
            response = requests.get(url, headers=HEADERS)
            if response.status_code == 200:
                for position in positions:
                    r = response.text.lower().find(position)
                    if r > -1:
                        print(f"check positions in {url}")
            else:
                print(f"Error on {url}, status {response.status_code}")

        except Exception:
            print(f"An exception occurred in {url}")


if __name__ == "__main__":
    main()
