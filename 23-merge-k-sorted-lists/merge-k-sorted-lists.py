# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap,(lists[i].val,i,lists[i]))
        dummy=ListNode()
        tail=dummy
        while heap:
            val,i,node=heappop(heap)
            tail.next=node
            tail=tail.next
            node=node.next
            if node:
                heappush(heap,(node.val,i,node))
        return dummy.next