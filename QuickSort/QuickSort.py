# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:46:30 2016

@author: Jake
"""

file = open('QuickSort.txt', 'r')
alist = []
for i in file.readlines():
    alist.append(int(i))
    
def QuickSort(alist):
    QuickSortHelp(alist, 0, len(alist)-1)
    
    
def QuickSortHelp(alist, first, last):
    if last <= first:        
        return
    
    else:
        splitpoint = Partition(alist, first, last)
        QuickSortHelp(alist, first, splitpoint-1)
        QuickSortHelp(alist, splitpoint+1, last)
        
def FindMedian(alist, a, b, c):
    return(alist[a] < alist[b] and alist[a] > alist[c]) or\
    (alist[a] > alist[b] and alist[a] < alist[c])
        
comp = 0    
def Partition(alist, first, last):

    #First
    pivot = alist[first]
    
    #Last
    alist[last], alist[first] = alist[first], alist[last]
    
    #Median
    middle = (first + last) // 2
    
    if FindMedian(alist, first, middle, last):
        pivot = alist[first]
    elif FindMedian(alist, middle, first, last):
        pivot = alist[middle]
        alist[middle], alist[first] = alist[first], alist[middle]
    else:
        pivot = alist[last]
        alist[last], alist[first] = alist[first], alist[last]
        
    print(pivot)
    
    pointer = first + 1

    global comp
    comp += last - first
    for index in range(first+1, last+1):
        if alist[index] < pivot:
            alist[index], alist[pointer] = alist[pointer], alist[index]
            pointer += 1

    alist[pointer-1], alist[first] = alist[first], alist[pointer-1] 

    return pointer - 1
    
     
#alist = [6,4,8,7,3,5,2,9,1]
QuickSort(alist)
print(alist)
print(comp)