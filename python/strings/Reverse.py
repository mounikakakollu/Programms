'''
Reverse a string

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''


class Reverse:
    def reverse(self, str):
        i = 0
        n = len(str)-1
        while(i<n):
            str[i], str[n] = str[n], str[i]
            i+=1
            n-=1
        return str
if __name__ == '__main__':
    obj = Reverse()
    # str = ["h","e","l","l","o"]
    str = ["H","a","n","n","a","h"]
    print(obj.reverse(str))