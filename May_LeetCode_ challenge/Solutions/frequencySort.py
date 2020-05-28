class Solution:
    def frequencySort(self, s: str) -> str:
        
        # Hash Map with String Builder
        
        str_counter = collections.Counter(s)
        
        new_string = []
        
        for char,count in str_counter.most_common():
            
            new_string.append(count * char)
            
        
        return "".join(new_string)
        
