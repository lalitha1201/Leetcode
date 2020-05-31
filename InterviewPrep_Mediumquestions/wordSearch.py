https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/797/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        if not board and word:
            return False
        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    res = res or self.helper(board, word, i, j, 0)
                    if res:
                        return True
        return res
   
    
    def helper(self, board, word, i, j, index):

        if i < 0 or i > len(board) - 1 or j < 0 or j > len(board[0]) -1:
            return False
        if board[i][j] != word[index]:
            return False
        if index == len(word)-1:
            return True   
	    # could not be used for more than once
        char = board[i][j]
        board[i][j] = '*'
        found = self.helper(board, word, i-1, j, index +1) or self.helper(board, word, i+1, j, index +1) or self.helper(board, word, i, j+1, index +1) or self.helper(board, word, i, j-1, index +1) 
        board[i][j] = char
        return found
