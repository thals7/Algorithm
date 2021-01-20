# 참고: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue: # queue가 비어있지 않은 동안
        n = queue.pop(0)
        if n not in visited:
            visited.add(n)
            queue.extend(graph[n] - visited)
    return visited


print(bfs(graph,'A'))