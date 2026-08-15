from collections import deque


def water_jug_bfs(jug1_capacity, jug2_capacity, target):

    start = (0, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:

        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        path = path + [(a, b)]

        # Goal
        if a == target or b == target:
            return path

        states = [
            # Fill Jug 1
            (jug1_capacity, b),

            # Fill Jug 2
            (a, jug2_capacity),

            # Empty Jug 1
            (0, b),

            # Empty Jug 2
            (a, 0),

            # Pour Jug 1 -> Jug 2
            (
                a - min(a, jug2_capacity - b),
                b + min(a, jug2_capacity - b)
            ),

            # Pour Jug 2 -> Jug 1
            (
                a + min(b, jug1_capacity - a),
                b - min(b, jug1_capacity - a)
            )
        ]

        for state in states:

            if state not in visited:
                queue.append((state, path))

    return None


# 4 litre jug, 5 litre jug, target = 2 litres
path = water_jug_bfs(4, 5, 2)

print("Solution:")

for state in path:
    print(state)