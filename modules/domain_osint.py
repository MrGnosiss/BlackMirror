import whois
import socket
import dns.resolver

def scan(domain):
    print(f"\n[+] DOMAIN OSINT for: {domain}")
    try:
        whois_info = whois.whois(domain)
        print("[+] WHOIS Data:")
        print(whois_info)
    except:
        print("[-] WHOIS lookup failed.")
    
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] IP Address: {ip}")
    except:
        print("[-] Couldn't resolve domain.")
    
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            print(f"[+] DNS A Record: {rdata.address}")
    except:
        print("[-] DNS lookup failed.")
