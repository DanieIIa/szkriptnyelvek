#!/usr/bin/env python3

def normalize(word):
    """Visszaadja a szöveget egy normalizáls állapotban
    (szóközök és nagybetűk eltávolítása)"""
    return word.lower().replace(" ","")

def anagramma(word1, word2):
    norm1 = normalize(word1)
    norm2 = normalize(word2)
    word1_list = [norm1[n] for n in range(0,len(norm1),1) ]
    word2_list = [norm2[n] for n in range(0,len(norm2),1) ]
    word1_list.sort()
    word2_list.sort()
    return word1_list == word2_list
def main():
    if(anagramma("A gentleman", "Elegant man")):
        print("A ket szo anagrammaja egymasnak")
    else:
        print("A ket szo nem anagrammaja egymasnak")
   
if __name__ == "__main__":
    main()

