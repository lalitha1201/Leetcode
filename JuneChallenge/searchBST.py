https://leetcode.com/problems/search-in-a-binary-search-tree/solution/
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None or root.val == val:
            return root
        
        return self.searchBST(root.left,val) if val < root.val else self.searchBST(root.right,val)
            
