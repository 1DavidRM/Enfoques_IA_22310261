import random

def obtener_conflictos(estado, n):
    """Cuenta el número total de pares de reinas que se atacan."""
    conflictos = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Misma fila
            if estado[i] == estado[j]:
                conflictos += 1
            # Diagonales
            if abs(i - j) == abs(estado[i] - estado[j]):
                conflictos += 1
    return conflictos

def min_conflictos(n, max_pasos=1000):
    # 1. Estado inicial aleatorio
    estado = [random.randint(0, n - 1) for _ in range(n)]
    
    for paso in range(max_pasos):
        conflictos_actuales = obtener_conflictos(estado, n)
        if conflictos_actuales == 0:
            return estado # Solución encontrada

        # 2. Seleccionar una variable en conflicto
        reinas_en_conflicto = []
        for i in range(n):
            if any(abs(i - j) == abs(estado[i] - estado[j]) or estado[i] == estado[j] 
                   for j in range(n) if i != j):
                reinas_en_conflicto.append(i)
        
        col = random.choice(reinas_en_conflicto)
        
        # 3. Minimizar conflictos para esa variable
        mejor_valor = estado[col]
        min_conf = float('inf')
        
        for fila in range(n):
            estado[col] = fila
            confs = obtener_conflictos(estado, n)
            if confs < min_conf:
                min_conf = confs
                mejor_valor = fila
        
        estado[col] = mejor_valor
        
    return None # No se encontró solución en el límite de pasos

# Ejemplo de uso
N = 8
solucion = min_conflictos(N)
print(f"Solución para {N}-reinas: {solucion}")
