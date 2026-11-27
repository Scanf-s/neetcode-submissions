# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes: list[ListNode] = []
        cur: Optional[ListNode] = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        start: int = 1
        end: int = len(nodes) - 1
        cur: Optional[ListNode] = head
        while cur and start < end:
            cur.next = nodes[end]
            cur = cur.next
            cur.next = nodes[start]
            cur = cur.next
            start += 1
            end -= 1
            if start == end:
                cur.next = nodes[start]
                cur.next.next = None
                break
            elif start > end:
                cur.next = None
                break
