class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # A.sort()
        i = 0
        j = len(A)-1
        maxSum = 0
        while(B>0):
            # print(A[j], A[i])
            while (i < B):
                currSum = sum(A[0:i + 1]) + sum(A[len(A)-(B-i):])
                if (maxSum < currSum):
                    maxSum = currSum
                i+=1
            return maxSum
A=[ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ]

obj = Solution()
print(obj.solve(A,48))



3
3
6
2
2
2
2
2
2
2
5