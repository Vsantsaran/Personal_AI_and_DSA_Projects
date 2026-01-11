# this program is about binary search

def binary_search(arr, val):
    n = len(arr)
    mid = n // 2
    if n == 1:
        if val == arr[mid]:
            return mid
        else:
            print('Not found.')
            exit(1)
    if val == arr[mid]:
        return mid
    if val < arr[mid]:
        return binary_search(arr[:mid], val)
    else:
        return mid + binary_search(arr[mid:], val)

if __name__ == '__main__':
    arr = [-8, -1, 0, 1, 37, 89, 89, 123, 128, 210, 2001]
    print('Array: ', arr)
    s_val = int(input('Enter search value: '))
    i = binary_search(arr, s_val)
    print(f'Found at {i}')
