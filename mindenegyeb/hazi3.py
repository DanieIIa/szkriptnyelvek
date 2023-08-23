#!/usr/bin/env python3

def palindrom1(s):
    if(s == s[::-1]):
        return True

def palindrom2(s):
    i = 0
    while(i <= (len(s)/2)):
        if(s[i] != s[len(s)-1-i]):
            return False 
        i += 1
    return True

def palindrom3(s):
    if len(s) < 2: return True
    if s[0] != s[-1]: return False
    return palindrom3(s[1:-1])

def main():
    if (palindrom1("aha")):
        print("A szó palindrom")
    else:
        print("Nem palindrom")
    if (palindrom2("ahhhja")):
        print("A szó palindrom")
    else:
        print("Nem palindrom")
    if (palindrom3("alkla")):
        print("A szó palindrom")
    else:
        print("Nem palindrom")



if __name__ == "__main__":
    main()