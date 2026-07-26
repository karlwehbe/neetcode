# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1, nums2 = [], []
        
        curr = l1
        while curr:
            nums1.append(curr.val)
            curr = curr.next
        nums1.reverse()

        curr = l2
        while curr:
            nums2.append(curr.val)
            curr = curr.next
        nums2.reverse()
        
        num1, num2 = "", ""
        for n1 in nums1:
            num1 += str(n1)
        for n2 in nums2:
            num2 += str(n2)

        res = int(num1) + int(num2)
        res = str(res)
        res = list(res.strip())
        res.reverse()

        nodes = []
        for i in range(len(res)):
            node = ListNode(res[i])
            nodes.append(node)
        
        for i in range(len(res)-1):
            nodes[i].next = nodes[i+1]
        
        return nodes[0]
