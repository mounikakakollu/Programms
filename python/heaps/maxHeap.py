def heapify(heap, i):
    if(int((i-1))/2 <0):
        return heap

    elif(heap[int((i-1)/2)] < heap[i]):
        tmp = heap[int((i-1)/2)]
        heap[int((i-1)/2)] = heap[i]
        heap[i] = tmp
        return heapify(heap, int((i-1)/2))
    else:
        return heap

def insertion(heap, ele):
    heap.append(ele)
    return heapify(heap, len(heap)-1)
heap = [4,5]
# print(insertion(heap, 7))
# print(insertion(heap, 6))
# print(insertion(heap, 4))
# print(insertion(heap, 5))
print(insertion(heap, 2))
# print(insertion(heap, 13))
# print(insertion(heap, 17))