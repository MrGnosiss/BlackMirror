import os
from PIL import Image
from PIL.ExifTags import TAGS

def extract(filepath):
    print(f"\n[+] Metadata for: {filepath}")
    try:
        image = Image.open(filepath)
        info = image._getexif()
        if info:
            for tag, value in info.items():
                print(f"{TAGS.get(tag)}: {value}")
        else:
            print("[-] No EXIF metadata found.")
    except:
        print("[-] File not supported or corrupted.")
