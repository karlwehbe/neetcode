# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
       
        def traverse(root, curr_depth):
            if not root: 
                return curr_depth
            
            depth_left = traverse(root.left, curr_depth + 1)
            depth_right = traverse(root.right, curr_depth + 1)
            

            return max(depth_left, depth_right)
        

        max_depth = traverse(root, 0)
        return max_depth