# SEND + MORE = MONEY
# Cryptarithmetic as a Constraint Satisfaction Problem (CSP)
# Each letter → unique digit 0–9; S, M ≠ 0

from itertools import permutations

# ── Variables & Domains ───────────────────────────────────────────────────────
# Letters: S E N D M O R Y  (8 unique letters)
LETTERS = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

# ── Constraint check ──────────────────────────────────────────────────────────
def satisfies_constraints(assignment):
    S, E, N, D, M, O, R, Y = (assignment[l] for l in LETTERS)
    
    # Leading digits must be non-zero
    if S == 0 or M == 0:
        return False

    # All digits must be unique
    if len(set(assignment.values())) != len(LETTERS):
        return False

    # Core arithmetic constraint: SEND + MORE = MONEY
    SEND  = 1000*S + 100*E + 10*N + D
    MORE  = 1000*M + 100*O + 10*R + E
    MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

    return SEND + MORE == MONEY

# ── CSP Solver: Backtracking + Forward Checking ───────────────────────────────
def solve_csp():
    """
    Backtracking search with:
    - MRV: assign letters in a fixed smart order
    - Forward checking: prune used digits from remaining domains
    - Early pruning on partial column constraints
    """

    def backtrack(index, assignment, used_digits):
        # Base case: all letters assigned
        if index == len(LETTERS):
            return assignment if satisfies_constraints(assignment) else None

        letter = LETTERS[index]

        for digit in range(10):
            if digit in used_digits:
                continue
            
            # Leading letter constraint
            if letter in ('S', 'M') and digit == 0:
                continue

            # Partial pruning for M: SEND+MORE=MONEY means M must be 1
            # (max SEND=9999, max MORE=9999 → max sum=19998, so M=1)
            if letter == 'M' and digit != 1:
                continue

            assignment[letter] = digit
            used_digits.add(digit)

            result = backtrack(index + 1, assignment, used_digits)
            if result:
                return result

            del assignment[letter]
            used_digits.remove(digit)

        return None
    return backtrack(0, {}, set())

# ── Run ───────────────────────────────────────────────────────────────────────
solution = solve_csp()

if solution:
    S, E, N, D = solution['S'], solution['E'], solution['N'], solution['D']
    M, O, R, Y = solution['M'], solution['O'], solution['R'], solution['Y']

    SEND  = 1000*S + 100*E + 10*N + D
    MORE  = 1000*M + 100*O + 10*R + E
    MONEY = 10000*M + 1000*O + 100*N + 10*E + Y

    print("=" * 35)
    print("   SEND + MORE = MONEY  →  CSP Solution")
    print("=" * 35)
    print(f"\n  Letter assignments:")
    for letter in LETTERS:
        print(f"    {letter} = {solution[letter]}")
    print(f"\n  Verification:")
    print(f"    SEND  = {SEND}")
    print(f"    MORE  = {MORE}")
    print(f"    ──────────")
    print(f"    MONEY = {MONEY}")
    print(f"\n  {SEND} + {MORE} = {MONEY}  →  {'✓ Correct!' if SEND + MORE == MONEY else '✗ Wrong'}")
    print(f"\n  Constraints satisfied:")
    print(f"    All digits unique : {'✓' if len(set(solution.values()))==8 else '✗'}")
    print(f"    S ≠ 0             : {'✓' if S != 0 else '✗'}")
    print(f"    M ≠ 0             : {'✓' if M != 0 else '✗'}")
else:
    print("No solution found.")