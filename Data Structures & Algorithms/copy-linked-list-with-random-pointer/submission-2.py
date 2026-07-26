"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
            
        curr = head
        node_idx = {}
        copied_nodes = []
        idx = 0
        while curr:
            node_idx[curr] = idx
            idx += 1
            node = Node(curr.val)
            copied_nodes.append(node)
            curr = curr.next

        curr = head
        random_idx = {}
        while curr:
            try: random_idx[curr] = node_idx[curr.random]
            except: random_idx[curr] = None
            curr = curr.next
        
        
        for i in range(len(copied_nodes)-1):
            node = copied_nodes[i]
            node.next = copied_nodes[i+1]
        
        for node, val in zip(copied_nodes, random_idx.values()):
            print(node, val)
            if val != None:
                node.random = copied_nodes[val]
            else:
                node.random = None

        return copied_nodes[0]

        