#!/usr/bin/env python3

def product(l2):
    if len(l2) == 0: return 0
    s = 1
    for p in l2:
        s *= p
    return s
        

def main():
   li = []
   li.append(22)
   li.append(33)
   li.append(44)

   print(f"{li=}")

   li.pop()

   print(f"{li=}")

   li.insert(2,111)
   print(f"{li=}")
   li = [1,2,3]
   print(product(li))
   
   for i in range(2,10,3):
        print(i)





if __name__ == "__main__":
    main()