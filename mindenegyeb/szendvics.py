#!/usr/bin/env python3


def szendvics(tartalom:str):
    def wrapper():
        print("kenyér")
        print(tartalom)
        print("kenyér")

    return wrapper()

def main():  
    sonkas_szendvics = szendvics("sonka")

    sonkas_szendvics()
if __name__ == "__main__":
    main()
