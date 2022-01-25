'''
Check whether a string is palindrome or not
'''

class Palindrome:
    def checkForPalindrome(self, str): # checks with ignore case
        n = len(str)-1
        i = 0
        while(i<n):
            if(str[i].lower() != str[n].lower()):
                return False
            i+=1
            n-=1
        return True
if __name__ == '__main__':
    obj = Palindrome()
    str = "Geekskeeg"
    print(obj.checkForPalindrome(str))