/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    var dum = &ListNode{Val:0, Next: nil}
    dum.Next = head
    var a = dum
    var b = dum

    for i := 0; i < n + 1; i++ {
        a = a.Next
    }

    for a != nil {
        b = b.Next
        a = a.Next
    }

    b.Next = b.Next.Next
    return dum.Next
}