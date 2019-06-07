#!/usr/bin/env python
# coding: utf-8

# In[8]:


from QuickSortFile import QuickSort
from bucketcountingsort import PhoneNumbersBucketSort
import datetime

class BinarySearch():
    
    def binarySearch(self,inList,element,l,r):
        if l > r:
            return -1
    
        mid = l + (int)((r-l)/2)
        if element == inList[mid]:
            return inList[mid]
    
        if element > inList[mid]:
            return binarySearch(inList, element, mid + 1, r)
        else:
            return binarySearch(inList, element, l, mid - 1)
    
def search(phoneNumber, fileName):
    phoneNumbers = []
    with open(fileName, mode='r', encoding='utf-8') as file:
        for line in file:
            s = line.strip('\n')
            phoneNumbers.append(s)
    
    print('begin sort')
    start = datetime.datetime.now()
    sorter = PhoneNumbersBucketSort()
    sorter.bucketSort(phoneNumbers)
    end = datetime.datetime.now()
    print(end - start)
    print('end sort')
#     sorter = QuickSort()
#     sorter.quickSort(phoneNumbers, 0, len(phoneNumbers)-1)
    searcher = BinarySearch()
    return searcher.binarySearch(phoneNumbers,phoneNumber,0, len(phoneNumbers)-1)
           
findedNumber = search('18610310611','./phoneNumbers.txt')
print(findedNumber)
# findedNumber = search('18610310601','./phoneNumbers.txt')
# print(findedNumber)


# In[ ]:





# In[ ]:





# In[ ]:




