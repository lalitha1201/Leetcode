class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        max_sum = float('-inf')
        def gain(node):
            nonlocal max_sum
            if not node:
                return 0
            cur = node.val
            left = gain(node.left)
            right = gain(node.right)
            cur_gain = cur + left + right
            max_sum = max(max_sum, cur_gain)
            return max(0, cur + max(left, right))
            
        gain(root)
        return max_sum
        
