'''
Find n ugly numbers
'''

n = 15
uglyNums = [1]
i2 = 0
i3 = 0
i5 = 0
for i in range(15):
    next2 = uglyNums[i2]*2
    next3 = uglyNums[i3]*3
    next5 = uglyNums[i5]*5
    uglyNums.append(min(next2, next3, next5))
    if(uglyNums[-1] == next2):
        i2+=1
    if(uglyNums[-1] == next3):
        i3+=1
    if(uglyNums[-1] == next5):
        i5+=1
print(uglyNums)