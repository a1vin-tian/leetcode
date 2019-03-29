package reverse_linked_list

type ListNode struct {
	Val  int
	Next *ListNode
}

/**
 * 可以用一个临时ListNode p ，将c.next 设置成 p 就实现转了
	时间： O(N)
	空间： O(1)
 */
func reverseList(head *ListNode) *ListNode {
	var p *ListNode = nil
	var c = head
	var n *ListNode
	for c != nil {
		n = c.Next
		c.Next = p
		p = c
		c = n
	}
	return p
}
