#!/usr/bin/env python3

def hamming_tav(str1, str2):
    if(len(str1) != len(str2)):
        return print("Nem meghatározható a Hamming-távolság")
    str1_l = [str1[i] for i in range(0, len(str1), 1)]    
    str2_l = [str2[i] for i in range(0, len(str2), 1)]
    counter = 0
    for index in range(0, len(str1),1):
        if(str1_l[index] != str2_l[index]):
            counter += 1
    print("A két szó Hamming-távolsága:", counter)



def main():
    hamming_tav("toneda", "roses")
    hamming_tav("toned", "roses")
    
   
if __name__ == "__main__":
    main()