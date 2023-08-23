#!/usr/bin/env python3

import random
import math


def main():
    total = 0
    in_circle = 0
    for i in range(0, 300000):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if(math.sqrt(x*x + y*y) <= 1):
            in_circle += 1
        total += 1
    pi = 4*(in_circle/total)
    print(pi)
    

if __name__ == "__main__":
    main()