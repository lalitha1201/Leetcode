https://leetcode.com/explore/featured/card/google/61/trees-and-graphs/3071/
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        left_depth = self.depth(root.left)
        
        right_depth = self.depth(root.right)
        
        if left_depth == right_depth:
            
            return pow(2,left_depth) + self.countNodes(root.right)
        
        else:
            
            return pow(2,right_depth) + self.countNodes(root.left)
        
    def depth(self,root):
        
        if not root:
            
            return 0
            
        return 1 + self.depth(root.left)    
            
            
        
