# District adjacency graph (only actual Gujarat districts)
adjacency = {
    'Kuchchh':        ['Jamnagar', 'Rajkot', 'Surendranagar', 'Patan', 'Banaskantha'],
    'Jamnagar':       ['Kuchchh', 'Rajkot', 'Porbandar'],
    'Rajkot':         ['Jamnagar', 'Kuchchh', 'Surendranagar', 'Morbi',
                       'Porbandar', 'Junaghad', 'Amreli'],
    'Porbandar':      ['Jamnagar', 'Rajkot', 'Junaghad'],
    'Junaghad':       ['Porbandar', 'Rajkot', 'Amreli', 'Gir_Somnath'],
    'Gir_Somnath':    ['Junaghad', 'Amreli'],
    'Amreli':         ['Rajkot', 'Junaghad', 'Gir_Somnath', 'Bhavnagar', 'Botad'],
    'Morbi':          ['Rajkot', 'Surendranagar', 'Kuchchh'],
    'Surendranagar':  ['Kuchchh', 'Rajkot', 'Morbi', 'Patan', 'Ahmedabad',
                       'Anand', 'Botad', 'Bhavnagar'],
    'Patan':          ['Kuchchh', 'Surendranagar', 'Banaskantha', 'Mehsana'],
    'Banaskantha':    ['Kuchchh', 'Patan', 'Mehsana', 'Sabarkantha'],
    'Mehsana':        ['Patan', 'Banaskantha', 'Sabarkantha', 'Gandhinagar', 'Ahmedabad'],
    'Sabarkantha':    ['Banaskantha', 'Mehsana', 'Gandhinagar', 'Kheda', 'Aravalli'],
    'Aravalli':       ['Sabarkantha', 'Mahisagar', 'Panchmahal'],
    'Gandhinagar':    ['Mehsana', 'Sabarkantha', 'Ahmedabad'],
    'Ahmedabad':      ['Surendranagar', 'Mehsana', 'Gandhinagar', 'Anand',
                       'Kheda', 'Botad'],
    'Anand':          ['Surendranagar', 'Ahmedabad', 'Kheda', 'Vadodara', 'Botad'],
    'Kheda':          ['Sabarkantha', 'Ahmedabad', 'Anand', 'Vadodara', 'Mahisagar'],
    'Botad':          ['Surendranagar', 'Amreli', 'Ahmedabad', 'Anand', 'Bhavnagar'],
    'Bhavnagar':      ['Amreli', 'Surendranagar', 'Botad', 'Anand'],
    'Mahisagar':      ['Sabarkantha', 'Aravalli', 'Panchmahal', 'Vadodara', 'Kheda'],
    'Vadodara':       ['Anand', 'Kheda', 'Mahisagar', 'Panchmahal',
                       'Chhota_Udaipur', 'Narmada'],
    'Panchmahal':     ['Aravalli', 'Mahisagar', 'Vadodara', 'Dahod',
                       'Chhota_Udaipur'],
    'Dahod':          ['Panchmahal', 'Chhota_Udaipur'],
    'Chhota_Udaipur': ['Vadodara', 'Panchmahal', 'Dahod', 'Narmada'],
    'Narmada':        ['Vadodara', 'Chhota_Udaipur', 'Bharuch', 'Surat'],
    'Bharuch':        ['Narmada', 'Surat', 'Vadodara'],
    'Surat':          ['Narmada', 'Bharuch', 'Navsari', 'Tapi', 'Dangs'],
    'Tapi':           ['Surat', 'Navsari', 'Dangs', 'Narmada'],
    'Navsari':        ['Surat', 'Tapi', 'Valsad', 'Dangs'],
    'Dangs':          ['Surat', 'Tapi', 'Navsari'],
    'Valsad':         ['Navsari'],
}

COLOR_NAMES = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple']

# ─────────────────────────────────────────────
#  Logging helpers
# ─────────────────────────────────────────────

step_counter = [0]   # mutable so nested functions can increment it

def indent(depth):
    return ""

