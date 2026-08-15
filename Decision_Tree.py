# Decision Tree using Pure Python
# No external libraries required


# Dataset
# [Outlook, Temperature, Humidity, Windy, Play]
data = [
    ["Sunny", "Hot", "High", "False", "No"],
    ["Sunny", "Hot", "High", "True", "No"],
    ["Overcast", "Hot", "High", "False", "Yes"],
    ["Rain", "Mild", "High", "False", "Yes"],
    ["Rain", "Cool", "Normal", "False", "Yes"],
    ["Rain", "Cool", "Normal", "True", "No"],
    ["Overcast", "Cool", "Normal", "True", "Yes"],
    ["Sunny", "Mild", "High", "False", "No"],
    ["Sunny", "Cool", "Normal", "False", "Yes"],
    ["Rain", "Mild", "Normal", "False", "Yes"],
    ["Sunny", "Mild", "Normal", "True", "Yes"],
    ["Overcast", "Mild", "High", "True", "Yes"],
    ["Overcast", "Hot", "Normal", "False", "Yes"],
    ["Rain", "Mild", "High", "True", "No"]
]


def entropy(rows):

    total = len(rows)

    yes = sum(1 for row in rows if row[-1] == "Yes")
    no = total - yes

    if yes == 0 or no == 0:
        return 0

    import math

    p_yes = yes / total
    p_no = no / total

    return -(p_yes * math.log2(p_yes) +
             p_no * math.log2(p_no))


def information_gain(rows, column):

    total_entropy = entropy(rows)

    values = set(row[column] for row in rows)

    weighted_entropy = 0

    for value in values:

        subset = [
            row for row in rows
            if row[column] == value
        ]

        weight = len(subset) / len(rows)

        weighted_entropy += weight * entropy(subset)

    return total_entropy - weighted_entropy


def majority_class(rows):

    yes = sum(1 for row in rows if row[-1] == "Yes")
    no = len(rows) - yes

    return "Yes" if yes >= no else "No"


def build_tree(rows, features):

    # All rows have same class
    classes = set(row[-1] for row in rows)

    if len(classes) == 1:
        return rows[0][-1]

    # No features remaining
    if not features:
        return majority_class(rows)

    # Find best feature
    best_feature = max(
        features,
        key=lambda f: information_gain(rows, f)
    )

    tree = {
        "feature": best_feature,
        "branches": {}
    }

    values = set(row[best_feature] for row in rows)

    remaining_features = [
        f for f in features
        if f != best_feature
    ]

    for value in values:

        subset = [
            row for row in rows
            if row[best_feature] == value
        ]

        tree["branches"][value] = build_tree(
            subset,
            remaining_features
        )

    return tree


def print_tree(tree, level=0):

    if isinstance(tree, str):
        print("  " * level + "-> " + tree)
        return

    print(
        "  " * level +
        "Feature:",
        tree["feature"]
    )

    for value, branch in tree["branches"].items():

        print(
            "  " * (level + 1) +
            "Value:",
            value
        )

        print_tree(branch, level + 2)


# Features
features = [0, 1, 2, 3]

# Build Decision Tree
tree = build_tree(data, features)

print("Decision Tree")
print("=============")

print_tree(tree)