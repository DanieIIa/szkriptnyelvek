#!/usr/bin/env python3

class Empty(object):
    pass

class Greeting:
    def __init__(self, name):
        self.name = name
        
    def greet(self):
        print(f"Hello {self.name}!")

def main():
    empty = Empty()
    empty.x = 12
    empty.y = 4

    #del empty.x
    print(empty)
    print(empty.x)

    me = Greeting()
    me.name = "Daniella"
    me.greet()
    
   
if __name__ == "__main__":
    main()