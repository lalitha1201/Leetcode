class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        
        def helper(root):
            
            if not root:
                return None
            
            if root.left:
                
                if root.next:
                    
                    root.right.next = root.next.left
                
                root.left.next = root.right
                
            
            helper(root.left)
            helper(root.right)
            
        helper(root)
            
        
        return root
