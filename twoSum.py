class Solution:
    def twoSum(self, nums:list[int],target:int)->list[int]:

        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i,pair_idx[target - num]]
            
            pair_idx[num] = i

solution = Solution()

print(solution.twoSum([2,7,11,15],9))