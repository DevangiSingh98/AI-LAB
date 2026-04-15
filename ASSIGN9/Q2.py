import math

distance = [
[0, 283, 345, 0, 182, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[283, 0, 0, 0, 0, 256, 0, 0, 0, 0, 0, 0, 0, 0],
[345, 0, 0, 144, 0, 189, 133, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 144, 0, 176, 0, 185, 0, 0, 0, 0, 0, 0, 0],
[182, 0, 0, 176, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 256, 189, 0, 0, 0, 0, 150, 0, 0, 0, 0, 0, 0],
[0, 0, 133, 185, 0, 0, 0, 0, 0, 305, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 150, 0, 0, 248, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 248, 0, 101, 0, 215, 181, 0],
[0, 0, 0, 0, 0, 0, 305, 0, 101, 0, 101, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 101, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 215, 0, 0, 0, 50, 107],
[0, 0, 0, 0, 0, 0, 0, 0, 181, 0, 0, 50, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 107, 0, 0]
]

States = {
0: "Chicago", 1: "Detroit", 2: "Cleveland", 3: "Columbus", 4: "Indianapolis",
5: "Buffalo", 6: "Pittsburgh", 7: "Syracuse", 8: "New York", 9: "Philadelphia",
10: "Baltimore", 11: "Boston", 12: "Providence", 13: "Portland"
}

START = 0
GOAL = 11

minimax_nodes = 0
alphabeta_nodes = 0


def neighbors(city):
    return [(i, distance[city][i]) for i in range(len(distance)) if distance[city][i] > 0]



def alphabeta(city, visited, bound):
    global alphabeta_nodes
    alphabeta_nodes += 1

    if city == GOAL:
        return 0, [city]

    visited.add(city)

    best_cost = float('inf')
    best_path = []

    for nxt, cost in neighbors(city):
        if nxt not in visited:
            val, path = alphabeta(nxt, visited.copy(), best_cost)

            if val != float('inf') and cost + val < best_cost:
                best_cost = cost + val
                best_path = [city] + path

            if best_cost >= bound:
                break

    return best_cost, best_path

def run():
    best_cost_mm = float('inf')
    best_path_mm = []

   
    best_cost_ab = float('inf')
    best_path_ab = []

    for nxt, cost in neighbors(START):
        val, path = alphabeta(nxt, set(), best_cost_ab)
        if val != float('inf') and cost + val < best_cost_ab:
            best_cost_ab = cost + val
            best_path_ab = [START] + path

    if not best_path_ab:
        best_path_ab = best_path_mm
        best_cost_ab = best_cost_mm

    return best_cost_mm, best_path_mm, best_cost_ab, best_path_ab


if __name__ == "__main__":
    mm_cost, mm_path, ab_cost, ab_path = run()

    print("\nAlpha-Beta Path:")
    print(" → ".join(States[i] for i in ab_path))
    print("Cost:", ab_cost)

    print("\nNodes Explored:")
    print("Alpha-Beta:", alphabeta_nodes)

    
