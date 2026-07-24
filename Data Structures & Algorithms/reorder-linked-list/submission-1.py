# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:        
        curr_node = head
        
        stack = []
        length = 0
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.next
            length += 1
        

        backwards = length // 2
        stack = stack[length-backwards:]

        curr_node = head
        dummy = ListNode()
        while len(stack) > 0:
            dummy = curr_node.next
            curr_node.next = stack.pop()
            curr_node = curr_node.next # 10 
            curr_node.next = dummy # 4
            curr_node = curr_node.next # 6
        
        curr_node.next = None