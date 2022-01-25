'''
Find the Kth Minimum and Maximum element from an array
'''

def Maxheapify(heap, i):
    largest = i
    if((2*i) +1 <len(heap) and heap[(2*i)+1] > heap[largest]):
        largest = (2*i)+1
    if((2*i)+2 < len(heap) and heap[(2*i)+2] > heap[largest]):
        largest = (2*i)+2
    if largest != i :
        heap[largest], heap[i] = heap[i], heap[largest]
        Minheapify(heap, largest)
def buildMaxHeap(heap):
    lastParentNode = int((len(heap)-1)/2)
    # print(heap)
    for i in range(lastParentNode, -1,-1):
        Maxheapify(heap, i)
    # print(heap)
    return heap;

def kthMinEle(array, k):
    maxheap = []
    j = 0
    for i in array:
        if(len(maxheap) < k):
            maxheap.append(i)
            buildMaxHeap(maxheap)
            j+=1
        else:
            ele = maxheap[0]
            if(maxheap[0] > i):
                del maxheap[0]
                maxheap.append(i)
                buildMaxHeap(maxheap)
    return maxheap[0]

def Minheapify(heap, i):
    smallest = i
    if((2*i) +1 <len(heap) and heap[(2*i)+1] < heap[smallest]):
        smallest = (2*i)+1
    if((2*i)+2 < len(heap) and heap[(2*i)+2] < heap[smallest]):
        smallest = (2*i)+2
    if smallest != i :
        heap[smallest], heap[i] = heap[i], heap[smallest]
        Minheapify(heap, smallest)


def buildMinHeap(heap):
    lastParentNode = int((len(heap)-1)/2)
    for i in range(lastParentNode, -1,-1):
        # print(heap)
        Minheapify(heap, i)
    return heap;

def kthMaxEle(array, k):
    minheap = []
    j = 0
    for i in array:
        if (len(minheap) < k):
            minheap.append(i)
            buildMinHeap(minheap)
            j += 1
        else:
            ele = minheap[0]
            if (minheap[0] < i):
                del minheap[0]
                minheap.append(i)
                buildMinHeap(minheap)
        # print(minheap)
    return minheap[0]



if __name__ == "__main__":
    # array = list(map(int, input().strip().split()))
    array = [7,6,4,5,2,3,1]
    k = 3
    # k = int(input())
    print("Finding kth minimum and maximul element from given array")
    print(kthMinEle(array, k))
    print(kthMaxEle(array, k))

    # print(buildMinHeap([7,6]))