
import random
    
class BucketSort():
    def __init__(self,bucketsNumber):
        self.bucketsNumber = bucketsNumber
    
    def sort(self, inList):
        buckets = []
        for x in range(0, self.bucketsNumber):
            buckets.append([])

        for x in inList:
            buckets[(int)(x)].append(x)

        inList.clear()
        for x in range(0, self.bucketsNumber):
            [inList.append(y) for y in buckets[x]]
            
    def sortViaBitIndex(self, inList, index):
        
        buckets = [] 
        for x in range(0, self.bucketsNumber):
            buckets.append([])
        
        for x in inList:
            bucketIndex = (int)(x[index])
            buckets[bucketIndex].append(x)
            
        inList.clear()    
        for x in range(0, self.bucketsNumber):
            [inList.append(y) for y in buckets[x]]
            
# inList = [random.randint(1,120) for x in range(0,1000)]
# print(inList)
# sorter = BucketSort(120)
# sorter.sort(inList)
# print(inList)




