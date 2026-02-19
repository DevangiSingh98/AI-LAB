# problem defintion
TOTAL = 3

def isvalid(state):
    gleft, bleft, boat = state
    gright = TOTAL - gleft
    bright = TOTAL - bleft

    # Girls should not be outnumbered on either side
    if (gleft > 0 and bleft > gleft):
        return False
    if (gright > 0 and bright > gright):
        return False

    return True


def goaltest(state):
    return state == (0, 0, 1)


def actions(state):
    gleft, bleft, boat = state
    possible_moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    validactions = []

    for g, b in possible_moves:
        if boat == 0:  # boat on left
            newstate = (gleft - g, bleft - b, 1)
        else:          # boat on right
            newstate = (gleft + g, bleft + b, 0)

        if 0 <= newstate[0] <= 3 and 0 <= newstate[1] <= 3:
            if isvalid(newstate):
                validactions.append(newstate)

    return validactions


# DLS

def dls(state, limit, path):

    if goaltest(state):
        return path

    elif limit == 0:
        return "cutoff"

    else:
        cutoff = False

        for child in actions(state):

            if child not in path:  # avoid cycles
                result = dls(child, limit - 1, path + [child])

                if result == "cutoff":
                    cutoff = True
                elif result != "failure":
                    return result

        if cutoff:
            return "cutoff"
        else:
            return "failure"


def depth_limited_search(limit):
    start = (3, 3, 0)
    return dls(start, limit, [start])


# iterative deepening search

def iterative_deepening_search():
    depth = 0
    while True:
        result = depth_limited_search(depth)
        if result != "cutoff":
            return result
        depth += 1


print("Depth Limited Search: ")
result = depth_limited_search(3)
print(result)

print("\nIterative Deepening Search")
ids = iterative_deepening_search()
print(ids)
