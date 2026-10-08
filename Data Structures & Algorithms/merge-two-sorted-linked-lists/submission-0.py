# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1curr = list1 
        l2curr = list2

        head = ListNode()
        rescurr = head

        while (l1curr is not None) or (l2curr is not None):
            if l1curr == None:
                rescurr.next = ListNode(l2curr.val)
                rescurr = rescurr.next
                l2curr= l2curr.next
                continue 

            if l2curr == None:
                rescurr.next = ListNode(l1curr.val)
                rescurr = rescurr.next 
                l1curr= l1curr.next
                continue 

            if l1curr.val > l2curr.val: 
                rescurr.next = ListNode(l2curr.val)
                rescurr = rescurr.next
                l2curr= l2curr.next

            else: 
                rescurr.next = ListNode(l1curr.val)
                rescurr = rescurr.next 
                l1curr= l1curr.next

        return head.next