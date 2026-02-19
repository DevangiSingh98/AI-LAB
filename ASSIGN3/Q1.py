adj = [
    # Room  Dirt  Left   Right   Action
    ["A",    1,   None,  "B",   "CLEAN"],
    ["A",    0,   None,  "B",   "RIGHT"],

    ["B",    1,   "A",   "C",   "CLEAN"],
    ["B",    0,   "A",   "C",   "LEFT"],

    ["C",    1,   "B",   None,  "CLEAN"],
    ["C",    0,   "B",   None,  "STOP"]
]

# 0 - Clean, 1 - Dirt


def agent(matrix, loc):
    #Find current dirt status
    current = None
    for row in matrix:
        if row[0] == loc:
            current = row[1]
            break


    for row in matrix:
        room, dirt, left, right, action = row
        if room == loc and dirt == current:
            return action

def update(matrix, loc, action):
    if action == "CLEAN":
        #only update the row that matches current dirt status
        for row in matrix:
            if row[0] == loc and row[1] == 1: #Only clean when dirty
                row[1] = 0
                break
    elif action == "LEFT" or action == "RIGHT":
        #Find any row for this loc to get navigation info

        for row in matrix:
            if row[0] == loc:
                if action == "LEFT":
                    return row[2]
                elif action == "RIGHT":
                    return row[3]
    return loc
        

start = "C"
step = 1

print("Initial matrix:", adj)
print("Start:", start)

while step < 10:
    action = agent(adj, start)

    print("\nStep:", step)
    print("Location:", start)
    print("Action:", action)

    if action == "STOP":
        print("\nAll rooms clean.")
        break

    start = update(adj, start, action)
    print("Matrix state:\n", adj)

    step += 1
