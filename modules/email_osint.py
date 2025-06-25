import requests

def scan(email):
    print(f"\n[+] EMAIL OSINT for: {email}")
    try:
        hunter = f"https://api.hunter.io/v2/email-verifier?email={email}&api_key=YOUR_HUNTER_API_KEY"
        data = requests.get(hunter).json()
        print(data)
    except:
        print("[-] Email OSINT failed.")
