#!/bin/python3

def staircase(n):
    result = ""
    for i in range(n):
        for j in range(n):
            if j >= (n-i-1):
                result += "#"
            else:
                result += " "
        result += "\n"
    
    print(result)