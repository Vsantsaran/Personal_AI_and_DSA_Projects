# zero sum triplets
# I have to find all 3-elements array whose sum is 0
from numpy import *
if __name__ == '__main__':
    trip = []
    arr = array([1, 8, -1, 0, 9, 7, -3, -2, -8, 5])
    for i in arr:
        for j in arr[1:]:
            for k in arr[2:]:
                if i+j+k == 0:
                    trip.append([i, j, k])
    new = []
    for i in trip:
        m = sorted(i)
        if m not in new:
            new.append(m)
    print(new)