'''code check the duplicates in a DLL and print the count of frequency
input=6
10
20
30
20
10
40
output:
DLL
10<-->20<-->30<-->20<-->10<-->40
duplicate values in DLL
10 appears 2 times
20 appears 2 times'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        def iae(self,data):
            newnode=Node(data):
            