class Solution:
    def topoSort(self, V, edges):
        vis = [False] * V
        inDegree = [0] * V
        d = dict()
        
        for a,b in edges:
            inDegree[b] += 1
            d[a] = d.get(a, [])
            d[a].append(b)

        ans = []
        
        for i in range(V):
            if inDegree[i] == 0:
                self.dfs(i, inDegree, vis, d, ans)
        
        return ans
        
    def dfs(self, node, inDegree, vis, d, ans):
        if vis[node]:
            return
        
        inDegree[node] = max(0, inDegree[node] - 1)
        
        if inDegree[node] == 0:
            vis[node] = True
            ans.append(node)
        else:
            return
            
        for nei in d.get(node, []):
            self.dfs(nei, inDegree, vis, d, ans)
        
