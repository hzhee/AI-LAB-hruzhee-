from queue import PriorityQueue


def a_star(graph, start, goal, heuristic):

    open_list = PriorityQueue()

    open_list.put((0, start))

    came_from = {}

    g_score = {
        node: float('inf')
        for node in graph
    }

    g_score[start] = 0

    while not open_list.empty():

        current_f, current = open_list.get()

        if current == goal:

            path = []

            while current in came_from:

                path.append(current)

                current = came_from[current]

            path.append(start)

            return path[::-1]

        for neighbour, cost in graph[current]:

            new_g = g_score[current] + cost

            if new_g < g_score[neighbour]:

                came_from[neighbour] = current

                g_score[neighbour] = new_g

                f_score = new_g + heuristic[neighbour]

                open_list.put(
                    (f_score, neighbour)
                )

    return None


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('D', 3)],
    'D': [('G', 1)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}


heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 3,
    'E': 4,
    'F': 2,
    'G': 0
}


path = a_star(
    graph,
    'A',
    'G',
    heuristic
)


print("A* Shortest Path:", path)