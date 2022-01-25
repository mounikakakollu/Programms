'''
Find the largest palindrome sub string

Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S).
Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S.
Incase of conflict, return the substring which occurs first ( with the least starting index).

Input:
S = "aaaabbaa"
Output: aabbaa
Explanation: The longest Palindromic
substring is "aabbaa".


Input:
S = "abc"
Output: a
Explanation: "a", "b" and "c" are the
longest palindromes with same length.
The result is the one with the least
starting index.
'''

class largestPalindromeSubStr:
    def findPalindromSubStr(self, word, start, end):
        subString = ""
        while(start>=0 and end<len(word)):
            if(word[start] == word[end]):
                subString = word[start:end + 1]
                start-=1
                end +=1
            else:
                break
        return subString

if __name__ == '__main__':
    obj = largestPalindromeSubStr()
    word = "babad"
    maxSubStr = word[0]
    for i in range(len(word)):
        subString = obj.findPalindromSubStr(word, i-1, i+1)
        if(subString and len(maxSubStr) < len(subString)):
            maxSubStr = subString
        subString = obj.findPalindromSubStr(word, i, i+1)
        if (subString and len(maxSubStr) < len(subString)):
            maxSubStr = subString
    print(maxSubStr)



