class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Solution using min-heap"""

        freq_dic: Dict[int, int] = {} # key: num, value: frequency

        for num in nums:
            if num not in freq_dic:
                freq_dic[num] = 1
            else:
                freq_dic[num] += 1
        
        heap = []

        for num in freq_dic.keys():
            heapq.heappush(heap, (freq_dic[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result