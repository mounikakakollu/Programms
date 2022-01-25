'''
Given two strings str1 and str2 and below operations that can performed on str1.
Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
'''

def editDistance(str1, str2, n, m, memory={}):
    if(m == 0):
        return n
    if(n == 0):
        return m
    key = str(m) + "-" + str(n)
    if(key in memory):
        return memory[key]
    if(str1[n-1] == str2[m-1]):
        tmp = editDistance(str1, str2, n-1, m-1, memory)
    else:
        tmp = 1+ min(
                editDistance(str1, str2, n, m-1, memory), #Insert
                editDistance(str1, str2, n-1, m, memory), #Delete
                editDistance(str1, str2, n-1, m-1, memory) #Replace
              )
    memory[key] = tmp
    return tmp
# str1 = "sunday"
# str2 = "saturday"

def findeditDistance( s, t, m, n, memory={}):
    if (m == 0):
        return n
    if (n == 0):
        return m
    key = str(m) + "-" + str(n)
    if (key in memory):
        return memory[key]
    if (s[m - 1] == t[n - 1]):
        tmp = findeditDistance(s, t, m - 1, n - 1, memory)
    else:
        tmp = 1 + min(
            findeditDistance(s, t, m, n - 1, memory),  # Insertion
            findeditDistance(s, t, m - 1, n - 1, memory),  # Replace
            findeditDistance(s, t, m - 1, n, memory)  # Deletion
        )
    memory[key] = tmp
    return tmp

class Solution:
    def minDistance(self, word1: str, word2: str, memory = {}) -> int:
        if(len(word1) == 0):
            return len(word2)
        elif(len(word2) == 0):
            return len(word1)
        key = str(len(word1)) + "_" + str(len(word2))
        if(key in memory):
            return memory[key]
        if(word1[-1] == word2[-1]):
            tmp = self.minDistance(word1[:-1], word2[:-1])
        else:
            tmp = 1+min(
                self.minDistance(word1[:-1], word2[:-1]),
                self.minDistance(word1, word2[:-1]),
                self.minDistance(word1[:-1], word2)
            )
        memory[key] = tmp
        return tmp

str1 = "intention"
str2 = "execution"
obj = Solution();
print(obj.minDistance(str1, str2))
print(obj.minDistance(str1, str2))

