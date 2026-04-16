from collections import deque

teams = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']

conflicts = {
    'P1': ['P2', 'P3', 'P6'],
    'P2': ['P1', 'P3', 'P4'],
    'P3': ['P1', 'P2', 'P5'],
    'P4': ['P2', 'P6'],
    'P5': ['P3', 'P6'],
    'P6': ['P1', 'P4', 'P5']
}

def make_domains():
    return {t: {'R1', 'R2', 'R3'} for t in teams}

def revise(domains, xi, xj):
    removed = False
    for room in set(domains[xi]):
        # check if there's any valid room for xj that's different
        if all(room == r for r in domains[xj]):
            domains[xi].remove(room)
            removed = True
    return removed

def ac3(domains, trace_limit=5):
    queue = deque()
    for t in teams:
        for neighbor in conflicts[t]:
            queue.append((t, neighbor))

    trace_count = 0
    print("\n--- AC-3 Trace ---")

    while queue:
        xi, xj = queue.popleft()

        changed = revise(domains, xi, xj)

        if trace_count < trace_limit:
            if changed:
                print(f"Arc ({xi},{xj}) checked -> domain of {xi} reduced to {domains[xi]}")
            else:
                print(f"Arc ({xi},{xj}) checked, no change")
            trace_count += 1

        if len(domains[xi]) == 0:
            print(f"\nFailure! domain of {xi} is empty.")
            return False

        if changed:
            for neighbor in conflicts[xi]:
                if neighbor != xj:
                    queue.append((neighbor, xi))

    return True

print("=== Part 1: AC-3 without any assignment ===")
domains = make_domains()
print("Initial domains:", {t: domains[t] for t in teams})

result = ac3(domains)

print("\nFinal domains:")
for t in teams:
    print(f"  {t}: {domains[t]}")

if result:
    print("\nProblem is arc-consistent.")
else:
    print("\nNot arc-consistent.")


print("\n=== Part 2: P1 assigned to R1, then AC-3 ===")
domains2 = make_domains()
domains2['P1'] = {'R1'}
print("Domains after assigning P1=R1:", {t: domains2[t] for t in teams})

# add arcs for p1's neighbors into queue manually by just running ac3
result2 = ac3(domains2)

print("\nFinal domains:")
for t in teams:
    print(f"  {t}: {domains2[t]}")

if result2:
    print("\nNo failure detected. Remaining domains are valid.")
else:
    print("\nAC-3 detected a failure!")