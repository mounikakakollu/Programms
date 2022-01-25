'''
Implementing fractional KnapSack. Here we can take fractional part of item from the toltal(means we can cut an item)

Algorithm
1. Val = [values of items]
2. wt = [weight of items]
3  W = knapsack capacity
4  calculate ratio of the val/wt
5  sort it
6 traverse the ratio sorted array and calculate the max value
'''

arr = [[100, 20],[60, 10], [120, 30]]
W = 50

# Calulating ratios and append the ratio to the 0th index of every subarray of arr
for i in arr:
    i.insert(0, i[0]/i[1])
arr.sort(reverse=True)
print(arr)

currCapacity = 0
maxVal = 0
i = 0
while(i<len(arr)):
    if(currCapacity + arr[i][2]<=W):
        currCapacity += arr[i][2]
        maxVal += arr[i][0]*arr[i][2]
        i+=1
    else:
        break
# print(maxVal, currCapacity, i)
if(currCapacity < W):
    maxVal += ((W - currCapacity) / arr[i][2]) * arr[i][1]
    currCapacity+= (W-currCapacity)
print(maxVal, currCapacity)