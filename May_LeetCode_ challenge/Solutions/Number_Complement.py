class Solution:
    def findComplement(self, num: int) -> int:
        
        # convert decimal to binary using bin function and consider numbers from second index
        
        # In the final step complement it and change it to decimal
        
        return int(''.join('1' if x == '0' else '0' for x in bin(num)[2:]),2)
