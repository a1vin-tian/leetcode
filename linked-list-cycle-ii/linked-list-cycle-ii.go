package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return nil
	}

	var f = head
	var s = head
	for {
		s = s.Next
		f = f.Next.Next
		if f == nil || f.Next == nil {
			return nil
		}
		if s == f {
			break
		}

	}
	s = head
	for s != f {
		s = s.Next
		f = f.Next
	}
	return s

}

func main() {
	var a = &ListNode{3, nil}
	var b = &ListNode{2, nil}
	var c = &ListNode{0, nil}
	var d = &ListNode{-4, nil}
	a.Next = b
	b.Next = c
	c.Next = d
	d.Next = b
	detectCycle(a)
}
