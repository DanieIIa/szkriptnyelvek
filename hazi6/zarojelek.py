#!/usr/bin/env python3

def test(expression):
    v = []
    correct = False
    for index in range(len(expression)):
        if(expression[index] == '{' or expression[index] == '[' or expression[index] == '('):
            v.append(expression[index])
        elif (expression[index] == '}' or expression[index] == ']' or expression[index] == ')'):
            out = v.pop()
            if((out == '{' and expression[index] == '}') or (out == '(' and expression[index] == ')') or(out == '[' and expression[index] == ']')):
                correct = True
            else: return False   
    return correct

def main():
    print(test("((5+3)*2+1)"))
    print(test("(3+{1-1)}"))
    print(test("[1+1]+(2*2)-{3/3}"))
if __name__ == "__main__":
    main()