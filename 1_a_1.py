import time 
import random
import statistics
 
# PYTHON BASICO Y TIEMPO DE EJECUCION



"""
Busca todas las ocurrencias de un valor en una lista y devuelve una lista con las posiciones (basadas en 1) donde se encuentra.

Args:
    lst (list): Lista en la que se buscará el valor.
    v (any): Valor a buscar en la lista.

Returns:
    list: Lista de posiciones (basadas en 1) donde el valor se encuentra en la lista original.
"""
def search_all(lst, v):
  
    l = list()
    for i, value in enumerate(lst):
        if v == value:
            l.append(i+1)
    return l

print("##################search all#####################")
print(search_all([1,2,3,4,5,1,2,3,4,5], 3))
print(search_all([1,2,3,4,5,1,2,3,4,5], 6))
print(search_all([1,2,3,4,5,1,2,3,4,5], 1))
print(search_all([], 1))
print(search_all([1,1,1,1,1], 1))
print(search_all([1,1,1,1,1], 2))
print(search_all([1], 1))
print()


# ELEMENTO MAYORITARIO


"""
Determines the majority element in a list, if it exists.

A majority element is an element that appears more than half the times in the list.
This function uses a variation of the Boyer-Moore Voting Algorithm to find a candidate,
then verifies if the candidate is indeed the majority element.

Args:
    lst (list): The list of elements to check.

Returns:
    The majority element if one exists, otherwise None.
"""
def majority_element(lst):
    
    max_reps = max (lst, key=lst.count)
    candidate = lst[0]
    count = 0
    for i, value in enumerate(lst):
        if value == candidate:
            count+=1
        else:
            count-=1
            if count == 0:
                candidate = value
    if (max_reps == candidate): 
        return candidate
    else: 
        return None
    
# SORTS

"""
    Sorts a list using the bubble sort algorithm.

    Args:
        lst (list): The list of elements to be sorted.
        orden (bool): If True, sorts the list in ascending order; if False, sorts in descending order.

    Returns:
        list: The sorted list.

    Example:
        bubble_sort([3, 1, 2], True)  # Returns [1, 2, 3]
        bubble_sort([3, 1, 2], False) # Returns [3, 2, 1]
"""
def bubble_sort(lst, orden):
    
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if (orden == True and lst[j] > lst[j+1]) or (orden == False and lst[j] < lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print("##################bubble sort#####################")
print(bubble_sort([64, 34, 25, 12, 22, 11, 90], True))

"""
    Sorts a list in ascending or descending order using the merge sort algorithm.

    Parameters:
        lst (list): The list of elements to be sorted.
        order (bool): If True, sorts in ascending order; if False, sorts in descending order.

    Returns:
        list: The sorted list.
"""
def merge_sort(lst, order):
  
    if len(lst) > 1:
        mid = len(lst) // 2
        L = lst[:mid]
        R = lst[mid:]

        merge_sort(L, order)
        merge_sort(R, order)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if (order == True and L[i] < R[j]) or (order == False and L[i] > R[j]):
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1
    return lst

# HEAPS
  
"""
    Reorganiza un heap para mantener la propiedad de heap máximo a partir de un índice dado.
    Args:
        h (list): Lista que representa el heap.
        i (int): Índice del nodo a partir del cual se aplica heapify.
    Returns:
        list: El heap reorganizado manteniendo la propiedad de heap máximo.
    Nota:
        La función asume que los subárboles izquierdo y derecho de 'i' ya son heaps.
"""
def heap_heapify (h,i):
    
    father = i
    left = 2*i+1
    right = 2*i+2

    max_son = father

    if right < len(h) and h[right] > h[max_son]:
        max_son = right

    if left < len(h) and h[left] > h[max_son]:
        max_son = left

    if max_son != father:
        h[max_son], h[father]=h[father], h[max_son]
        heap_heapify (h, max_son)
    
    return h

"""
    Inserta un elemento en un heap (montículo) máximo representado como una lista.

    Args:
        h (list): Lista que representa el heap máximo.
        key (int or float): Elemento a insertar en el heap.

    Returns:
        list: El heap actualizado después de insertar el nuevo elemento.

    El algoritmo añade el elemento al final del heap y lo intercambia hacia arriba
    hasta restaurar la propiedad de heap máximo.
"""
def heap_insert (h, key):
    
    pos = len(h)
    h.append(key)

    while pos > 0:
        if h[pos] > h[(pos-1) // 2]:
            h[pos], h[(pos-1) // 2] = h[(pos-1) // 2], h[pos]
            pos = (pos-1) // 2
        else:
            break
    return h 

def heap_extract (h):
    if len(h) == 0:
        return IndexError ("Heap is empty")

    extracted = h[0]
    
    h[0] = h[len(h)-1]
    h.pop()

    if len(h) > 0:
        heap_heapify (h, 0)

    return (h, extracted)

def heap_create (h):
    i = (len (h)// 2) - 1
    while (i >= 0):
        heap_heapify(h, i)
        i -= 1
    return h

# COLAS DE PRIORIDAD SOBRE MAX HEAP

def pq_ini ():
    lst = []
    return heap_create(lst)



def pq_insert(h, key):
    return heap_insert (h,key)


def pq_extract(h):
    return heap_extract (h)




# Prepara una permutacion de una lista de tamaño n con valores secuenciales de 1 a n
def dataprep_(n):
    xs = list(range(1, n+1))
    random.shuffle(xs)
    return (xs, True)


"""
Mide el tiempo de ejecución de una función `f` con datos preparados por `dataprep` para diferentes tamaños de entrada.

Args:
    f (function): Función a medir.
    dataprep (function): Función para preparar los datos de entrada.
    Nlst (list): Lista de tamaños de entrada para preparar los datos.
    Nrep (int): Número de repeticiones para cada tamaño de entrada.
    Nstat (int): número de repeticiones con entradas distintas de la misma dimensión para la valoración estadística
    (véase en apéndice)

Returns:
    list: Lista de tuplas con el tamaño de entrada y el tiempo promedio de ejecución.
"""
def time_measure(f, dataprep, Nlst, Nrep, Nstat):
    tiempos = []
    medias = []
    varianzas = []
    tupla=()
    lista_tuplas = []    


    for n in Nlst:
        datos = dataprep(n)
        for _ in range(Nstat):
            tiempos_temp = []
            for _ in range(Nrep):
                inicio = time.perf_counter()
                f(*datos)
                fin = time.perf_counter()
                tiempos_temp.append(fin - inicio)
            tiempos.append(statistics.mean(tiempos_temp))
        media = statistics.mean(tiempos)
        varianza = statistics.variance(tiempos)

        medias.append(media)
        varianzas.append(varianza)
        
        tupla = (n, media, varianza)
        tiempos = []
        lista_tuplas.append(tupla)

    return lista_tuplas

print("##################time measure#####################")
print(time_measure(bubble_sort, dataprep_, [10, 100, 1000], 10, 5))
print() 