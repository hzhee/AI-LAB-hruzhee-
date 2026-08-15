# Map Coloring using Backtracking


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}


colors = [
    'Red',
    'Green',
    'Blue'
]


solution = {}


def is_valid(region, color):

    for neighbour in graph[region]:

        if neighbour in solution:

            if solution[neighbour] == color:
                return False

    return True


def color_map(regions):

    # All regions colored
    if len(regions) == 0:
        return True

    region = regions[0]

    for color in colors:

        if is_valid(region, color):

            solution[region] = color

            if color_map(regions[1:]):
                return True

            # Backtrack
            del solution[region]

    return False


regions = list(graph.keys())


if color_map(regions):

    print("Map Coloring Solution:")

    for region in solution:

        print(
            region,
            "->",
            solution[region]
        )

else:

    print("No solution found")