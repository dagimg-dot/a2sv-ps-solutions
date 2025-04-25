"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head

        while curr:
            if curr.child == None:
                curr = curr.next
                continue
            
            temp = curr.child
            while temp.next != None:
                temp = temp.next
            
            temp.next = curr.next
            if curr.next != None:
                curr.next.prev = temp

            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None

        return head