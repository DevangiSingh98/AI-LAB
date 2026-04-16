from collections import deque

grid_str = "000006000059000008200008000045000000003000000006003050000007000000000000000500002"

# build initial domains
domains = {}
for i in range(81):
    r, c = i // 9, i % 9
    val = int(grid_str[i])
    if val != 0:
        domains[(r, c)] = {val}
    else:
        domains[(r, c)] = set(range(1, 10))

# generate all neighbors for a cell (same row, col, or 3x3 box)
def get_neighbors(r, c):
    neighbors = set()
    for j in range(9):
        if j != c:
            neighbors.add((r, j))
        if j != r:
            neighbors.add((j, c))
    br, bc = (r // 3) * 3, (c // 3) * 3
    for dr in range(3):
        for dc in range(3):
            nr, nc = br + dr, bc + dc
            if (nr, nc) != (r, c):
                neighbors.add((nr, nc))
    return neighbors

neighbors = {(r, c): get_neighbors(r, c) for r in range(9) for c in range(9)}

# generate all arcs
def get_arcs():
    arcs = []
    for r in range(9):
        for c in range(9):
            for nb in neighbors[(r, c)]:
                arcs.append(((r, c), nb))
    return arcs

def revise(domains, xi, xj):
    removed = False
    for val in set(domains[xi]):
        # val has no support in xj
        if all(val == v for v in domains[xj]):
            domains[xi].discard(val)
            removed = True
    return removed

def ac3(domains):
    queue = deque(get_arcs())
    total_removed = 0

    while queue:
        xi, xj = queue.popleft()
        if revise(domains, xi, xj):
            removed = 9 - len(domains[xi]) - (9 - len(domains[xi]))  # just track below
            if len(domains[xi]) == 0:
                return False, total_removed
            total_removed += 1
            for nb in neighbors[xi]:
                if nb != xj:
                    queue.append((nb, xi))

    return True, total_removed

# count total values before
before = sum(len(domains[k]) for k in domains)

ok, removed = ac3(domains)

after = sum(len(domains[k]) for k in domains)
actual_removed = before - after

print("=== AC-3 Sudoku ===\n")
print(f"Values before AC-3 : {before}")
print(f"Values after AC-3  : {after}")
print(f"Total values removed: {actual_removed}")

print("\n--- Domain size grid (1=solved, >1=unsolved) ---\n")
for r in range(9):
    row = ""
    for c in range(9):
        size = len(domains[(r, c)])
        row += str(size) + " "
    print(row)

print("\n--- Solved cells grid (. = unsolved) ---\n")
for r in range(9):
    row = ""
    for c in range(9):
        d = domains[(r, c)]
        if len(d) == 1:
            row += str(list(d)[0]) + " "
        else:
            row += ". "
    print(row)

solved = sum(1 for k in domains if len(domains[k]) == 1)
empty = sum(1 for k in domains if len(domains[k]) == 0)

print(f"\nSolved cells : {solved}/81")
print(f"Empty domains: {empty}")

if empty > 0:
    print("Result: AC-3 found a contradiction -> puzzle unsolvable")
elif solved == 81:
    print("Result: AC-3 solved the puzzle completely!")
else:
    print("Result: AC-3 reduced the search space but couldn't fully solve it.")
    print("        A backtracking algorithm would be needed next.")