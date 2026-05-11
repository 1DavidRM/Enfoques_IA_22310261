# Ejemplo conceptual simplificado de estructura de backtracking
def solve(variables, assignment, constraints):
    if not variables:
        return assignment
    
    var = variables[0]
    for value in get_domain(var):
        if is_consistent(var, value, assignment, constraints):
            assignment[var] = value
            result = solve(variables[1:], assignment, constraints)
            if result:
                return result
            # Si hay conflicto aquí, el CBJ saltaría 
            # más atrás que el backtracking normal
            del assignment[var]
    return None
