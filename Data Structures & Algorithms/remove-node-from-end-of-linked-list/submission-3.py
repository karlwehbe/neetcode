# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        if length == 1:
            return None

        prev, curr = None, head
        idx = length - n
        if idx == 0:
            return head.next

        while idx >= 0:   
            prev = curr     
            curr = curr.next
            if idx == 1:
                prev.next = curr.next
            
            idx -= 1
                
        return head 