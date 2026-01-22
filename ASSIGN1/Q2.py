graph= {"Raj": ["Priya", "Akash", "Sunil"],
        "Priya": ["Raj", "Aarav", "Neha"],
        "Aarav": ["Priya", "Neha", "Arjun"],
        "Akash": ["Raj", "Sunil", "Neha"],
        "Sunil": ["Raj", "Akash", "Sneha", "Maya"],
        "Neha": ["Priya", "Akash", "Aarav", "Rahul"],
        "Sneha": ["Sunil", "Rahul"],
        "Rahul": ["Sneha", "Neha", "Arjun", "Pooja"],
        "Arjun": ["Aarav", "Rahul", "Pooja"],
        "Pooja": ["Rahul", "Arjun"],
        "Maya": ["Sunil"]}

def bfs(graph, src):
    visited = set()
    queue = [src]
    tree = []

    visited.add(src)

    while queue:
        node= queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                tree.append((node, neighbor))  
    return tree


def dfs(graph, src):
    visited= set()
    tree= []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                tree.append((node, neighbor)) 
                dfs(neighbor)

    dfs(src)
    return tree


startnode = "Raj"

bfsTree = bfs(graph, startnode)
dfsTree = dfs(graph, startnode)

print("BFS Tree Edges:")
for edge in bfsTree:
    print(edge)
print("\nDFS Tree Edges:")
for edge in dfsTree:
    print(edge)
