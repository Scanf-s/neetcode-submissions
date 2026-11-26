# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        cur1: Optional[ListNode] = list1
        cur2: Optional[ListNode] = list2
        new_head: Optional[ListNode] = None
        cur: Optional[ListNode] = None
        while cur1 and cur2:
            if cur1.val > cur2.val:
                if not new_head:
                    new_head = ListNode(val=cur2.val, next=None)
                    cur = new_head
                else:
                    cur.next = ListNode(val=cur2.val, next=None)
                    cur = cur.next
                cur2 = cur2.next
            else:
                if not new_head:
                    new_head = ListNode(val=cur1.val, next=None)
                    cur = new_head
                else:
                    cur.next = ListNode(val=cur1.val, next=None)
                    cur = cur.next
                cur1 = cur1.next
        while cur1:
            cur.next = ListNode(val=cur1.val, next=None)
            cur = cur.next
            cur1 = cur1.next
        while cur2:
            cur.next = ListNode(val=cur2.val, next=None)
            cur = cur.next
            cur2 = cur2.next
        return new_head
        
                    

