'''
Rearrange the array in alternating positive and negative items with O(1) extra space
'''

class AlternativePosAndNegNum:
    def rearrange(self, arr):
        i = 0
        neg = 1
        while(i<len(arr)):
            if(i%2==0 and arr[i]>=0):
                i+=1
            elif(i%2==1 and arr[i]<0):
                i+=1
            else:
                if(i%2==0):
                    tmp = i+1
                    while(tmp<len(arr)):
                        if(arr[tmp]>=0):
                            arr[i], arr[tmp] = arr[tmp], arr[i]
                            break;
                        tmp+=1
                    i = i+1
                else:
                    tmp = i + 1
                    while (tmp < len(arr)):
                        if (arr[tmp] < 0):
                            arr[i], arr[tmp] = arr[tmp], arr[i]
                            break;
                        tmp+=1
                    i = i + 1

        return arr

if __name__ == '__main__':
    arr = [1,2,3,4,-1,2,-3,-4]
    obj = AlternativePosAndNegNum()
    print(obj.rearrange(arr))