from QuickSortFile import QuickSort
from bucketcountingsort import PhoneNumbersBucketSort
import datetime

class BinarySearch():

    def binarySearch(self,inList,element,l,r) -> int:
        if l > r:
            return -1

        mid = l + (int)((r-l)/2)
        if element == inList[mid]:
            return mid

        if element > inList[mid]:
            return self.binarySearch(inList, element, mid + 1, r)
        else:
            return self.binarySearch(inList, element, l, mid - 1)

    def binarySearchFirstIndex(self, inList, element, l, r) -> int:
        if l > r:
            return -1

        mid = l + (int)((r-l)/2)
        if element == inList[mid]:
            if mid == 0:
                return mid
            if element == inList[mid - 1]:
                return self.binarySearchFirstIndex(inList, element, l, mid - 1)
            else:
                return mid

        if element > inList[mid]:
            return self.binarySearchFirstIndex(inList, element, mid + 1, r)
        else:
            return self.binarySearchFirstIndex(inList, element, l, mid - 1)

    def binarySearchLastIndex(self, inList, element, l, r) -> int:
        if l > r:
            return -1

        mid = l + (int)((r-l)/2)
        if element == inList[mid]:
            if mid == len(inList) - 1:
                return mid
            if element == inList[mid + 1]:
                return self.binarySearchLastIndex(inList, element, mid + 1, r)
            else:
                return mid

        if element > inList[mid]:
            return self.binarySearchLastIndex(inList, element, mid + 1, r)
        else:
            return self.binarySearchLastIndex(inList, element, l, mid - 1)

    def binarySearchInRecusiveList(self, inList, element, l, r) -> int:
        if l > r:
            return -1

        mid = l + (int)((r-l)/2)
        if element == inList[mid]:
            return mid
        if element == inList[l]:
            return l
        if element == inList[r]:
            return r

        if inList[l] > inList[mid]:
            if element > inList[mid] and element > inList[l]:
                return self.binarySearchInRecusiveList(inList, element, l, mid - 1)
            else:
                return self.binarySearch(inList, element, mid + 1, r)

        if inList[l] < inList[mid]:
            if element > inList[mid]:
                return self.binarySearchInRecusiveList(inList, element, mid + 1, r)
            else:
                return self.binarySearch(inList, element, l, mid - 1)


def getSortedPhoneNumbers(fileName):

    phoneNumbers = []
    with open(fileName, mode='r', encoding='utf-8') as file:
        for line in file:
            s = line.strip('\n')
            phoneNumbers.append(s)

    start = datetime.datetime.now()
    #     sorter = QuickSort()
    #     sorter.quickSort(phoneNumbers, 0, len(phoneNumbers)-1)
    sorter = PhoneNumbersBucketSort()
    sorter.bucketSort(phoneNumbers)
    end = datetime.datetime.now()
    print(phoneNumbers)
    return phoneNumbers

def search(phoneNumber, phoneNumbers):

    searcher = BinarySearch()
    firstIndex= searcher.binarySearchFirstIndex(phoneNumbers,phoneNumber,0, len(phoneNumbers)-1)
    lastIndex = searcher.binarySearchLastIndex(phoneNumbers,phoneNumber,0, len(phoneNumbers)-1)
    print('firstIndex',firstIndex)
    print('lastIndex',lastIndex)
    index = searcher.binarySearchInRecusiveList(phoneNumbers, phoneNumber, 0, len(phoneNumbers)-1)
    print('recuresive',index)
    recursiveList = [20,34,59,75,99,102,300,700,0,1,3,5,6,7,8,12,19]
    print(len(recursiveList))
    index = searcher.binarySearchInRecusiveList(recursiveList, 0, 0, len(recursiveList)-1)
    print(index)

if __name__ == "__main__":
    search('18610310611',getSortedPhoneNumbers('./phoneNumbers.txt'))

