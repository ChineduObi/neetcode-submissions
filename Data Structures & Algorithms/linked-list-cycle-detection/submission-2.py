'''
Naive is to use a hash set and checking if the node was already viewed
Use fast and slow poitners to check when they meet'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        cur = head
        while cur:
            if cur in seen:
                return True

            seen.add(cur)
            cur = cur.next
        
        return False