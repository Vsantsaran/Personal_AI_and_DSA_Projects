# This program will merge two sorted lists

final_list = []
def merge (lst_1, l1, lst_2, l2):
    i = j = 0
    while True:
        if i == l1 or j == l2:
            break
        if lst_1[i] == lst_2[j]:
            final_list.append(lst_1[i])
            i += 1
            j+= 1
            continue
        if lst_1[i] < lst_2[j]:
            final_list.append(lst_1[i])
            i += 1
        else:
            final_list.append(lst_2[j])
            j += 1
    if i is j:
        return
    if i == l1:
        final_list.extend(lst_2[j: ])
    else:
        final_list.extend(lst_1[i:])

lst_1 = [1, 5, 9, 12, 16, 29, 44, 45, 55, 90, 999]
lst_2 = [-9, -2, 0, 16, 29, 55, 91, 440]
l1 = len(lst_1)
l2 = len(lst_2)
print("Original list 1: ", lst_1)
print("Original list 2: ", lst_2)
merge(lst_1, l1, lst_2, l2)
print("Merged list: ", final_list)