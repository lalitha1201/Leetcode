https://leetcode.com/explore/interview/card/top-interview-questions-easy/94/trees/555/
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        else:
            ldepth = self.maxDepth(root.left)
            
            rdepth = self.maxDepth(root.right)
            
        
        return max(ldepth,rdepth) + 1
            
            
