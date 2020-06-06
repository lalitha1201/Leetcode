# https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3347/
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        
        if not root:
            
            return None
        
        root.left , root.right = self.invertTree(root.right) , self.invertTree(root.left)
        
        return root
            
            
            
