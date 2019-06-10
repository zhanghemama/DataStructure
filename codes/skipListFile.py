import random
from typing import Optional

class Node():

    def __init__(self,data:Optional[int] = None):
        self.data = data
        self.forwards = []

class SkipList():
    Max_Level = 16

    def __init__(self):
        self.actualLevel = 1
        self.head = Node()
        self.head.forwards = [None]*self.Max_Level

    def randomLevel(self) -> int:
        level = random.randint(1, self.Max_Level)
        if (level + 1)%2 == 0:
            level = level + 1

        return level

    def find(self,value:int) -> Optional[Node]:

        p = self.head
        for level in reversed(range(self.actualLevel)):
            while p.forwards[level] != None and p.forwards[level].data < value:
                p = p.forwards[level]

        return p.forwards[0] if p.forwards[0] != None and p.forwards[0].data == value else None

    def insert(self, value:int):
        level = self.randomLevel()
        update = [self.head]*level

        p = self.head
        for index in reversed(range(level)):
            while p.forwards[index] != None and p.forwards[index].data < value:
                p = p.forwards[index]
            update[index] = p

        newNode = Node(value)
        newNode.forwards = [None]*level
        for index in range(0, level):
            newNode.forwards[index] = update[index].forwards[index]
            update[index].forwards[index] = newNode

        if self.actualLevel < level:
            self.actualLevel = level

    def delete(self, value:int):

        update = [None]*self.actualLevel

        p = self.head
        for level in reversed(range(self.actualLevel)):
            while p.forwards[level] != None and p.forwards[level].data < value:
                p = p.forwards[level]
            update[level] = p

        if p.forwards[0] != None and p.forwards[0].data == value:
            for level in range(0, self.actualLevel):
                if update[level].forwards[level] != None and update[level].forwards[level].data == value:
                    update[level].forwards[level] = update[level].forwards[level].forwards[level]

    def __repr__(self) ->str:

        values = []
        p = self.head
        while p.forwards[0] != None:
            values.append(str(p.forwards[0].data))
            p = p.forwards[0]
        return '->'.join(values)

if __name__ == '__main__':
    skipList = SkipList()
    skipList.insert(5)
    skipList.insert(1)
    skipList.insert(7)
    skipList.insert(8)
    skipList.insert(10)
    skipList.insert(9)
    skipList.insert(3)
    skipList.insert(4)
    skipList.insert(18)
    skipList.insert(17)
    skipList.insert(13)
    skipList.insert(16)
    print(skipList)
    p = skipList.find(7)
    print(p.data)
    skipList.delete(7)
    p = skipList.find(7)
    print(p)
