https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/791/
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        successor = None
        
        if not root:
            return None
        
        while root:
            
            if p.val < root.val:
                
                successor = root
                
                root = root.left
                
            else:
                root = root.right
                
        
        return successor
            
