def dfs(graph, node, visited=None):

    if visited is None:
        visited = set()

    if node not in visited:

        print(node, end=" ")

        visited.add(node)

        for neighbour in graph[node]:

            dfs(graph, neighbour, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}


print("DFS Traversal:")

dfs(graph, 'A')