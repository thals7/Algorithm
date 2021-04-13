# 1
def partition(list, start, end):
    pivot = list[end]
    i = start # index of smaller element
    for j in range(start, end): # j = index of current element
        if list[j] <= pivot:
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i], list[end] = list[end], list[i] # pivot의 위치를 i+1(작은값과 큰 값 사이)로 옮김
    return i

def quickSort(list, start, end):
    if start < end:
        pivot = partition(list, start, end)
        quickSort(list, start, pivot-1)
        quickSort(list, pivot+1, end)
    return list

lst = [int(i) for i in input().split()]
print(quickSort(lst, 0, len(lst)-1))



# 2
def quicksort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list)//2]
    left, right, same = [], [], []
    for i in list:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            same.append(i)
    return quicksort(left) + same + quicksort(right)



