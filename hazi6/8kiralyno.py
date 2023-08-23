#!/usr/bin/env python3

def rajzol(l):
    print("+-----------------+")
    n = 7
    while n >= 0:
        list = ['|', '.', '.', '.', '.', '.', '.','.','.', '|']
        list[l.index(n)+1] = "Q"
        for i in list:
            print(i,end = " ")
        print()
        n -= 1
    print("+-----------------+")

def main():
    list = [7,3,0,2,5,1,6,4]
    rajzol(list)
   
if __name__ == "__main__":
    main()