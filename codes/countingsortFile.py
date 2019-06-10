
import random
import datetime
import itertools

class CountingSort():
    
    def sort(self,inList):
        if len(inList) <=1:
            return
        
        countingList = [0]*(max(inList)+1)
        
        for x in inList:
            countingList[(int)(x)] += 1
        
        countingList = list(itertools.accumulate(countingList))
    
        tmp = [0]*len(inList)
        
        for x in reversed(inList):
            tmp[countingList[(int)(x)]-1] = x
            countingList[(int)(x)] -= 1
    
        inList[:] = tmp

    def sortViaBitIndex(self,inList ,bitIndex):
    
        max = 9
        countingList = [0]*(max+1)

        for x in inList:
            countingList[(int)(x[bitIndex])] += 1
        countingList = list(itertools.accumulate(countingList))
    
        tmp = [0]*len(inList)
        
        for x in reversed(inList):
            tmp[countingList[(int)(x[bitIndex])]-1] = x
            countingList[(int)(x[bitIndex])] -= 1

        inList[:] = tmp
  
if __name__ == "__main__":
    inList = [random.randint(1,120) for x in range(0,10)]
    print(inList)
    sorter = CountingSort()
    print(sorter.sort(inList))
    print(inList)

