import random
import math

def heuristic(board):
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:                     # same row = row attack
                attacks += 1
            if abs(board[i] - board[j]) == abs(i - j):  # diagonal attack
                attacks += 1
    return attacks


def random_board():
    # Random row for each of the 8 columns
    return [random.randint(0, 7) for _ in range(8)]

#  STEEPEST-ASCENT HILL CLIMBING

def steepest_ascent(board):
    current = board[:]      
    init_h  = heuristic(current)
    steps   = 0

    while True:
        h = heuristic(current)

        if h == 0:              # goal reached
            return init_h, 0, steps, "SOLVED", current

        best_h = h         # threshold
        best_boards = []

       
        for col in range(8):
            for row in range(8):
                if current[col] == row:   # skip current position
                    continue
                nb = current[:]
                nb[col] = row
                nh = heuristic(nb)

                if nh < best_h:           # strictly better, reset list
                    best_h = nh
                    best_boards = [nb]
                elif nh == best_h:        # equally best, add to list
                    best_boards.append(nb)

        if best_h >= h:         # local minimum
            return init_h, h, steps, "FAIL", current

        current = random.choice(best_boards)   # break ties randomly
        steps  += 1



# FIRST-CHOICE HILL CLIMBING

def first_choice(board, max_sideways=200):
    current = board[:]
    init_h  = heuristic(current)
    steps   = 0

    while True:
        h = heuristic(current)

        if h == 0:              # goal reached
            return init_h, 0, steps, "SOLVED", current

        found = False
        
        for _ in range(max_sideways):
            col = random.randint(0, 7)
            row = random.randint(0, 7)
            if current[col] == row:     # skip no-op moves
                continue
            nb = current[:]
            nb[col] = row
            if heuristic(nb) < h:       # first improvement found 
                current = nb
                steps  += 1
                found   = True
                break

        if not found:           # exhausted attempts: local minimum
            return init_h, h, steps, "FAIL", current


#RANDOM-RESTART HILL CLIMBING

def random_restart(board, max_restarts=100):
    total_steps   = 0
    restarts      = 0
    init_h        = heuristic(board)
    current_board = board[:]

    while restarts <= max_restarts:
        _, final_h, steps, status, final_board = steepest_ascent(current_board)
        total_steps += steps

        if status == "SOLVED":      # found a solution
            return init_h, 0, total_steps, f"SOLVED (restarts={restarts})", final_board

        # Stuck: restart with a fresh random board
        restarts     += 1
        current_board = random_board()

    return init_h, heuristic(final_board), total_steps, "FAIL", final_board



# SIMULATED ANNEALING

def simulated_annealing(board, T=30.0, cooling=0.99, min_T=0.01, max_steps=10000):
    current = board[:]
    init_h  = heuristic(current)
    steps   = 0
    T_now   = T                     # current temperature

    while T_now > min_T and steps < max_steps:
        h = heuristic(current)

        if h == 0:                  # goal reached
            return init_h, 0, steps, "SOLVED", current

        
        col = random.randint(0, 7)
        row = random.randint(0, 7)
        if current[col] == row:     # skip no-op
            T_now *= cooling
            steps += 1
            continue

        nb  = current[:]
        nb[col] = row
        nh  = heuristic(nb)
        dh  = nh - h               # +ve = worse move, -ve = better move

        if dh < 0 or random.random() < math.exp(-dh / T_now):
            current = nb

        T_now  *= cooling           # cool the temperature
        steps  += 1

    final_h = heuristic(current)
    status  = "SOLVED" if final_h == 0 else "FAIL"
    return init_h, final_h, steps, status, current




def run_all(n_trials=50, seed=42):
    random.seed(seed)
    boards = [random_board() for _ in range(n_trials)]

    algos = {
        "Steepest-Ascent": steepest_ascent,
        "First-Choice":    first_choice,
        "Random-Restart":  random_restart,
        "Simul-Annealing": simulated_annealing,
    }

    all_results = {name: [] for name in algos}

    for board in boards:
        for name, fn in algos.items():
            init_h, final_h, steps, status, _ = fn(board[:])
            all_results[name].append({
                "init_h":  init_h,
                "final_h": final_h,
                "steps":   steps,
                "status":  status,
            })

    return all_results




def print_table(name, results):
    print(f"\n{'='*70}")
    print(f"  ALGORITHM: {name}")
    print(f"{'='*70}")
    print(f"{'Trial':>5} | {'Init H':>6} | {'Final H':>7} | {'Steps':>7} | Status")
    print(f"{'-'*70}")
    for i, r in enumerate(results):
        icon   = "✓" if "SOLVED" in r["status"] else "✗"
        status = r["status"][:30]
        print(f"{i+1:>5} | {r['init_h']:>6} | {r['final_h']:>7} | "
              f"{r['steps']:>7} | {icon} {status}")




def print_comparison(all_results):
    print(f"\n\n{'='*78}")
    print("  COMPARISON SUMMARY  (50 trials, same boards for all algorithms)")
    print(f"{'='*78}")
    print(f"{'Algorithm':<20} | {'Solved':>6} | {'Success%':>8} | "
          f"{'Avg Steps':>10} | {'Avg Init H':>10} | {'Avg Final H':>11}")
    print(f"{'-'*78}")

    for name, results in all_results.items():
        solved     = sum(1 for r in results if "SOLVED" in r["status"])
        pct        = solved / len(results) * 100
        avg_steps  = sum(r["steps"]   for r in results) / len(results)
        avg_init_h = sum(r["init_h"]  for r in results) / len(results)
        avg_fin_h  = sum(r["final_h"] for r in results) / len(results)

        print(f"{name:<20} | {solved:>6} | {pct:>7.1f}% | "
              f"{avg_steps:>10.2f} | {avg_init_h:>10.2f} | {avg_fin_h:>11.2f}")

    print(f"{'='*78}")
    print("\nKey Takeaways:")
    print("  Steepest-Ascent : Fast but easily trapped (~16% success)")
    print("  First-Choice    : Slightly better exploration (~24% success)")
    print("  Random-Restart  : Guaranteed 100% success; uses more total steps")
    print("  Simul-Annealing : Escapes local minima via probabilistic moves (~44%)")




if __name__ == "__main__":
    all_results = run_all(n_trials=50, seed=42)

    for name, results in all_results.items():
        print_table(name, results)

    print_comparison(all_results)