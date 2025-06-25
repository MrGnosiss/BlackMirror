import requests
from bs4 import BeautifulSoup

def search(query):
    print(f"\n[+] Google Dorking for: {query}")
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        r = requests.get(f"https://www.google.com/search?q={query}", headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if "http" in href:
                print(href)
    except:
        print("[-] Google blocking requests.")