def log_try(depth, district, color):
    step_counter[0] += 1
    print(f"{indent(depth)}[Step {step_counter[0]}] Try {district!r:<22} = {COLOR_NAMES[color]}")

def log_conflict(depth, district, color, conflicting_nb):
    print(f"✗ CONFLICT: {district!r} = {COLOR_NAMES[color]} "
          f"clashes with neighbor {conflicting_nb!r} (already {COLOR_NAMES[color]})")

def log_dead_end(depth, district, color):
    print(f"✗ DEAD-END (forward check): assigning {COLOR_NAMES[color]} to "
          f"{district!r} would empty a neighbor's domain")

def log_failure(depth, district):
    print(f"FAILURE: no color works for {district!r} — backtracking ↩")

def log_assign(depth, district, color):
    print(f"✔ Assigned {district!r} = {COLOR_NAMES[color]}")

def log_undo(depth, district, color):
    print(f"↩ Undo {district!r} = {COLOR_NAMES[color]} (child failed)")

def log_solution(assignment):
    print("\n" + "═" * 50)
    print("  SOLUTION FOUND")
    print("═" * 50)
    print(f"  {'District':<22}  Color")
    print("  " + "─" * 35)
    for district, color in sorted(assignment.items()):
        print(f"  {district:<22}  {COLOR_NAMES[color]}")

# ─────────────────────────────────────────────
#  CSP core (same logic, verbose output added)
# ─────────────────────────────────────────────

def is_valid(district, color, assignment):
    for nb in adjacency[district]:
        if assignment.get(nb) == color:
            return False, nb          # return the offending neighbor for logging
    return True, None

def select_unassigned(assignment, domains):
    unassigned = [d for d in adjacency if d not in assignment]
    return min(unassigned, key=lambda d: len(domains[d]))

def forward_check(district, color, domains):
    new_domains = {d: set(v) for d, v in domains.items()}
    for nb in adjacency[district]:
        new_domains[nb].discard(color)
        if not new_domains[nb]:
            return None
    return new_domains

def backtrack(assignment, domains, num_colors, depth=0):
    # Base case: every district assigned → solution
    if len(assignment) == len(adjacency):
        log_solution(assignment)
        return assignment

    district = select_unassigned(assignment, domains)
    print(f"\n{indent(depth)}Assign district: {district!r}  "
          f"(domain: {[COLOR_NAMES[c] for c in sorted(domains[district])]})")

    for color in range(num_colors):
        if color not in domains[district]:
            continue                  # already pruned by forward checking

        log_try(depth, district, color)

        # ── Constraint check ──────────────────────────────────────────
        valid, conflicting_nb = is_valid(district, color, assignment)
        if not valid:
            log_conflict(depth, district, color, conflicting_nb)
            continue

        # ── Forward checking ──────────────────────────────────────────
        new_domains = forward_check(district, color, domains)
        if new_domains is None:
            log_dead_end(depth, district, color)
            continue

        # ── Commit ────────────────────────────────────────────────────
        log_assign(depth, district, color)
        assignment[district] = color

        result = backtrack(assignment, new_domains, num_colors, depth + 1)
        if result is not None:
            return result

        # ── Undo (child subtree failed) ───────────────────────────────
        log_undo(depth, district, color)
        del assignment[district]

    # No color worked → signal failure to parent
    log_failure(depth, district)
    return None

# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────

def solve_map_coloring():
    districts = list(adjacency.keys())
    for num_colors in range(2, len(districts) + 1):
        print("\n" + "═" * 50)
        print(f"  Trying with {num_colors} color(s): "
              f"{COLOR_NAMES[:num_colors]}")
        print("═" * 50)
        step_counter[0] = 0
        domains = {d: set(range(num_colors)) for d in districts}
        solution = backtrack({}, domains, num_colors)
        if solution:
            print(f"\n  Total steps taken: {step_counter[0]}")
            return solution, num_colors
        else:
            print(f"\n  ✗ No solution with {num_colors} color(s). "
                  f"Increasing color count...\n")
    return None, None

solve_map_coloring()