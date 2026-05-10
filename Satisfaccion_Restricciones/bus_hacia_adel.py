def forward_checking(variables, domains, constraints, assignment={}):
    """
    Implementación básica de Forward Checking para CSP.
    """
    # Si todas las variables están asignadas, hemos terminado
    if len(assignment) == len(variables):
        return assignment

    # Seleccionar una variable no asignada (heurística simple: primera disponible)
    unassigned = [v for v in variables if v not in assignment]
    var = unassigned[0]

    # Intentar asignar valores al dominio de la variable
    for value in domains[var]:
        if is_consistent(var, value, assignment, constraints):
            # Asignar valor
            local_assignment = assignment.copy()
            local_assignment[var] = value
            
            # --- COMPROBACIÓN HACIA DELANTE ---
            # Crear una copia de los dominios para no alterar el original
            new_domains = {v: list(d) for v, d in domains.items()}
            new_domains[var] = [value]
            
            # Reducir dominios de variables no asignadas basadas en la nueva asignación
            if forward_check(var, value, new_domains, constraints, unassigned[1:]):
                # Continuar búsqueda recursivamente
                result = forward_checking(variables, new_domains, constraints, local_assignment)
                if result is not None:
                    return result
            # Si forward_check falla, el valor no es válido, se hace backtracking implícito
                
    return None

def forward_check(var, value, domains, constraints, future_vars):
    """
    Elimina valores de los dominios futuros que violan restricciones
    con la asignación actual.
    """
    for future_var in future_vars:
        for future_val in list(domains[future_var]):
            # Si el valor futuro es incompatible con la asignación actual
            if not constraints(var, value, future_var, future_val):
                domains[future_var].remove(future_val)
                # Si el dominio queda vacío, la asignación es insostenible
                if not domains[future_var]:
                    return False
    return True

def is_consistent(var, value, assignment, constraints):
    """Verifica si el valor es consistente con las asignaciones actuales."""
    for other_var, other_val in assignment.items():
        if not constraints(var, value, other_var, other_val):
            return False
    return True

# --- EJEMPLO DE USO: Problema del Mapa (Coloreo simple) ---
# Variables: A, B, C. Colores: 'R', 'V'
# Restricción: A!=B, B!=C
variables = ['A', 'B', 'C']
domains = {
    'A': ['R', 'V'],
    'B': ['R', 'V'],
    'C': ['R', 'V']
}

def map_constraints(v1, val1, v2, val2):
    # Definir restricciones de vecindad
    if (v1 == 'A' and v2 == 'B') or (v1 == 'B' and v2 == 'A'):
        return val1 != val2
    if (v1 == 'B' and v2 == 'C') or (v1 == 'C' and v2 == 'B'):
        return val1 != val2
    return True

solution = forward_checking(variables, domains, map_constraints)
print("Solución encontrada:", solution)
