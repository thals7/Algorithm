def selectionSort(list):
    length = len(list)
    for i in range(length-1,0,-1):
        Max = i
        for j in range(0,i-1):
            if list[j] > list[Max]:
                Max = j
        list[i], list[Max] = list[Max], list[i]
    return list

lst = []
for i in input().split():
    lst.append(int(i))
print(selectionSort(lst))