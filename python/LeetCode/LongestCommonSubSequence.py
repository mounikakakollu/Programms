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

print(longestCommonSubsequence(s1, s2))