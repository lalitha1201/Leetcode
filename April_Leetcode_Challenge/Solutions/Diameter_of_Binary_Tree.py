class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        
        def helper(node):
            if not node:
                return 0
            L = helper(node.left)
            R = helper(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L,R) + 1
        
        helper(root)
        
        return self.ans -1 
        
