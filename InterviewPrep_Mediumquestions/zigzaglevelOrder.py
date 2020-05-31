https://leetcode.com/explore/interview/card/top-interview-questions-medium/108/trees-and-graphs/787/
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
        res = collections.defaultdict(collections.deque)
        
        def helper(root,level,res):
            if not root:
                return None
            if level % 2 == 0:
                res[level].append(root.val)
            else:
                res[level].appendleft(root.val)
                
            helper(root.left,level+1,res)
            helper(root.right,level+1,res)
        
        helper(root,0,res)
        return res.values()
                
