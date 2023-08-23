#!/usr/bin/env python3

import time

def main():
    szam = float(input("Várakozási idő: "))
    szam += 1
    
    time.sleep(szam)
    
    print(szam)    

if __name__ == "__main__":
    main()

