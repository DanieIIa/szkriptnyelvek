#!/usr/bin/env python3

import json

def main():
    with open("C:\Minden\Egyetem\szkriptnyelvek\data.json", "r") as json_reader:
        data = json.load(json_reader)
    data["23"].append(44)
    data["23"].append(55)
    with open("output.json", "w") as json_writer:
        json.dump(data, json_writer)
    print(data)

if __name__ == "__main__":
    main()