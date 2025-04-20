# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        answer = [None] * k
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        part_size = count // k
        rem = count % k

        curr = head
        prev = None

        i = 0
        while curr and i < k:
            answer[i] = curr
            for j in range(part_size):
                prev = curr
                curr = curr.next
            
            if rem > 0:
                prev = curr
                curr = curr.next
                rem -= 1

            i += 1

            
            prev.next = None
        
        return answer