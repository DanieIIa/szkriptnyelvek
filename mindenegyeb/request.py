#!/usr/bin/env python3

import requests

def main():
    url = "https://python.org"
    res = requests.get(url)
    
    page = res.text

    res.close()

    print(page)
if __name__ == "__main__":
    main()