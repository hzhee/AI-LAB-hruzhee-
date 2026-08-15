def alpha_beta(depth, node, maximizing_player, values, alpha, beta):

    # Leaf node
    if depth == 3:
        return values[node]

    if maximizing_player:

        best = float('-inf')

        for i in range(2):

            value = alpha_beta(
                depth + 1,
                node * 2 + i,
                False,
                values,
                alpha,
                beta
            )

            best = max(best, value)

            alpha = max(alpha, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best

    else:

        best = float('inf')

        for i in range(2):

            value = alpha_beta(
                depth + 1,
                node * 2 + i,
                True,
                values,
                alpha,
                beta
            )

            best = min(best, value)

            beta = min(beta, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]


# Start Alpha-Beta
result = alpha_beta(
    0,
    0,
    True,
    values,
    float('-inf'),
    float('inf')
)


print("Alpha-Beta Best Value:", result)