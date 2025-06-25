def scan(username):
    print(f"\n[+] USERNAME OSINT for: {username}")
    social_sites = [
        f"https://github.com/{username}",
        f"https://twitter.com/{username}",
        f"https://instagram.com/{username}",
        f"https://www.reddit.com/user/{username}"
    ]
    for site in social_sites:
        try:
            r = requests.get(site)
            if r.status_code == 200:
                print(f"[+] Found profile: {site}")
        except:
            pass
