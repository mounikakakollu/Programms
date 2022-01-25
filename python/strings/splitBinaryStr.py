'''
Split the binary string into substrings with equal number of 0s and 1s

Input: str = “0100110101”
Output: 4
The required substrings are “01”, “0011”, “01” and “01”.
Input: str = “0111100010”
Output: 3

'''


class splitBinaryStr:
    def splitBinaryStr(self, binary):
        count1 = 0
        count0 = 0
        result = []
        start = 0
        end = 0
        for i in range(len(binary)):
            if(binary[i] == '0'):
                count0 +=1
            else:
                count1 +=1
            end+=1
            if(count1 == count0):
                result.append(binary[start:end])
                start = end
                count0 = 0
                count1 = 0
        return result

if __name__ == '__main__':
    obj = splitBinaryStr()
    binary = "0100110101"
    print(obj.splitBinaryStr(binary))