# 참고: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# 원소와 연결된 원소들의 set을 대응시킨 dict로 표현
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack: # stack이 비어있지 않은 동안
        n = stack.pop()
        if n not in visited:
            visited.add(n)
            stack.extend(graph[n] - visited)
    return visited


print(dfs(graph,'A'))