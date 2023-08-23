#!/usr/bin/env python3

import re
from numpy import empty


class Bag:
    def __init__(self):
        self.data = list()
    def add(self, v):
        self.data.append(v)
    def add_twice(self, v):
        self.data.append(v)
        self.data.append(v)

    def __lt__(self, other): #kisebb mint
        return len(self) < len(other)

    def __len__(self):
        return len(self.data)


    def __str__(self): #mindenképp stringgel kell visszatérnie, felülirja a metódust
        return "Bag("+str(self.data)[1:-1]+")"

def main():
    bag = Bag()

    empty_bag = Bag()
    bag.add(12)
    bag.add_twice(33)
    
    print(bag)
    print(f"{len(bag)}")
    print(f"{len(empty_bag)}")


if __name__ == "__main__":
    main()