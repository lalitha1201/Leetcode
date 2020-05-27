class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        
        n = len(num)
        
        current = k
        
        for element in num:
            
            while stack and current and stack[-1] > element :
                
                stack.pop()
                
                current = current - 1
                
            stack.append(element)
        
        answer = "".join(stack[0 : n - k ]).lstrip("0")
        
        
        if len(answer):
            
            return answer
        
        else:
            
            return "0"
            
