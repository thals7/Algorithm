def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(i,len(list)-1):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list

lst = []
for i in input().split():
    lst.append(int(i))
print(bubbleSort(lst))