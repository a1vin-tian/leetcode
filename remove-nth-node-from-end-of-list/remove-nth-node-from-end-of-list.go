package remove_nth_node_from_end_of_list

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * https://leetcode.com/problems/remove-nth-node-from-end-of-list/
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	var dummy *ListNode = &ListNode{0, nil}
	dummy.Next = head
	var length int = 0
	var c = dummy
	for c != nil {
		c = c.Next
		length++
	}
	length = length - n
	c = dummy
	for ; length > 0; length-- {
		c = c.Next
	}
	c.Next = c.Next.Next
	return dummy.Next
}

