class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dic: Dict[Tuple, list] = {}
        for string in strs:
            l: List[int] = [0]*26
            for char in string:
                l[ord(char) - ord('a')] += 1
            
            t = tuple(l)
            if t in ans_dic:
                ans_dic[t].append(string)
            else:
                ans_dic[t] = [string]
        
        return list(ans_dic.values())