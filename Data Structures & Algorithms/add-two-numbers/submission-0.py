# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = [], []
        
        curr = l1
        while curr:
            n1.append(curr.val)
            curr = curr.next
        n1.reverse()

        curr = l2
        while curr:
            n2.append(curr.val)
            curr = curr.next
        n2.reverse()
        
        num1 = ""
        for n in n1:
            num1 += str(n)
        print(num1)

        num2 = ""
        for n in n2:
            num2 += str(n)
        print(num2)

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
