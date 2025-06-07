class Solution:
    def getIdx(self, ch):
        return ord(ch) - 96
    
    def search(self, pat, txt):
        if len(pat) > len(txt):
            return []
            
        MOD = 10 ** 9 + 7
        BASE = 26
        pows = [1] * len(pat)
        txtHash = [1] * len(txt)
        
        for i in reversed(range(len(pat) - 1)):
            pows[i] = (pows[i + 1] * BASE) % MOD
            
        ans = []
        
        # hash values for the pattern string
        patHash = [1] * len(pat)
        for i in range(len(pat)):
            patHash[i] = ((patHash[i - 1] if i - 1 >= 0 else 0) + self.getIdx(pat[i]) * pows[i]) % MOD
        
        for i in range(len(txt)):
            if i < len(pat):
                txtHash[i] = ((txtHash[i - 1] if i - 1 >= 0 else 0) + self.getIdx(txt[i]) * pows[i]) % MOD
            else:
                # this last windows's first char will have contribution into the sum as BASE ^ (len(pat) - 1) times if you mathematically induce via formula expansion
                last_char_hash_contribution = self.getIdx(txt[i - len(pat)]) * pows[0] % MOD
                
                txtHash[i] = ((26 * (txtHash[i - 1] - last_char_hash_contribution)) + self.getIdx(txt[i])) % MOD
        
            if txtHash[i] == patHash[-1] and self.checkIfSame(pat, txt, i - len(pat) + 1):
                ans.append(i - len(pat) + 2)
                
        
        return ans
        
    
    def checkIfSame(self, pat, txt, x):
        for i in range(len(pat)):
            if pat[i] != txt[x + i]:
                return False
        
        return True
