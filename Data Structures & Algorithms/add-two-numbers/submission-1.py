# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        currl1 = l1 
        currl2 = l2 

        l1num = 0 
        i = 0 
        while currl1 is not None: 
            l1num += (currl1.val * 10**i) 
            i += 1 
            currl1 = currl1.next 
        
        l2num = 0
        x = 0 
        while currl2 is not None: 
            l1num += (currl2.val * 10**x) 
            x += 1 
            currl2 = currl2.next 
        
        result = "".join(reversed(str(l1num + l2num)))

        head = ListNode(result[0])
        current = head 

        for i in range(1,len(result)):
            current.next = ListNode(int(result[i]))
            current = current.next 

        return head 


        