class Trie:

    def __init__(self):
        self.root = {} # TrieNode: is dict, or hashmap       
 
    def insert(self, word):
        p = self.root
        for c in word:            
            if c not in p: 
                p[c] = {}
            p = p[c]
        p['#'] = True  # ‘#’ is a key indicating word bounday
 
    def search(self, word):
        node = self.find(word)
        return node is not None and '#' in node        
 
    def startsWith(self, prefix):
        return self.find(prefix) is not None
    
    def find(self, prefix):
        p = self.root
        for c in prefix:            
            if c not in p: return None
            p = p[c]
        return p
