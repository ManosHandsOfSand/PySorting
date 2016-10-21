
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 14:24:53 2016

@author: f401051
"""
    
def BubbleSort(obj, ascending=True):
    li = []
    for val in obj:
        li.append(val)
    if ascending == True:
        for i in range(len(li)):
            for j in range(len(li)-1-i):
                if li[j] > li[j+1]:
                    li[j], li[j+1] = li[j+1], li[j]

    elif ascending == False:
        for i in range(len(li)):
            for j in range(len(li)-1-i):
                if li[j] < li[j+1]:
                    li[j], li[j+1] = li[j+1], li[j]

    return li
    
def QuickSort(li):
    if len(li) > 1:
        pivot_index = len(li)/2
        small = []
        large = []
                
        for i in range(len(li)):
            if i != pivot_index:
                if li[i] < li[pivot_index]:
                    small.append(li[i])
                else:
                    large.append(li[i])
        QuickSort(small)
        QuickSort(large)
        li[:] = small + [li[pivot_index]] + large
        return li
        
def QuickSortDesc(li):
    if len(li) > 1:
        pivot_index = len(li)/2
        small = []
        large = []
                
        for i in range(len(li)):
            if i != pivot_index:
                if li[i] < li[pivot_index]:
                    small.append(li[i])
                else:
                    large.append(li[i])
        QuickSort(small)
        QuickSort(large)
        li[:] = large + [li[pivot_index]] + small           
        return li
        
test = [3, 5, 2, 8, 9, 1, 3, 10, 15, 20, 100, 95, 12, 13, 18, 23]
        
testing = BubbleSort(test, ascending=False)
print(testing)

QS = QuickSort(test)
print(QS)
            
