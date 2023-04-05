class Solution(object):
    def twoSum(self,nums,target):
        self.nums = nums
        self.target = target
        self.output = [""]
        for i in range(0,len(self.nums)):
            for j in range(0,len(self.nums)):
             if self.target == self.nums[i] + self.nums[j]:
                if i != j:
                    self.output = [i,j]
                    return (self.output)
    def displayOutput(self):
        print(self.output)    
nums = [3,3,4]
if len(nums) < 2:
    print("Invalid sets of data")

s = Solution()
s.twoSum(nums,6)
s.displayOutput()
