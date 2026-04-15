# -------------------------------
# VACUUM WORLD (ERRATIC)
# -------------------------------

A = 'A'
B = 'B'

DIRTY = 'Dirty'
CLEAN = 'Clean'

# -------------------------------
# GOAL TEST
# -------------------------------
def goal_test(state):
    _, a, b = state
    return a == CLEAN and b == CLEAN

# -------------------------------
# ACTIONS
# -------------------------------
def actions(state):
    return ['Suck', 'Left', 'Right']

# -------------------------------
# RESULT FUNCTION (NON-DETERMINISTIC)
# -------------------------------
def results(state, action):
    loc, a, b = state

    outcomes = []

    if action == 'Suck':
        if loc == A:
            # Clean A
            new_a = CLEAN

            # Two possibilities
            # (1) Only A cleaned
            outcomes.append((A, new_a, b))

            # (2) A and B both cleaned
            outcomes.append((A, new_a, CLEAN))

        else:  # loc == B
            new_b = CLEAN

            outcomes.append((B, a, new_b))
            outcomes.append((B, CLEAN, new_b))

    elif action == 'Left':
        if loc == B:
            outcomes.append((A, a, b))
        else:
            outcomes.append(state)

    elif action == 'Right':
        if loc == A:
            outcomes.append((B, a, b))
        else:
            outcomes.append(state)

    return outcomes

# -------------------------------
# AND-OR SEARCH (AIMA STYLE)
# -------------------------------

def and_or_search(initial_state):
    return or_search(initial_state, [])

def or_search(state, path):
    if goal_test(state):
        return []

    if state in path:
        return None

    for action in actions(state):
        plan = and_search(results(state, action), path + [state])

        if plan is not None:
            return [action, plan]

    return None

def and_search(states, path):
    plans = []

    for s in states:
        plan = or_search(s, path)

        if plan is None:
            return None

        plans.append(plan)

    return plans

# -------------------------------
# TEST
# -------------------------------

initial_state = ('A', DIRTY, DIRTY)

plan = and_or_search(initial_state)

print("Plan:")
print(plan)