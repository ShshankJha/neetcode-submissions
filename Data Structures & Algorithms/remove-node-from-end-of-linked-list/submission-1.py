# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        head1 = head 
        dummy.next = head1 

        curr = head1
        dumcur = dummy  

        for _ in range(n):
            curr = curr.next
        
        while curr: 
            curr = curr.next 
            dumcur = dumcur.next 
        
        dumcur.next = dumcur.next.next

        return dummy.next


            

        