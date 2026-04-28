class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numNeed: Dict[int] = {} # key: target - num, value: index

        for i in range(0, len(nums)):
            if nums[i] in numNeed:
                return [numNeed[nums[i]], i]
            else:
                numNeed[target - nums[i]] = i