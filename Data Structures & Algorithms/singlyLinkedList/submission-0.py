from typing import List

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val
    
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        
        if self.head is None:
            # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            # Non-empty list
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
    
    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        
        if self.tail is None:
            # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            # Non-empty list
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
    
    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        
        if index == 0:
            # Remove head
            self.head = self.head.next
            if self.length == 1:
                # List becomes empty
                self.tail = None
        else:
            # Find node before the one to remove
            curr = self.head
            for i in range(index - 1):
                curr = curr.next
            
            # Remove the target node
            curr.next = curr.next.next
            
            # Update tail if removing last node
            if index == self.length - 1:
                self.tail = curr
        
        self.length -= 1
        return True
    
    def getValues(self) -> List[int]:
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result