# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp=head=ListNode()
        head1,head2=l1,l2
        a=0

        while head1 or head2:
            head.next=ListNode((head1.val+head2.val+a)%10)
            a=(head1.val+head2.val+a)//10
            head=head.next
            head1,head2=head1.next,head2.next
            if head1==None and head2!=None:
                head1=ListNode()
            elif head1!=None and head2==None:
                head2=ListNode()
        if a>0:
            head.next=ListNode(a)
            
        return temp.next
        
        