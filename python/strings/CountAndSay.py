'''
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character. Then for each group, say the number of characters, then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.

For example, the saying and conversion for digit string "3322251":

Example
Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
'''

class CountAndSay:
    def countAndSay(self, n):
        result = "1"
        if(n == 1):
            return result
        elif(n == 0):
            return 0
        for i in range(n-1):
            print(result)
            tmp = int(result)
            result = ""
            # prev = tmp%10
            # tmp = int(tmp/10)
            # count = 1
            prev = -1
            while(tmp):
                rem = tmp % 10
                if(prev == -1):
                    prev = rem
                    count = 0
                if(rem == prev):
                    count+=1
                else:
                    result = str(count) + str(prev) + result
                    prev = rem
                    count = 1
                tmp = int(tmp/10)
                if(not tmp):
                    result = str(count) + str(prev) + result
        return result

if __name__ == '__main__':
    obj = CountAndSay()
    n = 5
    print(obj.countAndSay(n))