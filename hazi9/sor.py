#!/usr/bin/env python3

class MyStack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def append(self, item):
        self.items.insert(0,item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()

    def size(self):
        return len(self.items)

class MyQueue(MyStack):
    def __init__(self):
        self.stack1 = MyStack()
        self.stack2 = MyStack()
    
    def append(self, item):
        return self.stack1.append(item)

    def popleft(self):
        self.stack1.items = self.items
        for i in range(0, self.stack1.size()-1,1):
            self.stack2.append(self.stack1.pop())
        for i in range(0, self.stack2.size(),1):
            self.append(self.stack2.pop())
        
        return self.pop()

    def is_empty(self):
        return self.isEmpty()

    def size(self):
        return super().size()



def main():
    sorom = MyQueue()
    
    sorom.items = [4,5,6,6,7,8]
    print("A sor elemei: ")
    print(sorom.items)
    print("A sor mérete: ")
    print(sorom.size()) 
    if(sorom.is_empty()):
        print("A sor ures")
    else:
        print("A sor nem ures")
    sorom.items.append(5)
    print("A sor elemei egy elem beszúrása után: ")
    print(sorom.items)   
    print("A sorból kivett elem: ")
    print(sorom.popleft())
    print("A sor elemei kivétel után")
    print(sorom.items)
    

if __name__ == "__main__":
    main()