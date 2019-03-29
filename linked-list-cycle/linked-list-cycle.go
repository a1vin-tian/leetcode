package linked_list_cycle

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * https://leetcode.com/problems/linked-list-cycle/
 */
func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}
	var f = head.Next
	var s = head
	for s != f {
		if f == nil || f.Next == nil {
			return false
		}
		s = s.Next
		f = f.Next.Next
	}
	return true
}
