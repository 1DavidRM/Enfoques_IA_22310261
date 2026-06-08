def straight_merge_sort(arr):
    # Paso 1: Comenzar con sublistas de tamaño 1
    width = 1
    n = len(arr)
    
    # Crear un arreglo auxiliar para no modificar el original en cada paso
    temp = [0] * n

    while width < n:
        # Mezclar pares de sublistas
        for i in range(0, n, 2 * width):
            # Definir los límites de las dos sublistas
            left1 = i
            right1 = min(i + width, n)
            left2 = right1
            right2 = min(i + 2 * width, n)
            
            # Realizar la fusión de las dos sublistas
            idx = left1
            i1 = left1
            i2 = left2
            
            while i1 < right1 and i2 < right2:
                if arr[i1] <= arr[i2]:
                    temp[idx] = arr[i1]
                    i1 += 1
                else:
                    temp[idx] = arr[i2]
                    i2 += 1
                idx += 1
                
            # Copiar elementos restantes de la primera sublista
            while i1 < right1:
                temp[idx] = arr[i1]
                i1 += 1
                idx += 1
                
            # Copiar elementos restantes de la segunda sublista
            while i2 < right2:
                temp[idx] = arr[i2]
                i2 += 1
                idx += 1
                
        # Copiar los elementos de temp de vuelta a arr
        for i in range(n):
            arr[i] = temp[i]
            
        # Duplicar el tamaño de la sublista
        width *= 2
        
    return arr
