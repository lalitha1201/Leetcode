https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/625/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, minValue = float('-inf'), maxValue = float('inf')):
            
            if not node:
                return True
            
            if node.val <= minValue or node.val >= maxValue:
                return False
            
            return helper(node.left,minValue,node.val) and helper(node.right,node.val, maxValue)
        
        return helper(root)
