# Definition for singly-linked list.
from hashlib import new
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        heap: list[int] = []
        cur1: Optional[ListNode] = list1
        cur2: Optional[ListNode] = list2
        while cur1:
            heapq.heappush(heap, cur1.val)
            cur1 = cur1.next
        while cur2:
            heapq.heappush(heap, cur2.val)
            cur2 = cur2.next
        
        new_head: Optional[ListNode] = None
        cur: Optional[ListNode] = None
        while heap:
            cur_val: int = heapq.heappop(heap)
            if not new_head:
                new_head = ListNode(val=cur_val, next=None)
                cur = new_head
            else:
                cur.next = ListNode(val=cur_val, next=None)
                cur = cur.next
        return new_head
