# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        left_boundary = float("-inf")
        right_boundary = float("inf")

        def traverse(node: Optional[TreeNode], left: int, right: int) -> bool :
            if not node:
                return True

            if not (node.val < right and node.val > left):
                return False
            
            res1 = traverse(node.left, left, node.val)
            res2 = traverse(node.right, node.val, right)

            return (res1 and res2)
        

        return traverse(root, left_boundary, right_boundary)