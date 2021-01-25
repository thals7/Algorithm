class unionFind:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for i in range(size)] # 트리의 높이

    # 부모 노드를 타고 올라가 자신이 속한 트리의 루트 노드를 찾는 함수
    # Path Compression 최적화
    def find(self, v):
        if self.parent[v] != v: # 자기 자신이 루트 노드가 아닌 경우(아직 루트노드를 찾지 못한 경우)
            self.parent[v] = self.find(self.parent[v]) # 부모 노드에 대한 재귀 함수를 호출하여 위로 올라가며 만나는 모든 노드의 부모 노드를 최종적으로 루트 노드로 바꿔줌
        return self.parent[v]


    # 두 노드가 속한 각각의 트리 중 작은 트리를 큰 트리로 흡수시킴 (작은 트리의 루트 노드의 부모 노드를 큰 트리의 루트 노드로 변경)
    # 이 때 트리의 크기는 self.rank(트리의 높이)를 이용
    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2: # v1과 v2가 각각 다른 트리에 속해있을때
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]: # 트리의 높이가 같은 경우였다면
                    self.rank[root2] += 1 # root2의 랭크 +1 해줌


