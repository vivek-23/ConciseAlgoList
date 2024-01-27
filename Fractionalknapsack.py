class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:
    def fractionalknapsack(self, W,arr,n):
        ans = 0
        ls = []
        for item in arr:
            ls.append([item.value / item.weight, item.weight])
        ls.sort(key=lambda x: -x[0])
        for wv in ls:
            if wv[1] <= W:
                ans += wv[0] * wv[1]
                W -= wv[1]
            else:
                ans += wv[0] * W
                break
        return ans
