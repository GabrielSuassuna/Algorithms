def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= x:
            i+=1
            aux = array[j]
            array[j] = array[i]
            array[i] = aux
    aux = array[i+1]
    array[i+1] = array[r]
    array[r] = aux
    return i+1

def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q-1)
        quicksort(array, q+1,r)

a = [5,13,2,25,7,17,20,8,4]
quicksort(a, 0, 8)
print(a)