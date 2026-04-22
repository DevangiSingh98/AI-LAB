from itertools import combinations


# forward chaining


def forwardchain(facts, rules, goal):

    inferred = set(facts)

    print("\nInitial Facts:", inferred)

    changed = True
    while changed:
        changed = False

        for premises, conclusion in rules:
            if premises.issubset(inferred) and conclusion not in inferred:
                print(f"Rule Applied: {set(premises)} -> {conclusion}")
                inferred.add(conclusion)
                changed = True

                if goal in inferred:
                    print("Goal Derived:", goal)
                    return True

    return goal in inferred

facts = {"A", "B", "M"}

rules= [
    ({"P"}, "Q"),
    ({"L", "M"}, "P"),
    ({"A", "B"}, "L")
]


print("1(a) FORWARD CHAINING")
result = forwardchain(facts, rules, "Q")
print("Conclusion Q:", result)
