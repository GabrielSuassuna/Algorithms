import math
class HeapSort(object):
    def __init__(self, array):
        self.heap_size = len(array)
        self.array = array
        self.heapsort(self.array)
    
    def parent(self, i):
        return math.floor(i/2)
    
    def left(self, i):
        return 2*i + 1
    
    def right(self, i):
        return 2*i + 2
    
    def lenght(self):
        return len(self.array)
    
    def max_heapify(self, array, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size and array[l]>array[i]:
            maior = l
        else:
            maior = i
        if r < self.heap_size and array[r]>array[maior]:
            maior = r
        if maior != i:
            aux = array[i]
            array[i] = array[maior]
            array[maior] = aux
            self.max_heapify(array, maior)
    
    def build_max_heap(self, array):
        for i in range(math.floor(self.heap_size/2), -1, -1):
            self.max_heapify(array, i)
    
    def heapsort(self, array):
        self.build_max_heap(array)
        for i in range(len(array)-1, 0, -1):
            aux = array[0]
            array[0] = array[i]
            array[i] = aux
            self.heap_size -= 1
            self.max_heapify(array,0)