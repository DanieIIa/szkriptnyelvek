#!/usr/bin/env python3

def main():
    print("1.feladat")
    print([word.upper() + '!' for word in ['auto', 'villamos', 'metro']])

    print("2.feladat")
    names = ['aladar', 'bela', 'cecil']
    print([name[0].upper() + name[1:] for name in names])

    print("3.feladat")
    nulls = [0 for n in range(0,10,1)]
    print(nulls)
 
    print("4.feladat")
    numbers = [n for n in range(1,11,1)]
    print([n*2 for n in numbers])

    print("5.feladat")
    string_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    print([int(num) for num in string_numbers])

    print("6.feladat")
    number = "1234567"
    num_list = [int(numbers[index]) for index in range(0,len(number),1)]
    print(num_list)

    print("7.feladat")
    sentence = "The quick brown fox jumps over the lazy dog"
    words = sentence.split()
    words_length = [len(word) for word in words]
    print(words_length)

    print("8.feladat")
    sentence = "python is awesome language"
    words = sentence.split()
    first_letter = [word[0] for word in words]
    print(first_letter)

    print("9.feladat")
    sentence = "The quick brown fox jumps over the lazy dog"
    words = sentence.split()
    words_length = [(word, len(word)) for word in words]
    print(words_length)

    print("10.feladat")
    e_numbers = [n for n in range(0,10,1) if(n % 2 == 0)] 
    print(e_numbers)

    print("11.feladat")
    square = [n*n for n in range(0,20,1) if ((n*n % 2) == 0) ]
    print(square)


    print("12.feladat")
    square = [n*n for n in range(0,20,1) if ((n*n%10) == 4) ]
    print(square)

    print("13.feladat")
    abc = [chr(i) for i in range(65,90,1)]
    print(abc)
    abc_string = "".join(abc)
    print(abc_string)
    
    print("14.feladat")
    fruits = [' apple ', ' banana ', ' kiwi ']
    print(["".join(fruit.split()) for fruit in fruits])

    print("15.feladat")
    list = [1,0,1,1,0,1,0,0]   
    word = ''.join([str(w) for w in list])
    print(word)
if __name__ == "__main__":
    main()