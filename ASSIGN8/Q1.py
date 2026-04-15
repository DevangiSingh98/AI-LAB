import random

graph = [
[0,10,15,20,25,30,35,40],
[12,0,35,15,20,25,30,45],
[25,30,0,10,40,20,15,35],
[18,25,12,0,15,30,20,10],
[22,18,28,20,0,15,25,30],
[35,22,18,28,12,0,40,20],
[30,35,22,18,28,32,0,15],
[40,28,35,22,18,25,12,0]
]

n = len(graph)

def path_cost(path):
    cost = 0
    for i in range(len(path)-1):
        cost += graph[path[i]][path[i+1]]
    cost += graph[path[-1]][path[0]]
    return cost


def get_neighbors(path):
    neighbors = []
    for i in range(1, n):
        for j in range(i+1, n):
            new_path = path[:]
            new_path[i], new_path[j] = new_path[j], new_path[i]
            neighbors.append(new_path)
    return neighbors


def local_beam_search(k, iterations=10):

    print("\n==============================")
    print("Running Local Beam Search with k =", k)

    states = []

    for _ in range(k):
        path = list(range(n))
        random.shuffle(path)
        states.append(path)

    print("\nInitial States:")
    for s in states:
        print(s + [s[0]], "Cost:", path_cost(s))

    best_path = None
    best_cost = float('inf')

    for it in range(iterations):

        print("\nIteration", it+1)

        all_neighbors = []

        for state in states:
            neighbors = get_neighbors(state)
            all_neighbors.extend(neighbors)

        all_neighbors.sort(key=lambda x: path_cost(x))

        states = all_neighbors[:k]                 #pruning

        print("Top", k, "states:")

        for s in states:
            print(s + [s[0]], "Cost:", path_cost(s))

        current_cost = path_cost(states[0])

        if current_cost < best_cost:
            best_cost = current_cost
            best_path = states[0]

    print("\nFinal Best Path:", best_path + [best_path[0]])
    print("Final Cost:", best_cost)

    return best_path, best_cost


for k in [3,5,10]:
    local_beam_search(k)