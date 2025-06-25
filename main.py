from modules import domain_osint, email_osint, username_osint, metadata_extractor, dorking
import argparse

def main():
    parser = argparse.ArgumentParser(description="BlackMirror - OSINT Framework")
    parser.add_argument("-d", "--domain", help="Domain for OSINT")
    parser.add_argument("-e", "--email", help="Email for OSINT")
    parser.add_argument("-u", "--username", help="Username for OSINT")
    parser.add_argument("-f", "--file", help="File to extract metadata")
    parser.add_argument("--dork", help="Google dork term")

    args = parser.parse_args()

    if args.domain:
        domain_osint.scan(args.domain)
    if args.email:
        email_osint.scan(args.email)
    if args.username:
        username_osint.scan(args.username)
    if args.file:
        metadata_extractor.extract(args.file)
    if args.dork:
        dorking.search(args.dork)

if __name__ == "__main__":
    main()
