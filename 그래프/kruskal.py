'''
pseudo code
# 선택된 간선 0개에서 출발
A = 공집합
for each vertex:
    do 각각 집합 만듦(초기화)
edge of E 비용에 따라 오름차순으로 정렬
# 가장 최소 비용 간선 A에 추가
# 그 다음 최소 비용 간선 중 사이클 형성하지 않는 간선을 계속해서 A에 추가
for each Edge of E: (비용 오름차순 edge대로 for문 돌아감)
    do if v와 u가 속한 집합이 다르면 (사이클 형성 유무를 union-find로 찾음)
            집합 A에 edge(v,u) 추가
            v,u 속한 두 집합 하나로 합침 (union func)
end.
'''


class unionFind:
    def __init__(self,size):
        self.parent = [i for i in range(size)]
        self.rank = [0 for i in range(size)] # 트리의 높이

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, root1, root2):
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                if self.rank[root1] == self.rank[root2]:
                    self.rank[root2] += 1

def kruskal(n, data): # n은 정점의 개수, edge([])에는 [a,b,c]의 형태로 a와 b를 잇는 간선의 가중치 c를 입력
    mst = []
    disjointSet = unionFind(n)
    edgeList = sorted(data, key=lambda weight: weight[2])
    for edge in edgeList:
        v, u, weight = edge
        root1 = disjointSet.find(v)
        root2 = disjointSet.find(u)
        if root1 != root2:
            disjointSet.union(root1,root2)
            mst.append(edge)
    return mst