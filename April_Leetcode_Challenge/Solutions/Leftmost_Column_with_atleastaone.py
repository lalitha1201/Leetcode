class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [n,m] = binaryMatrix.dimensions()
        x,y  = 0, m-1 
        x1 = y1 = 0
        ct = 0
        while x <= n-1 and y>=0:
            if binaryMatrix.get(x,y) == 1:
                x1, y1 = x, y
                y -= 1
                ct += 1
            else:
                x += 1
        if x1==0 and y1 ==0 and ct == 0:
            return -1
        else: return y1
