import heapq

def k_way_merge(archivos_entrada, archivo_salida):
    """
    Realiza una mezcla de múltiples vías (multiway merging) de archivos ordenados
    hacia un único archivo de salida.
    """
    # Lista para almacenar los iteradores y el primer elemento de cada archivo
    heap = []
    
    # Paso 1: Inicialización. Leer el primer elemento de cada archivo.
    for i, nombre_archivo in enumerate(archivos_entrada):
        f = open(nombre_archivo, 'r')
        linea = f.readline().strip()
        if linea:
            # Se guarda una tupla: (valor, identificador_archivo, objeto_archivo)
            # El identificador evita errores si dos archivos tienen el mismo valor
            heapq.heappush(heap, (int(linea), i, f))
        else:
            f.close()

    # Paso 2: Mezcla. Extraer el menor elemento y rellenar desde el mismo archivo.
    with open(archivo_salida, 'w') as out:
        while heap:
            valor, i, f = heapq.heappop(heap)
            
            # Escribir el elemento más pequeño encontrado
            out.write(f"{valor}\n")
            
            # Leer el siguiente elemento del archivo del que provino
            siguiente_linea = f.readline().strip()
            
            if siguiente_linea:
                heapq.heappush(heap, (int(siguiente_linea), i, f))
            else:
                f.close() # Se cierra el archivo cuando se agota