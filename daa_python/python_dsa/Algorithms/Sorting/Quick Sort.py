# Quick Sort algorithm
from math import *
import numpy as np
def partition(arr, pivot):
    i = 0
    j = len(arr) - 1
    while i <= j:
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i

def quick_sort(arr, n):
    if n == 1:
        return
    if n == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return
    pivot = floor((min(arr) + max(arr)) // 2)
    n_left = partition(arr, pivot)
    quick_sort(arr[:n_left], n_left)
    quick_sort(arr[n_left:], n-n_left)

if __name__ == '__main__':
    arr = np.array([12, 87, -9, -9, 88, -1, 77, 77, 90, 91, 20, 0])
    print('Original array: ', arr)
    quick_sort(arr, len(arr))
    print('Sorted array: ', arr)
