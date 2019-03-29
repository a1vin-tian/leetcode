package palindrome_linked_list

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

// https://leetcode.com/problems/palindrome-linked-list/
// 思路
// 1. 首先要确定前半段和后半段，所以采用两个指针，一个快指针，一个慢指针，
// 	  遍历的时候如果快指针为nil或者他的下一个为nil说明一半已经结束了，s则为后半段
// 2. 遍历的过程中，需要保存前半段的节点，可以用一个临时ListNode，保存的时候每次插入到前边，顺便实现逆序了。
// 3. 根据奇偶 将s做最后的移动，奇数的话需要把中间数字去除
// 4. 验证前半段和后半段是否一致

//
// 	时间： O(N)
//	空间： O(1)
func isPalindrome(head *ListNode) bool {
	var s *ListNode = head
	var f *ListNode = head
	var p *ListNode = nil
	for f != nil && f.Next != nil {
		f = f.Next.Next
		var n = s.Next
		s.Next = p
		p = s
		s = n
	}

	if f != nil {
		s = s.Next
	}
	for s != nil {
		if s.Val != p.Val {
			return false;
		}
		s = s.Next;
		p = p.Next;
	}
	return true
}
func main() {
	fmt.Print(isPalindrome(&ListNode{1, &ListNode{2, &ListNode{2, &ListNode{1, nil}}}}))
	fmt.Print(isPalindrome(&ListNode{1, &ListNode{2, &ListNode{3, &ListNode{2, &ListNode{1, nil}}}}}))
	fmt.Print(isPalindrome(&ListNode{1, &ListNode{2, nil}}))
	fmt.Print(isPalindrome(&ListNode{1, nil}))
}
