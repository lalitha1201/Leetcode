class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        count_ransomnote = collections.Counter(ransomNote)
        
        count_magazine = collections.Counter(magazine)
            
        
        for char,count in count_ransomnote.items():
            
            magazine_count = count_magazine[char]
            
            if magazine_count < count:
                
                return False
        
        return True
        
