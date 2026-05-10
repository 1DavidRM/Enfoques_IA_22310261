# Ejemplo conceptual simple utilizando la lógica de algoritmos genéticos
import random

# 1. Definir la función de aptitud (fitness)
def fitness_function(chromosome):
    return sum(chromosome) # Maximizar la suma de unos

# 2. Inicializar población
population = [[random.randint(0, 1) for _ in range(10)] for _ in range(5)]

# 3. Evolución (bucle)
for generation in range(10):
    # Evaluar y ordenar por aptitud
    population = sorted(population, key=lambda x: fitness_function(x), reverse=True)
    
    # Selección y cruce (simplificado)
    new_generation = population[:2] # Elitismo
    for _ in range(3):
        parent1 = random.choice(population[:3])
        parent2 = random.choice(population[:3])
        child = parent1[:5] + parent2[5:]
        # Mutación
        if random.random() < 0.1:
            child[random.randint(0, 9)] = 1 - child[random.randint(0, 9)]
        new_generation.append(child)
    population = new_generation

print("Mejor solución encontrada:", population[0])
