from itertools import permutations


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


def tsp(matrix):

    n = len(matrix)

    minimum_cost = float('inf')
    best_route = None

    # Start from city 0
    for route in permutations(range(1, n)):

        current_city = 0
        cost = 0

        for city in route:

            cost += matrix[current_city][city]

            current_city = city

        # Return to starting city
        cost += matrix[current_city][0]

        if cost < minimum_cost:

            minimum_cost = cost

            best_route = (0,) + route + (0,)

    print("Best Route:", best_route)
    print("Minimum Cost:", minimum_cost)


tsp(distance_matrix)