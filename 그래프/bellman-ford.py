'''
pseudo code

RELAX(u,v)
# 기존의 경로보다 더 나은 경로를 찾은 경우
  if d[v]>d[u]+w(u,v)
# 새로운 경로로 업데이트
    then d[v] <- d[u]+w(u,v)
      π[v] <- u

BELLMAN-FORD(G,s)
  for each vertex V in G
    d[v] <- infinite
      π[v] <- NULL
  d[s] <- 0

  for each vertex V in G
    for each edge (u,v) in G
    # Relax 수행
      if d[v] > d[u] + w(u,v)
        then d[v] <- d[u] + w(u,v)
        π[v] <- u

# 음수 가중치가 존재하는지 확인
# 최단 경로를 찾았음에도 불구하고 여전히 Relax가 가능하다면 이는 음수 사이클이 존재한다는 의미 (즉 최단경로 존재하지 않음)
  for each edge (u,v) in G
    if d[v] > d[u] + w(u,v)
      return False
  return True
'''

# 그래프는 {출발:(도착,가중치)} 형태의 인접리스트로 구현
# graph = {i:set() for i in range(1, n + 1)}
graph = {1: {(2, 4), (3, 3)}, 2: {(3, -1)}, 3: {(1, -2)}}


def bellmanFord(graph,start):
    distance = {}
    pi = {}
    for vertex in graph:
        distance[vertex] = float('inf')
        pi[vertex] = None
    distance[start] = 0

    for _ in range(len(graph)):
        # 그래프가 출발:(도착, 가중치) 형태로 되어있으므로 v가 최종 목적지, u가 목적지와 인접한 정점이라고 했을 때 그래프의 출발 노드가 인접 정점(u)가 되고 도착 노드가 최종 목적지(v)가 됨
        for u in graph:
            # RELAXATION
            for v,w in graph[u]:
                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    pi[v] = u
                    
    # negative cycle 존재하는지 검사                
    for u in graph:
        for v,w in graph[u]:
            if distance[v] > distance[u] + w:
                print("Negative cycle exists")
                return

    return distance

print(bellmanFord(graph,1))