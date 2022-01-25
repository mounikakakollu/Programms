'''
Find Target sum from an array. We can take array elements as many times
7 [5,3,4,7]
possibilities
[3,4], [7]
'''

class FindTargetSum:
    def findTargetSum(self, array, target, possibilities={}):
        if(target == 0):
            return []
        elif(target<0):
            return None
        elif(target in possibilities):
            return possibilities[target]
        for i in array:
            result = self.findTargetSum(array, target-i)
            if(result is not None):
                result.append(i)
                if(target not in possibilities):
                    possibilities[target] = result
                elif(len(possibilities[target]) > len(result)):
                    possibilities[target] = result
                # return possibilities[target]  for existence of target sum returns True/ False
        if(target in possibilities):
            return possibilities[target]
        else:
            possibilities[target] = None
            return None

if __name__ == '__main__':
    obj = FindTargetSum()
    array = [5,3,4,7]
    print(obj.findTargetSum(array, 7))