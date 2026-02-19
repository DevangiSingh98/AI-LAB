from queue import PriorityQueue

# Adjacency matrix 
adj = [
    [0,283,345,0,0,0,182,0,0,0,0,0,0,0],
    [283,0,169,256,0,0,0,0,0,0,0,0,0,0],
    [345,169,0,189,134,144,0,0,0,0,0,0,0,0],
    [0,256,189,0,215,0,0,150,0,0,0,0,0,0],
    [0,0,134,215,0,185,0,0,0,305,247,0,0,0],
    [0,0,144,0,185,0,176,0,0,0,0,0,0,0],
    [182,0,0,0,0,176,0,0,0,0,0,0,0,0],
    [0,0,0,150,0,0,0,0,254,253,0,312,0,0],
    [0,0,0,0,0,0,0,254,0,97,0,215,181,0],
    [0,0,0,0,305,0,0,253,97,0,101,0,0,0],
    [0,0,0,0,247,0,0,0,0,101,0,0,0,0],
    [0,0,0,0,0,0,0,312,215,0,0,0,50,107],
    [0,0,0,0,0,0,0,0,181,0,0,50,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,107,0,0]
]

# City names:
city = {
    0: "Chicago",
    1: "Detroit",
    2: "Cleveland",
    3: "Buffalo",
    4: "Syracuse",
    5: "Pittsburgh",
    6: "Columbus",
    7: "Indianapolis"
}

# Expand function
def expand(problem, node):
    state, parent, pathcost = node
    children = []

    for action in range(len(problem)):
        cost = problem[state][action]
        
        if ( cost > 0 ):
            child = (action, state, pathcost + cost)
            children.append(child)

    return children

# BeFS

def Befs(problem, start, goal):
    
    node = (start, None, 0)

    frontier = PriorityQueue()
    frontier.put((0, node))

    reached = {}
    reached[start] = node

    while not frontier.empty():

        priority, node = frontier.get()
        state, parent, pathcost = node

        if state == goal:
            return node, reached
        
        for child in expand(problem, node):
            s, priority, childcost = child

            if (s not in reached) or (childcost < reached[s][2]):
                reached[s] = child
                frontier.put((childcost,child))

    return None, reached

start = 4 # Syracuse
goal = 0 # Chicago

solution, reached = Befs(adj, start, goal)

if solution:
    path = []
    state = solution[0]

    while state is not None:
        path.append(state)
        state = reached[state][1]

    path.reverse()

    print("Optimal Path: ")

    for i in range((len(path))):
        print(city[path[i]], end = "")
        if i != len(path) - 1:
            print(" > ", end = "")

    print("\nTotal cost: ", solution[2])

else:
    print("Failure")