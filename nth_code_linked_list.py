#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        temp = ListNode(0, head)
        l = temp
        r = head

        while n > 0:
            r = r.next
            n -= 1
        
        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        return temp.next

s = Solution()
s.removeNthFromEnd(head = [1,2,3,4,5], n = 2)
