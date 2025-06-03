def dfs(graph: list[list], start_vertex: int) -> list[bool]:
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    visited = [False] * len(graph)
    _dfs(start_vertex)
    return visited


def bfs(graph: list[list], start_vertex: int) -> list[int | None]:
    lengths = [None] * len(graph)
    lengths[start_vertex] = 0
    queue = [start_vertex]
    while queue:
        cur_vertex = queue.pop(0)
        for vertex in graph[cur_vertex]:
            if lengths[vertex] is None:
                lengths[vertex] = lengths[cur_vertex] + 1
                queue.append(vertex)
    return lengths


graph = [
    # список смежности
    [1, 3],  # 0
    [0, 3, 4, 5],  # 1
    [4, 5],  # 2
    [0, 1, 5],  # 3
    [1, 2],  # 4
    [1, 2, 3],  # 5
    [7],  # 6
    [6]  # 7
]
start = 4


