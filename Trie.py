class TrieNode:      
    def __init__(self): 
        self.children = [None] * 26      
        self.isEndOfWord = False

class Solution:
    def insert(self, root, key):
        temp = root
        for i in range(len(key)):
            if temp.children[ord(key[i]) - 97] == None:
                temp.children[ord(key[i]) - 97] = TrieNode()
            temp = temp.children[ord(key[i]) - 97]
        temp.isEndOfWord = True
    def search(self, root, key):
        temp = root
        for i in range(len(key)):
            if temp.children[ord(key[i]) - 97] == None:
                return False
            temp = temp.children[ord(key[i]) - 97]
        return temp.isEndOfWord
