class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedListToBin:
    def getDecimalValue(self, head: ListNode) -> int:
        ListNode current = head
        binList = []
        sum = 0

        while current is not None:
            binList.append(current.val)
            current = current.next

        binList.reverse()      
        for i,a in enumerate(binList):
            sum = sum + (2**i) * a
    
        return sum
            



