import heapq

def polyphase_merge_runs(runs):
    """
    Simulación de la fase de mezcla en memoria: toma múltiples listas ordenadas 
    y las fusiona en una sola lista ordenada usando una cola de prioridad (min-heap).
    """
    merged_list = []
    # heapq.merge es el equivalente directo y altamente optimizado en Python 
    # para fusionar secuencias múltiples que ya están ordenadas.
    for val in heapq.merge(*runs):
        merged_list.append(val)
    return merged_list

def generate_runs(data, run_size):
    """
    Simulación de la fase de distribución: divide los datos grandes en 
    fragmentos (runs) del tamaño especificado y los ordena.
    """
    runs = []
    for i in range(0, len(data), run_size):
        run = sorted(data[i:i + run_size])
        runs.append(run)
    return runs

# Datos de ejemplo (como si fueran datos masivos que procesamos por partes)
large_dataset = [55, 23, 87, 12, 9, 34, 77, 42, 1, 6, 99, 14]
TAMANO_BLOQUE = 4  # Tamaño que cabe en la RAM simulada

# 1. Fase de Distribución y Ordenamiento en RAM
initial_runs = generate_runs(large_dataset, TAMANO_BLOQUE)
print(f"Fragmentos iniciales (runs) ordenados: {initial_runs}")

# 2. Fase de Mezcla Polifásica
final_sorted = polyphase_merge_runs(initial_runs)
print(f"Datos completamente ordenados: {final_sorted}")