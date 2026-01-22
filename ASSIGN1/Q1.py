graph = {
    "Syracuse": [("Buffalo", 150), ("New York", 254), ("Boston", 312),("Philadelphia",253)],
    "Buffalo": [("Syracuse", 150), ("Cleveland", 189), ("Detroit", 256), ("Pittsburgh", 215)],
    "Detroit": [("Buffalo", 256), ("Chicago", 283), ("Cleveland", 169)],
    "Cleveland": [("Detroit", 169), ("Buffalo", 189), ("Chicago", 345), ("Columbus", 144), ("Pittsburgh", 134)],
    "Pittsburgh": [("Cleveland", 134), ("Buffalo", 215), ("Columbus", 185), ("Philadelphia", 305), ("Baltimore", 247)],
    "Columbus": [("Cleveland", 144), ("Pittsburgh", 185), ("Indianapolis", 176)],
    "Indianapolis": [("Columbus", 176), ("Chicago", 182)],
    "Chicago": [("Detroit", 283), ("Cleveland", 345), ("Indianapolis", 182)],
    "New York": [("Philadelphia", 97)],
    "Philadelphia": [("New York", 97), ("Baltimore", 101), ("Pittsburgh", 305)],
    "Baltimore": [("Philadelphia", 101), ("Pittsburgh", 247)],
    "Boston": []
}

def bfs(graph, src, dest):
    queue=[(src, [src], 0)]
    paths=[]

    while queue:
        node, path, cost= queue.pop(0)  
        if node== dest:
            paths.append((path, cost))
            continue

        for neighbor, weight in graph[node]:
            if neighbor not in path:
                queue.append((neighbor,path +[neighbor],cost + weight))
    return paths




def dfs(graph, src, dest):
    paths = []
    def dfs(node, path, cost):
        if node==dest:
            paths.append((path, cost))
            return

        for neighbor, weight in graph[node]:
            if neighbor not in path:
                dfs(neighbor,path + [neighbor],cost + weight)
    dfs(src, [src], 0)
    return paths

bfsPaths= bfs(graph, "Syracuse", "Chicago")
dfsPaths= dfs(graph, "Syracuse", "Chicago")

print("BFS Paths:")
for path, cost in bfsPaths:
    print(path, "Cost:", cost)
print("\nDFS Paths:")
for path, cost in dfsPaths:
    print(path, "Cost:", cost)

