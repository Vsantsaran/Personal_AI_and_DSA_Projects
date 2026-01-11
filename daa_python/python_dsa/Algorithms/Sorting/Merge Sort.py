# Merge Sort algorithm

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        l1 = len(left)
        l2 = len(right)
        while i != l1 and j != l2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while j < l2:
            arr[k] = right[j]
            j += 1
            k += 1
        while i < l1:
            arr[k] = left[i]
            i += 1
            k += 1

if __name__ == '__main__':
    arr = [12, 87, 87, -9, -9, -34, 60, 0, 90, 66, 1, -1, 9]
    print(f"Original array: {arr}")
    merge_sort (arr)
    print(f"Sorted array: {arr}")