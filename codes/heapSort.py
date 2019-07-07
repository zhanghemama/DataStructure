#!/usr/bin/env python
# coding: utf-8

# In[8]:


from typing import Optional

class BinaryHeap():
    
    HEAPTYPE = '<'
    def __init__(self, capacity:int):
        self.data = [0]*(capacity + 1)
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
            return data[index] < data[comparedIndex]
        if cls.HEAPTYPE == '>':
            return data[index] > data[comparedIndex]
        
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
        
        parentIndex = BinaryHeap.parent(index)

        while parentIndex > 0 and BinaryHeap.fitHeapCharacter(self.data, parentIndex, index):
            self.swap(index, parentIndex)
            index = parentIndex
            parentIndex = BinaryHeap.parent(index)
            
    def insert(self, value:int):
        
        if self.length >= self.capacity: return
        self.length += 1

        self.data[self.length] = value
        self.siftUp(self.length)
        
    def deleteMax(self)-> Optional[int]:
        
        if self.length == 0: return
        k = 1
        deletedValue = self.data[k]
        self.data[k] = self.data[self.length]
        self.length -= 1
        
        BinaryHeap.siftDown(self.data, k, self.length)
        return deletedValue
    
    @classmethod
    def buildHeap(cls, data:list, length:int):
        for i in range(length // 2, 0, -1):
            BinaryHeap.siftDown(data,i,length)
       
    @classmethod
    def sort(cls, data:list, length:int):
        
        if length == 0: return
        cls.buildHeap(data, length)
        print(data)
        k = length
        while k > 1:
            data[1], data[k] = data[k],data[1]
            k -= 1
            cls.siftDown(data,1,k)
            
    def __repr__(self):
        return self.data[1:self.length+1].__repr__()
        

if __name__ == '__main__':
    BinaryHeap.HEAPTYPE = '>'
    hp = BinaryHeap(10)
    hp.insert(3)
    hp.insert(9)
    hp.insert(1)
    hp.insert(8)
    hp.insert(7)
    hp.insert(3)
    print(hp)
    
    for _ in range(6):
        print(hp.deleteMax())
    
    a = [0, 6, 3, 4, 0, 9, 2, 7, 5, -2, 8, 1, 6, 10]
    BinaryHeap.HEAPTYPE = '<'
    hp1 = BinaryHeap(20)
    BinaryHeap.sort(a, len(a)-1)
    print(a[1:])


# In[ ]:




