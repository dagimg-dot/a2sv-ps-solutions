"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = {None:None}
        curr = head

        while curr:
            hmap[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            cp = hmap[curr]
            cp.next = hmap[curr.next]
            cp.random = hmap[curr.random]
            curr = curr.next

        return hmap[head]