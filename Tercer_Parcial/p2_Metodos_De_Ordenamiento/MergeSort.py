from array import array
def importar_lista(archivo):
    lista = []
    with open(archivo) as tf:
        lines = tf.read().split('","')
    for line in lines:
        lista.append(line)
    return lista
def ordenar(lista):
    tamano_de_lista = len(lista)
    lista_temporaria = [0] * tamano_de_lista
    merge_sort(lista, lista_temporaria, 0, tamano_de_lista - 1)
def merge_sort(lista, lista_temporaria, inicio, fin):
    if inicio < fin:
        medio = (inicio + fin) // 2
        merge_sort(lista, lista_temporaria, inicio, medio)
        merge_sort(lista, lista_temporaria, medio + 1, fin)
        merge(lista, lista_temporaria, inicio, medio + 1, fin)
def merge(lista, lista_temporaria, inicio, medio, fin):
    fi_primera_parte = medio - 1
    indince_temporario = inicio
    tamano_de_lista = fin - inicio + 1
    while inicio <= fin_primera_parte and medio <= fin:
        if lista[inicio] <= lista[medio]:
            lista_temporaria[indice_temporario] = lista[inicio]
            inicio += 1
        else:
            lista_temporaria[indice_temporario] = lista[medio]
            medio += 1
        indice_temporario += 1
    while inicio <= fin_primera_parte:
        lista_temporaria[indice_temporario] = lista[inicio]
        indice_temporario += 1
        inicio += 1
    while medio <= fim:
        lista_temporaria[indice_temporario] = lista[medio]
        indice_temporario += 1
        medio += 1
    for i in range(0, tamano_de_lista):
        lista[fin] = lista_temporaria[fin]
        fin -= 1
def main():
    lista_de_alumnos = importa_lista('../data/lista_alumnos')
    ordenar(lista_de_alumnos)
    for nombre in lista_de_alumnos:
        print(nombre)
if __name__ == "__main__":
    main()