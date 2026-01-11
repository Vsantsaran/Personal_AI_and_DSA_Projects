# this is a program as to MAX-HEAPIFY a heap (array)
from numpy import *
arr = array([12, 45, 89, 45, 78, 34, -9, -88, -11, -9, 0, 99, 0])

def BUILD_MAX_HEAPIFY():
	'''Build max heap'''
	current = len(arr) // 2 - 1
	for current in range(current, -1, -1):
		MAX_HEAPIFY(current)

def MAX_HEAPIFY(i):
	'''MAX-HEAPIFY'''
	heap_size = len(arr)
	left = 2*i + 1
	right = 2*i + 2
	while left < heap_size:
		largest = i
		if arr[left] > arr[i]:
			if arr[left] > arr[right]:
				largest = left
			else: largest = right
		elif arr[right] > arr[i]:
			largest = right
		if i != largest:
			arr[i], arr[largest] = arr[largest], arr[i]
			MAX_HEAPIFY(largest)
		else: return

if __name__ == '__main__':
	print('Original array: ', arr)
	BUILD_MAX_HEAPIFY()
	print(f'MAX_HEAP: {arr}')
