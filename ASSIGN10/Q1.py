import numpy as np

# -------------------------------
# STEP 1: DATA (coordinates of the cities)
# -------------------------------
points = np.array([
    [0.046, 4.006],
    [-0.454, -0.706],
    [0.181, 5.769],
    [0.739, 4.741],
    [-0.11, 5.179],
    [-0.235, 0.271],
    [-0.265, 5.257],
    [0.148, 5.131],
    [0.458, 5.164],
    [5.104, 4.02],
    [-0.117, -0.117],
    [0.034, -0.712],
    [-0.351, 4.836],
    [5.515, 5.466],
    [-0.301, 0.926],
    [5.411, 4.39],
    [-0.196, 4.268],
    [5.166, 5.488],
    [0.181, 4.677],
    [4.58, 4.845],
    [0.121, -0.957],
    [-0.272, 0.055],
    [0.79, 0.384],
    [-0.506, 0.157],
    [0.049, 5.484],
    [0.003, 4.883],
    [-0.232, -0.233],
    [-0.3, -0.146],
    [-0.862, -0.281],
    [4.76, 4.907],
    [5.406, 5.678],
    [4.964, 5.502],
    [5.172, 4.118],
    [-0.018, 5.782],
    [-1.31, 5.411],
    [4.942, 4.849],
    [-0.007, -0.529],
    [5.369, 5.086],
    [4.261, 4.64],
    [-0.404, 4.749],
    [4.447, 4.402],
    [0.733, -0.113],
    [4.336, 5.098],
    [5.162, 4.807],
    [4.662, 5.306],
    [0.044, 4.85],
    [4.77, 5.529],
    [-0.575, 0.188],
    [0.248, -0.069],
    [0.324, 0.762]
])

k = 3  # reprsents the number of airports
alpha = 0.01  # learning rate (smaller learning rate is taken so that it doesnt overshoot and performs small learning. )
iterations = 10 

#Step 2 : Initializing W, choosing first k points (here 3)

centers = points[:k].copy()

# -------------------------------
# STEP 3: LOSS FUNCTION (J=∑min∣∣x−ck​∣∣2)
# -------------------------------
def compute_loss(points, centers):
    loss = 0
    for p in points:
        distances = [np.sum((p - c)**2) for c in centers]
        loss += min(distances)
    return loss

# -------------------------------
# STEP 4: ASSIGN POINTS
# -------------------------------
def assign_clusters(points, centers):
    clusters = [[] for _ in range(len(centers))]
    
    for p in points:
        distances = [np.sum((p - c)**2) for c in centers]
        idx = np.argmin(distances)
        clusters[idx].append(p)
    
    return clusters

# -------------------------------
# STEP 5: GRADIENT COMPUTATION
# -------------------------------
def compute_gradient(cluster, center):
    grad = np.zeros_like(center)
    for p in cluster:
        grad += (center - p)  # derivative of squared distance
    return grad

# -------------------------------
# STEP 6: GRADIENT DESCENT LOOP
# -------------------------------
for it in range(iterations):
    clusters = assign_clusters(points, centers)
    
    # AIMA: for each wi in w
    for i in range(len(centers)):
        if len(clusters[i]) == 0:
            continue
        
        grad = compute_gradient(clusters[i], centers[i])
        
        # AIMA UPDATE RULE
        centers[i] = centers[i] - alpha * grad
    
    print(f"Iteration {it+1}")
    print("Centers:\n", centers)
    print("Loss:", compute_loss(points, centers))
    print("-" * 40)

# -------------------------------
# FINAL RESULT
# -------------------------------
print("Final Airport Locations:")
print(centers)