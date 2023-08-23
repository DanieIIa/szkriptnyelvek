#!/usr/bin/env python3

import requests
import json

def get_object(id: str) -> dict:
     response_text = requests.get(f'https://youtube.com/oembed?url=https://www.youtube.com/watch?v={id}').text
     return json.loads(response_text)

def main():
   print(get_object("55iwMYv8tGI")["title"])
if __name__ == "__main__":
    main()
