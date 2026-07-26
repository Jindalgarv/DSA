# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head1,head2=list1,list2
        curr=dummy
        while head1 and head2:
            if head1.val<head2.val:
                curr.next=head1
                head1=head1.next
            else:
                curr.next=head2
                head2=head2.next
            curr=curr.next
        while head1:
            curr.next=head1
            curr,head1=curr.next,head1.next
        while head2:
            curr.next=head2
            curr,head2=curr.next,head2.next
        return dummy.next
      
        