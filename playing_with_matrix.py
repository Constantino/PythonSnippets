#!/bin/python3

def diagonalDifference(arr):
    d1, d2 = 0,0
    length = len(arr)

    for i in range(length):
        #sum first diagonal
        d1 += arr[i][i]
        #sum second diagonal
        d2 += arr[i][length-i-1]
    
    return abs(d1-d2)