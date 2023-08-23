#!/usr/bin/env python3

def hangrend(words):
    mely_maganh = ['a', 'á', 'o', 'u', 'ú']
    magas_maganh = ['e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű']
    mely_maganh = set(mely_maganh)
    magas_maganh = set(magas_maganh)
    for word in words:
        magas = False
        mely = False
        for i in range(0, len(word)):
            if( magas == False):
                magas = word[i] in magas_maganh
            if(mely == False):
                mely = word[i] in mely_maganh
        if(magas and not mely):
            print(word + " magas")
        elif(not magas and mely):
            print(word + " mély")
        elif(magas and mely):
            print(word + " vegyes")
        else:
            print(word + " semmilyen")
def main():
    words = ["ablak", "ajtó", "kisvasút", "magas", "mély", "Pfff"]
    hangrend(words)

if __name__ == "__main__":
    main()

