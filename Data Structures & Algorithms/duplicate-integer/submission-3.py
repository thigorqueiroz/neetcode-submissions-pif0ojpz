class Solution:
    #brute force O(nˆ2) n-square solution
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for nextIndex in range(i + 1, len(nums)):
                if nums[i] == nums[nextIndex]:
                    return True
        return False

        