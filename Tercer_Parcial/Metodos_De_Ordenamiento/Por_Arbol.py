class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

    def insertar(self, valor):
        """Inserta un valor manteniendo la regla del árbol de búsqueda."""
        if valor < self.valor:
            if self.izq is None:
                self.izq = Nodo(valor)
            else:
                self.izq.insertar(valor)
        elif valor > self.valor:
            if self.der is None:
                self.der = Nodo(valor)
            else:
                self.der.insertar(valor)

def recorrido_in_order(nodo, elementos_ordenados):
    """Recorre el árbol de izquierda a raíz a derecha."""
    if nodo is not None:
        recorrido_in_order(nodo.izq, elementos_ordenados)
        elementos_ordenados.append(nodo.valor)
        recorrido_in_order(nodo.der, elementos_ordenados)
    return elementos_ordenados

def arbol_ordenar(lista):
    """Ordena una lista utilizando un Árbol Binario de Búsqueda."""
    if not lista:
        return []
    
    # Crear la raíz con el primer elemento
    raiz = Nodo(lista[0])
    
    # Insertar el resto de los elementos
    for valor in lista[1:]:
        raiz.insertar(valor)
        
    # Extraer los elementos ordenados
    return recorrido_in_order(raiz, [])
