# Сюда отправляем решение задачи "Лабиринт с дверьми"
# Подумайте, как можно моделировать двери, используя существующие алгоритмы работы с графами.

def dfs(graph: list[list], start_vertex: int) -> list[bool]:
    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    visited = [False] * len(graph)
    _dfs(start_vertex)
    return visited


# Решите задачу и выведите ответ в нужном формате
graph = [
    [1],  # 0
    [0, 5],  # 1
    [6],  # 2
    [7],  # 3
    [8, 5],  # 4
    [1],  # 5
    [2, 10],  # 6
    [3, 11],  # 7
    [4, 9, 12],  # 8
    [8, 10],  # 9
    [6, 9],  # 10
    [7, 15],  # 11
    [8],  # 12
    [],  # 13
    [],  # 14
    [11],  # 15
]

visited = dfs(graph, 1)
print(visited)
start_nodes = [5, 13, 3, 8]
key1 = 10
key2 = 7
# keys = [10, 7]
target = 0

lock1 = (4, 5)
lock2 = (14, 15)
# locks = [(4, 5), (14, 15)]

def unlock(graph, a, b):
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)


lock1_opened = False
lock2_opened = False

for start in start_nodes:
    visited = dfs(graph, start)
    if not lock1_opened and visited[key1]:
        unlock(graph, *lock1)
        lock1_opened = True
        print(f"  → Ключ key1 ({key1}) найден. Замок 1 {lock1} открыт.")

    if not lock2_opened and visited[key2]:
        unlock(graph, *lock2)
        lock2_opened = True
        print(f"  → Ключ key2 ({key2}) найден. Замок 2 {lock2} открыт.")

    if not visited[key1] and not visited[key2]:
        print(" Ключи не найдены из этой вершины.")

    if lock1_opened and lock2_opened:
        print("Оба замка открыты. Поиск ключей завершён.\n")

reachable = False
for start in start_nodes:
    visited = dfs(graph, start)
    if visited[target]:
        print(f"Цель ({target}) достижима из вершины {start}.")
        reachable = True

if not reachable:
    print(f"Цель ({target}) недостижима ни из одной стартовой вершины.")
