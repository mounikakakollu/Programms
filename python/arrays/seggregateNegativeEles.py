'''
Move all the negative elements to one side of the array
'''

def seggregateNegativesWithoutOrder(array):
    i=0
    j = len(array)-1
    while(i<j):
        while(array[i]<0):
            i+=1
        while(array[j]>=0):
            j-=1
        if(i<j):
            array[i], array[j] = array[j], array[i]
# def seggregateNegatives(array):
#     i = 0
#     while(i<len(array)):
#         while(array[i]<0):
#             i+=1
#         pos = i;
#         while(array[i])
array = [1,2,3,4,-5,3,-6,-7,10]
seggregateNegativesWithoutOrder(array)
print(array)
# array = [1,2,3,4,-5,3,-6,-7,10]
# seggregateNegatives(array)
# print(array)