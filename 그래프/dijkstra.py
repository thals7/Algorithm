'''
pseudo code
Dijkstra(G,w,s)
  # 초기화
  for each u∈V do
   d[u] <- ∞
   π[u] <- NIL
  S <- ∅
  d[s] <- 0

  #  집합 S에 모든 정점들이 포함될 때까지 n-1번 반복
  while |S|<n do
    # 최소값 찾기
    find u∉S with the minimum d[u] value
    S <- S ∪ {u}
    for each u∉S with the adjacent to u
      # RELAXATION
      if d[v] > d[u]+w(u,v):
       d[v] = d[u]+w(u,v)
       π[v] <- u
'''
import heapq
# 그래프는 {출발:(도착,가중치)} 형태의 인접리스트
# graph = {i:set() for i in range(1,n+1)}

# example
graph = {
    1: {(3, 3), (2, 2)},
    2: {(4, 5), (3, 4)},
    3: {(4, 6)},
    4: set(),
    5: {(1, 1)}}

def dijkstra(graph,start):
    distance = {i:float('inf') for i in graph}
    distance[start] = 0
    Q = [] # 우선순위 큐 생성
    heapq.heappush(Q, [distance[start],start]) # 우선순위 큐에 최초 [d(u),u] 삽입

    while Q:
        # 거리 최소인 노드 선택
        d, u = heapq.heappop(Q)
        for v, w in graph[u]:
            # RELAXATION
            if distance[v] > d + w:
                distance[v] = d + w
                # u의 인접 노드 v를 큐에 삽입
                heapq.heappush(Q, [distance[v],v])

    return distance

print(dijkstra(graph,1))