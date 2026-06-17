# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        carry=0

        while l1 and l2:
            result=l1.val+l2.val+carry
            l1.val=result%10
            carry=result//10

            curr.next=l1
            curr=l1
            l1=l1.next
            l2=l2.next

        while l1:
            result=l1.val+carry
            l1.val=result%10
            carry=result//10

            curr.next=l1
            curr=l1
            l1=l1.next

        while l2:
            result=l2.val+carry
            l2.val=result%10
            carry=result//10

            curr.next=l2
            curr=l2
            l2=l2.next

        if carry:
            carryNode=ListNode()
            curr.next=carryNode
            carryNode.val=carry

        return dummy.next


        

        