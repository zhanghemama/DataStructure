#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import datetime

class CountingSort():
    
    def getIndex(self, x):
        return (int)(x)
        
    def sort(self,inList):
        if len(inList) <=1:
            return
        
        max = inList[0]
        for x in inList:
            if x > max:
               max = x
            
        countingList = [0]*(max+1)
        
        for x in inList:
            countingList[self.getIndex(x)] = countingList[self.getIndex(x)] + 1
        
        for x in range(1,max+1):
            countingList[x] = countingList[x] + countingList[x-1]
    
        tmp = [0]*len(inList)
        
        for x in inList[::-1]:
            tmp[countingList[self.getIndex(x)]-1] = x
            countingList[self.getIndex(x)] = countingList[self.getIndex(x)] - 1
    
        for x in range(len(tmp)):
            inList[x] = tmp[x]

    def sortViaBitIndex(self,inList ,bitIndex):
    
        max = 9
        countingList = [0]*(max+1)
        for x in inList:
            countingList[self.getIndex(x[bitIndex])] = countingList[self.getIndex(x[bitIndex])] + 1

        for x in range(1,max+1):
            countingList[x] = countingList[x] + countingList[x-1]
    
        tmp = [0]*len(inList)
        
        for x in inList[::-1]:
            tmp[countingList[self.getIndex(x[bitIndex])]-1] = x
            countingList[self.getIndex(x[bitIndex])] = countingList[self.getIndex(x[bitIndex])] - 1

        for x in range(len(tmp)):
            inList[x] = tmp[x]
    
inList = [random.randint(1,120) for x in range(0,10)]
print(inList)
sorter = CountingSort()
print(sorter.sort(inList))
print(inList)


# In[ ]:




