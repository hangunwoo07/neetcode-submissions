class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        is_duplicate: Dict[bool] = {}

        for num in nums:
            if num in is_duplicate:
                return True
            else:
                is_duplicate[num] = True
        
        return False