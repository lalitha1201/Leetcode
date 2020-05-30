#https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/786/
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        
        if not root:
            
            return None
        
        array = []
        
        def helper(root,array):
            if root:
                
                helper(root.left,array)
                array.append(root.val)
                helper(root.right,array)
            
        helper(root,array)
        return array
