'''
RANGE SUM QUERY - MUTABLE

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
'''

class NumArray:
    def __init__(self, nums: List[int]):
        self.sqrt = int(math.floor(math.sqrt(len(nums))))
        self.blocks = [0 for _ in range(len(nums) // self.sqrt + 1)]
        self.nums = nums
        ssum = ptr = 0

        for i in range(len(self.nums)):
            if i > 0 and i % self.sqrt == 0:
                self.blocks[ptr] = ssum
                ptr += 1
                ssum = 0
            ssum += self.nums[i]
        
        self.blocks[ptr] = ssum

    def update(self, index: int, val: int) -> None:
        prevVal = self.nums[index]
        self.nums[index] = val
        blockIdx = index // self.sqrt
        self.blocks[blockIdx] += -prevVal + val

    def sumRange(self, left: int, right: int) -> int:
        startBlock = left // self.sqrt
        endBlock = right // self.sqrt
        ans = 0

        for i in range(startBlock + 1, endBlock):
            ans += self.blocks[i]

        if right - left < self.sqrt:
            for i in range(left, right + 1):
                ans += self.nums[i]
            
            return ans
        
        if startBlock * self.sqrt == left:
            ans += self.blocks[startBlock]
        else:
            for i in range(left, self.sqrt * (startBlock + 1)):
                ans += self.nums[i]

        if startBlock != endBlock:
            if (endBlock + 1) * self.sqrt == right:
                ans += self.blocks[endBlock]
            else:
                for i in range( self.sqrt * endBlock, right + 1):
                    ans += self.nums[i]
        
        return ans

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
