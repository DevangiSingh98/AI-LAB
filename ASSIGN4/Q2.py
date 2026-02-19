from queue import PriorityQueue

# 1 = Wall, 0 = Free space
# S = Entry, G = Exit

grid = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],  
    [1,0,0,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],  
    [1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],  
    [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],  
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 
    [1,0,0,1,0,0,0,0,0,0,1,1,1,0,0,1,1,0,'G',1],  
    [1,0,0,1,1,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1],  
    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],  
    [1,'S',0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1],  
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

rows = len(grid)
cols = len(grid[0])

# Find start and goal
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'S':
            start = (i, j)
        if grid[i][j] == 'G':
            goal = (i, j)

# Allowed moves: UP, DOWN, LEFT, RIGHT
moves = [(-1,0), (1,0), (0,-1), (0,1)]


# Expand Function
def expand(problem, node):
    (x, y), parent, path_cost = node
    children = []

    for dx, dy in moves:
        new_x = x + dx
        new_y = y + dy

        if (0 <= new_x < rows and
            0 <= new_y < cols and
            problem[new_x][new_y] != 1):

            child = ((new_x, new_y), (x, y), path_cost + 1)
            children.append(child)

    return children


# befs
def best_first_search(problem, start, goal):

    node = (start, None, 0)

    frontier = PriorityQueue()
    frontier.put((0, node))

    reached = {}
    reached[start] = node

    explored = 0

    while not frontier.empty():

        priority, node = frontier.get()
        (x, y), parent, path_cost = node
        explored += 1

        if (x, y) == goal:
            return node, reached, explored

        for child in expand(problem, node):
            (nx, ny), _, child_cost = child

            if ((nx, ny) not in reached) or (child_cost < reached[(nx, ny)][2]):
                reached[(nx, ny)] = child
                frontier.put((child_cost, child))

    return None, reached, explored


solution, reached, explored_nodes = best_first_search(grid, start, goal)

if solution:

    path = []
    state = solution[0]

    while state is not None:
        path.append(state)
        state = reached[state][1]

    path.reverse()

    print("Evacuation Path:")
    for p in path:
        print(p)

    print("\nTotal Cost:", solution[2])
    print("Number of nodes explored:", explored_nodes)

else:
    print("Failure")
