'''
Find duplicate Characters in a string
'''

class DuplicateChars:
    def findDuplicateChars(self, stri):
        chars = []
        stri = stri.lower()
        for i in range(26):
            chars.append(0)
        for i in stri:
            chars[ord(i)-97] += 1
        for i in range(len(chars)):
            if(chars[i]>=2):
                print(chr(i+97) + " : " + str(chars[i]))
        print()

if __name__ == '__main__':
    obj = DuplicateChars()
    stri = "GeeksForGeeks"
    obj.findDuplicateChars(stri)