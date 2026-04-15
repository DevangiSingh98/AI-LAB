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

# Cost of a path
def path_cost(path):
    cost = 0
    for i in range(len(path)-1):
        cost += graph[path[i]][path[i+1]]
    cost += graph[path[-1]][path[0]]
    return cost


# Initial population
def create_population(size):
    pop = []
    for _ in range(size):
        p = list(range(n))
        random.shuffle(p)
        pop.append(p)
    return pop


# Fitness function
def fitness(path):
    return 1 / path_cost(path)


# Selection
def select(population):
    population = sorted(population, key=lambda x: path_cost(x))
    return population[:2]


# One Point Crossover
def one_point_crossover(p1, p2):
    point = random.randint(1, n-2)

    child = p1[:point]

    for city in p2:
        if city not in child:
            child.append(city)

    return child


# Two Point Crossover

def two_point_crossover(p1, p2):
    p, q = sorted(random.sample(range(n), 2))

    child = [None]*n
    child[p:q] = p1[p:q]

    fill = [c for c in p2 if c not in child]

    j = 0
    for i in range(n):
        if child[i] is None:
            child[i] = fill[j]
            j += 1

    return child



# Mutation

def mutate(path):
    i, j = random.sample(range(n),2)
    path[i], path[j] = path[j], path[i]



# Genetic Algorithm

def genetic_algorithm(crossover_type, generations=30, pop_size=10):

    population = create_population(pop_size)

    print("\n==========================")
    print("Running GA with", crossover_type)

    for g in range(generations):

        population = sorted(population, key=lambda x: path_cost(x))
        best = population[0]

        print("Generation", g+1, "Best Cost:", path_cost(best))

        new_population = population[:2]

        while len(new_population) < pop_size:

            p1, p2 = select(population)

            if crossover_type == "one":
                child = one_point_crossover(p1, p2)
            else:
                child = two_point_crossover(p1, p2)

            if random.random() < 0.2:
                mutate(child)

            new_population.append(child)

        population = new_population

    best = min(population, key=lambda x: path_cost(x))

    print("\nFinal Best Path:", best + [best[0]])
    print("Final Cost:", path_cost(best))



# Run both crossover types

genetic_algorithm("one")
genetic_algorithm("two")
