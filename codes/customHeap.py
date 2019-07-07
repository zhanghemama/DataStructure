#!/usr/bin/env python
# coding: utf-8

# In[31]:


from typing import Optional

class HeapNode():
    def __init__(self, data, index):
        self.data = data
        self.index = index
        
class CustomBinaryHeap():
    
    HEAPTYPE = '<'
    def __init__(self, capacity:int):
        self.data = [None]*(capacity + 1)
        self.capacity = capacity
        self.length = 0
        
    @classmethod
    def parent(cls, index:int) -> int:
        return index // 2
    
    @classmethod
    def left(cls, parentIndex:int) -> int:
        return 2 * parentIndex
    
    @classmethod
    def right(cls, parentIndex:int) -> int:
        return 2 * parentIndex + 1
    
    @classmethod
    def fitHeapCharacter(cls, data:list, index, comparedIndex):
        if cls.HEAPTYPE == '<':
            return data[index].data < data[comparedIndex].data
        if cls.HEAPTYPE == '>':
            return data[index].data > data[comparedIndex].data
        
    def swap(self,i:int, j:int):
        if i > self.length:
            return
        
        if j > self.length:
            return
        
        self.data[i], self.data[j] = self.data[j], self.data[i]
        
    @classmethod
    def siftDown(cls, data:list, index, length):
        if index < 1:
            return
        
        maxPos = index
        while True:
            if cls.left(index) <= length and cls.fitHeapCharacter(data, index, cls.left(index)):
                maxPos = cls.left(index)
            if cls.right(index) <= length and cls.fitHeapCharacter(data, maxPos, cls.right(index)):
                maxPos = cls.right(index)
            
            if maxPos == index: break
   
            data[index], data[maxPos] = data[maxPos],data[index]

            index = maxPos

    def siftUp(self, index:int):
        
        parentIndex = CustomBinaryHeap.parent(index)
        while parentIndex > 0 and CustomBinaryHeap.fitHeapCharacter(self.data, parentIndex, index):
            self.swap(index, parentIndex)
            index = parentIndex
            parentIndex = CustomBinaryHeap.parent(index)
            
    def insert(self, value:HeapNode):
        
        if self.length >= self.capacity: return
        self.length += 1

        self.data[self.length] = value
        self.siftUp(self.length)
        
    def deleteMax(self)-> Optional[HeapNode]:
        
        if self.length == 0: return
        k = 1
        deletedValue = self.data[k]
        self.data[k] = self.data[self.length]
        self.length -= 1
        
        CustomBinaryHeap.siftDown(self.data, k, self.length)
        return deletedValue
            
    def print(self):
        for i in range(1,self.length+1):
            print(self.data[i].data)
    
if __name__ == '__main__':
    hp = CustomBinaryHeap(10)
    hp.insert(HeapNode('mm',0))
    hp.insert(HeapNode('nn',0))
    hp.insert(HeapNode('aa',0))
    hp.insert(HeapNode('pp',0))
    hp.insert(HeapNode('g',0))
    hp.insert(HeapNode('e',0))
    hp.print()


# In[ ]:





# In[ ]:




