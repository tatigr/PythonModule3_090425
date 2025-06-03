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
    [4],  # 3
    [1, 3, 7],  # 4
    [2],  # 5
    [],  # 6
    [4, 8],  # 7
    [7],  # 8
]
objects = {
    "bank": 3,
    "shop": 5,
    "bar": 8,
    "hospital": 7,
}
home = 1
# Решите задачу и выведите ответ в нужном формате

visited = dfs(graph, home)

for name, vertex in objects.items():
    if visited[vertex]:
        print(f"Сan go to the {name}")
    else:
        print(f"Сan't go to the {name}")
