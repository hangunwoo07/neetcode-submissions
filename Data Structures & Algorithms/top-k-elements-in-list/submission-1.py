class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dic: Dict[int, int] = {}
        freq_list: List[List[int]] = [[] for i in range(0, len(nums) + 1)]

        for num in nums:
            if num not in freq_dic:
                freq_dic[num] = 1
            else:
                freq_dic[num] += 1
        
        for num in list(freq_dic.keys()):
            frequency = freq_dic[num]
            freq_list[frequency].append(num)
        
        result: List[int] = []

        for num_list in reversed(freq_list):
            for num in num_list:
                if num != 1001:
                    result.append(num)
            
            if len(result) == k:
                break
        
        return result