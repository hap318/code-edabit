# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Total = 0
        l2Total = 0
        count = 0
        while l1:
              l1Total += (l1.val * pow(10,count))
              l1 = l1.next
              count += 1
        count = 0
        while l2:
                l2Total += (l2.val * pow(10,count))
                l2 = l2.next
                count += 1
        total = l1Total + l2Total
        print(total)
        new = []
        for i in str(total):
            new.insert(0,int(i))
        print(new)

