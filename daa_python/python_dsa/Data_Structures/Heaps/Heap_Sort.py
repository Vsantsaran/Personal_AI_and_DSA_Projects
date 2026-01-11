# heap sort
from numpy import *
arr = array([12, 45, 89, 45, 78, 34, -9, -88, -11, -9, 0, 99, 0])
heap_size = len(arr)

def BUILD_MAX_HEAPIFY():
	'''Build max heap'''
	current = (heap_size // 2) - 1
	for current in range(current, -1, -1):
		MAX_HEAPIFY(current, heap_size)

def MAX_HEAPIFY(i, n):
	'''MAX-HEAPIFY'''
	left = 2*i + 1
	right = 2*i + 2
	while left < n:
		largest = i
		if arr[left] > arr[i]:
			if arr[left] > arr[right]:
				largest = left
			else: largest = right
		elif arr[right] > arr[i]:
			largest = right
		if i != largest:
			arr[i], arr[largest] = arr[largest], arr[i]
			MAX_HEAPIFY(largest, n)
		else: return

def heap_sort():
	'''heap sort'''
	BUILD_MAX_HEAPIFY()
	for i in range(heap_size-1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		MAX_HEAPIFY(0, i-1)

if __name__ == '__main__':
	print('Original array: ', arr)
	heap_sort()
	print('Sorted: ', arr)