'''
We have discussed Overlapping Subproblems and Optimal Substructure properties in Set 1 and Set 2 respectively.
We also discussed one example problem in Set 3.
Let us discuss Longest Common Subsequence (LCS) problem as one more example problem that can be solved using Dynamic Programming.

LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
 A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
 For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

 Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
'''

def findLongestCommonSubSequence(s1, s2, m, n, result):
    if(m <0 or n < 0):
        return 0
    if(s1[m] == s2[n]):
        result.append(s1[m])
        return 1 + findLongestCommonSubSequence(s1, s2, m-1, n-1,result)
    else:
        return max(findLongestCommonSubSequence(s1, s2, m, n-1,result), findLongestCommonSubSequence(s1, s2, m-1, n,result))

def findShortestCommonSuperSequence(s1, s2, m, n):
    if(m<0):
        return n+1
    if(n<0):
        return m+1
    # if(n<0):
    #     return m
    if(s1[m] == s2[n]):
        return 1 + findShortestCommonSuperSequence(s1, s2, m-1, n-1);
    else:
        return 1 + min(findShortestCommonSuperSequence(s1, s2, m, n-1), findShortestCommonSuperSequence(s1, s2, m-1,n))

def longestCommonSubsequence( text1: str, text2: str) -> int:
    tmp = [[0 for _ in range(len(text1) + 1)] for i in range(len(text2) + 1)]
    for i in range(1, len(text2) + 1):
        for j in range(1, len(text1) + 1):
            if (text1[j - 1] == text2[i - 1]):
                tmp[i][j] = tmp[i - 1][j-1] + 1
            else:
                tmp[i][j] = max(tmp[i - 1][j], tmp[i][j - 1])
    print(tmp)
    return tmp[len(text2)][len(text1)]
s1 = "abcba"
s2 = "abcbcba"
l1 = len(s1)-1
l2 = len(s2)-1
maxLen = 0
result = []
# print(findShortestCommonSuperSequence(s1, s2, l1, l2))
print(longestCommonSubsequence(s1, s2))