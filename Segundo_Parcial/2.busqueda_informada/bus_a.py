import heapq

def a_star(graph, start, goal, heuristic):
    open_list = [(0 + heuristic[start], 0, start, [])] # (f, g, nodo, camino)
    closed_list = set()
    
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        
        if current in closed_list:
            continue
            
        path = path + [current]
        if current == goal:
            return path
            
        closed_list.add(current)
        
        for neighbor, weight in graph[current].items():
            if neighbor not in closed_list:
                new_g = g + weight
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(open_list, (new_f, new_g, neighbor, path))
    return None

# Ejemplo de grafo y heurística
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
heuristic = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
print(a_star(graph, 'A', 'D', heuristic)) # Salida: ['A', 'B', 'C', 'D']
