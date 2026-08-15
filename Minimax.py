def minimax(depth, node, maximizing_player, values):

    # If leaf node is reached
    if depth == 3:
        return values[node]

    if maximizing_player:

        best = float('-inf')

        # MAX player
        for i in range(2):

            value = minimax(
                depth + 1,
                node * 2 + i,
                False,
                values
            )

            best = max(best, value)

        return best

    else:

        best = float('inf')

        # MIN player
        for i in range(2):

            value = minimax(
                depth + 1,
                node * 2 + i,
                True,
                values
            )

            best = min(best, value)

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]


# Start Minimax
result = minimax(
    0,
    0,
    True,
    values
)


print("Minimax Best Value:", result)