# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        count = 0
        c = dummy.next
        h = dummy
        p = dummy

        while c:
            c = c.next
            count += 1
        c = dummy.next
        while k <= count:
            for i in range(k):
                n = c.next
                c.next = p
                p = c
                c = n
            n = h.next
            n.next = c
            h.next = p
            h = n
            count -= k

        return dummy.next


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    Solution().reverseKGroup(l1, 2)
