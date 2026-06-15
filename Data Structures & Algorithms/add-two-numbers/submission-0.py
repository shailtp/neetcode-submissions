# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=l1
        carry=0

        while l1 and l2:
            result=l1.val+l2.val+carry
            carry=result//10
            l1.val=result%10
            prev=l1
            l1=l1.next
            l2=l2.next

        #check if remaining elements are in l1 or l2
        while l1:
            result=l1.val+carry
            carry=result//10
            l1.val=result%10

            prev=l1
            l1=l1.next
        
        while l2:
            prev.next=l2

            result=l2.val+carry
            carry=result//10
            l2.val=result%10

            l2=l2.next
            prev=prev.next

        if carry!=0:
                carryNode=ListNode()
                prev.next=carryNode
                carryNode.val=carry

        return dummy.next



            




        