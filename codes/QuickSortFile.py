#!/usr/bin/env python
# coding: utf-8

# In[9]:


class QuickSort():
    
    def swap(self,inList, p, q):
        tmp = inList[p]
        inList[p] = inList[q]
        inList[q] = tmp
    
    def quickPartition(self,inList, p, r):
        i = p
        for j in range(p, r):
            if inList[j] < inList[r]:
                self.swap(inList, i, j)
                i = i+1
    
        if inList[i] > inList[r]:
            self.swap(inList, i, r)
        return i

    def quickSort(self,inList, p, r):
        if p >= r:
            return
    
        q = self.quickPartition(inList, p, r)
        self.quickSort(inList, p, q-1)
        self.quickSort(inList, q+1,r)
        
    def queryKthEelement(self,inList, p, r, k):
    
        q = self.quickPartition(inList, p, r)
        if q == k:
            return inList[q]
        if q < k:
            return self.queryKthEelement(inList, q+1, r, k)
        if q > k:
            return self.queryKthEelement(inList, p, q-1, k)
        
# sorter = QuickSort()
#
# # inList = [4,7,1,3,6,10,2,5,8,8,9]
# # inList = ['18610310797', '18610310543', '18610310351', '18610310852', '18610310319', '18610310587', '18610310146', '18610310038',
# #           '18610310309', '18610310611']
# inList = [18610310797, 18610310543, 18610310351, 18610310852, 18610310319, 18610310587, 18610310146, 18610310038,
#           18610310309, 18610310611]
# print(inList)
# sorter.quickSort(inList, 0, 9)
# print(inList,'end')
# # print(sorter.queryKthEelement(inList, 0, 9, 2))







