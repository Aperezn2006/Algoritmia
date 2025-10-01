def search_all(lst,v):
    return [i+1 for i, x in enumerate(lst) if x == v]

print('*******************SEARCH ALL************************')

print(search_all([1,2,3,4,5,1,2,3,4,5], 3))
# [3, 8]
print(search_all([1,2,3,4,5], 6))
# []
print(search_all([], 3))
# []
print(search_all([1,1,1,1,1], 1))
# [1, 2, 3, 4, 5]




def majority_element(lst):
    if not lst:
        return None
    count = {}
    for num in lst:
        count[num] = count.get(num, 0) + 1
        if count[num] > len(lst) // 2:
            return num
    return None


print('*******************MAJORITY ELEMENT************************')

print(majority_element([1,2,3,1,1]))
# 1
print(majority_element([1,2,3,4]))
# None
print(majority_element([]))
# None

def bubble_sort(lst, orden):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if (orden == True and lst[j] > lst[j+1]) or (orden == False and lst[j] < lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


print('*******************BUBBLE SORT************************')

print(bubble_sort([64, 34, 25, 12, 22, 11, 90], True))
# [11, 12, 22, 25, 34, 64, 90]
print(bubble_sort([64, 34, 25, 12, 22, 11, 90], False))
# [90, 64, 34, 25, 22, 12, 11]
print(bubble_sort([], True))
# []
print(bubble_sort([1], False))
# [1]


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

print('*******************MERGE SORT************************')

print(merge_sort([38, 27, 43, 3, 9, 82, 10], True))
# [3, 9, 10, 27, 38, 43, 82]
print(merge_sort([38, 27, 43, 3, 9, 82, 10], False))
# [82, 43, 38, 27, 10, 9, 3]
print(merge_sort([], True))
# []
print(merge_sort([1], False))
# [1]

def heap_heapify(h, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < len(h) and h[left] > h[largest]:
        largest = left
    if right < len(h) and h[right] > h[largest]:
        largest = right
    if largest != i:
        h[i], h[largest] = h[largest], h[i]
        heap_heapify(h, largest)

def heap_insert(h, key):
    h.append(key)
    i = len(h) - 1
    while i != 0 and h[(i - 1) // 2] < h[i]:
        h[i], h[(i - 1) // 2] = h[(i - 1) // 2], h[i]
        i = (i - 1) // 2

def heap_extract(h):
    if len(h) == 0:
        return None
    root = h[0]
    h[0] = h[-1]
    h.pop()
    heap_heapify(h, 0)
    return root


def heap_create(h):
    for i in range(len(h) // 2 - 1, -1, -1):
        heap_heapify(h, i)
    return h
