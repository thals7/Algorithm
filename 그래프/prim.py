'''
pseudo code
  for each V[u]: 그래프 속한 모든 노드 u에 대해서
    key[u] = 무한대 u와 연결된 모든 에지의 가중치들 중 최소값을 무한대로 초기화
    π[u] = None key[u]를 가진 에지와 연결된 노드 None으로 초기화
  key[start] = 0 시작노드의 키값 0으로 설정
  Queue = graph 큐 생성
  while Queue != None 큐가 빌 때까지 while문 반복
    u = EXTRACT-MIN(Queue) Queue에서 key값 최소인 노드를 뽑아냄
        for each v = adj[u] u의 모든 인접 노드 v에 대해서
      if v가 Q에 들어있고 w(u,v)가 현재 key[v]보다 작으면
        π[v] = u v의 π값 갱신
        key[v] = w(u,v) 우선순위 큐에서 key값 DECREASE
'''


import sys, heapq

input = lambda: sys.stdin.readline().rstrip()

n,e = map(int,input().split()) # n: 정점의 개수 e: 에지의 개수

# 인접 리스트로 그래프 구현
graph = {i:dict() for i in range(1,n+1)}
for _ in range(e):
    i,j,w = map(int,input().split()) # i,j : 연결된 정점 w : 정점을 잇는 에지의 가중치
    graph[i][j] = w
    graph[j][i] = w


def prim(graph, start):
    key = [dict()]
    pi = {}
    total_weight = 0

    # 초기화
    for v in graph.keys():
        key[v] = float('inf')
        pi[v] = None
    key[start] = 0

    while key:
        node = heapq.heappop(key)[0]
        total_weight += node
        for adj, weight in graph[node].items():
            if adj in key and weight < key[adj]:
                key[adj] = weight
                pi[adj] = node
    return total_weight

print(prim(graph,1))