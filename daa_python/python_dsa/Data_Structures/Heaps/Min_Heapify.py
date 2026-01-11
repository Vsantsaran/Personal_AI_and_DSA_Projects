# this is a program as to MIN-HEAPIFY a heap (array)
from numpy import *
arr = array([12, 45, 89, 45, 78, 34, -9, -88, -11, -9, 0, 99, 0])

def BUILD_MIN_HEAPIFY():
	'''Build max heap'''
	current = len(arr) // 2 - 1
	for current in range(current, -1, -1):
		MIN_HEAPIFY(current)

def MIN_HEAPIFY(i):
	'''MAX-HEAPIFY'''
	heap_size = len(arr)
	left = 2*i + 1
	right = 2*i + 2
	while left < heap_size:
		smallest = i
		if arr[left] < arr[i]:
			if arr[left] < arr[right]:
				smallest = left
			else: smallest = right
		elif arr[right] < arr[i]:
			smallest = right
		if i != smallest:
			arr[i], arr[smallest] = arr[smallest], arr[i]
			MIN_HEAPIFY(smallest)
		else: return

if __name__ == '__main__':
	print('Original array: ', arr)
	BUILD_MIN_HEAPIFY()
	print(f'MIN HEAP: {arr}')
