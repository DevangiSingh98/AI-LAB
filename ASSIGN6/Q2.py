from queue import PriorityQueue

maze = [
    [2, 0, 0, 0, 1],
    [0, 1, 0, 0, 3],
    [0, 3, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [3, 0, 0, 0, 3]
]

rows = 5
cols = 5

# Directions: L, R, U, D
moves = [(0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U'), (1, 0, 'D')]

# Manhattan distance heuristic
def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

# A* to a single goal
def astar(start, goal):
    pq = PriorityQueue()
    counter = 0                         
    pq.put((0, counter, start))

    visited = set()
    parent = {}
    g_cost = {start: 0}
    visited_tiles = []

    while not pq.empty():
        _, _, current = pq.get()

        if current in visited:
            continue
        visited.add(current)
        visited_tiles.append(current)

        if current == goal:
            break

        x, y = current
        for dx, dy, _ in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if maze[nx][ny] != 1:           # not a wall
                    new_g = g_cost[current] + 1
                    if (nx, ny) not in g_cost or new_g < g_cost[(nx, ny)]:
                        g_cost[(nx, ny)] = new_g
                        f = new_g + heuristic(nx, ny, goal[0], goal[1])
                        counter += 1
                        pq.put((f, counter, (nx, ny)))
                        parent[(nx, ny)] = current

    # Reconstruct path from goal back to start
    path = []
    node = goal
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()
    return path, visited_tiles


# Reach All Rewards

# Find start position
start = None
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 2:
            start = (i, j)

# Find all rewards
rewards = []
for i in range(rows):
    for j in range(cols):
        if maze[i][j] == 3:
            rewards.append((i, j))

print("Start:", start)
print("Rewards to collect:", rewards)

current_position = start
all_visited = []
total_path = []

while rewards:
    # Choose nearest reward by Manhattan distance
    nearest = min(rewards,
                  key=lambda r: heuristic(current_position[0],
                                          current_position[1],
                                          r[0], r[1]))

    path, visited = astar(current_position, nearest)

   
    total_path.extend(path if not total_path else path[1:])
    all_visited.extend(visited)

    print(f"\n  Collected reward at {nearest}  |  path: {path}")

    current_position = nearest
    rewards.remove(nearest)

print("\n")
print("Full Path to Collect All Rewards:")
print(total_path)
print("\nTiles Visited During A* Search (per segment):")
print(all_visited)
print("\nTotal steps:", len(total_path) - 1)