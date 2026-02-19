from queue import PriorityQueue

#adj matrix
graph = [
    ["", "Chicago", "Detroit", "Indianapolis", "Columbus", "Cleveland", "Pittsburgh", "Buffalo", "Syracuse", "New York", "Philadelphia", "Baltimore", "Providence", "Boston"],
    ["Chicago",      0, 283, 183,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],
    ["Detroit",    283,   0,   0,   0, 169,   0,   0,   0,   0,   0,   0,   0,   0],
    ["Indianapolis",183,  0,   0, 176,   0,   0,   0,   0,   0,   0,   0,   0,   0],
    ["Columbus",     0,   0, 176,   0, 142, 185,   0,   0,   0,   0,   0,   0,   0],
    ["Cleveland",    0, 169,   0, 142,   0, 133, 191,   0,   0,   0,   0,   0,   0],
    ["Pittsburgh",   0,   0,   0, 185, 133,   0,   0,   0, 305,   0,   0,   0,   0],
    ["Buffalo",      0,   0,   0,   0, 191,   0,   0, 150,   0,   0,   0,   0,   0],
    ["Syracuse",     0,   0,   0,   0,   0,   0, 150,   0, 247,   0,   0,   0,   0],
    ["New York",     0,   0,   0,   0,   0,   0,   0, 247,   0,  95,   0, 181,   0],
    ["Philadelphia", 0,   0,   0,   0,   0, 305,   0,   0,  95,   0, 101,   0,   0],
    ["Baltimore",    0,   0,   0,   0,   0,   0,   0,   0,   0, 101,   0,   0,   0],
    ["Providence",   0,   0,   0,   0,   0,   0,   0,   0, 181,   0,   0,   0,  50],
    ["Boston",       0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  50,   0]
]

# Heuristic
h = [0, 860, 610, 780, 640, 550, 470, 400, 260, 215, 270, 360, 50, 0]

n = len(graph)

#Greedy Best First Search
def greedy(start, goal):

    pq = PriorityQueue()
    pq.put((h[start], start))

    visited = [False] * n
    parent = [-1] * n
    explored = 0

    while not pq.empty():

        _, current = pq.get()

        if visited[current]:
            continue

        visited[current] = True
        explored += 1

        if current == goal:
            break

        for i in range(1, n):
            if graph[current][i] != 0 and not visited[i]:
                parent[i] = current
                pq.put((h[i], i))

    # reconstruct path
    path = []
    temp = goal
    while temp != -1:
        path.append(graph[temp][0])
        temp = parent[temp]

    path.reverse()
    return path, explored



# A* Search

def astar(start, goal):

    pq = PriorityQueue()
    pq.put((h[start], 0, start))

    visited = [False] * n
    parent = [-1] * n
    g = [999999] * n
    g[start] = 0
    explored = 0

    while not pq.empty():

        _, cost_so_far, current = pq.get()

        if visited[current]:
            continue

        visited[current] = True
        explored += 1

        if current == goal:
            break

        for i in range(1, n):

            if graph[current][i] != 0:
                new_cost = cost_so_far + graph[current][i]

                if new_cost < g[i]:
                    g[i] = new_cost
                    parent[i] = current
                    f = new_cost + h[i]
                    pq.put((f, new_cost, i))

    # reconstruct path
    path = []
    temp = goal
    while temp != -1:
        path.append(graph[temp][0])
        temp = parent[temp]

    path.reverse()
    return path, explored



start = 1   # Chicago
goal = 13   # Boston

p1, c1 = greedy(start, goal)
p2, c2 = astar(start, goal)

print("Greedy Path:", p1)
print("Cities Explored:", c1)

print("\nA* Path:", p2)
print("Cities Explored:", c2)
