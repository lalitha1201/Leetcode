#https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/790/
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = [ ]
        
        while True:
            
            while root:
                stack.append(root)
                root = root.left
            
       
                
            root = stack.pop()
            k-=1
                
            if k == 0:
                return root.val
            root = root.right
            
                      
                
        

