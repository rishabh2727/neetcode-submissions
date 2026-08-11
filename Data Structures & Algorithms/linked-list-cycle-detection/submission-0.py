# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        mp = {}

        while curr:
            if curr in mp:
                return True
            else:
                mp[curr] = 1
            curr = curr.next

        print(mp)
        return False
        
        
        
        