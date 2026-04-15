board = [[" "] * 3 for _ in range(3)]

# ── Search tree printing ──────────────────────────────────────────
TREE_DEPTH = 2          # plies to show beneath each AI root move

_tree_lines = []


def _record(depth, move, player, val, pruned=False):
    if depth > TREE_DEPTH:
        return
    indent = "  " * depth
    tag = " [PRUNED]" if pruned else ""
    score = f" → score={val}" if val is not None else ""
    _tree_lines.append(f"{indent}[{player}] ({move[0]},{move[1]}){score}{tag}")


def show_tree():
    print("\n── AI search tree (depth ≤ "
          f"{TREE_DEPTH} beneath each root move) ──")
    for line in _tree_lines:
        print(line)
    print("──────────────────────────────────────\n")


# ── Board helpers ─────────────────────────────────────────────────

def show():
    print("  0 1 2")
    for idx, row in enumerate(board):
        print(idx, " ".join(row))
    print()


def win():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None


def full():
    return all(cell != " " for row in board for cell in row)


# ── Minimax with alpha-beta pruning (fixed) ───────────────────────

def minimax(is_max, alpha, beta, depth=0, recording=False):
    w = win()
    if w == "X":
        return 1
    if w == "O":
        return -1
    if full():
        return 0

    if is_max:
        best = -999
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    val = minimax(False, alpha, beta, depth + 1, recording)
                    board[i][j] = " "

                    if recording:
                        _record(depth, (i, j), "X", val)

                    if val > best:
                        best = val
                    if best > alpha:
                        alpha = best
                    # FIX: pruning breaks both loops via flag
                    if beta <= alpha:
                        if recording:
                            _record(depth, (i, j), "X", None, pruned=True)
                        break           # break inner j-loop
            else:
                continue                # inner loop wasn't broken
            break                       # break outer i-loop
        return best

    else:
        best = 999
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    val = minimax(True, alpha, beta, depth + 1, recording)
                    board[i][j] = " "

                    if recording:
                        _record(depth, (i, j), "O", val)

                    if val < best:
                        best = val
                    if best < beta:
                        beta = best
                    if beta <= alpha:
                        if recording:
                            _record(depth, (i, j), "O", None, pruned=True)
                        break
            else:
                continue
            break
        return best


# ── Best move (X is the AI) ───────────────────────────────────────

def best_move():
    global _tree_lines
    _tree_lines = []

    best_val = -999
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                # Insert root line FIRST, then let minimax append children
                root_idx = len(_tree_lines)
                _tree_lines.append("")          # placeholder
                board[i][j] = "X"
                val = minimax(False, -999, 999, depth=1, recording=True)
                board[i][j] = " "

                is_new_best = val > best_val
                marker = " *BEST*" if is_new_best else ""
                _tree_lines[root_idx] = f"[X root] ({i},{j}) → score={val}{marker}"

                if is_new_best:
                    best_val = val
                    move = (i, j)

    # rename *BEST* → *CHOSEN* for the final selected move
    for idx, line in enumerate(_tree_lines):
        if f"({move[0]},{move[1]})" in line and "X root" in line:
            _tree_lines[idx] = line.replace("*BEST*", "*CHOSEN*")
            break

    show_tree()
    return move


# ── Game loop ─────────────────────────────────────────────────────

while True:
    show()

    # FIX: validate input
    try:
        r = int(input("Your move — row (0-2): "))
        c = int(input("             col (0-2): "))
    except ValueError:
        print("Enter numbers only.\n")
        continue

    if not (0 <= r <= 2 and 0 <= c <= 2):
        print("Row and column must be 0, 1, or 2.\n")
        continue

    if board[r][c] != " ":
        print("Cell taken, try again.\n")
        continue

    board[r][c] = "O"

    if win() == "O":
        show()
        print("You win!")
        break

    if full():
        show()
        print("Draw!")
        break

    ai_r, ai_c = best_move()
    board[ai_r][ai_c] = "X"
    print(f"AI plays ({ai_r}, {ai_c})\n")

    if win() == "X":
        show()
        print("AI wins!")
        break

    if full():
        show()
        print("Draw!")
        break