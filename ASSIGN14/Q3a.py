from itertools import combinations

# resolution by refutation

def negate(lit):
    if lit.startswith("~"):
        return lit[1:]
    return "~" + lit


def resolve(ci, cj):

    resolvents = set()

    for lit in ci:
        if negate(lit) in cj:
            new_clause = (ci - {lit}) | (cj - {negate(lit)})
            resolvents.add(frozenset(new_clause))

    return resolvents


def resolution(kb_clauses, query):

    clauses = set(kb_clauses)
    clauses.add(frozenset({negate(query)}))

    print("\nInitial CNF Clauses:")
    for c in clauses:
        print(set(c))

    while True:
        new = set()

        pairs = list(combinations(clauses, 2))

        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)

            if frozenset() in resolvents:
                print("\nDerived Empty Clause {}")
                return True

            new = new.union(resolvents)

        if new.issubset(clauses):
            return False

        clauses = clauses.union(new)

        print("\nNew Clauses Added:")
        for c in new:
            print(set(c))



kb= {
    frozenset({"P", "Q"}),
    frozenset({"~P", "R"}),
    frozenset({"~Q", "S"}),
    frozenset({"~R", "S"})
}

print("3(a) RESOLUTION")
result = resolution(kb, "S")
print("Conclusion S:", result)
