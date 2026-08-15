from collections import deque

goal = "123456780"

def get_moves(state):
    i = state.index("0")
    moves = []

    if i > 2:
        moves.append(i - 3)
    if i < 6:
        moves.append(i + 3)
    if i % 3 != 0:
        moves.append(i - 1)
    if i % 3 != 2:
        moves.append(i + 1)

    for j in moves:
        s = list(state)
        s[i], s[j] = s[j], s[i]
        yield "".join(s)


def bfs(start):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        for next_state in get_moves(state):
            queue.append((next_state, path + [state]))

    return None


start = "123406758"
path = bfs(start)

if path:
    for state in path:
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()
else:
    print("No solution")