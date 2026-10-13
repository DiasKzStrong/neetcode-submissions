class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []

        for i in range(length):  
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            num = nums[i]  
        
            l , r = i+1, length - 1
            while l < r:
                num2, num3 = nums[l], nums[r]

                currSum = num + num2 + num3

                if currSum > 0:
                    r -= 1 
                elif currSum < 0:
                    l += 1
                elif currSum == 0:
                    res.append([num, num2, num3])
                    r -= 1
                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        

        return res