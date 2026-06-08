def natural_merge(arr):
    if not arr:
        return []

    # Paso 1: Encontrar los tramos (runs) ordenados iniciales
    runs = []
    n = len(arr)
    i = 0
    while i < n:
        start = i
        i += 1
        # Avanza mientras el elemento actual sea mayor o igual al anterior
        while i < n and arr[i] >= arr[i - 1]:
            i += 1
        runs.append(arr[start:i])

    # Paso 2: Fusionar tramos hasta que quede solo uno
    while len(runs) > 1:
        next_runs = []
        for j in range(0, len(runs), 2):
            if j + 1 < len(runs):
                next_runs.append(merge(runs[j], runs[j + 1]))
            else:
                next_runs.append(runs[j])
        runs = next_runs

    return runs[0]


def merge(left, right):
    """Función auxiliar para fusionar dos listas ordenadas"""
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged