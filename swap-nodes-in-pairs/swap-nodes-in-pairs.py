# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return "%s n: %s" % (self.val, self.next)


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        c = dummy
        while c.next and c.next.next:
            a = c.next
            b = c.next.next
            a.next = b.next
            b.next = a
            c.next = b
            c = c.next.next

        return dummy.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
print(Solution().swapPairs(a))
