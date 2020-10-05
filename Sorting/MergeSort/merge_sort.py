import math

def merge(array, p, q, r):
    n1 = q - p 
    n2 = r - q
    left = []
    right = []
    for i in range(n1):
        left.append(array[p+i])
    for j in range(n2):
        right.append(array[q+j])
    left.append(math.inf)
    right.append(math.inf)
    i = 0
    j = 0
    for k in range(p, r):
        if left[i] <= right[j]:
            array[k] = left[i]
            i = i+1
        else:
            array[k] = right[j]
            j = j+1

def merge_sort(array, p, r):
    if p < r:
        q = math.floor((p+r)/2)
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        merge(array, p, q, r)
    
array = [3,2,1,4,5]
merge_sort(array, 0, 5)
print(array)