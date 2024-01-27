from random import randint

class Solution:
    def quickSort(self,arr,low,high):
        if low >= high: return
        pivot = self.partition(arr, low, high)
        self.quickSort(arr, low, pivot - 1)
        self.quickSort(arr, pivot + 1, high)
        
    def partition(self,arr,low,high):
        pivotIdx = randint(low, high)
        pivotEle = arr[pivotIdx]
        #print(low, high, pivotEle)
        i = low
        idx = low - 1
        while i <= high:
            if arr[i] < pivotEle:
                idx += 1
                arr[idx], arr[i] = arr[i], arr[idx]
            i += 1
        for i in range(idx + 1, high + 1):
            if arr[i] == pivotEle:
                arr[idx + 1], arr[i] = arr[i], arr[idx + 1]
                break
        return idx + 1 
