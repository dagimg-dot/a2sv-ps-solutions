/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteMiddle(head *ListNode) *ListNode {
    if (head.Next == nil) {
        return nil
    }
    
    var fast = head.Next
    var slow = head

    for fast.Next != nil && fast.Next.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next
    }

    slow.Next = slow.Next.Next

    return head
}