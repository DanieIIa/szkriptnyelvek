#!/usr/bin/env python3

import requests

#https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=55iwMYv8tGI


def main():
    url = "https://python.org"
    res = requests.get(url)
    
    page = res.text

    res.close()

    print(page)
if __name__ == "__main__":
    main()

"""
feladat
def get_object(id: str) -> dict:

  response_text = requests.get(f'https://youtube.com/oembed?url=https://www.youtube.com/watch?v={id}').text

  return json.loads(response_text)
""""