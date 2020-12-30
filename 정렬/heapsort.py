import random

def heapify(list, index, size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    # left와 right 둘 중 더 큰 숫자의 index 찾음
    if left < size and list[left] > list[largest]:
        largest = left
    if right < size and list[right] > list[largest]:
        largest = right
    if largest != index: # largest가 left나 right로 바뀌었을때
        list[largest], list[index] = list[index], list[largest] # 부모 노드와 더 큰 자식 노드의 값을 교환
        heapify(list, largest, size) # 재귀를 통해 밑의 노드들도 heapify해줌

def heap_sort(list):
    n = len(list)
    for i in range(n//2-1, -1, -1): # n//2에 -1을 하는 이유는 배열의 첫번쩨 index가 0부터 시작하므로 / end가 -1이므로 -1 앞(0)까지 탐색
        heapify(list, i, n) # 주어진 데이터로 힙을 만듦
    for i in range(n-1, 0, -1):
        list[0], list[i] = list[i], list[0] # 힙의 최대값(루트)를 가장 마지막 값과 교환
        heapify(list, 0, i) # 루트 노드에 대해서 heapify
        # for문이 한 번 돌 때마다 힙의 크기는 1씩 줄어듦(가장 마지막 값은 힙의 일부가 아닌 것으로 간주)
    return list

lst = [random.randint(1,20) for i in range(20)]
print(lst)
print(heap_sort(lst))