#!/usr/bin/env python3

import os

PYTHON_STR = """#!/usr/bin/env python3 
                         
def main():  
    print('Py3')

###########################


if __name__ == "__main__":
    main()
"""
C_STR = """#include <stdio.h>

int main()
{
    printf("Hello");

    return 0;
}
"""
def main():
    print("-"*29 + "\n Create an empty source file \n" + "-"*29)
    datas = ["1) Python [py]", "2) C \t  [c]", "q) quit" ]
    for data in datas:
        print(data)
    number= input(">")
    for data in datas:
        if(number != "q" and data[0] != "q"):
            if int(number) == int(data[0]) and int(number) == 1:
                if(not os.path.isfile("alap.py")):
                    f = open("alap.py", 'w')
                    f.write(PYTHON_STR)
                    f.close()
                else:
                    print("Már van ilyen fájl")
            elif int(number) == int(data[0]) and int(number) == 2:
                if(not os.path.isfile("alap.c")):
                    g = open("alap.c", 'w')
                    g.write(C_STR)
                    g.close()
                else:
                    print("Már van ilyen fájl") 
        
if __name__ == "__main__":
    main()