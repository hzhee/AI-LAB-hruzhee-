from collections import deque


def valid_state(m, c):

    # Left side
    if m > 0 and m < c:
        return False

    # Right side
    right_m = 3 - m
    right_c = 3 - c

    if right_m > 0 and right_m < right_c:
        return False

    return True


def get_successors(state):

    m, c, boat = state

    moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1)
    ]

    successors = []

    for dm, dc in moves:

        if boat == 1:
            new_m = m - dm
            new_c = c - dc
            new_boat = 0

        else:
            new_m = m + dm
            new_c = c + dc
            new_boat = 1

        if 0 <= new_m <= 3 and 0 <= new_c <= 3:

            if valid_state(new_m, new_c):

                successors.append(
                    (new_m, new_c, new_boat)
                )

    return successors


def bfs():

    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:

        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)

        path = path + [state]

        if state == goal:
            return path

        for next_state in get_successors(state):

            if next_state not in visited:
                queue.append((next_state, path))

    return None


solution = bfs()

print("Solution:")

for state in solution:

    m, c, boat = state

    side = "Left" if boat == 1 else "Right"

    print(
        "Missionaries:", m,
        "Cannibals:", c,
        "Boat:", side
    )