class priorityQueue:
    def __init__(self):
        self.size = 0
        self.heap = []

    def Heap(self):
        return self.heap

    def maxHeapify(self,index): # index는 heapify 해야하는 노드의 배열 인덱스
        largest = index
        left = index*2+1
        right = index*2+2
        if left < self.size and self.heap[largest] < self.heap[left]:
            largest = left
        if right < self.size and self.heap[largest] < self.heap[right]:
            largest = right
        # 위쪽 노드가 왼쪽이나 오른쪽 자식 노드보다 작을때 (largest가 교체된 상태)
        if largest != index:
            # 해당 배열 인덱스의 값을 교체 (위쪽 노드 자리에 둘 중 큰 자식의 값을, 큰 자식이 있던 자리에는 heapify 해야하는 노드값으로 교체)
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.maxHeapify(largest) # 값이 제자리를 찾을때까지 재귀를 통해 heapify 해줌

    # 노드를 이진힙의 맨 끝에 삽입한 뒤 heapify 수행
    def insert(self, val):
        if self.size == 0: # 빈 트리인 경우
            self.heap.append(val)
            self.size += 1
        else:
            self.heap.append(val)
            self.size += 1
            # 맨 끝 노드(새롭게 추가된 노드)의 부모노드 인덱스부터 시작해서
            # 루트 노드의 인덱스(0), 즉 -1까지 1씩 줄여가면서(트리의 위로 올라가면서) heapify
            for i in range(self.size//2-1, -1, -1):
                self.maxHeapify(i)

    # 최대값 삭제 후 반환
    # 루트 노드(최대값) 삭제한 뒤 루트 노드 자리에 트리의 맨 끝값을 넣고 heapify 실행
    def extractMax(self):
        if self.size >= 1:
            maxVal = self.heap[0]
            self.heap[0] = self.heap[self.size-1]
            del self.heap[self.size-1]
            self.size -= 1
            self.maxHeapify(0)
            return maxVal


# practice
Q = priorityQueue()
Q.insert(5)
Q.insert(11)
Q.insert(2)
Q.insert(8)
Q.insert(7)
print(Q.size) # 5
print(Q.Heap()) # [11,8,2,5,7]
print(Q.extractMax()) # 11
print(Q.Heap()) # [8,7,2,5]
print(Q.extractMax()) # 8