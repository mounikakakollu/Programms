'''
Write a Code to check whether one string is a rotation of another

str1 = ABCD
str2 = CDBA
o/p True
'''

class CheckForRotationOfStr:
    def findTwoStrsAreEqual(self, str1, str2):
        n = len(str1)
        if(n != len(str2)):
            return False
        for i in range(n):
            str1 = str1[1:] + str1[0:1]
            if(str1 == str2):
                return True
        return False

if __name__ == '__main__':
    str1 = "ABCD"
    str2 = "CDAB"
    obj = CheckForRotationOfStr()
    print(obj.findTwoStrsAreEqual(str1, str2))