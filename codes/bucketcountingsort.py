#!/usr/bin/env python
# coding: utf-8

import os
import datetime
from countingsortFile import CountingSort
from bucketsortFile import BucketSort

fileNames = ['./phone1.txt', './phone2.txt', './phone3.txt']

class PhoneNumbersBucketSort():
    
    def bucketSort(self,phoneNumbers):
        print('begin')
        sorter = BucketSort(10)
        for index in range(3):
            sorter.sortViaBitIndex(phoneNumbers, 10-index)
        print('end')
    
def sortFilesTogether():
    phoneNumbers = []
    
    for fileName in fileNames:
        with open(fileName, mode='r', encoding='utf-8') as file:
            for line in file:
                s = line.strip('\n')
                phoneNumbers.append(s)
    baseSort(phoneNumbers)
    writeBack('./output.txt', phoneNumbers)
    
def baseSort(phoneNumbers):
    print('begin')
    sorter = CountingSort()
    for index in range(3):
        sorter.sortViaBitIndex(phoneNumbers, 10-index)
    print('end')

def writeBack(fileName, phoneNumbers):
    
    with open(fileName, mode='a') as file:
        for line in phoneNumbers:
            file.writelines(line+'\n')
    
def sortUsingBucket():
    
    phoneNumbers = []
    
    for fileName in fileNames:
        with open(fileName, mode='r', encoding='utf-8') as file:
            for line in file:
                s = line.strip('\n')
                phoneNumbers.append(s)
         
    sorter = PhoneNumbersBucketSort()
    sorter.bucketSort(phoneNumbers)
    writeBack('./output.txt', phoneNumbers)

    
start = datetime.datetime.now()
# sortUsingBucket()
sortFilesTogether()
end = datetime.datetime.now()

print(end - start)






