# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = []
        l2 = []
        pointer = head

        while slow:
            l1.append(slow.val)
            l2.append(pointer.val)
            slow = slow.next
            pointer = pointer.next


        l1.reverse()
        
        return l1 == l2


