package merge_two_sorted_lists

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * https://leetcode.com/problems/merge-two-sorted-lists/
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	var f *ListNode = &ListNode{0, nil}
	var c *ListNode = f
	for l1 != nil && l2 != nil {
		if l1.Val > l2.Val {
			c.Next = l2
			l2 = l2.Next
		} else {
			c.Next = l1
			l1 = l1.Next
		}
		c = c.Next
	}
	if l1 != nil {
		c.Next = l1
	}
	if l2 != nil {
		c.Next = l2
	}
	return f.Next
}
