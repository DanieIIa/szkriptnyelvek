#!/usr/bin/env python3

import requests
import json

def main():  
    url = "http://jsonip.com/"
    res = requests.get(url)

    page = res.text

    res.close()
    ip = json.loads(page)
    print("Az Ön IP címe: " + ip['ip'])

if __name__ == "__main__":
    main()
