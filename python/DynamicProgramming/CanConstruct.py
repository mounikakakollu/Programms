'''
Given an array of strings and a target. Find whether can we construct the target from the given array
'''


class CanConstruct:
    def canConstruct(self, words, target,possibilities = {}):
        if(target in possibilities):
            return possibilities[target]
        if(target == ""):
            return True
        for i in words:
            if(i in target  and target.index(i) == 0):
                index = target.index(i)
                if(self.canConstruct(words, target[:index] + target[index+len(i):])):
                    possibilities[target] = True
                    return True
        possibilities[target] = False
        return False

    def FindwordsWhichAreUsedToConstructTart(self, words, target,possibilities = {}):
        if(target in possibilities):
            return possibilities[target]
        if(target == ""):
            return []
        for i in words:
            if(i in target and target.index(i) == 0):
                index = target.index(i)
                tmp = self.FindwordsWhichAreUsedToConstructTart(words, target[:index] + target[index+len(i):])
                if(tmp is not None):
                    tmp.append(i)
                    possibilities[target] = tmp
                    return tmp
        possibilities[target] = None
        return None

    def FindwordsWhichAreUsedToConstructTartAllWays(self, words, target,possibilities = {}):
        if(target in possibilities):
            return possibilities[target]
        if(target == ""):
            return [[]]
        result = []
        for i in words:
            if(i in target and target.index(i) == 0):
                print("i=", i, end = " ")
                index = target.index(i)
                tmp = self.FindwordsWhichAreUsedToConstructTartAllWays(words, target[:index] + target[index+len(i):])
                if(tmp is not None and len(tmp) == 1):
                    print("i " + target, possibilities,tmp, end=" ")
                    tmp[0].append(i)
                    possibilities[target] = tmp
                    # result += tmp
                else:
                    for j in tmp:
                        print("j=" + j, target, possibilities, tmp, end=" ")
                        j+=i
                    possibilities[target] = tmp
                print( possibilities, tmp)

        if(target not in possibilities):
            possibilities[target] = None
        return possibilities[target]

    def FindwordsWhichAreUsedToConstructTartWithMinWords(self, words, target,possibilities = {}):
        if(target in possibilities):
            return possibilities[target]
        if(target == ""):
            return []
        for i in words:
            if(i in target  and target.index(i) == 0):
                index = target.index(i)
                tmp = self.FindwordsWhichAreUsedToConstructTartWithMinWords(words, target[:index] + target[index+len(i):])
                if(tmp is not None):
                    tmp.append(i)
                    if(target not in possibilities):
                        possibilities[target] = tmp
                    elif(len(possibilities[target]) > len(tmp)):
                        possibilities[target] = tmp

                    # return possibilities[target]
        if(target in possibilities):
            return possibilities[target]
        else:
            possibilities[target] = None
if __name__ == '__main__':
    words = ["ab", "abc","cd", "def","abcd","ef"]
    target = "abcdef"
    # words = ["bo","rd","ate","t","aka","sk","boar","d"]
    # target = "skateboard"
    obj = CanConstruct()
    # print(obj.canConstruct(words, target))
    # print(obj.FindwordsWhichAreUsedToConstructTart(words, target))
    # print(obj.FindwordsWhichAreUsedToConstructTartWithMinWords(words, target))
    print(obj.FindwordsWhichAreUsedToConstructTartAllWays(words, target))