#!/usr/bin/env python3

def main():
    s = input("Adjon meg egy szót! ")

    print(s.find('alm', 0, len(s)))


if __name__ == "__main__":
    main()