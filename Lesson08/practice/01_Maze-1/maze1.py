# Выверите и скопируйте сюда наиболее подходяший алгоритм для работы с графом(bfs/dfs)
def dfs(graph: list[list], start_vertex: int) -> list[bool]:
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    visited = [False] * len(graph)
    _dfs(start_vertex)
    return visited


# Опишите список смежности по изображению лабиринта из файла task.md
graph = [
    [1],  # 0
    [0, 4],  # 1
    [5],  # 2
    [4, 6],  # 3
    [1, 3, 5],  # 4
    [2, 4],  # 5
    [3],  # 6
    [8],  # 7
    [7],  # 8
]
home = 0
bank = 5
# Решите задачу и выведите ответ в нужном формате

visited = dfs(graph, home)

if visited[bank]:
    print("Сan go to the bank")
else:
    print("Сan't go to the bank")