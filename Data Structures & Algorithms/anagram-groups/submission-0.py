class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dic: Dict[Tuple, List[str]] = {}  # key: tuple with dictionary itmes, value: List[str]

        for string in strs:
            dic: Dict[int] = {}
            for char in string:
                if char in dic:
                    dic[char] += 1
                else:
                    dic[char] = 1

            t = tuple(sorted(dic.items()))

            if t in ans_dic:
                ans_dic[t].append(string)
            else:
                ans_dic[t] = [string]

        return list(ans_dic.values())
