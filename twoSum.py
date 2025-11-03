class Solution:
    def twoSum(self,numbers:list[int],target:int)->list[int]:
        pair_idx = {}

        for i, num in enumerate(numbers):
            if(target - num in pair_idx):
                return [i,pair_idx[target - num]]
            
            pair_idx[num] = i

solution = Solution()
print(solution.twoSum([2,4,6,9,12,17,2],23))
