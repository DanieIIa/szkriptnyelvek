#!/usr/bin/env python3


def main():
    cellak = []
    for i in range(600):
        cellak.append(0)
    for i in range(1,len(cellak)+1):
        for j in range(1,len(cellak)+1):
            if(j % i == 0):
                if(cellak[j-1] == 0):
                    cellak[j-1] = 1
                else:
                    cellak[j-1] = 0
    print("Nyitva maradt ajtók: ")
    for i in range(0,len(cellak)):
        if(cellak[i] == 1):
            print( i+1 , end=" ")
if __name__ == "__main__":
    main()