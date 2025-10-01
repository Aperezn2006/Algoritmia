import time 
 
# PYTHON BASICO Y TIEMPO DE EJECUCION

def dataprep(n):
    return list(range(n))

def time_measure(f, dataprep, Nlst, Nrep=1000, Nstat=100):
    return 

def search_all(lst, v):
    l = list()
    for i, value in enumerate(lst):
        if v == value:
            l.append(i+1)
    return l

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

def bubble_sort(lst, orden):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if (orden == True and lst[j] > lst[j+1]) or (orden == False and lst[j] < lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

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
