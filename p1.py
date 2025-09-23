import time 

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
    candidate = lst[0]
    count = 0
    for i, value in enumerate(lst):
        if value == candidate:
            count+=1
        else:
            count-=1
            if count == 0:
                candidate = value
    value.
