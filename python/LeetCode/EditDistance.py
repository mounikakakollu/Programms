def editDistance(str1, str2, memory={}):
    key = str1 + "-" + str2
    if(key in memory):
        return memory[key]
    if(len(str1)==0):
        return len(str2)
    if(len(str2) ==0):
        return len(str1)
    if(str1[-1] == str2[-1]):
        tmp = editDistance(str1[:-1],str2[:-1])
    else:
        tmp = 1 + min(editDistance(str1, str2[:-1]), editDistance(str1[:-1], str2), editDistance(str1[:-1], str2[:-1]))
    memory[key] = tmp
    return tmp

str1 = "intention"
str2 = "execution"
print(editDistance(str1, str2))