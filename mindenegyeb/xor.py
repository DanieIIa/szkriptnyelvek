#!/usr/bin/env python3

def xor(value1, value2):
    return (bool(value1) != bool(value2) and (bool(value1) or bool(value2)))
        
    
def main():
    print(xor("python", None))


if __name__ == "__main__":
    main()
