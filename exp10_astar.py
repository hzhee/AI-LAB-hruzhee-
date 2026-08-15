from queue import PriorityQueue


def a_star(graph, start, goal, heuristics):

    open_list = PriorityQueue()
    open_list.put((0, start))

    came_from = {}

    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while not open_list.empty():

        current = open_list.get()[1]

        # Check if goal is reached
        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)

            return path[::-1]

        # Explore neighbors
        for neighbor, cost in graph[current]:

            temp_g = g_score[current] + cost

            if temp_g < g_score[neighbor]:

                came_from[neighbor] = current
                g_score[neighbor] = temp_g

                f_score = temp_g + heuristics[neighbor]

                open_list.put((f_score, neighbor))

    return None


# Graph
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}


# Heuristic values
heuristics = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 4,
    'F': 2,
    'G': 0
}


# Find shortest path
path = a_star(graph, 'A', 'G', heuristics)

print("Shortest path found by A*:", path)
