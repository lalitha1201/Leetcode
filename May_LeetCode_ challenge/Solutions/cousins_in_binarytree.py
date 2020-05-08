class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        x_info = []
        y_info = []
        depth = 0
        parent = None
        
        if not root:
            return False
        
        self.helper(x,y,root,x_info,y_info,0,None)
        
        return x_info[0][0] == y_info[0][0] and x_info[0][1] != y_info[0][1]
        
        
        
    def helper(self,x,y,root,x_info,y_info,depth,parent):
        
        if not root:
            
            return False
            
        if root.val == x:
                
            x_info.append((depth,parent))
                
            
        if root.val == y:
            y_info.append((depth,parent))
                
            
        self.helper(x,y,root.left,x_info,y_info,depth+1,root)
        self.helper(x,y,root.right,x_info,y_info,depth+1,root)
            
        
