# https://www.hackerrank.com/challenges/almost-sorted/problem

import math
import os
import random
import re
import sys


def caso2(arr):
    n = len(arr)
    peak = -1
    valley = -1
    i = 0
    while i < n-1 and arr[i] < arr[i+1]: 
        i+=1
    peak = i
    
    while i < n-1 and arr[peak] >= arr[i]:
        i+=1
    valley = i-1
    
    if arr[valley] < arr[valley-1] and arr[valley] < arr[valley+1]:
        return peak, valley
    return -1, -1

def caso1(arr):
    n = len(arr)
    peak1 = -1
    peak2 = -1
    valley1 = -1
    valley2 = -1
    i = 0
    
    while i < n-1 and arr[i] < arr[i+1]:
        i+=1
    peak1 = i
    valley1 = i+1
    i+=2
    
    while i < n-1 and arr[i] > arr[valley1]:
        i+=1
    peak2 = i-1
    valley2 = i
    
    if arr[valley2] < arr[peak2] and arr[valley2] < arr[valley2+1]:
        return peak1, valley2
    return -1, -1

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def swap(arr, l, r):
    temp = arr[r]
    arr[r] = arr[l]
    arr[l] = temp
    #print(arr)
    if is_sorted(arr):
        print('yes')
        print('swap', l+1, r+1)
    else:
        print('no')
    
def reversee(arr, l, r):
    i = l
    j = r
    while i <= j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -=1
    #print(arr)
    if is_sorted(arr):
        print('yes')
        print('reverse', l+1, r+1)
    else:
        print('no')

def almostSorted(arr):
    if is_sorted(arr):
        print('yes')
        return
    n = len(arr)
    if arr[1] < arr[0] and n==2:
        print('yes')
        print('swap', 1, 2)
        return
    else:
        p, v = caso1(arr)
        if p != -1:
            swap(arr, p, v)
            return
        p, v = caso2(arr)
        if p != -1:
            if v-p == 1:
                 swap(arr, p, v)
                 return
            reversee(arr, p, v)
            return
    print('no')
        
    

n = int(input())

arr = list(map(int, input().rstrip().split()))

almostSorted(arr)



