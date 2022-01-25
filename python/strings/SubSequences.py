'''
Find all subSequences in a given strings (all combinations)
'''

'''
abcd
a, b, c, d, ab, abc, abcd, bc, bcd, cd
'''

class SubSequence:
    def findSubSequences(self, word):
        result = list(word)
        for i in range(len(word)):
            j = i+1
            while(j<len(word)):
                result.append(word[i:j+1])
                j+=1
        print(result)

if __name__ == '__main__':
    obj = SubSequence()
    print(obj.findSubSequences("abcd"))