# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge2Lists(self,list1,list2):
        dummy=ListNode()
        head=dummy
        head1,head2=list1,list2
        while head1 and head2:
            if head1.val<=head2.val:
                head.next=head1
                head=head.next
                head1=head1.next
            else:
                head.next=head2
                head=head.next
                head2=head2.next
        while head1:
            head.next=head1
            head1,head=head1.next,head.next
        while head2:
            head.next= head2
            head2,head=head2.next,head.next
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged= None
        for node in lists:
            merged= self.merge2Lists(merged,node)
        return merged
        
        