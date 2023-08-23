#!/usr/bin/env python3

def createdimond(height):
    if(height % 2 == 0):
        return "Invalid number"
    else:
        index = 1
        counter = height-1
        txt = ""
        while(index <= height):
            if(index <= (height/2+1)):
                txt = '*' * (2*index-1)
            else:
                txt = '*' * (counter - 1) 
                counter -= 2
            print(txt.center(height, ' '))
            index += 1
def main():
    createdimond(9)


if __name__ == "__main__":
    main()
