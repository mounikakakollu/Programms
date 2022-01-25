'''
Find minimum and maximum ele from an array
'''

def MinMaxEleWithLoop(array):
    min = array[0]
    max = array[0]
    i = 0
    j = len(array) -1
    while(i<j):
        if(array[i] < min):
            min = array[i]
        elif(array[i] > max):
            max = array[i]
        if (array[j] < min):
            min = array[j]
        elif (array[j] > max):
            max = array[j]
        i+=1;
        j-=1
    return min, max

def MinMaxEleWithOutLoop(array, index, min, max):
    if(index>=len(array)):
        return min, max
    if(min > array[index]):
        min = array[index]
    if(max < array[index]):
        max = array[index]
    return MinMaxEleWithOutLoop(array, index+1, min, max)

if __name__ == '__main__':
    array = list(map(int, input().strip().split()))

    print("Find minimum and maximum ele using loop")
    print(MinMaxEleWithLoop(array))

    print("Find minimum and maximum ele without using loop")
    print(MinMaxEleWithOutLoop(array, 0, array[0], array[0]))