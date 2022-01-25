'''
Reverse the given array using loops and without loops
'''

def reverseProgramWithLoop(array):
    i = 0;
    j = len(array) -1
    print(j)
    while(i<j):
        array[i] = array[i] + array[j];
        array[j] = array[i] - array[j];
        array[i] = array[i] - array[j];
        i+=1;
        j-=1;
    return array

def reverseProgramWithOutLoop(array, start, end):
    if(start>=end):
        return array
    array[start] = array[start] + array[end];
    array[end] = array[start] - array[end];
    array[start] = array[start] - array[end];
    return reverseProgramWithOutLoop(array, start+1, end-1)



if __name__ == '__main__':
    array = list(map(int,input().strip().split()))
    print("Reverse the list using loops")
    print(reverseProgramWithLoop(array))

    print("Reverse the list without using loops")
    print(reverseProgramWithOutLoop(array, 0, len(array)-1))
