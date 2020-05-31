https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/788/
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if inorder:
            rootVal = preorder[0]
            i = inorder.index(rootVal)
            root = TreeNode(rootVal)
            root.left = self.buildTree(preorder[1:i+1], inorder[0:i])
            root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
            return root
        
