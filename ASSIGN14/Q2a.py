from itertools import combinations

# backward chaining


def backwardchain(goal, facts, rules, visited=None):

    if visited is None:
        visited = set()

    print("Trying to prove:", goal)

    if goal in facts:
        print(goal, "is a fact.")
        return True

    if goal in visited:
        return False

    visited.add(goal)

    if goal not in rules:
        return False

    for premises in rules[goal]:
        print(f"Checking Rule: {premises} -> {goal}")

        all_true = True
        for p in premises:
            if not backwardchain(p, facts, rules, visited):
                all_true = False
                break

        if all_true:
            return True

    return False

facts= {"A", "B"}

rules = {
    "Q": [["P"], ["R"]],
    "P": [["A"]],
    "R": [["B"]]
}

print("2(a) BACKWARD CHAINING")
result = backwardchain("Q", facts, rules)
print("Conclusion Q:", result)

