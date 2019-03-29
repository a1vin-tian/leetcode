package middle_of_the_linked_list

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * https://leetcode.com/problems/middle-of-the-linked-list/
 * 时间: O(n)
 * 空间: O(1)
 */
func middleNode(head *ListNode) *ListNode {
	var f = head
	var s = head
	for f != nil && f.Next != nil {
		f = f.Next.Next
		s = s.Next
	}
	return s
}
