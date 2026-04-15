import random

# HEURISTIC: number of attacking queen pairs
# (lower is better; 0 = solution)

def heuristic(board):
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:                    # same row
                attacks += 1
            if abs(board[i] - board[j]) == abs(i - j): # same diagonal
                attacks += 1
    return attacks



# STEEPEST-ASCENT HILL CLIMBING
# Returns: (init_h, final_h, steps, status, final_board)

def steepest_ascent_hill_climbing(board):
    current = board[:]
    init_h  = heuristic(current)
    steps   = 0

    while True:
        h = heuristic(current)

        #Goal check
        if h == 0:
            return init_h, 0, steps, "SOLVED", current

        #Find best neighbour (move one queen in its column)
        best_h      = h
        best_boards = []
        n           = len(current)

        for col in range(n):
            for row in range(n):
                if current[col] == row:
                    continue
                neighbour = current[:]
                neighbour[col] = row
                nh = heuristic(neighbour)
                if nh < best_h:
                    best_h      = nh
                    best_boards = [neighbour]
                elif nh == best_h:
                    best_boards.append(neighbour)

        # Local minimum / plateau
        if best_h >= h:
            return init_h, h, steps, "FAIL (local min)", current

        # Move to a random best neighbour (break ties randomly)
        current = random.choice(best_boards)
        steps  += 1



# MAIN EXPERIMENT: 50 random initial boards

def run_experiment(n_trials=50, seed=42):
    random.seed(seed)
    results = []

    for trial in range(1, n_trials + 1):
        board = [random.randint(0, 7) for _ in range(8)]
        init_h, final_h, steps, status, final_board = steepest_ascent_hill_climbing(board)
        results.append({
            "trial":       trial,
            "init_board":  board,
            "init_h":      init_h,
            "final_h":     final_h,
            "steps":       steps,
            "status":      status,
            "final_board": final_board,
        })

    return results



# PRINT RESULTS TABLE

def print_results(results):
    header = f"{'Trial':>5} | {'Initial Board':^24} | {'Init H':>6} | {'Final H':>7} | {'Steps':>5} | Status"
    sep    = "=" * 80
    print(sep)
    print(header)
    print(sep)

    for r in results:
        board_str = str(r["init_board"])
        icon      = "✓" if "SOLVED" in r["status"] else "✗"
        print(f"{r['trial']:>5} | {board_str:^24} | {r['init_h']:>6} | {r['final_h']:>7} | "
              f"{r['steps']:>5} | {icon} {r['status']}")

    print(sep)

    solved  = sum(1 for r in results if "SOLVED" in r["status"])
    failed  = len(results) - solved
    avg_h0  = sum(r["init_h"] for r in results) / len(results)
    avg_s_s = (sum(r["steps"] for r in results if "SOLVED" in r["status"]) / solved) if solved else 0
    avg_s_f = (sum(r["steps"] for r in results if "FAIL"   in r["status"]) / failed) if failed else 0

    print(f"\nSUMMARY")
    print(f"  Solved : {solved}/{len(results)} ({solved/len(results)*100:.0f}%)")
    print(f"  Failed : {failed}/{len(results)} ({failed/len(results)*100:.0f}%)")
    print(f"  Avg initial h         : {avg_h0:.2f}")
    print(f"  Avg steps (solved)    : {avg_s_s:.2f}")
    print(f"  Avg steps (failed)    : {avg_s_f:.2f}")



# PROVE LOCAL MINIMUM

def prove_local_minimum(results):
    local_mins = [r for r in results if "FAIL" in r["status"]]
    if not local_mins:
        print("\nNo local minimum found in this run.")
        return

    ex    = local_mins[0]
    board = ex["final_board"]
    h     = ex["final_h"]
    n     = len(board)

    # Evaluate every single-queen move
    all_neighbour_h = [
        heuristic(board[:col] + [row] + board[col + 1:])
        for col in range(n)
        for row in range(n)
        if board[col] != row
    ]
    min_neighbour_h = min(all_neighbour_h)
    total_neighbours = len(all_neighbour_h)

 
    print("LOCAL MINIMUM PROOF")
 
    print(f"  Board state  : {board}")
    print(f"  Current h    : {h}  (not a solution — h ≠ 0)")
    print(f"  Neighbours   : {total_neighbours} possible single-queen moves")
    print(f"  Best neigh h : {min_neighbour_h}")
    print()
    if min_neighbour_h >= h:
        print(f"    CONFIRMED LOCAL MINIMUM")
        print(f"    Every neighbour has h ≥ {h}.")
        print(f"    Steepest-ascent is stuck — cannot improve without restart.")
    else:
        print("  Not a local minimum (algorithm should have continued).")


if __name__ == "__main__":
    results = run_experiment(n_trials=50, seed=42)
    print_results(results)
    prove_local_minimum(results)