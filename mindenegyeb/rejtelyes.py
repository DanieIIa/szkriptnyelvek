#!/usr/bin/env python3

TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""
def main():
    decoded = ""
    for i in range(0, len(TEXT)):
        if(TEXT[i].isalpha() and (TEXT[i]) != 'y' and (TEXT[i]) != 'Y'):
            decoded += chr(ord(TEXT[i]) +2)
        elif(TEXT[i] == 'y' and TEXT[i].isalpha() or (TEXT[i]) == 'Y'):
            decoded += chr(ord(TEXT[i])-24)
        else:
            decoded += TEXT[i]
    print(decoded)

if __name__ == "__main__":
    main()